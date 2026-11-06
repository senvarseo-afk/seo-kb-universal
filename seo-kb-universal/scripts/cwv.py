#!/usr/bin/env python3
"""用 PageSpeed Insights API 取 Core Web Vitals（真實使用者 CrUX 數據 + Lighthouse 實驗室值），對照 00 §4 門檻。

用法：cwv.py <url> [--desktop] [--json out.json]
環境變數 PSI_API_KEY 可選（無金鑰也能用，但有配額；申請：https://developers.google.com/speed/docs/insights/v5/get-started）。
門檻（04 §11）：LCP ≤ 2.5 s / INP ≤ 200 ms / CLS ≤ 0.1 為良好；> 4.0 s / > 500 ms / > 0.25 為不良。
"""
import sys, os, json, argparse
from urllib import request, parse, error

TH = {"LCP": (2500, 4000, "ms"), "INP": (200, 500, "ms"), "CLS": (0.1, 0.25, ""), "TTFB": (800, 1800, "ms"), "FCP": (1800, 3000, "ms")}
KEYS = {"LARGEST_CONTENTFUL_PAINT_MS": "LCP", "INTERACTION_TO_NEXT_PAINT": "INP", "CUMULATIVE_LAYOUT_SHIFT_SCORE": "CLS",
        "EXPERIMENTAL_TIME_TO_FIRST_BYTE": "TTFB", "FIRST_CONTENTFUL_PAINT_MS": "FCP"}

def grade(name, v):
    g, p, _ = TH[name]
    return "良好" if v <= g else ("待改進" if v <= p else "不良")

def fmt(name, v):
    return f"{v/1000:.2f} s" if TH[name][2] == "ms" and name in ("LCP", "FCP") else (f"{v:.0f} ms" if TH[name][2] == "ms" else f"{v:.3f}")

def run(url, strategy):
    q = {"url": url, "strategy": strategy, "category": "PERFORMANCE"}
    if os.environ.get("PSI_API_KEY"): q["key"] = os.environ["PSI_API_KEY"]
    api = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?" + parse.urlencode(q)
    try:
        with request.urlopen(request.Request(api, headers={"User-Agent": "seo-kb-universal-cwv"}), timeout=120) as r:
            return json.load(r)
    except error.HTTPError as e:
        sys.exit(f"PSI API HTTP {e.code}：{e.read()[:300].decode('utf-8','replace')}（配額用完可設 PSI_API_KEY）")

def summarize(data, strategy):
    out = {"strategy": strategy, "field_page": {}, "field_origin": {}, "lab": {}}
    for scope, key in (("field_page", "loadingExperience"), ("field_origin", "originLoadingExperience")):
        le = data.get(key) or {}
        for k, name in KEYS.items():
            m = (le.get("metrics") or {}).get(k)
            if m: out[scope][name] = {"p75": m.get("percentile"), "category": m.get("category")}
        out[scope]["_overall"] = le.get("overall_category")
    lr = data.get("lighthouseResult") or {}; au = lr.get("audits") or {}
    for aid, name in (("largest-contentful-paint", "LCP"), ("cumulative-layout-shift", "CLS"), ("total-blocking-time", "TBT"),
                      ("server-response-time", "TTFB"), ("first-contentful-paint", "FCP"), ("speed-index", "SI")):
        if aid in au and au[aid].get("numericValue") is not None: out["lab"][name] = au[aid]["numericValue"]
    out["lab"]["_score"] = round(((lr.get("categories") or {}).get("performance") or {}).get("score", 0) * 100)
    opp = []
    for aid, a in au.items():
        d = a.get("details") or {}
        if d.get("type") == "opportunity" and (d.get("overallSavingsMs") or 0) >= 300:
            opp.append((a.get("title"), int(d["overallSavingsMs"])))
    out["lab"]["_opportunities"] = sorted(opp, key=lambda x: -x[1])[:6]
    return out

def to_md(url, s):
    L = [f"## Core Web Vitals：{url}（{s['strategy']}）", ""]
    for scope, title in (("field_page", "真實使用者數據（CrUX，此網址）"), ("field_origin", "真實使用者數據（CrUX，整個網域）")):
        d = s[scope]
        L.append(f"**{title}**：" + (f"整體 {d.get('_overall')}" if d.get("_overall") else "無足夠流量，CrUX 沒有資料（新站或流量小常見；以實驗室值與 GSC CWV 報表為準）"))
        rows = [(n, v) for n, v in d.items() if not n.startswith("_")]
        if rows:
            L += ["", "| 指標 | p75 | 評級 | 門檻（良好 / 不良） |", "|---|---|---|---|"]
            for n, v in rows:
                if n in TH: L.append(f"| {n} | {fmt(n, v['p75'])} | {grade(n, v['p75'])} | ≤ {fmt(n, TH[n][0])} / > {fmt(n, TH[n][1])} |")
        L.append("")
    lab = s["lab"]
    L += [f"**實驗室值（Lighthouse，效能分數 {lab.get('_score')}）**：INP 無實驗室值，以 TBT 當代理（TBT ≤ 200 ms 約略對應）", "", "| 指標 | 值 | 評級 |", "|---|---|---|"]
    for n in ("LCP", "CLS", "TBT", "TTFB", "FCP", "SI"):
        if n in lab:
            v = lab[n]
            g = grade(n, v) if n in TH else ("良好" if (n == "TBT" and v <= 200) else ("待改進" if n == "TBT" and v <= 600 else ("不良" if n == "TBT" else "")))
            L.append(f"| {n} | {fmt(n, v) if n in TH else f'{v:.0f} ms'} | {g} |")
    if lab.get("_opportunities"):
        L += ["", "**主要改善機會（預估節省）**"] + [f"- {t}：約 {ms} ms" for t, ms in lab["_opportunities"]]
    L += ["", "規範與做法：04 §11（CWV）、04 §12（圖片與 TTFB）、15 §11（CWV 範本）、22 §3.7（廣告與 CWV）。排名用的是真實使用者 p75，實驗室值只用來找原因。"]
    return "\n".join(L)

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("url"); ap.add_argument("--desktop", action="store_true"); ap.add_argument("--json")
    a = ap.parse_args(); u = a.url if a.url.startswith("http") else "https://" + a.url
    strategy = "desktop" if a.desktop else "mobile"
    s = summarize(run(u, strategy), strategy); s["url"] = u
    print(to_md(u, s))
    if a.json: json.dump(s, open(a.json, "w", encoding="utf-8"), ensure_ascii=False, indent=1); print(f"\nJSON 已存 {a.json}")
