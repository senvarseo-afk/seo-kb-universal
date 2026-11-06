#!/usr/bin/env python3
"""把 site_audit.py 與 cwv.py 的 JSON 結果填進知識庫的「SEO 稽核報告」結構，產出可直接交付的 Markdown 草稿。

用法：report.py --audit audit.json [--cwv cwv.json] [--out 報告.md] [--site 名稱]
產出：§0 摘要（自動數 P1/P2）、§2 發現清單（fail / warn 逐項，附章節）、§4 技術摘要、§6 行動計畫骨架；
      §1 現況數據、§3 政策自查、§5 內容與 E-E-A-T 留空給人工（需要 GSC / GA4 / 人工閱讀）。
"""
import json, argparse, time, os

def load(p): return json.load(open(p, encoding="utf-8")) if p and os.path.exists(p) else None

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--audit", required=True); ap.add_argument("--cwv"); ap.add_argument("--out"); ap.add_argument("--site")
    a = ap.parse_args(); audit = load(a.audit); cwv = load(a.cwv)
    pages = audit if isinstance(audit, list) else [audit]
    site = a.site or pages[0]["url"]
    findings = []
    SITE_LEVEL = {"https", "hsts", "xcto", "http2https", "wwwvariant", "robots", "sitemap", "sitemap_noindex", "adstxt", "soft404", "ga4", "adsense", "language", "scripts"}
    seen = {}
    for pg in pages:
        for c in pg["checks"]:
            if c["status"] in ("fail", "warn"):
                key = (c["id"], c["detail"]) if c["id"] in SITE_LEVEL else (c["id"], c["detail"], pg["url"])
                if key in seen:
                    seen[key][4] = "全站（多個 URL 相同）"; continue
                row = [c["severity"], "技術" if c["id"] not in ("language", "adsense", "adstxt") else "變現", c["name"], c["detail"], pg["url"], c["ref"]]
                seen[key] = row; findings.append(row)
    if cwv:
        fp = cwv.get("field_page") or {}
        for n in ("LCP", "INP", "CLS"):
            v = fp.get(n)
            if v and v.get("category") in ("SLOW", "AVERAGE"):
                findings.append(["P1" if v["category"] == "SLOW" else "P2", "技術", f"CWV {n} {v['category']}", f"p75 = {v['p75']}（{cwv.get('strategy')}）", cwv.get("url"), "04 §11"])
        if fp.get("_overall") is None:
            findings.append(["P3", "技術", "CrUX 無資料", "流量不足以產生真實使用者數據；以 GSC CWV 報表與實驗室值追蹤", cwv.get("url"), "04 §11"])
    findings.sort(key=lambda f: f[0])
    p1 = sum(1 for f in findings if f[0] == "P1"); p2 = sum(1 for f in findings if f[0] == "P2"); p3 = len(findings) - p1 - p2
    top3 = "；".join(f"{f[2]}（{f[0]}）" for f in findings[:3]) or "無自動偵測到的問題"
    L = [f"# SEO 稽核報告（自動草稿）：{site}", "",
         f"> 產出日期 {time.strftime('%Y-%m-%d')}。由 seo-kb-universal skill 的 site_audit.py / cwv.py 自動填入技術項目；標「人工」的段落需用 GSC、GA4 與人工閱讀補齊。檢查項目以 `14-檢查清單.md` §E、§F 為準；每個發現對應章節。", "",
         "## 0. 摘要（給決策者，10 行內）", "", "| 項目 | 內容 |", "|---|---|",
         f"| 網站 / 範圍 / 稽核日期 | {site} / {len(pages)} 個 URL / {time.strftime('%Y-%m-%d')} |",
         "| 整體健康度（技術 / 內容 / 權威 / 變現，各 1–5） | 技術：自動項目見 §2；內容、權威、變現：人工 |",
         f"| 最嚴重的三個問題與預估影響 | {top3} |",
         f"| 自動偵測的問題數 | P1 {p1}、P2 {p2}、P3 {p3} |",
         "| 建議的前三個行動與預估工時 | 人工填寫（依 §2 的 P1 項目） |",
         "| 風險提醒（政策類：07 §4 清單） | 人工填寫（§3） |", "",
         "## 1. 現況數據（13 §13.10 的指標定義）", "", "人工：自然點擊 / 曝光 / CTR / 平均排名（GSC 近 28 天 vs 前期）、已索引頁數與未索引主因、CWV 通過率、引用網域、收益 / RPM。", "",
         "## 2. 發現清單", "", "嚴重度：P1（流量或政策風險，立即）、P2（兩週內）、P3（排程）。", "",
         "| # | 類別 | 發現 | 證據（URL） | 嚴重度 | 對應章節 | 建議做法 | 預估工時 | 負責人 |", "|---|---|---|---|---|---|---|---|---|"]
    for i, f in enumerate(findings, 1):
        L.append(f"| {i} | {f[1]} | {f[2]}：{f[3].replace('|','／')} | {f[4]} | {f[0]} | {f[5]} | 見章節「怎麼做」 | | |")
    if not findings: L.append("| 1 | — | 自動檢查未發現問題 | | | | | | |")
    L += ["", "## 3. 政策自查（07 §4，每項填「無 / 有 / 疑似」）", "", "人工：Scaled content abuse、Site reputation abuse、Expired domain abuse、Link spam、Thin affiliation、Back button hijacking、其他。", "",
          "## 4. 技術與架構摘要（04、03、15）", "", "| 項目 | 狀態 | 備註 |", "|---|---|---|"]
    def st(cid):
        for pg in pages:
            for c in pg["checks"]:
                if c["id"] == cid: return c
        return None
    def row(label, ids, note=""):
        cs = [st(i) for i in ids if st(i)]
        if not cs: L.append(f"| {label} | 人工 | {note} |"); return
        worst = sorted(cs, key=lambda c: {"fail": 0, "warn": 1, "manual": 2, "pass": 3}[c["status"]])[0]
        L.append(f"| {label} | {worst['status']} | " + "；".join(f"{c['name']}：{c['detail']}" for c in cs).replace("|", "／") + " |")
    row("URL 唯一版本（www / https / 尾斜線）", ["https", "http2https", "wwwvariant"])
    row("robots.txt / noindex / canonical 一致性", ["robots", "noindex", "xrobots", "canonical"])
    row("sitemap 內容正確性", ["sitemap"], "只檢查可存取與數量；內容需爬取比對")
    row("轉址鏈 / 狀態碼", ["redirect", "soft404"])
    row("JS 渲染", [], "人工：GSC URL 檢查工具「查看已檢索網頁」")
    if cwv:
        lab = cwv.get("lab", {}); fp = cwv.get("field_page", {})
        L.append(f"| CWV 三指標與主要原因 | {fp.get('_overall') or '無 CrUX'} | 實驗室 LCP {lab.get('LCP', 0)/1000:.2f}s、CLS {lab.get('CLS', 0):.3f}、TBT {lab.get('TBT', 0):.0f}ms；改善機會：" + "；".join(f"{t}（{ms}ms）" for t, ms in lab.get("_opportunities", [])[:3]) + " |")
    else: row("CWV 三指標與主要原因", ["ttfb"], "跑 cwv.py 取得 CrUX 與實驗室值")
    row("內部連結與孤兒頁", [], "人工：Screaming Frog 爬取")
    row("分面 / 參數 / 站內搜尋頁索引控制", [], "人工：爬取抽查")
    row("hreflang（若多語）", ["hreflang", "hreflang_rt"])
    row("結構化資料", ["jsonld"], "用 Rich Results Test 驗證必要屬性")
    row("語言與 AdSense 合規", ["language", "adsense", "adstxt"])
    L += ["", "## 5. 內容與 E-E-A-T 摘要（05）", "", "人工：薄 / 重複內容比例、作者與關於頁、標題規範與蠶食、內容時效、AI 輔助內容審核紀錄。可先用 `/seo-kb-universal review <文章>` 抽查 3–5 篇。", "",
          "## 6. 行動計畫", "", "| 階段 | 行動 | 對應發現 # | 完成日 | 驗收方式 |", "|---|---|---|---|---|",
          "| 立即（1 週） | " + "、".join(str(i) for i, f in enumerate(findings, 1) if f[0] == "P1") + " 號 P1 項目 | | | 章節的「驗收方式」 |",
          "| 短期（1 個月） | P2 項目 | | | |", "| 中期（1 季） | P3 與內容項目 | | | |", "", "## 7. 附錄", "", "原始輸出：" + a.audit + (f"、{a.cwv}" if a.cwv else "")]
    md = "\n".join(L)
    out = a.out or f"seo-audit-{time.strftime('%Y%m%d')}.md"
    open(out, "w", encoding="utf-8").write(md); print(f"報告草稿已存 {out}（{len(findings)} 個發現：P1 {p1}、P2 {p2}、P3 {p3}）")

if __name__ == "__main__": main()
