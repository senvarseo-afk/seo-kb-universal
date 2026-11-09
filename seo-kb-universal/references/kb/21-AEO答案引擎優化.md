# 21 AEO 答案引擎優化

> 版本：1.2 ｜ 更新日期：2026-11-09 ｜ 適用：所有 SEO 網站專案 ｜ 撰寫：Claude

## 本章摘要

1. AEO（Answer Engine Optimization）在本知識庫的定義：讓「一個具體問題」的答案在精選摘要、People Also Ask、知識面板、AI Overviews / AI Mode、語音助理、聊天型答案引擎中被選用、被正確呈現、被歸因到本站。它是 SEO 的一個工作面向，不是獨立學科；Google 2026-05-15 的生成式 AI 優化指南明說 AEO / GEO「still SEO」，同日並把「操弄 Search 內生成式 AI 回答」明文納入垃圾政策。
2. 版位現況（查閱 2026-11-05）：精選摘要仍存在，但第三方樣本顯示其出現率在 2025 上半年大幅下滑（Ahrefs 美國桌機 15.41% → 5.53%，與 AIO 成長負相關，作者強調相關非因果；不是 2026-11 的出現率），Google 工程副總也證實「無法產生 AIO 時會退回精選摘要」；PAA 同期微升，且 AlsoAsked 2026-09 英文樣本顯示 PAA 答案已多為 AIO；FAQ rich result 已於 2026-05-07 完全停止顯示；Speakable 仍是 beta、只限美國英文的 Google Home 裝置。
3. 寫作核心：一頁一個主問題、問題式 H2、標題下第一段 40–120 字可獨立成立的答案、步驟用有序清單、比較用 HTML 表格、數據附來源與日期；FAQ 區塊只留真實的延伸問題，不再為 rich result 標記 `FAQPage`。
4. 量測有盲區：GSC 沒有精選摘要或 PAA 的篩選，PAA 只在展開後才算曝光，Generative AI report 只提供 AIO / AI Mode 的曝光，點擊併入一般成效報表的 Web 總體資料、無法單獨拆出；GA4 自 2026-05 起有原生「AI Assistant」管道，但不含 AIO / AI Mode，第三方檢查（2026-07）也發現漏掉 Perplexity 流量（現況待查證），仍需自訂 regex 管道群組加上手動抽測。
5. AI Overviews / AI Mode 的機制、GEO 實務、AI 爬蟲、llms.txt、零點擊 KPI 的正典位置是 08 章；本章只補「問題 → 答案」層的研究、寫作、量測與狀況解法，並用「詳見 08 §N」交叉引用。

## 目錄

1. [AEO 的定義、界線與 Google 官方立場](#1-aeo-的定義界線與-google-官方立場)
2. [答案版位全覽與 2026 現況](#2-答案版位全覽與-2026-現況)
3. [問題研究：找出使用者會問的問題](#3-問題研究找出使用者會問的問題)
4. [答案優先寫作規範](#4-答案優先寫作規範)
5. [結構化資料與 AEO](#5-結構化資料與-aeo)
6. [品牌與實體被答案引擎提到](#6-品牌與實體被答案引擎提到)
7. [量測：追蹤精選摘要、PAA 與 AI 引用](#7-量測追蹤精選摘要paa-與-ai-引用)
8. [依專案類型的 AEO 策略](#8-依專案類型的-aeo-策略)
9. [問題排解：AEO 狀況與解法](#9-問題排解aeo-狀況與解法)
10. [本章檢查清單](#10-本章檢查清單)
11. [參考來源](#11-參考來源)

---

## 1. AEO 的定義、界線與 Google 官方立場

### 1.1 SEO / AEO / GEO 對照

| 項目 | SEO | AEO（本章） | GEO（08 章） |
|---|---|---|---|
| 最小單位 | 頁面 × 查詢 | 問題 × 答案段落 | 段落 × 生成式回答中的引用 |
| 主要版位 | 10 藍鏈、rich result、圖片 / 影片 / 新聞 | 精選摘要、PAA、知識面板、語音答案、聊天引擎的直接回答 | AI Overviews、AI Mode、ChatGPT search、Perplexity、Copilot、Gemini |
| 主要槓桿 | 索引、相關性、品質、連結、體驗 | 問題研究、答案區塊格式、實體資料正確性、段落選取 | 可擷取性、實體一致性、第三方提及、搜尋 bot 允許 |
| 成功指標 | 排名、點擊、轉換 | 是否「被選為答案」、答案是否正確、是否附本站連結 | AI 曝光、引用次數、引用段落、品牌搜尋 |
| 官方立場 | Search Essentials | Google：屬於 SEO，無專屬要求 | Google：屬於 SEO，無專屬要求 |
| 本知識庫正典 | 02–07 章 | 本章 | 08 章 |

### 1.2 Google 官方立場

**規範**：不把 AEO 當成獨立的技術工程或「新排名因素」，不採用任何 Google 明文否定的捷徑；所有 AEO 手法都要能通過 Search Essentials 與垃圾政策的檢驗。

**為什麼**：
- Google Search Central 2026-05-15 新增〈Optimizing your website for generative AI features〉指南，把 AEO 與 GEO 視為同一件事，定調為「optimizing for generative AI search is optimizing for the search experience, and thus still SEO」（https://developers.google.com/search/docs/fundamentals/ai-optimization-guide ，查閱 2026-11-04）。
- 該指南的「Mythbusting」段落明列不需要做的事：llms.txt 等特殊 AI 檔案、把內容切成小塊（chunking）、為 AI 重寫內容、製造不真實的品牌提及、過度依賴結構化資料（沒有生成式 AI 專用 schema）。
- 同日的文件更新「Clarifying that spam policies apply to generative AI responses in Google Search」：垃圾政策頁開頭的適用範圍現在寫明包含「attempting to manipulate generative AI responses in Google Search」；指南也寫明「大量產生頁面以操弄排名或 AI 回答」屬 scaled content abuse（https://developers.google.com/search/docs/essentials/spam-policies 、https://developers.google.com/search/updates ，查閱 2026-11-04；政策細節詳見 07 §5.2）。
- 精選摘要官方文件：Google 系統自動判斷頁面是否適合做精選摘要，網站無法申請（https://developers.google.com/search/docs/appearance/featured-snippets ，查閱 2026-11-04）。

**怎麼做**：AEO 工作只做三類事——(1) 找對問題（§3）；(2) 把答案寫成容易被選用、選用後仍正確的形式（§4）；(3) 讓本站與品牌的實體資料一致且正確（§6、08 §4.3）。

**驗收方式**：每一項 AEO 作法都能回答「沒有答案引擎時，這樣寫對讀者是否也更好」；答不出來的作法不做。

**常見錯誤**：把「AEO 服務」包裝的 FAQ 堆疊、為操弄排名隱藏問答、每頁加 `FAQPage` / `Speakable`、在第三方平台刷品牌提及當作新技術採購。這些問題的性質不同：為操弄排名而隱藏、使用者不易看到的內容屬垃圾政策的 hidden text abuse，但正常的折疊或分頁問答不違規（https://developers.google.com/search/docs/essentials/spam-policies ，查閱 2026-11-05）；`FAQPage` 已無搜尋展示效益，舊標記留著也不會造成問題（Google 2023 年說明，https://developers.google.com/search/blog/2023/08/howto-faq-changes ，查閱 2026-11-05），標記與可見內容不符才是規範問題（06 §9）；`Speakable` 只是市場不適用（§5）；製造不真實的品牌提及是指南明文否定的作法（§1.2）。

---

## 2. 答案版位全覽與 2026 現況

### 2.1 總表（查閱 2026-11-05）

| 版位 | 答案來源與觸發 | 2026-11 現況 | 對內容站的價值 | 量測方式 | 詳見 |
|---|---|---|---|---|---|
| 精選摘要（段落 / 清單 / 表格 / 影片） | 索引中排名前段的頁面段落，由 Google 自動選取 | 仍存在；Ahrefs 2025-01 至 06 美國桌機樣本出現率大幅下降（與 AIO 成長負相關，相關非因果，§2.2）；AIO 無法生成時會退回精選摘要 | 中：拿到仍帶點擊；2025 樣本顯示版位減少 | 排名工具 SERP feature；GSC 無專屬篩選 | §2.2 |
| People Also Ask（其他人也問了） | 相關問題 + 各自的摘要或 AI 生成答案與連結 | 仍普遍存在；Ahrefs 2025-01 至 06 美國桌機樣本約七至八成（歷史樣本，非 2026-11 數字） | 中：曝光多、點擊少，是問題研究金礦 | 排名工具；GSC 展開才計曝光 | §2.3 |
| 知識面板 | Knowledge Graph 實體資料 | 仍存在；Ahrefs 同樣本 2025 上半年小幅下降 | 品牌站高、流量站低 | 手動搜尋品牌名 | §2.4、08 §4.3 |
| AI Overviews / AI Mode | 同一索引，query fan-out 多次檢索 | 已覆蓋台灣等市場 | 高曝光、低點擊 | GSC Generative AI report（曝光）+ 一般成效報表 Web 總體資料（點擊併入） | 08 §1、§10 |
| 語音助理 | Gemini（手機端逐步取代 Google Assistant）、Siri AI、Alexa+ | 分階段轉向 LLM 助理，音箱端 Assistant 仍與 Gemini for Home 並存；非英語市場支援有限 | 低：幾乎無點擊、量測不到 | 手動抽測 | §2.5 |
| 聊天型答案引擎 | ChatGPT search（含 Bing）、Perplexity、Copilot、Gemini app | 各自索引與爬蟲；引用來源與 Google 排名重疊低 | 中：流量小但可量測 | GA4 管道、Bing AI Performance、手動抽測 | §2.6、08 §5 |
| Google 自有即時答案（計算機、匯率、天氣、比分等） | Google 或授權資料源 | 無法爭取 | 無 | — | §8 即時資料型網站 |

### 2.2 精選摘要

**格式**（依 Google 文件與常見 SERP 觀察）：
- **段落**：定義、原因類問題；答案片段可能被 highlight（2026-08 曾被觀察到測試粉紅色，https://www.seroundtable.com/google-pink-highlights-featured-snippets-41926.html ，查閱 2026-11-04）。
- **清單**：有序（步驟、排名）或無序（條件）；項目過多會截斷成「更多項目」。
- **表格**：價格、規格、時程、比較；Google 可能只取部分欄列。
- **影片**：多為 YouTube，可跳到片段；Google 會嘗試自動偵測影片關鍵時刻，YouTube 說明欄時間戳、`Clip` / `SeekToAction` 是自行提供章節的方法（Google 優先採用），不是必要條件（https://developers.google.com/search/docs/appearance/video ，查閱 2026-11-05；另見 06 §2 第 25 項）。

**現況與數據**：
- Ahrefs（2025-07-22 發布，100 萬個隨機美國桌機 SERP）：精選摘要出現率 2025-01 為 15.41%、2025-06 為 5.53%（-64%）；同期 AIO 由 3.93% 升到 27.43%；兩者相關係數 -0.9053，作者強調相關非因果（https://ahrefs.com/blog/how-serp-features-have-evolved-in-the-ai-era ，查閱 2026-11-04）。
- Serpstat（2025-12-25 發布，10 億關鍵字）：觀察到 Google 傾向以 AIO「取代」而非並列精選摘要，2025 Q4 起兩者「apparently」不再同時出現（https://serpstat.com/blog/year-in-search-ai-overview-study ，查閱 2026-11-04）。
- Google 搜尋工程副總 Rajan Patel（2026-01-22，X）證實：「On occasion we fall back to featured snippets when we are unable to generate an AI Overview」（https://www.seroundtable.com/google-featured-snippets-ai-overviews-fail-40805.html ，查閱 2026-11-04）。
- 2026 年網路流傳的出現率數字（0.1%、8%、12.3% 等）多為無方法說明的二手統計，本知識庫不引用；**台灣市場的精選摘要出現率沒有公開研究，待以自家排名工具驗證**。

**機制要點**：
- 2020-01-22 起，被選為精選摘要的頁面不再重複出現在第一頁一般結果（Danny Sullivan 說明，https://seroundtable.com/google-featured-snippet-deduplication-change-summary-28921.html ，查閱 2026-11-04）。
- GSC 計算：點精選摘要內的連結算點擊，曝光與位置套用標準規則（https://support.google.com/webmasters/answer/7042828 ，查閱 2026-11-04）。
- 退出：`nosnippet` 同時封鎖精選摘要與一般摘要；`data-nosnippet` 封鎖指定段落；`max-snippet` 調小只會「降低」機率，Google 不公布精選摘要的最短長度，要保證退出只能用 `nosnippet`（精選摘要官方文件）。

### 2.3 People Also Ask

- Ahrefs 同一份研究中 PAA（工具標為 question）2025-01 至 06 由 73.73% 升到 79.13%，是該樣本中少數成長的版位（同上來源；美國桌機歷史樣本，非 2026-11 數字）。
- PAA 展開後的答案要分兩種看：傳統的頁面段落摘錄，以及生成式 AI 答案。AlsoAsked 2026 年約 1,920 萬筆英文樣本顯示，PAA 答案屬 AIO 的比例 2026-08 為 86%、9 月第一週為 97%，約 14 個月前僅約 12%（Mark Williams-Cook，https://www.linkedin.com/feed/update/urn:li:activity:7503164423075725313/ ；Search Engine Roundtable 2026-09-09，https://seroundtable.com/ppa-ai-overviews-google-42047.html ，查閱 2026-11-05）。這是第三方英文樣本，未註明市場，不能外推到所有國家與語言；繁中 PAA 以 §7.5 抽測確認。
- GSC 計算：點擊展開不算點擊；**只有展開後**，展開區內的本站連結才算曝光（https://support.google.com/webmasters/answer/7042828 ，查閱 2026-11-04）。所以 PAA 的 GSC 曝光天生偏低，不能拿來判斷「PAA 沒用」。
- PAA 的主要價值在問題研究（§3）：它列出 Google 認定的同意圖子問題。

### 2.4 知識面板

- 資料來自 Knowledge Graph；人物或組織可在面板底部「Claim this knowledge panel」，以 YouTube、Search Console、Twitter（X）或 Facebook 等官方帳號驗證；驗證後的回饋有優先處理；並非所有面板都可認領；本地商家應改用 Google 商家檔案（https://support.google.com/knowledgepanel/answer/7534902 ，查閱 2026-11-04；本地詳見 17）。
- Ahrefs 樣本中知識面板出現率 14.09% → 12.95%（-8%，同上來源）。

### 2.5 語音助理

| 助理 | 2026-11 狀態 | 與東南亞、台灣市場的關係 | 來源（查閱 2026-11-05） |
|---|---|---|---|
| Google Assistant → Gemini（手機） | 9to5Google 2026-08-04 引述 Google 寄給使用者的通知：自 2026-09-04 起逐步移除 Android 手機、平板、Wear OS 與手機投影 Android Auto 上的 Assistant，改由 Gemini 取代；內建 Google 的車款暫時保留（第三方報導；此日期未見於官方部落格，官方來源待查證） | Android 使用者的語音查詢逐步轉入 Gemini；答案邏輯是否與 AI Mode 同源，官方未說明（待查證） | https://9to5google.com/2026/08/04/google-assistant-september-2026-shutdown/ ；官方 2025-03-14 升級公告（未列此日期）：https://blog.google/products-and-platforms/products/gemini/google-assistant-gemini-mobile/ |
| Gemini for Home（智慧音箱） | Gemini for Home 以 Early Access 分階段開放；Google Home 說明頁仍同時列出 Gemini for Home 與 Google Assistant 的支援範圍，尚非全面取代 | Early Access 國家未列台灣；台灣音箱仍列 Assistant（Mandarin）；開放時程待查證 | https://support.google.com/googlehome/answer/7550584?hl=en ；https://blog.google/products-and-platforms/devices/google-nest/gemini-for-home-launch/ |
| Siri AI（Apple） | iOS 27 於 2026-09-14 推出 Siri AI（beta），採與 Google 合作、運用 Gemini 技術開發的 Apple Foundation models，可上網查資料回答一般問題（此段依 MacRumors 彙整）；初期僅英文（美、英、加、澳、愛爾蘭、印度、紐西蘭、南非），Apple 2026-10-26 公告隨 27.2 加入法、日、韓、葡、西文，繁中預計 2026 年底前加入；是否顯示來源連結未確認 | 台灣繁中截至 2026-11-05 尚未支援（各地區開放狀態待查證） | https://www.apple.com/newsroom/2026/10/siri-ai-is-available-in-more-languages-starting-today/ ；https://support.apple.com/en-us/127893 ；https://www.macrumors.com/roundup/ios-27/（第三方彙整） |
| Alexa+（Amazon） | Amazon 官方截至 2026-10-28：美國、加拿大可用（加拿大 Early Access 已於 2026-06-11 結束）；英、墨、義、西、德、奧、法、巴西，以及 8/6 澳洲、9/16 印度、10/29 日本為 Early Access；2027 再擴展至超過 10 國（未列國名） | 官方清單未列台灣；不列入優先 | https://www.aboutamazon.com/news/devices/alexa-plus-international-launch |

**結論**：語音查詢正分階段轉向 LLM 助理，手機端轉換較快，音箱與非英語市場仍在過渡，Assistant 尚未全面退場；AEO 上不必當獨立版位投入，Speakable 見 §5。

### 2.6 聊天型答案引擎

| 引擎 | 被引用的前提 | AEO 特有注意事項 | 來源（查閱 2026-11-04） |
|---|---|---|---|
| ChatGPT search | 允許 `OAI-SearchBot`；Bing 可能是來源之一 | ChatGPT 會在引用連結加 `utm_source=chatgpt.com`，在 GA4 可直接辨識 | OpenAI Publishers and developers FAQ：https://help.openai.com/en/articles/12627856-publishers-and-developers-faq（本次 WebFetch 回 403，內容依搜尋引擎摘錄）；爬蟲詳見 08 §7 |
| Perplexity | 允許 `PerplexityBot`（官方稱不用於訓練） | 每答引用數最多、偏好新鮮內容；`Perplexity-User` 一般不理會 robots.txt | https://docs.perplexity.ai/guides/bots |
| Microsoft Copilot / Bing AI 摘要 | Bing 索引 | Bing Webmaster Tools「AI Performance」可看引用次數與 grounding queries（§7.4） | https://blogs.bing.com/webmaster/2026/2/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview/ |
| Gemini app | Google 索引 grounding（受 `Google-Extended` 控制） | 答案邏輯是否與 AI Mode 同源，官方未說明（待查證）；手機語音查詢也走這裡 | 08 §5、§7 |

引用偏好與重疊研究詳見 08 §5；各引擎的引用占比與實際導流規模詳見 08 §2.3，兩者不可互相代換。

---

## 3. 問題研究：找出使用者會問的問題

**規範**：每個主題群集（cluster）建立一份「問題母表」，至少涵蓋 5 種來源、標註語言與意圖，並由母表決定「哪些問題自成一頁、哪些併入既有頁的 H2、哪些放進 FAQ 區塊」。

**為什麼**：答案版位以「問題」為單位分配；PAA 與 AI Mode 的 query fan-out 顯示，一個主查詢可能延伸出多個子主題（Google 確認 fan-out，但未公布數量，https://developers.google.com/search/docs/appearance/ai-features ，查閱 2026-11-05）。只做主關鍵字的頁面，會在子問題上整批讓給競品。關鍵字研究流程本身詳見 02 §2，本節只補問句層。

### 3.1 問題來源

| 來源 | 怎麼取 | 強項 | 限制 |
|---|---|---|---|
| People Also Ask | 無痕視窗、目標國家，展開 2–3 層並記錄 | Google 自己認定的同意圖子問題 | 每次展開結果不同，需重複抽樣 |
| Google 自動完成 | 主詞 + 疑問詞（中、英各一輪） | 真實輸入習慣、口語拼法 | 不顯示搜尋量 |
| AlsoAsked / AnswerThePublic | 免費額度擷取 PAA 樹 | 一次看到問題層級 | 免費次數有限（13 §13.5） |
| GSC 問句 regex | 成效 → 查詢 → 自訂（regex），§3.2 | 已有曝光、最容易先贏 | 匿名查詢被省略，長尾問句被低估（https://support.google.com/webmasters/answer/17011165 ，查閱 2026-11-04） |
| Reddit / 論壇 / FB 社團 / Dcard / PTT | 搜尋 `site:reddit.com/r/taiwan 主題`、在地社團關鍵字 | 真實痛點、在地用語、新問題 | 需人工整理、不可直接抄錄內容 |
| AI 引擎的追問建議 | 在 AI Mode、ChatGPT、Perplexity、Gemini 問主問題，記錄它主動提出的 follow-up 與「相關問題」 | 反映 fan-out 子主題 | 非確定性，同一問題要跑 2–3 次 |
| 站內搜尋與客服 / 留言 | GA4 `view_search_results`、留言區 | 已到站使用者沒找到的答案 | 需先有流量 |

### 3.2 GSC 問句篩選 regex

GSC 成效報表的 regex 採 RE2 語法、預設部分比對且不分大小寫；`^`、`$` 可錨定，選「不符合 regex」可反向排除（https://support.google.com/webmasters/answer/17011165 ，查閱 2026-11-04；API 版上限 4,096 字元：https://developers.google.com/webmaster-tools/v1/searchanalytics/query）。

```
# 英文問句
^(who|what|when|where|why|how|which|is|are|can|does|do|should|will|was)\b

# 繁體中文問句（無空格，不用 \b）
(怎麼|怎样|怎樣|如何|什麼|甚麼|為什麼|為何|多少|幾[天個年歲點]|哪裡|哪個|哪家|哪些|是否|嗎|呢|可以|能不能|要不要|推薦|差別|比較|vs)
```

注意：簡中查詢另建一組 regex。

### 3.3 繁中問句的特殊處理

- **繁中**：台灣使用者常用「嗎 / 呢」結尾的完整句（「機車駕照可以線上考嗎」）與「推薦 / 比較 / PTT / Dcard」等修飾詞；後者代表使用者想看第一手經驗，答案要有實測或親身說明，不能只給定義。
- **地區用語**：繁中頁一律用台灣用語（網路、影片、軟體），避免被當成簡轉繁頁（10 §5）。
- **混語查詢**：同一問題的英文、在地語與混語寫法都要進母表，頁面版本依 25 §3 的規則決定。AIO / AI Mode 會依查詢語言生成，混語頁會被歸入其主要語言（08 §1.2）。
- **口語拼法**：同一問題的不同拼法在母表合併為一列、記錄所有拼法，H2 用標準拼法、內文自然出現口語拼法一次即可。

### 3.4 問題母表欄位

| 欄位 | 範例 | 用途 |
|---|---|---|
| 問題（標準寫法） | SIM 卡註冊要多久？ | H2 或頁面主題 |
| 變體 / 口語拼法 | how long SIM registration、SIM 註冊時間 | 內文自然出現 |
| 語言 / 市場 | zh-TW / en | 對應頁面版本 |
| 來源 | PAA、GSC、Reddit、AI 追問 | 判斷可信度 |
| 意圖與答案型態 | Know Simple → 段落；Do → 步驟；比較 → 表格 | 決定格式（§4） |
| 處理方式 | 獨立頁 / 併入某頁 H2 / FAQ 區塊 / 不做 | 防止蠶食（02 §12） |
| 目前版位持有者 | 競品 A 精選摘要；AIO 引用 B | 量測基準（§7.5） |

**驗收方式**：每個 cluster 的母表 ≥ 30 個問題、≥ 5 種來源；每個問題都有「處理方式」；同一問題不指派給兩個 URL。

**常見錯誤**：只用工具抓英文 PAA 再翻成中文；把每個 PAA 問題都做成一頁（變成薄頁群，觸發 11 §6 的索引問題）；忽略口語拼法。

---

## 4. 答案優先寫作規範

本節延伸 05 §6（首段直接回答）與 08 §4.2（段落可擷取性），只寫 AEO 特有的格式細節；長度數字是本知識庫的編輯標準，不是 Google 官方門檻。

### 4.1 答案區塊的長度與格式

**規範**：每個目標問題配一個「答案區塊」，緊接在問題式標題之後：段落型 40–120 字（定義句 40–60 字）、清單型 3–8 項、表格型 3–6 欄 × 3–10 列；答案區塊之後才放背景、例外與延伸。

**為什麼**：答案引擎擷取「緊接在問題後、可獨立成立」的片段；Google 不公布長度門檻（精選摘要官方文件），過長段落會被截斷或改選他段。

**怎麼做**：
1. 公式：`〔主詞〕+〔直接答案〕+〔關鍵條件 / 數字〕+〔時間點〕`。例（沿用 05 §6）：「台灣護照入境目標國觀光可免簽 N 天（截至 2026-11）；超過需當地延簽或事先辦簽證。」
2. 答案區塊不用代名詞開頭，不寫「如上所述」。
3. 清單每項以同一句型開頭、一項一個動作或條件。
4. 表格用 HTML `<table>`，第一列為表頭，單位寫在格內。

**驗收方式**：答案區塊單獨貼出仍看得懂且正確；字數在範圍內；URL 檢查的轉譯 HTML 中有答案區塊。

**常見錯誤**：答案藏在第三段；用「這取決於很多因素」當開頭；把表格做成圖片；答案區塊放在 tab 或折疊區（Google 文件建議內容對使用者立即可見，見 §4.2）。

### 4.2 問題式標題與段落定位

**規範**：目標問題寫成 H2 / H3，用使用者實際的問法（來自 §3 母表）；標題與答案區塊之間不插入廣告、圖片或 CTA。

**為什麼**：問題標題讓答案引擎確認「下一段在回答什麼」；Google 摘要文件（2026-04-20 新增「Read more」深連結段落）建議：內容要對使用者立即可見、不藏在可展開區塊或分頁介面、不要在載入時用 JavaScript 強制捲動、更改 `location.hash` 時保留片段，才更容易出現跳到指定段落的連結（https://developers.google.com/search/docs/appearance/snippet ，查閱 2026-11-04）。

**怎麼做**：H2 用完整問句（「SIM 卡註冊要準備哪些文件？」），不用「文件準備」這種名詞片語；每個 H2 給穩定的 `id`，供深連結與 text fragment 使用；廣告放在答案區塊之後（版位規範詳見 09 §7）。

**驗收方式**：抽 10 個 H2，每個都能在母表找到對應問題；行動版首屏內可看到第一個答案區塊。

**常見錯誤**：標題寫成口號；同一問題在一頁出現兩個 H2；標題與答案之間塞廣告。

### 4.3 定義句

**規範**：「X 是什麼」類問題的第一句用「X 是〔類別〕，〔區別特徵〕」句型，40–60 字內完成；第一次出現的專有名詞寫全名並附英文。

**為什麼**：定義型查詢最常觸發精選摘要與 AIO（08 §1.3）；被選中時至少要帶出正確資訊。

**怎麼做**：例：「中央氣象署（Central Weather Administration）是交通部所屬的氣象機關，負責發布天氣預報、颱風警報與地震資訊。」定義後立刻接「本站提供什麼別處沒有的東西」（例如歷史資料查詢工具）。

**驗收方式**：定義句不需上下文、不含「本文」「我們」；與 Wikipedia / 官方定義無事實衝突。

**常見錯誤**：定義句抄官方原文（重複內容、也沒有增值）；為了「可被摘要」把整篇寫成 20 個定義句。

### 4.4 步驟

**規範**：流程型答案用 `<ol>`，每步一個動詞開頭的動作，3–8 步；步驟超過 8 個時分成「階段」H3，每個階段再列步驟。

**為什麼**：清單型精選摘要直接讀取 HTML 清單；HowTo rich result 已於 2023-09 停用（06 §3），步驟的可見性只剩 HTML 結構本身。

**怎麼做**：每步格式「動詞 + 對象 + 關鍵數值」（「開啟電信商 app 的 SIM 註冊頁，上傳一張有效證件」）；需要的文件、費用、時間放在步驟清單之前的摘要表。

**驗收方式**：關閉 CSS 時清單仍可讀；清單由 `<ol><li>` 構成，不是用 `<p>` 加數字。

**常見錯誤**：每步插大圖把清單拆散；步驟編號寫在圖片裡。

### 4.5 比較表

**規範**：「A 還是 B」「哪個比較便宜」類問題用 HTML 比較表回答，欄位含「項目、數值、條件、資料日期」，表格前一句先給結論。

**為什麼**：表格型精選摘要與 AI 回答都偏好結構化比較；結論句讓只讀第一段的引擎也拿得到答案。

**怎麼做**：結論句句型：「〔日期〕〔類別〕中，〔A〕單價最低，〔B〕覆蓋最廣。」表格欄位不超過 6 欄；行動版用可水平捲動的容器，不改成圖片。

**驗收方式**：表格在初始 HTML；每格能單獨讀懂（08 §4.2）；資料日期在表內或表下。

**常見錯誤**：比較表只有勾勾沒有數值；不同列的單位不一致；表格是聯盟商提供的嵌入 iframe（引擎讀不到）。

### 4.6 數據與日期

**規範**：答案中的每個數字附「來源 + 日期」；會變動的答案（價格、法規、比分、匯率）在答案區塊內寫明「截至 YYYY-MM-DD」，並在資料變動當天更新內容與 `dateModified`。

**為什麼**：答案引擎會把過時答案當現在式呈現，錯誤落在被引用的網站上（日期處理詳見 20 §20.5）。

**怎麼做**：在 CMS 為會變動的數值建立單一資料源，頁面與結構化資料同源輸出；每個答案區塊旁留下「最後核對」欄位供編輯維護。

**驗收方式**：抽查 10 個答案區塊，數字都能追溯到來源；`dateModified` 與實際修改日期一致。

**常見錯誤**：只改日期不改內容（05 §12 已列為不可靠訊號）；「最新」「今年」不寫具體年份。

### 4.7 一頁一主問題 vs FAQ 區塊

**規範**：有獨立搜尋需求、需要 ≥ 300 字才能答好的問題自成一頁；同一意圖下的延伸問題併入主頁 H2；FAQ 區塊只放 3–8 個「讀完主文仍可能問」的短問題，不標記 `FAQPage`。

**為什麼**：FAQ rich result 已於 2026-05-07 完全停止顯示、文件 2026-06-15 移除（06 §3，https://developers.google.com/search/updates ，查閱 2026-11-04）；FAQ 區塊的價值只剩「可見內容被擷取」。拆成太多小頁會製造蠶食與薄頁。

**怎麼做**：用 §3.4 母表的「處理方式」欄決定；FAQ 問題不得與 H2 重複；FAQ 答案同樣遵守 §4.1 的答案區塊格式。

**驗收方式**：站內同一問題只有一個主要回答位置；FAQ 區塊的問題在 GSC 有曝光或來自真實使用者提問。

**常見錯誤**：用 LLM 為每頁產生相似的 FAQ（11 §5 已列為程序化 SEO 的薄內容訊號）；FAQ 與主文互相矛盾。

### 4.8 多語言版本的答案

**規範**：每個語言版本的答案區塊都由該語言重新撰寫並在地化數值與例子；hreflang 與 canonical 正確（詳見 10 §2），讓答案引擎把對的語言版本配給對的查詢。

**為什麼**：Google 以可見內文判定語言（10 本章摘要第 3 條、25 §3）；機器翻譯的答案區塊常出現單位、貨幣、法規錯誤，被選為答案時錯誤會放大。

**怎麼做**：繁中版用新台幣與台灣法規，其他版本用當地貨幣與機關名稱；同一問題的各語言版答案數值一致時，共用同一資料源；混語查詢依 §3.3 決定版本。

**驗收方式**：用 `hl` / `gl` 參數或目標國家 VPN 搜尋同一問題的各語言版本，確認被選用的是對應語言頁（§9 狀況 S14）。

**常見錯誤**：只翻 H2 不改數值；英文版答案出現在繁中查詢；各語言版答案日期不同步。

---

## 5. 結構化資料與 AEO

現況與範本一律以 06 章為準，本節只評估 AEO 的實際價值（查閱 2026-11-04）。

| 類型 | Google 現況（06 章） | 對 AEO 的實際價值 | 建議 |
|---|---|---|---|
| `FAQPage` | rich result 2026-05-07 起完全不顯示（06 §3） | 無；可見 FAQ 文字仍可被擷取 | 新頁不再加；舊標記留著不造成問題，官方表示不必主動移除，改版時順手清掉（本站建議） |
| `HowTo` | 2023-09 停用（06 §3） | 無；步驟靠 `<ol>` | 移除標記 |
| `QAPage` | 支援；限「一問、使用者可提交多個答案」的頁面，站方自寫的 FAQ 不符資格；2026-03-24 文件新增支援屬性，含標示 AI 生成內容的 `digitalSourceType`（https://developers.google.com/search/docs/appearance/structured-data/qapage） | 論壇 / 問答社群有價值；一般內容站不適用 | 只用在真實 UGC 問答頁 |
| `speakable` | 仍為 beta；只限美國、英文設定的 Google Home 裝置、新聞類主題查詢；每段約 20–30 秒（https://developers.google.com/search/docs/appearance/structured-data/speakable） | 對台灣市場幾乎為零；Assistant 轉為 Gemini 後文件未更新，是否仍生效待查證 | 只有美國英文新聞站考慮 |
| `Article` / `BlogPosting` | 支援（06 §2 第 1 項） | 作者、日期讓答案的時效與來源判斷正確 | 必備 |
| `Organization` / `Person` / `ProfilePage` | 支援（06 §2、§4） | 知識面板與 AI 回答中的品牌、作者實體對齊 | 必備，`sameAs` 全站一致（08 §4.3） |
| `VideoObject` + `Clip` / `SeekToAction` | 支援（06 §2 第 25 項） | 影片型精選摘要與「關鍵時刻」 | 影片為主要內容的頁面才標 |
| `Product` / `LocalBusiness` | 支援（06 §2；電商 19、本地 17） | 購物與本地類 AI 回答的價格、營業資訊 | 依專案類型 |
| `DiscussionForumPosting` | 支援（06 §2 第 6 項） | 「討論與論壇」區塊；AI 引擎偏好的「人味」來源 | 論壇站使用 |

**規範**：不為「餵答案引擎」新增任何沒有 rich result 或實體價值的標記；Google 指南明言生成式 AI 功能沒有專用 schema（§1.2）。其他引擎是否讀取 JSON-LD 各家未公開（06 §10）。

---

## 6. 品牌與實體被答案引擎提到

實體一致性的基本作法（Organization schema、`sameAs`、Wikidata、品牌名統一、真實第三方提及）詳見 08 §4.3，本節只補 AEO 特有的「推薦查詢測試法」與「答案修正流程」。

### 6.1 品牌推薦查詢測試法

**規範**：每月以固定提示集測試品牌在 4 個答案引擎中「是否被提到、是否被推薦、描述是否正確、引用哪個 URL」，結果存成可比較的時間序列。

**為什麼**：聊天引擎的推薦是非確定性的，單次查詢不能代表常態；固定樣本才看得出趨勢與修正效果。

**怎麼做**：
1. 提示集 30 題，分三類各 10 題：品牌直接查詢（「〔品牌〕是什麼 / 可信嗎」）、類別推薦（「台灣推薦的〇〇比較網站」）、比較（「〔品牌〕vs〔競品〕」）。每題準備英文、混語、繁中版本中與市場相關者。
2. 引擎：Google AI Mode、ChatGPT（開啟搜尋）、Perplexity、Gemini；Copilot 視 Bing 流量決定。
3. 條件：登出或新對話、關閉記憶與個人化、記錄國家 / 語言設定與日期。
4. 每題每引擎跑 3 次，記錄：是否提到（0/1）、排序位置、描述是否正確（正確 / 部分錯 / 錯）、引用 URL、引用的是本站還是第三方頁。
5. 指標：提及率 = 提到次數 / 總次數；正確率；本站 URL 被引用率。

**驗收方式**：試算表每月新增一欄，三個月可比；任何「描述錯誤」都轉成 §9 S10 的處理工單。

**常見錯誤**：用自己常用、有記憶的帳號測；只測一次就下結論；把「被提到」與「被連結」混為一談。

**2026-11 補充**：桌機品牌字查詢的 AI Overviews 有時出現在右側欄，也就是知識面板位置（08 §1.4）。抽測品牌查詢時，加記一欄「AIO 位置：主欄、右欄、無」，主欄與右欄對點擊的影響不同，不能混算。

### 6.2 答案修正流程（依管道）

| 錯誤出現在 | 修正管道 | 備註 |
|---|---|---|
| Google 知識面板 | 認領後用 Feedback 逐項標記並附證明連結（§2.4） | 已驗證者優先處理 |
| AIO / AI Mode / 精選摘要 | 先修正自家頁面與第三方來源，再用結果下方的意見回饋 | Google 不提供站方直接修改答案的管道 |
| ChatGPT / Perplexity / Gemini | 修正被引用的來源頁 → 等重新抓取；使用介面的回饋功能 | 站方專用修正表單：待查證 |
| 第三方目錄 / 維基 | 依各平台規則修改，不可自吹自擂（08 §4.3） | Wikipedia 有利益衝突規範 |

---

## 7. 量測：追蹤精選摘要、PAA 與 AI 引用

### 7.1 指標與資料來源

| 指標 | 資料來源 | 頻率 | 限制 |
|---|---|---|---|
| 精選摘要持有數 | 排名工具的 SERP feature 欄（是否持有、持有 URL） | 每週 | 工具樣本與地區設定決定準確度；台灣需確認工具支援該地區 |
| PAA 出現本站次數 | 排名工具或手動抽測 | 每月 | GSC 只在展開後計曝光 |
| AIO / AI Mode 曝光 | GSC Generative AI performance report | 每週 | 報表本身只有曝光、無查詢；點擊併入一般成效報表 Web 總體資料，無法單獨拆出（08 §10） |
| Copilot / Bing AI 引用 | Bing Webmaster Tools AI Performance | 每月 | 抽樣資料、無點擊（§7.4） |
| 聊天引擎推薦流量 | GA4 原生 AI Assistant 管道 + 自訂 regex 管道 | 每月 | 無 referrer 的 App 流量會落入 Direct |
| 品牌搜尋量 | GSC 品牌詞 regex + Google Trends | 每月 | 匿名查詢省略 |
| 推薦查詢提及率 / 正確率 | §6.1 測試表 | 每月 | 非確定性，需重複抽樣 |

### 7.2 GSC 的限制

- 沒有「精選摘要」或「PAA」的搜尋外觀篩選（官方成效報表說明頁未列，查閱 2026-11-04），只能用「排名約 1 + CTR 突變」間接推論，必須搭配排名工具確認。
- 精選摘要套用標準位置規則；AIO 整個區塊算一個位置；PAA 展開才算曝光；AIO 與 AI Mode 內連到外部頁的點擊都算點擊（https://support.google.com/webmasters/answer/7042828 ，查閱 2026-11-05），並計入 Web 搜尋類型的總體資料（https://developers.google.com/search/docs/appearance/ai-features ，查閱 2026-11-05）。Generative AI performance report 是另一份只看曝光的報表（https://support.google.com/webmasters/answer/16984139?hl=en ，查閱 2026-11-05）。
- 加了查詢或網址篩選後，總數會因匿名查詢省略與資料截斷而對不上（https://support.google.com/webmasters/answer/17011165 ）；問句 regex 的結果只能看趨勢，不能當成問句流量總量。

### 7.3 GA4 抓 AI 引擎推薦流量

- GA4 於 2026-05-13 推出 AI 助理流量量測，在預設管道群組加入「AI Assistant」（官方發版紀錄，https://support.google.com/analytics/answer/9164320?hl=en ，查閱 2026-11-05）。歸入條件是 medium 完全符合 `ai-assistant`；referrer 符合 Google 的 AI 助理清單時，GA4 會自動把 medium 設為 `ai-assistant`、campaign 設為 `(ai-assistant)`。所以只帶 `utm_source=chatgpt.com` 而沒有相符 referrer 時，不保證進這個管道。說明頁列舉 ChatGPT、Gemini、Deepseek、Copilot、Grok 等為例，**不含 Google AI Overviews 與 AI Mode**（後者仍算 Organic Search）（https://support.google.com/analytics/answer/9756891 ，查閱 2026-11-05）。
- 第三方檢查發現原生管道漏掉 Perplexity，部分 ChatGPT 流量落在 Referral 或 Unassigned（Search Engine Journal 2026-07-15，https://www.searchenginejournal.com/ga4s-ai-assistant-channel-undercounts-your-ai-traffic-how-to-build-one-that-doesnt/580133/ ，第三方觀察；Google 未公布完整清單，現況待查證）。
- 所以仍建立自訂管道群組，新增「AI 答案引擎」管道。GA4 把流量歸入第一個符合的管道，官方範例要求把 AI 管道排在 Referrals 之前，必要時也排在 Organic Search 等其他管道之前（https://support.google.com/analytics/answer/13051316 ，查閱 2026-11-05）；若群組內同時有原生 AI Assistant 管道，依同一規則也要排在它之前，才能把兩邊流量合併。條件：工作階段來源「部分符合 regex」：

```
(chatgpt\.com|chat\.openai\.com|perplexity\.ai|perplexity|gemini\.google\.com|copilot\.microsoft\.com|copilot\.com|claude\.ai|chat\.deepseek\.com|deepseek\.com|grok\.com|meta\.ai|chat\.mistral\.ai|you\.com|poe\.com)
```

  或工作階段媒介完全符合 `ai-assistant`（這條要生效，此管道必須排在原生 AI Assistant 之前）。每季用「來源 / 媒介」報表檢查有沒有新的 AI 網域。
- ChatGPT 在引用連結加 `utm_source=chatgpt.com`（OpenAI 發布者 FAQ），所以即使 App 不帶 referrer，上述自訂管道的來源條件多半仍能歸因 ChatGPT 流量（原生 AI Assistant 管道看 medium 或 referrer，不保證納入）；其他引擎的 App 流量可能落入 Direct，直接流量的異常成長要一併觀察。

### 7.4 Bing Webmaster Tools AI Performance

2026-02-10 以公開預覽推出：Total Citations、Average Cited Pages、頁面層級引用次數、時間趨勢，以及抽樣的 grounding queries（引擎檢索本站內容時用的關鍵片語），涵蓋 Copilot、Bing AI 摘要與部分合作夥伴，沒有點擊資料（https://blogs.bing.com/webmaster/2026/2/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview/ ，查閱 2026-11-04）。2026-06 再加 Intents、Topics、Citation Share、Compare 預覽功能（https://blogs.bing.com/search/June-2026/New-AI-Visibility-Insights-in-Bing-Webmaster-Tools-Intents-Topics-Citation-Share-Compare ）。2026-10-13 新增 Topics Portfolio（Beta），把 grounding queries 歸成主題，並列出其他網站有出現、本站沒有的機會查詢；主題分類由 AI 產生，官方提醒只當方向參考（https://blogs.bing.com/webmaster/2026/10/introducing-topics-portfolio-beta-in-ai-performance/ ，查閱 2026-11-05）。grounding queries 是 AI 檢索時用的關鍵片語抽樣，不等於使用者的原始問題；Bing 也說明引用資料不代表排名、權威或頁面在回答中的角色（2026-02 公告，查閱 2026-11-05）。可匯入 §3.4 母表當問題線索。工具設定詳見 13。

### 7.5 手動抽測樣本設計

**規範**：每月固定抽測 50 個目標問題，樣本分層、條件固定、結果可比。

**怎麼做**：
1. 分層：資訊型 25、商業 / 比較型 15、品牌型 10；語言依市場比例分配（例：zh-TW 30、en 20）。
2. 前 30 個固定不變（看趨勢），後 20 個每月輪換（看新問題）。
3. 條件：無痕視窗、登出、目標國家（VPN 或 `gl=tw` 與 `hl` 參數，兩者結果可能不同，固定用一種）、行動版 UA。
4. 每題記錄：精選摘要持有者與格式、PAA 前 4 題是否有本站、AIO 是否出現與是否引用本站、ChatGPT / Perplexity 是否引用本站。
5. 截圖存檔，檔名含日期與問題編號。

**驗收方式**：同一題兩位人員各測一次結果一致率 ≥ 80%；月報能列出「新增 / 失去」的答案版位清單。

**常見錯誤**：每月換一組問題導致不可比；用桌機在台灣測其他市場；只記錄有沒有被引用、不記錄被引用的段落。

---

## 8. 依專案類型的 AEO 策略

AI 搜尋層的專案策略見 08 §8，AdSense／聯盟內容站的投入優先順序（高／中／低，社群共識）見 08 §4.5；下表只列答案層的取捨。

| 專案類型 | 該爭取的答案版位 | 該放棄或降低投入的 | 關鍵作法 |
|---|---|---|---|
| 內容站 / 流量站（AdSense / 聯盟） | 比較表、步驟、在地化數值型問題（價格、時程、文件） | 一句話就能答完的定義題（Know Simple，02 §1） | 答案區塊給結論、頁面保留「必須點進來」的工具或完整表格（08 §8）；聯盟頁的比較表附揭露（09 §9） |
| 電商 | 產品比較、規格、尺寸、相容性問題；PAA 的購買前問題 | 泛知識型部落格文 | 產品頁加真實 Q&A 與規格表；Merchant Center 資料即時（19）；指南提到的 Business Agent 等代理式體驗屬選配 |
| 本地商家 | 「附近」「營業時間」「價格」「怎麼去」 | 全國性資訊題 | GBP 資料完整（17 §3）；落地頁回答在地問題；各目錄 NAP 一致 |
| 新聞 / 時效 | Top stories、AIO 中的偏好來源標章、即時事實問題 | Speakable（非美國英文市場） | 鼓勵讀者在 Google 偏好來源工具加入本站（只限網域或子網域，AIO / AI Mode 需未退出生成式 AI 功能，https://developers.google.com/search/docs/appearance/preferred-sources ，查閱 2026-11-04；詳見 20） |

**即時資料型站點**（以比分、匯率這類資料站為例）：
1. 答案區塊固定格式並在資料公布後數分鐘內更新：「A 隊 vs B 隊比分（2026-11-03，19:00 場）：〔比分〕；資料來源：〔官方資料源〕」。日期、場次、來源三項缺一不可，避免答案引擎把舊資料當今日結果。
2. H1 / title 含日期，歷史結果用每期一個穩定 URL 或歷史表；「today」頁只放最新一期並連到歷史頁，避免同一 URL 內容每天變動卻被快取成舊答案。
3. 與官方資料源對照的校驗程序寫進發布流程；錯誤數據被答案引擎引用的傷害遠大於晚幾分鐘發布。
4. Google 是否對該類查詢顯示自有即時答案模組：待查證（以 §7.5 抽測確認）；若有，該查詢的點擊預期要大幅下修，改攻歷史統計、趨勢比較等工具型問題。
5. 涉及博弈的資料不寫「保證中獎」「預測號碼」類答案。博弈類內容在 AdSense 的限制本知識庫 09 章尚未涵蓋，使用前查 AdSense Program policies 與 Google Publisher Restrictions（待查證）。

---

## 9. 問題排解：AEO 狀況與解法

結構依 12 章：症狀 / 可能原因 / 診斷步驟 / 解法 / 預防 / 預估恢復時間 / 證據等級。與 08 §11、12 B6 / C3 重疊的狀況只寫 AEO 特有部分。

| 編號 | 症狀 | 第一個要查的 |
|---|---|---|
| S1 | 精選摘要被競品拿走 | 競品答案格式 |
| S2 | 精選摘要顯示錯誤或過時內容 | 被擷取的段落 |
| S3 | 精選摘要整個消失 | 該查詢是否改出 AIO |
| S4 | 答案被摘走但點擊歸零 | GSC 曝光 / 點擊剪刀差 |
| S5 | PAA 引用競品、沒有本站 | 母表是否涵蓋該問題 |
| S6 | 答案區塊被截斷 | 清單項數與段落長度 |
| S7 | 被選中的是錯的段落 | 頁面有無更貼近問題的段落 |
| S8 | FAQ / HowTo rich result 消失 | 06 §3 退場清單 |
| S9 | 知識面板錯誤或沒有知識面板 | 實體資料一致性 |
| S10 | AI 引擎說錯品牌資訊 | 錯誤資訊的源頭 |
| S11 | 聊天引擎完全不引用本站 | 搜尋 bot 是否被擋 |
| S12 | 類別推薦查詢只推薦競品 | 第三方提及與比較頁 |
| S13 | 語音查詢沒出現、Speakable 無效 | 市場與語言支援 |
| S14 | 多語言版本答案錯配 | hreflang 與可見語言 |
| S15 | 即時資料答案過時 | 快取與更新時間 |
| S16 | 所有答案版位同時消失 | `nosnippet` / `max-snippet` |

### S1. 精選摘要被競品拿走

- **症狀**：排名工具顯示精選摘要持有者換成競品；GSC 該查詢 CTR 下滑、位置變化不大。
- **可能原因**：(1) 競品答案格式更貼近 SERP 偏好（例如改成表格或清單）；(2) 本站答案區塊被改長或移位；(3) 競品資料更新、本站過時；(4) 本站排名從前段掉出。
- **診斷步驟**：1. 截圖比較新舊持有者的格式、長度、日期；2. 用 Wayback 或 CMS 版本紀錄確認本站頁面最近改過什麼；3. 確認本站一般排名仍在前段（掉出前段先看 12 C2 / B5）。
- **解法**：依 §4 重寫答案區塊為 SERP 現行格式（05 §17 狀況表已列格式對照）；補最新數據與日期；在 GSC 要求重新索引。
- **預防**：每篇內容在 §3.4 母表記錄版位持有者，每週由排名工具告警。
- **預估恢復時間**：重新抓取後數天到 4 週；也可能不回來（Google 系統自動選取）。
- **證據等級**：Google 官方證實（自動選取、無法申請）；社群共識（格式對齊有效）。

### S2. 精選摘要顯示錯誤或過時內容

- **症狀**：本站持有精選摘要，但顯示的數字、日期或步驟已過時，或擷取到斷章取義的句子。
- **可能原因**：(1) 頁面已更新但 Google 尚未重新抓取；(2) 頁面上仍留有舊版段落（例如「2025 年價格」段）；(3) 擷取到反例或引述句。
- **診斷步驟**：1. URL 檢查工具看最後檢索日期與轉譯 HTML；2. 在頁面搜尋 SERP 顯示的句子，找到來源段落；3. 確認是否有 CDN 快取舊 HTML（12 E12）。
- **解法**：刪除或改寫舊段落、把過時資料移到明確標示「歷史資料」的表格；要求重新索引；必要時對誤導段落加 `data-nosnippet`；在 SERP 結果下方使用意見回饋。
- **預防**：會變動的數值用單一資料源（§4.6）；舊資料不與現行答案寫在同一段。
- **預估恢復時間**：重新索引後通常數天到 2 週。
- **證據等級**：Google 官方證實（`data-nosnippet`、重新索引）；個人經驗（時程）。

### S3. 精選摘要整個消失

- **症狀**：精選摘要不見、競品也沒有；SERP 頂部改為 AIO。
- **可能原因**：(1) 該查詢改由 AIO 回答（Serpstat 觀察兩者趨向不並存）；(2) Google 調整該類查詢的版面。
- **診斷步驟**：1. 目標國家抽測 SERP；2. GSC Generative AI report 看該頁 AI 曝光；3. 排名工具看同類查詢是否整批消失。
- **解法**：轉為爭取 AIO 引用（08 §4）；頁面加強摘要之外的價值；接受該查詢 CTR 新基準（08 §2.2）。
- **預防**：選題評分加入「精選摘要 / AIO 版位穩定性」（02 §7）。
- **預估恢復時間**：不會恢復到原狀；AIO 無法生成時可能偶爾退回精選摘要。
- **證據等級**：Google 官方證實（退回精選摘要的說法，Rajan Patel 2026-01）；社群共識（取代趨勢，第三方研究）。

### S4. 答案被摘走但點擊歸零

- **症狀**：本站持有精選摘要或被 AIO 引用，曝光上升、點擊接近零；GA4 該頁自然流量崩落。
- **可能原因**：答案區塊已完整滿足查詢（Know Simple），使用者沒有點擊理由。
- **診斷步驟**：1. GSC 看該頁查詢組成；2. 判斷是否一句話可答（02 §1）；3. 摘要範圍是否等於頁面全部價值。
- **解法**：保留精準答案（放棄只會讓給競品），把「下一步」放在摘要無法涵蓋處：計算機、可篩選表格、下載、在地化細節。不建議加 `nosnippet`（連一般摘要一起失去）。
- **預防**：選題時就為每篇設計「必須點進來的理由」（05 §17）。
- **預估恢復時間**：改版後 1–3 個月觀察點擊收斂；Know Simple 類查詢點擊不會恢復。
- **證據等級**：社群共識（零點擊現象，08 §2 研究）；個人經驗（頁型改造）。

### S5. PAA 引用競品，沒有本站

- **症狀**：主查詢本站排名前段，但 PAA 的問題全部連到競品。
- **可能原因**：(1) 沒有回答這些子問題；(2) 答案藏在長段落、沒有問題式標題；(3) 子問題意圖與本頁不符。
- **診斷步驟**：1. PAA 問題對照 §3.4 母表；2. 找本頁答案位置；3. 看競品答案格式與長度。
- **解法**：為缺漏問題補 H2 + 答案區塊，或併入 FAQ 區塊；有獨立需求者另開頁（避免蠶食）。
- **預防**：每個 cluster 每季重抓一次 PAA 樹更新母表。
- **預估恢復時間**：重新索引後 2–6 週。
- **證據等級**：社群共識；個人經驗。

### S6. 答案區塊被截斷

- **症狀**：精選摘要或 PAA 顯示到一半出現「…」或「更多項目」，關鍵資訊被截掉。
- **可能原因**：(1) 清單項目過多；(2) 段落過長；(3) 表格欄列太多，Google 只取部分；(4) `max-snippet` 數值設太小。
- **診斷步驟**：1. 量答案區塊字數與項數（§4.1）；2. 檢查 robots meta 與 `X-Robots-Tag` 的 `max-snippet`；3. 對照 SERP 截斷位置。
- **解法**：把關鍵資訊移到前 1–2 句或前 3 項；長清單拆成「階段」；表格把最重要的欄放左側；放寬 `max-snippet`（或 -1）。被截斷但仍帶點擊的「更多項目」可保留。
- **預防**：答案區塊格式寫進發布前檢查清單（14 C2）。
- **預估恢復時間**：重新索引後數天到 2 週。
- **證據等級**：Google 官方證實（`max-snippet` 影響摘要長度）；社群共識（項數與長度門檻，Google 未公布）。

### S7. 被選中的是錯的段落

- **症狀**：Google 選了頁尾、留言、反例段落或另一個問題的答案。
- **可能原因**：(1) 真正的答案段落沒有緊接問題標題；(2) 多個段落都在回答同一問題；(3) 留言區或推薦區塊內容與查詢更貼近。
- **診斷步驟**：1. 找出被擷取的段落；2. 檢查留言與推薦模組是否在初始 HTML 中。
- **解法**：讓唯一的答案段落緊接問題標題；刪除重複回答；對不該被擷取的區塊加 `data-nosnippet`。
- **預防**：一個問題只有一個主要答案位置（§4.7）。
- **預估恢復時間**：數天到 3 週。
- **證據等級**：Google 官方證實（`data-nosnippet`）；個人經驗。

### S8. FAQ / HowTo rich result 消失

- **症狀**：GSC 的 FAQ 增強功能報表消失或歸零；SERP 不再出現可展開問答；HowTo 早已不顯示。
- **可能原因**：Google 全面停用：FAQ 於 2026-05-07 停止顯示、2026-06-15 移除文件；HowTo 於 2023-09 停用（06 §3）。不是網站問題。
- **診斷步驟**：對照 06 §3 退場日期；確認點擊下滑只發生在原有 FAQ rich result 的頁面。
- **解法**：不再新增 `FAQPage` / `HowTo` 標記；舊標記不必急著移除（未使用的標記不造成問題，改版時順手清掉）；保留可見的 FAQ 與步驟內容；不要改用其他類型（如 `QAPage`）偽裝，屬違規標記風險（06 §9）。
- **預防**：每季對照 06 §3 與 Search Central 文件更新紀錄。
- **預估恢復時間**：不會恢復；點擊影響通常在 1 個月內穩定。
- **證據等級**：Google 官方證實。

### S9. 知識面板錯誤或沒有知識面板

- **症狀**：搜尋品牌名沒有知識面板，或面板中的 logo、創辦人、網址、成立日期錯誤。
- **可能原因**：(1) 實體在 Knowledge Graph 中尚未被辨識；(2) 各平台資料不一致；(3) 舊資料仍存在於高權威第三方頁面。
- **診斷步驟**：1. 檢查 Organization schema 與 `sameAs`；2. 盤點社群、目錄、Wikidata 資料；3. 確認面板是否可認領。
- **解法**：依 08 §4.3 統一實體資料；可認領者以官方帳號驗證後逐項回報（§2.4）；本地商家走 GBP（17）。
- **預防**：維護品牌資料單一來源表（08 §11）。
- **預估恢復時間**：回報後數週；面板生成無固定時程。
- **證據等級**：Google 官方證實（認領與回報流程）；社群共識（生成時程）。

### S10. AI 引擎說錯品牌資訊

- **症狀**：§6.1 測試中，答案引擎描述本站的成立時間、服務、價格或所有權錯誤。
- **可能原因**：(1) 引用了過時的第三方頁或本站舊頁；(2) 與同名實體混淆；(3) 本站沒有可擷取的「關於我們」答案段落。
- **診斷步驟**：1. 看錯誤答案引用的 URL；2. 各引擎重跑 3 次確認是否穩定錯誤；3. 檢查 About 頁有無品牌定義句。
- **解法**：先修正源頭（本站舊頁 301 或更新、第三方資料更正）；About 頁加 §4.3 格式的品牌定義句與關鍵事實表；依 §6.2 管道回報。08 §11 的通用作法不重複。
- **預防**：品牌事實表與 §6.1 每月測試。
- **預估恢復時間**：Google 系統隨重新抓取數週；聊天引擎依各家索引更新，數週到數月（個人經驗）。
- **證據等級**：社群共識；個人經驗。

### S11. 聊天引擎完全不引用本站

- **症狀**：Google 有排名或 AIO 引用，但 ChatGPT / Perplexity 從不引用；GA4 AI 管道近乎零。
- **可能原因**：(1) `OAI-SearchBot` / `PerplexityBot` 被 robots.txt 或 WAF 擋；(2) Bing 未索引；(3) 核心內容需 JS 才出現。
- **診斷步驟**：依 08 §11 第三列（Bing、日誌、robots）；另用 `curl -A` 模擬各 bot 確認初始 HTML 有答案區塊。
- **解法**：允許搜尋 bot、提交 Bing sitemap 與 IndexNow（08 §7、15）；答案區塊改伺服器端輸出。
- **預防**：WAF 規則白名單；每月檢查日誌中各搜尋 bot 的狀態碼。
- **預估恢復時間**：robots 變更約 24 小時生效（OpenAI、Perplexity 官方文件），引用出現數週。
- **證據等級**：社群共識（引用時程）；bot 與 robots 規則由 OpenAI、Perplexity 官方文件證實（非 Google）。

### S12. 類別推薦查詢只推薦競品

- **症狀**：「最好的〇〇網站」類提示中，聊天引擎穩定推薦競品，本站提及率近零。
- **可能原因**：(1) 第三方比較文、論壇、目錄中沒有本站；(2) 本站沒有清楚的「適合誰」定位頁；(3) 品牌名不一致導致實體分散。
- **診斷步驟**：1. 看推薦競品時引用哪些頁（多為第三方清單或 Reddit）；2. 這些頁是否提到本站；3. 品牌名拼法。
- **解法**：以真實方式出現在引擎引用的來源中（被媒體評測、在論壇真實回答問題，詳見 16；不可買提及）；建立本站的定位頁與比較頁並誠實列出競品優點。
- **預防**：數位公關與社群經營納入每季計畫。
- **預估恢復時間**：3–6 個月（個人經驗）。
- **證據等級**：Google 官方證實（人為製造提及無效，§1.2）；社群共識（第三方清單影響推薦）。

### S13. 語音查詢沒出現、Speakable 無效

- **症狀**：加了 `speakable` 標記，語音助理仍不朗讀本站；語音查詢量測不到任何流量。
- **可能原因**：Speakable 是 beta，只限美國、英文設定的 Google Home 裝置、新聞主題；手機上的 Assistant 逐步轉為 Gemini；Siri AI 尚未支援繁中（預計 2026 年底前加入，§2.5）。
- **診斷步驟**：1. 確認目標市場與語言是否在支援範圍；2. 確認內容是否為新聞類。
- **解法**：非美國英文新聞站移除 `speakable` 期待；把語音查詢視為 Gemini / 聊天引擎的問題，依 §4 與 08 §4 處理。
- **預防**：不為語音另做工程；每年檢查一次 §2.5 表。
- **預估恢復時間**：不適用。
- **證據等級**：Google 官方證實（Speakable 文件）；Apple、Amazon 官方公告（Siri AI 語言、Alexa+ 上線國家）；Assistant 停用時程為第三方報導。

### S14. 多語言版本答案錯配

- **症狀**：繁中查詢的答案引用本站英文或簡中頁；混語查詢拿到 `en-US` 頁。
- **可能原因**：(1) hreflang 缺回傳標記或與 canonical 衝突；(2) 目標語言版沒有該問題的答案區塊，Google 退而選其他語言；(3) 可見內文語言不明確（混語過多）。
- **診斷步驟**：1. 依 12 E5 / I2 檢查 hreflang 與 canonical；2. 確認各語言版是否都有同一問題的 H2 與答案；3. 用 `hl` / `gl` 參數重測。
- **解法**：補齊各語言版答案區塊（§4.8）；修正 hreflang（10 §2）；混語頁依 25 §3 明確主要語言。
- **預防**：母表的「語言 / 市場」欄確保每個問題在每個目標語言都有負責頁面。
- **預估恢復時間**：hreflang 修正後 2–8 週（12 I2）。
- **證據等級**：Google 官方證實（hreflang、可見內文判定語言）；個人經驗。

### S15. 即時資料答案過時

- **症狀**：AI 回答或精選摘要把昨天的比分、舊匯率、舊價格當成「今天」的答案，且引用本站。
- **可能原因**：(1) 「today」頁 URL 固定、內容每天變，答案引擎快取舊版；(2) 答案區塊沒有日期與場次；(3) CDN 或伺服器快取延遲更新。
- **診斷步驟**：1. 看引用的 URL 與擷取句是否含日期；2. 查 CDN 快取設定與 `Last-Modified`；3. 檢查 sitemap `lastmod` 是否即時。
- **解法**：答案區塊強制含日期、場次、來源（§8）；每期一個歷史 URL；更新後清除 CDN 快取並更新 `lastmod`；時效內容作法詳見 20 §20.6。
- **預防**：發布流程自動寫入日期欄位；資料公布後自動比對官方資料。
- **預估恢復時間**：Google 視重新抓取頻率數小時到數天；聊天引擎不確定。
- **證據等級**：社群共識；個人經驗。

### S16. 所有答案版位同時消失

- **症狀**：全站精選摘要、PAA、AIO 引用同一天消失，一般排名仍在，摘要變空白。
- **可能原因**：(1) 全站被加上 `nosnippet` 或極小的 `max-snippet`（SEO 外掛、主題更新、CDN 規則）；(2) 誤用 GSC「Search generative AI」控制項排除（只影響 AI 功能，08 §10）；(3) 大量內容改成 JS 渲染或藏入 tab。
- **診斷步驟**：1. URL 檢查工具看 robots meta 與 HTTP 標頭；2. 查 GSC 設定的生成式 AI 控制項狀態；3. 比對上線紀錄。
- **解法**：移除不必要的 snippet 限制並重新索引；恢復控制項為 include；答案區塊回到初始 HTML。
- **預防**：部署前自動檢查 robots meta 與 `X-Robots-Tag`（15）；控制項變更需紀錄。
- **預估恢復時間**：重新抓取後數天到 2 週；控制項生效通常數天（08 §10）。
- **證據等級**：Google 官方證實。

---

## 10. 本章檢查清單

- [ ] 每個 cluster 有問題母表（≥ 30 題、≥ 5 種來源、含繁中與混語變體），每題都有處理方式。（§3）
- [ ] GSC 已存好英文、繁中兩組問句 regex，每月看趨勢。（§3.2）
- [ ] 目標問題用問題式 H2，緊接 40–120 字答案區塊；步驟用 `<ol>`、比較用 HTML 表格。（§4.1–4.5）
- [ ] 答案區塊與標題之間沒有廣告、tab、折疊區；內容在初始 HTML。（§4.2）
- [ ] 會變動的答案寫「截至日期」，資料單一來源、`dateModified` 真實。（§4.6）
- [ ] 新頁不加 `FAQPage` / `HowTo` 標記（舊標記不必主動移除）；`QAPage` 只用於真實 UGC 問答；非美國英文新聞站不投入 `speakable`。（§5）
- [ ] 各語言版本都有對應答案區塊，hreflang 正確。（§4.8）
- [ ] 每月跑品牌推薦查詢測試（30 題 × 4 引擎 × 3 次），描述錯誤轉成工單。（§6）
- [ ] 排名工具追蹤精選摘要與 PAA 持有；GA4 自訂「AI 答案引擎」管道排在 Referral 與其他會先匹配的管道（原生 AI Assistant、Organic Search 等）之前；Bing AI Performance 已啟用。（§7）
- [ ] 每月 50 題手動抽測，前 30 題固定。（§7.5）
- [ ] 部署前檢查 `nosnippet` / `max-snippet` 與 GSC 生成式 AI 控制項。（§9 S16）
- [ ] 每季重查 §2 版位現況與 06 §3 退場清單。

---

## 11. 參考來源

（未另註者查閱日期皆為 2026-11-04；2026-11-05 修訂時新增或重新核對的來源逐條註明）

**Google 官方**
- Google Search Central — Optimizing your website for generative AI features（2026-05-15 新增）：https://developers.google.com/search/docs/fundamentals/ai-optimization-guide
- Google Search Central — Latest documentation updates（2026-05-15 垃圾政策適用生成式 AI 回答、2026-05-08 / 06-15 FAQ 停用與移除、2026-03-24 QAPage 屬性、2026-04-20 Read more 深連結、2026-05-27 偏好來源擴及 AIO / AI Mode）：https://developers.google.com/search/updates
- Google Search Central — Spam policies for Google web search：https://developers.google.com/search/docs/essentials/spam-policies
- Google Search Central — Featured snippets and your website：https://developers.google.com/search/docs/appearance/featured-snippets
- Google Search Central — Control your snippets in search results（Read more 深連結、`nosnippet`、`max-snippet`、`data-nosnippet`）：https://developers.google.com/search/docs/appearance/snippet
- Google Search Central — Speakable（beta）：https://developers.google.com/search/docs/appearance/structured-data/speakable
- Google Search Central — Q&A（QAPage）structured data：https://developers.google.com/search/docs/appearance/structured-data/qapage
- Google Search Central — Preferred sources：https://developers.google.com/search/docs/appearance/preferred-sources
- Google Search Central — AI features and your website（query fan-out、計入 Search Console Web 總體資料；查閱 2026-11-05）：https://developers.google.com/search/docs/appearance/ai-features
- Google Search Central — Video SEO best practices（key moments；查閱 2026-11-05）：https://developers.google.com/search/docs/appearance/video
- Google Search Central Blog — Changes to HowTo and FAQ rich results（2023-08；查閱 2026-11-05）：https://developers.google.com/search/blog/2023/08/howto-faq-changes
- Google Search Console Help — Performance report：位置、曝光、點擊的計算（精選摘要、PAA、AIO）：https://support.google.com/webmasters/answer/7042828
- Google Search Console Help — Search generative AI performance report（只提供曝光；查閱 2026-11-05）：https://support.google.com/webmasters/answer/16984139?hl=en
- Google Search Console Help — Performance report: Advanced filtering and comparison（RE2 regex、匿名查詢）：https://support.google.com/webmasters/answer/17011165
- Search Console API — Search Analytics: query（regex 4,096 字元上限）：https://developers.google.com/webmaster-tools/v1/searchanalytics/query
- Google Knowledge Panel Help — 認領與更新知識面板：https://support.google.com/knowledgepanel/answer/7534902
- Google Analytics Help — Default channel group（AI Assistant 管道；查閱 2026-11-05）：https://support.google.com/analytics/answer/9756891
- Google Analytics Help — What's new in Google Analytics（2026-05-13 AI Assistant 發版紀錄；查閱 2026-11-05）：https://support.google.com/analytics/answer/9164320?hl=en
- Google Analytics Help — Custom channel groups（第一個符合的管道、排序範例；查閱 2026-11-05）：https://support.google.com/analytics/answer/13051316
- Google Blog — The Assistant experience on mobile is upgrading to Gemini（2025-03-14，未列 2026-09-04 時程；查閱 2026-11-05）：https://blog.google/products-and-platforms/products/gemini/google-assistant-gemini-mobile/
- Google Blog — Gemini for Home launch：https://blog.google/products-and-platforms/devices/google-nest/gemini-for-home-launch/
- Google Home Help — Assistant 與 Gemini for Home 支援語言及國家（查閱 2026-11-05）：https://support.google.com/googlehome/answer/7550584?hl=en

**其他引擎官方**
- Microsoft Bing Webmaster Blog — Introducing AI Performance in Bing Webmaster Tools Public Preview（2026-02-10）：https://blogs.bing.com/webmaster/2026/2/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview/
- Microsoft Bing Blog — New AI Visibility Insights in Bing Webmaster Tools（2026-06）：https://blogs.bing.com/search/June-2026/New-AI-Visibility-Insights-in-Bing-Webmaster-Tools-Intents-Topics-Citation-Share-Compare
- Microsoft Bing Webmaster Blog — Introducing Topics Portfolio (Beta) in AI Performance（2026-10-13；查閱 2026-11-05）：https://blogs.bing.com/webmaster/2026/10/introducing-topics-portfolio-beta-in-ai-performance/
- OpenAI — Publishers and developers FAQ（`utm_source=chatgpt.com`；本次直接讀取回 403，依搜尋摘錄）：https://help.openai.com/en/articles/12627856-publishers-and-developers-faq
- Perplexity — Perplexity crawlers：https://docs.perplexity.ai/guides/bots
- Apple Newsroom — Siri AI is available in more languages starting today（2026-10-26；查閱 2026-11-05）：https://www.apple.com/newsroom/2026/10/siri-ai-is-available-in-more-languages-starting-today/
- Apple Support — How to get Siri AI（支援語言、裝置與地區限制；查閱 2026-11-05）：https://support.apple.com/en-us/127893
- About Amazon — Alexa+ 國際上線清單（2026-10-28 更新；查閱 2026-11-05）：https://www.aboutamazon.com/news/devices/alexa-plus-international-launch

**研究與報導**
- Ahrefs — How SERP Features Have Evolved in the AI Era（2025-07-22，100 萬美國桌機 SERP）：https://ahrefs.com/blog/how-serp-features-have-evolved-in-the-ai-era
- Serpstat — Year in Search: AI Overview study（2025-12-25）：https://serpstat.com/blog/year-in-search-ai-overview-study
- Search Engine Roundtable — Google Falls Back To Featured Snippets When AI Overviews Don't Generate（2026-01-23）：https://www.seroundtable.com/google-featured-snippets-ai-overviews-fail-40805.html
- Search Engine Roundtable — Google Tests Pink Highlights In Featured Snippets（2026-08-24）：https://www.seroundtable.com/google-pink-highlights-featured-snippets-41926.html
- Search Engine Roundtable — Featured snippet deduplication change summary（2020-01）：https://seroundtable.com/google-featured-snippet-deduplication-change-summary-28921.html
- Search Engine Journal — GA4's AI Assistant channel undercounts your AI traffic（2026-07-15）：https://www.searchenginejournal.com/ga4s-ai-assistant-channel-undercounts-your-ai-traffic-how-to-build-one-that-doesnt/580133/
- 9to5Google — Google Assistant shutting down on Android and Wear OS in September（2026-08-04）：https://9to5google.com/2026/08/04/google-assistant-september-2026-shutdown/
- MacRumors — iOS 27: Everything We Know（iOS 27 於 2026-09-14 推出、Gemini 技術、英文地區清單；第三方彙整，查閱 2026-11-05）：https://www.macrumors.com/roundup/ios-27/
- Mark Williams-Cook（AlsoAsked）LinkedIn 貼文 — PAA 答案的 AIO 比例（2026-09，約 1,920 萬筆英文樣本；查閱 2026-11-05）：https://www.linkedin.com/feed/update/urn:li:activity:7503164423075725313/
- Search Engine Roundtable — Almost 100% Of People Also Ask Results Are Answered By Google AI Overviews（2026-09-09；查閱 2026-11-05）：https://seroundtable.com/ppa-ai-overviews-google-42047.html

**本知識庫交叉引用**：02 §1–§2、§7、§12；05 §6、§13.1、§17；06 §2、§3、§9、§10；07 §5.2；08 §1–§11；09 §7、§9；10 §1、§2；25 §3；12 B6、C3、E5、E12、I2；13；15；16；17；19；20 §20.5、§20.6。
