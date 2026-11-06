# check：網站稽核（上線前、改版後、每季）

目標：用腳本把能自動化的技術項目跑完，再補腳本做不到的人工項目，產出一份對應 KB 章節的稽核報告。

## 步驟

1. 確認範圍：首頁 + 一個主要內容模板頁 + 一個列表頁（至少三個 URL）；多語站各語言各抽一頁。問使用者是「上線前」「改版後」還是「季稽核」，對應 14 章 §A、§G、§F。
2. 跑腳本（在專案資料夾執行，輸出檔留在那裡）：
   ```bash
   S="<SKILL_DIR>/scripts"
   python3 "$S/site_audit.py" <url1> <url2> <url3> --json audit.json [--hreflang-check]
   python3 "$S/cwv.py" <主要內容頁 url> --json cwv.json          # PSI 要 30–60 秒；匿名配額常被用完（HTTP 429），請用 PSI_API_KEY=<key> 執行，金鑰免費：https://developers.google.com/speed/docs/insights/v5/get-started
   python3 "$S/report.py" --audit audit.json --cwv cwv.json --out seo-audit-<日期>.md --site <網站名>
   ```
3. 讀對應清單，逐項補人工判定：
   ```bash
   python3 "<SKILL_DIR>/scripts/kb_lookup.py" --section "14 A"   # 上線前（A1 技術、A2 內容、A3 追蹤）
   python3 "<SKILL_DIR>/scripts/kb_lookup.py" --section "14 G"   # 搬遷 / 改版
   python3 "<SKILL_DIR>/scripts/kb_lookup.py" --section "14 F"   # 每季稽核
   ```
   腳本沒覆蓋、必須人工或用 GSC 的項目（至少確認這些）：GSC 已驗證與索引涵蓋狀況、URL 檢查工具的渲染結果、內部連結深度與孤兒頁（Screaming Frog）、About / 聯絡 / 隱私 / 作者頁存在、無 Lorem ipsum 與空分類頁、CMP 設定（有 EEA 流量時）、07 §4 的政策自查七項。
4. 每個未通過或注意的項目，用 `kb_lookup.py --section` 讀該章節的「怎麼做」，寫進報告的建議做法欄；不要只貼症狀。
5. 若是流量站，依目標市場加查語言合規與技術要點，例如字型與編碼、slug、首屏大小、Discover 大圖。台灣看 24 章，其他市場看 25 章。

## 判讀提醒

- cwv.py 回 429 時不要重試，改請使用者設 PSI_API_KEY，或先用 Chrome DevTools / GSC CWV 報表補。
- CWV 排名用的是 CrUX 真實使用者 p75；新站沒有 CrUX 是正常的，用實驗室值找原因，用 GSC CWV 報表追蹤。
- `site_audit.py` 的「主要文字系統」只是偵測，混語頁要人工判定主要語言（25 §3）。同一種文字可能對應多種語言，要確認實際語言是否在支援清單。
- FAQ / HowTo 的 JSON-LD 仍可放，但 rich result 已退場，不要當成 CTR 手段（06 §2）。
- 報告裡每個數字門檻都來自 00 §4，不要另外發明。

## 輸出格式

直接交付 `report.py` 產出的 Markdown，再在對話中給三行摘要：P1 幾項、最該先做的一件事、哪些項目需要使用者提供 GSC 資料才能判定。
