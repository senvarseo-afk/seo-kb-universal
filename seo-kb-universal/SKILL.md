---
name: seo-kb-universal
description: "SEO 知識庫執行器，內含 25 章規範、狀況解法手冊、台灣市場速查、通用市場評估框架、AdSense 與 Google Ads 規範，用來啟動網站專案、稽核網站、診斷流量問題、評估新市場與審稿。只要任務碰到 SEO、網站上線或改版、流量下降、Google Search Console、AdSense、Discover、AEO、GEO、AI Overviews、hreflang 多語言、台灣市場、繁體中文 SEO、海外市場評估、內容站、流量站、程序化 SEO、關鍵字與標題、結構化資料、Core Web Vitals，即使使用者沒有說「知識庫」或「SEO」，也要用這個 skill，先查知識庫再回答並標明章節。Use for any SEO, site audit, traffic drop, AdSense or AI search task."
metadata:
  version: "1.0.0"
  kb_version: "1.5-universal (2026-11-06)"
---

# SEO 知識庫執行器

這個 skill 是知識庫的「路由器加工具箱」。知識庫有二十多萬字，放在 `references/kb/`，不要整份載入；依任務只讀該讀的小節，用腳本做可自動化的檢查，回答時標明章節。

下文的 `<SKILL_DIR>` 指這個 skill 的根目錄，也就是載入時顯示的 base directory。執行指令時換成實際路徑，路徑有空格時要加引號。

預設情境是靠廣告或聯盟變現的內容站，但規範適用各類網站，不限特定國家。除了台灣（24 章），知識庫沒有個別國家的市場數據，遇到其他市場要先查證，不要用別國數字推估。回覆使用者慣用的語言；知識庫原文是繁體中文，技術名詞保留英文。

## 鐵則

1. **先讀再答**：先用 `kb_lookup.py` 抓對應小節，再回答；不要憑記憶回答知識庫已涵蓋的問題。讀 `00-快速啟動指南.md` 的對應段落（§2 閱讀路徑、§4 數值速查、§6 症狀表）通常就能定位。
2. **註明出處**：回答寫明章節與小節，例如「依 04 §5」「12 H5」。
3. **分清證據等級**：知識庫把內容分成官方證實、社群共識（標「社群主張」）、待查證。輸出時保留這個標示，不把社群主張講成確定機制。
4. **時效**：內容查證至 2026-11-06。政策、門檻、工具功能類內容若距今超過 90 天，先用可用的網路工具查證官方來源；無法查證時要明說這是當時的內容。
5. **遇到知識庫沒有的狀況**：解決後依第 12 章的結構（症狀、可能原因、診斷步驟、解法、預防、預估恢復時間、證據等級）整理給使用者。只有使用者要求時才修改 `references/kb/`。

## 子指令路由

使用者的第一個參數決定流程，對應 `references/` 裡的一份作業指引。讀該指引後照做；沒有參數時，依使用者描述判斷最接近的一種，並說明你選了哪個。

| 子指令 | 用途 | 讀這份指引 | 主要工具 |
|---|---|---|---|
| `start <專案類型> [市場]` | 新專案啟動：複製啟動表、列閱讀路徑、給前兩週行動 | `references/start.md` | kb_lookup |
| `check <url> [url...]` | 上線前、改版後、季稽核：跑技術稽核與 CWV，補人工項目，產出報告 | `references/check.md` | site_audit、cwv、report |
| `diagnose <症狀或描述>` | 流量掉、沒索引、CTR 低、AdSense 警示等：走症狀表與第 12 章決策樹 | `references/diagnose.md` | kb_lookup --symptom |
| `market <國家>` | 評估台灣或任何市場；台灣看 24 章，其他市場用 25 章框架 | `references/market.md` | kb_lookup --section |
| `review <檔案或 url>` | 單篇審稿：標題、答案優先、E-E-A-T、政策、混語、AdSense 內容政策 | `references/review.md` | kb_lookup、site_audit --no-extra |
| `lookup <關鍵字或章節>` | 直接查知識庫 | 本檔下方「查詢工具」 | kb_lookup |

## 查詢工具

```bash
python3 "<SKILL_DIR>/scripts/kb_lookup.py" <關鍵字...>             # 全文搜尋，回傳章節 §小節與前後行
python3 "<SKILL_DIR>/scripts/kb_lookup.py" --section "24 §6"       # 印出某小節全文；第 12 章用狀況編號，如 "12 H5"
python3 "<SKILL_DIR>/scripts/kb_lookup.py" --symptom 收錄 # 查 00 §6 症狀表
python3 "<SKILL_DIR>/scripts/kb_lookup.py" --toc 22                # 某章目錄
```

先用 `--symptom` 或 `--toc` 定位，再用 `--section` 讀整節；全文搜尋只用來找不知道在哪章的東西。一次讀三到五個小節，超過就表示任務太大，應拆開處理。

無法執行腳本時，直接讀 `references/kb/` 下的章節檔。檔案很大，先用搜尋定位再讀片段。

## 稽核工具

```bash
python3 "<SKILL_DIR>/scripts/site_audit.py" <url> [--json audit.json] [--hreflang-check]   # 技術檢查
python3 "<SKILL_DIR>/scripts/cwv.py" <url> [--desktop] [--json cwv.json]                   # PageSpeed Insights，CrUX 與實驗室值
python3 "<SKILL_DIR>/scripts/report.py" --audit audit.json --cwv cwv.json --out 報告.md    # 填稽核報告結構
```

- 只需要 Python 3.9 以上，不用安裝套件。
- 這些腳本要能連上目標網站。環境不能連外時要告知使用者，改請對方貼上 HTML 或改用其他方式檢查。
- `cwv.py` 的匿名額度常用完，遇到 HTTP 429 不要重試。請使用者設定環境變數 `PSI_API_KEY`，它要到 Google Cloud 免費申請。
- 腳本只做可自動化的技術檢查：狀態碼與轉址、HTTPS 與安全標頭、robots 與 sitemap、canonical、hreflang、title、meta、H1、meta robots、JSON-LD、圖片屬性、AdSense 與 ads.txt、主要文字系統是否在 AdSense 支援語言清單、CWV。內容品質、E-E-A-T、政策、選題紅線與流量根因，要照指引讀知識庫判斷。

## 輸出格式通則

- 結論先行，再給依據與章節。
- 檢查類輸出用三欄表：項目｜結果（通過、未通過、注意、人工判定）｜章節。未通過的項目要附知識庫裡的「怎麼做」。
- 數字來自 00 §4 數值速查或各章，不自己編門檻。RPM、渠道排名、AEO 優先順序這類社群主張要標「社群主張」。
- 要寫檔時放在使用者的專案資料夾，不放在 skill 目錄裡。
- 建議涉及賭博、金融、醫療等敏感主題時，要如實指出法律與平台政策風險。
