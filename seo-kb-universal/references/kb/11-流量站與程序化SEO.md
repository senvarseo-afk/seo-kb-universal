# 11 流量站與程序化 SEO

> 版本：1.1 ｜ 更新日期：2026-11-05 ｜ 適用：所有 SEO 網站專案 ｜ 撰寫：Claude（§17 附錄整合 Grok 社群觀點）

## 本章摘要

1. 流量站的商業模式是「搜尋流量 × RPM／佣金」，兩個變數在 2025–2026 都承壓（AI Overviews 壓 CTR、聯播網門檻變動），所以定位必須從「資訊彙整」轉向「資料、工具、第一手經驗、在地化」四種 AI 難以取代的價值。
2. 程序化 SEO（pSEO）的合法邊界只有一條：**每一頁對應一個真實查詢需求，且有該頁獨有、來自資料而非模板的價值**；做不到就 `noindex`。
3. Google 的三條相關垃圾政策（scaled content abuse、site reputation abuse、expired domain abuse）於 2024-03-05 公布，scaled content abuse 與 expired domain abuse 隨公告生效，site reputation abuse 延至 2024-05-05 生效（https://developers.google.com/search/blog/2024/03/core-update-spam-policies）；2026 年仍以手動處置＋演算法並行執行；site reputation abuse 自 2026-08-30 起僅在 EEA 內不套用手動處置的排名影響。
4. AI 輔助內容產線必須是「研究 → 大綱 → 生成 → 事實查核 → 人審 → 發布 → 監測」七步，Google 官方要求「manually factcheck and review all AI-generated content」；省掉查核與人審的產線就是 scaled content abuse 的候選。
5. 站群的風險不在「擁有多站」，而在「同模板、同主機、同內容、互鏈」讓 Google 把它們視為一個操縱網絡；第二站只在第一站達到穩定（12 個月、營收與流量雙成長、已有可複製 SOP）後才開。

## 目錄

1. [流量站的定位與商業模式](#1-流量站的定位與商業模式)
2. [退出：出售平台與估值倍數現況](#2-退出出售平台與估值倍數現況)
3. [選題與利基評估框架（簡述）](#3-選題與利基評估框架簡述)
4. [程序化 SEO：適用情境與資料來源](#4-程序化-seo適用情境與資料來源)
5. [程序化 SEO：頁面模板設計](#5-程序化-seo頁面模板設計)
6. [程序化 SEO：品質門檻與索引控制](#6-程序化-seo品質門檻與索引控制)
7. [Thin content、Doorway、Scaled content abuse 的界線](#7-thin-contentdoorwayscaled-content-abuse-的界線)
8. [大量內容的品質管控流程](#8-大量內容的品質管控流程)
9. [AI 輔助內容產線 SOP](#9-ai-輔助內容產線-sop)
10. [站群策略與風險](#10-站群策略與風險)
11. [Site reputation abuse 與第三方內容的界線](#11-site-reputation-abuse-與第三方內容的界線)
12. [Expired domain abuse](#12-expired-domain-abuse)
13. [擴張策略：何時開第二站](#13-擴張策略何時開第二站)
14. [流量站 → 狀況解法表](#14-流量站--狀況解法表)
15. [本章檢查清單](#15-本章檢查清單)
16. [參考來源](#16-參考來源)

---

## 1. 流量站的定位與商業模式

### 1.1 定義與類型

流量站（content site / niche site / authority site）是以搜尋（與 Discover、社群）帶來的流量為資產、以廣告（AdSense、聯播網）與聯盟佣金為主要收入的網站。依規模與定位分三類：

| 類型 | 規模 | 收入結構 | 2026 年的處境 |
|---|---|---|---|
| Niche site | 50–300 頁、單一細分主題 | 聯盟為主 | 最脆弱：主題窄、品牌弱、AI 可直接回答 |
| Authority site | 500–5,000 頁、一個大主題的完整覆蓋 | 廣告＋聯盟＋自有產品／電子報 | 可存活：品牌搜尋、回訪、聯播網資格 |
| Programmatic / data site | 1,000–100 萬頁、資料驅動 | 廣告＋API／工具付費 | 兩極：有獨家資料的強、模板堆疊的被 scaled content 政策清掉 |

### 1.2 收入公式與 2026 的壓力點

```
月收入 = 工作階段 × 頁／工作階段 × Page RPM ÷ 1000 + 點擊出去的聯盟 × 轉換率 × 平均佣金
```

| 變數 | 壓力來源（2025–2026） | 對策（詳見章節） |
|---|---|---|
| 工作階段 | AIO 壓資訊型 CTR（Pew 8% vs 15%；Seer -61%；另一擴大樣本 2026 初回升，非同一序列）；Chartbeat：小型發布者兩年搜尋導流 -60% | 08 的選題轉向；Discover、電子報、社群分散（渠道評估見 §17） |
| 頁／工作階段 | AI 使用者「問完就走」 | 內部連結與工具型內容（03） |
| RPM | 東南亞流量 RPM 低；聯播網門檻變動 | 09 的市場分流與 GAM+MCM |
| 聯盟 | Amazon 佣金率低、平台政策緊 | 高價金融／保險／軟體類聯盟 |

### 1.3 定位規範

**規範**：每個流量站必須能用一句話說明「為什麼使用者需要點進來而不是看 AI 摘要」，且答案必須落在以下四類之一：(a) 獨家或整理成本高的資料（價格、時刻、費率、法規彙整）、(b) 互動工具（計算機、比較器、產生器）、(c) 第一手經驗（實測、實地、實拍）、(d) 在地化（特定國家／城市／語言的版本，AI 的訓練資料覆蓋薄）。

**為什麼**：Google 對 AIO 的定位是回答「可被摘要的問題」；Google 官方 AI 指引建議內容要有「unique value」；研究顯示被引用但不被點擊的多是「定義型、步驟型」內容。

**怎麼做**：盤點現有頁面，標記每頁屬於 a/b/c/d 或「無」；「無」且 12 個月無流量成長的頁面合併或刪除；新選題只做 a–d。

**驗收方式**：站內 ≥ 70% 的流量頁屬 a–d；GSC 曝光／點擊剪刀差（詳見 08）在這些頁不惡化。

**常見錯誤**：把「What is X」「X vs Y」大量化；以為加 FAQ 區塊就是價值；在地化只改了貨幣。

---

## 2. 退出：出售平台與估值倍數現況

查閱日期 2026-11-03；估值由市場決定，以下為各平台公開或二手整理的參考，交易前以平台當期數據為準。

| 平台 | 適合規模 | 估值方法 | 2025–2026 參考倍數 | 備註 |
|---|---|---|---|---|
| **Empire Flippers** | $50K–$5M | 2026-09-08 起改以年淨利 × 年倍數計價（換算：年倍數 × 12 ≈ 月倍數，例如 2x 年淨利 ≈ 24x 月淨利；https://empireflippers.com/switching-to-annual-multiples/） | 官方：2025 內容站平均成交約 2x 年淨利（≈ 24x 月淨利；https://empireflippers.com/how-to-sell-website/） | 審核嚴、佣金高（約 15% 遞減）；買家重視流量來源多元化與 AI 風險 |
| **Flippa** | < $250K 為主 | 淨利 × 倍數 | 內容／聯盟站約 25–40x（二手）；Flippa 自家 2026 H1 報告以「年」倍數呈現，平均約 2.3x 年利潤、前四分位 4.7x | 審核寬鬆、品質參差 |
| **Motion Invest** | $1K–$50K | 月淨利 × 倍數 | 官方部落格：倍數過去兩年「大幅下降」，目前接近 30x | 專做內容站，可直接向平台出售 |
| **FE International** | $100K+ | SDE 倍數 | 2026-10-16 文章：私有網路事業整體約 3x–10x 年收益（SDE），內容站／部落格／電子報落在該區間中低段，FAQ 舉例旅遊部落格 3.5x（一手，查閱 2026-11-03） | 偏中大型 |
| **Acquire.com / 私下交易** | 各種 | 協商 | — | 內容站不是主力 |

**影響倍數的因素**（買家 due diligence 清單）：
- 流量來源：Google 占比 > 80% 會被折價；Discover、電子報、社群、直接流量加分。
- AI 風險：資訊型內容占比高、AIO 覆蓋高的主題折價；工具／資料／在地化加分。
- 收入來源：AdSense 單一來源折價；高階聯播網（Mediavine / Raptive）加分；聯盟多商家加分。
- 歷史：12 個月以上穩定或成長；核心更新後的跌幅與恢復。
- 可移轉性：聯播網帳號能否移轉（Mediavine、Raptive 需重新審核）；作者與品牌是否綁定站主本人。
- 合規：無手動處置、無 scaled content 痕跡、無 expired domain 歷史、揭露齊全。

**規範**：若有出售計畫，至少提前 12 個月開始「去個人化」（品牌作者、SOP 文件化、流量分散、收入多元）並保存完整 GA4 與 AdSense／聯盟報表存取權。

---

## 3. 選題與利基評估框架（簡述）

完整的關鍵字研究與主題規劃詳見 01-策略與專案流程.md 與 02-關鍵字研究與主題規劃.md。流量站特有的評分維度：

| 維度 | 問題 | 打分（1–5） |
|---|---|---|
| AI 可替代性 | 主題的頭部查詢是否多被 AIO 直接回答？（在一般搜尋結果查 20 個頭部詞，記錄是否出現 AIO；AI Mode 與 AIO 是不同功能，https://developers.google.com/search/docs/appearance/ai-features） | AIO 覆蓋 > 70% = 1；< 30% = 5 |
| 變現價值 | 該市場的 RPM 與聯盟佣金（09 的 RPM 矩陣） | 低 RPM 市場通用資訊 = 1；US 金融 = 5 |
| 資料可得性 | 有無公開資料／API 可做 a 類（資料）或 b 類（工具）內容 | |
| 第一手可行性 | 自己能否實測／實地／實拍 | |
| 在地化缺口 | 該語言／國家是否缺乏高品質內容（用 `hl`/`gl` 查看前 10 名品質） | |
| 競爭 | 前 10 名的網域權重與內容品質 | |
| 季節與壽命 | 常綠 vs 時效 | |
| 政策風險 | 是否落在 YMYL、Publisher Restrictions（賭博、酒、藥）| |

**規範**：總分 < 24（滿分 40）的主題不開站；AI 可替代性 ≤ 2 的主題即使其他分數高也不開。

---

## 4. 程序化 SEO：適用情境與資料來源

### 4.1 什麼是程序化 SEO

用結構化資料集 + 模板，自動產生大量針對「同型查詢」的頁面（例如「〔城市〕到〔城市〕巴士時刻」「〔幣別〕兌〔幣別〕匯率」「〔產品 A〕vs〔產品 B〕」）。John Mueller 曾稱程序化 SEO 常是「垃圾內容的旗幟」，並強調它與技術 SEO 是不同的東西；Google 不禁止方法，禁止的是結果（scaled content abuse、doorway）。

### 4.2 適用情境判斷

**規範**：只有同時滿足以下四條件才做 pSEO：
1. 查詢模式真實存在且可用資料區分（GSC 或關鍵字工具證明「〔變數〕+ 固定詞」有搜尋量，且不同變數的意圖不同）。
2. 每一頁都有該變數獨有的資料（至少 3 個欄位的值不同且對使用者有意義）。
3. 資料可持續更新（有來源、有更新頻率）。
4. 頁面在沒有搜尋引擎的情況下也會有人想用（內部搜尋、工具入口）。

| 適合 | 不適合 |
|---|---|
| 匯率、天氣、時刻表、費率、法規差異、地點（店家／學校／醫院）、產品規格比較、工具（計算機每個參數組合）、字典／詞彙、資料庫（藥品、食品營養） | 「〔城市〕最佳 SEO 公司」只換城市名的文章；「〔產品〕review」沒有實測；「〔關鍵字〕是什麼」用 LLM 生成；翻譯同一頁到 20 種語言未審校 |

### 4.3 資料來源

| 來源 | 範例 | 優點 | 風險 |
|---|---|---|---|
| 公開 API | 匯率（各央行、Open Exchange Rates）、天氣（OpenWeather）、地理（OpenStreetMap）、政府開放資料（data.gov.tw） | 可持續更新、可信 | 授權條款（有些禁止商用或要求標示）；API 失效 |
| 公開資料集 | 統計局、WHO、World Bank、Wikidata | 權威 | 更新慢；大家都有，無獨特性 |
| 自建資料 | 自己爬取並整理（注意版權與 robots）、問卷、實測、使用者提交 | **唯一能建立護城河的來源** | 成本高；爬取需合法 |
| 第三方商業資料 | 產品目錄（聯盟 feed）、商家資料庫 | 快 | 「thin affiliation」風險：直接用商家描述不加值會違規 |
| LLM 生成 | 用 LLM 填模板欄位 | 快 | **不可作為事實資料來源**；只能生成「非事實」的說明文字並經人審 |

**規範**：pSEO 頁面的核心欄位必須來自可驗證的資料（API／資料集／自建），LLM 只能用於潤飾說明文字，且說明文字不得是頁面的主要價值。

**怎麼做**：為每個資料欄位記錄「來源、授權、更新頻率、最後更新時間」，並在頁面顯示「資料來源：X，更新於 YYYY-MM-DD」。

**驗收方式**：資料字典（data dictionary）存在；抽 20 頁核對資料與來源一致。

---

## 5. 程序化 SEO：頁面模板設計

**規範**：模板必須有 ≥ 40% 的可見內容來自該頁的資料變數（非固定文案），並包含：獨特 title／H1、資料區塊、依資料動態生成的摘要、相關實體連結、更新時間、來源、結構化資料。

**為什麼**：Google 判斷 doorway 與 scaled content 的核心是「頁與頁之間是否只有關鍵字不同」；可見內容的資料占比是最直接的工程指標。

**模板結構**（以「〔城市 A〕到〔城市 B〕巴士」為例）：

| 區塊 | 內容 | 資料驅動？ |
|---|---|---|
| Title / H1 | 「Taipei to Kaohsiung Bus: Schedule, Fare & Travel Time (Updated Nov 2026)」 | 是（城市、更新月） |
| 首段摘要 | 依資料生成：「有 6 家業者、每日 42 班、票價 NT$300–NT$800、車程 4–6 小時；最早 00:30、最晚 23:30。」 | 是（由資料計算） |
| 核心表格 | 業者、出發站、班次、票價、車型、訂票連結 | 是 |
| 條件式區塊 | 若有夜車 → 顯示夜車段；若有折扣 → 顯示 | 是（有資料才出現） |
| 靜態說明 | 怎麼訂票、注意事項（每類路線一份，不是每頁重複同一段） | 部分 |
| 人工補充 | 編輯對熱門路線寫的實際經驗（Top 20% 頁面） | 是（人工） |
| 相關連結 | 反向路線、同起點其他終點、同終點其他起點 | 是 |
| FAQ | 只放資料能回答的問題（「最便宜是哪家」由資料算） | 是 |
| 結構化資料 | `Trip`／`BusTrip`、`BreadcrumbList`、`Dataset`（若提供資料下載） | 是 |
| 來源與更新 | 「資料來源：各業者官網，最後核對 2026-11-01」 | 是 |

**規範補充**：
- 靜態文案以「類型」為單位（不同路線類型不同文案），且總字數不得超過動態內容。
- 沒有資料的欄位不顯示「N/A」整段，直接隱藏區塊；若核心欄位缺失（例如沒有票價也沒有班次），該頁 `noindex`。
- title 不要用公式堆疊關鍵字（「Taipei Kaohsiung bus schedule fare time booking cheap」）。
- 圖片：每頁有該實體的圖（地圖、產品圖）而非同一張模板圖。

**驗收方式**：寫一個「模板相似度」腳本：隨機取 100 頁，去掉 HTML 後計算兩兩文字相似度（如 shingling），中位數 < 40%；人工抽 10 頁判斷「若只看這頁，是否知道它與其他頁的差別」。

**常見錯誤**：每頁 1,200 字裡 1,000 字相同；FAQ 以 LLM 對每頁生成相似問答；城市名替換進同一段「〔城市〕是一座美麗的城市」。

---

## 6. 程序化 SEO：品質門檻與索引控制

### 6.1 每頁獨特價值門檻

**規範**：頁面要被索引必須同時通過：
1. 核心資料欄位完整率 ≥ 80%（定義每個模板的核心欄位）。
2. 動態內容占可見文字 ≥ 40%。
3. 對應查詢有需求證據（關鍵字量、內部搜尋、或同型頁在 GSC 有曝光）。
4. 與站內其他頁相似度 < 60%。
5. 資料更新時間在合理期限內（匯率 1 天、時刻表 90 天、法規 365 天）。

不通過 → `noindex, follow`（保留內部連結傳遞）或不生成。

### 6.2 哪些頁該 noindex（或不生成）

| 頁型 | 處理 |
|---|---|
| 組合爆炸頁（A×B 全排列中沒有需求的組合，如「Taipei to Taipei」、兩個小鎮之間） | 不生成；或只生成有資料的組合 |
| 分頁（?page=N） | 每一頁自我 canonical，不要 canonical 到第一頁（https://developers.google.com/search/docs/specialty/ecommerce/pagination-and-incremental-page-loading） |
| 篩選／排序參數頁 | 只有內容與主頁真正重複時才 canonical 到主頁；篩選頁若有獨立需求（「高雄夜車」）才獨立 URL |
| 資料稀疏頁（< 80% 核心欄位） | `noindex, follow` |
| 搜尋結果頁 | `noindex`（Google 明言不要索引站內搜尋結果） |
| 過期資料頁（活動已結束、產品下架） | 保留 + 標示「已結束」+ 連到替代；長期無價值則 410 |
| 同語言地區複製頁（內容完全相同） | canonical 合併（詳見 10） |
| 作者／標籤／日期彙整頁 | 多數 `noindex`；有編輯價值的主題頁可索引 |

### 6.3 索引預算與推進節奏

**規範**：新 pSEO 區塊分批開放索引：第一批 ≤ 500 頁，觀察 4–6 週 GSC 的「已檢索但未索引」與「已找到但未索引」比例 < 20% 且有曝光後，再開下一批（每批最多前一批的 2 倍）。

**為什麼**：Google 對新站／新區塊的抓取預算有限；大量低品質頁會拉低整站的品質評估（Mueller：薄內容問題是「站級」而非「頁級」）。

**怎麼做**：sitemap 依批次拆檔並加 `lastmod`；內部連結從既有高權重頁導入（分類頁、hub 頁）；每批上線前跑第 6.1 門檻腳本。

**驗收方式**：GSC 頁面索引報告：pSEO 區塊「已索引」比例 ≥ 70%；「已檢索但未索引」< 20%；核心更新期間該區塊流量不劇烈下滑。

**常見錯誤**：一次丟 5 萬頁進 sitemap；用 `noindex` 後仍放在 sitemap；把 noindex 頁當 hub 連來連去。

---

## 7. Thin content、Doorway、Scaled content abuse 的界線

Google spam policies（查閱 2026-11-03）的定義與 pSEO／流量站的對應：

| 政策 | Google 定義（摘要） | 典型違規樣態 | 安全做法 |
|---|---|---|---|
| **Scaled content abuse**（2024-03 起） | 「many pages are generated for the primary purpose of manipulating search rankings and not helping users」，不論用 AI、人工或兩者混合；例子：AI 大量生成無價值頁、抓取／改寫／翻譯他站內容、拼接多頁內容不加值、建多個站掩蓋規模、充滿關鍵字但讀不通的頁 | 用 LLM 對 5,000 個關鍵字各生一篇「指南」；把 Reddit／YouTube 轉錄拼成文章；同一內容翻成 15 種語言 | 每頁有資料／經驗／在地化價值；人審；分批 |
| **Doorway abuse** | 為特定相似查詢建立的頁或站，把使用者導向中間頁；例子：多個網域／頁面針對不同地區或城市把使用者導向同一頁；「substantially similar pages that are closer to search results than a clearly defined, browseable hierarchy」 | 「〔城市〕水電工」200 頁都導向同一個表單；城市頁只換地名 | 每個城市頁有該城市的資料（店家、價格、法規）；有可瀏覽的層級 |
| **Thin affiliation** | 「product descriptions and reviews are copied directly from the original merchant」，無原創內容或附加價值；分銷網絡的 cookie-cutter 站 | 聯盟 feed 直接出頁；「Top 10 〔產品〕」沒有實測只有 Amazon 摘要 | 原創評測、實測數據、比較、價格歷史、篩選導覽 |
| **Thin content**（既是常見描述，也是正式手動處置類型「Thin content with little or no added value」；https://support.google.com/webmasters/answer/9044175） | 頁面對使用者幾乎沒有價值；Mueller：站級問題 | 大量 300 字「what is」頁 | 合併／刪除／加值 |
| **Keyword stuffing / hidden text** | — | pSEO 模板在頁尾塞 50 個城市名 | 相關連結限制在有意義的數量（≤ 20）並以使用者導向排列 |

**Google 對 AI 內容的官方立場**（using-gen-ai-content，查閱 2026-11-03）：不禁止 AI；要求符合 Search Essentials；「It is critical to manually factcheck and review all AI-generated content for accuracy」；大量生成無價值頁「may violate… scaled content abuse」；可考慮揭露內容如何產生；Merchant Center 的 AI 生成產品資料須標示。Search Quality Rater Guidelines 4.6.5／4.6.6 把「低努力、無編輯、無原創」列為最低品質。

**執行方式**：手動處置（GSC 會通知）＋演算法（核心更新與 spam update）。官方可確認的只有：2024-03-05 公告 scaled content abuse 為垃圾政策並以手動處置＋自動系統執行；2026-09-24 至 10-08 的 September 2026 spam update 官方公告只寫「applies globally and to all languages」，未點名任何垃圾類型（https://status.search.google.com/incidents/XhUDXP7A67iHCD2kmbVu，查閱 2026-11-03）。「2025-06 起針對 AI 量產站發手動處置」「2026-09 更新特別涵蓋 AI 量產」皆為社群推測／第三方報導，Google 未說明。

---

## 8. 大量內容的品質管控流程

**規範**：任何月產出 > 50 篇（或 pSEO > 500 頁）的站，必須有書面的品質管控流程，包含抽樣率、審核標準、退件處理、上線後監測四部分。

| 階段 | 動作 | 標準 | 工具 |
|---|---|---|---|
| 入口 | 選題需求證據 | 關鍵字量或 GSC 曝光證據；AI 可替代性評分 ≥ 3 | 02 的流程 |
| 生成／撰寫 | 依 brief 與模板 | brief 含目標查詢、意圖、必備資料、禁止事項 | 內容 brief 範本（15） |
| 自動檢查 | 相似度、字數分布、資料完整率、連結、結構化資料、可讀性、禁用詞 | 相似度 < 60%；核心欄位 ≥ 80%；無壞鏈；schema 無錯誤 | 自寫腳本 + Screaming Frog |
| 事實查核 | 每個數字、日期、名稱、法規對照來源 | 100%（AI 生成內容）；人工撰寫抽 30% | 查核清單；來源連結 |
| 人審 | 編輯評分：價值、原創、在地化、可讀 | 4 項各 ≥ 3/5，總分 ≥ 14/20 | 評分表 |
| 抽樣率 | AI 產線 100% 人審；pSEO 每批隨機 5%（≥ 30 頁）+ 全部自動檢查 | | |
| 發布 | 分批；sitemap；內部連結 | 第 6.3 節 | CMS |
| 上線後 30／60／90 天 | GSC 曝光／點擊／索引；停留；跳出；AI 引用 | 90 天無曝光頁列入「加值或 noindex」清單 | GSC API + Looker Studio（13） |
| 退場 | 12 個月無流量且無策略價值 | 合併、更新、noindex 或 410 | 每季內容審計（Content Audit） |

**驗收方式**：流程文件存在且有版本；每批有審核紀錄；季審計報告。

**常見錯誤**：只在上線前檢查、不看上線後表現；抽樣只抽「看起來好的」；把退件直接改幾個字重送。

---

## 9. AI 輔助內容產線 SOP

**規範**：AI 用於研究整理、大綱、初稿、改寫、翻譯初稿、結構化資料生成；**不用於**產生事實、數據、引用、評測結論、第一手經驗；每篇輸出都經事實查核與人審後才發布；在編輯政策頁揭露 AI 使用方式。

| 步驟 | 做什麼 | 人／AI | 工具（示例） | 產出與檢核 |
|---|---|---|---|---|
| 1. 研究 | 收集目標查詢、SERP 前 10 的結構與缺口、PAA、論壇問題、官方來源、自有資料 | AI 整理 + 人判斷 | Ahrefs／Semrush、GSC、AI Mode／Perplexity（看引用來源）、自有資料庫 | 研究包：查詢清單、來源清單（含 URL）、缺口清單 |
| 2. 大綱 | 依意圖排 H2／H3，每節標註「資料來源」「需要的獨特價值類型（a–d）」 | AI 草擬、人定稿 | LLM + brief 範本 | 大綱含每節的可擷取答案句（08） |
| 3. 生成 | 依大綱與研究包寫初稿；要求 AI 在每個事實旁標註來源編號；禁止 AI 自行補數據 | AI | LLM（長上下文、附研究包） | 初稿 + 來源標註 |
| 4. 事實查核 | 逐一核對數字、日期、名稱、法規、價格；移除無來源主張；用官方／一手來源替換二手來源 | 人（可用 AI 輔助比對） | 查核清單；WebFetch 類工具抓官方頁 | 查核表（每項：主張／來源／狀態） |
| 5. 人審 | 加入第一手經驗、在地化、觀點；刪除空泛段落；檢查可擷取性、語氣、混語自然度；評分 | 人（母語／領域編輯） | 評分表 | 評分 ≥ 14/20 才過 |
| 6. 發布 | title／meta／schema／圖片 alt（AI 可生成但人審）；內部連結；作者署名（真人）；AI 使用揭露 | 人 + 自動化 | CMS、schema 產生器 | 上線檢查清單（14） |
| 7. 監測 | 30／60／90 天 GSC 與 AI 引用；讀者回饋；更新排程 | 自動 + 人 | GSC API、Looker Studio、AI 可見度工具 | 更新或退場決策 |

**關鍵控制**：
- 「AI 不得補數據」是提示詞的硬規則，並在查核階段逐項驗證；LLM 的幻覺率在數字與引用最高。
- 作者署名用真實編輯（有作者頁與資歷），不用虛構人名；Google 未要求揭露 AI，但要求「accuracy, quality, relevance」。
- 同一提示詞批量生成 100 篇會產生結構雷同、句式雷同；每篇大綱必須不同、研究包必須不同。
- 圖片：AI 生成圖只用於示意，產品／地點／實測必須真實照片。
- 翻譯：MT 初稿後走第 4–5 步（詳見 10）。

**驗收方式**：每篇有查核表與審核紀錄；抽查 10 篇的事實錯誤率 < 2%；AI 產線文章 90 天的 GSC 表現不低於人工文章中位數。

**常見錯誤**：讓 AI「寫一篇 2,000 字關於 X 的完整指南」沒有研究包；把 ChatGPT 的引用直接貼上（常為虛構）；省略第 4 步；用 AI 寫「我實際使用了三個月」。

---

## 10. 站群策略與風險

### 10.1 Google 怎麼看多站

擁有多個網站本身合法；Google spam policies 明列的風險是「creating multiple sites with the intention of hiding the scaled nature of the content」（scaled content abuse）與「multiple domain names or pages targeted at specific regions or cities that funnel users to one page」（doorway）。此外連結相關的政策（link spam）涵蓋站群互鏈以操縱 PageRank（PBN）。

### 10.2 關聯訊號

| 訊號 | 風險程度 | 說明 |
|---|---|---|
| 站間互鏈（尤其頁尾、側欄、全站連結） | 高 | 最直接的 PBN 特徵 |
| 相同模板／主題／外掛指紋 | 中（推測） | 可識別的關聯訊號，但 Google 未公開以此降權；單獨不構成違規，「與其他訊號疊加則顯著」屬推測 |
| 相同主機／IP／AdSense pub ID／GA 帳號／WHOIS | 中（推測） | 可識別的關聯訊號（Google 技術上可取得 AdSense 與 GA 關聯），但 Google 未公開以此判定站群或降權；屬推測，單獨不違規 |
| 相同或改寫的內容 | 高 | 重複內容本身通常不違規；大量低價值複製／改寫且主要為操弄排名時可能構成 scaled content abuse（https://developers.google.com/search/docs/essentials/spam-policies#scaled-content） |
| 相同作者／品牌名稱 | 低（若真實） | 真實的多品牌出版集團很常見 |
| 相同導向（都把使用者導到同一個轉換頁） | 高 | doorway |

### 10.3 站群規範

**規範**：多站必須各自是「可獨立存在的品牌」：不同主題或不同市場、獨立內容、獨立編輯、不互相全站連結（只有在對使用者有意義時才做單篇內文連結且 `nofollow` 或 `sponsored` 不需要——真實推薦可 dofollow 但數量極少）、獨立 ads.txt 與各自合規。

**怎麼做**：
- 第二站與第一站的主題交集 < 20%；或同主題但不同語言／市場（這是 10 的多語言站，應是同一站的子目錄而非站群）。
- 技術可共用（主機、模板、團隊）——不必刻意「隱藏關聯」，刻意隱藏本身就是訊號；重點是內容與連結獨立。
- 內容不得互相改寫／翻譯複製。
- 用集團頁（「本站隸屬 XX Media」）公開關係是可接受的；頁尾 10 個站互鏈不可接受。
- 一個站受手動處置時，不要把內容搬到另一站（Google 明言「policy circumvention」）。

**驗收方式**：Ahrefs／Semrush 看站間連結數 < 5 條且皆為內文自然連結；內容相似度掃描跨站為 0；各站各自通過 14 的檢查清單。

**常見錯誤**：為了「權重」用舊站頁尾連新站；用同一批 AI 文章改標題分發到 3 個站；用 expired domain 建 5 個「支援站」連主站（PBN）。

---

## 11. Site reputation abuse 與第三方內容的界線

**定義**（Google spam policies，查閱 2026-11-03）：第三方內容「published on a host site mainly because of that host's already-established ranking signals」，目的是借主站權重讓內容排得比自己放更好。

**時間軸**：2024-03 公布、2024-05-05 開始手動處置 → 2024-11-19 更新：即使主站有「參與或監督」（白標、授權、部分持股），「No amount of first-party involvement alters the fundamental third-party nature of the content」→ 2026-08-30 起（Google 2026-08 公告）：EEA 內使用者看到的結果不再受此手動處置影響，受影響區塊可能在系統中被「分離」獨立排名；**EEA 外完全照舊**；GSC 仍會通知，可提重審與調解。

**判斷標準**（Google 列出的考量）：內容是否有「sufficient input, editorial oversight, or contribution from the host site to be considered fully integrated」；主站是否控制頁面設計、品質、作者；內容是否以相同或近似形式出現在其他站。

| 不違規（Google 明列） | 違規樣態 |
|---|---|
| 通訊社、新聞稿站；新聞站之間的聯合發布 | 新聞站上的「優惠券」「貸款比較」「產品評測」子目錄由外部聯盟團隊營運，且未與主站整合、無署名／編輯責任、主要借主站訊號排名（整合良好、經策展的優惠券合作官方列為「不太可能」處置；https://developers.google.com/search/docs/essentials/spam-policies#site-reputation） |
| 論壇、留言等 UGC | 教育機構網域租給賭場／貸款內容 |
| 專欄、投書、評論等編輯內容 | 「客座文章」頁面由 SEO 公司供稿並付費，主站不審 |
| 經主站直接提供給讀者的贊助／廣編內容 | 白標「評測」由第三方供稿、同時出現在多個主站 |
| 有正確連結標記的聯盟連結、嵌入的第三方廣告單元 | 把第三方內容放在子網域假裝獨立 |

**對流量站的規範**：
- 不出租子目錄／子網域給第三方。
- 不接受「付費客座文章」作為主要收入；贊助內容依 09 第 11 節標籤與 `rel="sponsored"`。
- 若與第三方合作做內容（例如由保險比較平台供稿），由本站編輯主導選題、改寫、審核、署名，且內容不得同時出現在其他站。
- 自己「寄生」別人的高權重站（在 Medium、LinkedIn、新聞站投放大量 SEO 文）：對方站受罰、自己不會直接受罰，但流量不可控且 2024 後此類頁面多已被清理，不作為策略。

**驗收方式**：GSC 手動處置報告無項目；站內第三方供稿頁 100% 有編輯審核紀錄。

---

## 12. Expired domain abuse

**定義**（Google spam policies）：「an expired domain name is purchased and repurposed primarily to manipulate search rankings by hosting content that provides little to no value to users」；例子：政府機構舊網域放聯盟內容、醫療慈善舊網域賣醫療產品、小學舊網域放賭場內容。

**規範**：
1. 不為了「繼承權重」購買與新主題無關的過期網域；若購買過期網域，新站主題必須與該網域的歷史用途一致或合理延續，且內容本身達到本章品質門檻。
2. 不用過期網域建 PBN 連主站。
3. 購買前查 Wayback Machine 歷史、是否曾有垃圾內容或手動處置（換所有人不保證清除既有處置，既有處置可能仍影響，取得 GSC 後先確認手動處置報告並視需要申請重審（https://developers.google.com/search/help/crawling-index-faq）；演算法效應與既有垃圾外鏈也會跟著網域；Mueller：舊網域的歷史狀態「需要時間擺脫」）。
4. 只有在原網域有大量垃圾／付費連結，且已造成或很可能造成手動處置時才 Disavow（官方條件；https://support.google.com/webmasters/answer/2648487），詳見 16。
5. 購買後先清理：移除所有舊內容的 404／410、檢查 robots、設定新的 GSC 資產、檢查有無殘留的惡意轉址。

**為什麼**：2024-03 起為明文垃圾政策；GSC 垃圾回報工具（2024-05）加入「expired domain abuse」選項，意味著對手可以檢舉。「高權重過期網域的繼承在 2024 後多被重置」為社群推測：2024-03 官方公告只定義 expired domain abuse 並說「it's fine to use an old domain name for a new, original site that's designed to serve people first」，未提及權重重置（https://developers.google.com/search/blog/2024/03/core-update-spam-policies，查閱 2026-11-03）。

**驗收方式**：購買決策紀錄含歷史用途與新用途的一致性說明；GSC 無手動處置。

**常見錯誤**：買 DR 60 的廢棄 NGO 網域做金融聯盟站；用 301 把過期網域導到主站「灌權重」（Google 的 expired domain 政策與 link spam 都涵蓋）。

---

## 13. 擴張策略：何時開第二站

**規範**：只有在第一站同時滿足以下條件後才開第二站；否則資源投入第一站的深度與多元流量。

| 條件 | 門檻 |
|---|---|
| 時間 | 上線 ≥ 12 個月、經歷 ≥ 2 次核心更新且淨流量成長 |
| 流量 | 月工作階段達到該市場聯播網門檻（例如 Journey 的 1,000 premium sessions 或 Raptive 的 25,000 pv）且 Google 占比 < 80% |
| 收入 | 連續 6 個月營收成長；RPM 矩陣已建立 |
| 流程 | 內容產線與 QA 流程（第 8、9 節）文件化並由非站主執行過 |
| 內容 | 第一站的主題已覆蓋 ≥ 70% 的核心關鍵字叢集（擴張的邊際報酬遞減） |
| 法遵 | 無手動處置；揭露、隱私、CMP 齊全 |

**第二站的選型優先序**：
1. **同主題、新市場／語言**（例如單一市場站成功後擴到其他語言）：優先做成同站子目錄（10 的多語言站），只有在品牌、法規或出售需求下才獨立網域。
2. **相鄰主題、同市場**：可複用受眾與聯盟關係；主題交集 < 20%。
3. **完全不同主題**：最慢，但風險最分散。
4. **把成功站的子主題拆出去**：通常是錯的——拆分會失去權重與內部連結，除非該子主題需要獨立品牌或要賣。

**組織**：每站獨立的編輯負責人、獨立的 GSC／GA4 資產、獨立的 ads.txt；共用的只有技術平台與 SOP。

**退出考量**：若計畫出售，獨立網域比子目錄易售；但要在開站時就決定，之後遷移成本高（詳見 03 的遷移規範）。

---

## 14. 流量站 → 狀況解法表

| 症狀 | 可能原因 | 診斷步驟 | 解法 | 預防 |
|---|---|---|---|---|
| 核心更新後整站流量 -40% 以上 | 站級品質評估下降：薄頁比例高、AI 量產、資訊型內容被 AIO 吃掉 | 對照更新日期；分頁型看跌幅（pSEO 區、AI 文、舊薄頁）；GSC 曝光／點擊剪刀差 | 內容審計：合併／加值／noindex 薄頁；補第一手與資料型內容；等下一次核心更新驗證（通常 2–4 個月） | 第 8 節季審計；選題只做 a–d |
| GSC 收到 scaled content abuse 手動處置 | AI／模板量產頁無價值 | 讀處置範圍（整站或部分） | 移除或 noindex 受影響頁；人審剩餘；提交重審並附具體流程改變 | 第 9 節 SOP |
| GSC 收到 site reputation abuse 手動處置 | 第三方內容區塊 | 看處置指出的目錄 | 移除／noindex 該區塊或由本站編輯完全重做；重審；手動處置的直接效果限 EEA 外，EEA 內仍可能因該區塊被獨立評估而改變排名 | 第 11 節 |
| pSEO 頁「已檢索但未索引」> 50% | 相似度高、資料稀疏、無內部連結 | 抽 30 頁跑相似度與完整率 | 補資料欄位；提高動態比例；hub 頁導入連結；不合格頁 noindex | 第 6 節門檻腳本 |
| pSEO 頁有索引但零曝光 | 無真實查詢需求（組合爆炸） | GSC 以 URL 前綴看曝光分布 | 只保留有曝光／需求證據的組合；其餘 noindex 或 410 | 第 4.2 節條件 1 |
| 流量穩定但收入下滑 | RPM 下滑（季節、流量國別變化）或聯盟佣金率變 | 09 的 RPM 矩陣 | 09 的對策；調整內容投資到高 RPM 市場／主題 | 月 RPM 監控 |
| 多站同時下跌 | 站群關聯：互鏈、內容重複、同模板 | 檢查站間連結與內容相似度 | 移除互鏈；去重；各站補獨立內容 | 第 10 節規範 |
| 買來的過期網域新站起不來 | 歷史不相關、舊垃圾外鏈、演算法殘留 | Wayback；外鏈審計 | 符合官方條件（大量垃圾連結且已造成或可能造成手動處置）才 Disavow；主題對齊；時間 | 第 12 節 |
| AI 產線文章事實錯誤被讀者／媒體指出 | 省略查核 | 檢查查核表是否存在 | 立即更正並標示更正紀錄；全量回查同批文章 | 第 9 節第 4 步 100% |
| 想賣站但買家因 AI 風險砍價 | 資訊型占比高、Google 依賴 > 80% | 流量來源與內容類型分析 | 12 個月：分散流量、加工具／資料型內容、品牌搜尋 | 第 2 節提前準備 |
| AdSense 以「Low value content」拒絕 pSEO 站 | 模板頁被視為薄 | 看索引率與動態內容比例 | 先改善或移除低價值 pSEO 頁面（補資料、提高動態比例、刪除稀疏頁），並以人工高品質文章（≥ 30 篇）補強後重送；noindex 不影響 AdSense 審查（https://support.google.com/adsense/answer/48182） | 09 第 1 節 |
| 第二站拖垮第一站 | 資源分散、SOP 未成熟 | 比較兩站的內容產出與品質分數 | 暫停第二站，回填第一站 | 第 13 節門檻 |

---

## 15. 本章檢查清單

- [ ] 每個流量頁可歸類到 a 資料／b 工具／c 第一手／d 在地化；「無」類頁面已有合併／退場計畫。
- [ ] 主題評分 ≥ 24/40 且 AI 可替代性 ≥ 3 才開站或開新主題。
- [ ] pSEO：四個適用條件全部成立；資料字典含來源、授權、更新頻率；頁面顯示來源與更新時間。
- [ ] pSEO 模板：動態內容 ≥ 40%；核心欄位完整率 ≥ 80% 才索引；相似度中位數 < 40%；無「N/A」區塊。
- [ ] pSEO 索引分批（首批 ≤ 500）；「已檢索但未索引」< 20% 才開下一批；搜尋結果頁、稀疏頁、組合爆炸頁 noindex 或不生成。
- [ ] 月產 > 50 篇或 pSEO > 500 頁的站有書面 QA 流程、抽樣率、評分表、季審計。
- [ ] AI 產線：研究包 → 大綱 → 生成（禁補數據）→ 100% 事實查核 → 人審 ≥ 14/20 → 真人署名發布 → 90 天監測；編輯政策頁揭露 AI 使用。
- [ ] 多站：主題交集 < 20%（或為同站多語言）；無全站互鏈；無跨站內容複製；受處置內容不搬站。
- [ ] 無出租目錄／子網域；第三方供稿由本站編輯主導且不重複出現在他站；贊助內容依 09 標示。
- [ ] 過期網域：購買前查歷史；主題一致；不做 PBN；不 301 灌權重。
- [ ] 第二站門檻（12 個月、2 次核心更新、Google 占比 < 80%、SOP 文件化、連續 6 個月營收成長）全部達標才開。
- [ ] 若有出售計畫：提前 12 個月去個人化、流量與收入多元化、保存完整報表存取權。

## 16. 參考來源

（查閱日期皆為 2026-11-03）

- Google Search Central — Spam policies for Google web search（scaled content abuse、site reputation abuse、expired domain abuse、doorway abuse、thin affiliation）：https://developers.google.com/search/docs/essentials/spam-policies
- Google Search Central — Google Search's guidance about AI-generated content：https://developers.google.com/search/docs/fundamentals/using-gen-ai-content
- Google Search Central Blog — Updating our site reputation abuse policy（2024-11）：https://developers.google.com/search/blog/2024/11/site-reputation-abuse
- Google Search Central Blog — Update to the Site Reputation Policy（2026-08，EEA 調整）：https://developers.google.com/search/blog/2026/08/update-site-reputation-policy
- Google Search Central Blog — New ways we're tackling spammy, low-quality content on Search（2024-03；未提及過期網域權重重置）：https://developers.google.com/search/blog/2024/03/core-update-spam-policies
- Google Search Status Dashboard — September 2026 spam update（2026-09-24 至 10-08；只寫全球、全語言）：https://status.search.google.com/incidents/XhUDXP7A67iHCD2kmbVu
- Search Engine Land — Google site reputation abuse policy now includes first-party involvement（2024-11）：https://searchengineland.com/google-site-reputation-abuse-policy-now-includes-first-party-involvement-or-oversight-of-content-448432
- Search Engine Roundtable — Google: technical SEO vs programmatic SEO are different（Mueller）：https://www.seroundtable.com/google-technical-seo-vs-programmatic-seo-39473.html
- Search Engine Roundtable — Google: thin content issues are site specific：https://seroundtable.com/google-thin-content-issues-33202.html
- Search Engine Roundtable — Google report spam tool adds site reputation & expired domain abuse（2024-05）：https://www.seroundtable.com/google-report-spam-tool-adds-options-37479.html
- Search Engine Roundtable — Google: old domain history needs time to be shaken off：https://www.seroundtable.com/google-old-domain-history-40184.html
- Empire Flippers — Switching to annual multiples（2026-09-08 起改年淨利倍數）：https://empireflippers.com/switching-to-annual-multiples/
- Empire Flippers — How to sell a website（2025 內容站平均約 2x 年淨利）：https://empireflippers.com/how-to-sell-website/
- Google Search Central — AI features and your website（AIO 與 AI Mode 的差異）：https://developers.google.com/search/docs/appearance/ai-features
- Google Search Central — Pagination and incremental page loading（分頁自我 canonical）：https://developers.google.com/search/docs/specialty/ecommerce/pagination-and-incremental-page-loading
- Google Search Console Help — Manual Actions report（Thin content 類型、規避處置）：https://support.google.com/webmasters/answer/9044175
- Google Search Central — Crawling and indexing FAQ（換所有人與既有處置）：https://developers.google.com/search/help/crawling-index-faq
- Google Search Console Help — Disavow links（使用條件）：https://support.google.com/webmasters/answer/2648487
- Google AdSense Help — AdSense Program policies：https://support.google.com/adsense/answer/48182
- Motion Invest — 部落格（倍數近 30x 的說明）：https://www.motioninvest.com/
- FE International — Website and content business valuation multiples in 2026：https://www.feinternational.com/blog/website-and-content-business-valuation-multiples-in-2026
- Flippa — Insights（Digital M&A Insights Report H1 2026；內容站倍數以當期報告為準）：https://flippa.com/insights（查閱 2026-11-03）
- Press Gazette — Reuters Institute / Chartbeat：Google 導流 -33%（2026）：https://pressgazette.co.uk/publishers/digital-journalism/google-traffic-down-2025-trends-report-2026/
- Google Search Quality Rater Guidelines（4.6.5 / 4.6.6 低品質與 scaled content 判定）：https://static.googleusercontent.com/media/guidelines.raterhub.com/en//searchqualityevaluatorguidelines.pdf

---

## 17. 附錄：SEO 以外的曝光與點擊渠道（社群實測，2026-11-05）

來源：Grok 整理 r/SEO、r/juststart、r/Blogging、r/Pinterest、Facebook niche site 社團、BlackHatWorld、Indie Hackers 與東南亞站長社群的討論，全為社群主張；Claude 整合。各市場的渠道盤點見 25 §4；Discover 與 Google News 的規範見 20 章。完整整理見 《社群調查-SEO-AEO-曝光點擊最大化-2026-11-05》（原始報告未隨附）。

### 17.1 渠道評分表

| 渠道 | 流量潛力 | 東南亞適用 | 對 AdSense RPM | 起步做法 | 陷阱 |
|---|---|---|---|---|---|
| Google Discover | 極高但不穩定 | 中 | 中偏低 | 封面圖 1,200px 以上、時效或情緒標題、穩定更新、Web Stories（20 §20.7） | 無法主動提交；標題黨被砍；流量來去快 |
| Google News／Top Stories | 中高 | 中 | 中高 | News sitemap、原創時效、作者頁、Publisher Center（20） | 聯盟文與薄內容進不去；被踢出難回 |
| Pinterest | 高、複利 | 弱（美英強） | 美英中高 | 商業帳號、直式圖 2:3、關鍵字描述、每週批量釘圖、季節性重釘 | 多數人做三週沒爆就放棄；圖不直連文章 |
| YouTube／Shorts | 中 | 高 | 中低 | 關鍵字標題、前 15 秒留人、描述放連結、Shorts 導長片再導站 | 觀看量不等於點擊；Shorts 外連極差 |
| TikTok | 曝光極高、點擊極低 | 極高 | 低 | 本地語口播 15–45 秒、Bio 放連結、一題多剪、導到快載入頁 | 「娛樂流量，不是點擊流量」；連結在 Bio 流失大半 |
| Facebook 社團／粉專 | 高 | 極高 | 中低、量大 | 先經營社團再養粉專、原生語言、討論型貼文、適度外連 | 過度外連限流；互動誘餌；share group 造成無效流量（22 §5） |
| Reddit | 中（美英） | 弱 | 中 | 先貢獻再偶爾連、對子版規則、AMA 與真實案例 | 新站硬發必 ban；自推被當 spam |
| Threads／X | 低 | 中 | 低 | 專業人設、鉤子第一句、串文末放連結 | X 連結貼文觸及差，幾乎要付費 |
| Email newsletter | 慢但穩 | 中 | 最高 | 站內浮層或文末蒐集、週更一封、前三封自動序列、每封一個主 CTA | 彈窗傷 UX；買名單；發太勤退訂 |
| Web push | 中 | 中 | PV 升 RPM 常降 | 延遲詢問、分類訂閱、頻率上限、深夜少推 | 一進站就問；狂推導致封鎖與廣告品質分下降 |
| Bing／DuckDuckGo | 低競爭、總量小 | 弱 | 部分利基不差 | IndexNow、Bing Webmaster、標題直答（04） | 期待量等於 Google |
| Quora | 高峰已過 | 弱 | 中 | 完整回答、截圖步驟、文末自然連、經營 Space | 短答加硬廣；同一連結貼爆 |
| Flipboard／聚合 | 低 | 弱 | 中 | 申請 publisher、RSS 乾淨、封面一致 | 聯盟站多半審不過 |
| Telegram／WhatsApp／Viber／Zalo／LINE | 直達但粗 | 高（依國家） | 低，回訪可培養 | 頻道加討論群、每日 1–3 則、預覽圖加短連結、轉發到在地群 | 只廣播不互動；連結被平台限制；洗群被踢 |

### 17.2 最被低估與最被高估（社群主張）

- 最被低估：Pinterest（美英食譜、DIY 站 6 到 12 個月後流量複利）、Email（幾千訂閱比十萬社群粉穩，演算法變了信還在）、Facebook 社團（東南亞「粉專死、社團活」，在地語實用文在社團的點擊遠高於粉專讚數）。
- 最被高估：TikTok 導站（觀看破百萬、點進網站常只有數百）、X 有機曝光（要量幾乎得付費）、Reddit 自推（成功案例幾乎是先當長期居民）。

### 17.4 本附錄檢查清單

- [ ] 流量來源任一渠道不超過 50%；Email 或 push 至少一項有保底機制。
- [ ] 社群導流的落地頁先給完整答案再放廣告；爆發日降廣告密度。
- [ ] TikTok 與 Shorts 的 KPI 是品牌搜尋與回訪，不是站外點擊。
- [ ] Pinterest 只在美英受眾有量的主題做；東南亞不當主力。
