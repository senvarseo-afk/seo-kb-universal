# 04 技術 SEO 規範

> 版本：1.1 ｜ 更新日期：2026-11-05 ｜ 適用：所有 SEO 網站專案 ｜ 撰寫：Claude

## 本章摘要

1. Google 處理一個頁面的順序是「發現 → 爬取 → （排隊）渲染 → 索引 → 排名」；每一關都有獨立的失敗點，診斷時先定位卡在哪一關。
2. robots.txt 管「爬不爬」、meta robots / X-Robots-Tag 管「索不索引」、canonical 管「哪個版本代表」——三者各司其職，被 robots.txt 擋住的頁面看不到後兩者。
3. 轉址用 301 / 308（永久、強訊號）；302 / 307 只用於真正暫時的情況；404 與 410 在 Google 眼中幾乎等價；5xx 與 429 會降低爬取速率，持續則從索引移除。
4. Core Web Vitals 現行三指標：LCP ≤ 2.5 s、INP ≤ 200 ms、CLS ≤ 0.1，以 CrUX 真實使用者 75 百分位、手機 / 桌機分開評估；FID 已於 2024-03-12 退役。
5. JavaScript 站點優先 SSR / SSG / ISR；Google 以 evergreen Chromium 渲染但有延遲與資源限制；動態渲染（dynamic rendering）Google 已不建議作為長期方案。

## 目錄

1. [爬取與索引機制](#1-爬取與索引機制)
2. [robots.txt](#2-robotstxt)
3. [meta robots 與 X-Robots-Tag](#3-meta-robots-與-x-robots-tag)
4. [XML Sitemap](#4-xml-sitemap)
5. [Canonical 規則與常見衝突](#5-canonical-規則與常見衝突)
6. [重複內容與參數](#6-重複內容與參數)
7. [HTTP 狀態碼與轉址規範](#7-http-狀態碼與轉址規範)
8. [HTTPS 與 HSTS](#8-https-與-hsts)
9. [行動優先索引](#9-行動優先索引)
10. [JavaScript SEO](#10-javascript-seo)
11. [Core Web Vitals](#11-core-web-vitals)
12. [其他效能項目](#12-其他效能項目)
13. [安全與 HTTP 標頭](#13-安全與-http-標頭)
14. [記錄檔（Log）分析要點](#14-記錄檔log分析要點)
15. [hreflang 概述](#15-hreflang-概述)
16. [主機、DNS 與 CDN 注意事項](#16-主機dns-與-cdn-注意事項)
17. [Bing、IndexNow 與其他搜尋引擎](#17-bingindexnow-與其他搜尋引擎)
18. [常見技術 SEO 狀況 → 解法表](#18-常見技術-seo-狀況--解法表)
19. [本章檢查清單](#19-本章檢查清單)
20. [參考來源](#20-參考來源)

---

## 1. 爬取與索引機制

### 1.1 流程

```
發現 (Discover) → 爬取 (Crawl) → 處理 (Process) → 渲染佇列 (Render) → 索引 (Index) → 排名 (Rank / Serve)
     ↑                                                      │
     └──────── 從渲染後 HTML 擷取新連結 ─────────────────────┘
```

| 階段 | Google 做什麼 | 常見失敗點 | 在 GSC 看哪裡 |
|---|---|---|---|
| 發現 | 從 sitemap、內部 / 外部連結、過去的爬取記錄得到 URL | 孤兒頁、未提交 sitemap | 網頁 → 已找到 - 目前尚未建立索引 |
| 爬取 | 先讀 robots.txt；允許才抓取 HTML；依 crawl budget 排程 | robots.txt 擋、5xx、逾時、DNS | 檢索統計；網頁 → 遭 robots.txt 封鎖 |
| 處理 | 解析 HTML、擷取 `<a href>`、讀 meta robots / canonical；把 200 頁面放進渲染佇列 | noindex、錯誤 canonical | 網頁 → 遭 noindex 排除 / 重複網頁 |
| 渲染 | 用 headless evergreen Chromium 執行 JS（有延遲，從數秒到數天） | 資源被擋、JS 錯誤、需要互動才載入的內容 | URL 檢查 → 查看已檢索的網頁 → 螢幕截圖 / HTML |
| 索引 | 以渲染後 HTML 決定內容、canonical、是否收錄 | 品質不足、重複、軟性 404 | 網頁 → 已檢索 - 目前尚未建立索引 |
| 排名 | 依查詢即時計算 | — | 成效報表 |

來源：Google「JavaScript SEO basics」與「How Google Search works」（查閱 2026-11-03）。

### 1.2 Googlebot 的技術限制（2026-11-03 查證）

- 支援 HTTP/1.1 與 HTTP/2（預設 1.1，視過去統計自動切換）；HTTP/2 省資源但**無排名加成**；可對 HTTP/2 回 421 拒絕。官方文件「How Google's crawlers work」僅載明「Google's crawlers and fetchers support HTTP/1.1 and HTTP/2」，未提及 HTTP/3（查閱 2026-11-03）；視為不支援，HTTP/3 只服務一般使用者。
- 支援 gzip、deflate、Brotli。
- 檔案大小上限：Googlebot 搜尋爬取目前明列一般支援檔案類型 2 MB、PDF 64 MB（解壓縮後）；15 MB 是 Google 通用爬蟲基礎設施的預設值，不是 Googlebot 的實際上限（HTML 與個別資源各自計算；Google 於 2026-02-03 新增各 crawler 預設檔案大小上限文件）；超過的部分忽略（https://developers.google.com/search/docs/crawling-indexing/googlebot）。
- 支援 `ETag` / `If-None-Match` 與 `Last-Modified` / `If-Modified-Since`；兩者都有時優先 ETag；建議兩者都送。
- 驗證真假 Googlebot：先對來源 IP 做反向 DNS，主機名稱須屬於 `googlebot.com` / `google.com` / `googleusercontent.com`，再對該主機名稱做正向 DNS 確認解析回同一個 IP（只做反向 DNS 不足）；或直接比對 Google 公布的 IP 範圍 JSON（`/crawling/ipranges`）（https://developers.google.com/crawling/docs/crawlers-fetchers/verify-google-requests）。2026-03 起 Google 另有 `Google-Agent`（使用者觸發的代理）IP 範圍。
- 主要爬取 IP 在美國；地理定向內容要注意 Googlebot 看到的是美國版本。

來源：Google Crawling docs「How Google's crawlers work」、changelog（查閱 2026-11-03）。

### 1.3 Google 爬蟲與 AI 相關 token（2026-11-03 查證）

| Token | 用途 | 對 robots.txt |
|---|---|---|
| `Googlebot` | Search、Discover、Images、Video、News 的主爬蟲（含 smartphone 與 desktop UA） | 遵守 |
| `Googlebot-Image` / `Googlebot-Video` | 圖片 / 影片 | 遵守 |
| `Googlebot-News` | Google News（無獨立 UA 字串，使用 Googlebot 字串，但可用此 token 寫規則） | 遵守 |
| `Storebot-Google` | Shopping | 遵守 |
| `Google-InspectionTool` | Search Console 測試工具 | 遵守 |
| `GoogleOther`（含 -Image / -Video） | 研發用一次性爬取 | 遵守 |
| `Google-CloudVertexBot` | 站長自行要求的 Vertex AI 爬取 | 遵守 |
| `Google-Extended` | **純控制 token，無獨立 UA**：擋它 = 內容不用於訓練 Gemini 與 Gemini Apps / Vertex AI grounding；**不影響 Search 收錄與排名，也不影響 AI Overviews**（AI Overviews 由 Googlebot 與 `nosnippet` 控制，詳見 08） | 遵守 |
| `Mediapartners-Google` | AdSense 與其他廣告產品的內容判讀（2026-09 文件已泛化） | 遵守；**流量站不要擋**（詳見 09） |
| 使用者觸發 fetcher（`Google-GeminiNotebook`、`Google-Read-Aloud`、`FeedFetcher-Google`、`Google-Site-Verification`、`Google-Pinpoint`、`Google-CWS`、Google Messages 預覽等） | 使用者主動要求的抓取 | **一般忽略 robots.txt** |

- 2026-10-30 Google 文件新增：Google 「打算支援」一個跨公司共用、機器可讀的 AI 訓練偏好訊號（IETF AIPREF 相關），官方 changelog（2026-10-30 條目，查閱 2026-11-03）只說「intends to support」並連到部落格說明；Google 目標於 2027 年支援 IETF AIPREF 共用 AI 訓練控制，尚未承諾確切日期（來源：https://developers.google.com/search/blog/2026/10/ai-training-control ，查閱 2026-11-03）；目前未生效。
- `Google-NotebookLM` 已於 2026-07-16 改名為 `Google-GeminiNotebook`（舊名過渡期仍可用）。

---

## 2. robots.txt

**規範**：每個主機（含每個子網域、每種協定）在根目錄放一份 UTF-8 的 `robots.txt`，≤ 500 KiB，只用 `User-agent` / `Allow` / `Disallow` / `Sitemap` 四個欄位，且**永遠不用它來控制索引**。

**為什麼**：Google 只讀前 500 KiB；只支援上述四個欄位，`Crawl-delay`、`Noindex`、`Host` 等一律忽略（Google「robots.txt specification」，2026-10-23 更新，查閱 2026-11-03）。被 Disallow 的 URL 仍可能因外部連結而被索引（顯示「沒有可用的說明」），因為 Google 根本沒抓到頁面、看不到 noindex。

**怎麼做**（機制重點，範本見 15）：

| 規則 | 說明 |
|---|---|
| 位置 | `https://example.com/robots.txt`；`https://blog.example.com/` 要另一份；`http://` 與 `https://` 各自讀自己的（但一般 http 已 301 到 https） |
| 比對 | 路徑大小寫敏感；`*` 萬用、`$` 結尾；最長（最具體）的規則勝出；Allow 與 Disallow 等長時 Allow 勝 |
| 群組 | Google 只採用「最具體匹配 UA」的群組；同一個 UA 若分散在多個群組，Google 會把這些群組的規則合併適用，但不會與 `*` 群組合併 → 如果你為 `Googlebot` 開了一組，`*` 裡的規則對它全部失效，要複製一份（https://developers.google.com/crawling/docs/robots-txt/robots-txt-spec#order-of-precedence-for-user-agents） |
| 編碼 | 非 ASCII 路徑在規則中使用 percent-encoding（2026-10-23 Google 新增建議） |
| 快取 | Google 通常快取 24 小時；可用 `Cache-Control: max-age` 調整 |
| 狀態碼 | 2xx：照讀；3xx：Google 至少跟隨五跳，超過則視為 404（robots.txt 本身應直接回 200，不要轉址）；**4xx（429 除外）：視為沒有限制、全部可爬**；**5xx / 網路錯誤：先暫停爬取最多 12 小時並重試，之後用最後一份快取最多 30 天**；若長期 5xx 且站點整體可用，視同 404 |
| Sitemap 欄位 | 絕對 URL，可多行，可指向其他主機 |
| 資源 | **不要擋 CSS / JS / 圖片 / 字型 / API endpoint**（渲染需要）；WordPress 不要擋 `/wp-content/`、`/wp-includes/js/` |
| 測試 | Search Console「設定 → robots.txt」報表（2023 年取代了舊的 robots.txt 測試工具）可看各主機的抓取狀態與版本 |

**什麼該擋**：站內搜尋結果、分面組合參數、購物車 / 結帳、登入後頁面、API、staging、`/wp-admin/`（保留 `admin-ajax.php`）、`?replytocom=`、feed（視需求）。

**什麼不該擋**：想 noindex 的頁面（擋了就看不到 noindex）、想 canonical 合併的重複頁、CSS / JS、分頁、任何已有排名的頁面。

**驗收方式**：`curl -I https://example.com/robots.txt` 回 200 與 `text/plain`；GSC robots.txt 報表無「擷取錯誤」；URL 檢查工具對重要頁面顯示「允許檢索」；爬蟲以 Googlebot UA 爬取時被擋的 URL 清單符合預期。

**常見錯誤**：測試環境 `Disallow: /` 跟著部署上線；`Disallow: /*?` 把分頁一起擋掉；只寫 `User-agent: Googlebot` 一組卻忘了其他 bot 的規則；用 robots.txt 「刪除」已索引頁面（應改用 noindex 或 410）。

---

## 3. meta robots 與 X-Robots-Tag

**規範**：頁面層級的索引控制一律用 `<meta name="robots">`（HTML）或 `X-Robots-Tag` HTTP 標頭（非 HTML 檔案如 PDF、圖片，或需要在伺服器層統一設定時）；要生效，該 URL 必須**可爬取**。

**支援的指令**（Google「Robots meta tag, data-nosnippet, and X-Robots-Tag specifications」，查閱 2026-11-03）：

| 指令 | 效果 | 備註 |
|---|---|---|
| `noindex` | 不收錄 | 看到後數天到數週生效；Google 長期看到 noindex 後會**降低爬取頻率**，且可能最終視為 nofollow（連結不再傳遞） |
| `nofollow` | 不跟隨此頁所有連結 | 內部頁面幾乎不該用；想不索引但保留連結請用 `noindex`（不加 nofollow） |
| `none` | = noindex, nofollow | |
| `nosnippet` | 不顯示文字摘要與影片預覽；**同時不作為 AI Overviews 與 AI Mode 的輸入** | 流量站慎用（會降低點閱） |
| `max-snippet:[n]` | 摘要字元上限；`-1` 不限、`0` = nosnippet | |
| `max-image-preview:[none/standard/large]` | 圖片預覽大小；**要允許 Discover 大圖預覽，設定 `large` 並符合圖片規格**（不是收錄 Discover 的必要條件；https://developers.google.com/search/docs/appearance/google-discover） | 流量站預設 `large` |
| `max-video-preview:[n]` | 影片預覽秒數 | |
| `notranslate` | 不提供翻譯 | |
| `noimageindex` | 此頁圖片不索引 | |
| `unavailable_after: [RFC 822 / ISO 8601]` | 指定日期後移除 | 日期無效則忽略 |
| `indexifembedded` | 與 noindex 搭配，允許在 iframe 內被索引 | |
| `noarchive` | **已停用**：Google 已移除快取連結功能，此指令現在無作用 | |
| `data-nosnippet`（HTML 屬性） | 區塊級排除摘要 | 可用於廣告 / 免責聲明區塊 |

**規則**：

- 多個指令以逗號分隔，或多個 meta 標籤；衝突時採最嚴格者。
- `<meta name="googlebot">` 只對 Google 生效；`robots` 對所有。
- 必須在 `<head>` 內、原始 HTML 中；JS 注入的 noindex Google 可讀但不保證即時；**不要依賴 JS 移除原始 HTML 中的 noindex**（Google 看到 noindex 可能跳過渲染，移除不會生效）；在可渲染的頁面用 JS 新增 noindex 是 Google 文件提供的做法，但仍以原始 HTML 為首選（https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics#use-robots-meta-tags-carefully）。
- `X-Robots-Tag: noindex` 用於 PDF、圖片、整個目錄、以及 staging 全站。
- 與 robots.txt 互斥：被 Disallow 的 URL 這些指令全部無效。

**驗收方式**：URL 檢查工具 → 「索引建立」→「允許建立索引？」；Screaming Frog「Directives」分頁篩選 noindex；`curl -I` 查 X-Robots-Tag。

**常見錯誤**：WordPress 的「阻擋搜尋引擎索引這個網站」在正式站被勾；Next.js `robots` metadata 在 layout 設了 `index: false` 後被所有子頁繼承；staging 用 X-Robots-Tag noindex 後連同標頭設定搬到正式站。

---

## 4. XML Sitemap

### 4.1 規範

**規範**：所有可索引的 canonical URL 都在 sitemap 中，且只放這些；每個 sitemap 檔 ≤ 50,000 URL 且未壓縮 ≤ 50 MB；超過則用 sitemap index；`<lastmod>` 必須反映真實的重要更新；`priority` 與 `changefreq` 可省略。

**為什麼**：Google 明確「忽略 `<priority>` 與 `<changefreq>`」，只在 `<lastmod>` 「一貫且可驗證地準確」時才使用（Google「Build and submit a sitemap」，查閱 2026-11-03）。sitemap 同時是「canonical 提示」之一——列在 sitemap 裡的 URL Google 視為你偏好的版本。

### 4.2 各類型限制（2026-11-03 查證）

| 類型 | 用途 | 限制 / 必填 |
|---|---|---|
| 標準 `urlset` | 頁面 | 50,000 URL / 50 MB；`<loc>` 必填（絕對 URL、與 canonical 完全一致含尾斜線）；`<lastmod>` W3C datetime |
| Sitemap index | 彙整多個 sitemap | 同樣 50,000 筆 / 50 MB；index 不可再指向 index（Google 只接受一層） |
| Image | 圖片搜尋 | 每個 `<url>` 最多 1,000 個 `<image:image>`；只需 `<image:loc>`（`caption`、`title`、`geo_location`、`license` 已於 2022 年停用） |
| Video | 影片 | 每個 `<url>` 的 `<video:video>` 必填 `thumbnail_loc`、`title`、`description`、以及 `content_loc` 或 `player_loc` 擇一 |
| News | Google News | **最多 1,000 個 `<news:news>`**；只放**過去 2 天**的文章；必填 `publication/name`、`publication/language`、`publication_date`、`title`；`zh-tw` 代表繁中 |
| 多語言 | hreflang | 每個 `<url>` 內用 `<xhtml:link rel="alternate" hreflang="..." href="..."/>` 列出所有版本（含自己與 x-default）；詳見 10 |
| 文字檔 | 簡單清單 | 一行一個 URL，UTF-8，`.txt` |
| RSS / Atom / mRSS | 最新內容 / 影片 | 可作補充，不建議當唯一 sitemap |

### 4.3 怎麼做

- 位置：`/sitemap.xml`（或 `/sitemap_index.xml`）；可放在任何路徑，但 sitemap 只能包含「其所在目錄之下」的 URL，除非透過 robots.txt `Sitemap:` 宣告或在 GSC 提交（跨主機也可）。
- 分割策略：依類型（posts / pages / categories / products）或依時間；流量站建議「每類一檔 + 最近 30 天一檔」，方便在 GSC 看各類型的索引率。
- `lastmod`：內容、結構化資料、重要連結更新才改；不要每次 build 都設成 `new Date()`（Next.js 範例常見錯誤）——Google 發現不可信後會整站忽略。
- 動態產生 + CDN 快取 10–60 分鐘；大型站用 sitemap index + 每個子檔獨立快取。
- 排除：noindex 頁、非 canonical 版本、3xx / 4xx、站內搜尋，以及非 canonical、不可索引或不希望出現在搜尋結果的分頁／參數 URL（分頁與參數 URL 若本身是 canonical 且可索引，可以列入；依可索引性與 canonical 判斷，不是一律排除）。
- 提交：GSC「Sitemap」+ robots.txt `Sitemap:` 行（後者也供 Bing 等引擎發現）。
- 新內容：發布即更新 sitemap 與 lastmod；搭配 IndexNow 推 Bing（第 17 節）。Google 沒有即時推送 API 可用（Indexing API 僅限 JobPosting 與 BroadcastEvent，濫用會被停權）。

**驗收方式**：GSC Sitemap 報表「成功」且「已找到的網頁數」= 實際可索引頁數；GSC「網頁」報表用「所有已提交的網頁」篩選，索引率 ≥ 90%；用 Screaming Frog「List mode」匯入 sitemap 爬取：100% 回 200、canonical 自指、無 noindex。

**常見錯誤**：sitemap 含 `http://` URL 或不含尾斜線的版本；WordPress 同時有 Yoast 與核心兩套 sitemap；News sitemap 放了 3 個月的文章；image sitemap 用了已停用的 caption 欄位（無害但無用）。

---

## 5. Canonical 規則與常見衝突

### 5.1 規範

**規範**：每個可索引頁面在原始 HTML `<head>` 內有且只有一個 `<link rel="canonical" href="絕對 URL">`，指向自己（或指向該內容的代表版本）；所有內部連結、sitemap、hreflang、結構化資料的 `url` 都指向同一個 canonical。

**為什麼**：Google 把 canonical 當「強提示」而非指令，並綜合 301、sitemap、內部連結、HTTPS 偏好、hreflang 叢集等訊號後自行選擇。訊號互相矛盾時，Google 自選的結果常與你預期不同（Google「How to specify a canonical with rel="canonical" and other methods」，查閱 2026-11-03）。

### 5.2 訊號強弱與使用時機

| 方法 | 強度 | 用於 |
|---|---|---|
| 301 / 308 轉址 | 最強 | 重複版本不需要存在時（http → https、大小寫、尾斜線、舊 URL） |
| `rel="canonical"`（HTML 或 HTTP `Link:` 標頭） | 強提示 | 重複版本需要存在（追蹤參數、列印版、AMP 已不建議；聯合發布的跨站 canonical 只是提示，見 5.3 第 11 條） |
| sitemap 收錄 | 弱提示 | 大型站的補強 |
| 內部連結一致 | 弱提示 | 永遠要做 |

### 5.3 規則清單

1. 絕對 URL（含 `https://` 與主機名）；相對路徑容易被解析錯。
2. 自指 canonical 是預設（每頁都要），不是可選。
3. 只能有一個；WordPress 常見 Yoast + 主題 + 外掛各輸出一個，Google 遇到多個相異 canonical 會全部忽略。
4. HTML 版本放 `<head>`；若 `<head>` 內出現無效元素（如 `<div>`、未閉合標籤）會讓 Google 提前結束 head 解析，canonical 失效。
5. canonical 的目標必須回 200、可索引、不被 robots.txt 擋、不帶 noindex；**不能指向 404、3xx、noindex 頁**。
6. 跨語言不要用 canonical（`/tl/` 不能 canonical 到 `/en/`），用 hreflang。
7. 分頁不要全部指向第 1 頁（見 03 第 7 節）。
8. canonical 不能指向帶片段 `#` 的 URL。
9. JS 不得修改 canonical；SPA 必須在伺服器 HTML 就輸出正確值。
10. 行動 / 桌機分離站（m.）：**桌機頁**放 `<link rel="alternate" media="only screen and (max-width: 640px)" href="https://m.example.com/page">` 指向手機頁；**手機頁**放 `<link rel="canonical" href="https://www.example.com/page">` 指向桌機頁；桌機頁可自我 canonical（來源：https://developers.google.com/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing ，查閱 2026-11-03）——此架構 2026 年已不建議，改用 RWD。
11. 跨網域聯合發布（syndication）：首選約定對方頁面加 noindex（Google 的建議）；跨站 canonical 指回你只是「可能被採用」的提示，不保證 Google 選你的版本；至少要求連回原文（https://support.google.com/news/publisher-center/answer/9606800）。

### 5.4 常見衝突與判讀

| 衝突 | 結果 | 修法 |
|---|---|---|
| canonical 指向 A，但 A 301 到 B | Google 多半選 B，但會有延遲與「重複網頁」警告 | canonical 直接指 B |
| canonical 指 A，sitemap 列 B，內部連結連 C | Google 自選，常選連結最多的 | 全部統一 |
| canonical 指 A，A 有 noindex | 整組可能都不索引 | 移除 noindex 或改 canonical |
| 頁面 canonical 指自己，但內容與另一頁 95% 相同 | Google 可能無視 canonical 把兩頁合併，選它認為的那一頁 | 真正差異化內容，或主動 canonical 到主版本 |
| HTTP 版與 HTTPS 版都 200、都自指 | Google 偏好 HTTPS，但這是重複 | 301 HTTP → HTTPS |
| hreflang 叢集中某頁 canonical 指向其他語言 | 該頁從叢集中掉出且不索引 | canonical 自指 |

**驗收方式**：URL 檢查「使用者宣告的標準網址」= 「Google 選擇的標準網址」；Screaming Frog「Canonicals」分頁：Missing = 0、Multiple = 0、Non-Indexable Canonical = 0、Canonicalised（指向他頁）的清單符合預期。

---

## 6. 重複內容與參數

**規範**：同一內容只允許一個可索引 URL；技術性重複（協定、主機、大小寫、尾斜線、`index.html`、追蹤參數）用 301 或 canonical 消除；內容性重複（極相似的程序化頁、同商品多分類）在架構階段避免。

**為什麼**：Google 沒有「重複內容懲罰」，但重複會：稀釋連結訊號、讓 Google 自選你不想要的版本、吃爬取預算、並在程序化規模下觸發「規模化內容濫用」或品質判定（詳見 07、11）。

**怎麼做**：

| 重複來源 | 首選解法 | 備援 |
|---|---|---|
| `http` / `https`、`www` / 非 www | 301 | — |
| 大小寫 | 伺服器 301 至小寫 | canonical |
| 尾斜線 | 301 | canonical |
| `/index.html`、`/index.php`、`/default.aspx` | 301 至目錄 | canonical |
| `utm_*`、`fbclid`、`gclid`、`ref`、`srsltid`（Google Merchant 自動加的） | canonical 自指乾淨 URL（頁面仍回 200） | robots.txt `Disallow: /*?*utm_`（路徑須以 `/` 開頭；封鎖後 Google 讀不到 canonical，所以這不是 canonical 的等效備援，只能減少爬取） |
| 分面 / 排序 | 見 03 第 8 節 | — |
| 列印版 `?print=1` | canonical | noindex |
| 相同內容多個 slug（CMS 改標題重產 slug） | 301 舊 → 新 | — |
| 商品多分類路徑 | 商品 URL 不含分類 | canonical 到主分類版本 |
| 近似程序化頁（城市 × 服務） | 只對有獨特資料的組合建頁；其餘不建或 noindex | 詳見 11 |
| 聯合發布到其他網站 | 對方 noindex + 連回原文（Google 建議） | 對方 canonical 指回（僅為提示，可能不被採用） |
| 樣板文字佔比過高（每頁 800 字樣板 + 150 字內容） | 減少樣板、把重複區塊改為折疊或共用頁 | — |

**驗收方式**：GSC「網頁」中「重複網頁，Google 選擇的標準網址與使用者不同」與「重複網頁，使用者未選取標準網頁」各 < 可索引頁 1%；Siteliner / Screaming Frog「Content → Near Duplicates」（相似度 ≥ 90%）清單人工審查。

---

## 7. HTTP 狀態碼與轉址規範

### 7.1 Google 如何看待各狀態碼（Google Crawling docs「How HTTP status codes affect Google's crawlers」，查閱 2026-11-03）

| 狀態碼 | Google 行為 | 使用規範 |
|---|---|---|
| 200 | 送入索引流程（不保證收錄） | 正常頁 |
| 204 | 無內容、不處理 | 不要用在頁面 |
| 301 / 308 | 跟隨；視為「強訊號」目標為 canonical；傳遞連結訊號 | 永久搬移。308 與 301 對 Google 等價，差別在 308 保留 POST method |
| 302 / 303 / 307 | 跟隨；視為「弱訊號」；長期存在時 Google 可能當 301 處理，但不保證 | 真正暫時（A/B、維護、地區暫導）。307 與 302 對 Google 等價 |
| 304 | 內容未變；不影響索引 | 配合 ETag / Last-Modified 實作 |
| 404 | 內容不存在；已索引的會被移除；爬取頻率逐漸降低 | 頁面真的不存在 |
| 410 | 與 404 **相同**：Google 文件明寫「所有 4xx（除 429）一視同仁」，404 與 410 兩列的說明文字完全一樣；「410 移除略快」是業界**經驗說法**，Google 文件無此描述，不要以此為決策依據 | 明確永久移除（語意上較清楚，但 Google 處理方式與 404 無異） |
| 401 / 403 | 同 404 類；**不要**用它們限制爬取速率 | 登入 / 禁止區 |
| 429 | 視為伺服器過載 → **降低爬取速率**；持續則移除索引 | 真正的速率限制；要回 `Retry-After`（2026-10-06 Google 新增文件） |
| 500 / 502 / 503 | 暫時降低爬取速率，比例與錯誤 URL 數成正比；已索引頁先保留、持續錯誤則移除；恢復 2xx 後逐步回升 | 維護用 503 + `Retry-After`，**不超過數天**（Google 未公布確切天數；實務觀察 1–2 週內恢復通常無永久損失） |
| 軟性 404（回 200 但內容是「找不到」） | Google 判定為 404 且浪費爬取 | 必須修成真 404 / 410 |

### 7.2 轉址規範

**規範**：

1. 永久搬移一律 301（或 308）；伺服器層（nginx / Apache / Cloudflare / Next.js `redirects()`）實作，**不用** meta refresh 或 JS 轉址（Google 可解析：立即的 meta refresh（0 秒）視為永久轉址、有延遲的視為暫時轉址；JS 轉址要等渲染後才被發現，較慢且不保證；https://developers.google.com/search/docs/crawling-indexing/301-redirects#metarefresh）。
2. 轉址鏈 ≤ 1 跳；Google 最多跟 10 跳（文件：robots.txt 至少跟隨五跳、頁面 10 跳）；Google 明確表示永久轉址不造成 PageRank 損失，但每一跳都增加延遲與爬取成本，鏈過長時 Google 可能放棄跟隨（https://developers.google.com/search/docs/crawling-indexing/301-redirects）；爬蟲報告中內部 3xx 必須為 0。
3. 不得轉址迴圈。
4. 轉址目標必須回 200、是 canonical、且主題相關；大量舊頁 301 到首頁或分類首頁會被當軟性 404。
5. 新舊 URL 的順序：`http → https` 與 `非 www → www` 與尾斜線與大小寫，合併成**一條**規則一次到位（範本見 15）。
6. 行動 / 桌機不做 UA 轉址（RWD 下沒有這回事）；語言不做 IP 自動轉址。
7. 轉址保留期：至少 1 年；有外鏈者永久。
8. 刪除頁面：有相關替代頁 → 301；沒有 → 410 / 404 並從 sitemap 與內鏈移除；**不要**把所有 404 都 301 到首頁。

**驗收方式**：`curl -sIL https://example.com/OLD | grep -E "HTTP|location"` 顯示恰好一個 301 與最終 200；Screaming Frog「Redirect Chains」報表為空；GSC「網頁」中「網頁會重新導向」的數量只包含預期的舊 URL。

---

## 8. HTTPS 與 HSTS

**規範**：全站 HTTPS、有效憑證涵蓋所有使用的主機名（含 www 與非 www）、HTTP 一律 301 至 HTTPS、無混合內容、送出 `Strict-Transport-Security` 標頭，並視情況加入 HSTS preload。

**為什麼**：HTTPS 是輕量排名訊號（2014 起），更重要的是 Google 以 HTTPS 版本為預設 canonical；混合內容或憑證錯誤會使 Google 退回選 HTTP 版本（Google「Consolidate duplicate URLs」提到憑證無效、不安全依賴、HTTPS 轉回 HTTP 會讓 Google 不選 HTTPS）。Chrome 自 2023 起預設 HTTPS-First。

**怎麼做**：

- 憑證：Let's Encrypt（90 天自動更新）或 Cloudflare 邊緣憑證；SAN 含 `example.com` 與 `www.example.com`；通配 `*.example.com` 用於多子網域。
- Cloudflare：SSL/TLS 模式設 **Full (strict)**（`Flexible` 會造成轉址迴圈或源站 HTTP 明文）；開 Always Use HTTPS、Automatic HTTPS Rewrites。
- HSTS：`Strict-Transport-Security: max-age=31536000; includeSubDomains; preload`。先用 `max-age=300` 測一週，確認所有子網域都支援 HTTPS 再拉長；`preload` 送進 hstspreload.org 後幾乎不可逆，確定不會有任何 HTTP-only 子網域再提交。
- 混合內容：資源一律 `https://` 或 `//` 省略協定（後者已不建議，直接寫 https）；WordPress 用 Better Search Replace 批次改資料庫中的 `http://`。
- Search Console 以「網域資源」驗證（涵蓋 http / https / 所有子網域），不要只驗 `https://www`。

**驗收方式**：SSL Labs 評等 A 以上；Chrome DevTools Security 面板無混合內容；`curl -I http://example.com/` 回 301 至 `https://`；Screaming Frog「Security」分頁：HTTP URLs = 0、Mixed Content = 0、Missing HSTS Header = 0。

---

## 9. 行動優先索引

**規範**：Google 以「Googlebot Smartphone」抓取的手機版 HTML 為唯一索引依據（2024-07-05 起全面實施，桌機版僅作少數驗證用途）；手機版必須與桌機版有相同的主要內容、標題、meta、結構化資料、內部連結、圖片與 alt。

**為什麼**：Google「Mobile-first indexing best practices」（查閱 2026-11-03）明列：手機版少內容、少結構化資料、不同 meta、圖片被擋、手機版 noindex、手機版回錯誤碼等都會直接造成索引內容縮水或頁面消失。

**怎麼做**：

- 一律 RWD；不要再做 m. 子網域或動態服務（dynamic serving）。
- 手機版可折疊（accordion / tab）內容——Google 明確接受，前提是 HTML 已存在，而不是點擊後才請求。
- 不要對手機版做「精簡版導覽」刪掉連結。
- 圖片用 `<img>`（或 `<picture>`）帶 `src`，不要只靠 CSS background 放主要圖片；lazy loading 用原生 `loading="lazy"`，首屏圖片不 lazy。
- 字體 ≥ 16 px、點擊目標 ≥ 48 px、視窗 `<meta name="viewport" content="width=device-width, initial-scale=1">`。
- 插頁式廣告與頂部大面積廣告違反 Better Ads Standards 會影響頁面體驗評估（詳見 09）。
- 伺服器容量：手機版 UA 爬取量 = 全部爬取量，確保能承受。

**驗收方式**：URL 檢查 →「檢索方式：Googlebot 智慧型手機」且「查看已檢索的網頁」HTML 內有完整內容；Screaming Frog 以 Googlebot Smartphone UA + JS 渲染爬取，與桌機 UA 比較字數、內鏈數、結構化資料數（差異 < 5%）。

---

## 10. JavaScript SEO

### 10.1 渲染模式與 Googlebot 的影響

| 模式 | 初始 HTML 內容 | Googlebot 看到的 | 風險 | 建議 |
|---|---|---|---|---|
| **CSR**（純前端渲染，如 CRA、Vite SPA） | 空殼 `<div id="root">` | 必須等渲染佇列才看到內容；索引延遲數小時到數天；JS 出錯 = 空頁 | 高 | **不用於需要 SEO 的頁面** |
| **SSR**（每次請求伺服器渲染；Next.js dynamic、Nuxt server） | 完整 HTML | 第一次抓取就有內容 | TTFB 較高；需要快取 | 動態內容、個人化 |
| **SSG**（建置時產生靜態 HTML；Astro 預設、Next.js static、Nuxt generate） | 完整 HTML | 最佳 | 建置時間隨頁數成長；內容更新需重建 | 內容站首選 |
| **ISR / 增量再生**（Next.js ISR、Nuxt SWR routeRules、Astro on-demand + CDN cache） | 完整 HTML（快取） | 最佳 | 第一次請求可能回舊版 | 大型內容站、程序化頁 |
| **Streaming SSR / RSC** | 完整 HTML 但分段送出 | Google 可處理；Next.js 15.2+ 的「streaming metadata」會把 `<title>` 等放到 `<body>`，Google 可讀，但 Next.js 對不執行 JS 的 bot（如 facebookexternalhit）自動改回阻塞式輸出 | 其他爬蟲 / AI bot 可能讀不到 | 確認 `htmlLimitedBots` 設定；重要頁可停用 streaming metadata |
| **動態渲染**（偵測 bot 另給預渲染 HTML，如 Rendertron、prerender.io） | 給 bot 的是預渲染版 | 可索引 | Google 2022 年起文件改為「**是權宜之計（workaround），不是長期方案**」；維護兩套輸出、容易被判定 cloaking（若內容不同） | 僅過渡用；盡快遷到 SSR / SSG |

來源：Google「JavaScript SEO basics」、「Dynamic rendering as a workaround」（查閱 2026-11-03）；Next.js「generateMetadata → Streaming metadata」（2026-08-19 更新，查閱 2026-11-03）。

### 10.2 規範

1. **所有要排名的頁面：主要內容、title、meta description、canonical、hreflang、結構化資料、內部連結都必須出現在伺服器回傳的原始 HTML**（不是 hydration 之後）。
2. Hydration 不得改變上述元素；hydration 錯誤（React「Hydration failed」）會造成 CLS 與內容閃爍，必須修。
3. 連結用 `<a href>`（框架的 `<Link>` 元件可）；路由用 History API，不用 `#`。
4. 不依賴使用者互動（點擊、捲動、hover）才載入主要內容；「載入更多」要有 URL（03 第 7 節）。
5. 404 必須回真正的 404 狀態碼；SPA 無法回狀態碼時，用 JS 加 `noindex` 或轉到真 404 URL（Google 建議），但 SSR 框架都能回正確碼，應直接做到。
6. 不要把 API endpoint、JS chunk、CSS 擋在 robots.txt。
7. 長效快取 + 內容指紋檔名（`app.a1b2c3.js`）；Googlebot 可能忽略 Cache-Control 而用舊 JS，指紋檔名可避免。
8. 不用 `window.location` 做 SEO 轉址；用伺服器 301。
9. Web Components：內容要出現在渲染後的 light DOM / shadow DOM（Google 會攤平），`<slot>` 內容可索引。
10. 第三方 widget（評論、評分）若內容重要，SSR 它或提供 HTML 備援。

**驗收方式**：

- `curl -A "Googlebot" https://example.com/page/ | grep -c "<h1"`（原始 HTML 有內容）。
- URL 檢查工具 → 即時測試 → 「查看已測試的網頁」：HTML 與螢幕截圖完整、「更多資訊 → 網頁資源」無被擋資源、「JavaScript 主控台訊息」無錯誤。
- Screaming Frog 分別用「Text Only」與「JavaScript」模式爬，比較 title / H1 / 字數 / 內鏈；差異應為 0 或僅限次要互動元件。

**常見錯誤**：Next.js 把 `generateMetadata` 寫在 Client Component（無效）；Nuxt 用 `useHead` 於 `onMounted` 內（只在客戶端跑）；Astro 的 `client:only` 元件裡放主要內容；整頁內容靠 `useEffect` fetch。

---

## 11. Core Web Vitals

### 11.1 現行定義與門檻（web.dev，查閱 2026-11-03）

| 指標 | 衡量 | 良好 | 需改善 | 不佳 |
|---|---|---|---|---|
| **LCP**（Largest Contentful Paint） | 視窗內最大圖片 / 文字區塊渲染完成時間 | ≤ 2.5 s | 2.5–4.0 s | > 4.0 s |
| **INP**（Interaction to Next Paint） | 整個頁面存續期間，所有點擊 / 觸控 / 鍵盤互動中最慢者（排除離群：每 50 次互動忽略 1 個最差）到下一次畫面更新的延遲 | ≤ 200 ms | 200–500 ms | > 500 ms |
| **CLS**（Cumulative Layout Shift） | 最大「工作階段視窗」（5 秒內、間隔 ≤ 1 秒的位移累計）的非預期版面位移分數 | ≤ 0.1 | 0.1–0.25 | > 0.25 |

- 評估基準：**真實使用者（CrUX）的 75 百分位**，手機與桌機分開；三項都達「良好」才算通過。
- **FID（First Input Delay）已於 2024-03-12 退役，由 INP 取代**（已停用）。任何仍以 FID 報告的工具或文件都是過時的。
- hover、捲動、縮放不算 INP 的互動。
- 2026-11-03 查證：web.dev INP 文件（最後更新 2025-09-02）「良好」門檻仍為 **≤ 200 ms**，並無改為 150 ms；web.dev Web Vitals 總覽（2024-10-31）與 Search Central 部落格 2026 年文章清單亦無任何門檻變更公告。若日後看到「150 ms」說法，先回到 https://web.dev/articles/inp 核對再採用。
- Google 將 CWV 用於頁面體驗評估，屬輕量排名因素；但它直接影響廣告可視度、跳出率與 Discover 表現（詳見 09）。

### 11.2 CrUX（Field）vs Lab

| | CrUX / Field（真實使用者） | Lab（Lighthouse、PSI 實驗室、WebPageTest） |
|---|---|---|
| 資料來源 | Chrome 使用者（已同意回傳）過去 28 天 | 一次模擬載入 |
| 決定 GSC 的 CWV 狀態 | **是** | 否 |
| 有 INP | 是 | Lighthouse 是實驗室工具，用 TBT 等診斷指標當代理，不直接輸出 INP；要量 INP 用 DevTools Performance 面板（與頁面互動後看 INP）或 `web-vitals` 程式庫（來源：https://web.dev/articles/vitals ，查閱 2026-11-03） |
| 看哪裡 | GSC「核心網頁生命力」報表、PSI 上半部、CrUX Dashboard / BigQuery / API | PSI 下半部、Lighthouse、DevTools Performance |
| 流量門檻 | 頁面或 origin 要有足夠樣本；小站只有 origin 層級資料或「資料不足」 | 無 |
| 用途 | 判定通過 / 診斷哪些 URL 群組有問題 | 找原因、驗證修法 |

- Lighthouse 13（2025-10）把舊 audit 改為「Insights」，診斷呈現方式與 audit ID 改變，但效能評分（計分項目與權重）未變（https://developer.chrome.com/blog/lighthouse-13-0）；DevTools Performance 面板可即時看 LCP 元素與 INP 互動（本地互動時顯示）。
- 流量站東南亞使用者多用中低階 Android + 4G，CrUX 數值通常比 Lab 差很多；Lab 要用「Moto G Power / Slow 4G」設定才接近真實。

### 11.3 LCP：常見原因 → 修法

| 原因 | 診斷 | 修法 |
|---|---|---|
| TTFB 慢（> 800 ms） | PSI「TTFB」、DevTools Network | 快取（CDN / 全頁快取 / ISR）、升級主機、減少 DB 查詢（第 12 節） |
| LCP 圖片未在初始 HTML（CSS background、JS 注入、lazy load） | DevTools Performance → LCP element；PSI「LCP request discovery」 | 用 `<img>` 放在 HTML、`fetchpriority="high"`、不加 `loading="lazy"`、必要時 `<link rel="preload" as="image">` |
| 圖片過大 / 格式差 | PSI「Properly size images」 | WebP / AVIF、`srcset` + `sizes`、CDN 自動縮圖 |
| render-blocking CSS / JS | PSI「Render blocking requests」 | 關鍵 CSS inline、其餘 `media="print" onload`、JS `defer` |
| 字型阻塞文字（LCP 是文字時） | PSI「Font display」 | `font-display: swap`、preload 主要字型、自架字型 |
| 廣告 / 第三方腳本搶頻寬 | Network 瀑布圖 | 延後載入廣告到 LCP 之後；見 12.6 |
| 重導向鏈 | Network 第一個請求 | 消除鏈 |

### 11.4 INP：常見原因 → 修法

| 原因 | 診斷 | 修法 |
|---|---|---|
| 長任務（> 50 ms）佔用主執行緒（廣告、分析、聊天 widget、Hydration） | DevTools Performance 互動後的 long task；web-vitals 庫 attribution | 拆分任務、`scheduler.yield()` / `setTimeout` 讓出、延後非必要 JS、減少 hydration 範圍（Astro islands、RSC） |
| 互動後觸發大量 DOM 更新 | Performance「Rendering」區 | 虛擬化長列表、減少 DOM 節點（< 1,500）、避免同步 layout（讀 offsetHeight 後立即寫 style） |
| 事件處理器做同步 fetch 或大量運算 | 程式碼審查 | 先更新 UI（loading state）再處理 |
| 第三方 consent / 廣告腳本攔截第一次點擊 | 看 INP attribution 的 target | 延後或 sandbox iframe |
| 同意彈窗 / 插頁於頁面載入時出現 | — | 改為非阻塞、延後顯示 |

### 11.5 CLS：常見原因 → 修法

| 原因 | 修法 |
|---|---|
| 圖片 / 影片無尺寸 | `width` / `height` 屬性或 CSS `aspect-ratio` |
| 廣告位無預留 | 用固定高度 / `min-height` 容器包廣告（最常見的 AdSense 問題，範本見 15） |
| 動態插入內容（通知列、推薦區、「訂閱」區塊）在既有內容上方 | 只在視窗下方插入，或預留空間 |
| 字型替換（FOUT）造成文字重排 | `font-display: optional` 或 `size-adjust` 調整 fallback；preload |
| 無尺寸的 iframe、embed | 預留容器 |
| Hydration 不一致 | 修 SSR / CSR 差異 |
| 頂部延遲載入的導覽 / cookie bar | 以固定高度或 `position: fixed` 覆蓋而非推擠 |

### 11.6 流程與驗收

**規範**：每個專案在 GSC「核心網頁生命力」中手機與桌機的「不佳」URL = 0、「需改善」< 10%；主要範本（首頁、文章頁、hub 頁）各做 Lab 診斷。

**驗收方式**：GSC CWV 報表；PSI 的 Field 區塊三項綠色；`web-vitals` JS 庫送 GA4 事件（埋設見 15）觀察 75 百分位；修復後 28 天 CrUX 才會完整反映。

---

## 12. 其他效能項目

### 12.1 TTFB

**規範**：75 百分位 TTFB ≤ 800 ms（web.dev 建議門檻）；內容站目標 ≤ 500 ms（Google 爬取統計的「平均回應時間」也受此影響）。

**怎麼做**：全頁快取（WordPress：主機層快取或 WP Rocket / LiteSpeed Cache；Next.js：SSG / ISR；Astro：靜態）+ CDN 邊緣快取 HTML（Cloudflare Cache Rules「Cache Everything」+ 略過登入 cookie）；資料庫查詢 < 50 ms；主機就近東南亞使用者（新加坡區域）或靠 CDN。

### 12.2 圖片

**規範**：主要格式 WebP（相容性最好）或 AVIF（更小，Safari 16+ 支援）+ `<picture>` 降級；所有 `<img>` 有 `width` / `height` / `alt`；`srcset` 提供 3–5 個寬度；首屏外的圖片 `loading="lazy"`；單張 ≤ 200 KB；LCP 圖片 `fetchpriority="high"`。

**為什麼**：圖片通常是 LCP 元素與總傳輸量的大宗；Google 圖片搜尋對流量站是可觀的流量來源，需要 `<img>` + alt + 可爬的圖片 URL（不要 base64 inline 大圖、不要擋 CDN 圖片主機）。

**怎麼做**：Next.js `<Image>`、Nuxt `<NuxtImg>`、Astro `<Image>` 都自動產生 srcset 與現代格式；WordPress 6.5+ 可輸出 AVIF；Cloudflare Images / Polish 可在邊緣轉格式。圖片 URL 穩定（改圖不改 URL 會讓 Google 圖片索引保留舊快取；改內容時用新檔名）。

### 12.3 字型

**規範**：自架字型（不用 Google Fonts 外連，省一個連線與隱私問題）、WOFF2、子集化（中文字型必做，否則 5–10 MB）、`font-display: swap` 或 `optional`、preload 首屏用的 1–2 個檔案；總字型 ≤ 100 KB（拉丁）/ 依子集（CJK）。

### 12.4 快取

**規範**：靜態資源（JS / CSS / 圖片 / 字型）`Cache-Control: public, max-age=31536000, immutable` + 指紋檔名；HTML `Cache-Control: public, max-age=0, s-maxage=600, stale-while-revalidate=86400`（CDN 快取、瀏覽器不快取）；送 `ETag` 與 `Last-Modified` 讓 Googlebot 用 304。

### 12.5 CDN

**規範**：所有專案前面放 CDN（Cloudflare 免費方案足夠內容站）；開啟 HTML 邊緣快取、Brotli、HTTP/2 / HTTP/3、Early Hints（103）；Cloudflare 的 Rocket Loader 預設**關閉**（會延後 JS 執行，常造成 hydration 與 CLS 問題）；Email Obfuscation 視狀況關閉（Mirage 已於 2025-09-15 退場，不再需要設定；https://developers.cloudflare.com/speed/optimization/images/mirage/）；Bot Fight Mode 不得擋 Googlebot / Bingbot（Cloudflare 預設放行已驗證的 bot，但自訂 WAF 規則要留白名單）。詳細設定見 15。

### 12.6 第三方腳本與廣告腳本

**規範**：第三方 JS 總量 ≤ 首方 JS；每個第三方都要回答「它影響哪個 CWV、能否延後、能否移除」；廣告腳本（AdSense、Ezoic、Mediavine 等）以 `async` 載入、在 LCP 之後初始化、廣告容器預留高度；GTM 內的 tag 數 ≤ 15。

**為什麼**：流量站 CWV 不佳的第一原因幾乎都是廣告與分析腳本——它們產生長任務（INP）、無預留空間（CLS）、搶首屏頻寬（LCP）。AdSense 官方腳本本身是 async，但自動廣告（Auto ads）會在任意位置插入廣告 → CLS 風險最高（詳見 09 對廣告版位的規範）。

**怎麼做**：

- 廣告：固定尺寸單元 + 容器 `min-height`；自動廣告關閉「錨定」以外的動態插入或限制區塊；Auto ads 由 Google 控制載入；手動單元自行以 IntersectionObserver 延遲插入首屏以下的單元，不要先用 `display:none` 藏起來（初始隱藏的單元可能不發請求，詳見 22 章 §3.6）。
- 分析 / 像素：GA4 用 `gtag` async 或 GTM；Facebook Pixel、TikTok Pixel 等延後到 `requestIdleCallback` 或使用者互動後。
- 聊天 / 推播 / 社群嵌入：點擊後才載入（facade 模式）；YouTube 用 `lite-youtube-embed`。
- Partytown（Astro / Next.js 可用）可把第三方跑在 Web Worker，但與部分廣告腳本不相容，需測試。
- 每季用 PSI「Reduce the impact of third-party code」或 WebPageTest 看第三方阻塞時間。

**驗收方式**：Lighthouse「Third-party」Insight 中的主執行緒阻塞時間 < 250 ms（手機）；首屏完成前的請求中第三方 ≤ 3 個。

---

## 13. 安全與 HTTP 標頭

**規範**：所有回應送出以下標頭（值可依專案調整，範本見 15）：

| 標頭 | 建議值 | SEO 相關性 |
|---|---|---|
| `Strict-Transport-Security` | `max-age=31536000; includeSubDomains; preload` | HTTPS canonical 穩定 |
| `Content-Security-Policy` | 至少 `upgrade-insecure-requests`；有廣告的站用 nonce + `strict-dynamic` 的 strict CSP（AdSense / GAM 不支援網域白名單，詳見 15 §12；來源：https://support.google.com/adsense/answer/16283098 、https://developers.google.com/publisher-tag/guides/content-security-policy ，查閱 2026-11-03），先用 `Content-Security-Policy-Report-Only` 測 | 阻止混合內容與注入；**擋到 Googlebot 需要的資源會影響渲染**，用 URL 檢查確認 |
| `X-Content-Type-Options` | `nosniff` | — |
| `X-Frame-Options` / CSP `frame-ancestors` | `SAMEORIGIN` / `'self'` | 防止被 iframe 嵌入（內容盜用） |
| `Referrer-Policy` | `strict-origin-when-cross-origin` | 讓 GA4 仍能看到來源 |
| `Permissions-Policy` | 關閉用不到的 API（camera、microphone、geolocation）；**注意**：若用 Google 廣告，`interest-cohort`/Topics 等相關設定要看 09 | — |
| `Cache-Control` / `ETag` / `Last-Modified` | 見 12.4 | 爬取效率 |
| `X-Robots-Tag` | 僅在需要時（PDF、staging） | 索引控制 |
| `Content-Type` | `text/html; charset=utf-8` | 編碼錯誤會造成亂碼索引 |
| `Vary` | 有依 Accept-Encoding / Cookie 變化時正確設定；**不要**用 `Vary: User-Agent` 做內容差異（RWD 下沒必要） | 快取正確性 |

- 被駭風險：WordPress 外掛漏洞是流量站被注入垃圾頁（日文 / 藥品 / 賭博關鍵字）的主因——GSC「安全性問題」報表每週看；外掛 ≤ 20 個且全部維護中；檔案權限與 `wp-config.php` 保護；詳見 12 的被駭處理流程。
- 不要用 Cloudflare「Under Attack Mode」長期開著（JS challenge 會擋爬蟲）。

**驗收方式**：securityheaders.com 評等 A；URL 檢查「網頁資源」無因 CSP 被擋的項目；Screaming Frog「Security」分頁全綠。

---

## 14. 記錄檔（Log）分析要點

**規範**：中大型站（≥ 1 萬頁）或遇到索引問題時，每月分析至少 7 天的伺服器 / CDN 存取記錄；小站用 GSC「檢索統計資料」代替即可。

**為什麼**：記錄檔是唯一能看到「Googlebot 實際抓了什麼、多常、回了什麼碼」的來源；GSC 檢索統計只有彙總與抽樣。

**怎麼做**：

1. 來源：nginx / Apache access log、Cloudflare Logpush（付費）或 Cloudflare「Analytics → Security / Traffic」粗略看；Vercel / Netlify 的 log 保留短，需外送到 Axiom / Datadog / BigQuery。
2. 篩選：UA 含 `Googlebot` 且 IP 反查驗證（假 Googlebot 很多）；分開 Smartphone 與 Desktop、Googlebot-Image、AdsBot、Mediapartners、GoogleOther。
3. 必看指標：
   - 每日 Googlebot 請求數趨勢（突然下降 = 伺服器問題或品質下降；突然上升 = 無限 URL 或被駭）。
   - 狀態碼分佈：200 ≥ 80%、3xx < 10%、4xx < 5%、5xx ≈ 0。
   - 被爬 URL 中「可索引 canonical 頁」佔比 ≥ 70%；其餘（參數、noindex、資源）過高表示浪費。
   - 重要頁面最近一次被爬時間（超過 30 天未爬的營收頁要補內鏈）。
   - 從未被爬的 sitemap URL 清單（= 發現問題）。
   - 回應時間分佈（> 1 s 的比例）。
   - 爬取了哪些不存在於 sitemap 的 URL（找出意外曝光的 URL 來源）。
4. 工具：Screaming Frog Log File Analyser、JetOctopus、Botify、或自寫 SQL（BigQuery）。
5. 與 GSC 交叉：把「已檢索 - 目前尚未建立索引」的 URL 對上記錄檔，看是品質（有爬、沒收）還是爬取（沒爬）問題。

**驗收方式**：產出月報：請求數、狀態碼比例、可索引佔比、前 20 個最常被爬的 URL 模式、未爬 sitemap URL 數。

---

## 15. hreflang 概述

只列技術要點，完整規範（語言 / 地區選擇、x-default、內容本地化、常見錯誤）詳見 10。

- 三種實作擇一：HTML `<link rel="alternate" hreflang="x" href="…">`、HTTP `Link:` 標頭、XML sitemap `<xhtml:link>`；大型多語站用 sitemap 最好維護。
- 必須**雙向互指**且每頁包含自己；缺回連的配對可能被忽略，其餘有效配對仍可處理（https://developers.google.com/search/docs/specialty/international/localized-versions）。
- 使用絕對 URL、指向 canonical（自指）版本、回 200。
- 語言碼 ISO 639-1、地區碼 ISO 3166-1 Alpha-2（`en-US`、`pt-BR`、`zh-Hant-TW` 用 script 子標籤）；`x-default` 給語言選擇頁或預設版本。
- 同一頁面每個 hreflang 標籤 ≤ 1 個；超過 50 個語言版本時用 sitemap。
- hreflang 不會合併重複，也不是 canonical；兩者衝突時 canonical 勝（會把該語言踢出叢集）。
- 驗收：GSC「國際指定目標」報表已移除（2022），改用 Screaming Frog「Hreflang」分頁（Missing Return Links、Inconsistent Language、Non-Canonical Return Links 都要為 0）。

---

## 16. 主機、DNS 與 CDN 注意事項

- **DNS**：TTL 300–3600 s；搬遷前 24 小時降到 300；DNS 失敗對 Google 等同站點不可用（持續則降爬取與移除）；用 Cloudflare DNS 或主機商 Anycast DNS；DNSSEC 可開但驗證設定正確（設錯整站消失）。
- **主機位置**：對東南亞使用者優先新加坡 / 日本區域 + CDN；主機位置本身非排名因素，但影響 TTFB 與 CrUX。
- **共享主機**：IP 共享不影響 SEO；但鄰居造成的 5xx 與慢回應會影響。流量站月流量 > 50 萬 PV 建議 VPS / 託管 WordPress / 靜態 + CDN。
- **Cloudflare 常見陷阱**：Flexible SSL 迴圈；Rocket Loader；「Browser Integrity Check」或 WAF 自訂規則誤擋 Googlebot（看 Security Events 中 Googlebot 的 block / challenge 數必須為 0）；Cache Everything 把登入頁 / 個人化內容快取給所有人；Cloudflare 的 managed robots.txt 會在你的 robots.txt 前面加入 Content Signals 區塊（GSC 可能報「語法不明」，Cloudflare 稱不影響爬取；詳見 15 與 08）。
- **Vercel / Netlify**：每個 deploy 都有預覽 URL（`*.vercel.app`、`*.netlify.app`）。Vercel 的 Preview 部署預設就回 `X-Robots-Tag: noindex`，但 Production 部署的 `*.vercel.app` 網域不會（https://vercel.com/docs/headers/response-headers#x-robots-tag）；Netlify 需自行設定。先用 `curl -I` 檢查實際標頭，再依平台與部署類型在非正式環境加 `X-Robots-Tag: noindex`（Vercel 可依 `VERCEL_ENV` 判斷）；只有正式網域允許索引。
- **維護**：用 503 + `Retry-After`，不用 200 的「維護中」頁面；時間 < 數小時最佳。
- **監測**：uptime 監控（1 分鐘頻率）、5xx 告警、憑證到期告警（詳見 13）。

---

## 17. Bing、IndexNow 與其他搜尋引擎

- **Bing Webmaster Tools**：所有專案都要驗證（可從 GSC 匯入）；Bing 的「網站掃描」與「URL 檢查」可補 GSC 不足；Bing 對 `rel="prev/next"` 的立場只有 2012-04-13 的官方部落格文章：視為「分頁結構的提示」、放在 `<head>`、**不合併分頁訊號、不改變結果外觀**；2026-11-03 查閱 Bing Webmaster 說明中心已無現行文件說明此標記 → 保留標記無害，但效果屬**專案執行時驗證**（Bing Webmaster Tools 的 URL 檢查 / 網站掃描看分頁是否被完整索引）；Bing 支援 `Crawl-delay`（在其 UA 群組下）。
- **IndexNow**（查閱 2026-11-03）：參與者為 Microsoft Bing、Naver、Seznam.cz、Yandex、Yep；**Google 不參與**（Google 曾於 2021 年表示「測試」，至今未採用）。機制：在根目錄放 `{key}.txt`（8–128 字元，僅英數與連字號），對 `https://api.indexnow.org/indexnow` 或 `https://www.bing.com/indexnow` 送 GET（單一 URL）或 POST JSON（`host`、`key`、`urlList` 最多 10,000 筆）；回 200 / 202 僅代表收到。WordPress 用 Rank Math / Yoast / Bing 官方外掛自動推；Next.js 在發布 webhook 中呼叫（範本見 15）。對東南亞市場 Bing 流量通常 < 3%，但成本極低，一律實作。
- **Yandex / Naver / Baidu**：僅在目標市場為俄語 / 韓語 / 中國大陸時處理；Baidu 對 JS 渲染支援差、要求 ICP 備案與中國境內主機，不在本知識庫預設範圍。
- **AI 搜尋引擎的爬蟲（OAI-SearchBot、PerplexityBot、Claude-SearchBot、Applebot 等）**：控制策略與 robots.txt 範本見 15；策略面詳見 08。

---

## 18. 常見技術 SEO 狀況 → 解法表

| 症狀 | 可能原因 | 診斷步驟 | 解法 | 預防 |
|---|---|---|---|---|
| 整站突然從 Google 消失 | robots.txt `Disallow: /`、全站 noindex、DNS / 憑證失效、手動處置、被駭 | GSC「網頁」急降類別；`curl -I`；GSC 安全性 / 手動操作 | 修正後 GSC 驗證 / 請求索引 | 部署檢查清單加 robots / noindex 比對；uptime 監控 |
| 「已檢索 - 目前尚未建立索引」大量 | 品質不足、重複、thin、程序化頁過多 | 抽樣看內容獨特性；比對記錄檔確認有爬 | 提升內容、合併、noindex 低價值頁 | 11 章的程序化品質門檻 |
| 「已找到 - 目前尚未建立索引」大量 | 爬取預算 / 伺服器慢 / 孤兒 | 檢索統計回應時間；inlinks | 加速、加內鏈、減少無限 URL | 03 第 11 節 |
| 「遭 robots.txt 封鎖」但想索引 | 規則過寬 | 個別頁面用 GSC「網址檢查」的即時測試（現行 robots.txt 報表只提供抓取版本、錯誤與重新抓取，沒有 URL 測試功能；https://support.google.com/webmasters/answer/6062598）；未部署的規則用本機 robots.txt 解析器或爬蟲工具測 | 改規則 | 上線前測試 |
| 「已編入索引，但遭 robots.txt 封鎖」 | 擋了又有外鏈 | — | 想刪：解除封鎖 + noindex；想留：解除封鎖 | 不用 robots.txt 做索引控制 |
| 「網頁含有重新導向」（內部大量） | 內鏈指向舊 URL | 爬蟲 3xx 清單 | 內鏈改最終 URL | 改版流程 |
| 「軟性 404」 | 空分類 / 空搜尋 / 「無結果」回 200 | 抽樣看頁面 | 回 404 / 410 或補內容 | 0 結果回 404 |
| 「伺服器錯誤 (5xx)」 | 主機過載、WAF、PHP 錯誤 | 記錄檔 5xx 時間分佈 | 修主機 / 快取；若是速率問題用 429 + Retry-After | 監控 |
| 「重複網頁，Google 選擇的標準網址與使用者不同」 | canonical 訊號衝突 | 第 5.4 節表 | 統一訊號 | 爬蟲 Canonicals 檢查 |
| Google 顯示的 title 不是我設的 | title 過長 / 樣板化 / 與 H1 不符 | 比對 title、H1、錨文字 | 改寫 title 與 H1 一致（詳見 05） | — |
| 手機版 CWV 全紅、桌機綠 | 廣告 / 第三方腳本、圖片未最佳化、低階裝置 | PSI 手機 Field + Lab | 11.3–11.5 與 12.6 | 廣告容器預留、延後第三方 |
| INP 不佳但找不到原因 | 廣告 / consent 腳本、hydration | web-vitals attribution 回報 target 元素 | 延後第三方、減少 hydration | — |
| CLS 不佳 | 廣告無預留、圖片無尺寸、字型 | DevTools Layout Shift Regions | 11.5 | 範本見 15 |
| 新文章 Google 看到的是空白 | CSR / 需互動 / JS 錯誤 / 資源被擋 | URL 檢查 → 已檢索的網頁 HTML | SSR / SSG；解除資源封鎖 | 10.2 規範 |
| 圖片搜尋無流量 | 圖片 CSS background、CDN 擋 Googlebot-Image、無 alt、lazy 載入錯誤 | 爬蟲 Images 分頁；robots 測試圖片 URL | `<img>` + alt + image sitemap | — |
| hreflang 失效 | 缺回連、canonical 指他語、相對 URL | Screaming Frog Hreflang 分頁 | 修正 | 詳見 10 |
| Googlebot 被 Cloudflare 擋 | WAF / Bot Fight / Under Attack | Cloudflare Security Events 篩 Googlebot | 放行已驗證 bot | 設定審查 |
| Vercel 預覽網址被索引 | 無 noindex | `site:vercel.app` 查 | 預覽環境加 X-Robots-Tag noindex；GSC 移除 | 部署設定 |
| 被駭注入垃圾頁（日文關鍵字） | 外掛漏洞 | GSC 安全性；`site:` 查詢異常 URL；記錄檔 | 清除、換密碼、更新、410 垃圾 URL、GSC 要求審查 | 外掛管理、WAF |
| sitemap「無法讀取」 | 錯誤 XML、gzip 壞、被 robots 擋、超大 | 用 XML validator；curl | 修正、分割 | 自動化驗證 |
| 搬家後舊 URL 仍在索引數月 | 正常；Google 需重爬 301 | — | 保留舊 sitemap、確認一跳 301 | — |

---

## 19. 本章檢查清單

**爬取與索引**
- [ ] robots.txt：200、≤ 500 KiB、不擋 CSS / JS / 圖片、staging 規則未上線、含 Sitemap 行
- [ ] 重要頁面 URL 檢查：允許檢索、允許索引、Google 選擇的 canonical = 使用者宣告
- [ ] 搜尋 / 分面 / 參數 / feed 依 03 的策略處理
- [ ] noindex 頁不在 sitemap、不被 robots.txt 擋

**Sitemap 與 canonical**
- [ ] sitemap 只含可索引 canonical URL；lastmod 真實；≤ 50,000 / 50 MB；GSC 提交成功
- [ ] 每頁恰一個自指 canonical（絕對 URL）；內鏈 / sitemap / hreflang 一致
- [ ] 協定、主機、大小寫、尾斜線、index.html 皆一跳 301

**狀態碼與轉址**
- [ ] 內部 3xx = 0；轉址鏈 = 0；無迴圈
- [ ] 不存在頁面回 404 / 410（非軟性 404）；無大量 301 至首頁
- [ ] 維護用 503 + Retry-After

**HTTPS / 安全**
- [ ] 全站 HTTPS、HSTS、無混合內容、SSL Labs A
- [ ] 安全標頭齊全且 CSP 不擋 Googlebot 資源
- [ ] GSC 安全性問題 = 0

**行動 / JS**
- [ ] RWD；手機版內容 / 內鏈 / 結構化資料 = 桌機版
- [ ] 原始 HTML 含主要內容、title、canonical、結構化資料；Text-only 與 JS 爬取差異 ≈ 0
- [ ] 不使用動態渲染作為長期方案

**效能**
- [ ] GSC CWV 手機 + 桌機：不佳 = 0；LCP ≤ 2.5 s、INP ≤ 200 ms、CLS ≤ 0.1（75 百分位）
- [ ] TTFB ≤ 800 ms（目標 500）；HTML 邊緣快取；靜態資源一年快取 + 指紋
- [ ] 圖片 WebP / AVIF + 尺寸屬性 + srcset；字型自架 WOFF2 + 子集
- [ ] 廣告容器預留高度；第三方腳本延後；Rocket Loader 關閉

**監測**
- [ ] GSC 檢索統計每月檢視（200 ≥ 80%、5xx ≈ 0、回應 < 500 ms）
- [ ] 中大型站每月記錄檔分析
- [ ] Bing Webmaster Tools 驗證；IndexNow 實作
- [ ] uptime / 憑證 / 5xx 告警

---

## 20. 參考來源

- Google Search Central — JavaScript SEO basics：https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics（查閱 2026-11-03）
- Google Search Central — Dynamic rendering as a workaround：https://developers.google.com/search/docs/crawling-indexing/javascript/dynamic-rendering（查閱 2026-11-03）
- Google Crawling docs — How Google's crawlers work（HTTP/2、壓縮、15 MB、ETag）：https://developers.google.com/crawling/docs/crawlers-fetchers/overview-google-crawlers（查閱 2026-11-03）
- Google Crawling docs — Overview of Google crawlers and fetchers（僅支援 HTTP/1.1 與 HTTP/2，預設 HTTP/1.1）：https://developers.google.com/crawling/docs/crawlers-fetchers/overview（查閱 2026-11-03）
- Google Crawling docs — List of Google's common crawlers（Google-Extended、Google-CloudVertexBot、AIPREF 意向）：https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers（查閱 2026-11-03）
- Google Crawling docs — User-triggered fetchers（一般忽略 robots.txt）：https://developers.google.com/crawling/docs/crawlers-fetchers/google-user-triggered-fetchers（查閱 2026-11-03）
- Google Crawling docs — Changelog（2025–2026 更新：Google-GeminiNotebook 改名、Retry-After、percent-encoding、Web Bot Auth、檔案大小上限）：https://developers.google.com/crawling/docs/changelog（查閱 2026-11-03）
- Google Crawling docs — How Google interprets the robots.txt specification（2026-10-23 更新）：https://developers.google.com/crawling/docs/robots-txt/robots-txt-spec（查閱 2026-11-03；舊網址 developers.google.com/search/docs/crawling-indexing/robots/robots_txt 會 301 至此；`/crawling/docs/robots-txt` 本身為 404）
- Google Search Central — Robots meta tag, data-nosnippet, and X-Robots-Tag specifications：https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag（查閱 2026-11-03）
- Google Search Central — Build and submit a sitemap（50,000 / 50 MB、忽略 priority / changefreq）：https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap（查閱 2026-11-03）
- Google Search Central — News sitemap（1,000 筆、2 天）：https://developers.google.com/search/docs/crawling-indexing/sitemaps/news-sitemap（查閱 2026-11-03）
- Google Search Central — How to specify a canonical with rel="canonical" and other methods：https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls（查閱 2026-11-03）
- Google Crawling docs — How HTTP status codes affect Google's crawlers（404 / 410 同等處理）：https://developers.google.com/crawling/docs/troubleshooting/http-status-codes（查閱 2026-11-03；舊網址 developers.google.com/search/docs/crawling-indexing/http-network-errors 會 301 至此；`/crawling/docs/http-network-errors` 為 404）
- 2026-11-03 逐一驗證本節 crawling 文件路徑：`/crawling/docs/crawlers-fetchers/overview-google-crawlers`、`/google-common-crawlers`、`/google-user-triggered-fetchers`、`/verify-google-requests`、`/crawling/docs/changelog`、`/crawling/docs/crawl-budget`、`/crawling/docs/robots-txt/robots-txt-spec`、`/crawling/docs/robots-txt/create-robots-txt`、`/crawling/docs/troubleshooting/http-status-codes` 皆回 200；對應的舊 `search/docs/crawling-indexing/...` 路徑皆 301 到新路徑。仍留在 Search Central 的：`googlebot`、`robots/intro`、`robots-meta-tag`、`301-redirects`、`consolidate-duplicate-urls`、`sitemaps/*`（皆 200）。
- Google Crawling docs — Large site owner's guide to managing your crawl budget（2026-07-22 更新）：https://developers.google.com/crawling/docs/crawl-budget（查閱 2026-11-03）
- Google Search Central — Mobile-first indexing best practices：https://developers.google.com/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing（查閱 2026-11-03）
- Google Search Central — Pagination, incremental page loading（rel prev/next 不再使用）：https://developers.google.com/search/docs/specialty/ecommerce/pagination-and-incremental-page-loading（查閱 2026-11-03）
- web.dev — Web Vitals（LCP / INP / CLS 門檻、75 百分位、FID 退役）：https://web.dev/articles/vitals（頁面更新 2024-10-31，查閱 2026-11-03）
- web.dev — Interaction to Next Paint (INP)（200 / 500 ms、互動定義；頁面最後更新 2025-09-02，門檻未改為 150 ms）：https://web.dev/articles/inp（查閱 2026-11-03）
- Google Search Central Blog — 2026 年文章清單（無 CWV / INP 門檻變更公告）：https://developers.google.com/search/blog（查閱 2026-11-03）
- Bing Webmaster Blog — Implementing Markup For Paginated And Sequenced Content（2012-04-13；rel prev/next 為提示、不合併）：https://blogs.bing.com/webmaster/2012/04/13/implementing-markup-for-paginated-and-sequenced-content（查閱 2026-11-03；Bing Webmaster 說明中心 https://www.bing.com/webmasters/help/ 無現行對應文件）
- Chrome Developers — Lighthouse 13.0（2025-10-10，舊 audit 移除改 Insights）：https://developer.chrome.com/blog/lighthouse-13-0（查閱 2026-11-03）
- Next.js Docs — generateMetadata（Streaming metadata、htmlLimitedBots；2026-08-19 更新）：https://nextjs.org/docs/app/api-reference/functions/generate-metadata（查閱 2026-11-03）
- IndexNow — 官方文件與參與引擎：https://www.indexnow.org/ 、https://www.indexnow.org/documentation（查閱 2026-11-03）
- Cloudflare Docs — Managed robots.txt / Content Signals Policy：https://developers.cloudflare.com/bots/additional-configurations/managed-robots-txt/（查閱 2026-11-03）
