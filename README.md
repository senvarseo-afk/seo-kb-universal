# SEO 知識庫 skill

這是一份可直接安裝的 SEO 知識庫 skill，內含 26 章規範、狀況解法手冊、台灣市場速查、通用市場評估框架、AdSense、Google Ads 與社群廣告規範。內容查證至 2026-11-09。

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

也可以直接描述問題，例如「我的網站核心更新後流量掉了」。

## 選用設定

`check` 的 Core Web Vitals 使用 Google PageSpeed Insights。匿名額度常用完，建議申請免費金鑰，並設定環境變數 `PSI_API_KEY`。

## 使用限制

- 需要 Python 3.9 以上，不用安裝套件。
- `check` 要能連上目標網站。環境不能連外時，稽核腳本會失敗，查知識庫不受影響。
- 台灣以外的市場沒有內建數據，只提供評估框架。
- 內容是固定快照。政策、門檻與工具功能超過 90 天就要先查證。
- 法規內容是整理，不是法律意見。
