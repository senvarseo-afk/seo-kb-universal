---
name: seo-kb-universal
description: "SEO 知識庫執行器，內含 26 章規範、狀況解法手冊、台灣市場速查、通用市場評估框架、AdSense、Google Ads 與社群廣告規範，加上用 Google Search Console 資料跑的關鍵字持續優化例行（週檢、月研究、季檢、內容 A–E 分級、研究時程）。用來啟動網站專案、稽核網站、診斷流量問題、評估新市場、審稿、決定這週該改哪些標題與更新哪些文章。只要任務碰到 SEO、網站上線或改版、流量下降、Google Search Console、GSC 查詢 / 曝光 / CTR、關鍵字研究或優化、內容更新與汰舊、AdSense、Facebook / Instagram / TikTok 投廣、廣告帳號停權、Discover、AEO、GEO、AI Overviews、hreflang 多語言、台灣市場、繁體中文 SEO、海外市場評估、內容站、流量站、程序化 SEO、關鍵字與標題、結構化資料、Core Web Vitals，即使使用者沒有說「知識庫」或「SEO」，也要用這個 skill，先查知識庫再回答並標明章節。Use for any SEO, site audit, traffic drop, keyword ops, Search Console analysis, AdSense or AI search task."
metadata:
  version: "1.2.0"
  kb_version: "1.6-universal (2026-11-09)"
---

# SEO 知識庫執行器

這個 skill 是知識庫的「路由器加工具箱」。知識庫有二十多萬字，放在 `references/kb/`，不要整份載入；依任務只讀該讀的小節，用腳本做可自動化的檢查，回答時標明章節。

下文的 `<SKILL_DIR>` 指這個 skill 的根目錄，也就是載入時顯示的 base directory。執行指令時換成實際路徑，路徑有空格時要加引號。

預設情境是靠廣告或聯盟變現的內容站，但規範適用各類網站，不限特定國家。除了台灣（24 章），知識庫沒有個別國家的市場數據，遇到其他市場要先查證，不要用別國數字推估。回覆使用者慣用的語言；知識庫原文是繁體中文，技術名詞保留英文。

## 鐵則

1. **先讀再答**：先用 `kb_lookup.py` 抓對應小節，再回答；不要憑記憶回答知識庫已涵蓋的問題。讀 `00-快速啟動指南.md` 的對應段落（§2 閱讀路徑、§4 數值速查、§6 症狀表）通常就能定位。
2. **註明出處**：回答寫明章節與小節，例如「依 04 §5」「12 H5」。
3. **分清證據等級**：知識庫把內容分成官方證實、社群共識（標「社群主張」）、待查證。輸出時保留這個標示，不把社群主張講成確定機制。
4. **時效**：內容查證至 2026-11-09。政策、門檻、工具功能類內容若距今超過 90 天，先用可用的網路工具查證官方來源；無法查證時要明說這是當時的內容。
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
| `ops setup <專案資料夾> <GSC 資源>` | 第一次替某站建立關鍵字優化例行：GSC 取數、seo-ops 資料夾、13 週時程、基線報告 | `references/ops-setup.md` | ops_calendar init、gsc_pull --list-sites |
| `ops next [專案資料夾]` | 「這週 / 今天 SEO 要做什麼」：列到期例行與完整指令 | 本檔「關鍵字持續優化例行」 | ops_calendar next |
| `ops weekly [專案資料夾]` | 每週 30 分鐘：告警、衰退頁、標題佇列 | `references/weekly.md` | gsc_pull、kw_analyze |
| `ops monthly [專案資料夾]` | 每月 2 小時：新查詢進母表、SERP 分析、評分、蠶食、下月日曆 | `references/monthly.md` | gsc_pull、kw_analyze --master |
| `ops quarterly [專案資料夾]` | 每 13 週半天：內容 A–E 分級與汰舊、母表重評分、季節字 | `references/quarterly.md` | gsc_pull --days 90 --yoy、kw_analyze --grade |
| `ops research <hub 或種子>` | 新 hub、新站、新市場的 8 步關鍵字研究 | `references/research.md` | kb_lookup（02 §2–§8）、母表 |

`ops` 沒給第二個參數時：專案還沒有 `seo-ops/` 就走 setup；有就先 next 看到期哪個，再進該例行。使用者直接問「哪些文章該更新」「標題怎麼改」「GSC 冒出哪些新字」也屬於 ops。

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

## 關鍵字持續優化例行（ops）

把「看 GSC → 決定做什麼 → 做 → 回看」變成固定節奏。三支腳本抓資料、算清單、管時程；判斷門檻全部來自知識庫，腳本已內建，不要另外發明。

```bash
S="<SKILL_DIR>/scripts"; O=<專案>/seo-ops
python3 "$S/ops_calendar.py" init --site sc-domain:example.com --out $O --project <站名> --brand "<品牌 regex>" --country <國碼> --sa ~/keys/gsc-sa.json --sitemap <sitemap url>
python3 "$S/ops_calendar.py" next --out $O                      # 到期例行 + 該跑的完整指令
python3 "$S/gsc_pull.py" --site sc-domain:example.com --sa ~/keys/gsc-sa.json --days 28 --out $O/data      # 本期 + 前期；季檢用 --days 90 --yoy
python3 "$S/gsc_pull.py" --from-csv <GSC 匯出資料夾> --prev-csv <前期匯出> --start <日期> --end <日期> --out $O/data   # 沒有 API 時
python3 "$S/kw_analyze.py" $O/data/<日期>/gsc.json --config $O/config.json --master $O/keyword-master.csv --out $O/reports --append-log $O/action-log.csv [--grade --sitemap <url>]
python3 "$S/ops_calendar.py" done weekly --out $O --note "改了 3 個 title"
```

| 例行 | 頻率 | 時間 | 核心問題 | 知識庫 |
|---|---|---|---|---|
| weekly | 每週固定一天 | 30 分 | 有沒有掉？哪 5 頁該改標題、哪 5 頁在衰退？ | 13 §13.9.1、§13.10.2、12 C3 |
| monthly | 每月第一個週槽 | 2 小時 | GSC 冒出哪些新查詢與缺專頁？母表怎麼排？下月日曆？ | 02 §7、§8、§9、§12 |
| quarterly | 每 13 週（首次在 setup 當天做基線） | 半天 | 全站哪些頁更新 / 合併 / 刪？季節字提前 8–12 週了嗎？ | 02 §11、§13、14 §F |
| research | 不定期 | 1 天 | 新 hub 值不值得做、先做哪 5–8 篇？ | 02 §2–§8 |
| 核心更新後 | 事件 | 2 小時 | 前後各 14 天比較，完成後才下結論 | 07 §7、14 章「演算法更新後」 |

- 門檻：週比 −20%、單日 −30%、CTR −1 個百分點（13 §13.9.1）；衝刺區 5–20 名（02 §13.1）；低 CTR = 低於本站同位置中位數 50%（12 C3）；衰退 = 點擊 −30% 且排名下滑（02 §13.1 B）；蠶食 = 同查詢 ≥ 2 URL 各佔 ≥ 20%（02 §12）；D 級 < 15%（02 §13）。
- 先排除假訊號再行動：GSC 延遲、季節（--yoy）、追蹤壞掉、bot 灌水（12 B3、B4、§12 (11)）。單日告警觸發時走 `diagnose`，不在 ops 裡改站。
- 報告列很多候選，回覆時挑出「最該先做的 3 件」（對象、證據、動作、章節），並列出需要使用者人工判定的項目（SERP 目視、發佈日期、意圖）。
- 更新不改 URL、不只改日期（02 §13.2）；更新前先匯出該頁所有排名查詢（02 §14）；標題改寫一定記 `title-test-log.csv`，28 天後對照（12 C3）。
- `kw_analyze.py` 產 `reports/<日期>-keyword-ops.md`（九節報告）與 `-actions.csv`（行動清單含 due）；`--grade` 時檔名多 `-quarterly` 並另產 `-grades.csv`。`--append-log` 把新行動併進 action-log，同 type+target 不重複。
- GSC 取數：service account JSON 用 openssl 簽 JWT 換 token，只要 Python 3.9 與 openssl，不裝套件；設定步驟在 `references/ops-setup.md`。介面匯出的 CSV 上限 1,000 列且沒有查詢 × 網頁維度，蠶食與缺專頁兩節會略過。
- 專案資料全放使用者專案的 `seo-ops/`（config.json、ops-plan.md、keyword-master.csv、action-log.csv、title-test-log.csv、serp-analysis.md、data/、reports/）；service account JSON 不進 repo。

## 輸出格式通則

- 結論先行，再給依據與章節。
- 檢查類輸出用三欄表：項目｜結果（通過、未通過、注意、人工判定）｜章節。未通過的項目要附知識庫裡的「怎麼做」。
- 數字來自 00 §4 數值速查或各章，不自己編門檻。RPM、渠道排名、AEO 優先順序這類社群主張要標「社群主張」。
- 要寫檔時放在使用者的專案資料夾，不放在 skill 目錄裡。
- 建議涉及賭博、金融、醫療等敏感主題時，要如實指出法律與平台政策風險。
