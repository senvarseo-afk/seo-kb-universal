# 20. 新聞與時效型內容 SEO

> 版本：1.0 ｜ 更新日期：2026-11-03 ｜ 適用：所有 SEO 網站專案 ｜ 撰寫：Claude

## 本章摘要

1. 2025 年起 Google News 不再接受手動提交：只要內容被索引且符合 Google News 內容政策，就「自動具備資格」；Publisher Center 幾乎只剩 News Showcase 與 Reader Revenue Manager 的用途。
2. Top stories、Google News、Discover 三個入口的共通門檻是：清楚的日期與署名、原創內容、≥ 1200 px 的大圖加 `max-image-preview:large`、以及不誇大的標題。
3. 時效性內容的核心規範是「日期必須誠實」：`datePublished` 永遠是首發時間、`dateModified` 只在實質更新時變動、可見日期與結構化資料一致；人工刷新日期是 Google News 明文禁止的行為。
4. 即時型內容（比分、颱風、匯率）要分「固定 URL 持續更新」與「每日 / 每期新頁」兩種模式，依查詢意圖與歷史價值選擇，不可兩者混用造成重複。
5. 2026-02 的 Discover 核心更新明確以「本地相關性、減少 clickbait、依主題判定的站點專業度」為方向，流量站若靠 Discover 必須把主題集中度當成第一優先。

## 目錄

- [20.1 三個入口的現況與收錄條件](#201-三個入口的現況與收錄條件)
- [20.2 Google News Publisher Center 現況](#202-google-news-publisher-center-現況)
- [20.3 新聞 Sitemap 規範](#203-新聞-sitemap-規範)
- [20.4 NewsArticle 結構化資料要點](#204-newsarticle-結構化資料要點)
- [20.5 時效性內容的日期處理](#205-時效性內容的日期處理)
- [20.6 即時內容的頁面設計與索引策略](#206-即時內容的頁面設計與索引策略)
- [20.7 Google Discover 的觸發特性](#207-google-discover-的觸發特性)
- [20.8 時效性查詢與 QDF 機制](#208-時效性查詢與-qdf-機制)
- [20.9 快訊與 Live blog](#209-快訊與-live-blog)
- [20.10 新聞類網站的 E-E-A-T 與作者要求](#2010-新聞類網站的-e-e-a-t-與作者要求)
- [20.11 避免被判為新聞類垃圾](#2011-避免被判為新聞類垃圾)
- [20.12 時效內容 → 狀況解法表](#2012-時效內容--狀況解法表)
- [本章檢查清單](#本章檢查清單)
- [參考來源](#參考來源)

---

## 20.1 三個入口的現況與收錄條件

Google 的「新聞 / 時效」流量來自三個不同系統，規則重疊但不相同：

| 入口 | 位置 | 資格判定 | 主要訊號 | GSC 報表 |
|---|---|---|---|---|
| **Top stories**（熱門報導輪播） | Google Search 結果頁上方 / 中段 | 演算法判定頁面為「新聞性」內容，且網站符合 Search 的內容政策與 Google News 內容政策；不需要加入 Google News，不需要結構化資料（有則有助理解） | 新鮮度、原創性、站點在該主題的權威、頁面體驗、日期與署名清楚 | GSC 搜尋外觀沒有 Top stories 篩選項（官方清單：support.google.com/webmasters/answer/17011259，查閱 2026-11-03）；只能用搜尋類型 = News 看 Google 新聞分頁、用整體曝光 / 點擊變化與手機實搜觀察 Top stories |
| **Google News**（news.google.com、App） | 獨立產品 | 2025 年起自動：被索引 + 符合 Google News 內容政策即自動納入考慮；Google 演算法決定是否出現 | 相關性、顯著性（prominence）、權威性、新鮮度、可用性、地區與語言 | 左側「Google 新聞」成效報表 |
| **Discover** | Chrome 新分頁、Google App 首頁、Android 首頁左滑 | 被索引 + 符合 Discover 內容政策即自動具資格；不需結構化資料或特殊標籤 | 與使用者興趣的匹配（基於 Web & App Activity）、大圖、標題、E-E-A-T、站點在該主題的專業度、本地相關性 | 左側「Discover」成效報表（達最低曝光門檻才顯示） |

（來源：Google Search Central「Get on Discover」；Google News Publisher Center 說明「Google News transitions to automatically-generated publication pages」「How Google News ranks」；查閱 2026-11-03）

**規範**：任何想取得時效流量的專案，都以「Top stories + Discover」為主要目標，Google News App 為附帶；不再為「申請 Google News」投入任何流程。

**為什麼**：三者資格皆為自動；Google News 的獨立產品流量對台灣與東南亞市場的內容站而言通常遠小於 Discover。Preferred Sources（2025-08 上線，2026 已支援所有語言）讓使用者把你的網站設為偏好來源後，Top stories、AI Mode 與 AI Overviews 更可能顯示你的內容並加上「preferred」標章；只有網域或子網域層級可被選為來源，子目錄不行（來源：Google Search Central「Preferred Sources」，查閱 2026-11-03）。

**怎麼做**：
1. 確認網站不違反 Google 搜尋垃圾內容政策、Search features 政策與 Google News 內容政策（20.11）。
2. 每篇時效文章具備：可見的發布時間（含時區）、署名、作者頁、大圖、Article / NewsArticle 結構化資料。
3. 提交 news sitemap（20.3）；在頁面與社群放 Preferred Sources 按鈕或深連結（`https://www.google.com/preferences/source?q=https://example.com`）。
4. 在 GSC 分開追蹤 Web（含 Top stories 曝光，無獨立篩選項）、News（搜尋類型）、Discover 三份報表。

**驗收方式**：目標關鍵字手機實搜出現在 Top stories；News 搜尋類型與 Discover 報表開始有資料；news sitemap 狀態成功。

**常見錯誤**：把「沒有被 Google News App 收錄」當作問題去申訴（已無申請機制）；在子目錄 `/news/` 經營新聞卻期待 Preferred Sources 單獨列出（需子網域）。

---

## 20.2 Google News Publisher Center 現況

**已變更（2025-02-10 公告，2025-03 至 2025-04 完成）**（來源：Google News Publisher Center 說明 answer/15898024，查閱 2026-11-03）：

| 項目 | 現況 |
|---|---|
| 新增 / 提交出版品 | **已停用**。無法再手動把網站提交到 Google News |
| 出版品頁面（publication page） | 全面改為**自動生成**；手動建立的頁面不再顯示；部分出版品可能沒有自動頁面 |
| RSS feed / 網址區段（sections） | Google News **不再使用** Publisher Center 提交的 feed 與網址 |
| 標誌與出版品名稱 | 改用網站的 **favicon 與 site name**（來自結構化資料與頁面訊號，詳 06-結構化資料規範.md 的 Organization / WebSite） |
| 地區限制發布 | 已停用；預設全球發布，使用者依自己的語言 / 地區設定看到內容 |
| YouTube 內容提交 | 已停用；自動納入考慮 |
| Google Assistant 朗讀 | 美國以外停止；不想被朗讀可加 `<meta name="google" content="nopagereadaloud">` |
| 仍可做的事 | News Showcase 與 Reader Revenue Manager 的標誌上傳、News Showcase 面板的國家允許 / 封鎖 |

**規範**：新專案不建立 Publisher Center 出版品（除非要用 Reader Revenue Manager 做訂閱 / 打賞）；既有出版品不再維護 sections。

**為什麼**：以前「Publisher Center 審核通過」是進入 Google News 的門票；現在門票是「符合政策 + 被索引 + 網站訊號清楚」。資源應轉到 favicon、site name、Organization 結構化資料與作者頁。

**怎麼做**：
1. favicon：至少 48×48 的倍數、`<link rel="icon">` 可被抓取、所有頁面一致。
2. site name：`WebSite` 結構化資料的 `name` + `alternateName`、`<title>` 一致、`og:site_name`。
3. Google News 出版品頁面的名稱必須與 news sitemap 的 `<news:name>` 完全相同（扣除括號內文字）。

**驗收方式**：在 news.google.com 搜尋你的站名能看到自動生成的出版品頁；GSC 的「Google 新聞」報表有資料。

**常見錯誤**：沿用舊教學去 Publisher Center「新增出版品」找不到按鈕；多個子品牌共用同一 favicon 導致 Google News 混淆來源。

---

## 20.3 新聞 Sitemap 規範

**規範**（來源：Google Search Central「News sitemaps」，查閱 2026-11-03）：
- 只放**最近 2 天（48 小時）內發布**的文章；更舊的 URL 要移除，或移除其 `<news:news>` 標籤。
- 單一 news sitemap 最多 **1,000** 個 `<news:news>` 標籤；超過就拆分並用 sitemap index。
- 每個 `<url>` 只能有一個 `<news:news>`。
- 必填：`<news:publication>`（含 `<news:name>`、`<news:language>`）、`<news:publication_date>`（W3C 格式，首發日期而非加入 sitemap 的日期）、`<news:title>`（與頁面標題一致，不含作者、出版品名、日期）。
- `<news:language>` 用 ISO 639（2–3 碼）；繁中 `zh-tw`、簡中 `zh-cn`；印尼語 `id`。
- 新文章加進**既有** news sitemap，不要每次更新都建新檔；Google 抓 news sitemap 的頻率與抓站內其他頁相當。
- 沒有近 2 天文章時 sitemap 可為空；GSC 會顯示「空的 Sitemap」警告但無害。
- 可獨立成 `news-sitemap.xml` 並在 GSC 單獨提交，方便追蹤；一般 sitemap 另外維持。
- 已不再支援的標籤（**已停用**，2019 年起）：`<news:keywords>`、`<news:genres>`、`<news:access>`、`<news:stock_tickers>`；放了會被忽略但不報錯。

**範例**：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:news="http://www.google.com/schemas/sitemap-news/0.9">
  <url>
    <loc>https://example.com/news/2026/11/03/typhoon-land-warning-northern-taiwan</loc>
    <news:news>
      <news:publication>
        <news:name>Example Daily</news:name>
        <news:language>en</news:language>
      </news:publication>
      <news:publication_date>2026-11-03T08:15:00+08:00</news:publication_date>
      <news:title>Land typhoon warning issued for northern Taiwan</news:title>
    </news:news>
  </url>
</urlset>
```

**多語言站**：每個語言版本各自一個 `<url>` 與對應的 `<news:language>`；hreflang 另在一般 sitemap 或 HTML 內處理（詳 10-國際與多語言SEO.md）。

**為什麼**：news sitemap 是 Google 發現「新文章」最快的管道（配合首頁 / 分類頁內部連結）；48 小時限制讓 Google 只需抓小檔案就能看到所有新文。

**怎麼做**：CMS 自動產生（WordPress：Yoast News SEO、RankMath 的 News Sitemap 模組；自建：以 `publish_time >= now()-48h` 查詢動態輸出並快取 5–10 分鐘）；在 GSC 提交 `https://example.com/news-sitemap.xml`；robots.txt 內列出 `Sitemap:`。

**驗收方式**：GSC Sitemaps 報表狀態成功、類型顯示「新聞」；新文發布後 15–60 分鐘內 URL 檢查可見「已抓取」；Screaming Frog 以 List 模式載入 news sitemap 檢查全部回 200 且可索引。

**常見錯誤**：把全站 5 萬篇舊文塞進 news sitemap（超過 1,000 筆且違反 48 小時）；`publication_date` 用更新時間；`<news:name>` 與自動生成的出版品名不一致；news sitemap 被 CDN 快取 24 小時。

---

## 20.4 NewsArticle 結構化資料要點

> 完整 JSON-LD 範本與驗證流程詳 06-結構化資料規範.md；本節只列新聞 / 時效內容的要點。

**規範**（來源：Google Search Central「Article structured data」、Google News Publisher Center「Article page guidelines」，查閱 2026-11-03）：
- 類型：新聞用 `NewsArticle`，部落格 / 評測用 `BlogPosting` 或 `Article`；三者對 Search 的效果相同，`NewsArticle` 只是語意更明確。
- 建議屬性（無「必填」，但缺了等於白做）：`headline`（≤ 110 字元，過長會被截斷）、`image`（多張、各 ≥ 50,000 像素、含 16:9 / 4:3 / 1:1 三種比例；Discover 另要求 ≥ 1200 px 寬）、`datePublished`、`dateModified`（ISO 8601 含時區，例 `2026-11-03T08:15:00+08:00`）、`author`（`Person` 或 `Organization`，每位作者各一個物件，附 `url` 或 `sameAs`；`name` 只放名字，不放職稱 / 出版品名 / 「文 /」）、`publisher`（可省略，Google 會以 site name 與 favicon 判斷）、`isAccessibleForFree`（付費牆用，搭配 `hasPart` 標示付費區塊）。
- 不要用 `Thing` 當作者類型；不要把多位作者合併成一個 `name`。
- 連載 / 分頁文章：`rel=canonical` 指向各分頁自身或 view-all 頁，不要全指向第 1 頁。
- AMP：**已不再是 Top stories 的必要條件**（2021 年 Page experience 更新後取消），不需為新聞另做 AMP。

**為什麼**：Google 明說結構化資料不是 Top stories 的資格條件，但能幫助正確顯示標題、圖片、日期與作者，而「日期與署名」正是 Google News 透明度政策的核心。

**怎麼做**：CMS 模板輸出 JSON-LD；作者物件的 `url` 指向站內作者頁（含簡介、社群 `sameAs`）；圖片物件用 `ImageObject` 並提供三種裁切；更新文章時只改 `dateModified`。

**驗收方式**：Rich Results Test 無錯誤；GSC 強化報表（若 Google 偵測到）Error = 0；URL 檢查工具的「已轉譯 HTML」含 JSON-LD。

**常見錯誤**：`datePublished` 隨每次儲存變動；`image` 只給一張 800 px 的橫圖；作者 `name` 寫成「Example Daily 編輯部 / 記者 王小明」；在列表頁也輸出 `NewsArticle`（列表頁應用 `ItemList` 或不標）。

---

## 20.5 時效性內容的日期處理

**規範**：
1. 每頁只顯示**一組**清楚標示的日期：「發布」必有，「更新」在實質更新時才顯示；位置在標題與正文之間，含時間與時區。
2. 可見日期 = `datePublished` / `dateModified` = news sitemap `publication_date`（三者一致）。
3. `dateModified` 只在「使用者能察覺的實質變更」時更新：新增段落 / 資料、修正事實、更新數據表；修錯字、換圖、改版面、加內部連結不算。
4. 不得有未來日期；日期必須是「頁面」的發布 / 更新時間，不是事件發生時間（事件用 `Event` 標記）。
5. 不得把舊文「換日期重發」或「小改 + 轉址到新 URL」；Google News 指南明列此為違規（artificially freshened stories）。

（來源：Google Search Central「Provide a publication date」、Google News「Article page guidelines」，查閱 2026-11-03）

**為什麼**：Google 以多重訊號估計 byline date（可見日期、結構化資料、sitemap、首次抓取時間、頁面內其他日期），任一訊號矛盾就可能選錯或不顯示日期；Google 對「假更新」的偵測包括比對內容差異，實質未變卻一直更新日期會讓 `dateModified` 失去可信度，進而影響整站 sitemap `lastmod` 的可信度（詳 13-工具與監測.md 13.1.3）。

**怎麼做**：
- CMS 層：把「更新日期」設為需作者勾選「這是實質更新」才寫入；預設儲存不動 `dateModified`。
- 模板層：頁面只輸出一處 `<time datetime="2026-11-03T08:15:00+08:00">`；側欄「最新文章」列表的日期用純文字、不包 `<time>`，避免被誤判。
- 常青文章（evergreen）的年度更新：標題可含年份（「2026 年所得稅級距」），更新時**保留同一 URL**、更新正文與 `dateModified`、標題年份一併改；不要另建 `/2027/` 新頁再轉址。
- 多語言：各語言版本各自的日期，不要共用英文版的日期。

**驗收方式**：Google 搜尋結果顯示的日期與頁面一致；URL 檢查的已轉譯 HTML 中 `datePublished` 不隨重新儲存變動（可用 Screaming Frog Custom Extraction 抓 `datePublished` 做兩次爬取比對，變動的 URL 數應 ≈ 實際更新篇數）。

**常見錯誤**：WordPress 外掛「自動更新 modified date」全站開啟；在「更新日期」只顯示更新不顯示發布（Google 會把更新日當發布日，舊文看起來像新文，被判為刷新日期）；表格內的「資料截至 2026-10-31」被 Google 當成頁面日期（加上明確的「發布 / 更新」標籤即可）。

---

## 20.6 即時內容的頁面設計與索引策略

即時型內容（賽事比分、天氣 / 颱風、匯率、油價、股價、航班、停班停課）是流量站常見的高頻查詢來源，核心決策是 **URL 策略**。

### 20.6.1 兩種模式

| 模式 | 適用 | 做法 | 風險 |
|---|---|---|---|
| **A. 固定 URL 持續更新** | 查詢意圖是「現在的值」：今日匯率、今日油價、目前颱風動態、即時比分、今天停班停課 | 一個永久 URL（`/usd-twd-exchange-rate/`），內容區塊由 API 或編輯即時更新；`dateModified` 隨實質數據變動；頁面有歷史區塊（近 30 天表格） | 若只有一行數字會被判薄內容；更新頻率高但 Google 抓取跟不上時，摘要會顯示舊值 |
| **B. 每期 / 每日新頁** | 查詢意圖含「特定期數 / 日期」且有長期查找價值：第 X 期結果、某場比賽結果、某颱風的完整紀錄、某日匯率歷史 | 每期一個 URL（`/results/2026-11-03/`、`/typhoon/2026/uwan/`），加「本期 / 上期 / 下期」連結；固定的「最新一期」hub（模式 A）指向最新期 | 大量相似模板頁 → Crawled – currently not indexed；每日新頁的索引延遲 |
| **A + B 混合（建議）** | 大多數即時主題 | Hub 頁（模式 A，承接「最新」查詢、持續更新、累積權重）+ 期數頁（模式 B，承接「某期」長尾、作為歷史檔案）；Hub 內嵌最新一期的完整內容並 canonical 自指，期數頁也 canonical 自指（內容不同：期數頁含該期完整分析，hub 只含摘要 + 連結） | 若 hub 與最新期數頁內容幾乎相同，Google 會自選 canonical，造成排名在兩頁間跳動 |

**規範**：
- 「最新」查詢永遠由 hub 頁承接；hub 頁 URL 不含日期 / 期數。
- 期數頁每頁必須有**超出數據本身**的獨特內容（該期統計、對比、說明），否則改為只在 hub 的歷史表格列出、不獨立成頁。
- 即時數據區塊要在 HTML 中**伺服器端輸出**（SSR），不依賴前端 JS 拉 API；並在數據旁標示「更新時間」。
- 頁面上要有 Google 可抓取的靜態歷史（近 N 期表格），讓頁面在任何時刻都不是「只有一行數字」。

**為什麼**：Google 對同一 URL 的重新抓取頻率取決於歷史變動率與站點權重；hub 頁長期累積「這個 URL 每小時都在變」的訊號後，抓取頻率會提高。每日新頁則每天都是新 URL，需要重新被發現、抓取、評估，在抓取預算有限的中小站上常常 1–3 天後才索引，錯過時效。

**怎麼做（颱風 / 天氣範例）**：
- Hub：`/typhoon/`（「颱風最新動態」）— SSR 輸出目前所有活躍颱風、警報等級、更新時間；`WebPage` + `dateModified`。
- 個別颱風：`/typhoon/2026/uwan/` — 從生成到消散持續更新（模式 A 的子型態），結束後成為歷史檔案；標題含颱風名與年份。
- 停班停課：`/class-suspensions/`（hub）+ `/class-suspensions/2026-11-03/`（當日頁，含各地區完整列表與公告來源）。
- 比分：`/scores/league-a/`（hub：最新一場 + 近 20 場表）+ `/scores/league-a/2026-11-03/`（單場頁：該場比分、球員數據、統計）。
- 匯率：`/usd-to-twd/`（hub）；歷史用 `/usd-to-twd/history/2026-11/` 按月而非按日分頁（減少頁數）。

**索引加速**：news sitemap 只適用於「文章」性質的即時內容（如「颱風 X 升為強颱」快訊），hub 數據頁不放 news sitemap；一般 sitemap 的 `lastmod` 要真實反映 hub 更新；從首頁放置固定的「即時」區塊連結到所有 hub；IndexNow 送 Bing（Google 無即時 API，Indexing API 僅限 JobPosting 與 BroadcastEvent）。

**驗收方式**：hub 頁 URL 檢查的「上次抓取」在高峰期間為數小時內；期數頁 72 小時內索引率 ≥ 80%；GSC Pages 分頁中 hub 承接含「today / 今天 / latest」的查詢，期數頁承接含日期 / 期數的查詢。

**常見錯誤**：每日以新 URL 發「今日匯率」導致數百個薄頁；hub 頁只靠前端 JS 顯示數據，Googlebot 看到空白；兩種模式都用卻互相 canonical 混亂；即時頁放了 `max-snippet` 限制導致摘要不顯示數值。

---

## 20.7 Google Discover 的觸發特性

**規範**（來源：Google Search Central「Get on Discover」、Google Search Central Blog「February 2026 Discover Core Update」，查閱 2026-11-03）：
1. 圖片：≥ **1200 px** 寬、總像素 > 300,000、**16:9**；用 `max-image-preview:large`（robots meta）或 AMP 啟用大圖預覽；以 `og:image` 或結構化資料指定代表圖；不要用網站 Logo、文字圖、通用示意圖；手動裁切時保留主體。
2. 標題：反映內容本質、不誇大、不留懸念（clickbait）、不以聳動 / 獵奇 / 激怒為餌；預覽（標題 + 摘要 + 圖片）不可承諾內容沒有的東西。
3. 內容：people-first、原創、有深度、時效或獨特；站點在該**主題**上有持續產出（2026-02 更新明確改為「依主題判定專業度」：一個本地新聞站若有專門的園藝版面，可被視為園藝專家；影評站只寫一篇園藝文則否）。
4. 本地性：2026-02 更新後，Discover 更偏好使用者所在國家的網站；針對特定市場的內容站若主機、作者、內容語境都在當地，會比「海外團隊寫當地內容」更有利（待實證，屬 Google 公告的方向性描述）。
5. 頁面體驗：CWV 良好、無侵入式插頁、廣告不過量（Discover 流量以行動裝置為主，首屏廣告過多會拉高跳出並影響後續曝光）。
6. Discover 不會顯示：求職申請、連署、表單、程式碼庫、未標示的諷刺內容；套用 SafeSearch；避免令人震驚或不適的內容。
7. 違反 Discover 內容政策會收到**手動處置**（顯示在 GSC「安全性和專人介入處理」）。
8. 「Follow」功能已於 2025-11 從 Discover 移除（Google 已撤除相關文件），不再需要為此設定 feed；但 Preferred Sources（來源偏好）仍影響 Discover 的個人化。

**為什麼**：Discover 沒有查詢字，完全靠「使用者興趣 × 內容訊號」推送，所以圖片與標題承擔了 SERP 中「關鍵字相關性」的角色；而 Google 反覆強調 Discover 流量「不可預測、應視為補充」。

**怎麼做**：
- 模板：`<meta name="robots" content="max-image-preview:large">`；特色圖上傳規範 1600×900 以上；`og:image` 指向同一張。
- 編輯規範：標題先寫「事實版」再潤飾；禁用「你絕對想不到」「震驚」「竟然」類詞；標題與 H1 一致。
- 主題策略：流量站若有 10 個分類，Discover 通常只會對你「最厚」的 2–3 個主題持續推送；把產能集中。
- 監測：GSC Discover 報表分「頁面」看哪類主題被推；Discover 的 CTR 通常 3–8%，低於 2% 的頁面檢查標題 / 圖片是否誤導。

**驗收方式**：Discover 報表曝光穩定成長；Discover 來源的頁面平均互動時間（GA4）不顯著低於搜尋來源（若低很多表示標題誤導）。

**常見錯誤**：首圖用有大字的「標題卡」；為了 Discover 大量產出名人八卦、驚悚社會新聞（2026-02 更新後首當其衝）；把 Discover 流量當基準做預算（一次更新可以歸零）。

---

## 20.8 時效性查詢與 QDF 機制

**定義**：QDF（Query Deserves Freshness）是業界對 Google「對特定查詢提高新鮮內容權重」行為的稱呼。Google 並未以 QDF 為名發布文件，但在 2011 年「Freshness update」（基於 Caffeine 索引）公開說明：對正在發生的事件、定期重複的事件（選舉、賽事、季度財報）、需要最新資訊的主題（新手機評測），會更傾向顯示新內容；Google「How Search Works」頁亦說明以「freshness」作為部分查詢的排名因素（來源：Google Search Central「How Search works」；Google 官方部落格 2011-11「Giving you fresher, more recent search results」，查閱 2026-11-03）。

**規範**：對每個目標關鍵字判定其「新鮮度需求等級」，並以此決定更新節奏與內容型態：

| 等級 | 查詢特徵 | SERP 訊號 | 內容策略 | 更新節奏 |
|---|---|---|---|---|
| 突發（breaking） | 事件正在發生：颱風、地震、停電、名人事件 | Top stories、Live 標籤、結果日期都是數小時內 | 快訊（短）→ 持續補充 → 整理成完整報導 | 分鐘–小時 |
| 週期（recurring） | 每日 / 每期重複：比分、匯率、油價、停班停課 | 結果日期為當日；常見 hub 型頁面 | 20.6 的 hub + 期數頁 | 依週期 |
| 年度 / 季節 | 「2026」「今年」「最新」：稅率、申請流程、排行榜、評測 | 結果標題多含年份 | 常青頁年度更新，同 URL | 每年 + 有變動時 |
| 常青（evergreen） | 定義、教學、歷史 | 結果日期混雜，舊文也能排前 | 深度與完整性優先 | 每 12–18 個月檢查 |

**為什麼**：對「突發」與「週期」查詢，再好的舊文也會被新文擠下；反之對常青查詢頻繁改日期沒有幫助還會觸發 20.5 的問題。SERP 本身就是最準的 QDF 偵測器：前 10 名中有 ≥ 5 個結果日期在 7 天內 → 高新鮮度需求。

**怎麼做**：關鍵字研究表（詳 02-關鍵字研究與主題規劃.md）增加「新鮮度等級」欄；用排名追蹤器記錄 SERP 特徵（Top stories 出現與否）；對高新鮮度字設「事件日曆」（颱風季、選舉、開學、報稅季、雙 11）提前 2–4 週準備 hub 頁並在事件前更新。

**驗收方式**：事件期間 hub 頁在事件開始後 24 小時內進入 Top stories 或前 3 名；事件後 30 天仍保有長尾（期數頁）流量。

**常見錯誤**：事件發生後才建頁（抓取與評估需時，錯過高峰）；為常青字每週「更新」日期。

---

## 20.9 快訊與 Live blog

**規範**：
- 突發事件用**單一 Live blog 頁面**（固定 URL）持續追加更新，而不是每小時發一篇新文；事件結束後保留該頁並在頂部加「事件總結」。
- Live blog 使用 schema.org `LiveBlogPosting`，含 `coverageStartTime`、`coverageEndTime`（結束後填）、`liveBlogUpdate`（每則更新為一個 `BlogPosting`，含 `datePublished`、`headline`、`articleBody`）；`dateModified` 隨每則更新變動。
- 每則更新在 HTML 中有自己的時間戳與錨點（`#update-1030`），最新更新在最上方。
- 事件結束後 24 小時內把 `coverageEndTime` 填入並停止更新 `dateModified`。

**現況說明**：Google 曾於 2021 年為 Top stories 推出「LIVE」標籤並以 `LiveBlogPosting` 為訊號；但 Google 的結構化資料功能庫（Search gallery）2026-11 查閱時**未列出** LiveBlogPosting 專屬文件（Top stories 輪播的 AMP 版文件已移除）。2026-11-03 再次查證：搜尋圖庫 25 項無 LiveBlogPosting；〈Latest documentation updates〉2025–2026 無任何 LiveBlogPosting / live blog 條目；Article 文件僅列 `Article` / `NewsArticle` / `BlogPosting` 三種型別。因此：`LiveBlogPosting` 是合法的 schema.org 類型、Google 可理解、且業界持續觀察到 LIVE 標籤，但 **Google 目前沒有專屬文件與資格條件**，效果屬**專案執行時驗證**：上線後用 GSC「成效」看曝光／點擊變化（搜尋外觀沒有一般性的 Top stories 篩選項；來源：https://support.google.com/webmasters/answer/17011259 ，查閱 2026-11-03），並以目標關鍵字在手機實際搜尋觀察是否出現 LIVE 標籤；Rich Results Test 不會驗證 LiveBlogPosting（非支援類型），schema.org 語法用 Schema Markup Validator（validator.schema.org）驗。保守做法是同時滿足 `NewsArticle` 的所有建議屬性（`LiveBlogPosting` 是 `Article` 的子型別，屬性相容）。

**範例（精簡）**：
```json
{
  "@context": "https://schema.org",
  "@type": "LiveBlogPosting",
  "headline": "Typhoon X live updates: land warning for northern Taiwan",
  "datePublished": "2026-11-03T06:00:00+08:00",
  "dateModified": "2026-11-03T10:30:00+08:00",
  "coverageStartTime": "2026-11-03T06:00:00+08:00",
  "coverageEndTime": "",
  "author": {"@type": "Person", "name": "Maria Santos", "url": "https://example.com/author/maria-santos/"},
  "image": ["https://example.com/img/uwan-16x9.jpg", "https://example.com/img/uwan-4x3.jpg", "https://example.com/img/uwan-1x1.jpg"],
  "liveBlogUpdate": [
    {
      "@type": "BlogPosting",
      "headline": "Central Weather Administration issues land warning for northern Taiwan",
      "datePublished": "2026-11-03T10:30:00+08:00",
      "articleBody": "...",
      "url": "https://example.com/typhoon/2026/uwan/live/#update-1030"
    }
  ]
}
```

**為什麼**：一個持續更新的 URL 能累積外部連結與社群分享，並持續向 Google 發出「高變動率」訊號，比 20 篇各自 200 字的快訊更容易進入 Top stories；單篇快訊則容易被判為薄內容。

**怎麼做**：CMS 支援「live 文章」型態（更新列表 + 自動輸出 JSON-LD）；頁面標題含「live / 即時更新」；首屏放最新 3 則更新的摘要 + 事件背景一段（讓第一次抓取時就有足夠內容）；事件結束改標題為「颱風 X 完整紀錄」並保留所有更新。

**驗收方式**：schema 語法用 Schema Markup Validator（validator.schema.org）驗；Google 支援的 Article 屬性（`headline`、`image`、`datePublished`、`author` 等）另用 Rich Results Test 驗；LIVE 標籤效果只能用目標關鍵字在手機實際搜尋觀察；GSC 搜尋外觀沒有一般性的 Top stories 篩選項，只能看整體曝光／點擊變化（來源：https://support.google.com/webmasters/answer/17011259 ，查閱 2026-11-03）；事件期間 URL 檢查「上次抓取」為 1–2 小時內。

**常見錯誤**：每則更新一個新 URL 再互相轉址；live 頁只靠 WebSocket / JS 載入更新（Googlebot 看不到）；事件結束後把 live 頁 301 到「總結文」（丟掉已累積的訊號；應反過來把總結放進 live 頁頂部）。

---

## 20.10 新聞類網站的 E-E-A-T 與作者要求

**規範**（來源：Google News 內容政策「Transparency」；Google 搜尋品質評分者指南對 YMYL 與新聞的要求；查閱 2026-11-03）：
1. 每篇文章有**署名**（byline）與**日期**；署名連到作者頁。
2. 作者頁：真名或固定筆名、照片、簡介（專長領域、經歷）、聯絡 / 社群 `sameAs`、該作者的文章列表；用 `ProfilePage` + `Person` 結構化資料（詳 06）。
3. 網站層級：「關於我們」（編輯團隊、所有權、資金來源）、「編輯方針」（更正政策、消息來源政策、AI 使用政策）、「聯絡我們」（可用的 email 與實體地址）、`Organization` 結構化資料含 `foundingDate`、`address`、`contactPoint`。
4. 更正與更新要在文內註明（「更正：本文原稱…」），不得無聲修改。
5. 引用來源：一手來源（官方公告、原始文件、當事人）以超連結標示；改寫他站報導要連回原報導。
6. YMYL 時效內容（健康、金融、法律、災害）：作者或審稿者需具備可查證的資格，頁面標示「審閱者」。
7. 使用 AI 輔助：可用，但需有人工編輯負責，並在編輯方針中揭露；不要在每篇文章署名「AI」。

**為什麼**：Google News 政策要求新聞來源提供清楚日期與署名、作者 / 出版品 / 出版商資訊、背後公司或網路的資訊、聯絡方式；缺乏這些是被排除在新聞介面之外（而非只是降排名）的理由。Discover 的 2026-02 更新也以「站點在主題上的可證明專業度」為核心。

**怎麼做**：模板層強制 byline 與作者頁；建立「編輯方針」頁並從頁尾連結；每個作者至少 10 篇同主題文章再開始署名新主題（主題專業度累積）；外包寫手仍要以真實身分署名（或固定筆名 + 真實簡介），不要用「編輯部」當唯一作者。

**驗收方式**：Screaming Frog Custom Extraction 抓作者名 → 無作者的文章 = 0；作者頁 `ProfilePage` 無結構化資料錯誤；Organization 的聯絡資訊在 Rich Results Test 可見。

**常見錯誤**：所有文章署名「Admin」；作者頁只有名字無簡介；「關於我們」寫的是公司願景而非「誰在寫、誰負責」；更正政策頁存在但從未使用。

---

## 20.11 避免被判為新聞類垃圾

**規範**：下列行為在 Google 搜尋垃圾內容政策、Google News 內容政策或 Discover 政策中屬違規或高風險，新聞 / 時效型專案一律禁止：

| 行為 | 對應政策 | 風險 |
|---|---|---|
| 直接刊登新聞稿 / 通訊社稿件而無自家補充 | 「Scraped content」「原創性」；Google News 偏好 original journalism | 被視為重複 / 抄襲內容；多站同稿時只有一站能排 |
| 自動改寫（spin）他站報導、AI 批量改寫 | 「Scaled content abuse」（2024-03 起）、「Scraped content」 | 手動處置或演算法降級；Discover 直接消失 |
| 刷新日期 / 舊聞重發 | Google News「artificially freshened」 | 從新聞介面移除 |
| 在高權重站開「新聞 / 優惠」子目錄給第三方 | 「Site reputation abuse」（2024-05-05 生效，2024-11 起手動處置） | 該子目錄被移除索引 |
| 標題黨、預覽與內容不符 | Discover「Misleading content」、Google News「Misleading content」 | Discover 手動處置 |
| 廣告 / 贊助內容超過正文、未揭露贊助 | Google News「Ads & sponsored content」 | 從新聞介面移除 |
| 偽造署名、虛構作者 | Google News「Transparency」、「Deceptive practices」 | 從新聞介面移除；E-E-A-T 崩潰 |
| 自動產生無價值的「某地天氣今日」「某股今日股價」頁海 | 「Scaled content abuse」「Thin content」 | Crawled – currently not indexed 大量上升 → 整站品質訊號下降 |
| 以「返回鍵劫持」留住 Discover 流量 | 「Back button hijacking」（2026-04 新增垃圾政策，來源：Search Central 文件更新記錄） | 手動處置 |
| 在 AI Overviews / 生成式回應中操弄 | 2026-05 起垃圾內容政策明確適用於生成式 AI 回應 | 同一般垃圾處置 |

**怎麼做（合規的新聞稿 / 通訊社內容用法）**：
- 新聞稿：只摘要關鍵事實並加入自家分析、背景、當地影響、引用來源；若全文刊登，加 `rel="canonical"` 指向原始發布處或設 noindex。
- 通訊社稿（wire）：Google 會辨識同一稿件的多個版本並選擇一個顯示；若你不是原始來源，不要期望它帶來搜尋流量，可 noindex 以免稀釋站點品質。
- 翻譯外電：翻譯本身不算原創；加入在地脈絡、額外採訪或整理，並註明原文來源。
- AI 輔助：用於整理資料、草稿、校對；不得用於「一鍵生成 50 篇地區變體」。

**驗收方式**：GSC 手動處置 = 無；Crawled – currently not indexed 占新發布文章比例 < 20%；Discover 曝光未在核心更新後歸零。

**常見錯誤**：以為加了「來源：XX 通訊社」就不算抄襲；用「各城市天氣」程序化頁當新聞；在部落格站突然開「即時新聞」區塊大量發布改寫稿。

---

## 20.12 時效內容 → 狀況解法表

| 症狀 | 可能原因 | 診斷步驟 | 解法 | 預防 |
|---|---|---|---|---|
| 新文章發布 6–24 小時後仍未索引，錯過熱點 | 未在 news sitemap；首頁 / 分類頁未連到；抓取頻率低；站點新鮮度訊號不足 | URL 檢查看「發現方式」與「上次抓取」；確認 news sitemap 含該 URL；看抓取統計資料的每日抓取量 | 補 news sitemap、首頁即時區塊連結；IndexNow 送 Bing；短期可用 URL 檢查「要求建立索引」（每日有限） | 建立「發布 → sitemap 更新 → 首頁區塊 → 社群」自動流程；事件前先建 hub |
| 文章被索引但從未出現在 Top stories | 網站未被視為新聞來源；缺署名 / 日期；主題非新聞性；該查詢的 Top stories 由少數大媒體壟斷 | 以目標查詢手機實搜確認是否出現在 Top stories（GSC 無該篩選項）；檢查 byline / 日期 / Organization 資料；看該查詢 SERP 的 Top stories 來源 | 補 20.10 的透明度要素；從地方性 / 利基主題切入（大媒體覆蓋少）；申請 Preferred Sources 推廣 | 先在一個利基主題累積 50+ 篇原創再擴張 |
| Discover 流量在某天驟降 80% 以上 | Discover 核心更新（例如 2026-02）；內容轉向八卦 / 聳動；圖片不合規；Discover 手動處置 | 對照 Search Status Dashboard 日期；看 GSC 手動處置；比對驟降前後發布的文章主題與標題風格 | 若為更新：回到主題集中、提升原創深度、去除 clickbait，等待下次更新評估；若為手動處置：修正後重審 | Discover 不列入基準預算；標題與圖片規範寫進編輯 SOP |
| Google 顯示的日期錯誤（顯示舊日期或側欄日期） | 頁面有多個日期；可見日期與結構化資料不一致；只顯示更新日 | 檢視 HTML 中所有 `<time>` 與日期字串；Rich Results Test 看 `datePublished` | 統一為一組「發布 / 更新」日期並標籤化；移除側欄 `<time>` | 模板只允許一處 `<time>` |
| 更新常青文後排名反而下降 | 更新時刪除了原本排名的段落 / 關鍵字；URL 或標題改動過大；更新日期被判為假更新 | 比對更新前後版本（Wayback / Git）；GSC 看該頁查詢變化 | 還原被刪的內容再補新內容；標題只改年份 | 更新前先匯出該頁 GSC 查詢清單，確保更新後仍涵蓋 |
| 即時數據頁（匯率 / 比分）摘要顯示舊數值 | Google 抓取間隔長於更新頻率；數據只由 JS 載入；頁面被 CDN 長時間快取 | URL 檢查看 Googlebot 看到的 HTML 與時間；檢查 CDN cache header | SSR 輸出數值並在旁標時間；`Cache-Control` 設 5–15 分鐘；頁面加「資料更新時間」讓使用者理解 | 即時頁模板一律 SSR |
| 大量期數頁出現 Crawled – currently not indexed | 期數頁只有數字，模板化過重 | 抽 10 頁看獨特內容量 | 期數頁合併為月表，或補每期統計 / 分析；低價值期數頁 noindex | 期數頁最低內容門檻（如 ≥ 3 個獨特資料區塊） |
| Live blog 事件後流量歸零 | 事件結束，查詢消失（正常）；live 頁未轉為總結檔案 | GSC 看該 URL 查詢變化 | 改標題為「完整紀錄」、頂部加總結、內部連結到相關常青頁（防災指南、保險理賠） | 每個事件配套 1–2 篇常青頁承接後續需求 |
| 被判 Site reputation abuse（第三方內容） | 高權重站開放第三方「新聞 / 優惠碼 / 評測」區塊 | GSC 手動處置說明 | 移除或 noindex 第三方區塊；若保留需有自家編輯實質參與 | 第三方合作內容另用獨立網域 |
| news sitemap 顯示「空的 Sitemap」警告 | 48 小時內無新文（正常） | 看最近發布時間 | 無需處理 | — |
| 同一事件多篇文章互相競爭（內部競食） | 快訊、後續、整理各自成頁且標題相似 | GSC 看同一查詢在多個 URL 間跳動 | 合併為 live 頁或主文 + 明確分工標題（「即時」「完整分析」「影響」） | 事件報導採「一主頁 + 子題」架構 |

---

## 本章檢查清單

- [ ] 不再嘗試「提交到 Google News」；favicon 與 site name 正確（Publisher Center 已不管理這兩項）
- [ ] news sitemap：只含 48 小時內文章、≤ 1,000 筆、`publication_date` 為首發時間、`<news:name>` 與出版品頁一致，已在 GSC 提交
- [ ] 每篇文章：可見的發布（與必要時的更新）日期 + 時區；署名連到作者頁
- [ ] `datePublished` 不隨儲存變動；`dateModified` 只在實質更新時改；三處日期一致
- [ ] `NewsArticle` / `Article`：headline ≤ 110 字元、三種比例圖片、作者 `Person` 含 `url`
- [ ] Discover：`max-image-preview:large`、首圖 ≥ 1200 px 寬、16:9、非 Logo / 文字圖；標題無 clickbait
- [ ] 即時主題：hub 頁（固定 URL、SSR、含歷史表）+ 期數頁（有獨特內容）策略已決定並文件化
- [ ] 關鍵字表含「新鮮度等級」；高新鮮度主題有事件日曆與預建 hub
- [ ] 突發事件用單一 live 頁 + `LiveBlogPosting`，結束後改為總結檔案（不轉址）
- [ ] 作者頁（`ProfilePage`）、關於我們、編輯方針、更正政策、聯絡頁齊全；`Organization` 含地址與聯絡方式
- [ ] 禁止：直接刊新聞稿、自動改寫、刷新日期、第三方內容子目錄、返回鍵劫持、程序化「每日 X」頁海
- [ ] GSC 分別追蹤 Web、News（搜尋類型）、Discover（Top stories 無獨立篩選項，用實搜抽查）；Discover 不列入基準預算
- [ ] Preferred Sources 按鈕 / 深連結已放置（網域或子網域層級）
- [ ] 已知「已停用 / 已變更」：Publisher Center 手動提交與 sections、news sitemap 的 keywords / genres / access / stock_tickers 標籤、AMP 作為 Top stories 條件、Discover Follow 功能、Special announcement 結構化資料

## 參考來源

（皆於 2026-11-03 查閱）

- Google Search Central：Get on Discover（Discover and your website） https://developers.google.com/search/docs/appearance/google-discover
- Google Search Central Blog：Google's February 2026 Discover Core Update（2026-02-05） https://developers.google.com/search/blog/2026/02/discover-core-update
- Google Search Central：Preferred Sources https://developers.google.com/search/docs/appearance/preferred-sources
- Google Search Central：News sitemaps https://developers.google.com/search/docs/crawling-indexing/sitemaps/news-sitemap
- Google Search Central：Article structured data（僅列 Article / NewsArticle / BlogPosting；無 LiveBlogPosting） https://developers.google.com/search/docs/appearance/structured-data/article
- Google Search Central：Provide a publication date to Google Search https://developers.google.com/search/docs/appearance/publication-dates
- Google Search Central：Structured data features gallery（LiveBlogPosting 未列出） https://developers.google.com/search/docs/appearance/structured-data/search-gallery
- Google Search Central：文件更新記錄（Follow 移除、Back button hijacking、生成式 AI 垃圾政策等；2025–2026 無 LiveBlogPosting 條目） https://developers.google.com/search/updates
- Google News Publisher Center 說明：Google News transitions to automatically-generated publication pages（2025-02-10） https://support.google.com/news/publisher-center/answer/15898024
- Google News Publisher Center 說明：Google News content policies https://support.google.com/news/publisher-center/answer/6204050
- Google News Publisher Center 說明：How Google News ranks https://support.google.com/news/publisher-center/answer/9606702
- Google News Publisher Center 說明：Article page guidelines（技術要求） https://support.google.com/news/publisher-center/answer/9607104
- Google Search Central：Spam policies（Scaled content abuse、Site reputation abuse 等） https://developers.google.com/search/docs/essentials/spam-policies
- Google Search Central：How Search works（freshness） https://www.google.com/search/howsearchworks/
- Google 官方部落格：Giving you fresher, more recent search results（2011-11-03） https://blog.google/products/search/giving-you-fresher-more-recent-search-results/
- schema.org：LiveBlogPosting https://schema.org/LiveBlogPosting
- Search Engine Land：Google launches live label in carousel for live blog publishers（2021） https://searchengineland.com/google-launches-live-label-in-carousel-for-live-blog-publishers-236488
- Search Engine Journal：Google Releases Discover-Focused Core Update（2026-02） https://www.searchenginejournal.com/google-releases-discover-focused-core-update/566647
