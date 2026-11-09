#!/usr/bin/env python3
"""關鍵字優化例行的時程管理：建立專案的 seo-ops 資料夾、產 13 週時程、告訴你今天該跑哪個例行、記錄完成。

  ops_calendar.py init --site sc-domain:example.com --out seo-ops [--project 名稱] [--start 2026-11-10] [--weekday 0]
                       [--brand "regex"] [--country twn] [--sa ~/keys/gsc-sa.json] [--sitemap https://example.com/sitemap.xml]
  ops_calendar.py next --out seo-ops                 # 到期 / 過期的例行與該跑的指令
  ops_calendar.py done weekly|monthly|quarterly|research --out seo-ops [--note "..."]
  ops_calendar.py schedule --out seo-ops [--weeks 13] # 重產 ops-plan.md 的時程表

節奏（13 §13.9.1、02 §8、§13、14 §F）：
  weekly    每週固定一天（預設週一）：拉 GSC、看告警、衰退頁、標題佇列各 ≤ 5 條。30 分鐘。
  monthly   每月第一個 weekly 槽：新查詢進母表、SERP 分析、評分、排下月日曆（20% 產能給更新）。2 小時。
  quarterly 每 13 週：內容 A–E 分級、母表重新評分（季節係數）、蠶食稽核、競爭者矩陣。半天。
  research  不定期：新 hub 的 8 步關鍵字研究（02 §2）。
"""
import sys, os, json, argparse, shutil
import datetime as dt

HERE = os.path.dirname(os.path.abspath(__file__))
TPL = os.path.join(os.path.dirname(HERE), "templates")
ROUTINES = ["weekly", "monthly", "quarterly", "research"]
WD = "一二三四五六日"

def load(out):
    p = os.path.join(out, "config.json")
    if not os.path.exists(p): sys.exit(f"找不到 {p}，先跑 ops_calendar.py init。")
    return json.load(open(p, encoding="utf-8")), p

def save(cfg, p): json.dump(cfg, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

def slots(start, weekday, weeks):
    """從 start 起第一個 weekday 開始，每週一個槽；回傳 [(date, {'W','M','Q'})]"""
    d = start + dt.timedelta(days=(weekday - start.weekday()) % 7)
    out, seen_months = [], set()
    for i in range(weeks):
        tags = {"W"}
        ym = (d.year, d.month)
        if ym not in seen_months: seen_months.add(ym); tags.add("M")
        if i % 13 == 0: tags.add("Q")
        out.append((d, tags)); d += dt.timedelta(days=7)
    return out

def schedule_md(cfg, weeks):
    start = dt.date.fromisoformat(cfg["start"]); rows = ["| 週 | 日期 | 例行 | 內容 |", "|---|---|---|---|"]
    names = {"W": "週檢", "M": "月研究", "Q": "季檢"}
    desc = {"Q": "A–E 分級、母表重評分、蠶食稽核、競爭者矩陣", "M": "新查詢進母表、SERP 分析、評分、下月日曆", "W": "拉 GSC、告警、衰退、標題佇列"}
    for i, (d, tags) in enumerate(slots(start, cfg["weekday"], weeks), 1):
        order = [t for t in ("Q", "M", "W") if t in tags]
        rows.append(f"| {i} | {d.isoformat()} | {' + '.join(names[t] for t in order)} | {'；'.join(desc[t] for t in order)} |")
    return "\n".join(rows)

def write_plan(cfg, out, weeks=13):
    p = os.path.join(out, "ops-plan.md")
    src = p if os.path.exists(p) else os.path.join(TPL, "ops-plan.md")
    tpl = open(src, encoding="utf-8").read()
    table = schedule_md(cfg, weeks)
    s, e = "<!-- schedule:start -->", "<!-- schedule:end -->"
    if s in tpl and e in tpl:
        tpl = tpl[:tpl.index(s) + len(s)] + "\n" + table + "\n" + tpl[tpl.index(e):]
    repl = {"{{site}}": cfg["site"], "{{project}}": cfg.get("project", ""), "{{start}}": cfg["start"],
            "{{weekday}}": WD[cfg["weekday"]], "{{country}}": cfg.get("market_country") or "全部",
            "{{brand}}": cfg.get("brand_regex") or "（未設）", "{{out}}": out}
    for k, v in repl.items(): tpl = tpl.replace(k, str(v))
    open(p, "w", encoding="utf-8").write(tpl)
    return p

def cmd_init(a):
    os.makedirs(os.path.join(a.out, "data"), exist_ok=True); os.makedirs(os.path.join(a.out, "reports"), exist_ok=True)
    cfg_p = os.path.join(a.out, "config.json")
    if os.path.exists(cfg_p) and not a.force: sys.exit(f"{cfg_p} 已存在，加 --force 覆寫（runs 會保留）。")
    old = json.load(open(cfg_p, encoding="utf-8")) if os.path.exists(cfg_p) else {}
    project = a.project or os.path.basename(os.path.abspath(os.path.join(a.out, os.pardir)))
    cfg = {"site": a.site, "project": project, "market_country": a.country, "search_type": "web",
           "brand_regex": a.brand, "sa_json": a.sa, "sitemap": a.sitemap, "weekday": a.weekday,
           "start": a.start or dt.date.today().isoformat(), "days_weekly": 28, "days_quarterly": 90,
           "runs": old.get("runs", {r: [] for r in ROUTINES})}
    save(cfg, cfg_p)
    for f in ("keyword-master.csv", "action-log.csv", "title-test-log.csv", "serp-analysis.md"):
        dst = os.path.join(a.out, f)
        if not os.path.exists(dst): shutil.copy(os.path.join(TPL, f), dst)
    plan = write_plan(cfg, a.out)
    print(f"已建立 {a.out}/：config.json、ops-plan.md、keyword-master.csv、action-log.csv、title-test-log.csv、serp-analysis.md、data/、reports/")
    print(f"時程表在 {plan}。下一步：ops_calendar.py next --out {a.out}")

def first_slot_of_month(year, month, wd):
    d = dt.date(year, month, 1); return d + dt.timedelta(days=(wd - d.weekday()) % 7)

def due_info(cfg, today):
    start = dt.date.fromisoformat(cfg["start"]); wd = cfg["weekday"]
    this_slot = today - dt.timedelta(days=(today.weekday() - wd) % 7)
    runs = {r: [dt.date.fromisoformat(x["date"]) for x in cfg["runs"].get(r, [])] for r in ROUTINES}
    last = {r: (max(v) if v else None) for r, v in runs.items()}
    info = {}
    # weekly：本週槽還沒做就到期
    if last["weekly"] is None or last["weekly"] < this_slot: nxt = max(this_slot, start)
    else: nxt = this_slot + dt.timedelta(days=7)
    info["weekly"] = (last["weekly"], nxt)
    # monthly：本月第一個槽；本月做過就排下月
    fs = first_slot_of_month(today.year, today.month, wd)
    done_this_month = last["monthly"] is not None and (last["monthly"].year, last["monthly"].month) == (today.year, today.month)
    if done_this_month or (today < fs and last["monthly"] is not None):
        ny, nm = (today.year + 1, 1) if today.month == 12 else (today.year, today.month + 1)
        info["monthly"] = (last["monthly"], first_slot_of_month(ny, nm, wd) if done_this_month else fs)
    else:
        info["monthly"] = (last["monthly"], max(fs, start))
    # quarterly：首次立刻（基線），之後每 91 天
    if last["quarterly"] is None: info["quarterly"] = (None, start)
    else: info["quarterly"] = (last["quarterly"], last["quarterly"] + dt.timedelta(days=91))
    info["research"] = (last["research"], None)
    return info

def cmd_next(a):
    cfg, _ = load(a.out); today = dt.date.today(); info = due_info(cfg, today)
    print(f"今天 {today.isoformat()}（週{WD[today.weekday()]}），專案 {cfg.get('project')}，資源 {cfg['site']}\n")
    print("| 例行 | 上次 | 下次 | 狀態 |\n|---|---|---|---|")
    due = []
    for r in ROUTINES:
        last, nxt = info[r]
        if r == "research": st = "不定期（新 hub 時）"
        elif nxt <= today:
            over = (today - nxt).days; st = "**到期**" if over == 0 else f"**過期 {over} 天**"; due.append(r)
        else: st = f"未到（{(nxt - today).days} 天後）"
        print(f"| {r} | {last.isoformat() if last else '從未'} | {nxt.isoformat() if nxt else '—'} | {st} |")
    S = HERE; o = a.out
    sa = f" --sa {cfg['sa_json']}" if cfg.get("sa_json") else ""
    c = f" --country {cfg['market_country']}" if cfg.get("market_country") else ""
    print()
    if not due: print("沒有到期的例行。"); return
    print("該跑的（依序）：")
    common = f"--config {o}/config.json --master {o}/keyword-master.csv --out {o}/reports --append-log {o}/action-log.csv"
    if "quarterly" in due:
        print(f"  季檢（references/quarterly.md）：")
        print(f"    python3 {S}/gsc_pull.py --site {cfg['site']}{sa}{c} --days {cfg.get('days_quarterly', 90)} --yoy --out {o}/data")
        print(f"    python3 {S}/kw_analyze.py {o}/data/<日期>/gsc.json {common} --grade")
    if "monthly" in due or "weekly" in due:
        label = "月研究（references/monthly.md）" if "monthly" in due else "週檢（references/weekly.md）"
        print(f"  {label}：")
        print(f"    python3 {S}/gsc_pull.py --site {cfg['site']}{sa}{c} --days {cfg.get('days_weekly', 28)} --out {o}/data")
        print(f"    python3 {S}/kw_analyze.py {o}/data/<日期>/gsc.json {common}")
    print(f"  做完：python3 {S}/ops_calendar.py done <{'|'.join(due)}> --out {o}")

def cmd_done(a):
    cfg, p = load(a.out); today = dt.date.today().isoformat()
    cfg["runs"].setdefault(a.routine, []).append({"date": today, "note": a.note or ""})
    save(cfg, p)
    plan = os.path.join(a.out, "ops-plan.md")
    if os.path.exists(plan):
        with open(plan, "a", encoding="utf-8") as f: f.write(f"\n- {today} {a.routine}：{a.note or '完成'}")
    print(f"已記錄 {a.routine} 於 {today}。")

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd")
    i = sub.add_parser("init"); i.add_argument("--site", required=True); i.add_argument("--out", default="seo-ops"); i.add_argument("--project")
    i.add_argument("--start"); i.add_argument("--weekday", type=int, default=0, help="0=週一 … 6=週日"); i.add_argument("--brand"); i.add_argument("--country")
    i.add_argument("--sa"); i.add_argument("--sitemap"); i.add_argument("--force", action="store_true")
    n = sub.add_parser("next"); n.add_argument("--out", default="seo-ops")
    d = sub.add_parser("done"); d.add_argument("routine", choices=ROUTINES); d.add_argument("--out", default="seo-ops"); d.add_argument("--note")
    s = sub.add_parser("schedule"); s.add_argument("--out", default="seo-ops"); s.add_argument("--weeks", type=int, default=13)
    a = ap.parse_args()
    if not a.cmd: ap.print_help(); sys.exit(1)
    if a.cmd == "init": cmd_init(a)
    elif a.cmd == "next": cmd_next(a)
    elif a.cmd == "done": cmd_done(a)
    else:
        cfg, _ = load(a.out); print(write_plan(cfg, a.out, a.weeks))

if __name__ == "__main__":
    main()
