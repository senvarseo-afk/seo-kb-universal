# 17 本地 SEO 與 Google 商家檔案（Google Business Profile）

> 版本：1.0 ｜ 更新日期：2026-11-09 ｜ 適用：所有 SEO 網站專案 ｜ 撰寫：Claude

## 本章摘要

1. 本地排名 = Google 官方三要素：Relevance、Distance、Prominence；可操作的最大槓桿是主要類別、商家名稱、評論。
2. Google Business Profile（GBP）是核心資產；2026 年政策收緊：檔案不可含限時促銷 / 價格 / 直接 CTA，禁止員工評論配額與指定評論內容。
3. 評論只能「邀請真實顧客、不給誘因、不篩選」，並 100% 回覆。
4. 多據點 / 多服務區域「一據點一頁、一服務一頁」；NAP 在網站、GBP、引用來源逐字一致。
5. 停權多源於名稱 / 地址 / 類別違規或可疑編輯；申訴前先修正根因，絕不另建新檔案。

## 目錄

1. [適用範圍與專案類型](#1-適用範圍與專案類型)
2. [本地搜尋排名因素](#2-本地搜尋排名因素)
3. [GBP 完整優化規範](#3-gbp-完整優化規範)
4. [GBP 政策、停權與申訴](#4-gbp-政策停權與申訴)
5. [NAP 一致性與引用（Citations）](#5-nap-一致性與引用citations)
6. [評論策略與回覆規範](#6-評論策略與回覆規範)
7. [本地關鍵字與落地頁架構](#7-本地關鍵字與落地頁架構)
8. [LocalBusiness 結構化資料要點](#8-localbusiness-結構化資料要點)
9. [本地連結與社群](#9-本地連結與社群)
10. [Apple Business Connect 與 Bing Places](#10-apple-business-connect-與-bing-places)
11. [地圖包（Local Pack）追蹤工具](#11-地圖包local-pack追蹤工具)
12. [狀況 → 解法表](#12-狀況--解法表)
13. [本章檢查清單](#13-本章檢查清單)
14. [參考來源](#14-參考來源)

---

## 1. 適用範圍與專案類型

| 專案類型 | 適用程度 | 說明 |
|---|---|---|
| 本地商家 | 核心 | 全章適用，GBP 第一優先 |
| 企業官網（有辦公室 / 門市） | 高 | GBP、NAP、LocalBusiness schema、據點頁 |
| 電商（有實體店 / 取貨點） | 中 | GBP 店內商品 + Merchant Center 本地庫存（詳見 19） |
| SaaS | 低 | GBP 僅作品牌實體訊號 |
| 流量站 / 內容站 | 低～中 | 自身無 GBP；「{城市} 最佳 XX」清單用第 7、9 節原則；「專家精選清單」是 Whitespark 2026 AI 本地可見度第 1 因素 |

結構化資料語法詳見 06、hreflang 詳見 10、CWV 詳見 04。

---

## 2. 本地搜尋排名因素

### 2.1 Google 官方三要素

**規範**：所有本地 SEO 決策都要對應到相關性、距離、知名度之一，無法對應的工作先砍。

**為什麼**：Google 官方指出本地結果「主要基於 relevance、distance、prominence」，且「There's no way to request or pay for a better local ranking on Google」（來源：support.google.com/business/answer/7091，查閱 2026-11-03）。

| 要素 | Google 定義 | 可操作項目 |
|---|---|---|
| Relevance | 商家檔案與搜尋意圖的匹配程度 | 類別、名稱、服務 / 商品、描述、屬性、落地頁內容 |
| Distance | 商家與搜尋者（或搜尋詞地點）的距離 | 地址真實性、釘點、服務區域、多據點佈局（只能正確設定，無法優化） |
| Prominence | 知名程度：連結數、評論數與評分、目錄與文章提及、網站一般 SEO 表現 | 評論、本地連結、引用、媒體提及、網站權威 |

### 2.2 業界調查的權重（實務參考）

**為什麼**：Whitespark《2026 Local Search Ranking Factors》（47 位專家評分 187 項因素，2025-11-06 發布）是最完整的實務調查，但屬專家意見而非 Google 證實的因果（來源：whitespark.ca/local-search-ranking-factors，查閱 2026-11-03）。地圖包前 15 名因素（調查加權分）：

| 排名 | 因素 | 分數 | 對應三要素 |
|---|---|---|---|
| 1 | GBP 主要類別 | 227 | 相關性 |
| 2 | 商家地址與搜尋點的距離 | 225 | 距離 |
| 3 | 商家名稱中的關鍵字 | 223 | 相關性（但須符合政策，見 3.2） |
| 4 | 實體地址位於搜尋城市內 | 213 | 距離 |
| 5 | 搜尋時正在營業（營業時間） | 189 | 相關性 |
| 6 | 高數值評分（4–5 星） | 181 | 知名度 |
| 7 | GBP 顯示地址（非服務區域商家） | 176 | 距離 |
| 8 | GBP 次要類別 | 173 | 相關性 |
| 9 | 含文字的原生 Google 評論數量 | 170 | 知名度 |
| 10 | 地圖釘位置正確 | 165 | 距離 |
| 11 | 評論新鮮度 | 164 | 知名度 |
| 12 | 地址與城市中心點距離 | 157 | 距離 |
| 13 | 地圖包 / Maps 結果的點閱率 | 156 | 行為訊號 |
| 14 | 評論持續穩定流入 | 154 | 知名度 |
| 15 | 網站 HTML 上的 NAP 與 GBP 一致 | 153 | 相關性 / 信任 |

2026 年版趨勢：評論與行為訊號上升；頁面、連結、引用訊號小幅下降；新增「社群訊號」。「負面影響 / 停權風險」前幾名：網站 URL 轉址到不同網域（115 / 115）、SAB 卻顯示地址（39 / 105）、多據點服務區域重疊（71 / 102）、服務區域 > 2 小時車程（53 / 82）、AI 生成照片 / 影片（55 / 45）、貼文關鍵字堆砌（38 / 51）。

**驗收方式**：每個專案建「因素 → 現況 → 行動」表。

**常見錯誤**：預算花在引用量產卻沒選對主要類別；為「距離」租虛擬辦公室（直接違反政策）。

**AI Mode 預約連結（2026-11-04，美國）**：Google 的 Robby Stein 宣布，AI Mode 的居家服務結果可直接連到 Angi、Thumbtack、Housecall Pro、Jobber 預約或詢價，ServiceTitan 之後加入。Housecall Pro 表示其用戶自動加入且不收導客費；Jobber 建議使用可預約的表單並持續累積評論。Google 未說明業者如何被選中，也未表示加入合作平台會影響推薦，不要把它當排名因素。台灣與其他地區目前沒有對應功能。來源：Search Engine Journal、Angi 新聞稿、Housecall Pro 說明頁（查閱 2026-11-08）。

---

## 3. GBP 完整優化規範

### 3.1 驗證（Verification）

**規範**：以 Google 指定方式完成驗證；影片驗證準備「一鏡到底、3 分鐘內」的影片，依序拍外觀招牌與門牌 → 內部環境 → 管理權證明（開門、收銀機、員工制服、工具車）。

**為什麼**：Google 指出驗證「證明你有權代表該商家」，是出現在本地結果的前提（來源：support.google.com/business/answer/7091，查閱 2026-11-03）；影片驗證 FAQ 要求一段連續影片（Search Engine Roundtable 轉述，2023）。多篇 2026 年第三方文章指出影片驗證已是新檔案、地址變更、高風險類別的主要方式，2025-04 起有「影片預覽」可送出前自檢；官方未公布比例；影片驗證為常見方式之一。

**怎麼做**：驗證前先完成名稱、地址、類別、電話、網站並確認與招牌、官網、登記一致；影片不拍人臉與個資文件；SAB 拍有商標的車輛、工具與遮蔽個資的登記文件；地址變更會觸發重新驗證，先備妥素材。

**驗收方式**：GBP 顯示「已驗證」；Knowledge Panel 的「你是這家商家的擁有者嗎？」消失。

**常見錯誤**：影片剪接拼接；驗證失敗後另建新檔案（造成重複與停權）。

### 3.2 商家名稱

**規範**：名稱只能是「招牌、官網、公司文件一致使用的真實名稱」；不加關鍵字、城市、標語、電話、網址、「位於 XX 內」。

**為什麼**：Google 商家代表指南禁止名稱加入標語、商店代碼、營業時間、電話、網址、服務描述、地點、containment 資訊；全大寫、商標符號、LLC / Inc 需有真實世界一致使用的證明（來源：support.google.com/business/answer/3038177，查閱 2026-11-03）。「名稱含關鍵字」雖排 Whitespark 第 3，但塞字是停權與被競爭者檢舉的首要原因。

**怎麼做**：真實名稱本身含服務詞（「大安牙醫診所」）可用；不含就不為 SEO 改名。連鎖各據點名稱一致。

**常見錯誤**：名稱加「| 台北推薦」；以多語言 / 多字體重複同一名稱（指南禁止）。

### 3.3 類別（Categories）

**規範**：主要類別選最具體、描述商家「是什麼」的一個；次要類別只補確實提供的核心業務（一般 2–5 個）。

**為什麼**：主要類別是 Whitespark 第 1 因素；Google 指南要求「用最少的類別描述核心業務，類別描述商家是什麼而非提供什麼」，且不得用同址其他商家的類別（來源：support.google.com/business/answer/3038177）。

**怎麼做**：用 GMB Everywhere / PlePer 查地圖包前 3 名競爭者的主要類別；主要類別 = 最高價值主服務，每 6 個月檢查 Google 是否新增更精準類別；同址獨立營運的部門（旅館內餐廳、超市內藥局）依指南建獨立檔案。

**驗收方式**：GBP Performance「搜尋字詞」符合主要類別意圖；Local Falcon 目標關鍵字排名提升。

**常見錯誤**：主要類別太廣（「商店」而非「寵物用品店」）；加 10 個無關類別觸發審核。

### 3.4 地址、地圖釘與服務區域

**規範**：有實體店面才顯示地址；到府服務的 SAB 隱藏地址並以城市 / 郵遞區號設定服務區域（≤ 約 2 小時車程）；地圖釘放正門。

**為什麼**：Google 指南：虛擬辦公室不符資格；共享辦公室需有招牌且營業時間內有員工現場服務；P.O. Box 不可；SAB 以一個檔案代表總部並隱藏地址；服務區域一般不超過 2 小時車程（來源：support.google.com/business/answer/3038177，查閱 2026-11-03）。「SAB 顯示地址」與「服務區域重疊」是 Whitespark 停權風險前 3。

**怎麼做**：樓層 / 室填地址第二行；地址不含關鍵字或 URL；釘點放建築正門。

**常見錯誤**：在家開業卻顯示住家地址（應改 SAB 隱藏）；跨縣市設一個超大服務區域。

### 3.5 營業時間與特殊時間

**規範**：填面對顧客的實際營業時間；假日、颱風假、季節性休業用「特殊營業時間」提前設定；暫停營業用「暫時歇業」而非刪除時間。

**為什麼**：「搜尋時正在營業」是 Whitespark 第 5 因素；Google 指南要求列顧客可到訪的常規時間，旅館、學校、僅預約制不應列時間（來源：support.google.com/business/answer/3038177）。

**怎麼做**：每季排程未來 3 個月假日；24 小時客服但門市非 24 小時者只填門市時間。

**驗收方式**：搜尋顯示的「營業中 / 已打烊」與實際一致，無「營業時間可能不同」提示。

### 3.6 電話與網站 URL

**規範**：填該據點直撥電話；網站 URL 指向該據點專屬落地頁，不可轉址到其他網域。

**為什麼**：Google 指南要求電話與網站連到特定據點、商家直接控制號碼（來源同上）；「網站 URL 轉址到不同網域」是 Whitespark 停權風險第 1 名。

**怎麼做**：多據點每據點 URL `/locations/{city}/`；追蹤電話只能「主要電話填真實號碼、追蹤號碼填附加電話」且長期持有。URL 加 `?utm_source=google&utm_medium=organic&utm_campaign=gbp` 以便在 GA4 區分。

### 3.7 商家描述（Description）

**規範**：≤ 750 字元（前 250 字元在摘要可見），寫商家是誰、提供什麼、服務哪裡、特色；不含限時促銷、價格、直接 CTA、連結、關鍵字堆砌。

**為什麼**：Google 指南要求描述相關、乾淨、無連結，「不應聚焦促銷、價格、特賣」，不允許範例：「Everything on sale, -50%」（來源：support.google.com/business/answer/3038177）。2026-10 Google 更新 Prohibited and restricted content 的 Advertising & solicitation 段：「商家檔案（listings）不得含有限時促銷、價格或直接 CTA 的促銷 / 商業內容」；貼文仍允許優惠與更新，但不得含與商家無關的 email、電話、社群連結、外站連結（來源：support.google.com/business/answer/7400114，查閱 2026-11-03；Search Engine Roundtable 2026-10-06）。政策頁（7400114）只分「Listings」「Posts」「Users（評論）」三類，未逐欄位列出 listing 涵蓋哪些欄位；對照 Guidelines（3038177）逐欄位可確認的是：商家名稱不得含行銷標語與產品／服務資訊，描述不得聚焦促銷、價格、特賣且不得放連結，商品須遵守 Shopping Ads 政策（受管制商品不得有 CTA、優惠、價格）。服務、屬性等其他欄位官方未明文，保守做法：所有 listing 欄位都不放限時促銷、價格比較或 CTA，優惠一律放貼文（查閱 2026-11-03）。

**怎麼做**：一句定位（主服務 + 城市）→ 3–5 項核心服務 → 差異化（年資、認證、在地故事）→ 服務區域；不用 AI 泛用文案（Whitespark 列為負面因素）。

### 3.8 屬性（Attributes）

**規範**：填滿所有適用屬性（無障礙、付款、服務選項、設施）；每月檢查新增的類別專屬屬性；不勾選未真實提供的屬性。

**為什麼**：Google 把「停車、Wi-Fi 等屬性」列入「完整資訊」範例，完整資訊的商家「更可能出現在本地結果」（來源：support.google.com/business/answer/7091）；屬性也用於「附近提供外送的餐廳」等篩選查詢。

### 3.9 照片與影片

**規範**：首月 ≥ 20 張實拍（外觀、內部、團隊、商品 / 服務、工作過程），之後每月 3–5 張；不用 AI 生成或素材庫圖；影片 30 秒內、100MB 以下、720p 以上（GBP 介面限制）。

**為什麼**：Google 建議「新增照片和影片展示你提供什麼」（來源同上）；AI 生成影像是 Whitespark 2026 新列的負面 / 停權風險因素。

**怎麼做**：封面照代表核心業務；商標正方形；EXIF 地理資訊對排名無證據；定期檢舉顧客上傳的違規照片。

### 3.10 貼文（Posts / Updates）

**規範**：每週至少 1 則貼文；促銷、價格、CTA 只放貼文而非描述；不塞關鍵字、不放無關外連。2026-10 政策把促銷內容歸到 Posts 允許、檔案本身禁止（來源同 3.7）；貼文關鍵字堆砌是 Whitespark 停權風險因素（51 分）。

**怎麼做**：「優惠」填起訖日與優惠碼、「活動」填時間、「更新」寫近況；每則配 1200×900 以上圖片，CTA 連到對應落地頁並加 UTM。

**驗收方式**：貼文狀態「已發布」而非「已拒絕」；GA4 可見 `utm_campaign=gbp_post` 流量。

### 3.11 商品（Products）與服務（Services）

**規範**：零售在「商品」填主力品項（名稱、類別、固定價、描述、圖、連結）；服務類在「服務」填每項服務並對應網站服務頁；價格填固定價或留白，不填區間。

**為什麼**：Google 自 2023-02-15 起不允許商品價格區間（來源：Search Engine Land；查閱 2026-11-03）；官方指出符合條件地區的零售商可顯示「店內商品」並在本地結果顯示庫存（來源：support.google.com/business/answer/7091）。大量 SKU 改走 Merchant Center 本地庫存（詳見 19 第 9 節）。

**常見錯誤**：服務名稱塞城市關鍵字；商品描述放限時促銷（違反 3.7）。

### 3.12 Q&A（問與答）

**規範**：若後台仍可新增問題則建立 5–10 題並自答，否則 FAQ 改放網站落地頁；每週檢查，24 小時內回覆；錯誤答案檢舉。任何人都可回答，放任會出現錯誤資訊。Q&A API 已於 2025-11-03 停用；Google 員工（非產品專家）Dan Boguslavsky 2025-12-03 在 Google Business Profile 說明社群公告「A heads up about the upcoming changes to the Q&A feature」：顧客可在 Maps 直接提問並即時得到依商家回答與評論生成的答案；既有問題仍可在 Business Profile 回答；已發布的 Q&A 仍可供 Maps 參考（來源：https://support.google.com/business/thread/392024106 ，查閱 2026-11-03）。Gold 產品專家 Faris Abdulaziz 2025-12-05（12-08 編輯）在討論串「Q&A button missing」說明 Q&A 正逐步被 AI 系統「Ask about this place」（第三方簡稱 Ask 按鈕）取代（來源：https://support.google.com/business/thread/392365178 ，查閱 2026-11-03）；Search Engine Roundtable 2025-12-15 的報導為上述貼文的轉述。Google 說明中心無獨立公告頁，「Ask about this place」的地區／類別限制僅第三方觀察。FAQ 同步放在網站落地頁（詳見 06）。

### 3.13 預約、訂位與連結

**規範**：用 GBP 支援的預約夥伴或填自家預約頁；外送 / 訂位 / 菜單連結只能連到商家直接控制或正式合作的頁面（Business links policies；未授權連結會被移除）。驗收看 GBP Performance 的預約次數。

### 3.14 已停用 / 已變更的 GBP 功能（避免引用過時教學）

| 功能 | 狀態 | 日期與來源（查閱 2026-11-03） |
|---|---|---|
| 內建聊天（Chat）與通話紀錄 | 已停用 | 2024-07-31 完全移除（第三方轉述 Google 公告） |
| GBP 免費網站 | 已停用 | 2024-03 關閉，轉址 2024-06-10 結束 |
| Q&A API | 已停用 | 2025-11-03（第三方報導） |
| 短網址名稱（@name） | 停止顯示、不可新建 | 2026-02（Search Engine Roundtable） |
| 商品價格區間 | 不允許 | 2023-02-15（Search Engine Land） |
| Google My Business App；Insights 同業比較 | 已停用 / 已移除 | 2022；改於 Maps / Search 內管理，Performance 僅提供絕對數 |

---

## 4. GBP 政策、停權與申訴

### 4.1 停權類型

| 類型 | 症狀 | 常見原因 |
|---|---|---|
| 軟停權 | 檔案仍在地圖但失去管理權 | 帳號問題、可疑擁有權變更 |
| 硬停權 | 檔案從 Search / Maps 消失 | 名稱 / 地址 / 類別違規、虛擬辦公室、重複檔案、禁限制產業 |
| 評論限制 | 顯示警告、暫停新評論 | 偵測到付費 / 誘因評論（Google 稱 2025 年封鎖或移除逾 2.92 億則違規評論，第三方轉述，查閱 2026-11-03） |
| 帳號限制 | 整個帳號無法管理任何檔案 | 多檔案違規、可疑行為 |

### 4.2 高風險行為清單（停權前兆）

1. 同時大幅修改名稱、地址、主要類別。
2. SAB 顯示地址 / 住家地址；虛擬或無招牌的共享辦公室。
3. 網站 URL 轉址到其他網域。
4. 同一帳號管理大量不同產業檔案（代理商帳號）。
5. 高風險類別（鎖匠、搬家、水電 / 清潔、律師、戒癮、車庫門等）審核更嚴。
6. 短時間湧入大量 5 星、同 IP / 裝置評論；AI 生成照片或文案。

### 4.3 申訴流程

**規範**：先修正所有違規，再用官方 Appeals tool 送出一次完整的申訴並附齊文件；同一決定只能申訴一次；絕不新建同商家檔案。

**怎麼做**（來源：support.google.com/business/answer/4569145，查閱 2026-11-03）：
1. 對照指南修正名稱、地址、類別、網站。
2. 以管理該檔案的帳號開啟 Appeals tool，選擇檔案與要申訴的決定。
3. 上傳證據：公司登記 / 營業執照 / 稅籍證明、商家名義的水電 / 電話帳單（名稱地址須與檔案完全一致）、招牌 / 店面 / 車輛照片；一段式說明商家是什麼、位於哪、已修正什麼。
4. 等 email 決定（Google 未承諾時程）。被拒後可要求額外審核並補新證據；EEA 另有救濟管道。
5. > 10 個停權檔案可用 bulk appeal 附 Business Profile ID 試算表；帳號被限制者先在「My accounts」申訴帳號。

**驗收方式**：Appeals tool 狀態 Submitted → Approved；Maps 可重新搜尋到檔案。

**常見錯誤**：未修正就申訴（最常見被拒原因）；同時建新檔案；用代理商帳號申訴；證據地址與檔案不一致。

---

## 5. NAP 一致性與引用（Citations）

### 5.1 NAP 一致性

**規範**：NAP 在 GBP、網站（頁尾、聯絡頁、據點頁）、schema、社群、所有目錄逐字一致（含「號 / 樓」寫法、電話格式）。「網站 NAP 與 GBP 一致」是 Whitespark 2026 第 15 因素；Google 以一致性判斷不同來源指向同一商家。

**怎麼做**：建立「NAP 主檔」試算表（正式名稱、中 / 英地址、E.164 電話、URL、營業時間、類別）；網站頁尾放文字版 NAP 並與 `LocalBusiness` schema 相同；每季用 BrightLocal Citation Tracker / Whitespark Local Citation Finder / Semrush Listing Management 掃描並修正；搬遷或改名依序更新 GBP → 網站與 schema → 前 20 大目錄，舊地址做「已搬遷」頁而非刪除。

**驗收方式**：引用一致率 ≥ 95%；搜尋舊電話 / 舊地址不再出現舊資訊。

### 5.2 引用來源的優先順序

| 層級 | 來源 | 做法 |
|---|---|---|
| 1（必做） | GBP、Apple Business Connect、Bing Places、Facebook、LinkedIn | 擁有並驗證 |
| 2（聚合商 / 主流平台） | 美國：Data Axle、Foursquare、Neustar/Localeze；台灣 / 東南亞無統一聚合商，以當地主流平台為準 | 一次提交、年度檢查 |
| 3（產業 / 地區目錄） | 商會、公會、地方新聞商家目錄、社區網站 | 挑真人審核、DR 高者，寧缺勿濫 |
| 4（非結構化引用） | 新聞、部落格、Podcast、YouTube 中的品牌 + 地址提及 | 2026 年 AI 搜尋可見度最被重視的訊號（Whitespark：品質第 4、數量第 7） |

**常見錯誤**：購買「500 個目錄提交」套餐（垃圾目錄且無法更新）；多據點共用總公司電話。

---

## 6. 評論策略與回覆規範

### 6.1 政策底線（必讀）

**規範**：只能邀請每一位真實顧客留真實評論；不給報酬 / 折扣 / 贈品，不篩選，不設員工配額，不要求提及特定員工或內容，不在店內施壓當場評分。

**為什麼**：Google Maps 使用者貢獻內容政策「Fake engagement / Rating manipulation」禁止：付費或實物換評論、因折扣 / 免費商品而生的評論、以誘因要求修改或移除評論、不尋常的評論量或模式、利益衝突評論（員工、承包商、親屬、競爭者）、「阻止負評或選擇性徵求好評」、「要求員工徵求特定數量的評論」、「要求員工徵求含特定內容（含指認員工）的評論」、「在現場施壓使用者評分」；允許「徵求對真實經驗的評論，不提供誘因、不影響評分或內容」。員工配額與指定內容兩條為 2026-04-17 新增（來源：support.google.com/contributionpolicy/answer/7400114，查閱 2026-11-03）。另，自家網站對自己加 `LocalBusiness` 星等不符 rich result 資格，且 2026-07-24 起 review snippet 指南禁止假評論與未揭露誘因評論（詳見 06）。

### 6.2 合規的評論取得流程

**怎麼做**：用 GBP 評論短連結（`https://search.google.com/local/writereview?placeid=...`）；服務完成當下出示 QR code 或 24 小時內 email / 簡訊 / LINE 一次；合規文案：「歡迎在 Google 分享您的真實體驗，無論好壞都能幫助我們進步：{連結}」，禁止「留 5 星送飲料」「滿意再留」「請提到 Amy」；不用「滿意才導到 Google」的 gating 工具；節奏求穩定（持續流入第 14、新鮮度第 11）；鼓勵文字與照片但不指定內容。

**驗收方式**：每月新評論穩定（實務基準：餐飲 / 零售 ≥ 10 則、專業服務 ≥ 3 則）；評分 ≥ 4.3；無「評論暫停」警告。

### 6.3 回覆規範

**規範**：100% 回覆、48 小時內、個人化；負評用「感謝 → 致歉 / 說明 → 解決方案 → 線下聯絡」四段式；不洩露顧客個資（醫療、法律尤其）；不塞關鍵字 / 促銷。

**為什麼**：Google 官方將「回覆評論」列為改善本地排名的建議，「有幫助的回覆能讓商家脫穎而出」（來源：support.google.com/business/answer/7091，查閱 2026-11-03）。

**怎麼做**：模板但每則改寫；負評先查內部紀錄；違規評論檢舉 + 評論管理工具申請移除，同時公開理性回覆。驗收：「未回覆評論」= 0。

### 6.4 第三方評論平台

Google 原生評論對排名影響最大，但「評論所在第三方網站的權威」是 Whitespark 2026 AI 可見度第 5 因素；各產業同步經營 1–2 個主要平台。第三方評論不可搬到自家 schema 充當 `aggregateRating`（詳見 06）。

---

## 7. 本地關鍵字與落地頁架構

### 7.1 本地關鍵字的三種形態

| 形態 | 範例 | 排名載體 |
|---|---|---|
| 顯性地理詞 | 「台北 植牙」「dentist in Makati」 | 落地頁 + GBP |
| 隱性本地意圖 | 「植牙」「near me」 | GBP（地圖包）為主 |
| 服務 + 鄰里 / 地標 | 「信義區 植牙」「BGC dentist」 | 據點頁內段落（不為每個鄰里建薄頁） |

關鍵字研究詳見 02；本地特有來源：GBP Performance「搜尋字詞」、GSC 含城市名的查詢、網格掃描找出掉出前 3 的鄰里。多語市場以 GSC 實際查詢語言決定頁面語言（hreflang 詳見 10）。

### 7.2 單據點網站的落地頁架構

**規範**：首頁 = 品牌 + 主服務 + 城市；每項核心服務一頁（`/services/{service}/`）；「聯絡 / 據點」頁含 NAP、地圖、營業時間、交通、照片；服務頁內嵌「服務區域」段落。

**為什麼**：「每項服務有專屬頁面」是 Whitespark 2026 AI 可見度第 2 因素、「內容的城市 / 鄰里相關性」第 6；一頁塞所有服務會稀釋相關性。

### 7.3 多據點 / 多服務區域架構

**規範**：
- 多據點（實體店）：`/locations/` 總覽 → `/locations/{city}-{area}/` 據點頁（每頁獨特：NAP、時間、該店照片 / 團隊 / 評論摘錄 / 服務差異 / 交通 / FAQ）→ 據點 × 服務頁只在服務確實因據點不同、且有搜尋量與獨特內容時建立。
- 多服務區域（SAB）：「服務區域」總覽頁 + 主要城市各一頁（≥ 60% 內容獨特：該城市案例、當地法規 / 氣候 / 建築型態、該區評論、抵達時間）；小鄉鎮在總覽頁以段落涵蓋，不建獨立頁。
- GBP 每據點一檔案，網站 URL 填各自據點頁；`LocalBusiness` schema 各自獨立含 `@id`。

**為什麼**：城市名替換的大量薄頁會被視為 doorway pages（詳見 07）；內容真實獨特的據點頁才同時滿足相關性與距離。

**怎麼做**（據點頁最低規格）：H1 `{品牌} {城市}`；首屏文字 NAP、「規劃路線」、`tel:`、與 GBP 同步的時間；300–800 字獨特內容 + ≥ 3 張實拍；地圖 embed 延遲載入；3–5 則該店評論摘錄（不加 `aggregateRating`）；內部連結總覽 ↔ 據點 ↔ 服務 ↔ 相鄰據點。

**驗收方式**：Screaming Frog 據點頁相似度 < 70%；GSC 各據點頁城市查詢曝光；Local Falcon 各據點 ARP。

**常見錯誤**：同一文案替換城市名生成 50 頁；據點頁放總公司電話。

---

## 8. LocalBusiness 結構化資料要點

語法詳見 06；本地 SEO 的決策：
1. 用最具體子類型（`Dentist`、`Plumber`、`Restaurant`），無適合子型別就用 `LocalBusiness`；需要多重類型時用 `@type` 陣列，Google 不支援 `additionalType`（來源：https://developers.google.com/search/docs/appearance/structured-data/local-business ，查閱 2026-11-03）。
2. Google 必要屬性只有 `name` 與 `address`；`@id`、`url`、`telephone`（E.164）、`geo`、`image`、`openingHoursSpecification` 等為建議屬性，本地 SEO 專案一律補齊（來源：https://developers.google.com/search/docs/appearance/structured-data/local-business ，查閱 2026-11-03）；多據點每頁一個，`@id` 為該據點頁 URL。
3. 不自行加 `aggregateRating` / `review`：`LocalBusiness`／`Organization` 上的自我服務評論（商家自己放在自己頁面的評論）不具 review snippet 資格，Google 會直接不顯示；單純因此不會有 manual action，造假評論則另屬違規（來源：https://developers.google.com/search/blog/2019/09/making-review-rich-results-more-helpful ，查閱 2026-11-03）。
4. `sameAs` 列 GBP Place 連結、Facebook、Apple Maps；SAB 用 `areaServed`；`hasMap` 連 Google Maps。
5. 名稱、地址、電話、時間與 GBP 逐字一致。

驗收：Rich Results Test 無錯誤；GSC 無 LocalBusiness 警告。

---

## 9. 本地連結與社群

**規範**：每季至少 3–5 個在地相關連結或提及（含無連結的品牌 + 地址提及）；來源為地方媒體、商會、贊助、社區活動、在地部落客、合作商家；通則詳見 16。

**為什麼**：Google 的 prominence 定義包含「連結到該商家的網站數量」；Whitespark 2026 AI 可見度前五有三項與引用 / 提及相關（「mentions are the new link」）。

**怎麼做**：贊助在地球隊、校園活動、路跑（附贊助商頁連結）；對地方新聞提供專家觀點；與鄰近非競爭商家互設「推薦夥伴」頁；在地 Facebook 社團 / LINE 社群（東南亞以 Facebook 群組為主）提供真實價值而非廣告；爭取進入「{城市} 最佳 {服務}」編輯精選清單（AI 可見度第 1 因素）；社群訊號只需 NAP 一致、連到據點頁、定期更新，不刷互動。

**驗收方式**：反向連結中在地網域比例上升；搜尋「"品牌名" + 城市」的提及數。

---

## 10. Apple Business Connect 與 Bing Places

### 10.1 Apple Business Connect

**規範**：所有商家在 Apple Business Connect（2023-01 推出，現屬 Apple Business 平台）認領並完善名稱、類別、NAP、時間、照片、Showcase（可放優惠 / 季節商品）、預約 / 訂位按鈕。

**為什麼**：Apple Maps 是 iOS 預設地圖，Siri、Spotlight、Safari、Wallet 皆用其資料；2026 年 Apple 於美加推出 Apple Maps 付費廣告（Suggested Places、搜尋結果頂部；來源：第三方 2026 報導與 ads.apple.com/maps，查閱 2026-11-03）。iOS 市占高的市場（台灣、新加坡）尤其重要。

**怎麼做**：登入 businessconnect.apple.com → 搜尋並認領（電話或文件驗證）→ 填寫；多據點用 CSV 批次匯入；Showcase 每月更新。Apple Maps 評分來自 Yelp（部分地區）與內建評分，無法像 GBP 直接管理評論。驗收：Apple Maps 顯示「已驗證」與 Showcase。

### 10.2 Bing Places for Business

**規範**：用「從 GBP 匯入」建立並開啟定期同步；匯入後檢查 Import Summary 的缺漏屬性與重複檔案。

**為什麼**：Microsoft 2025-10 推出新版 Bing Places（bing.com/forbusiness）並改良匯入工具（來源：blogs.bing.com，查閱 2026-11-03）；Bing 資料供 Copilot、Windows 搜尋、Yahoo、DuckDuckGo（部分）使用。

**怎麼做**：Bing Places → Import from Google → 授權 → 選據點 → 設同步週期；已驗證的 GBP 通常可自動完成 Bing 驗證（第三方估發布 7–12 天）。常見錯誤：匯入後從未再登入，同步失敗不會主動通知。

### 10.3 其他平台（依市場）

東南亞：Grab、Foodpanda、Waze for Brands、Facebook Page（印尼 / 越南使用率高）；台灣：Google 主導，兼顧 Facebook、LINE 官方帳號。

---

## 11. 地圖包（Local Pack）追蹤工具

**規範**：用「網格式（geo-grid）」追蹤而非單點排名；核心關鍵字每 2 週掃 7×7 或 9×9 網格，間距依城市密度 0.5–2 km。距離是第 2 大因素，同城市不同位置的排名可差 1 → 20 名。

| 工具 | 用途 |
|---|---|
| Local Falcon | 網格掃描、競爭者比較、Share of Local Voice；最常用 |
| BrightLocal Local Search Grid + Citation Tracker | 網格 + 引用審核 + 評論監控，代理商整合型 |
| Whitespark Local Rank Tracker / Local Citation Finder | 排名 + 本地 SERP 特徵 + 引用 |
| Semrush Map Rank Tracker / Listing Management | 熱點圖 + 多平台目錄同步 |
| GMB Everywhere、PlePer | 免費診斷：競爭者類別、評論審核、類別研究 |
| GBP Performance（官方） | 曝光、搜尋字詞、通話、路線、網站點擊；唯一第一方資料，僅保留 6 個月 |
| Google Search Console | 落地頁的含城市名查詢曝光與點擊 |

**驗收指標**：網格平均排名（ARP）、前 3 名覆蓋率、GBP 通話 / 路線 / 網站點擊月趨勢、新評論數與回覆率、引用一致率。

---

## 12. 狀況 → 解法表

| 症狀 | 可能原因 | 診斷步驟 | 解法 | 預防 |
|---|---|---|---|---|
| 檔案從地圖消失（硬停權） | 名稱塞字、地址違規、網站轉址他網域、重複檔案、近期大幅編輯 | 看 GBP 停權通知；逐項核對 3038177；查重複檔案 | 修正根因 → Appeals tool 一次附齊登記文件 + 帳單 + 店面照片；被拒再申請額外審核 | 重大編輯分批；高風險類別先備文件；不用代理商帳號當主要擁有者 |
| 排名大幅下滑但檔案正常 | 競爭者改類別、自家主要類別被 Google 自動調整、評論停滯、本地演算法更新 | Local Falcon 比較前後網格；檢查類別；評論趨勢；查 07 演算法時間軸 | 重選主要類別；重啟評論流程；補據點頁內容；檢查 NAP | 每月檢查類別與屬性；評論節奏穩定 |
| 只在店址附近 1 km 排名 | 正常距離效應 + 知名度不足 | 網格掃描看衰減半徑；比對競爭者評論 / 連結數 | 提升知名度（評論、在地連結、媒體提及）；落地頁加強鄰里內容；多據點才能擴大半徑 | 設定合理期望 |
| 名稱 / 類別被人改掉 | 使用者「建議編輯」被自動採納、競爭者惡意編輯 | GBP 通知中心「Google 更新」與編輯紀錄 | 改回並拒絕更新；提供招牌照片佐證 | 名稱與招牌、官網一致；開啟通知 email |
| 評論被大量移除 / 「評論暫停」 | 偵測到誘因、員工配額、同裝置評論、刷評；或誤判 | 檢查近期評論取得方式與活動 | 停止違規；真實評論被誤刪可透過評論管理工具申訴（成功率低） | 遵守 6.1；不用 gating 工具 |
| 1 星惡意 / 非顧客評論 | 競爭者、前員工、誤評 | 核對顧客紀錄；看評論者歷史 | 公開理性回覆 → 檢舉（利益衝突 / 非真實體驗）→ 評論管理工具追蹤；法律途徑最後 | 建立 SOP；不情緒回覆 |
| 多據點互搶排名或只出現一個 | 據點頁雷同、GBP 網站 URL 全填首頁、服務區域重疊、電話共用 | 比對據點頁相似度；檢查各據點網站欄位、服務區域、電話 | 每據點獨立 URL / 電話 / 內容；服務區域去重疊；schema 各自 `@id` | 7.3 規格 |
| Knowledge Panel 顯示舊地址 / 舊時間 | 引用不一致、Google 從舊目錄抓資料 | 引用掃描找舊資料來源；查 GBP「Google 更新」 | 更新 GBP → 修正主要引用 → Knowledge Panel「提供意見」回報 | NAP 主檔 + 季度引用審核 |
| 搬遷後排名歸零 | 地址變更觸發重新驗證；舊引用仍在 | 查 GBP 驗證狀態；引用掃描 | 完成影片驗證；更新引用；舊地址頁改「已搬遷」並 301 到新據點頁 | 搬遷前 1 個月備妥文件、影片、引用清單 |
| 影片驗證一再失敗 | 剪接、未拍門牌 / 招牌、SAB 未展示管理權證明 | 回看是否涵蓋位置、業務、管理權 | 重拍：一鏡到底，街景門牌 → 招牌 → 室內 → 管理權證明 | 建檔前先拍好 |
| 新檔案數週仍不出現 | 未驗證；審核中；同址已有同名檔案 | 搜尋商家名 + 地址；查 GBP 狀態 | 完成驗證；審核超過 7 天聯絡支援 | 建檔前先搜尋既存檔案改用認領 |
| 內容站想在「{城市} 最佳 XX」取得流量 | 競爭者是 Yelp / TripAdvisor 類大站 | 看 SERP 是否以地圖包 + 大站為主 | 真實走訪 + 獨家資料 + 可驗證作者；`ItemList` schema；在地連結 | 程序化風險詳見 11 |

---

## 13. 本章檢查清單

**GBP**
- [ ] 已驗證；名稱 = 招牌 = 官網 = 登記，無附加關鍵字
- [ ] 主要類別最具體；次要類別 ≤ 5
- [ ] 地址真實；SAB 隱藏地址、服務區域 ≤ 2 小時車程且無重疊；釘點在正門
- [ ] 電話據點直撥；網站 URL 為同網域據點頁並加 UTM；營業時間與假日已設
- [ ] 描述無促銷 / 價格 / CTA / 連結；屬性填滿；商品價格為固定價
- [ ] 照片 ≥ 20 張實拍且每月新增；每週 1 則貼文；Q&A（若後台仍可用）自建 5–10 題；預約連結已設

**評論**
- [ ] 邀請流程無誘因、無篩選、無員工配額、無指定內容
- [ ] 100% 回覆、48 小時內、個人化；違規評論有檢舉 SOP
- [ ] 網站未對自家商家加 `aggregateRating`

**網站與引用**
- [ ] 每項核心服務一頁；每據點一頁且內容獨特 ≥ 60%，首屏有 NAP、路線、`tel:`、營業時間
- [ ] 全站文字版 NAP 與 GBP 逐字一致；`LocalBusiness` 子類型 schema 每據點一個
- [ ] Apple Business Connect、Bing Places（含同步）、Facebook 已認領且 NAP 一致；季度引用一致率 ≥ 95%
- [ ] 每季 3–5 個在地連結 / 提及

**監測**
- [ ] 核心關鍵字每 2 週網格掃描，記錄 ARP 與前 3 覆蓋率
- [ ] GBP Performance 每月匯出；GBP 通知 email 開啟，監控「Google 更新」與編輯建議

---

## 14. 參考來源

- Google — How to improve your local ranking on Google：https://support.google.com/business/answer/7091（查閱 2026-11-03）
- Google — Guidelines for representing your business on Google：https://support.google.com/business/answer/3038177（查閱 2026-11-03）
- Google — Prohibited and restricted content（Business Profile，含 2026-10 Advertising & solicitation 更新）：https://support.google.com/business/answer/7400114（查閱 2026-11-03）
- Google — Maps user contributed content policy（Fake engagement / Rating manipulation，含 2026-04-17 員工配額條款）：https://support.google.com/contributionpolicy/answer/7400114（查閱 2026-11-03）
- Google — Appeal a suspended or disabled Business Profile：https://support.google.com/business/answer/4569145（查閱 2026-11-03）
- Google Search Central — Review snippet structured data（2026-07-24 新增假評論 / 未揭露誘因條款）：https://developers.google.com/search/docs/appearance/structured-data/review-snippet（查閱 2026-11-03）
- Whitespark — 2026 Local Search Ranking Factors（2025-11-06 發布）：https://whitespark.ca/local-search-ranking-factors（查閱 2026-11-03）
- Search Engine Roundtable — GBP policy update on promotions（2026-10-06）；Short names removed（2026-02）；Review policies updated（2026-04）；Video verification FAQs（2023）：https://www.seroundtable.com/（查閱 2026-11-03）
- Relevant Audience — GBP policy bans time-bound promotions and pricing in listings（2026-10-08）：https://www.relevantaudience.com/seo/google-business-profile-policy-bans-promotions-in-listings/（查閱 2026-11-03）
- Search Engine Land — GBP to stop allowing price ranges on products（2023-02）：https://searchengineland.com/google-business-profiles-to-stop-allowing-price-ranges-on-products-on-february-15-391244（查閱 2026-11-03）
- Microsoft Bing Blog — Introducing the New Bing Places for Business（2025-10）：https://blogs.bing.com/search/October-2025/Introducing-the-New-Bing-Places-for-Business-Built-for-Business-Owners,-Powered-by-Research（查閱 2026-11-03）
- Apple Business Connect：https://businessconnect.apple.com/；Apple Ads in Maps：https://ads.apple.com/maps（查閱 2026-11-03）
- Google Business Profile Help Community — A heads up about the upcoming changes to the Q&A feature（Google 員工 Dan Boguslavsky，2025-12-03；查閱 2026-11-03）：https://support.google.com/business/thread/392024106
- Google Business Profile Help Community — Q&A button missing（Gold 產品專家 Faris Abdulaziz，2025-12-05、12-08 編輯；「Ask about this place」；查閱 2026-11-03）：https://support.google.com/business/thread/392365178
- Search Engine Roundtable — Google Removing Q&A Feature In Google Maps For AI-Powered Ask Button（2025-12-15；轉述上述官方討論串）：https://www.seroundtable.com/google-maps-qa-feature-ask-40594.html（查閱 2026-11-03）
- 第三方報導（Chat / 通話紀錄 2024-07 停用、Q&A API 2025-11-03 停用）：TechRadar、Reputation.com、Engage Web（查閱 2026-11-03）
