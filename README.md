# SEO 知識庫 skill

這是一份可直接安裝的 SEO 知識庫 skill，內含 26 章規範、狀況解法手冊、台灣市場速查、通用市場評估框架、AdSense、Google Ads 與社群廣告規範。內容查證至 2026-11-09。

v1.2 起加入「關鍵字持續優化例行」：用 Google Search Console 資料跑週檢、月研究、季檢，產出該改標題、該更新、該合併或汰舊的行動清單，並管理研究時程。

## 安裝

**Claude Code**

1. 下載或 clone 這個 repo。
2. 把 `seo-kb-universal` 資料夾複製到 `~/.claude/skills/`。
3. 開新的 session，就能使用 `/seo-kb-universal`。

**Claude 網頁版或桌面版**

1. 確認帳號已開啟程式碼執行功能。
2. 到 Customize，選 Skills，按「+」，選 Upload a skill。
3. 上傳 Releases 裡的 `seo-kb-universal.zip`。選單名稱可能依版本不同，以畫面為準。

## 怎麼用

| 指令 | 用途 |
|---|---|
| `/seo-kb-universal start 內容站 台灣` | 新專案啟動 |
| `/seo-kb-universal check https://example.com` | 網站稽核 |
| `/seo-kb-universal diagnose 流量突然掉` | 診斷問題 |
| `/seo-kb-universal market 台灣` | 評估市場，其他國家也可以 |
| `/seo-kb-universal review 文章.md` | 審稿 |
| `/seo-kb-universal lookup hreflang` | 查知識庫 |
| `/seo-kb-universal ops setup ./my-site sc-domain:example.com` | 替一個站建立關鍵字優化例行（GSC 取數、資料夾、13 週時程、基線報告） |
| `/seo-kb-universal ops next` | 問這週 / 今天 SEO 該做什麼 |
| `/seo-kb-universal ops weekly` | 每週 30 分鐘：告警、衰退頁、標題佇列 |
| `/seo-kb-universal ops monthly` | 每月 2 小時：新查詢進母表、SERP 分析、評分、蠶食、下月日曆 |
| `/seo-kb-universal ops quarterly` | 每 13 週半天：內容 A–E 分級與汰舊、母表重評分、季節字 |
| `/seo-kb-universal ops research 信用卡` | 新 hub 的 8 步關鍵字研究 |

也可以直接描述問題，例如「我的網站核心更新後流量掉了」。

## 選用設定

`check` 的 Core Web Vitals 使用 Google PageSpeed Insights。匿名額度常用完，建議申請免費金鑰，並設定環境變數 `PSI_API_KEY`。

`ops` 的 Search Console 資料有兩種來源：
- API（建議）：Google Cloud 建 service account 並啟用 Search Console API，下載 JSON 金鑰，在 Search Console 把該帳戶加為「受限」使用者。腳本只用標準庫與系統的 openssl，不用安裝套件。步驟在 `references/ops-setup.md`。
- CSV：沒有 API 時，用 Search Console 成效報表的「匯出」下載 zip，解壓後交給腳本。上限 1,000 列，且沒有「查詢 × 網頁」維度，蠶食與缺專頁分析會略過。

## 使用限制

- 需要 Python 3.9 以上，不用安裝套件。
- `check` 要能連上目標網站。環境不能連外時，稽核腳本會失敗，查知識庫不受影響。
- 台灣以外的市場沒有內建數據，只提供評估框架。
- 內容是固定快照。政策、門檻與工具功能超過 90 天就要先查證。
- 法規內容是整理，不是法律意見。
- `ops` 的門檻（週比 −20%、低 CTR 以本站同位置中位數 50% 為準、D 級 < 15% 等）來自知識庫對應章節；知識庫改版時要一併核對腳本。
- 「缺專頁」是以查詢與網址 slug 的字詞比對做的啟發式，只列候選；內容 D 級需要人工補發佈日期，E 級（過時 / 違規）只能人工判定。
