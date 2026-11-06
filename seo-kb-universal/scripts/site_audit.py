#!/usr/bin/env python3
"""對一個或多個 URL 做可自動化的技術 SEO 稽核，對照 seo-knowledge-base 的規範輸出結果。

用法：
  site_audit.py <url> [url...] [--json out.json] [--no-extra] [--hreflang-check] [--timeout 20]
輸出：Markdown 表（項目｜結果｜說明｜章節），--json 另存結構化結果給 report.py 用。
結果代碼：pass 通過 / fail 未通過 / warn 需注意 / manual 無法自動判定（要人工或 GSC）
只用 Python 標準庫，不需安裝套件。數值門檻依 00-快速啟動指南 §4。
"""
import sys, re, json, argparse, time, html as htmlmod
from urllib import request, error, parse
from html.parser import HTMLParser

UA = "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Mobile Safari/537.36 seo-kb-universal-audit"
TIMEOUT = 20

class Redir(request.HTTPRedirectHandler):
    def __init__(self): self.chain = []
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        self.chain.append((req.full_url, code, newurl))
        return super().redirect_request(req, fp, code, msg, headers, newurl)

def fetch(url, method="GET", maxbytes=3_000_000):
    rh = Redir()
    opener = request.build_opener(rh)
    req = request.Request(url, headers={"User-Agent": UA, "Accept-Language": "en"}, method=method)
    t0 = time.time()
    try:
        with opener.open(req, timeout=TIMEOUT) as r:
            body = r.read(maxbytes) if method == "GET" else b""
            return {"ok": True, "status": r.status, "url": r.geturl(), "headers": dict(r.headers), "body": body,
                    "chain": rh.chain, "ms": int((time.time() - t0) * 1000)}
    except error.HTTPError as e:
        return {"ok": False, "status": e.code, "url": e.geturl() if hasattr(e, "geturl") else url, "headers": dict(e.headers or {}),
                "body": b"", "chain": rh.chain, "ms": int((time.time() - t0) * 1000)}
    except Exception as e:
        return {"ok": False, "status": None, "url": url, "headers": {}, "body": b"", "chain": rh.chain, "err": str(e), "ms": 0}

class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title = ""; self.in_title = False; self.metas = []; self.links = []; self.h1 = []; self.in_h1 = False
        self.jsonld = []; self.in_ld = False; self.scripts = []; self.imgs = []; self.lang = None; self.text = []
        self.skip = 0; self.in_body = False; self.anchors = 0; self.iframes = 0
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "html": self.lang = a.get("lang")
        elif tag == "title": self.in_title = True
        elif tag == "meta": self.metas.append(a)
        elif tag == "link": self.links.append(a)
        elif tag == "h1": self.in_h1 = True; self.h1.append("")
        elif tag == "script":
            if (a.get("type") or "").lower() == "application/ld+json": self.in_ld = True; self.jsonld.append("")
            else: self.scripts.append(a); self.skip += 1
        elif tag in ("style", "noscript", "svg"): self.skip += 1
        elif tag == "img": self.imgs.append(a)
        elif tag == "body": self.in_body = True
        elif tag == "a": self.anchors += 1
        elif tag == "iframe": self.iframes += 1
    def handle_endtag(self, tag):
        if tag == "title": self.in_title = False
        elif tag == "h1": self.in_h1 = False
        elif tag == "script":
            if self.in_ld: self.in_ld = False
            elif self.skip: self.skip -= 1
        elif tag in ("style", "noscript", "svg") and self.skip: self.skip -= 1
    def handle_data(self, d):
        if self.in_title: self.title += d
        if self.in_h1 and self.h1: self.h1[-1] += d
        if self.in_ld: self.jsonld[-1] += d
        elif self.in_body and not self.skip and not self.in_title: self.text.append(d)

SCRIPTS = [("Han", 0x4E00, 0x9FFF), ("Thai", 0x0E00, 0x0E7F), ("Bengali", 0x0980, 0x09FF), ("Devanagari", 0x0900, 0x097F),
           ("Sinhala", 0x0D80, 0x0DFF), ("Tamil", 0x0B80, 0x0BFF), ("Arabic", 0x0600, 0x06FF), ("Cyrillic", 0x0400, 0x04FF),
           ("Hangul", 0xAC00, 0xD7AF), ("Kana", 0x3040, 0x30FF), ("Khmer", 0x1780, 0x17FF), ("Myanmar", 0x1000, 0x109F), ("Lao", 0x0E80, 0x0EFF)]
ADSENSE_NOTE = {"Latin": "manual|拉丁字母：英文、Filipino、越南、印尼、馬來皆支援；Cebuano、Ilocano 不支援，需人工判斷主要語言",
    "Han": "pass|中文（繁 / 簡）支援", "Thai": "pass|Thai 支援", "Bengali": "pass|Bengali (Bangla) 支援", "Tamil": "pass|Tamil 支援",
    "Devanagari": "manual|天城文：Hindi、Marathi 支援，Nepali 不支援，需人工判斷", "Sinhala": "fail|Sinhala 不在 AdSense 支援清單",
    "Khmer": "fail|Khmer 不支援", "Myanmar": "fail|Burmese 不支援", "Lao": "fail|Lao 不支援", "Arabic": "pass|Arabic 支援",
    "Cyrillic": "pass|俄文等支援", "Hangul": "pass|Korean 支援", "Kana": "pass|Japanese 支援"}

def detect_script(text):
    cnt = {}
    for ch in text:
        o = ord(ch)
        if ch.isascii():
            if ch.isalpha(): cnt["Latin"] = cnt.get("Latin", 0) + 1
            continue
        for name, lo, hi in SCRIPTS:
            if lo <= o <= hi: cnt[name] = cnt.get(name, 0) + 1; break
    total = sum(cnt.values()) or 1
    top = sorted(cnt.items(), key=lambda x: -x[1])
    return top, total

def vis_len(s):
    """標題長度：全形字算 2、半形算 1（對照 00 §4：英文 50–60 字元 / 中文 25–32 全形字）"""
    return sum(2 if ord(c) > 0x2E7F else 1 for c in s.strip())

def add(res, cid, name, status, detail, ref, sev="P2"):
    res.append({"id": cid, "name": name, "status": status, "detail": detail, "ref": ref, "severity": sev})

def audit(url, extra=True, hreflang_check=False):
    res = []; info = {"url": url}
    r = fetch(url)
    info["final_url"] = r["url"]; info["status"] = r["status"]; info["ms"] = r["ms"]; info["bytes"] = len(r["body"])
    if not r["ok"] or r["status"] != 200:
        add(res, "fetch", "頁面可存取", "fail", f"HTTP {r['status']} {r.get('err','')}", "04 §7", "P1"); return res, info
    add(res, "fetch", "頁面可存取", "pass", f"HTTP 200，{r['ms']} ms，HTML {len(r['body'])//1024} KB", "04 §7")
    hops = len(r["chain"])
    if hops == 0: add(res, "redirect", "無轉址鏈", "pass", "直接 200", "04 §7")
    elif hops <= 2: add(res, "redirect", "轉址跳數", "warn", f"{hops} 跳：" + " → ".join(f"{c[1]}" for c in r["chain"]) + f" → {r['url']}", "04 §7")
    else: add(res, "redirect", "轉址跳數", "fail", f"{hops} 跳（規範 ≤ 2）", "04 §7", "P2")
    fu = parse.urlsplit(r["url"])
    local = fu.hostname in ("localhost", "127.0.0.1", "::1") or (fu.hostname or "").endswith((".localhost", ".test", ".local"))
    info["local"] = local
    h = {k.lower(): v for k, v in r["headers"].items()}
    if local:
        add(res, "https", "HTTPS / HSTS / 安全標頭 / www 版本", "manual", "本機預覽環境，這些由正式主機與 CDN 決定，上線後再測", "04 §10、15 §12")
    else:
        add(res, "https", "HTTPS", "pass" if fu.scheme == "https" else "fail", r["url"], "04 §10", "P1")
        add(res, "hsts", "HSTS 標頭", "pass" if "strict-transport-security" in h else "warn", h.get("strict-transport-security", "缺少"), "15 §12", "P3")
        add(res, "xcto", "X-Content-Type-Options", "pass" if "x-content-type-options" in h else "warn", h.get("x-content-type-options", "缺少"), "15 §12", "P3")
    xr = h.get("x-robots-tag", "")
    if "noindex" in xr.lower(): add(res, "xrobots", "X-Robots-Tag", "fail", xr, "04 §3", "P1")
    if r["ms"] > 800: add(res, "ttfb", "回應時間（含下載，近似 TTFB）", "warn", f"{r['ms']} ms（建議 TTFB ≤ 800 ms，正式值用 WebPageTest 目標市場節點）", "04 §12", "P3")
    else: add(res, "ttfb", "回應時間（含下載，近似 TTFB）", "pass", f"{r['ms']} ms", "04 §12")
    if len(r["body"]) > 1_000_000: add(res, "htmlsize", "HTML 大小", "warn", f"{len(r['body'])//1024} KB，低階手機與小流量方案建議首屏總重 < 1–2 MB", "04 §11", "P3")

    body = r["body"].decode("utf-8", "replace")
    p = P()
    try: p.feed(body)
    except Exception as e: add(res, "parse", "HTML 解析", "warn", f"解析例外：{e}", "04 §9")
    metas = {}
    for m in p.metas:
        k = (m.get("name") or m.get("property") or m.get("http-equiv") or "").lower()
        if k: metas.setdefault(k, m.get("content", ""))
    # title / meta
    t = htmlmod.unescape(p.title).strip(); tl = vis_len(t)
    if not t: add(res, "title", "Title", "fail", "缺少", "05 §1", "P1")
    elif tl > 64: add(res, "title", "Title 長度", "warn", f"{tl} 半形單位（英文 50–60 字元 / 中文 25–32 全形字；手機約前 40 字最重要）：{t[:80]}", "05 §1")
    else: add(res, "title", "Title", "pass", f"{tl} 半形單位：{t[:80]}", "05 §1")
    d = metas.get("description", ""); dl = vis_len(d)
    if not d: add(res, "desc", "Meta description", "warn", "缺少（Google 常改寫，但不可空白）", "05 §2")
    elif dl > 170: add(res, "desc", "Meta description 長度", "warn", f"{dl} 半形單位（英文 150–160 / 中文 70–80 全形）", "05 §2", "P3")
    else: add(res, "desc", "Meta description", "pass", f"{dl} 半形單位", "05 §2")
    h1s = [htmlmod.unescape(x).strip() for x in p.h1]
    if len(h1s) == 0: add(res, "h1", "H1", "fail", "缺少", "05 §3", "P2")
    elif len(h1s) > 1: add(res, "h1", "H1", "warn", f"{len(h1s)} 個（建議單一 H1，多個不違規）：{h1s[:3]}", "05 §3", "P3")
    else: add(res, "h1", "H1", "pass", h1s[0][:80], "05 §3")
    # robots meta
    rb = (metas.get("robots", "") + " " + metas.get("googlebot", "")).lower()
    if "noindex" in rb: add(res, "noindex", "meta robots", "fail", f"含 noindex：{rb.strip()}", "04 §3", "P1")
    else: add(res, "noindex", "meta robots", "pass", rb.strip() or "未設定（預設可索引）", "04 §3")
    if "max-image-preview:large" in rb.replace(" ", ""): add(res, "imgprev", "max-image-preview:large（Discover 大圖）", "pass", "已設定", "20 §20.7")
    else: add(res, "imgprev", "max-image-preview:large（Discover 大圖）", "warn", "未設定；要吃 Discover 流量需設定並用 ≥ 1200px 圖", "20 §20.7", "P3")
    add(res, "viewport", "viewport", "pass" if "viewport" in metas else "fail", metas.get("viewport", "缺少"), "04 §9", "P2")
    # canonical
    canon = [l.get("href") for l in p.links if (l.get("rel") or "").lower() == "canonical"]
    if not canon: add(res, "canonical", "canonical", "warn", "缺少自我參照 canonical", "04 §5", "P2")
    else:
        c = parse.urljoin(r["url"], canon[0]); same = c.rstrip("/") == r["url"].rstrip("/")
        if not c.startswith("http"): add(res, "canonical", "canonical", "fail", f"非絕對網址：{canon[0]}", "04 §5", "P2")
        elif len(canon) > 1: add(res, "canonical", "canonical", "fail", f"多個 canonical：{canon}", "04 §5", "P1")
        elif same: add(res, "canonical", "canonical", "pass", "自我參照", "04 §5")
        elif local and parse.urlsplit(c).path.rstrip("/") == fu.path.rstrip("/"): add(res, "canonical", "canonical", "pass", f"指向正式網域同路徑：{c}（本機預覽正常）", "04 §5"); info["prod_base"] = f"{parse.urlsplit(c).scheme}://{parse.urlsplit(c).netloc}"
        else: add(res, "canonical", "canonical", "warn", f"指向別處：{c}（若本頁是重複版本則正確）", "04 §5")
    # lang / hreflang
    add(res, "lang", "html lang", "pass" if p.lang else "warn", p.lang or "缺少（Google 不看 lang，但 Bing 與輔助工具會）", "10 §2", "P3")
    hl = [(l.get("hreflang"), parse.urljoin(r["url"], l.get("href", ""))) for l in p.links if (l.get("rel") or "").lower() == "alternate" and l.get("hreflang")]
    info["hreflang"] = hl
    if hl:
        codes = [c for c, _ in hl]; selfref = any(u.rstrip("/") == r["url"].rstrip("/") for _, u in hl)
        bad = [c for c in codes if not re.match(r"^(x-default|[a-z]{2,3}(-[A-Za-z]{2}|-[A-Za-z]{4})?)$", c) or c.lower().endswith("-uk") or c.lower() == "es-419"]
        msgs = [f"{len(hl)} 組"]
        if "x-default" not in codes: msgs.append("缺 x-default")
        if not selfref: msgs.append("缺自指")
        if bad: msgs.append(f"語言碼可疑：{bad}")
        st = "pass" if len(msgs) == 1 else "warn"
        add(res, "hreflang", "hreflang", st, "；".join(msgs), "10 §2", "P2")
        if hreflang_check:
            miss = []
            for c, u in hl[:10]:
                if u.rstrip("/") == r["url"].rstrip("/"): continue
                rr = fetch(u)
                if not rr["ok"]: miss.append(f"{c}: HTTP {rr['status']}"); continue
                if r["url"].rstrip("/") not in rr["body"].decode("utf-8", "replace"): miss.append(f"{c}: 無回傳標記")
            add(res, "hreflang_rt", "hreflang 雙向回傳", "pass" if not miss else "fail", "；".join(miss) or "抽查的版本皆互指", "10 §2", "P2")
    else: add(res, "hreflang", "hreflang", "manual", "無（單語站正常；多語站必須有）", "10 §2")
    # JSON-LD
    types = []
    for blk in p.jsonld:
        try:
            j = json.loads(blk.strip())
            items = j if isinstance(j, list) else [j]
            for it in items:
                if isinstance(it, dict):
                    if "@graph" in it: items.extend([g for g in it["@graph"] if isinstance(g, dict)])
                    tt = it.get("@type");
                    if tt: types.append(tt if isinstance(tt, str) else "/".join(map(str, tt)))
        except Exception: types.append("（JSON 解析失敗）")
    if not p.jsonld: add(res, "jsonld", "結構化資料（JSON-LD）", "warn", "無；內容站至少 Article / Organization / Person", "06 §2", "P3")
    elif "（JSON 解析失敗）" in types: add(res, "jsonld", "結構化資料（JSON-LD）", "fail", f"有語法錯誤：{types}", "06 §6", "P2")
    else:
        st = "warn" if any(t in ("FAQPage", "HowTo") for t in types) else "pass"
        add(res, "jsonld", "結構化資料（JSON-LD）", st, ", ".join(types) + ("（FAQ / HowTo rich result 已退場，確認仍有用途）" if st == "warn" else "") + "；語法與必要屬性用 Rich Results Test 驗證", "06 §2、§5")
    # images
    imgs = p.imgs; noalt = sum(1 for i in imgs if "alt" not in i); deco = sum(1 for i in imgs if "alt" in i and not (i.get("alt") or "").strip())
    nodim = sum(1 for i in imgs if not (i.get("width") and i.get("height")))
    def big(i):
        try: return int(re.sub(r"\D", "", i.get("width") or "0") or 0) >= 300
        except Exception: return True
    lazy_first = bool(imgs) and (imgs[0].get("loading") or "").lower() == "lazy" and (("width" not in imgs[0]) or big(imgs[0]))
    msg = f"{len(imgs)} 張；缺 alt 屬性 {noalt}（另有 {deco} 張 alt=\"\" 裝飾圖，需確認非內容圖）；缺 width/height {nodim}" + ("；首張大圖 lazy-load（LCP 圖不應延遲）" if lazy_first else "")
    add(res, "images", "圖片 alt 與尺寸屬性", "pass" if (noalt == 0 and nodim == 0 and not lazy_first) else "warn", msg, "04 §12、05 §5", "P3")
    ogimg = metas.get("og:image", "")
    add(res, "ogimage", "og:image（社群與 Discover 預覽）", "pass" if ogimg else "warn", ogimg[:100] or "缺少", "20 §20.7", "P3")
    # scripts / ads / analytics
    srcs = [s.get("src", "") for s in p.scripts if s.get("src")]
    ext = [s for s in srcs if s.startswith("http") and fu.netloc not in s]
    add(res, "scripts", "外部 script 數", "pass" if len(ext) <= 8 else "warn", f"{len(ext)} 個外部 / {len(p.scripts)} 個 script（低階機市場建議減少第三方）", "04 §11")
    ads = any("adsbygoogle" in s or "pagead2" in s for s in srcs) or "adsbygoogle" in body
    pub = re.search(r"ca-pub-\d{10,}", body)
    info["adsense_pub"] = pub.group(0) if pub else None
    add(res, "adsense", "AdSense 程式碼", "pass" if ads else "manual", (pub.group(0) if pub else "有 adsbygoogle") if ads else "未偵測到（未變現或用其他聯播網）", "22 §3")
    ga = "gtag(" in body or "googletagmanager.com" in body or "G-" in body and "gtag" in body
    add(res, "ga4", "GA4 / GTM", "pass" if ga else "warn", "已偵測" if ga else "未偵測到", "13 §13.2", "P3")
    # language detection vs AdSense
    text = " ".join(p.text); text = re.sub(r"\s+", " ", text)
    info["text_chars"] = len(text)
    top, total = detect_script(text)
    if top:
        main, n = top[0]; share = n / total
        st, note = ADSENSE_NOTE.get(main, "manual|未知文字系統").split("|", 1)
        mix = ", ".join(f"{k} {v/total:.0%}" for k, v in top[:3])
        add(res, "language", "主要文字系統 vs AdSense 支援語言", st, f"{mix}；{note}" + ("；混語比例高，Google 依可見內文判定主要語言，建議主要語言 ≥ 80%" if share < 0.75 else ""), "22 §1.1、10 §6", "P1" if st == "fail" else "P2")
    add(res, "textlen", "可見文字量", "pass" if len(text) >= 600 else "warn", f"約 {len(text)} 字元（含導覽；< 600 可能被視為薄內容）", "05 §9", "P3")
    info["title"] = t; info["h1"] = h1s; info["jsonld_types"] = types; info["lang"] = p.lang
    if not extra: return res, info
    # robots.txt
    base = f"{fu.scheme}://{fu.netloc}"
    rb = fetch(base + "/robots.txt")
    sitemaps = []
    if rb["ok"] and rb["status"] == 200:
        txt = rb["body"].decode("utf-8", "replace")
        sitemaps = re.findall(r"(?im)^sitemap:\s*(\S+)", txt)
        block_all = re.search(r"(?is)user-agent:\s*\*\s*(?:\n[^\n]*)*?\ndisallow:\s*/\s*$", txt, re.M) is not None
        blocks_assets = re.search(r"(?im)^disallow:\s*/(wp-includes|wp-content|assets|static|css|js)\b", txt) is not None
        st = "fail" if block_all else ("warn" if blocks_assets else "pass")
        add(res, "robots", "robots.txt", st, ("封鎖整站" if block_all else "") + ("；封鎖 CSS/JS 目錄（Googlebot 需渲染）" if blocks_assets else "") + f"；Sitemap 指令 {len(sitemaps)} 條" + (f"；{len(txt)//1024} KB" if len(txt) > 400_000 else ""), "04 §2", "P1" if block_all else "P3")
    else: add(res, "robots", "robots.txt", "warn", f"HTTP {rb['status']}（缺少時 Google 視為全部可抓，但 5xx 會停抓）", "04 §2", "P2")
    sm_url = sitemaps[0] if sitemaps else base + "/sitemap.xml"
    if local and info.get("prod_base") and sm_url.startswith(info["prod_base"]): sm_url = base + sm_url[len(info["prod_base"]):]
    if not local or True:
        pass
    sm = fetch(sm_url)
    if sm["ok"] and sm["status"] == 200:
        x = sm["body"].decode("utf-8", "replace"); locs = len(re.findall(r"<loc>", x)); idx = "<sitemapindex" in x
        add(res, "sitemap", "XML sitemap", "pass" if locs else "warn", f"{sm_url}：{'索引檔' if idx else '一般檔'}，{locs} 個 <loc>" + ("（> 50,000 需分檔）" if locs > 50000 else ""), "04 §4")
        # 抽查 sitemap 內的 URL 是否 noindex（14 §A：sitemap 只含可索引 URL）
        child = x
        if idx:
            subs = re.findall(r"<loc>([^<]+)</loc>", x)[:1]
            if subs:
                su = subs[0]
                if local and info.get("prod_base") and su.startswith(info["prod_base"]): su = base + su[len(info["prod_base"]):]
                sr = fetch(su); child = sr["body"].decode("utf-8", "replace") if sr["ok"] else ""
        urls = re.findall(r"<loc>([^<]+)</loc>", child)
        import random; random.seed(7); sample = random.sample(urls, min(20, len(urls))) if urls else []
        bad = []
        for su in sample:
            if local and info.get("prod_base") and su.startswith(info["prod_base"]): su = base + su[len(info["prod_base"]):]
            sr = fetch(su)
            if not sr["ok"] or sr["status"] != 200: bad.append(f"{su} HTTP {sr['status']}"); continue
            if re.search(r'<meta[^>]+name=["\']robots["\'][^>]+noindex', sr["body"].decode("utf-8", "replace"), re.I): bad.append(f"{su} noindex")
        if sample:
            add(res, "sitemap_noindex", "sitemap 抽查：URL 皆 200 且可索引", "pass" if not bad else "fail", f"抽 {len(sample)} 筆；問題 {len(bad)}：" + "；".join(bad[:5]) if bad else f"抽 {len(sample)} 筆皆正常", "04 §4、14 §A", "P2")
    else: add(res, "sitemap", "XML sitemap", "warn", f"{sm_url} HTTP {sm['status']}", "04 §4", "P2")
    # ads.txt
    at = fetch(base + "/ads.txt")
    if at["ok"] and at["status"] == 200 and b"google.com" in at["body"]:
        ok = (not pub) or (pub.group(0).replace("ca-", "").encode() in at["body"])
        add(res, "adstxt", "ads.txt", "pass" if ok else "fail", "含 google.com 行" + ("" if ok else f"，但不含本頁的 {pub.group(0)}"), "22 §2.7", "P2")
    elif ads: add(res, "adstxt", "ads.txt", "fail", f"HTTP {at['status']} 或無 google.com 行（AdSense 會顯示 Earnings at risk）", "22 §2.7", "P1")
    else: add(res, "adstxt", "ads.txt", "manual", "未變現站可略", "22 §2.7")
    # 404
    nf = fetch(base + "/seo-kb-universal-this-page-should-not-exist-404-check")
    add(res, "soft404", "不存在頁回 404", "pass" if nf["status"] in (404, 410) else "fail", f"HTTP {nf['status']}（200 即 soft 404）", "04 §7、12 A4", "P2")
    # http → https, www variants
    if fu.scheme == "https" and not local:
        hv = fetch("http://" + fu.netloc + fu.path, method="HEAD")
        add(res, "http2https", "HTTP → HTTPS 轉址", "pass" if hv["url"].startswith("https://") else "fail", f"最終 {hv['url']}", "04 §10", "P1")
    if local: return res, info
    alt_host = fu.netloc[4:] if fu.netloc.startswith("www.") else "www." + fu.netloc
    av = fetch(f"{fu.scheme}://{alt_host}{fu.path}", method="HEAD")
    if av["status"] is None: add(res, "wwwvariant", "www / 非 www 單一版本", "warn", f"{alt_host} 無法連線（DNS 未設定也算只有一版，但建議 301）", "04 §5", "P3")
    else: add(res, "wwwvariant", "www / 非 www 單一版本", "pass" if parse.urlsplit(av["url"]).netloc == fu.netloc else "fail", f"{alt_host} → {av['url']}", "04 §5", "P2")
    return res, info

SYM = {"pass": "✅ 通過", "fail": "❌ 未通過", "warn": "⚠️ 注意", "manual": "👤 人工判定"}
def to_md(url, res, info):
    out = [f"## 稽核：{url}", "", f"最終網址 {info.get('final_url')}；HTTP {info.get('status')}；{info.get('ms')} ms；主要語言偵測與結構化資料見表。", "",
           "| 項目 | 結果 | 說明 | 嚴重度 | 章節 |", "|---|---|---|---|---|"]
    order = {"fail": 0, "warn": 1, "manual": 2, "pass": 3}
    for c in sorted(res, key=lambda c: (order[c["status"]], c["severity"])):
        out.append(f"| {c['name']} | {SYM[c['status']]} | {c['detail'].replace('|', '／')} | {c['severity'] if c['status'] in ('fail','warn') else ''} | {c['ref']} |")
    n = {k: sum(1 for c in res if c["status"] == k) for k in SYM}
    out += ["", f"合計：未通過 {n['fail']}、注意 {n['warn']}、人工判定 {n['manual']}、通過 {n['pass']}。",
            "本腳本只做可自動化的技術檢查；內容品質、E-E-A-T、政策與 CWV 實測請依 skill 的 check 流程補人工項目與 cwv.py。"]
    return "\n".join(out)

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("urls", nargs="+"); ap.add_argument("--json"); ap.add_argument("--no-extra", action="store_true")
    ap.add_argument("--hreflang-check", action="store_true"); ap.add_argument("--timeout", type=int, default=20)
    a = ap.parse_args(); TIMEOUT = a.timeout
    allres = []
    for u in a.urls:
        if not u.startswith("http"): u = "https://" + u
        res, info = audit(u, extra=not a.no_extra, hreflang_check=a.hreflang_check)
        print(to_md(u, res, info)); print()
        allres.append({"url": u, "info": info, "checks": res, "audited_at": time.strftime("%Y-%m-%d %H:%M")})
    if a.json:
        json.dump(allres, open(a.json, "w", encoding="utf-8"), ensure_ascii=False, indent=1, default=str); print(f"JSON 已存 {a.json}")
