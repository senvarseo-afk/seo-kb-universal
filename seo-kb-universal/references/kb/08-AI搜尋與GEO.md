# 08 AI 搜尋與 GEO（生成式引擎優化）

> 版本：1.3 ｜ 更新日期：2026-11-09 ｜ 適用：所有 SEO 網站專案 ｜ 撰寫：Claude（§4.5 整合 Grok 社群觀點與 Codex 2026 年 Reddit 討論查證）

## 本章摘要

1. AI Overviews（AIO）與 AI Mode 已覆蓋 200+ 國家／地區、約 100 種語言（含台灣；繁體中文已支援），是所有專案的預設環境，不是「未來趨勢」。
2. 2025–2026 的研究一致指出：AIO 出現時自然點擊率大幅下滑（Pew：8% vs 15%；Seer：2025-09 樣本 -61%；另一擴大樣本（53 品牌、含商業與交易意圖）在其樣本內從 2025-12 約 1.3% 回升至 2026-02 約 2.4%，兩者不是同一時間序列；Ahrefs：第 1 名 CTR 約 -34.5%，2026 重跑後更差），但各研究量級不同，規劃時以「AIO 會持續壓低資訊型查詢 CTR」為前提。
3. Google 官方立場：出現在 AIO / AI Mode **沒有任何額外要求**，不需要 llms.txt、不需要特殊 schema；GEO 的本質仍是 SEO，差別在「可擷取性」與「實體一致性」的優先序提高。
4. 控制權：`Google-Extended` 只管 Gemini 訓練與 grounding、不影響 Search；Search Console 的「Search generative AI」控制項（2026-08-31 全球開放；同日另推出 Generative AI performance report，見 13 §13.1）可依 GSC 資產範圍退出 AIO / AI Mode / Discover AI（可按已驗證的子網域或子路徑資產設定；https://support.google.com/webmasters/answer/16908024），但退出就失去這些曝光與流量。
5. 零點擊時代的 KPI 要改：追蹤 AI 曝光（GSC Generative AI report 目前只有曝光；AIO / AI Mode 的點擊併入一般成效報表的 Web 總體資料）、品牌搜尋量、AI 引用次數、直接流量與訂閱／回訪，而不只盯點擊。AI 助理的導流仍遠小於 Google（Ahrefs 2026-10 樣本：0.46% 對 24.74%），引用與導流要分開追蹤（§2.3）。

## 目錄

1. [AI Overviews 與 AI Mode 現況](#1-ai-overviews-與-ai-mode-現況)
2. [對發布者 CTR 與流量的影響：研究數據](#2-對發布者-ctr-與流量的影響研究數據)
3. [Google 官方指引：有沒有「專門優化法」](#3-google-官方指引有沒有專門優化法)
4. [GEO 實務規範](#4-geo-實務規範)
5. [各 AI 引擎的引用來源機制與差異](#5-各-ai-引擎的引用來源機制與差異)
6. [llms.txt 的現況與爭議](#6-llmstxt-的現況與爭議)
7. [AI 爬蟲控制：誰該擋、誰不該擋](#7-ai-爬蟲控制誰該擋誰不該擋)
8. [依專案類型的策略調整](#8-依專案類型的策略調整)
9. [零點擊時代的 KPI 與量測](#9-零點擊時代的-kpi-與量測)
10. [在 GSC 看 AI 相關表現（現況）](#10-在-gsc-看-ai-相關表現現況)
11. [AI 搜尋 → 狀況解法表](#11-ai-搜尋--狀況解法表)
12. [本章檢查清單](#12-本章檢查清單)
13. [參考來源](#13-參考來源)

---

## 1. AI Overviews 與 AI Mode 現況

### 1.1 兩個功能的差別

| 項目 | AI Overviews（AIO） | AI Mode |
|---|---|---|
| 位置 | 傳統 SERP 最上方的 AI 摘要區塊，下方仍有 10 藍鏈 | 獨立分頁／入口，整頁都是對話式回答，追問會再查詢（query fan-out） |
| 觸發 | Google 系統判定「生成式 AI 特別有幫助」時自動出現 | 使用者主動切換，或由 AIO 的「深入了解」導入 |
| 來源連結 | 摘要旁／內嵌的引用卡片 | 回答內嵌的連結與右側／下方來源列 |
| GSC 計算 | 整個 AIO 區塊算同一個位置（通常 1），裡面所有連結共用 | 依搜尋結果元素計算；複合元素內的連結可能共用位置（https://support.google.com/webmasters/answer/7042828#ai-mode） |
| 範圍（2026-11 查閱） | 200+ 國家／地區、約 110 種語言 | 200+ 國家／地區、約 100 種語言（2026-02 一次新增 53 種） |

### 1.2 涵蓋國家與語言

- Google 官方 AI Mode 支援頁（查閱日期 2026-11-03）已列出：Taiwan、Indonesia、Malaysia、Singapore、Vietnam；語言包含 Chinese (Traditional)、Vietnamese、Malay、Indonesian。
- AI Overviews 官方支援頁同樣列出上述國家與語言。
- 時間軸：2024-05 美國英文上線 → 2024-10 擴至 100+ 國 → 2025-10 AI Mode 擴至 200+ 國家／地區、35+ 新語言 → 2026-02 AI Mode 再加 53 種語言 → 2026 I/O 後 Google 表示多語言模型讓新功能可在「數月內」而非「數年」推到所有市場。
- **對混語內容的意義**：Google 的語言偵測看可見內文，不看 `lang` 屬性（詳見 10-國際與多語言SEO.md）。混語頁面會被歸入「主要語言」，AIO 以該語言生成；混語本身不會被排除，但純在地語與純英文的查詢會各自觸發不同語言的 AIO，所以關鍵字研究要分語言做（詳見 02、25 §3）。

### 1.3 觸發查詢類型比例（2025–2026 研究）

| 來源 | 數據 | 查閱日期 |
|---|---|---|
| BrightEdge（2026-02-12，自家追蹤關鍵字集） | 約 48% 的追蹤查詢出現 AIO（2025-02 約 30–31%，原報告稱一年增 58%）；約 52% 查詢無 AIO | 2026-11-03（已核對原報告：https://www.brightedge.com/resources/weekly-ai-search-insights/ai-overviews-one-year-presence-size-citing） |
| 「Google 稱美國約 50% 查詢出現 AIO」 | 未找到 Google 官方原始發言（I/O、財報、官方部落格皆無）；Search Engine Roundtable 2026-07-30「近半數搜尋有 AIO」一文的數據實為 Similarweb（約 43%）與 Semrush（約 48%）的第三方追蹤，不是 Google 說法。本知識庫不引用此比例 | 2026-11-03（https://www.seroundtable.com/half-google-searches-ai-overviews-41780.html） |
| Semrush（2025-11，1,000 萬關鍵字） | 15.69%（2025-11；2025-01 為 6.49%，2025-07 高點 24.61%）；其他 Semrush 數據集 15–25% | 2026-11-03（一手：Semrush 原文，2025-12-15 發布） |
| Seer Interactive（49,358 查詢） | 資訊型 36%、商業型 8%、交易型 5% | 2026-11-03（https://www.seerinteractive.com/insights/aio-impact-on-google-ctr-2026-update） |
| Ahrefs（2025-04） | 觸發 AIO 的關鍵字 99.2% 為資訊型 | 2026-11-03 |
| Conductor（2026-05-20 至 06-20，1,610 萬次美國搜尋，672 個 Publishing 網域的查詢集） | Publishing 類搜尋 41.3% 出現 AIO | 2026-11-05（https://www.conductor.com/academy/2026-publishing-ai-search-benchmarks/） |

解讀：不同工具的關鍵字樣本差異很大（追蹤集偏向高量資訊詞），所以「比例」本身不可比，**可比的是方向**：資訊型／長尾／How-to／定義型查詢是 AIO 重災區；交易型、導航型、本地型相對安全。流量站以資訊型內容為主，受影響最深。

### 1.4 2026-11 介面觀察（未確認全面上線）

以下都是第三方觀察或 Google 主管的社群貼文，不是官方文件，出現頻率與地區不明（查閱 2026-11-08）。

| 日期 | 變化 | 對網站的意義 | 來源 |
|---|---|---|---|
| 2026-11-02 | 多個品牌字查詢的 AI Overviews 從主欄移到桌機右側欄，也就是知識面板的位置 | 品牌自家結果在主欄可能更顯眼，但 AI 對品牌的描述仍很醒目，要定期檢查描述是否正確（21 §6） | https://www.seroundtable.com/google-ai-overviews-brands-right-42440.html |
| 2026-11-04 | 美國 AI Mode 的居家服務結果加入預約連結，合作方為 Angi、Thumbtack、Housecall Pro、Jobber，ServiceTitan 之後加入 | AI Mode 從研究延伸到下單，見 17 §2 | Robby Stein X 貼文；Search Engine Journal、Angi 新聞稿 |
| 2026-11-04 | 單一查詢的 AI Mode 回答出現 4 則廣告 | 觀察者也不確定是否為新行為；商業查詢的自然引用可能被往下擠 | https://www.seroundtable.com/google-ai-mode-four-ads-42443.html |
| 2026-11-06 | AI Mode 出現「continue with this search」提示，並推使用者開啟 Personal Intelligence | 個人化程度提高，抽測 AI 結果時要記錄帳號狀態、地區與對話脈絡（21 §7.5） | https://www.seroundtable.com/google-ai-mode-continue-with-this-search-42475.html、https://www.seroundtable.com/google-personal-intelligence-popup-42468.html |
| 2026-11 | 有人回報 Google 測試從搜尋框移除 AI Mode 按鈕，報導者本人無法重現 | 入口位置在實驗中，不代表 AI Mode 停用 | https://www.seroundtable.com/google-removing-ai-mode-42436.html |

**怎麼用**：這些變化影響的是版面與點擊，不是排名。流量變動時，先拆分「排名掉」與「有曝光沒點擊」（08 §9），不要直接歸因到某個介面測試。

---

## 2. 對發布者 CTR 與流量的影響：研究數據

### 2.1 主要研究一覽

| 研究 | 方法 | 核心數據 | 注意事項 |
|---|---|---|---|
| **Pew Research Center**（2025-07 發布） | 900 名美國成人 2025-03 的瀏覽紀錄（Ipsos KnowledgePanel） | 有 AIO 時點傳統結果 8%，無 AIO 時 15%；點 AIO 內的連結僅 1%；看到 AIO 的使用者更常直接結束工作階段 | 單一市場、單月、面板自選；Google 公開質疑其方法 |
| **Ahrefs**（2025-04） | 30 萬關鍵字，比較 2024-03 vs 2025-03 的 GSC 第 1 名 CTR | 第 1 名 CTR 由 7.3% 降至 2.6%，扣除整體資訊型下滑後約 **-34.5%** | 相關非因果；桌機資料（https://ahrefs.com/blog/ai-overviews-reduce-clicks/） |
| **Ahrefs**（2026-02 重跑） | 同一方法，比較 2023-12 vs 2025-12 的第 1 名 CTR | 原始數據 7.3% → 1.6%，調整後約 **-58%** | 相關非因果；兩版比較區間不同，不可直接串成同一序列（https://ahrefs.com/blog/ai-overviews-reduce-clicks-update/） |
| **Seer Interactive v2**（資料截至 2025-09，2025-11-04 發布） | 42 個組織，2024-06 至 2025-09 | AIO 查詢的自然 CTR 由 1.76% 降至 0.61%（端點換算約 **-65%**，作者另報 **-61%**），付費 CTR -68% | 以 B2B／品牌客戶為主（https://www.seerinteractive.com/insights/aio-impact-on-google-ctr-september-2025-update） |
| **Seer Interactive v3**（2026-04-24） | 53 個品牌、547 萬查詢、2025-01 至 2026-02 | 其樣本內自然 CTR 從 2025-12 約 1.3% 回升至 2026-02 約 2.4%（樣本含商業與交易意圖，與 v2 不是同一樣本，不可接成同一時間序列）；AIO 查詢的付費 CTR 由 14.64% 升至 16.21% | Seer 自述：不能用 2025 外推 2026，仍應假設 AIO 持續壓低 CTR |
| **Reuters Institute × Chartbeat**（2026 Trends Report） | 2,500+ 發布者站 | 截至 2025-11 的一年，Google Search 導流全球 **-33%**（美國 -38%），Discover -21% | 新聞／媒體站為主 |
| **Chartbeat**（2026-03） | 兩年期 | 小型發布者（日 PV 1,000–10,000）搜尋導流 -60%，中型（10,001–100,000）-47%，大型（100,000+）-22%；整體 Google Search PV 2024-12→2025-12 -34%、Discover -16% | Chartbeat 原文（查閱 2026-11-03）+ Axios 報導（2026-03-17；Axios 頁本次無法讀取） |
| 隨機對照實驗（約 1,100 人，2025–2026；arXiv 2026-08） | 預註冊實驗，分組隱藏 AI 搜尋或強制使用 AI Mode | 「No AI Search」組點擊第三方發布者的比例 **+8.8 個百分點**；「強制 AI Mode」組 **-18.8 個百分點**（相對對照組） | 因果證據最強，但樣本小；研究期間 Google 改了 AIO 的 HTML，「No AI Search」組僅 51.1% 的 AIO 被成功隱藏，+8.8 要依此解讀（https://arxiv.org/html/2608.18352v1，2026-11-05 核對原文） |
| **SparkToro × Similarweb**（2026-06-08 發布） | Similarweb 點擊流面板，美國 Google 搜尋 | 2026 年 1 至 4 月零點擊 **68.01%**（2024 年 60.45%） | 僅美國；零點擊比例隨面板、裝置與定義差異很大，不同來源不可互比，也不可接成趨勢；未分離 AI 的因果貢獻（https://sparktoro.com/blog/in-2026-less-than-one-third-of-google-searches-still-send-a-click/） |

### 2.2 怎麼用這些數字做規劃

- **預算假設**：資訊型關鍵字的自然 CTR 以「過去基準 × 0.5–0.65」做保守估計；交易型與品牌型查詢不套這個折扣。
- **不要只看 CTR**：AIO 引用會帶來曝光（GSC 曝光上升、點擊下降是常見現象，但需用 Generative AI report 與排名、查詢拆解確認，不能直接當作 AIO 引用的證據），品牌搜尋與直接流量才是 AIO 曝光的下游指標（見第 9 節）。
- **Google 的反論**：Google 主張 AIO 帶來的點擊「品質更高」（bounce 較少）且使用者會問更複雜的問題；這點目前沒有第三方數據驗證，規劃時不要依賴。
- **2026-05 的調整**：Google 宣布 AIO 改版以「送更多流量給發布者」，包括訂閱標籤與「深入探索」連結區；實際效果各站不同，用自己的 GSC 分段驗證。

### 2.3 AI 導流規模與引用占比（查閱 2026-11-05）

**規範**：引用可見度、可歸因流量、收入三者分開量測，不把「被引用」當成「有點擊」，也不把 AI 導流當成搜尋流失的補償。

| 來源 | 樣本 | 數據 | 注意事項 |
|---|---|---|---|
| **Ahrefs AI vs Search**（2026-11-03 更新） | 118,671 站，2026-10，固定樣本 | Search 合計 27.55%，其中 Google 24.74%（2.978 億次）；AI 助理合計 0.46%，其中 ChatGPT 0.36%（430 萬次）、Gemini 18.33 萬次、Perplexity 6.13 萬次 | 只含使用 Ahrefs Web Analytics 的網站，不是全網；這是導向網站的流量，不是搜尋或提問量；AIO／AI Mode 的點擊算在 Google，不在 AI 助理內（https://ahrefs.com/benchmarks/ai-vs-search） |
| **BrightEdge**（2026-09-24 新聞稿） | 品牌網站的 AI 導流，2026-08 | ChatGPT 占 AI 導流 **95.1%**；2026 年 1 至 8 月 ChatGPT 導流 +101%；8 月 Gemini +1%、Claude -15%、Perplexity -17% | 分母是「AI 導流」，不是全部流量；新聞稿未見樣本與方法說明（https://www.brightedge.com/news/press-releases/brightedge-data-chatgpt-referral-traffic-doubles-in-2026） |
| **Conductor**（AEO 分析） | 美國，2026-01-01 至 05-31，1,300 萬+ Publishing 引用、672 個網域、69 萬+ 提示 | 引用占比 AI Mode **54.3%**、ChatGPT 19.4%、Perplexity 13.1%；AI Mode 平均每答 7 個引用 | 是樣本內的引用占比，不是用戶或導流占比；每答引用數多也會推高占比（https://www.conductor.com/academy/2026-publishing-ai-search-benchmarks/） |
| **Conductor**（AIO 分析） | 美國，2026-05-20 至 06-20，1,610 萬次搜尋 | Publishing 類的 AIO 引用 **57.8%** 來自自然排名前十以外的頁面 | 排名與引用要分開看；這不代表傳統 SEO 不重要（見下方解讀） |

**怎麼解讀**：

- 引用最多的 AI Mode 與導流最多的 ChatGPT 不是同一個平台，所以「引用占比」與「導流占比」不能互相代換。
- 第 1 列是規劃時最該用的尺度：即使 AI 導流持續成長，目前量級仍無法補回搜尋流失。
- 57.8% 的可能解釋之一是 query fan-out：頁面可能在子查詢排名前段，但不在原始查詢的前十。這是推論，Conductor 未說明，不可視為已證實。
- 以上數據都是美國或全球面板，東南亞市場沒有對等資料，套用到其他市場時只能看方向（25 章）。

**驗收方式**：月報能分開回答「被引用幾次」「AI 帶來幾次造訪」「這些造訪賺多少」（見第 9 節）。

**常見錯誤**：用 ChatGPT 的 95.1% 當成它與 Google 的流量比較；用引用次數向客戶證明流量成長；只追 Google 排名而不抽查 AI 引用。

---

## 3. Google 官方指引：有沒有「專門優化法」

**規範**：不為 AIO / AI Mode 做任何「專屬」技術工程；把資源放在可索引、可擷取、可驗證的內容與實體訊號。

**為什麼**：Google Search Central「AI features and your website」（2025-05-21 新增；另有 2026-05-15 新增的「Optimizing for generative AI features」指南，以及 2026-06-15 文件更新對 llms.txt 的澄清：Google 搜尋不需要也不使用該檔；https://developers.google.com/search/updates，查閱 2026-11-03）明文：
- 「There are no additional requirements to appear in AI Overviews or AI Mode.」
- 「You don't need to create new machine readable files, AI text files, or markup to appear in these features.」
- 「There's also no special schema.org structured data that you need to add.」
- 資格條件只有一個：頁面已索引、且符合可帶 snippet 顯示的標準 Search 技術要求。AIO / AI Mode 建立在核心排名與品質系統之上，用的是同一個索引。
- Google 對 GEO 的定調：「optimizing for generative AI search is optimizing for the search experience, and thus still SEO.」並明確不背書 llms.txt、「內容切塊（chunking）」工程、以及人為製造的品牌提及。

**怎麼做**（官方列出的最佳實務，對應到本知識庫其他章節）：
1. robots.txt 與 CDN／主機層都允許 Googlebot 抓取（詳見 04）。
2. 內部連結讓重要頁可被發現（詳見 03）。
3. 頁面體驗良好（Core Web Vitals，詳見 04）。
4. 重要內容用**文字**呈現，不要鎖在圖片、影片或 JS 互動元件裡。
5. 圖片與影片作為輔助，並有對應文字說明。
6. 結構化資料必須與可見文字一致（詳見 06）。
7. Merchant Center、Business Profile 資料保持最新（電商／本地專案）。
8. 在 Search Console 驗證資產，用 URL 檢查工具確認控制項（`nosnippet`、`max-snippet`）被 Googlebot 看見。

**驗收方式**：URL 檢查工具顯示「已編入索引」且無 snippet 限制；GSC Generative AI report 出現曝光（見第 10 節）。

**常見錯誤**：花預算做 llms.txt、FAQ 堆疊、「AI 專用」隱藏文字；把 `max-snippet` 設太小導致無法被摘要引用；JS 渲染後才出現的核心段落。

---

## 4. GEO 實務規範

GEO（Generative Engine Optimization）在本知識庫的定義：**讓內容在被 LLM 檢索（retrieval）、擷取（extraction）、歸因（attribution）三個階段都勝出**。這三個階段對應的槓桿不同。「問題 → 答案」層的問題研究、答案區塊寫作、精選摘要 / PAA / 語音與聊天引擎的量測與狀況解法，詳見 21 章（AEO）。

### 4.1 容易被引用的內容特徵

**規範**：每一篇目標被引用的內容，必須同時具備「直接回答、可驗證資料、原創觀點、明確實體、更新日期」五項中的至少四項。

**為什麼**：
- 檢索階段：AIO / AI Mode 的 query fan-out 會把一個問題拆成多個子查詢去檢索索引，排名前段且與子查詢語意緊密的段落勝出（排名指子查詢，不一定是原始查詢；Conductor 的引用與排名落差見 §2.3）；Google 自述「rooted in core Search ranking and quality systems」。
- 擷取階段：LLM 偏好可獨立成立的段落（self-contained passage）——第一句就是答案、附數字、附條件、附來源。
- 歸因階段：多項 2026 研究（Semrush 32.5 萬提示；Digital Applied 5,000+ 查詢）顯示 Reddit、Wikipedia、YouTube、LinkedIn 等「人味＋實體明確」的來源在各引擎都排前段；原創第一手經驗（「I tried」型內容）在推薦類查詢被大量引用。

**怎麼做**：

| 特徵 | 具體做法 | 範例 |
|---|---|---|
| 直接回答 | H2 用問題句，下一段 40–80 字內給答案，再展開 | 「SIM 卡註冊要多久？」→「線上註冊通常 10–15 分鐘，電信業者的 app 都支援，截止日後未註冊會被停用。」 |
| 結構化 | 用表格放比較、用有序清單放步驟、用定義清單放術語 | 比較表欄位：項目／價格／條件／更新日期 |
| 數據 | 每個關鍵主張附數字＋來源＋日期；自有數據（問卷、測試、爬取統計）最強 | 「我們測了 12 款（2026-09）…」 |
| 原創 | 第一手經驗、自拍圖片、原始截圖、作者具名與資歷 | 作者頁含 `sameAs` 連到 LinkedIn／社群 |
| 權威 | 外部引用與提及（詳見 16）、Wikipedia／Wikidata 實體、維持一致的品牌名稱 | 品牌名在站內、社群、目錄完全一致 |
| 更新 | 顯示 `dateModified` 且真的有改內容；在首段標註「本文更新於 2026-11」 | 不要只改日期不改內容（可被偵測） |

**驗收方式**：對 20 個目標查詢手動在 AI Mode、ChatGPT Search、Perplexity 各查一次，記錄是否被引用、引用的是哪一段；用第三方 AI 可見度工具（詳見 13）做週追蹤。

**常見錯誤**：答案藏在第 5 段；用「許多專家認為」代替具體數據；表格做成圖片；同一品牌在不同平台拼法不一致。

### 4.2 段落可擷取性（passage extractability）

**規範**：每個 H2 / H3 下的第一段必須能脫離上下文單獨成立，長度 40–120 字，含主詞（不要用「它」「這個」開頭）。

**為什麼**：AI 引擎擷取的是段落而非整頁。Google 的 passage ranking 是以段落理解整頁與查詢的相關性；AI Mode 的 query fan-out 則是對相關子主題發出多次子查詢，兩者機制不同，官方並未說兩者都是段落層級檢索（https://developers.google.com/search/docs/appearance/ai-features）。「段落可獨立理解」是本知識庫的編輯策略，不是官方要求。

**怎麼做**：
1. 一個段落一個主張；主張句在前、證據在後。
2. 專有名詞第一次出現寫全名（含英文），之後才用簡稱。
3. 表格每列都能單獨讀懂（欄位名清楚、單位寫在格內）。
4. 避免「如上所述」「見下文」這類跨段依賴。
5. 程式碼、數據表外加一句文字摘要。

**驗收方式**：隨機抽 10 個段落貼進 LLM 問「這段在講什麼、可信嗎」，若需要上下文才懂，就是不及格。

**常見錯誤**：為了「可擷取」把每段都寫成 FAQ 式短句，整篇變成關鍵字堆疊；或是為了塞答案而重複同一句話多次。

### 4.3 實體與品牌一致性

**規範**：品牌／作者／產品在站內、結構化資料、社群、第三方目錄使用完全相同的名稱、描述與連結，並建立可被 Knowledge Graph 辨識的實體。

**為什麼**：LLM 回答時會把網頁內容與實體知識（Knowledge Graph、Wikidata、社群提及）對齊；名稱不一致會被視為不同實體，稀釋引用機率。Google 官方同時警告「inauthentic mentions」（人為製造的提及）不是有效做法。

**怎麼做**：
1. `Organization` / `Person` schema 含 `name`、`url`、`logo`、`sameAs`（社群、Wikidata、Crunchbase 等），全站一致（詳見 06）。
2. 作者頁具名＋資歷＋`sameAs`，文章用 `author` 指向作者頁。
3. 在 Wikidata 建立實體（需符合其收錄標準，不可自吹自擂）。
4. 品牌名稱的中英文、大小寫、空格固定一種寫法。
5. 真實的第三方提及：被媒體、論壇、目錄引用（詳見 16）。

**驗收方式**：Google 搜尋品牌名出現 Knowledge Panel；在 Gemini / ChatGPT 問「〔品牌〕是什麼」能得到正確描述。

**常見錯誤**：網站用「XX 旅遊網」、FB 粉專用「XX Travel」、schema 用第三種名稱；買「AI 提及」服務。

### 4.4 技術面：讓 AI 引擎讀得到

- 核心內容在伺服器端渲染（SSR）或至少在初始 HTML 中；AI 爬蟲多半不執行 JS（Googlebot 會，但 OAI-SearchBot、PerplexityBot 的 JS 支援有限；詳見 04、15）。
- 不要用 Cloudflare 等 WAF 把所有 bot 擋掉；區分「搜尋用」與「訓練用」bot（第 7 節）。
- `max-snippet` 不要設限（或設 -1）；`nosnippet` 只用在真的不想被摘要的頁。
- 提供乾淨的 `lastmod` sitemap，AI 引擎的新鮮度判斷倚賴它。

### 4.5 AdSense／聯盟內容站的 AEO／GEO 投入優先順序（社群共識，2026-11-05）

來源：Grok 整理 r/SEO、r/bigseo、HN、LinkedIn SEO 圈與 Lily Ray、Glenn Gabe、Cyrus Shepard、Aleyda Solis、Marie Haynes 等人的公開討論；Codex 查證 2026 年 1 到 11 月 r/SEO 高票討論串。全為社群主張，不是官方機制；完整整理見 《社群調查-SEO-AEO-曝光點擊最大化-2026-11-05》（原始報告未隨附）。

**規範**：把 AEO／GEO 當成現有內容結構的附加規格，不另開以 AI 引用為 KPI 的產線；只投入「高優先」五項，「中優先」有餘力再做，「低優先」不做。

**為什麼**：社群對 AEO 的態度高度一致。2026-10-22 r/SEO 高票討論直接把「GEO／AEO 取代 SEO」當賣服務的話術；2026-08 的「How much SEO do you do for AI」討論認為多數 AI 優化就是既有的可存取、結構清楚的內容加上可引用的答案與一致命名。AI 引用帶來的流量對 AdSense 站普遍被認為不划算：出現 AI Overviews 的資訊型 query，organic CTR 常掉 15–60%（社群主張，隨產業而異）；ChatGPT 與 Perplexity 的出處點擊量遠小於藍鏈，停留短、RPM 差；2026-08 有發布者回報被 AI 引用但資訊型 CTR 掉 25%，社群結論是 AI 可見度要另外追蹤，不能拿來補點擊損失。聯盟站的特殊風險是「被引用卻被移出購買旅程」，成為來源與保住佣金是兩個目標。

**怎麼做**

| 優先 | 做法 | 理由 |
|---|---|---|
| 高 | 資訊頁改答案優先結構：首段 40–80 字直接回答、H2 用問句、比較用 HTML table、步驟用有序清單、可見更新日期（§4.2、21 §4） | 同一套結構同時服務 SERP snippet 與 AI 抽取，成本最低 |
| 高 | 保住 Googlebot 可抓的完整 HTML 與內鏈（§4.4） | AI Overviews／AI Mode 走 Googlebot，技術壞了兩邊都沒有 |
| 高 | 原創數據、在地價格、實測，每季一篇小研究，標題含年份與市場，附可下載表 | 少數能被引用又做得出差異化的資產 |
| 高 | 定期更新會被 AI 摘要的金錢頁與比較頁，更新日期與內文一起動 | 新鮮度同時抗 CTR 下滑與過時被擠出引用 |
| 高 | 品牌與作者 entity：About、作者頁、跨網一致命名、Organization／Person schema（§4.3） | 沒有實體，模型和 Google 都傾向引用大媒體 |
| 中 | Reddit、Quora、當地論壇的真實參與、產業新聞具名 | RAG 愛引用第三方來源，但費時、難規模化 |
| 中 | 放行 OAI-SearchBot、PerplexityBot；訓練型 GPTBot、Google-Extended、CCBot 可擋（§7） | 成本近零，換少量品牌曝光 |
| 中 | 比較／「best」頁強化 E-E-A-T 與出處 | 聯盟轉換較可能發生在這裡，不是純定義頁 |
| 低 | llms.txt 當核心策略（§6）、AI 專用落地頁、付費 GEO 套餐、「保證進 AI Overviews」 | 社群普遍當話術 |
| 低 | 灌 FAQ schema、隱藏問答、為各 AI 引擎各寫一套文 | FAQ rich result 已退場（06）；沒有穩定排名機制，維護成本高過點擊 |
| 低 | 全面封鎖所有 AI 爬蟲 | 擋掉本就不多的引用，又擋不住 Google 零點擊 |

**驗收方式**：GSC Generative AI 報表的曝光（§10）與頁面層級 CTR 變化分開看；GA4 的 AI 引擎推薦流量（21 §7.3）單獨成管道，不併入自然搜尋 KPI。

**常見錯誤**：把「被引用次數」當 KPI；把資訊型頁的 CTR 下降一律歸因 AI（2026-08 一個案例細看是 bot、曝光下降與 query mix 改變疊加，12 §12 (1)）；為了 AEO 另寫一套內容。

---

## 5. 各 AI 引擎的引用來源機制與差異

| 引擎 | 檢索來源 | 引用特性（2026 研究） | 對發布者的意義 |
|---|---|---|---|
| **Google AI Overviews / AI Mode** | Google 自家索引；query fan-out 拆子查詢 | 傳統排名是基礎但不等於引用：Conductor 美國 Publishing 樣本 57.8% 的 AIO 引用來自自然排名前十以外（§2.3）；一個回答多個來源；Reddit、LinkedIn 常見；Wikipedia 在 AI Mode 僅約 2%（Semrush 2025-10） | 先贏傳統排名與子查詢，再優化段落可擷取性；排名與引用分開抽查；GSC 可見曝光 |
| **Gemini（app）** | Google 索引 grounding（受 `Google-Extended` 控制） | 與 AI Mode 類似；「更依賴 Knowledge Graph」為業界推測，未見量化研究或 Google 說明（2026-11-03 查證） | 實體一致性仍是最穩的做法 |
| **ChatGPT Search** | Bing 索引＋OpenAI 自有爬取（OAI-SearchBot）＋即時抓取（ChatGPT-User） | 每答引用數依研究而異（第三方統計約 8–10）；Yext（680 萬引用，本地品牌查詢樣本）：該樣本中 48.7% 引用來自第三方清單／目錄（Yelp、TripAdvisor、BBB 等），不代表 ChatGPT 整體偏好（https://investors.yext.com/news-events/press-releases/detail/376/yext-research-86-of-ai-citations-come-from-brand-managed）；Ahrefs 2025-08-11（15,000 個長尾提示，ChatGPT 資料 2025-07 初收集）：ChatGPT 內文引用僅 8.8% 落在 Google 前 100 名、8.0% 在前 10 名；「80% 被引頁面完全不在 Google 該查詢的排名內」是 ChatGPT／Gemini／Copilot／Perplexity 四家的整體彙整（不是等權平均），不是 ChatGPT 單獨數字（https://ahrefs.com/blog/ai-search-overlap/）；Reddit 引用比例波動大（2025-09 曾跌至約 10%） | Bing 可能是來源之一（Bing Webmaster Tools、IndexNow 仍值得做）；**允許 OAI-SearchBot 是官方列出的收錄條件**（https://developers.openai.com/api/docs/bots）；本地商家查詢中目錄與清單型頁面有優勢，要把目錄資料做齊（詳見 17） |
| **Perplexity** | 自有索引（PerplexityBot）＋即時抓取（Perplexity-User，通常不理 robots.txt） | 每答引用最多（第三方統計約 21.9）；偏好新聞媒體與論壇；YouTube 引用多 | 新鮮度與時效性內容有優勢；Reddit 討論串常被用作「人味」來源 |
| **Bing Copilot** | Bing 索引 | 與 ChatGPT Search 高度重疊 | Bing SEO 與 ChatGPT 同一套 |
| **Claude（含搜尋）** | 自有搜尋（Claude-SearchBot）＋使用者觸發抓取（Claude-User） | 引用數較少、偏官方文件與權威站 | 允許 Claude-SearchBot 即可 |

跨引擎重疊度：「ChatGPT 與 Perplexity 被引網域僅約 11% 重疊」在 2026 年廣為流傳，但原始研究未能取得——常被歸給 Averi（6.8 億引用；同一「6.8 億」數字也被指為 Profound 的資料集），Whitehat SEO 自述的 11.8 萬回答分析涵蓋四個平台且未公開方法與分母；僅第三方報導，未獲原始研究證實，不要引用具體百分比。可確認的一手數據是 Ahrefs（2025-08）：ChatGPT 內文引用只有 8.8% 落在 Google 該查詢前 100 名、8.0% 在前 10 名；「約 80% 被引頁面不在 Google 前 100」「約 12% 重疊」則是 Ahrefs 對 ChatGPT、Gemini、Copilot、Perplexity 四個平台的整體彙整，不是等權平均，原研究也分開計算內文引用與底部來源（來源：https://ahrefs.com/blog/ai-search-overlap/ ，查閱 2026-11-03）——意思是「在 Google 排第 1」不保證在 ChatGPT 被引用，反之亦然。實務上：Google 體系靠排名，ChatGPT 體系靠允許 OAI-SearchBot（Bing 可能是來源之一；目錄／清單型頁的優勢目前只在本地查詢樣本得到證實），Perplexity 靠新鮮度與論壇。

---

## 6. llms.txt 的現況與爭議

**規範**：不把 llms.txt 列為必要項目；若團隊想放，視為「無害的零成本實驗」，但不能擠掉任何 SEO 工作，也不能據此宣稱有效。

**現況（查閱 2026-11-03）**：
- **Google**：Gary Illyes（2025-07 Search Central Live）表示 Google 不支援、也沒有計畫支援；John Mueller 2025-06 指出「伺服器日誌顯示 AI bot 根本不去抓這個檔」，2026-05 稱其為「purely speculative for now」，並把它比作當年的 meta keywords；Google 官方 AI features 文件明言不需要「AI text files」。Google 自家某些產品網域雖有 llms.txt，Mueller 表示那「不是背書」。
- **OpenAI**：未公開承諾支援；有報導稱 OpenAI 的爬蟲曾抓取 llms.txt，但 OpenAI 爬蟲文件未提及，僅第三方觀察、未獲官方證實。
- **Anthropic**：自家文件站提供 llms.txt（作為開發者文件格式），未宣稱 Claude 搜尋使用它。
- **Bing / Perplexity**：未找到官方支援聲明（2026-11-03 再查仍無）。
- **採用率**（一手資料）：Rankability 2026-09-18 掃描 Tranco 前 10,000 網域，8.3% 確認有 llms.txt（前 1,000 為 9.3%；HTML／空檔／catch-all 回應不計）；Common Crawl 2026-07 爬取樣本中 11.72% 的 `/llms.txt` 請求回傳文字檔（非全網比例；68% 為平台模板自動產生，Wix 占 41%）。使用率：Ahrefs 2026-05 稱 97% 的 llms.txt 零請求（第三方報導）。結論：頭部網站約一成放置，AI 引擎幾乎不讀取。

**結論**：llms.txt 是供 LLM／agent 使用的網站資訊提案（https://llmstxt.org/），不是搜尋訊號；Google 已於 2026-06-15 文件更新澄清搜尋不需要也不使用它（https://developers.google.com/search/updates）。若 Mueller 提到的 WebMCP（讓 agent 與網站互動的標準）成熟，再評估；詳見 15 的檔案範本說明。

---

## 7. AI 爬蟲控制：誰該擋、誰不該擋

**規範**：預設**允許所有「搜尋／引用用途」的 bot**，**依商業判斷決定「訓練用途」的 bot**；絕不用整站 WAF 規則一刀切。robots 範本詳見 15-技術實作範本.md。

**為什麼**：各家已把「訓練」與「搜尋」拆成不同 user-agent，且文件明確說兩者獨立：擋訓練 bot 不會讓你退出搜尋，但擋錯 bot 會直接從 AI 答案消失。

| 業者 | Token / UA | 用途 | 擋了會怎樣 | 遵守 robots.txt |
|---|---|---|---|---|
| Google | `Google-Extended` | Gemini 模型訓練＋Gemini app / Vertex AI 的 grounding | **不影響** Search、不影響 AIO / AI Mode（官方：「does not impact a site's inclusion in Google Search nor is it used as a ranking signal」） | 是（它不是獨立爬蟲，只是 robots token） |
| Google | `Googlebot` | Search 索引（AIO / AI Mode 同一索引） | 停止爬取，但 robots.txt 不保證移出索引（已索引或被外連的 URL 仍可能出現在結果中）；要退出搜尋應使用 Googlebot 可讀取的 `noindex`；AI 功能的使用另由 GSC 控制項管理（https://developers.google.com/search/docs/crawling-indexing/robots/intro） | 是 |
| Google | Search Console「Search generative AI」控制項 | 以 GSC 資產為範圍退出 AIO / AI Mode / Discover AI 功能（可按已驗證的子網域或 URL-prefix 子路徑資產設定，子資產可覆寫父資產） | 失去這些曝光與流量；官方稱不作為一般排名訊號 | 不適用（GSC 設定） |
| OpenAI | `OAI-SearchBot` | ChatGPT 搜尋功能的索引與引用 | 從 ChatGPT 搜尋答案消失（仍可能以導航連結出現） | 是，更新後約 24 小時生效 |
| OpenAI | `GPTBot` | 模型訓練 | 只是表達不授權訓練 | 是 |
| OpenAI | `ChatGPT-User` | 使用者觸發的即時抓取 | 不影響搜尋收錄；robots 可能不生效 | 不一定 |
| Anthropic | `Claude-SearchBot` | Claude 搜尋索引 | 降低在 Claude 搜尋的可見度 | 是 |
| Anthropic | `Claude-User` | 使用者觸發抓取 | 使用者問到時抓不到你 | 是（官方建議用 robots，IP 封鎖不可靠） |
| Anthropic | `ClaudeBot` | 訓練 | 表達不授權訓練；支援 `Crawl-delay` | 是 |
| Perplexity | `PerplexityBot` | Perplexity 搜尋索引（官方稱不用於訓練） | 從 Perplexity 結果消失 | 是 |
| Perplexity | `Perplexity-User` | 使用者觸發抓取 | — | 官方文件：「generally ignores robots.txt」（2025-08 Cloudflare 曾指控其用未宣告 UA 繞過封鎖） |
| 通用 | `CCBot`（Common Crawl） | 開放資料集，被多家用於訓練 | 不影響搜尋 | 是 |

**趨勢數據**（原始資料集：Cloudflare Radar radar.cloudflare.com/bots；SEOmator 2026-10-10 整理，數字為 Radar 2026-01 至 2026-09 各月份）：AI bot 請求中「搜尋用途」占比由 2026-01 的 2.6% 升到 2026-09 的 10.6%（Cloudflare 於 7 月後修訂用途分類，7 月值由 11.6% 改為 5.6%，跨月比較要小心）；GPTBot 占比由 12.6% 降到 6.2%；Cloudflare Radar 2026-10-05 掃描 4,261 份頭部網域 robots.txt：GPTBot 被提及 703 次、被禁 546 次，OAI-SearchBot 允許 316／禁止 279（同一檔可同時含允許與禁止規則）。

**怎麼做**（決策）：
- 流量站／內容站：允許 `OAI-SearchBot`、`PerplexityBot`、`Claude-SearchBot`；`GPTBot`、`ClaudeBot`、`CCBot`、`Google-Extended` 依「內容是否為核心資產」決定——若內容是可被輕易重製的資訊彙整，擋訓練 bot 的實益有限；若是獨家資料／原創研究，可擋訓練並保留搜尋。
- 電商／SaaS：全部允許搜尋 bot；訓練 bot 通常也允許（產品被 AI 推薦的價值大於被訓練的損失）。
- 新聞／付費牆：擋訓練 bot，搜尋 bot 允許但配合 paywall 結構化資料（詳見 09）。
- Google 目標於 2027 年支援 IETF AIPREF 共用 AI 訓練控制（`user-agent: __usage_ai-training`），尚未承諾確切日期或年初上線（來源：https://developers.google.com/search/blog/2026/10/ai-training-control ，查閱 2026-11-03）；屆時檢視 15 的範本。

**驗收方式**：伺服器日誌每月統計各 UA 抓取量；用 robots.txt 測試工具確認規則；在 ChatGPT / Perplexity 搜尋站名能看到引用。

**常見錯誤**：Cloudflare「Block AI bots」一鍵全擋（包含搜尋 bot）；在 `User-agent: *` 區塊 Disallow 後忘了為搜尋 bot 開例外；誤以為擋 `Google-Extended` 可以退出 AIO。

---

## 8. 依專案類型的策略調整

| 專案類型 | 主要風險 | 優先策略 |
|---|---|---|
| **流量站（AdSense／聯盟）** | 資訊型查詢 CTR 腰斬；薄的「what is」「how to」頁最先被 AIO 取代 | (1) 砍掉可被一句話回答的頁，改做「需要看完整頁才有價值」的內容：工具、計算機、比較表、第一手測試、在地化資料（如各城市價格）；(2) 經營品牌與回訪（電子報、社群、PWA 推播）；(3) 把 RPM 做高來補點擊減少（詳見 09）；(4) 擴大到 ChatGPT／Perplexity 的引用面（允許 OAI-SearchBot；Bing 索引可能是來源之一） |
| **電商** | AIO 的購物模組與 AI Mode 的 agentic 購物會跳過品類頁 | Merchant Center 資料完整且即時；產品頁有獨家規格／評論／比較；`Product`、`Offer`、`Review` 結構化資料（詳見 06、19） |
| **企業官網／B2B** | 品牌描述被 AI 寫錯 | 實體一致性；About／產品頁用可擷取段落；在產業目錄與 LinkedIn 保持一致資料 |
| **SaaS** | 功能比較被 AI 直接回答 | 公開文件站（docs）SSR、可深連結；比較頁用自家數據；整合頁（integrations）做成程序化但每頁有獨特內容（詳見 11） |
| **本地商家** | ChatGPT 近半引用來自目錄 | Google Business Profile、Yelp、TripAdvisor、本地目錄資料一致（詳見 17） |
| **新聞／時效** | AIO 摘要新聞、Discover AI 摘要 | 付費牆標記、獨家報導、品牌訂閱；考慮 `max-snippet` 策略（詳見 20） |

---

## 9. 零點擊時代的 KPI 與量測

**規範**：每個專案的月報至少包含以下 6 個指標，且「AI 曝光」與「點擊」分開呈現。

| KPI | 來源 | 說明 |
|---|---|---|
| AI 曝光（AIO / AI Mode / Discover AI） | GSC Generative AI performance report | 目前只有曝光，無點擊、無查詢維度（2026-11 現況） |
| 整體曝光 vs 點擊剪刀差 | GSC Performance（Web） | 曝光升、點擊降只是需要拆解的現象，不能直接證明被 AIO 引用或因果關係；先用 Generative AI performance report 確認 AI 曝光，再分別分析排名、查詢與 CTR（https://support.google.com/webmasters/answer/7042828） |
| 品牌搜尋量 | GSC 查詢篩選「品牌詞」＋ Google Trends | AI 引用的下游效果；每月追蹤 |
| AI 引用次數／占比 | 第三方 AI 可見度工具（詳見 13）＋手動抽查 20 個查詢 | 分引擎記錄；同時記錄「引用的是哪個頁、哪一段」 |
| AI 來源的推薦流量 | GA4 預設管道「AI Assistant」（medium = `ai-assistant`，2026 新增；不含 AI Overviews / AI Mode，兩者仍算 Organic Search）＋自訂 regex 補漏（chatgpt.com、perplexity.ai、copilot.microsoft.com、gemini.google.com） | 預設管道可能漏算部分來源（第三方觀察：Perplexity、部分 ChatGPT 流量落在 Referral / Unassigned），GA4 採第一個符合的管道，自訂管道須排在 Referral 及其他會先匹配的管道之前，詳見 21 章 §7.3；來源 https://support.google.com/analytics/answer/9756891 （查閱 2026-11-04） |
| 直接／回訪／訂閱 | GA4、電子報工具 | 不依賴搜尋的流量基礎 |

**為什麼**：點擊已不能完整代表可見度；對廣告變現站而言，點擊仍是收入來源，所以要同時看「AI 曝光」與「每次點擊價值」。

**驗收方式**：月報包含上述 6 項、且能回答「AI 曝光成長時，品牌搜尋與直接流量是否跟著成長」。

**常見錯誤**：把 AI 推薦流量的 GA4 來源歸在 referral 不另拆；只報曝光成長掩蓋點擊下滑。

---

## 10. 在 GSC 看 AI 相關表現（現況）

查閱日期 2026-11-03：

1. **Performance（Web）**：AIO 與 AI Mode 的曝光、點擊、位置一直都算在「Web」搜尋類型內。
   - AIO：整個區塊算一個位置（通常 1），內部所有連結共用；連結要捲入可視區才算曝光。
   - AI Mode：依搜尋結果元素計算位置，複合元素內的連結可能共用位置；追問被當成新查詢，各自計算曝光／點擊（https://support.google.com/webmasters/answer/7042828#ai-mode）。
   - 同一 URL 在同一次搜尋出現多次只算一次曝光。
2. **Search Generative AI performance report**（2026-06-03 以 beta 推出，**2026-08-31 起全球所有網站可用**）：
   - 指標：只有**曝光**（「URL 出現在 Search 與 Discover 的生成式 AI 功能的次數」）。
   - 維度：頁面、國家、裝置（僅 Search）、日期（可到小時）。**沒有查詢維度、沒有點擊**。
   - 資料與主報告重疊（主報告仍包含這些曝光），不是加總。
   - 資料起算日：官方說明頁（16984139）與 2026-06-03 部落格公告皆未載明；多篇第三方文章稱資料自 2026-05-18 起、無回填，僅第三方報導，未獲官方證實。
3. **Search generative AI 控制項**（Settings → Search generative AI；支援頁 support.google.com/webmasters/answer/16908024）：
   - 三種狀態：include（預設）／exclude／inherit（子資產預設繼承最近的父資產）；控制以 GSC 資產為範圍，已驗證的子網域與 URL-prefix 子路徑資產可覆寫父資產，不是只能整站設定。
   - 排除後連結與內容不再出現在 AIO、AI Mode、Discover AI 功能；官方稱不影響其他搜尋排名；不影響 AI 訓練（那是 `Google-Extended` 的事）。控制項只涵蓋 AI Overviews、AI Mode 與 Discover 的生成式 AI 功能，不等於退出 Search（來源：https://support.google.com/webmasters/answer/16908024 ，查閱 2026-11-03）。
   - 生效通常數天，快取可能延長。
   - 頁面層級控制與點擊資料：官方說明頁（16908024、16984139）與部落格只說「涵蓋功能清單會隨 Search 發展更新」「可能逐步加入更多指標」，沒有任何時程；控制項目前以 GSC 資產為單位，沒有頁面層級。網路流傳的具體加入日期無官方依據，不採用。
4. **實務用法**：
   - 每週匯出 Generative AI report 的頁面清單，對照 Web 報告同頁的點擊變化，找出「高 AI 曝光、低點擊」頁，優先改寫成需要點進來的形式（工具、下載、互動）。
   - 用國家維度看台灣等目標市場的 AI 曝光是否已出現。
   - 要不要「退出」：對流量站幾乎永遠不要；退出不會讓 AIO 消失，只會把你的位置讓給競品。

---

## 11. AI 搜尋 → 狀況解法表

| 症狀 | 可能原因 | 診斷步驟 | 解法 | 預防 |
|---|---|---|---|---|
| GSC 曝光大增、點擊持平或下滑 | 可能是頁面被 AIO 引用但使用者不點；也可能是排名、查詢結構變化 | Generative AI report 看哪些頁曝光高；對照 Web 報告同頁 CTR | 把頁面改成「需要點進來」的形式（互動工具、完整表格、下載）；首段保留摘要但把核心價值放在摘要無法涵蓋的部分 | 選題時避開可一句話回答的查詢 |
| 排名第 1 但不在 AIO 引用內 | 段落不可擷取；內容與子查詢不對齊；頁面有 `nosnippet` / `max-snippet` | URL 檢查看 snippet 設定；在 AI Mode 查看引用了誰、引用了哪段 | 重寫 H2 第一段為直接回答；補數據與日期；移除不必要的 snippet 限制 | 內容規範納入可擷取性檢查（4.2） |
| 在 Google 有引用，在 ChatGPT 完全沒有 | Bing 未索引；`OAI-SearchBot` 被擋；內容型態不符 ChatGPT 偏好 | Bing Webmaster Tools 查索引；日誌查 OAI-SearchBot 是否 403 | 提交 Bing sitemap、啟用 IndexNow；robots 允許 OAI-SearchBot；補目錄／清單型頁 | WAF 規則白名單 |
| AI 把品牌描述寫錯 | 實體訊號不一致；舊資訊仍被引用 | 在各引擎問品牌；檢查 Organization schema、Wikidata、社群簡介 | 統一名稱與描述；更新所有第三方資料；發布一篇權威的「關於我們」可擷取頁 | 品牌資料單一來源（SSOT）表 |
| 競品的 Reddit 討論被引用、自己沒有 | 缺少第三方「人味」來源 | 搜尋 `site:reddit.com 〔主題〕` | 真實參與社群討論、回答問題（不可刷文）；鼓勵使用者在論壇分享經驗 | 社群經營納入內容流程 |
| 流量整體 -30% 以上、排名沒變 | 市場級 AIO 擴張（例如 2026-02 新語言上線） | 比對 GSC 曝光／點擊剪刀差；確認該語言 AIO 上線日期 | 改 KPI；提高 RPM；擴大非搜尋流量；調整選題 | 每季重估各市場 AIO 覆蓋 |
| 被 AIO 引用後流量反而增加 | 內容屬「需深入閱讀」型；或商業型查詢 AIO 少 | 記錄被引用的查詢類型 | 複製成功模式到同類主題 | 建立「被引用頁」資料庫 |
| 想退出 AIO 但保留排名 | 商業決策（如付費牆） | 評估 Generative AI report 曝光 | 用 GSC 控制項（資產範圍，可按子網域／子路徑資產）或 `nosnippet`（頁級）；不要用 Google-Extended（無效） | 先小範圍測試 |
| AI 推薦流量在 GA4 看不到 | 來源被歸 direct 或 referral 未拆分 | 先看預設管道「AI Assistant」；再檢查 session_source 含 chatgpt.com、perplexity.ai 等是否落在 Referral / Unassigned | 建立自訂管道群組補漏（regex 見 21 章 §7.3） | GA4 設定標準化（詳見 13） |

---

## 12. 本章檢查清單

- [ ] 已確認目標市場與語言在 AIO / AI Mode 的官方支援清單內，並記錄上線日期。
- [ ] 所有目標頁面可索引、無不必要的 `nosnippet` / `max-snippet`，核心內容在初始 HTML。
- [ ] 每篇內容的 H2 / H3 第一段為可獨立成立的直接回答（40–120 字）。
- [ ] 關鍵主張附數字＋來源＋日期；比較資料用 HTML 表格而非圖片。
- [ ] Organization / Person schema 含 `sameAs`，品牌名稱全網一致。
- [ ] robots.txt 區分搜尋 bot（允許）與訓練 bot（依策略），WAF 無一刀切規則。
- [ ] Bing Webmaster Tools 已驗證、sitemap 已提交、IndexNow 已啟用。
- [ ] GSC Generative AI report 已納入月報；AI 推薦流量在 GA4 有獨立管道（預設 AI Assistant 管道＋自訂補漏，詳見 21 章 §7.3）。
- [ ] 月報包含：AI 曝光、曝光／點擊剪刀差、品牌搜尋、AI 引用次數、AI 推薦流量、直接／回訪。
- [ ] 未投入資源於 llms.txt 以外的「AI 專用」偽技術；若放 llms.txt 已標註為實驗。
- [ ] 每季重新檢視本章數據（AIO 覆蓋、CTR 研究、bot 清單）。

## 13. 參考來源

（查閱日期皆為 2026-11-03）

- Google Search Central — AI features and your website：https://developers.google.com/search/docs/appearance/ai-features
- Google Search Central Blog — Introducing Search Generative AI performance reports in Search Console（2026-06）：https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports
- Google Search Console Help — Search generative AI control：https://support.google.com/webmasters/answer/16908024
- Google Search Console Help — Search generative AI performance report（只有曝光；無起算日、無時程）：https://support.google.com/webmasters/answer/16984139
- Google Search Central — Documentation updates（2026-06-15 llms.txt 澄清；2026-10-21 Search generative AI control 納入 control-what-you-share）：https://developers.google.com/search/updates
- Google — AI Mode 支援國家／語言：https://support.google.com/websearch/answer/16011537
- Google — AI Overviews 支援國家／語言：https://support.google.com/websearch/answer/14901683
- Google Search Central — Google 的常見爬蟲（Google-Extended、AIPREF）：https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers
- OpenAI — Overview of OpenAI crawlers（OAI-SearchBot / GPTBot / ChatGPT-User）：https://developers.openai.com/api/docs/bots
- Anthropic — Does Anthropic crawl data from the web：https://support.claude.com/en/articles/8896518
- Perplexity — Perplexity crawlers：https://docs.perplexity.ai/guides/bots
- BrightEdge — AI Overviews at the One-Year Mark: Presence, Size, and What They're Citing（2026-02-12；48% / 30–31% 原始出處）：https://www.brightedge.com/resources/weekly-ai-search-insights/ai-overviews-one-year-presence-size-citing
- Search Engine Roundtable — Almost Half Of Google Searches Have AI Overviews（2026-07-30；Similarweb 43%、Semrush 48%，非 Google 發言）：https://www.seroundtable.com/half-google-searches-ai-overviews-41780.html
- Ahrefs — Only 12% of AI Cited URLs Rank in Google's Top 10 for the Original Prompt（2025-08-11，15,000 提示）：https://ahrefs.com/blog/ai-search-overlap/
- Whitehat SEO — Perplexity vs ChatGPT vs Gemini: How AI Engines Cite Content（11% 說法來源之一，方法未公開）：https://whitehat-seo.co.uk/blog/ai-engines-comparison-citations
- Rankability — llms.txt Adoption Research Report（2026-09-18，Tranco 前 10,000）：https://www.rankability.com/llms-report/
- Common Crawl — A content analysis of llms.txt files from the July 2026 crawl archive（2026-08-31）：https://commoncrawl.org/blog/a-content-analysis-of-llms-txt-files-from-the-july-2026-crawl-archive
- Cloudflare Radar — Bots & crawlers（AI bot 用途占比、robots.txt 掃描原始資料集）：https://radar.cloudflare.com/bots
- Pew Research Center（2025-07）AI Overviews 點擊研究（經 Search Engine Roundtable 與 Fortune 報導）：https://www.seroundtable.com/pew-google-ai-overviews-39808.html
- Ahrefs — AI Overviews reduce clicks by 34.5%（2025-04）：https://ahrefs.com/blog/ai-overviews-reduce-clicks/
- Ahrefs — AI Overviews reduce clicks（2026-02 重跑，2023-12 vs 2025-12）：https://ahrefs.com/blog/ai-overviews-reduce-clicks-update/
- Seer Interactive — AIO Impact on Google CTR: 2026 Update（2026-04）：https://www.seerinteractive.com/insights/aio-impact-on-google-ctr-2026-update
- Seer Interactive — September 2025 Update（2025-11-04 發布）：https://www.seerinteractive.com/insights/aio-impact-on-google-ctr-september-2025-update
- arXiv — AI 搜尋對發布者點擊的隨機對照實驗（2026-08）：https://arxiv.org/html/2608.18352v1
- Yext — 86% of AI citations come from brand-managed sources（本地品牌查詢樣本）：https://investors.yext.com/news-events/press-releases/detail/376/yext-research-86-of-ai-citations-come-from-brand-managed
- llms.txt 提案：https://llmstxt.org/
- Google Search Console Help — Performance report（AIO / AI Mode 位置計算）：https://support.google.com/webmasters/answer/7042828
- Google Search Central — robots.txt 簡介（不保證移出索引）：https://developers.google.com/search/docs/crawling-indexing/robots/intro
- Press Gazette — Reuters Institute / Chartbeat 2026 Trends Report 數據：https://pressgazette.co.uk/publishers/digital-journalism/google-traffic-down-2025-trends-report-2026/
- Semrush — Most cited domains in AI（2025-10；2026 版經 eMarketer 引用）：https://www.semrush.com/blog/most-cited-domains-ai/
- Semrush — AI Overviews Study（2025-12-15；2025-11 觸發率 15.69%）：https://www.semrush.com/blog/semrush-ai-overviews-study/（查閱 2026-11-03）
- Chartbeat — Pageviews are down: what AI is doing to publisher traffic（小型 -60% / 中型 -47% / 大型 -22%；Google Search PV -34%）：https://chartbeat.com/resources/articles/pageviews-down-ai-impact/（查閱 2026-11-03）
- Axios — Chartbeat: search traffic to publishers plunges amid AI chatbots（2026-03-17）：https://www.axios.com/2026/03/17/chartbeat-search-traffic-ai-chatbots（本次無法讀取，以 Chartbeat 原文為準）
- Search Engine Roundtable — Google does not endorse llms.txt（2026）：https://www.seroundtable.com/google-does-not-endorse-llms-txt-40789.html
- Search Engine Journal — Google says AI Mode can now scale faster across languages（2026）：https://www.searchenginejournal.com/google-says-ai-mode-can-now-scale-faster-across-languages/575791/
- Search Engine Roundtable — AI Mode expands to 53 new languages（2026-02）：https://seroundtable.com/google-expands-ai-mode-to-53-new-languages-40958.html
- SEOmator — Monthly AI Crawler Report: September 2026（2026-10-10 發布，整理 Cloudflare Radar 資料）：https://seomator.com/blog/ai-search-optimisation-insights
- Search Engine Land — Search Console AI performance reports and Search generative AI control rolling out globally：https://searchengineland.com/google-search-console-ai-performance-reports-and-search-generative-ai-control-rolling-out-globally-486269
- Ahrefs — AI vs Search 流量基準（118,671 站，2026-11-03 更新，資料至 2026-10；查閱 2026-11-05）：https://ahrefs.com/benchmarks/ai-vs-search
- BrightEdge — ChatGPT referral traffic more than doubles in 2026（2026-09-24；查閱 2026-11-05）：https://www.brightedge.com/news/press-releases/brightedge-data-chatgpt-referral-traffic-doubles-in-2026
- Conductor — 2026 Publishing AI search benchmarks（查閱 2026-11-05）：https://www.conductor.com/academy/2026-publishing-ai-search-benchmarks/
- SparkToro — In 2026, Less Than One Third of Google Searches Still Send a Click（2026-06-08；查閱 2026-11-05）：https://sparktoro.com/blog/in-2026-less-than-one-third-of-google-searches-still-send-a-click/
