#!/usr/bin/env python3
"""從 Google Search Console 拉成效資料（本期 vs 前期），存成分析腳本吃的 gsc.json。純標準庫，不需安裝套件。

兩種來源：
  A. Search Analytics API（建議）：service account JSON 用 openssl 簽 JWT 換 access token。
     gsc_pull.py --site sc-domain:example.com --sa ~/keys/gsc-sa.json --out seo-ops/data [--days 28] [--end 2026-11-06]
     gsc_pull.py --site https://example.com/ --sa ... --country twn --yoy        # 只看某國；另拉去年同期（季節性，02 §11）
     gsc_pull.py --sa ~/keys/gsc-sa.json --list-sites                            # 確認 service account 看得到哪些資源
     也可用環境變數：GSC_SA_JSON=<路徑>、GSC_ACCESS_TOKEN=<現成 token>（二擇一）。
  B. GSC 介面匯出的 CSV（無 API 時）：成效報表右上「匯出」→ 下載 zip 解開後的資料夾（含 Queries.csv、Pages.csv…）。
     gsc_pull.py --from-csv <本期資料夾> [--prev-csv <前期資料夾>] --start 2026-10-10 --end 2026-11-06 --out seo-ops/data
     介面匯出沒有「查詢 × 網頁」維度，蠶食與缺專頁分析會略過；上限 1,000 列（13 §13.1.12）。

輸出：<out>/<end 日期>/gsc.json。資料口徑：type=web（不含 Discover / News，13 §13.10.1），dataState=final。
GSC 資料通常延遲 2–3 天，預設 end = 今天 − 3 天；API 配額 1,200 QPM / 站（13 §13.1.12）。
"""
import sys, os, json, csv, argparse, base64, time, subprocess, tempfile, glob, re
import datetime as dt
from urllib import request, parse, error

SCOPE = "https://www.googleapis.com/auth/webmasters.readonly"
TOKEN_URL = "https://oauth2.googleapis.com/token"
API = "https://www.googleapis.com/webmasters/v3/sites/{site}/searchAnalytics/query"
SITES_API = "https://www.googleapis.com/webmasters/v3/sites"
DIMS = {"query": ["query"], "page": ["page"], "query_page": ["query", "page"],
        "country": ["country"], "device": ["device"], "date": ["date"]}
PAGE = 25000

def b64(b): return base64.urlsafe_b64encode(b).rstrip(b"=").decode()

def sa_token(sa_path):
    sa = json.load(open(os.path.expanduser(sa_path), encoding="utf-8"))
    now = int(time.time())
    header = b64(json.dumps({"alg": "RS256", "typ": "JWT"}).encode())
    claims = b64(json.dumps({"iss": sa["client_email"], "scope": SCOPE, "aud": TOKEN_URL,
                             "iat": now, "exp": now + 3600}).encode())
    signing_input = f"{header}.{claims}".encode()
    fd, key_path = tempfile.mkstemp(suffix=".pem")
    try:
        with os.fdopen(fd, "w") as f: f.write(sa["private_key"])
        os.chmod(key_path, 0o600)
        sig = subprocess.run(["openssl", "dgst", "-sha256", "-sign", key_path],
                             input=signing_input, capture_output=True, check=True).stdout
    finally:
        os.unlink(key_path)
    body = parse.urlencode({"grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer",
                            "assertion": f"{header}.{claims}.{b64(sig)}"}).encode()
    try:
        with request.urlopen(request.Request(TOKEN_URL, data=body,
                             headers={"Content-Type": "application/x-www-form-urlencoded"}), timeout=60) as r:
            return json.load(r)["access_token"]
    except error.HTTPError as e:
        sys.exit(f"換 token 失敗 HTTP {e.code}：{e.read()[:300].decode('utf-8','replace')}\n"
                 "檢查：service account JSON 是否完整、系統時間是否正確、Search Console API 是否已在該 Cloud 專案啟用。")

def get_token(a):
    if a.sa or os.environ.get("GSC_SA_JSON"):
        return sa_token(a.sa or os.environ["GSC_SA_JSON"])
    if os.environ.get("GSC_ACCESS_TOKEN"):
        return os.environ["GSC_ACCESS_TOKEN"]
    sys.exit("沒有憑證：給 --sa <service account JSON>，或設 GSC_SA_JSON / GSC_ACCESS_TOKEN。設定步驟見 references/setup.md。")

def api_call(url, token, body=None):
    req = request.Request(url, data=json.dumps(body).encode() if body is not None else None,
                          headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"})
    try:
        with request.urlopen(req, timeout=120) as r:
            return json.load(r)
    except error.HTTPError as e:
        msg = e.read()[:400].decode("utf-8", "replace")
        hint = ""
        if e.code == 403: hint = "\n403 通常是 service account 沒被加進 GSC 資源（設定 → 使用者和權限 → 新增，Restricted 即可），或 site 寫法不對（sc-domain:example.com 與 https://example.com/ 是不同資源，用 --list-sites 看）。"
        if e.code == 429: hint = "\n429 配額用完，等一分鐘再跑，或減少 --days 與維度。"
        sys.exit(f"GSC API HTTP {e.code}：{msg}{hint}")

def query(token, site, start, end, dims, search_type, country=None):
    rows, start_row = [], 0
    while True:
        body = {"startDate": start, "endDate": end, "dimensions": dims, "rowLimit": PAGE,
                "startRow": start_row, "dataState": "final", "type": search_type}
        if country:
            body["dimensionFilterGroups"] = [{"filters": [{"dimension": "country", "operator": "equals", "expression": country}]}]
        data = api_call(API.format(site=parse.quote(site, safe="")), token, body)
        batch = data.get("rows", [])
        rows += [{"keys": b["keys"], "clicks": b["clicks"], "impressions": b["impressions"],
                  "ctr": b["ctr"], "position": b["position"]} for b in batch]
        if len(batch) < PAGE or start_row >= PAGE * 3:   # 最多 4 頁 10 萬列，夠用
            break
        start_row += PAGE
    return rows

def pull_period(token, a, start, end, with_qp=True):
    out = {"start": start, "end": end}
    for name, dims in DIMS.items():
        if name == "query_page" and not with_qp: continue
        out[name] = query(token, a.site, start, end, dims, a.search_type, a.country)
        print(f"  {start}～{end} {name}: {len(out[name])} 列", file=sys.stderr)
    return out

# ---------- CSV（介面匯出） ----------
FILE_MAP = [("query", r"quer|查詢|搜尋字詞"), ("page", r"page|網頁|頁面"), ("country", r"countr|國家"),
            ("device", r"device|裝置"), ("date", r"date|日期")]

def num(s):
    s = str(s).strip().replace(",", "").replace("%", "").replace("％", "")
    try: return float(s)
    except ValueError: return 0.0

def read_csv_dir(d):
    out = {}
    for path in glob.glob(os.path.join(d, "*.csv")):
        base = os.path.basename(path).lower()
        kind = next((k for k, pat in FILE_MAP if re.search(pat, base)), None)
        if not kind: continue
        with open(path, encoding="utf-8-sig", newline="") as f:
            rd = csv.reader(f); header = next(rd, None)
            if not header: continue
            def col(pat):
                for i, h in enumerate(header):
                    if re.search(pat, h, re.I): return i
                return None
            ci, ii, ri, pi = col(r"click|點擊"), col(r"impress|曝光"), col(r"ctr|點閱|點擊率"), col(r"position|排名|位置|名次")
            if ci is None or ii is None: continue
            rows = []
            for r in rd:
                if not r or not r[0].strip(): continue
                clicks, impr = num(r[ci]), num(r[ii])
                ctr = num(r[ri]) / 100 if ri is not None else (clicks / impr if impr else 0)
                rows.append({"keys": [r[0].strip()], "clicks": clicks, "impressions": impr,
                             "ctr": ctr, "position": num(r[pi]) if pi is not None else 0})
            out[kind] = rows
    if "query" not in out and "page" not in out:
        sys.exit(f"{d} 裡找不到 Queries.csv / Pages.csv（或中文檔名）。請解壓 GSC 匯出的 zip 後指向該資料夾。")
    return out

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--site", help="sc-domain:example.com 或 https://example.com/")
    ap.add_argument("--sa", help="service account JSON 路徑")
    ap.add_argument("--list-sites", action="store_true")
    ap.add_argument("--days", type=int, default=28, help="本期天數（預設 28；季檢用 90）")
    ap.add_argument("--end", help="本期結束日 YYYY-MM-DD（預設今天 − 3 天）")
    ap.add_argument("--start", help="CSV 模式：本期開始日")
    ap.add_argument("--country", help="ISO 3166-1 alpha-3 小寫，如 twn、usa、jpn")
    ap.add_argument("--search-type", default="web", choices=["web", "image", "video", "news", "discover"])
    ap.add_argument("--yoy", action="store_true", help="另拉去年同期（季節性比較）")
    ap.add_argument("--from-csv", help="GSC 介面匯出資料夾（本期）")
    ap.add_argument("--prev-csv", help="GSC 介面匯出資料夾（前期）")
    ap.add_argument("--out", default="seo-ops/data")
    a = ap.parse_args()

    if a.list_sites:
        token = get_token(a)
        for s in api_call(SITES_API, token).get("siteEntry", []):
            print(f"{s['siteUrl']}\t{s['permissionLevel']}")
        return

    end = dt.date.fromisoformat(a.end) if a.end else dt.date.today() - dt.timedelta(days=3)
    result = {"site": a.site, "search_type": a.search_type, "country_filter": a.country,
              "pulled_at": dt.datetime.now().isoformat(timespec="seconds"), "source": None}

    if a.from_csv:
        if not a.start: sys.exit("CSV 模式要給 --start 與 --end（匯出時選的區間）。")
        start = dt.date.fromisoformat(a.start)
        cur = read_csv_dir(a.from_csv); cur.update({"start": a.start, "end": end.isoformat()})
        result["source"] = "csv"; result["current"] = cur
        if a.prev_csv:
            days = (end - start).days + 1
            prev = read_csv_dir(a.prev_csv)
            prev.update({"start": (start - dt.timedelta(days=days)).isoformat(), "end": (start - dt.timedelta(days=1)).isoformat()})
            result["previous"] = prev
    else:
        if not a.site: sys.exit("API 模式要給 --site。")
        token = get_token(a)
        cur_start = end - dt.timedelta(days=a.days - 1)
        prev_end = cur_start - dt.timedelta(days=1); prev_start = prev_end - dt.timedelta(days=a.days - 1)
        result["source"] = "api"
        print(f"拉 {a.site} 本期 {cur_start}～{end}、前期 {prev_start}～{prev_end}", file=sys.stderr)
        result["current"] = pull_period(token, a, cur_start.isoformat(), end.isoformat())
        result["previous"] = pull_period(token, a, prev_start.isoformat(), prev_end.isoformat(), with_qp=False)
        if a.yoy:
            ys, ye = cur_start.replace(year=cur_start.year - 1), end.replace(year=end.year - 1)
            result["yoy"] = pull_period(token, a, ys.isoformat(), ye.isoformat(), with_qp=False)

    out_dir = os.path.join(a.out, end.isoformat()); os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "gsc.json")
    json.dump(result, open(path, "w", encoding="utf-8"), ensure_ascii=False)
    print(path)

if __name__ == "__main__":
    main()
