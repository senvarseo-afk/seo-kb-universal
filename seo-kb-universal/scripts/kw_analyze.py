#!/usr/bin/env python3
"""讀 gsc_pull.py 的 gsc.json，依知識庫規則產出關鍵字優化行動清單與報告。

用法：
  kw_analyze.py seo-ops/data/2026-11-06/gsc.json --out seo-ops/reports [--config seo-ops/config.json]
  kw_analyze.py <gsc.json> --grade --sitemap https://example.com/sitemap.xml      # 季檢：內容 A–E 分級（02 §13.1）
  kw_analyze.py <gsc.json> --master seo-ops/keyword-master.csv                     # 對照關鍵字母表，標出母表沒有的新查詢
  kw_analyze.py <gsc.json> --append-log seo-ops/action-log.csv                     # 新行動併入行動紀錄（同 type+target 不重複）
選項：--min-impr 100（頁面納入門檻）、--top 20（每節列數）、--brand "regex"（品牌字，config 有則不用給）

分析項目與規則出處：
  1 總覽與告警         13 §13.9.1（週比點擊 −20%、CTR −1 個百分點、單日 vs 前 7 週同星期 −30%）
  2 品牌 / 非品牌       13 §13.1.12
  3 衝刺區（5–20 名）   02 §13.1 A、01 §2.6
  4 標題佇列（低 CTR）  12 C3 預防規則：排名 ≤ 10 且 CTR 低於站內同位置中位數 50%；05 §1
  5 衰退 / 成長頁       02 §13.1 B（點擊 −30% 且排名下滑）、12 B6 / C3（排名沒掉但點擊掉）
  6 新查詢 / 消失查詢   02 §9.1、§9.2
  7 蠶食               02 §12（同查詢 ≥ 2 個 URL 各佔 ≥ 20% 曝光）
  8 可能缺專頁          02 §9.1（查詢與到達頁 slug 無共同字）
  9 A–E 分級（--grade） 02 §13.1；D 級比例門檻 15%
"""
import sys, os, re, csv, json, argparse, statistics
import datetime as dt
from urllib.parse import urlparse, unquote
from urllib import request

STOP = set("""the a an of to in for and or is are how what when where why which who with on at by from vs versus be do does
can my your it this that ng sa ang mga na ba ko mo ano paano saan ba po ka si ni ay para kung at
的 是 什麼 怎麼 如何 和 與 在 有 嗎 了""".split())

def tokens(s):
    return {t for t in re.split(r"[^0-9a-z\u00c0-\u024f\u0e00-\u0e7f\u0980-\u09ff\u4e00-\u9fff]+", unquote(s).lower()) if len(t) >= 2 and t not in STOP}

def slug_tokens(url):
    p = urlparse(url).path
    return tokens(p.replace("-", " ").replace("_", " ").replace("/", " ").replace(".html", ""))

def idx(rows, n=1):
    return {tuple(r["keys"][:n]): r for r in rows or []}

def totals(rows):
    c = sum(r["clicks"] for r in rows); i = sum(r["impressions"] for r in rows)
    pos = sum(r["position"] * r["impressions"] for r in rows) / i if i else 0
    return {"clicks": c, "impressions": i, "ctr": c / i if i else 0, "position": pos}

def delta(a, b): return None if not b else (a - b) / b
def fd(x): return "—" if x is None else f"{x*100:+.0f}%"
def fp(x): return f"{x*100:.1f}%"
def fn(x): return f"{x:,.0f}"
def md_cell(s): return str(s).replace("|", "\\|").replace("\n", " ")

def bucket(pos):
    for lim, name in ((1.5, "1"), (2.5, "2"), (3.5, "3"), (5.5, "4–5"), (10.5, "6–10"), (20.5, "11–20")):
        if pos < lim: return name
    return "21+"

def bucket_medians(rows, min_impr=50):
    groups = {}
    for r in rows:
        if r["impressions"] >= min_impr: groups.setdefault(bucket(r["position"]), []).append(r["ctr"])
    return {b: statistics.median(v) for b, v in groups.items() if len(v) >= 3}

def fetch_sitemap(src, seen=None, depth=0):
    seen = seen if seen is not None else set()
    if src in seen or depth > 3: return []
    seen.add(src)
    try:
        if src.startswith("http"):
            with request.urlopen(request.Request(src, headers={"User-Agent": "seo-kb-universal"}), timeout=60) as r: xml = r.read().decode("utf-8", "replace")
        else:
            xml = open(src, encoding="utf-8").read()
    except Exception as e:
        print(f"讀不到 sitemap {src}：{e}", file=sys.stderr); return []
    locs = re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", xml)
    if "<sitemapindex" in xml:
        urls = []
        for l in locs: urls += fetch_sitemap(l, seen, depth + 1)
        return urls
    return locs

class Report:
    def __init__(self): self.L = []; self.actions = []
    def h(self, t): self.L += ["", f"## {t}", ""]
    def p(self, t): self.L += [t, ""]
    def table(self, header, rows):
        if not rows: self.L += ["（無符合項目）", ""]; return
        self.L += ["| " + " | ".join(header) + " |", "|" + "---|" * len(header)]
        self.L += ["| " + " | ".join(md_cell(c) for c in r) + " |" for r in rows]
        self.L.append("")
    def act(self, typ, target, evidence, action, ref, cadence="weekly"):
        self.actions.append({"type": typ, "target": target, "evidence": evidence, "action": action, "kb_ref": ref, "cadence": cadence})

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("gsc_json"); ap.add_argument("--out", default="seo-ops/reports"); ap.add_argument("--config")
    ap.add_argument("--brand"); ap.add_argument("--min-impr", type=float, default=100); ap.add_argument("--top", type=int, default=20)
    ap.add_argument("--grade", action="store_true"); ap.add_argument("--sitemap"); ap.add_argument("--master"); ap.add_argument("--append-log")
    a = ap.parse_args()

    data = json.load(open(a.gsc_json, encoding="utf-8"))
    cfg = json.load(open(a.config, encoding="utf-8")) if a.config and os.path.exists(a.config) else {}
    brand = a.brand or cfg.get("brand_regex"); brand_re = re.compile(brand, re.I) if brand else None
    a.sitemap = a.sitemap or (cfg.get("sitemap") if a.grade else None)
    cur, prev, yoy = data["current"], data.get("previous"), data.get("yoy")
    site = data.get("site") or cfg.get("site") or "（未知資源）"
    R = Report(); R.L += [f"# 關鍵字優化檢視：{site}", "",
        f"資料：{data.get('source','?')}，type={data.get('search_type','web')}" + (f"，國家={data['country_filter']}" if data.get("country_filter") else "") +
        f"，拉取 {data.get('pulled_at','')[:16]}。本期 {cur['start']}～{cur['end']}" + (f"；前期 {prev['start']}～{prev['end']}" if prev else "；無前期資料") + "。",
        "", "口徑：GSC Web 搜尋，不含 Discover / News（13 §13.10.1）。GSC 介面與 API 會匿名化長尾查詢，查詢加總小於頁面加總是正常的（13 §13.1.1）。"]
    if not prev: R.p("**注意**：沒有前期資料，衰退、新查詢、告警三節會略過。用 API 模式或加 --prev-csv。")

    qi, pi = idx(cur.get("query")), idx(cur.get("page"))
    qp = cur.get("query_page") or []
    pqi, ppi = idx(prev.get("query")) if prev else {}, idx(prev.get("page")) if prev else {}
    medians = bucket_medians(cur.get("query") or [])

    # 1 總覽
    R.h("1. 總覽與告警（13 §13.9.1）")
    tc = totals(cur.get("page") or cur.get("query") or [])
    rows = []
    if prev:
        tp = totals(prev.get("page") or prev.get("query") or [])
        dc, di = delta(tc["clicks"], tp["clicks"]), delta(tc["impressions"], tp["impressions"])
        dctr = tc["ctr"] - tp["ctr"]; dpos = tc["position"] - tp["position"]
        rows = [["點擊", fn(tc["clicks"]), fn(tp["clicks"]), fd(dc), "週比 −20%（28 天比照用）", "注意" if dc is not None and dc <= -0.2 else "通過"],
                ["曝光", fn(tc["impressions"]), fn(tp["impressions"]), fd(di), "—", "注意" if di is not None and di <= -0.2 else "通過"],
                ["CTR", fp(tc["ctr"]), fp(tp["ctr"]), f"{dctr*100:+.1f} pt", "−1 個百分點", "注意" if dctr <= -0.01 else "通過"],
                ["平均位置", f"{tc['position']:.1f}", f"{tp['position']:.1f}", f"{dpos:+.1f}", "—", "注意" if dpos >= 1 else "通過"]]
        R.table(["指標", "本期", "前期", "變化", "門檻", "判定"], rows)
        if yoy:
            ty = totals(yoy.get("page") or yoy.get("query") or [])
            R.p(f"去年同期 {yoy['start']}～{yoy['end']}：點擊 {fn(ty['clicks'])}（年比 {fd(delta(tc['clicks'], ty['clicks']))}）、曝光 {fn(ty['impressions'])}（{fd(delta(tc['impressions'], ty['impressions']))}）。年比用來分辨季節性與真實衰退（02 §11、12 B3）。")
    else:
        R.table(["指標", "本期"], [["點擊", fn(tc["clicks"])], ["曝光", fn(tc["impressions"])], ["CTR", fp(tc["ctr"])], ["平均位置", f"{tc['position']:.1f}"]])

    # 單日告警
    dates = {r["keys"][0]: r for r in (cur.get("date") or []) + ((prev.get("date") or []) if prev else [])}
    if len(dates) >= 14:
        ds = sorted(dates); last = ds[-1]; ld = dt.date.fromisoformat(last)
        same = [dates[d]["clicks"] for d in ds[:-1] if dt.date.fromisoformat(d).weekday() == ld.weekday()][-7:]
        if same:
            avg = sum(same) / len(same); dd = delta(dates[last]["clicks"], avg)
            flag = dd is not None and dd <= -0.3
            R.p(f"最新完整日 {last}：點擊 {fn(dates[last]['clicks'])}，前 {len(same)} 週同星期平均 {avg:.0f}（{fd(dd)}）。門檻 −30%：{'**觸發**，先排除 GSC 延遲與假驟降（12 B4、B3），再走 diagnose' if flag else '通過'}。")
            if flag: R.act("alert_daily_drop", site, f"{last} 點擊 {fd(dd)} vs 同星期均值", "排除資料延遲、追蹤與季節後走 diagnose 子指令", "13 §13.9、12 §1")
    # 國家 / 裝置
    for dim, title in (("country", "國家"), ("device", "裝置")):
        ci, cpi = idx(cur.get(dim)), idx(prev.get(dim)) if prev else {}
        if not ci: continue
        top = sorted(ci.values(), key=lambda r: -r["clicks"])[:6]
        rows = []
        for r in top:
            p = cpi.get(tuple(r["keys"][:1])); d = delta(r["clicks"], p["clicks"]) if p else None
            rows.append([r["keys"][0], fn(r["clicks"]), fn(r["impressions"]), fp(r["ctr"]), f"{r['position']:.1f}", fd(d), "注意" if d is not None and d <= -0.2 else ""])
            if d is not None and d <= -0.2 and r["clicks"] >= 50:
                R.act("segment_drop", f"{dim}:{r['keys'][0]}", f"點擊 {fd(d)}", "拆此區段看 Pages × Queries，確認是 SERP 變化、季節或技術", "13 §13.1.1、12 I5" if dim == "country" else "13 §13.1.1")
        R.p(f"**{title}**" + ("（多國站務必分國家看，各國走勢常不同步，13 §13.1.1）" if dim == "country" else "（2026-11 起 GSC 可多選裝置直接比較，13 §13.1.1）"))
        R.table([title, "點擊", "曝光", "CTR", "位置", "點擊變化", ""], rows)

    # 2 品牌
    R.h("2. 品牌 vs 非品牌")
    if brand_re and qi:
        def split(rows): 
            b = [r for r in rows if brand_re.search(r["keys"][0])]; nb = [r for r in rows if not brand_re.search(r["keys"][0])]
            return totals(b), totals(nb)
        cb, cn = split(cur["query"]); rows = []
        if prev and prev.get("query"):
            pb, pn = split(prev["query"])
            rows = [["品牌", fn(cb["clicks"]), fd(delta(cb["clicks"], pb["clicks"])), fn(cb["impressions"]), fp(cb["ctr"])],
                    ["非品牌", fn(cn["clicks"]), fd(delta(cn["clicks"], pn["clicks"])), fn(cn["impressions"]), fp(cn["ctr"])]]
            R.table(["分組", "點擊", "點擊變化", "曝光", "CTR"], rows)
        else:
            R.table(["分組", "點擊", "曝光", "CTR"], [["品牌", fn(cb["clicks"]), fn(cb["impressions"]), fp(cb["ctr"])], ["非品牌", fn(cn["clicks"]), fn(cn["impressions"]), fp(cn["ctr"])]])
        R.p(f"品牌 regex：`{brand}`。SEO 成效看非品牌；品牌字成長是品牌搜尋量指標（01 §3.2 12–24 個月領先指標）。")
    else:
        R.p("未設品牌 regex（config.json 的 brand_regex 或 --brand），略過。")

    # 查詢→頁面 對照
    q_pages = {}
    for r in qp: q_pages.setdefault(r["keys"][0], []).append(r)
    p_queries = {}
    for r in qp: p_queries.setdefault(r["keys"][1], []).append(r)
    def top_q(url, n=3):
        return "；".join(f"{r['keys'][0]}（{fn(r['impressions'])}，{r['position']:.0f} 名）" for r in sorted(p_queries.get(url, []), key=lambda r: -r["impressions"])[:n]) or "（需 query×page 維度）"

    # 3 衝刺區
    R.h("3. 衝刺區：排名 5–20、曝光高的頁面（02 §13.1 A、01 §2.6）")
    sd = sorted([r for r in pi.values() if 5 <= r["position"] <= 20 and r["impressions"] >= a.min_impr], key=lambda r: -r["impressions"])[:a.top]
    rows = []
    for r in sd:
        med = medians.get(bucket(r["position"])); low = med is not None and r["ctr"] < med * 0.5
        rows.append([r["keys"][0], fn(r["impressions"]), fn(r["clicks"]), fp(r["ctr"]) + ("（偏低）" if low else ""), f"{r['position']:.1f}", top_q(r["keys"][0])])
        R.act("update_content", r["keys"][0], f"曝光 {fn(r['impressions'])}、位置 {r['position']:.1f}、CTR {fp(r['ctr'])}", "重寫 title / 首段、補子主題與表格、更新資料與日期、補 3 個內部連結", "02 §13.1 A、05 §1、§6", "monthly")
    R.table(["頁面", "曝光", "點擊", "CTR", "位置", "主要查詢"], rows)
    R.p("規則：每月保留 20% 產能給這類更新（02 §8）；更新前先匯出該頁所有排名查詢，避免刪掉原本排名的段落（02 §14）。更新後請求重新索引，30–60 天回看。")

    # 4 標題佇列
    R.h("4. 標題佇列：排名 ≤ 10 但 CTR 低於站內同位置中位數一半（12 C3、05 §1）")
    if medians:
        order = ["1", "2", "3", "4–5", "6–10", "11–20", "21+"]
        R.p("站內 CTR 中位數（查詢層、曝光 ≥ 50）：" + "、".join(f"{b} 名 {fp(medians[b])}" for b in order if b in medians) + "。這是本站自己的基準，不是通用 CTR 表。")
    tq = []
    for r in pi.values():
        med = medians.get(bucket(r["position"]))
        if med and r["position"] <= 10 and r["impressions"] >= a.min_impr and r["ctr"] < med * 0.5:
            tq.append((r, med))
    tq.sort(key=lambda x: -x[0]["impressions"]); rows = []
    for r, med in tq[:a.top]:
        rows.append([r["keys"][0], fn(r["impressions"]), fp(r["ctr"]), fp(med), f"{r['position']:.1f}", top_q(r["keys"][0])])
        R.act("title_rewrite", r["keys"][0], f"位置 {r['position']:.1f}、CTR {fp(r['ctr'])} vs 中位數 {fp(med)}", "先查 SERP（目標國家、手機、無痕）確認首屏與 Google 顯示標題；重寫 title / description；記入 title-test-log，28 天後對照", "12 C3、05 §1.2、§2")
    R.table(["頁面", "曝光", "CTR", "同位置中位數", "位置", "主要查詢"], rows)
    R.p("判讀：先用「查詢 × 國家 × 裝置」確認主要市場真實位置（平均位置會被稀釋）；SERP 有 AI Overviews 或論壇區塊時 CTR 低是結構性的，標題改寫幫助有限（08 §2、12 B6）。")

    # 5 衰退 / 成長
    R.h("5. 衰退頁與成長頁（02 §13.1 B、12 B6 / C3）")
    if prev and ppi:
        dec, gain = [], []
        for k, r in pi.items():
            p = ppi.get(k)
            if not p: continue
            dcl = delta(r["clicks"], p["clicks"]); dpos = r["position"] - p["position"]
            if p["clicks"] >= 20 and dcl is not None and dcl <= -0.3:
                kind = "B 衰退：排名下滑" if dpos >= 1 else "排名沒掉、點擊掉（SERP / 標題）"
                dec.append([r["keys"][0], fn(p["clicks"]), fn(r["clicks"]), fd(dcl), f"{p['position']:.1f}→{r['position']:.1f}", kind])
                R.act("investigate_decline", r["keys"][0], f"點擊 {fd(dcl)}、位置 {p['position']:.1f}→{r['position']:.1f}",
                      "比對 SERP 是否變了（新格式、新競爭者、AIO）；依新 SERP 重寫並補內部連結" if dpos >= 1 else "查 SERP 功能與 Google 顯示標題；核對是否季節或資料延遲",
                      "02 §13.1 B、12 B1/B6" if dpos >= 1 else "12 C3、B6")
            if r["clicks"] - p["clicks"] >= 10: gain.append([r["keys"][0], fn(p["clicks"]), fn(r["clicks"]), fd(dcl), f"{p['position']:.1f}→{r['position']:.1f}"])
        dec.sort(key=lambda x: float(x[1].replace(",", "")) - float(x[2].replace(",", "")), reverse=True)
        R.p("**衰退（前期點擊 ≥ 20，點擊 −30% 以上）**"); R.table(["頁面", "前期點擊", "本期點擊", "變化", "位置", "判定"], dec[:a.top])
        gain.sort(key=lambda x: -(float(x[2].replace(",", "")) - float(x[1].replace(",", ""))))
        R.p("**成長（以表現好的頁為核心擴張 spoke，02 §14）**"); R.table(["頁面", "前期點擊", "本期點擊", "變化", "位置"], gain[:10])
        new_pages = [r for k, r in pi.items() if k not in ppi and r["impressions"] >= 20]
        if new_pages: R.p(f"本期新出現在 GSC 的頁面 {len(new_pages)} 個（前期無曝光）：" + "、".join(r["keys"][0] for r in sorted(new_pages, key=lambda r: -r["impressions"])[:10]))
    else:
        R.p("無前期頁面資料，略過。")

    # 6 新查詢 / 消失
    R.h("6. 新查詢與消失查詢（02 §9.1、§9.2 零量字驗證）")
    master_kw = set()
    if a.master and os.path.exists(a.master):
        with open(a.master, encoding="utf-8-sig", newline="") as f:
            for row in csv.DictReader(f):
                k = (row.get("keyword") or "").strip().lower()
                if k: master_kw.add(k)
    def in_master(q):
        ql = q.lower(); return any(ql == m or m in ql for m in master_kw)
    if prev and pqi:
        newq = sorted([r for k, r in qi.items() if k not in pqi and r["impressions"] >= 20], key=lambda r: -r["impressions"])
        rows = []
        for r in newq[:a.top]:
            lp = sorted(q_pages.get(r["keys"][0], []), key=lambda x: -x["impressions"])
            land = lp[0]["keys"][1] if lp else "（需 query×page）"
            rows.append([r["keys"][0], fn(r["impressions"]), fn(r["clicks"]), f"{r['position']:.1f}", land, ("已在母表" if in_master(r["keys"][0]) else "母表沒有") if master_kw else ""])
            if r["impressions"] >= 50 and (not master_kw or not in_master(r["keys"][0])):
                R.act("new_query", r["keys"][0], f"新查詢曝光 {fn(r['impressions'])}、位置 {r['position']:.1f}", "加入關鍵字母表→做 SERP 分析→判斷擴寫既有頁或開新 spoke", "02 §9、§4、§7", "monthly")
        R.table(["查詢", "曝光", "點擊", "位置", "到達頁", "母表"], rows)
        lost = sorted([r for k, r in pqi.items() if k not in qi and r["impressions"] >= 50], key=lambda r: -r["impressions"])[:10]
        if lost: R.p("**消失查詢**（前期曝光 ≥ 50，本期為 0）：" + "、".join(f"{r['keys'][0]}（{fn(r['impressions'])}）" for r in lost) + "。可能是季節、匿名化或排名掉出，季檢時再確認。")
    else:
        R.p("無前期查詢資料，略過。" + ("" if not master_kw else f" 母表載入 {len(master_kw)} 個關鍵字。"))

    # 7 蠶食
    R.h("7. 蠶食候選：同一查詢 ≥ 2 個 URL 各佔 ≥ 20% 曝光（02 §12）")
    if qp:
        rows = []
        for q, lst in sorted(q_pages.items(), key=lambda kv: -sum(r["impressions"] for r in kv[1])):
            tot = sum(r["impressions"] for r in lst)
            if tot < 50: continue
            shares = [r for r in lst if r["impressions"] / tot >= 0.2]
            if len(shares) >= 2:
                rows.append([q, fn(tot), " ／ ".join(f"{r['keys'][1]}（{r['impressions']/tot*100:.0f}%，{r['position']:.0f} 名）" for r in sorted(shares, key=lambda r: -r["impressions"]))])
                R.act("cannibalization", q, f"{len(shares)} 個 URL 分攤 {fn(tot)} 曝光", "判定意圖是否相同：相同→合併至較好 URL 並 301；不同→重寫 title / H1 / 首段區分並互連", "02 §12.3", "monthly")
            if len(rows) >= a.top: break
        R.table(["查詢", "曝光", "URL（份額，位置）"], rows)
        R.p("雙排名且兩頁都穩定靠前不是蠶食（02 §12.1），只處理「排名輪替且都不理想」的。")
    else:
        R.p("沒有查詢 × 網頁維度（介面匯出的 CSV 沒有），略過。用 API 模式可得。")

    # 8 缺專頁
    R.h("8. 可能缺專頁：查詢與到達頁 slug 無共同字（02 §9.1）")
    if qp:
        rows = []
        for q, lst in sorted(q_pages.items(), key=lambda kv: -sum(r["impressions"] for r in kv[1])):
            tot = sum(r["impressions"] for r in lst)
            if tot < 50: continue
            if brand_re and brand_re.search(q): continue
            top = max(lst, key=lambda r: r["impressions"]); url = top["keys"][1]
            is_home = urlparse(url).path in ("", "/")
            if is_home or not (tokens(q) & slug_tokens(url)):
                rows.append([q, fn(tot), f"{top['position']:.0f}", url, "落在首頁" if is_home else "slug 無共同字", ("已在母表" if in_master(q) else "母表沒有") if master_kw else ""])
                R.act("missing_page", q, f"曝光 {fn(tot)} 落在 {url}", "人工確認：該頁是否真的回答此查詢；否則開專頁或在既有頁加專節並調整內部連結錨文字", "02 §9.1、§6、03 §5", "monthly")
            if len(rows) >= a.top: break
        R.table(["查詢", "曝光", "位置", "到達頁", "原因", "母表"], rows)
        R.p("這是啟發式，中文、日文等沒有空白分詞的語言比對粗糙，列出的只是候選，要人工看。")
    else:
        R.p("沒有查詢 × 網頁維度，略過。")

    # 9 分級
    if a.grade:
        R.h("9. 內容分級 A–E（02 §13.1，季檢）")
        days = (dt.date.fromisoformat(cur["end"]) - dt.date.fromisoformat(cur["start"])).days + 1
        if days < 60: R.p(f"本期只有 {days} 天，分級規範是近 3 個月 vs 前 3 個月，建議用 --days 90 重拉。")
        sm = fetch_sitemap(a.sitemap) if a.sitemap else []
        def norm(u): return u.rstrip("/").lower()
        gsc_urls = {norm(k[0]) for k in pi}
        grades = {}
        for k, r in pi.items():
            url = k[0]; p = ppi.get(k); med = medians.get(bucket(r["position"]))
            g, why = None, ""
            if p and p["clicks"] >= 20 and delta(r["clicks"], p["clicks"]) is not None and delta(r["clicks"], p["clicks"]) <= -0.3 and r["position"] - p["position"] >= 1:
                g, why = "B", f"點擊 {fd(delta(r['clicks'], p['clicks']))}、位置 {p['position']:.1f}→{r['position']:.1f}"
            elif r["impressions"] >= a.min_impr and 5 <= r["position"] <= 20:
                g, why = "A", f"曝光 {fn(r['impressions'])}、位置 {r['position']:.1f}" + ("、CTR 偏低" if med and r["ctr"] < med else "")
            elif r["position"] <= 5 and r["impressions"] >= a.min_impr:
                g, why = "C", f"位置 {r['position']:.1f}、點擊 {fn(r['clicks'])}"
            elif r["impressions"] < 50 * max(1, days / 30):
                g, why = "D?", f"本期曝光僅 {fn(r['impressions'])}（需確認發佈 > 6 個月）"
            else:
                g, why = "—", f"曝光 {fn(r['impressions'])}、位置 {r['position']:.1f}（未達任何分級門檻，續觀察）"
            grades[url] = (g, why, r)
        zero = [u for u in sm if norm(u) not in gsc_urls]
        for u in zero: grades[u] = ("D?", "sitemap 有、本期 GSC 零曝光（需確認發佈 > 6 個月且可索引）", None)
        counts = {}
        for g, _, _ in grades.values(): counts[g] = counts.get(g, 0) + 1
        total = len(grades); dq = counts.get("D?", 0)
        R.table(["分級", "頁數", "動作（02 §13.1）"], [
            ["A 更新優先", counts.get("A", 0), "重寫 title / 首段、補子主題、更新資料與日期、加表格 / 圖"],
            ["B 衰退", counts.get("B", 0), "檢查 SERP 是否變了；依新 SERP 重寫；補連結"],
            ["C 穩定", counts.get("C", 0), "每 6–12 個月輕量更新"],
            ["D? 零流量候選", dq, "確認發佈 > 6 個月後：合併（301）、改寫瞄準新意圖、或刪除（410）"],
            ["— 未分級", counts.get("—", 0), "續觀察"],
            ["E 過時 / 違規", "人工", "資訊錯誤、產品停售、政策已變：立即更新或下架"]])
        ratio = dq / total if total else 0
        R.p(f"D 級候選比例 {ratio*100:.0f}%（{dq}/{total}，{'含' if sm else '不含'} sitemap 零曝光頁）；驗收門檻 < 15%（02 §13）：{'**未通過**' if ratio >= 0.15 else '通過'}。刪除前確認外部連結與內部連結（02 §13.2）。")
        gpath = os.path.join(a.out, f"{cur['end']}-grades.csv"); os.makedirs(a.out, exist_ok=True)
        with open(gpath, "w", encoding="utf-8", newline="") as f:
            w = csv.writer(f); w.writerow(["url", "grade", "why", "clicks", "impressions", "ctr", "position", "top_queries"])
            for u, (g, why, r) in sorted(grades.items(), key=lambda kv: (kv[1][0], -(kv[1][2]["impressions"] if kv[1][2] else 0))):
                w.writerow([u, g, why] + ([fn(r["clicks"]), fn(r["impressions"]), fp(r["ctr"]), f"{r['position']:.1f}", top_q(u)] if r else ["0", "0", "", "", ""]))
        R.p(f"全頁分級表：`{gpath}`。D? 要人工補發佈日期與索引狀態；E 級只能人工判定。")
        for u, (g, why, r) in grades.items():
            if g == "D?": R.act("grade_D", u, why, "確認發佈日期與索引狀態；合併 / 改寫 / 410 三選一", "02 §13.1 D、§13.2", "quarterly")

    # 行動清單
    R.h("行動清單")
    R.p(f"共 {len(R.actions)} 項，依類型：" + "、".join(f"{t} {n}" for t, n in sorted({x['type']: sum(1 for y in R.actions if y['type'] == x['type']) for x in R.actions}.items(), key=lambda kv: -kv[1])))
    R.table(["類型", "對象", "證據", "建議動作", "章節"], [[x["type"], x["target"], x["evidence"], x["action"], x["kb_ref"]] for x in R.actions[:60]])
    R.p("每項做完記錄到 action-log.csv（日期、改了什麼、原因），30–60 天後回看成效（02 §13.2）。")

    os.makedirs(a.out, exist_ok=True)
    tag = "-quarterly" if a.grade else ""
    rpath = os.path.join(a.out, f"{cur['end']}{tag}-keyword-ops.md")
    open(rpath, "w", encoding="utf-8").write("\n".join(R.L).strip() + "\n")
    apath = os.path.join(a.out, f"{cur['end']}{tag}-actions.csv")
    with open(apath, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["date", "cadence", "type", "target", "evidence", "action", "kb_ref", "status", "due", "done_date", "note"])
        w.writeheader()
        for x in R.actions:
            w.writerow({"date": cur["end"], "cadence": x["cadence"], "type": x["type"], "target": x["target"], "evidence": x["evidence"],
                        "action": x["action"], "kb_ref": x["kb_ref"], "status": "待處理",
                        "due": (dt.date.fromisoformat(cur["end"]) + dt.timedelta(days={"weekly": 7, "monthly": 30, "quarterly": 60}[x["cadence"]])).isoformat(), "done_date": "", "note": ""})
    if a.append_log:
        existing = set()
        exists = os.path.exists(a.append_log)
        if exists:
            with open(a.append_log, encoding="utf-8-sig", newline="") as f:
                for row in csv.DictReader(f): existing.add((row.get("type"), row.get("target")))
        added = 0
        with open(a.append_log, "a", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=["date", "cadence", "type", "target", "evidence", "action", "kb_ref", "status", "due", "done_date", "note"])
            if not exists: w.writeheader()
            for row in csv.DictReader(open(apath, encoding="utf-8", newline="")):
                if (row["type"], row["target"]) not in existing: w.writerow(row); added += 1
        print(f"action-log 新增 {added} 項（略過已存在 {len(R.actions) - added} 項）", file=sys.stderr)
    print(rpath); print(apath)

if __name__ == "__main__":
    main()
