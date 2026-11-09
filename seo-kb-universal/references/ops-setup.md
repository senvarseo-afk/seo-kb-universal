# setup：替一個站建立關鍵字優化例行

目標：專案資料夾裡有 `seo-ops/`，GSC 取得到資料，第一份基線報告（季檢規格）產出，13 週時程排好。約 1 小時（不含等 Google Cloud 權限生效）。

## 步驟

1. 問或確認：專案資料夾、GSC 資源寫法（`sc-domain:example.com` 網域資源，或 `https://example.com/` 網址前置字元資源；兩者是不同資源）、主要市場國碼（ISO 3166-1 alpha-3 小寫，如 twn、usa、jpn）、品牌字 regex、sitemap 網址、每週例行日。
2. 選取數方式：
   - **A. API（建議，可自動化）**：
     1. Google Cloud 建專案 → 啟用 **Google Search Console API**。
     2. IAM → 服務帳戶 → 建立 → 金鑰 → JSON，存到 `~/keys/<站名>-gsc-sa.json`（chmod 600，不進 repo）。
     3. GSC → 設定 → 使用者和權限 → 新增該 service account 的 email，權限 **受限（Restricted）** 即可（唯讀 scope `webmasters.readonly`）。
     4. 驗證：`python3 $S/gsc_pull.py --sa ~/keys/<站名>-gsc-sa.json --list-sites`，要看到該資源與 `siteRestrictedUser` 或以上。
     - 專案若已有其他用途的 service account（如 GA4 拉取），可直接沿用，只要加進 GSC 權限。
   - **B. CSV 匯出（沒有 API 時）**：GSC 成效 → 篩選日期（28 天）與「比較」關閉 → 右上匯出 → 下載 zip → 解壓成一個資料夾；前期再匯一次放另一個資料夾。限制：1,000 列、無查詢 × 網頁維度（13 §13.1.12）。
   - **C. 多站 / 要 16 個月以上**：開 Bulk data export 到 BigQuery（13 §13.1.12），本 skill 暫不讀 BigQuery，之後要接再加。
3. 建資料夾與時程：
   ```bash
   S="<SKILL_DIR>/scripts"
   python3 $S/ops_calendar.py init --site <資源> --out <專案>/seo-ops --project <站名> --brand "<regex>" --country <國碼> --sa ~/keys/<站名>-gsc-sa.json --sitemap <sitemap url> --weekday 0
   ```
4. 基線（季檢規格，之後每 13 週一次）：
   ```bash
   python3 $S/gsc_pull.py --site <資源> --sa ~/keys/<站名>-gsc-sa.json --country <國碼> --days 90 --yoy --out <專案>/seo-ops/data
   python3 $S/kw_analyze.py <專案>/seo-ops/data/<日期>/gsc.json --config <專案>/seo-ops/config.json --grade --out <專案>/seo-ops/reports --append-log <專案>/seo-ops/action-log.csv
   python3 $S/ops_calendar.py done quarterly --out <專案>/seo-ops --note "基線"
   ```
   新站（上線 < 90 天）資料少：`--days 28`，分級那節只看 A 與標題佇列，D 級等 6 個月後再算（02 §13.1）。
5. 把既有關鍵字研究（若有 P1 階段的母表、主題地圖）轉進 `keyword-master.csv`，欄位依 02 §2 驗收：keyword、volume、kd、cpc、intent、format、serp_features、cluster、hub、score、status、url。沒有就留空，月研究會從 GSC 新查詢開始填。
6. 專案 `CLAUDE.md` 加一行指向本 skill 與 `seo-ops/`。若要自動化週拉取，走專案自己的排程（GitHub Actions 或雲端排程 Claude），本 skill 只提供腳本。

## 判讀提醒

- `--list-sites` 403 或空清單：service account 還沒被加進 GSC，或加錯資源（網域 vs 網址前置字元）。權限加完幾分鐘內生效。
- 換 token 失敗：檢查系統時間、JSON 是否完整、API 是否啟用。
- `--country` 只在主要市場明確時用；多國站先不篩，報告第 1 節會列國家拆分。
- 目標市場是台灣時先讀 24 章速查，其他市場用 25 章框架評估；在地語言或混語查詢的處理方式寫進 config 的 note（02 §10、10 §5）。
