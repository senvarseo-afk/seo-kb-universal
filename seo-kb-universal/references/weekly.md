# weekly：週檢（30 分鐘）

目標：知道有沒有掉、掉在哪；挑出 ≤ 5 頁改標題、≤ 5 頁查衰退；記進 action-log。不做研究、不做大改。對應 13 §13.9.1 每週列與 §13.10.2 週報。

## 步驟

1. `ops_calendar.py next` 確認到期；若 monthly 或 quarterly 同時到期，改走那份指引（它們包含週檢）。
2. 拉資料並分析（28 天 vs 前 28 天；資料延遲 2–3 天是正常的）：
   ```bash
   S="<SKILL_DIR>/scripts"; O=<專案>/seo-ops
   python3 $S/gsc_pull.py --site <資源> --sa <sa.json> [--country <國碼>] --days 28 --out $O/data
   python3 $S/kw_analyze.py $O/data/<日期>/gsc.json --config $O/config.json --master $O/keyword-master.csv --out $O/reports --append-log $O/action-log.csv
   ```
3. 讀報告第 1 節（總覽與告警）：
   - 單日 −30% 觸發 → 先看 GSC 介面「上次更新」是否超過 48 小時（13 §13.1.1），再看 status.search.google.com 有無更新中，然後 `diagnose 子指令`。本 skill 到此為止。
   - 某國 −20% → 拆該國 Pages × Queries；多國站各國走勢常不同步（13 §13.1.1）。
   - 2026-11 起有站回報點擊異常暴增而曝光持平，先對照 GA4 再當真（13 §13.1.1）。
4. 讀第 4 節（標題佇列）：挑曝光最高 ≤ 5 頁。每頁先手機無痕看目標國家 SERP：本站在首屏還是摺疊下、Google 顯示的標題是否被改寫（05 §1.2）、SERP 有無 AIO / 論壇區塊。結構性壓縮的不改標題（12 B6）；其餘重寫 title 與 description（05 §1、§2），寫進 `title-test-log.csv`（baseline 用報告數字，check_date = +28 天）。
5. 讀第 5 節（衰退頁）：「排名下滑」類查 SERP 是否變了（02 §13.1 B）；「排名沒掉點擊掉」類看 SERP 功能與標題（12 C3）。只記錄與排程，不當週大改。
6. 第 3 節（衝刺區）與第 6 節（新查詢）只掃一眼，留給月研究。
7. 到期的標題測試（title-test-log 的 check_date ≤ 今天）：從本期報告或 GSC 填 result_*；排名下滑 > 1 位 → 回滾；CTR 升 → 保留並寫 verdict。
8. `action-log.csv` 把做完的改 status 與 done_date。`ops_calendar.py done weekly --note "..."`。

## 週報 SEO 段落（給 13 §13.10.2 的第 1、2、6 項）

```
本週 vs 上週（28 天滾動）：點擊 N（±x%）、曝光 N（±x%）、CTR x%（±x pt）、位置 x.x；主要國家：PH ±x%、…
成長頁 Top 5 / 衰退頁 Top 5：URL、點擊差、主要查詢（報告第 5 節）
本週動作：改 title N 頁（列 URL）、排程更新 N 頁；下週：…
外部事件：Google 更新 / 季節 / 競爭者（有才寫）
```

## 判讀提醒

- 報告的「同位置中位數」是本站自己算的，站小（查詢 < 200 筆）時中位數不穩，標題佇列只當參考。
- 不要把查詢加總跟頁面加總互比（匿名化），也不要把圖表平均位置跟表格互比（13 §13.1.1）。
- 新站前 3 個月週檢重點是索引與曝光是否逐週上升（01 §3.2），標題佇列多半還沒意義。
