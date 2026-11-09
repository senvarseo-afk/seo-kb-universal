# 23 Google Ads 廣告規範與問題排解

> 版本：1.0 ｜ 更新日期：2026-11-09 ｜ 適用：使用 Google Ads 推廣網站或幫客戶投放的專案 ｜ 撰寫：Claude

## 本章摘要

1. 本章是**廣告主端**（花錢買 Google Ads）；發布者端的 AdSense 與聯播網見 09 章與 22 章。帳號安全三條底線：廣告主驗證在期限內完成（期限不可延長，逾期暫停）、付款資料與驗證身分一致、被停權後**絕不開新帳號**（Circumventing systems，偵測即停權、不預警）。
2. 2026 年必知變動：Search 活動的語言設定 2026-09 移除；自動建立素材與活動層級廣泛比對的 Search 活動 2026-09 起自動升級 AI Max（DSA 延到 2027-02）；Enhanced conversions 合併為單一開關、離線轉換上傳 2026-06-15 起以 Data Manager API 為主（Google Ads API 不再接受新使用者）；帳戶內申訴只受理 6 個月內的決定；Limited ad serving 擴及所有 Google Ads；AI Mode 廣告 2026-10-28 擴及 10 國。
3. 台灣的賭博廣告只限國營 / 國家許可業者經認證投放，gambling-promoting content（聯盟與資訊彙整站）在台灣不在可投清單。台灣金融服務需驗證（2022-08-30 起）。
4. 投放地基是乾淨的轉換資料：Google tag + Enhanced conversions + 單一主要轉換目標；EEA / UK / 瑞士流量必須送 Consent Mode 訊號。Smart Bidding「Learning」狀態最長 7 天，評估看 2 個轉換週期或 2 週。
5. Google 官方明言廣告不影響自然排名；SEO 與付費的協同在資料（Search terms、Paid & organic report）與著陸頁。品牌字買不買，用暫停測試量增量。

## 目錄

1. [本章定位與範圍](#1-本章定位與範圍)
2. [帳號基礎](#2-帳號基礎)
3. [政策全覽](#3-政策全覽)
4. [審核與處置](#4-審核與處置)
5. [投放建議](#5-投放建議)
6. [SEO 與付費搜尋的協同](#6-seo-與付費搜尋的協同)
7. [Google Ads 狀況 → 解法（P1–P28）](#7-google-ads-狀況--解法p1p28)
8. [本章檢查清單](#8-本章檢查清單)
9. [參考來源](#9-參考來源)

---

## 1. 本章定位與範圍

| 主題 | 本章 | 其他章節 |
|---|---|---|
| 帳號、付款、驗證、政策、審核、停權 | 全部 | — |
| 轉換、出價、關鍵字、AI Max、PMax、Demand Gen、素材、地區語言、預算 | 全部 | GA4 事件定義見 13 §13.2 |
| Shopping / PMax 商品資料 | 只寫投放面 | 19 §9 Merchant Center |
| 著陸頁品質與速度 | 只寫與 Quality Score 的關係 | 05 §14、04 §11 |
| AdSense、無效流量（發布者端） | 只寫導流到 AdSense 頁的廣告主端規範 | 09 §8、22 章 |
| 聯盟揭露法規 | 不重寫 | 09 §9 |
| Meta、TikTok 與其他廣告平台 | 不寫 | 26 章 |

所有官方來源查閱日期：2026-11-04；2026-11-05 查證修正的項目以當日為準，§9 逐筆標註。

---

## 2. 帳號基礎

### 2.1 帳號結構（MCC、帳號、活動、廣告群組）

**規範**：一個事業（一個付款主體）一個帳號；代客戶投放用 Manager account（MCC）連結，**付款資料與管理員權限留在客戶名下**；活動依「目標 × 市場 × 語言」切，廣告群組依「單一意圖」切。

**為什麼**：Google 會連帶停權共用身分文件、付款資料或網站的相關帳號（https://support.google.com/adspolicy/answer/2375414 ）；連結到違規 MCC 的帳號可能被暫停（https://support.google.com/adspolicy/answer/9872152 ）；Unfair advantage 禁止在同一廣告位置為同一事業顯示多則廣告（https://support.google.com/adspolicy/answer/15936768 ）；Smart Bidding 官方建議整併活動集中資料（https://support.google.com/google-ads/answer/13020501 ）。

**怎麼做**：

```
MCC（代理商帳戶）
 ├─ 自有帳號 → SRCH｜TW｜ZH｜品牌、SRCH｜TW｜ZH｜非品牌｜主題、PMAX｜TW｜ZH
 └─ 客戶帳號（客戶付款、客戶為管理員）→ 活動 → 廣告群組（RSA × 2 + 關鍵字 + 資產）
```

命名固定為 `類型｜國家｜語言｜品牌 / 非品牌｜主題`；時區與幣別開戶時決定（開戶後無法修改，URL 待查證）；至少 2 位管理員並啟用兩步驟驗證；品牌與非品牌分活動（§6.2）。

**驗收方式**：存取權與安全性 ≥ 2 位管理員；客戶帳號付款抬頭 = 客戶法定名稱；同一網域只在一個帳號投放。

**常見錯誤**：用個人卡付客戶帳號（觸發 Suspicious payment activity）；同一網站兩個帳號同時投；一個活動混多國多語言。

### 2.2 付款設定

**規範**：帳單國家 = 付款主體所在國、幣別 = 主要付款工具幣別；設主要 + 備用付款方式；付款資料名稱、地址與驗證文件一致。

**為什麼**：可用付款方式依商家地址、幣別與付款設定（postpay / prepay、月結需申請）而定（https://support.google.com/google-ads/answer/2375375 ）；扣款失敗累積未付餘額會導致停權（§4.3）。付款驗證可用驗證碼（暫扣不超過 USD 1.95、30 天內退回）、付款或文件，路徑 管理 → 政策 → 帳戶 →「Complete Payment Verification」，只有管理員能做（https://support.google.com/google-ads/answer/13704200 ）。

**怎麼做**：

| 項目 | 台灣 |
|---|---|
| 幣別 | TWD |
| 付款方式 | 信用卡 / 簽帳卡；官方另列 7-Eleven 超商、中華郵政、匯款（皆為預付，僅限開戶時選擇，https://support.google.com/google-ads/answer/2375433 ）；實際選項以後台「帳單 → 付款方式」為準 |
| 建議 | 公司卡 + 備用卡；客戶帳號用客戶公司卡 |

**驗收方式**：首筆扣款成功；有 2 個有效付款方式。

**常見錯誤**：VPN 開戶；短期反覆換卡；用第三人卡片；對合法扣款申請退單（chargeback，帳戶可能被停權）。

### 2.3 廣告主驗證（Advertiser verification）

**規範**：收到通知當天開始、期限內完成；組織名稱、文件、付款資料三者逐字一致；驗證期間不改付款資料。

**為什麼**（https://support.google.com/adspolicy/answer/9703665 、https://support.google.com/adspolicy/answer/15588490 、https://support.google.com/adspolicy/answer/9872152 ）：
- 所有廣告主最終都要驗證；金融等產業、對品牌相關查詢出價、使用常被濫用功能、申訴停權者會被提早要求。
- 有期限的驗證**不能延長**，逾期帳號暫停，只能完成驗證才解除；審查最多 5 個工作天（無期限案件罕見到 30 天）。
- 常見失敗：名稱與文件不符、文件過期、業務類型宣告錯誤、未揭露業務關係、缺產業執照；變更付款資料法定名稱會立即觸發重新驗證。
- 驗證後名稱與所在地會公開在廣告揭露與 Ads Transparency Center。
- 停權申訴前可能須先完成驗證，驗證 3 次失敗不能申訴（https://support.google.com/adspolicy/answer/2375414 ）。

**怎麼做**：備妥公司登記文件（台灣商工登記，依通知要求）、負責人證件、與付款資料相同的地址證明；代客戶投放時以客戶名義驗證。台灣另注意：數位發展部 2024-09-16 依《詐欺犯罪危害防制條例》指定 Google LLC 為網路廣告平臺業者（PPC Land 2024-12-07 報導），條例要求平臺揭露委刊者與出資者；Google Ads 對台灣廣告主的具體欄位要求待查證，以帳戶通知為準。

**驗收方式**：驗證狀態「已完成」；Ads Transparency Center 顯示正確組織名稱與國家。

**常見錯誤**：拖到最後幾天；文件用簡稱、付款資料用全名；驗證中途改付款資料。

### 2.4 帳單與稅務

**規範**：統編 / TIN 第一次就填對；第一張月結單出來先核對稅額行與抬頭。

**為什麼**：
- **台灣**：Google Ads 有台灣專用帳單表單，處理電子統一發票（GUI）問題（https://support.google.com/google-ads/contact/billing_tw ）；Google Play 官方載明台灣收 5% 營業稅並開電子發票（https://support.google.com/paymentscenter/answer/9251135 ），但 **Google Ads 是否一律加收 5% 與發票開立主體未見官方說明（待查證）**。

**怎麼做**：帳單 → 設定填統編 / TIN；台灣發票問題走 billing_tw 表單。

**常見錯誤**：帳單國家填錯導致無法開當地發票；代客戶付費再請款，稅務主體混亂。

---

## 3. 政策全覽

### 3.1 政策架構與執行方式

| 類別 | 內容 | 一般後果 | 嚴重違規後果 |
|---|---|---|---|
| Prohibited content | 仿冒品、危險產品、助長不誠實行為、不當內容 | 拒登；重複違規停權 | 仿冒品、兒少性剝削：偵測即停權 |
| Prohibited practices | Abusing the ad network、資料收集、Misrepresentation | 拒登；停權前至少 7 天警告 | Circumventing systems、Unacceptable business practices、Coordinated deceptive practices、惡意軟體：偵測即停權 |
| Restricted content and features | 賭博、金融、醫療、酒精、政治、商標、加密貨幣 | Eligible (limited) 或需認證 | 未認證投放賭博可能被禁投或停權 |
| Editorial and technical | 編輯、到達網頁、技術、格式 | 拒登；停權前至少 7 天警告 | 編輯問題不會被判 Circumventing systems |

來源：https://support.google.com/adspolicy/answer/6008942 、https://support.google.com/adspolicy/answer/2375414 。部分政策另走三振制度（§4.4）。

### 3.2 Prohibited content

**規範**：不投仿冒品、危險產品或服務、助長不誠實行為（駭客工具、偽造文件、代考、間諜軟體）。助長不誠實行為屬三振政策；兒少性剝削政策 2027-01 改為獨立 Child Safety 政策（https://support.google.com/adspolicy/answer/18797274 ）。接案前用 §8.1 清單過濾產品類別。

### 3.3 Prohibited practices

**Abusing the ad network 七個子政策**（https://support.google.com/adspolicy/answer/6020954 ）：

| 子政策 | 內容 | 專案風險點 |
|---|---|---|
| Malicious software / Compromised sites / Unwanted software | 惡意軟體、被駭頁、未揭露的軟體行為 | 網站被駭（先依 12 D7 清理） |
| Unfair advantage | 同一廣告位置多則自家廣告；聯盟違反聯盟計畫規則投放 | 多帳號、多網域投同一品牌 |
| Evasive ad content | 操弄文字、圖片、網域以規避偵測 | 被拒後換字形或子網域重送 |
| Circumventing systems | Cloaking、停權後開新帳號、多帳號散布違規、驗證造假、賭博認證重大變更未重申 | 最常見的永久停權原因 |
| Spam policies for Google Web Search | 違反搜尋垃圾政策 | 到達頁本身是 doorway、scaled content（07 §4） |

Circumventing systems 依地點或連線速度顯示不同語言 / 內容是允許的（產品相同即可）；違規「偵測即停權、不預警，且不得再用 Google Ads」，只在有說服力的情況（如誤判）恢復（https://support.google.com/adspolicy/answer/15938075 ）。

**Misrepresentation 十個子類**（https://support.google.com/adspolicy/answer/6020955 ）：Unacceptable business practices 與 Coordinated deceptive practices 為嚴重違規（偵測即停權）；Clickbait、Misleading ad design 屬三振政策；其餘為 Misleading representation、Dishonest pricing practices、Manipulated media、Unreliable claims、Unclear relevance、Unavailable offers。

**怎麼做**：廣告中的每個價格、折扣、「免費」、「保證」都要在到達頁首屏找得到；不冒充官方。

### 3.4 Restricted content and features

#### 3.4.1 賭博與遊戲（Gambling and games）

**規範**：賭博或宣傳賭博的廣告 = 目標國在允許清單 + 取得 Google 認證 + 到達頁符合負責任博弈要求 + 不鎖定未成年人。

**為什麼**（https://support.google.com/adspolicy/answer/6018017 ）：

| 項目 | 台灣 |
|---|---|
| 可投線上賭博產品 | State-run / State-hosted lotteries |
| 業者條件 | 「state approved entity」 |
| Gambling-promoting content（聯盟 / 彙整站） | 不在清單 → 不得投放 |
| 實體賭場等 offline gambling | 禁止 |
| Social casino | Group 2 |

官方原則：「未列出 online gambling-promoting content 的國家，不得投放」；目前允許的是阿根廷、哥倫比亞、丹麥、法國、希臘、愛爾蘭、肯亞、墨西哥、莫三比克、秘魯、葡萄牙、羅馬尼亞、塞爾維亞、烏克蘭、英國（北愛爾蘭除外）、美國。2026-08-26 起新版認證表單：每個目標地區要有效當地執照、到達頁需年齡警示、成癮資源、條款與含執照號碼的頁尾、每國分開申請、重大變更須重新認證（https://support.google.com/adspolicy/answer/17258294 ）。

#### 3.4.3 金融服務驗證

台灣自 2022-08-30 起需金融服務驗證，主管機關含金管會、財政部與保險經紀 / 代理公會；東南亞在清單的含新加坡（2022-08-30）、印尼（2023-01-24）、馬來西亞（2026-04-14）（https://support.google.com/adspolicy/answer/12390454 ）。2026-06-23 公告新增 24 個 EEA 市場（2026-07-23 起分批），只有 First Party 或 Authorized Advertisers 能申請，沒有監管授權的推廣者（Approved Third Party Advertisers）須由前兩者代為申請（https://support.google.com/adspolicy/answer/17127726 ）。Personal loans、Binary options、Credit repair 屬三振政策。**實務意義**：台灣信用卡 / 貸款比較站投放前，先確認商家能否代為申請；拿不到就不投台灣金融字。

#### 3.4.4 加密貨幣、醫療、酒精、政治

| 類別 | 台灣 | 來源 |
|---|---|---|
| 加密貨幣交易所 / 錢包 | 是否允許待查證 | https://support.google.com/adspolicy/answer/14009787 |
| 醫療與藥品 | 處方藥、線上藥局依國家需認證，細節待查證 | https://support.google.com/adspolicy/answer/176031 |
| 酒精 | 2026-07-28 擴大的 29 國不含 TW，現行規定待查證 | https://support.google.com/adspolicy/answer/17230661 |
| 政治 | 禁止以政黨、現任民選公職、各級候選人為內容的廣告 | https://support.google.com/adspolicy/answer/6014595 |

**遠距醫療（2026-11-04 公告）**：Google 將於 2026-11 更新加拿大、英國、美國的醫療政策：通過美國藥事委員會聯合會（NABP）Healthcare Merchant Accreditation Program 認證的遠距醫療廣告主，可申請 Google Ads 遠距醫療認證，原有認證途徑保留。須先取得 NABP 認證，NABP 認證也不等於 Google 核准；申請要等政策頁更新後才開放。不涉及台灣（https://support.google.com/adspolicy/answer/18794834 ，查閱 2026-11-08）。

### 3.5 Editorial and technical 與 Destination requirements

#### 3.5.1 編輯規範

**規範**（https://support.google.com/adspolicy/answer/6021546 ）：標點符號依原本用途、不用不支援字元；大寫正確；拼字文法通順；不做噱頭式重複；寫明推廣對象；商家名稱欄不放促銷語；**廣告文字不得放電話號碼**（改用通話素材）；圖片清楚。2026-10 起商家名稱在有限情況可與網域不同，但**聯盟分銷者不適用**，也不得用所售品牌當商家名稱（https://support.google.com/adspolicy/answer/18287059 ）。繁中 RSA 以雙寬字元計：標題 30 字元 = 15 個中文字、說明 90 字元 = 45 個中文字（https://support.google.com/google-ads/answer/7684791 ）。

**常見錯誤**：「★★★」「↗」當裝飾；文案全大寫加「FREE!!!」；商家名稱寫「XX 官方」。

#### 3.5.2 Destination requirements

違規停權前至少 7 天警告（https://support.google.com/adspolicy/answer/6368661 ）：

| 子政策 | 意思 | 修正重點 |
|---|---|---|
| Destination not working | 對 AdsBot 回 4xx、5xx、DNS 錯誤、轉址迴圈、逾時、需登入；「Under Construction」頁 | 常見裝置回 200；用 DevTools 把 UA 改 AdsBot 測（https://support.google.com/adspolicy/answer/16428019 ） |
| Destination mismatch | 顯示網址與最終網址網域不符、轉到其他網域、追蹤網址內容不同 | 同網域；2026-06-23 公告、2026-07 初生效：跨網域轉址僅限特定情況並須事先核准（例：消費品製造商導預先核准的零售商，https://support.google.com/adspolicy/answer/17140995 ） |
| Destination not crawlable | Google Ads 爬不到 | robots.txt 不點名封鎖 AdsBot-Google / AdsBot-Google-Mobile（兩者忽略 `*`） |
| Destination not accessible | 目標地區打不開 | 檢查 Cloudflare / SiteGround 地區封鎖與挑戰頁 |
| Destination experience | 難導覽、直接下載、濫用體驗、違反 Better Ads Standards | 移除彈窗與自動下載（09 §7） |
| Insufficient original content | 主要為展示廣告的頁、無增值複製內容、只轉向他處的 bridge / doorway 頁、停車網域 | 補原創內容、減廣告（https://support.google.com/adspolicy/answer/16427718 ） |
| Unacceptable URL / Unrecognized app | 格式錯誤網址、IP 當顯示網址、無法辨識的 App | 用正式網域與商店連結 |
| Unverified / Unacceptable phone number | 未驗證、付費、虛擬、非目標國、無語音信箱的號碼 | 用當地可接通號碼並驗證 |

**驗收方式**：每個最終網址 `curl -A "AdsBot-Google (+http://www.google.com/adsbot.html)" -I` 回 200；美國與目標國都能開。

### 3.6 商標政策

Google **不限制把商標當關鍵字**，限制的是**廣告文字**使用商標，通常在商標權人投訴後執行；經銷商（到達頁可購買、有價格、看得出是經銷商）、資訊站、描述性使用不受限；投訴只對特定廣告主、只在權利人證明有權利的國家與產業生效；違規停權前至少 7 天警告（https://support.google.com/adspolicy/answer/6118 ）。**Google 允許不等於聯盟商家允許**：多數聯盟合約限制品牌字競價，違反屬 Unfair advantage 並可能被追回佣金。

### 3.7 聯盟行銷投放規範

**規範**：只導到**自有網域、有原創價值的內容頁**；不把最終網址設成商家連結或只有按鈕的 bridge page；遵守聯盟合約的付費搜尋條款；商家名稱用自有品牌。

**為什麼**：bridge / doorway 頁屬 Insufficient original content；轉到商家網域屬 Destination mismatch；違反聯盟計畫規則屬 Unfair advantage；聯盟分銷者不得用所售品牌當商家名稱（§3.5.1）；Limited ad serving 會限制引用其他品牌或無品牌廣告的曝光，官方建議品牌清楚、標題放網域（https://support.google.com/adspolicy/answer/17122370 ）。揭露見 09 §9。

**怎麼做**：到達頁有自寫比較表、實測、優缺點，揭露在第一個聯盟連結前；標題 1 放自有品牌或網域；主打品類與比較意圖字（best、vs、review、推薦）；主要轉換用聯盟後台訂單離線匯入（§5.1）。

**驗收方式**：拿掉聯盟按鈕後頁面仍完整；最終網址網域 = 顯示網址網域；聯盟合約付費搜尋條款已存檔。

**常見錯誤**：Shopee / Lazada 短連結當最終網址；整頁三行字加按鈕；競價商家品牌字被追回佣金。

### 3.8 用 Google Ads 導流量到 AdSense 頁面（發布者端詳見 22 章）

**規範**：買流量導到放 AdSense 的頁面，到達頁必須以原創內容為主、廣告不壓過內容；不做「買低價點擊、賺高價展示」的套利頁。

**為什麼**：廣告主端，主要為展示廣告而建的頁屬 Insufficient original content；發布者端，付費流量不違規，但無效流量、意外點擊是帳號層級風險（09 §8）。兩端都由 Google 判讀，一端出事常牽動另一端。

**怎麼做**：付費流量頁不放滿版或黏著廣告；GA4 用 UTM 分開看付費流量的 AdSense Page CTR；異常就暫停活動。**發布者端的風險、監控與停權處理詳見 22 章；其他廣告平台對這類頁面的限制見 26 §2.1。**

### 3.9 Policy change log：2025–2026 重要變動

來源：2026 年頁面 https://support.google.com/adspolicy/topic/16794025 、2025 年頁面 https://support.google.com/adspolicy/topic/16083443 、含 2025 年初條目的 2024 年頁面 https://support.google.com/adspolicy/topic/16090031 ；條目網址為 `support.google.com/adspolicy/answer/[ID]`。

| 時間 | 變動 | ID / 來源 |
|---|---|---|
| 2025-01 | 金融產品、醫療、Customer Match 政策更新 | 15709802、15322474、15532497 |
| 2025-03 | 新增 Dating and Companionship 政策與認證 | 15327789 |
| 2025-07 | 政治內容與選舉廣告驗證頁更新 | 16289331 |
| 2025-10-22 | 政府文件服務適用的 Search 廣告由 Google 自動加「Not a government website」揭露（2025-09-22 公告，約四週逐步全面執行，已認證為政府提供者者除外） | 16561193 |
| 2025-10-28 | Dishonest pricing practices 更新（2025-09-23 公告，約四週逐步全面執行） | 16502634 |
| 2026-01-26 | 「新增 RSA」建議不再自動套用 | google-ads/answer/10279006 |
| 2026-03 | 淘汰部分舊廣告格式規定 | 16971215 |
| 2026-06 | 跨網域轉址經事先核准可允許（2026-07 初生效） | 17140995 |
| 2026-06、2026-08 | Limited ad serving 新增 Search 段落並擴及所有 Google Ads，2028 年前完成 | 17122370、17344822 |
| 2026-06-23 | 24 個 EEA 市場新增金融服務驗證 | 17127726 |
| 2026-07-09 | 圖片與影片可加 AI 生成標示，不算違反文字疊加規定 | 17257106 |
| 2026-07-21 | 帳戶內申訴只限 6 個月內的政策決定 | 17251522 |
| 2026-08-26 | 賭博認證新版申請表 | 17258294 |
| 2026-09-30 | Destination not working 說明頁增加範例，不改變執法 | 18631563 |
| 2026-10 | 商家名稱例外（聯盟不適用）；預測市場、加密貨幣、金融產品、YouTube Masthead 更新 | 18287059、18712810、18785604、18546412、18429295 |
| 2026-11-19 | 線上賭博認證申請改由 Google Ads 帳戶提交，Help Center 表單停用（https://support.google.com/adspolicy/answer/15132179 ，查閱 2026-11-05） | 15132179 |
| 2027-01 | CSAE 改為獨立 Child Safety 政策 | 18797274 |

產品面變動（AI Max、語言設定、Enhanced conversions、Smart Bidding、AI Mode）見 §5。

---

## 4. 審核與處置

### 4.1 審核狀態

| 狀態 | 意思 | 會不會曝光 | 下一步 |
|---|---|---|---|
| Under review | 審查中 | 不會 | 等待；修改後重審通常 24–48 小時（https://support.google.com/adspolicy/answer/15936768 ） |
| Eligible | 通過 | 會 | 正常 |
| Eligible (limited) | 因酒精、賭博、醫療、商標等限制部分地點、年齡或裝置 | 部分 | 看「政策詳細資料」；誤判依拒登流程申訴（https://support.google.com/adspolicy/answer/2684542 ） |
| Disapproved | 違反政策 | 不會 | 修正後重審或申訴（§4.2） |

### 4.2 政策管理員（Policy manager）與申訴

**規範**：每週看 工具 → 政策管理員；先修正再申訴（「我已修改」或「爭議決定」）；一個帳號一個問題，不重複狂按。

**為什麼**：2026-07-21 起，超過 6 個月的政策決定不提供帳戶內直接申訴選項（https://support.google.com/adspolicy/answer/17251522 ）；停權則是自停權日起至少有 6 個月可申訴，兩者不能合併解讀成所有申訴一律 6 個月截止；停權申訴每個帳號分開提出，濫用申訴會被暫緩 7 天，被駁回可再申訴（https://support.google.com/adspolicy/answer/2375414 ）；暫停類申訴多數 5–7 個工作天（https://support.google.com/adspolicy/answer/9872152 ）。

**怎麼做**：拒登 → 讀原因 → 修廣告或到達頁 → 申訴「我已修改」；誤判 → 「爭議決定」附一句具體說明；停權 → 通知中「Contact Us」，先完成被要求的驗證，寫「原因 → 已採取措施 → 預防」並附證據。

**常見錯誤**：不修就申訴；停權後同時開新帳號，使原帳號失去恢復可能。

### 4.3 帳號停用的種類

| 類型 | 觸發 | 預警 | 處理 |
|---|---|---|---|
| Circumventing systems | Cloaking、停權後開新帳號、多帳號、驗證造假 | 無 | 申訴，只在誤判等情況恢復（15938075） |
| Unacceptable business practices | 詐騙、冒充、無法交付 | 無 | 同上（6020955） |
| Suspicious payment activity | 可疑或未授權付款 | 可能先限制支出 | 30 天內驗證付款方式後審查（google-ads/answer/13704200） |
| Unpaid balance | 未付餘額、扣款被拒 | — | 付清、修正付款方式（同上） |
| Chargeback / Promotional code abuse | 對合法帳款退單、販售或重複使用優惠碼 | — | 預防為主（同上） |
| 重複違規 | 同一政策多次違規 | 至少 7 天警告 | 修正並申訴（2375414） |
| 暫停（paused） | 未完成驗證、業務運作驗證、暫時調查、MCC 違規 | — | 完成驗證或表單、等候、解除 MCC 連結（9872152） |

被停權者新開的帳號也可能被停權，官方建議先恢復原帳號；符合資格者可取消帳號申請退款（2375414）。

### 4.4 三振制度（Strike system）

適用政策：Enabling dishonest behavior、Unapproved substances、Guns、Explosives、Other weapons、Tobacco、Compensated sexual acts、Mail-order brides、Clickbait、Misleading ad design、Bail bond services、Call directories、Credit repair services、Binary options、Personal loans（https://support.google.com/adspolicy/answer/10922738 ）。

| 階段 | 觸發 | 後果 |
|---|---|---|
| 警告 | 首次違反 | 不暫停 |
| 第 1 振 | 警告後再違反同一政策 | 暫停 3 天 |
| 第 2 振 | 第 1 振後 90 天內再犯 | 暫停 7 天 |
| 第 3 振 | 第 2 振後 90 天內再犯 | 停權 |

修正全部違規並送確認表單即依天數恢復；振數保留 90 天，申訴成功則移除（https://support.google.com/adspolicy/answer/10908668 ）。第 3 振造成的帳戶停權須申訴成功才解除，不會等 90 天自動恢復。最需注意 Demand Gen / Display 圖片的 Clickbait 與 Misleading ad design。

---

## 5. 投放建議

### 5.1 轉換追蹤（Google tag、GA4 匯入、Enhanced conversions、Consent Mode v2、離線轉換）

**規範**：每個帳號的出價集中在 **1 個一致的主要轉換目標**（conversion goal），目標內只放同一商業結果的主要轉換動作，其餘動作設次要；網站轉換用 Google tag（或 GTM）+ Enhanced conversions；EEA / UK / 瑞士流量必須送 Consent Mode 或 TCF 訊號；聯盟訂單、電話成交用離線轉換經 Data Manager 匯入。

**為什麼**：
- Smart Bidding 官方最佳做法是單一一致的主要轉換目標（13020501）；目標（conversion goal）不等於動作（conversion action），一個目標由相關的轉換動作組成，官方未限定只能有一個主要動作（https://support.google.com/google-ads/answer/10995103 、https://support.google.com/google-ads/answer/11461796 ）。
- 2026-04 起 Google Ads 同時接受網站標記、Data Manager、API 的使用者提供資料；2026-06 起網站與潛在客戶 Enhanced conversions 合併為單一開關（目標 → 設定 →「客戶資料使用」，需同意資料處理條款）；2026-06-15 起離線轉換匯入與潛在客戶上傳以 Data Manager API 為主，Google Ads API 不再接受新使用者（https://support.google.com/google-ads/answer/16884284 、https://ads-developers.googleblog.com/2026/05/changes-to-offline-click-conversion.html ）；這不是全面封鎖：2025-12-17 至 2026-06-15 未送出離線轉換上傳請求的 developer token 才受限，UploadClickConversions 回傳 CUSTOMER_NOT_ALLOWLISTED_FOR_THIS_FEATURE（https://developers.google.com/google-ads/api/docs/deprecations ；Help Center 寫的區間是 2026-01 至 2026-06，以開發者文件為準），developer token 2026-09-09 淘汰後此限制沿用；既有存取保留多久官方未寫，新流程一律走 Data Manager API；GCLID 型離線匯入官方稱為舊版功能（https://support.google.com/google-ads/answer/14274408 ）。
- Consent Mode：Basic 在同意前不載入標記、拒絕則不送任何資料；Advanced 先載入、拒絕時送無 cookie ping 並以廣告主專屬模型補值（需達門檻）；實作至少 7 個完整日後才可能累積足夠資料顯示 uplift，且須達最低資料門檻（https://support.google.com/google-ads/answer/10000067 ）。EU 使用者同意政策適用 EEA、UK、瑞士使用者（https://support.google.com/google-ads/answer/16724512 ）；台灣（個資法）依當地法規處理（律師確認）。
- Google tag gateway 讓標記經自家網域載入，2026 年起支援 Akamai 與 Google Cloud 部署（https://support.google.com/google-ads/answer/16214371 ；2026 整合為第三方報導）。

**怎麼做**：
1. 主要轉換只留商業結果（購買、合格名單、聯盟訂單）；`affiliate_click` 設次要。
2. GTM 轉換標記以交易 ID 去重；GA4 匯入的轉換設為次要，避免與 Google tag 雙算（13 §13.2）。
3. 開 Enhanced conversions；聯盟後台訂單每日經 Data Manager 匯入。
4. EEA / UK 流量：CMP + Consent Mode v2（範本見 15 章）。

**驗收方式**：轉換診斷「有效」；Tag Assistant 一次轉換只計一次；Consent Mode 實作滿 7 個完整日後檢查 uplift 報表（未達最低資料門檻時不顯示）。

**常見錯誤**：Google tag 與 GA4 匯入都設主要；頁面瀏覽當主要轉換；預設 denied 卻沒有 CMP update；新流程仍用 Ads API 舊路徑上傳離線轉換（無既有存取的 token 會回 CUSTOMER_NOT_ALLOWLISTED_FOR_THIS_FEATURE）。

### 5.2 出價策略與學習期

**規範**：新帳號先用「盡量爭取轉換」累積資料，穩定後加 tCPA；有可靠轉換價值才用 tROAS；同一轉換週期內不多次改目標。

**為什麼**（https://support.google.com/google-ads/answer/13020501 ，2026-10 改寫，Search Engine Roundtable 2026-10-21 報導）：「Learning」狀態**最長 7 天**，只由三件事觸發：新建或重啟出價策略、組成變更（增刪活動 / 廣告群組 / 關鍵字）、轉換目標大幅變更；改 CPA / ROAS 目標、預算、素材、地區受眾語言**不會**觸發，目標下一次競價就生效；成效通常 1–2 個轉換週期收斂，評估取「2 個轉換週期或 2 週」較長者；官方沒有最低轉換數門檻（「每月 50 次轉換」是第三方說法）。

**怎麼做**：用轉換延遲報表算轉換週期；新活動先跑 2–4 週無目標，再設 tCPA ≈ 過去 30 天實際 CPA × 1.0–1.2（經驗值）；每次只改一個變數並寫變更註解。

**常見錯誤**：一週內把 tCPA 改來改去；只有點擊類轉換就上 tROAS。

### 5.3 關鍵字比對類型與否定關鍵字

**規範**：品牌與核心字用完全比對；探索用詞組或廣泛比對（搭配 Smart Bidding）；每週從 Search terms 加否定字；建帳號層級否定清單。

**報表欄位（2026-11-04 Ads Liaison 說明）**：「Search terms match type (Keywords)」對應關鍵字分頁的區隔；「Search terms match type」對應搜尋字詞分頁的比對類型欄。目前 Report Editor 要同時加入「Search term」欄，後者才會列出包含 AI Max 在內的全部比對類型，Google 表示會修正（Search Engine Roundtable 轉載：https://www.seroundtable.com/google-ads-search-terms-match-type-keywords-42463.html）。

**為什麼**：完全比對含同義近似變體；**否定關鍵字不比對近似變體**，同義詞、單複數要自己列；大小寫與拼字錯誤系統自動處理，不必另加；帶重音符號的字算不同否定字（https://support.google.com/google-ads/answer/2453972 、https://support.google.com/google-ads/answer/7478529 ）。

**怎麼做**：否定分三層（帳號、活動、廣告群組）；目標市場有多種語言時同時列各語言變體；非品牌活動把品牌字設為否定。

**常見錯誤**：只加單一字形；否定詞擋到自己的主力字。

### 5.4 AI Max for Search

**規範**：先在非品牌、轉換足夠的活動用實驗測；開啟後設品牌控制、URL 排除與文字指引；需固定文案（法規、聯盟限制）的活動關閉最終網址擴展或文字自訂。

**為什麼**：AI Max 包含搜尋字詞比對（可在廣告群組關閉）、文字自訂、最終網址擴展（需文字自訂才能開）；最終網址擴展選了更相關網址時，**固定的 RSA 素材不會被使用**；可用 URL 排除 / 納入限制（https://support.google.com/google-ads/answer/15910187 ）。2026-04-15 Google 宣布 AI Max 結束 Beta；自動建立素材與活動層級廣泛比對的 Search 活動 **2026-09 起自動升級**；DSA 延到 **2027-02**；Google 內部資料稱全功能開啟比只開搜尋字詞比對平均多 7% 轉換或轉換價值（非零售廣告主）（https://blog.google/products/ads-commerce/dsa-upgrade-to-ai-max-2026/ ）。

**怎麼做**：實驗 50 / 50 跑 4 週；非品牌活動排除自家品牌；排除登入、標籤頁、薄頁網址；文字指引列禁用詞（「保證」「官方」「中獎」）；檢查活動是否已在 2026-09 被自動升級。

**常見錯誤**：沒發現已被自動升級；固定法規文案卻開著最終網址擴展；AI 文案寫出到達頁沒有的優惠（Unavailable offers）。

### 5.5 Performance Max

**規範**：PMax 用於有商品 feed 的電商或有明確轉換的名單客戶；一定設**品牌排除**、活動否定字、刊登位置排除；資產群組依產品線或受眾主題切；品牌字另開 Search 完全比對活動。

**為什麼**：含完全比對（或拼字修正後相同）關鍵字的 Search 活動優先於 PMax；搜尋主題與詞組、廣泛比對同優先；但 Search 活動受預算或較嚴目標限制時，PMax 仍可能出現在品牌查詢（https://support.google.com/google-ads/answer/10724817 、https://support.google.com/google-ads/answer/13810170 ）。PMax 活動否定字上限 2025-03 提高到每活動 10,000 個，只作用於 Search 與 Shopping 庫存（Search Engine Roundtable 報導 Google 公告）。

**怎麼做**：設定 → 品牌排除；每組資產群組素材完整；每週看搜尋字詞洞察與管道成效，加活動否定；最終網址擴展關閉或加 URL 排除；feed 規範依 19 §9。

**驗收方式**：PMax 品牌字花費占比 < 5%（經驗值）；低轉換管道花費受控。

**常見錯誤**：PMax 與品牌 Search 同開、未排除品牌，誤以為 PMax 很強；只放一張圖。

### 5.6 Demand Gen 與 YouTube

**規範**：Demand Gen 先用管道控制限縮在 YouTube 或 Discover 測試，再擴到 Gmail、Display；用轉換型出價。

**為什麼**：Video action campaigns 2025-04 起無法新建，剩餘活動 2026-04 前自動升級為 Demand Gen；Demand Gen 庫存含 YouTube、Discover、Gmail 與多媒體聯播網（https://support.google.com/google-ads/answer/15110871 ）；YouTube 與 Discover 廣告規定 2026-08 更新（https://support.google.com/adspolicy/answer/17455694 ）。圖片素材最容易觸發 Clickbait / Misleading ad design 三振。

**常見錯誤**：「系統警告」「點這裡領獎」風格圖片；用 Demand Gen 低價流量導到 AdSense 頁（§3.8）。

### 5.7 Shopping

Shopping / PMax 的商品資料、feed 屬性與 Merchant Center 診斷以 **19 §9** 為準。投放面：連結 Merchant Center 與 Google Ads；用購買價值當轉換；用 `custom_label_0` 依利潤分組；Standard Shopping 做精細控制、PMax 做擴量；每週看 Merchant Center 診斷。

### 5.8 廣告素材（RSA、資產、廣告強度）

**規範**：每個廣告群組 ≥ 2 則 RSA、廣告強度「良好」以上；標題 15 則、說明 4 則且彼此不同；少用固定位置；帳號、活動、廣告群組合計 ≥ 6 個網站連結。

**為什麼**：RSA 標題 3–15 則（30 字元）、說明 2–4 則（90 字元），雙寬字元算 2；固定到標題 1、2 或說明 1 的素材一定顯示但減少組合（https://support.google.com/google-ads/answer/7684791 ）。**廣告強度不直接影響放送資格，也不用於 Ad Rank 與 Quality Score**（https://support.google.com/google-ads/answer/9921843 ）。

**怎麼做**：15 則標題 = 3 則關鍵字 + 3 則品牌 / 網域 + 3 則利益點 + 3 則證據 + 3 則行動；繁中每則 ≤ 15 字；不同語言分組（§5.10）；每月依素材報表的完整成效指標替換表現差的標題（Performance label 已淘汰，完整統計支援 2025-06-05 起的資料；這與廣告整體的 Ad Strength 不同，https://support.google.com/google-ads/answer/9564897 ）。

### 5.9 Quality Score 與著陸頁體驗

**規範**：用 Quality Score 三元件（預期點閱率、廣告相關性、著陸頁體驗）找問題，不把分數當 KPI；著陸頁體驗低時套用 05 §14 評分表與 04 §11 Core Web Vitals。

**為什麼**：Quality Score 1–10 分是關鍵字層級診斷工具，**不是競價輸入值**（https://support.google.com/google-ads/answer/6167118 ）。著陸頁體驗看相關、原創、易導覽、行動版、速度，和 SEO 頁面品質高度重疊；一頁同時服務兩邊時，改一次兩邊受益。

**怎麼做**：加 Quality Score 與三元件欄位；著陸頁「低於平均」先查 LCP / INP / CLS 與首屏是否回答廣告承諾；廣告相關性低就拆細廣告群組。

**常見錯誤**：為分數做只給廣告看的薄頁；所有關鍵字導到首頁。

### 5.10 地區與語言設定

**規範**：地區選項用 Presence（位於目標地區的人），除非是旅遊、不動產、教育；2026-09 後 Search 沒有語言設定可選，**用文案與到達頁的語言決定配對**：一個廣告群組一種語言。

**為什麼**：地區預設是 Presence or interest（https://support.google.com/google-ads/answer/1722038 ）。2026-09 起 Search 活動的活動層級語言設定移除，依廣告本身語言比對；PMax 的語言設定不再套用於 Search 聯播網（其他管道與 PMax 內的 Shopping 不受影響）；Display、YouTube 不變；Google 用搜尋字詞語言與使用者語言設定判斷使用者懂哪些語言；Google 不翻譯廣告（https://support.google.com/google-ads/answer/1722078 ）。

**怎麼做**：台灣繁中文案配繁中頁，用 Search terms 檢查簡中查詢；混語文案的判定方式官方未說明（待查證，先以報表驗證）；多語言網址與 hreflang 依 10 章。

**常見錯誤**：以為「語言 = 英文」還能擋其他語言查詢；台灣活動用 Presence or interest，港陸流量進來。

### 5.11 預算與小預算帳戶

**規範**：小預算（經驗分級：每日 USD 10–30 / TWD 300–1,000）只開 1–2 個 Search 活動、集中最高意圖字；不開 Display / Demand Gen；不讓 PMax 與 Search 搶同一批查詢。

**為什麼**：單日可能花到平均每日預算 2 倍，但每月收費不超過平均每日預算 × 30.4（https://support.google.com/google-ads/answer/2375423 ）；轉換分散時每個活動的 Smart Bidding 資料都不足。

**怎麼做**：每日預算 ≥ 目標 CPA × 2–3（社群經驗值）；達不到時先用盡量爭取點擊或手動 CPC 累積轉換；完全 + 詞組比對 20–50 個高意圖字。

**常見錯誤**：每日 USD 10 開 5 個活動；接受「提高預算」建議而不看邊際 CPA。

### 5.12 Optimization score、Recommendations 與 auto-apply

**規範**：最佳化分數不是 KPI；建議逐項審核再手動套用；自動套用只開低風險類型（移除重複或未放送關鍵字），出價目標、廣泛比對、新增關鍵字、擴大聯播網一律關閉。

**為什麼**：最佳化分數是 Google 估計帳戶潛力的 0–100%，各建議提升值可能重疊，Quality Score 不使用它（https://support.google.com/google-ads/answer/9061546 ）。可自動套用的建議分廣告與素材、出價（調整目標、改 Smart Bidding）、關鍵字與指定目標（新增受眾、廣泛比對、Search 夥伴、Display 擴展）、評估四類；不會提高預算；排程中的建議可在建議頁底部佇列關閉；2026-01-26 起「新增 RSA」不再自動套用（https://support.google.com/google-ads/answer/10279006 ）。

**怎麼做**：建議 → 自動套用 → 取消高風險類型；MCC 層級統一設定；每週看佇列。

### 5.13 AI 功能與 Gemini（2026）

**規範**：Gemini 新功能先在非主力帳號試用；AI 生成的文案與圖片上線前人工審核政策與事實；AI 版位不能單獨購買。

**為什麼**：Google Marketing Live 2026（2026-05-20）宣布 Ask Advisor（以 Gemini 打造的統一代理，橫跨 Google Ads、Analytics、Google Marketing Platform，當時官方寫 Merchant Center 代理即將加入；官方說明為英文帳戶 Beta，https://blog.google/products/ads-commerce/ask-advisor/ ）與 Asset Studio（https://blog.google/products/ads-commerce/google-marketing-live-2026-collection/ ；Ask Advisor 在台灣的開放狀態待查證）。AI Overviews 與 AI Mode 廣告：現有 Search、Shopping、PMax 活動自動符合資格；廣泛比對、AI Max、Shopping、PMax 可做查詢與 AI 回答的情境比對，完全與詞組比對只在直接商業意圖時符合資格；不能單獨鎖定或退出；語言只有英文，台灣未列入（https://support.google.com/google-ads/answer/18826097 ）；2026-10-28 宣布 AI Mode 廣告擴及 10 國（https://blog.google/products/ads-commerce/ads-in-ai-mode-global/ ）。AI 生成素材的政策責任仍在廣告主。

**怎麼做**：英文活動不必為了 AI 版位改比對類型：完全與詞組比對在查詢有直接商業意圖時即符合資格；要涵蓋探索型問題再靠廣泛比對、AI Max、Shopping 或 PMax 的情境比對，並用否定字與品牌排除控制；AI 生成圖片加 AI 標示（17257106）。

---

## 6. SEO 與付費搜尋的協同

### 6.1 Google Ads 不影響自然排名（官方）

Google Ads 說明頁：「Running online ads has no impact on where your website appears in organic search results.」（https://support.google.com/google-ads/answer/6227161 ）；Paid & organic report 說明頁也寫付費支出不影響自然排名（https://support.google.com/google-ads/answer/3097241 ）。不要向客戶承諾「投廣告幫 SEO」；品牌曝光帶動搜尋需求屬間接效果（社群共識），停投時品牌查詢與自然點擊可能一起變動，報表要分開看。

### 6.2 品牌字要不要買：增量測試

**規範**：自然排名第一且 SERP 沒有競爭者 / 聯盟廣告時，品牌字可不買或低預算防守；有人競價、AI Overviews 或購物版位把自然結果推到首屏下、或要控制促銷訊息時，買。一律用測試決定。

**為什麼**：Google 2011 年 Search Ads Pause Studies（446 個帳號）顯示暫停廣告後平均 89% 的付費點擊沒被自然點擊補回（https://research.google/pubs/incremental-clicks-impact-of-search-advertising/ ）；這是舊研究且**不專指品牌字**，品牌字增量通常低得多（社群共識）。

**怎麼做**：連結 Search Console 開 Paid & organic report；品牌活動在一半地區暫停 2–4 週（台灣北部 vs 中南部）；比較兩組「付費 + 自然」總點擊與總轉換，並記錄拍賣洞察中的競爭者曝光；增量低就降預算。

**常見錯誤**：只看自然點擊增加就宣布成功；PMax 未排除品牌，暫停後 PMax 接手（P23）。

### 6.3 用 Search terms report 找 SEO 關鍵字

**規範**：每月匯出 Search terms 與 PMax 搜尋字詞洞察中「有轉換、自然排名第 2 頁以後或沒有頁面」的查詢，排入內容規劃（02 §7）。

**為什麼**：付費搜尋字詞是附轉換資料的真實查詢；Paid & organic report 可篩「廣告曝光 = 0」找只有自然曝光的查詢；限制：只算文字廣告、資料從連結日起算、不能只篩部分網域（https://support.google.com/google-ads/answer/3097241 ）。

**怎麼做**：90 天 Search terms 與 GSC 查詢比對 → 標記「付費有轉換、自然排名 > 10」→ 依 02 章分群決定新寫或改寫；反向用廣告先測 GSC 高曝光商業字的轉換率。

### 6.4 著陸頁共用與 noindex

**規範**：優先導到既有 SEO 頁；廣告專用變體頁一律 `noindex` 或 canonical 指向 SEO 主頁（擇一，不與 robots Disallow 同用，04 §3）；最終網址不帶 UTM（用追蹤範本）；robots.txt 不封鎖 AdsBot。

**為什麼**：重複頁分散自然訊號（04 §5–§6，12 C1 蠶食）；`noindex` 不影響廣告審查；AdsBot-Google 與 AdsBot-Google-Mobile **忽略 robots.txt 的 `*`**，只有點名才擋得到，擋了就無法審查（https://developers.google.com/crawling/docs/crawlers-fetchers/google-special-case-crawlers ）。

**驗收方式**：Screaming Frog 確認變體頁皆 noindex 或 canonical 至主頁；sitemap 不含廣告專用頁。

---

## 7. Google Ads 狀況 → 解法（P1–P28）

依第 12 章固定結構。證據等級：Google 官方證實 / 社群共識 / 個人經驗。

### P1. 廣告被拒：Misrepresentation

- **症狀**：遭拒，原因為 Misrepresentation 子類（Dishonest pricing、Unreliable claims、Unavailable offers、Unclear relevance）。
- **可能原因**：1. 廣告的價格、折扣、「免費」在到達頁找不到或有隱藏費用；2. 宣稱不太可能的結果；3. 廣告與到達頁主題不符。
- **診斷步驟**：1. 政策管理員看子類；2. 逐句對照廣告與到達頁首屏；3. 走一次結帳看隱藏費用。
- **解法**：立即：修文案或到達頁讓每句有出處，申訴「我已修改」。中期：建文案審核清單。
- **預防**：AI Max 文字指引列禁用詞；聯盟站不寫「官方」。
- **預估恢復時間**：重審 24–48 小時。
- **證據等級**：Google 官方證實（6020955）。
- **詳見**：§3.3。

### P2. 廣告被拒：Editorial

- **症狀**：遭拒原因為 Punctuation、Capitalization、Repetition、Business name、Phone number in ad text。
- **可能原因**：1. 符號裝飾或全大寫；2. 素材重複；3. 商家名稱放促銷語或他人品牌；4. 文案放電話。
- **診斷步驟**：1. 看被標記素材；2. 檢查商家名稱與網域關係。
- **解法**：立即：改寫；電話改通話素材；商家名稱改自有品牌。中期：建繁中文案範本。
- **預防**：§3.5.1。
- **預估恢復時間**：24–48 小時。
- **證據等級**：Google 官方證實（6021546、18287059）。
- **詳見**：§3.5.1。

### P3. Eligible (limited) 或 Limited ad serving

- **症狀**：可放送但曝光遠低於預期；狀態「符合資格（受限）」或新帳號特定搜尋幾乎不出現。
- **可能原因**：1. 廣告文字用了他人商標；2. 受限類別限制地區、年齡或裝置；3. Limited ad serving（帳號成熟度低、無品牌或引用他牌）。
- **診斷步驟**：1. 看「政策詳細資料」；2. 確認受限地區是否為主要市場；3. 檢查廣告是否清楚呈現自家品牌。
- **解法**：立即：移除商標字或取得授權；受限類別申請認證；標題 1 放品牌或網域。中期：完成驗證、保持政策紀錄乾淨；誤判用表單申訴。
- **預防**：§3.6、§3.7。
- **預估恢復時間**：商標改寫 24–48 小時；Limited ad serving 無官方時程（個人經驗：數週到數月）。
- **證據等級**：Google 官方證實（2684542、17122370、17344822）；時程為個人經驗。
- **詳見**：§4.1、§3.7。

### P4. Destination not working

- **症狀**：遭拒「到達網頁無法運作」，自己打開卻正常。
- **可能原因**：1. Cloudflare / WAF 對 AdsBot（美國 IP）回挑戰頁或 403；2. 網址打錯或改版 404；3. 主機逾時、5xx；4. 轉址迴圈或需登入。
- **診斷步驟**：1. AdsBot UA `curl -I` 測最終與展開網址；2. 從美國節點測；3. 看主機與 Cloudflare 安全事件。
- **解法**：立即：放行已驗證的 Google 爬蟲、修網址、申訴重審。中期：每 5 分鐘監控最終網址。
- **預防**：改版前列出廣告網址並 301；不封鎖美國流量。
- **預估恢復時間**：修正並申訴後 1–2 天。
- **證據等級**：Google 官方證實（16428019）；Cloudflare 原因屬社群共識。
- **詳見**：§3.5.2、04 §16、15 §13。

### P5. Destination mismatch

- **症狀**：遭拒「到達網頁不符」。
- **可能原因**：1. 最終網址轉到其他網域（聯盟短連結）；2. 追蹤範本轉到不同網域；3. 顯示網址與最終網址網域不同。
- **診斷步驟**：1. `curl -IL` 追轉址鏈；2. 檢查各層追蹤範本。
- **解法**：立即：最終網址改自有網域頁，追蹤改同網域參數。中期：品牌商導零售商時依 2026-07 初生效的新規確認是否適用，並事先申請核准。
- **預防**：聯盟站一律導自有內容頁。
- **預估恢復時間**：24–48 小時。
- **證據等級**：Google 官方證實（6368661、17140995）。
- **詳見**：§3.5.2、§3.7。

### P6. 聯盟落地頁被拒（bridge page）

- **症狀**：評測或比較頁遭拒「原創內容不足」或 Unfair advantage。
- **可能原因**：1. 頁面主要是聯盟按鈕、抄商家描述；2. 廣告比內容多；3. 違反聯盟合約付費搜尋條款。
- **診斷步驟**：1. 拿掉按鈕與廣告後還剩什麼；2. 05 §14 評分；3. 讀聯盟合約。
- **解法**：立即：補原創比較與實測、減廣告後申訴。中期：改成持續更新的評測主題頁。
- **預防**：只拿 SEO 表現好的內容頁投廣告。
- **預估恢復時間**：24–48 小時；Unfair advantage 須先停止違規投放。
- **證據等級**：Google 官方證實（16427718、15936768）。
- **詳見**：§3.7、09 §9。

### P7. 賭博 / 金融廣告需要認證

- **症狀**：遭拒「Gambling and games」或「需要金融服務驗證」；台灣信用卡比較頁廣告被拒。
- **可能原因**：1. 帳號無賭博認證或金融驗證；2. 目標國（如 TW）不允許 gambling-promoting content；3. 自己是推廣者而非持照業者，無法自行申請。
- **診斷步驟**：1. 確認角色（業者 / 推廣者）；2. 對照 §3.4.1 與 §3.4.3 的國家清單；3. 掃描站內外連是否連到投注服務。
- **解法**：立即：資訊站被判定為賭博類時，在 TW 停止相關廣告，不換網域重送；金融推廣請商家代為申請。中期：持照業者依 2026-08-26 新表單每國申請。
- **預防**：§3.4。
- **預估恢復時間**：認證與驗證審查時程官方未公布（待查證）。
- **證據等級**：Google 官方證實（6018017、17258294、12390454）。
- **詳見**：§3.4。

### P8. 商標投訴 / 商標限制

- **症狀**：廣告因 Trademarks 受限；或聯盟商家來信指你競價其品牌。
- **可能原因**：1. 文案用了商標且權利人已投訴；2. 聯盟合約禁止品牌字競價；3. 誤判（你是授權經銷商或資訊站）。
- **診斷步驟**：1. 確認受限的是文案（Google 只限制文案）；2. 讀聯盟合約；3. 檢查到達頁是否標示經銷商 / 資訊站身分。
- **解法**：立即：移除文案商標；合約禁止就把品牌字設否定。中期：請權利人授權帳號；誤判依通知申訴。
- **預防**：§3.6。
- **預估恢復時間**：改文案 24–48 小時；授權流程待查證。
- **證據等級**：Google 官方證實（6118）；聯盟合約限制為社群共識。
- **詳見**：§3.6。

### P9. 帳號停用：Circumventing systems

- **症狀**：突然停權、無預警，原因「規避系統」。
- **可能原因**：1. 與曾被停權帳號有關聯（同人、卡、網站、裝置）或停權後開新帳號；2. 被拒後改字、換子網域重送；3. Cloaking（含被駭轉址）；4. 驗證資訊不實。
- **診斷步驟**：1. 列出所有可能關聯帳號；2. 用 AdsBot 與一般 UA、不同國家 IP 比對到達頁；3. 檢查被駭（12 D7）。
- **解法**：立即：停止開新帳號，修正 cloaking 或被駭，申訴並誠實說明關聯。中期：申訴失敗就不要再開帳號，評估其他平台。
- **預防**：一事業一帳號；客戶間不共用付款資料；不做 UA 內容分支。
- **預估恢復時間**：只在誤判等情況恢復；數週（個人經驗），多數無法恢復。
- **證據等級**：Google 官方證實（15938075）；時程為個人經驗。
- **詳見**：§3.3、§4.3。

### P10. 帳號停用：Suspicious payment activity

- **症狀**：停權原因「可疑付款活動」，常在新帳號首次扣款前後。
- **可能原因**：1. 持卡人與帳號主體不同；2. 帳單地址、IP 國家、發卡國不一致；3. 短時間反覆換卡或扣款失敗。
- **診斷步驟**：1. 比對付款資料與驗證文件；2. 看交易紀錄的失敗或爭議。
- **解法**：立即：申訴並在 30 天內完成付款方式驗證，說明持卡人與帳號關係。中期：改用帳號主體自己的付款工具。
- **預防**：§2.2。
- **預估恢復時間**：驗證後審查以 Email 通知（官方未給天數；個人經驗 3–10 天）。
- **證據等級**：Google 官方證實（google-ads/answer/13704200）；原因排序為社群共識。
- **詳見**：§2.2、§4.3。

### P11. 帳號停用：Unpaid balance

- **症狀**：停權原因為未付餘額或對未來付款有疑慮。
- **可能原因**：1. 自動扣款失敗後未處理；2. 卡片過期或額度不足；3. 月結逾期。
- **診斷步驟**：1. 帳單 → 摘要看未付金額；2. 交易紀錄看失敗原因。
- **解法**：立即：付清、更新付款方式、必要時驗證，再申訴。中期：設備用付款方式與帳單提醒。
- **預防**：信用卡到期前 1 個月更換。
- **預估恢復時間**：付清後數天內（個人經驗）。
- **證據等級**：Google 官方證實（13704200）。
- **詳見**：§4.3。

### P12. 信用卡扣款失敗

- **症狀**：帳單出現「付款遭拒」，廣告停止或帳號暫停。
- **可能原因**：1. 發卡行擋國際 / 線上交易；2. 額度或單筆上限；3. 卡片幣別與帳戶幣別不同觸發風控。
- **診斷步驟**：1. 看失敗代碼；2. 打給發卡行確認風控。
- **解法**：立即：請發卡行放行 Google，改用備用付款方式「立即付款」。中期：調整付款門檻或申請月結。
- **預防**：備用付款方式；首月觀察。
- **預估恢復時間**：成功付款後數小時到 1 天（個人經驗）。
- **證據等級**：社群共識；暫停與驗證流程為官方證實（13704200）。
- **詳見**：§2.2。

### P13. 帳號停用：Misrepresentation / Unacceptable business practices

- **症狀**：停權原因「不當商業行為」或「不實陳述」，無預警。
- **可能原因**：1. 冒充品牌、政府或官方；2. 隱藏公司、聯絡、退款資訊；3. 大量使用者檢舉或無法交付；4. 網站被駭導向詐騙頁。
- **診斷步驟**：1. 用使用者角度確認看得出是誰、怎麼聯絡、怎麼退款；2. 搜尋品牌 + scam；3. 檢查被駭。
- **解法**：立即：補齊公司資訊與退款政策、移除官方暗示、完成驗證後申訴。中期：處理客訴與交付。
- **預防**：必要頁面齊全（22 §1.1）；接客戶前做背景檢查。
- **預估恢復時間**：只在誤判時恢復；數週（個人經驗）。
- **證據等級**：Google 官方證實（6020955）。
- **詳見**：§3.3、§4.3。

### P14. 廣告主驗證失敗或逾期

- **症狀**：帳號暫停，提示未完成驗證；或狀態「無法驗證」。
- **可能原因**：1. 期限內未完成（不可延長）；2. 文件名稱與付款資料不符或過期；3. 業務類型宣告錯誤或未揭露代理關係。
- **診斷步驟**：1. 廣告主驗證頁看每個任務原因；2. 逐字比對文件、付款資料、組織名稱。
- **解法**：立即：用通知信連結重新開始，上傳名稱一致的有效文件。中期：付款資料統一為法定全名。
- **預防**：通知當天開始；驗證期間不改資料。
- **預估恢復時間**：審查最多 5 個工作天（罕見 30 天），通過後才解除暫停。
- **證據等級**：Google 官方證實（15588490、9872152）。
- **詳見**：§2.3。

### P15. 廣告不出現 / 曝光很低

- **症狀**：活動符合資格但曝光極少；自己搜尋看不到。
- **可能原因**：1. 出價或預算太低（排名損失高）；2. 關鍵字 Low search volume 或 Rarely shown（P16、P17）；3. 地區、排程過窄或否定字擋主力字；4. 受限或 Limited ad serving（P3）。
- **診斷步驟**：1. 用廣告預覽與診斷工具，不要自己反覆搜尋；2. 看搜尋曝光比重的排名與預算損失；3. 看關鍵字狀態欄。
- **解法**：立即：提高主力群組出價或預算、放寬地區排程、移除衝突否定字。中期：改善 Quality Score 元件。
- **預防**：上線前跑診斷工具。
- **預估恢復時間**：數小時到 1 天。
- **證據等級**：Google 官方證實（關鍵字狀態：https://support.google.com/google-ads/answer/2453978 ）；原因排序為社群共識。
- **詳見**：§5.3、§5.9、§5.11。

### P16. 關鍵字狀態「Low search volume」

- **症狀**：關鍵字「搜尋量偏低」，不觸發廣告。
- **可能原因**：1. 長尾字搜尋量太少（繁中長尾常見）；2. 拼法罕見或過度精確。
- **診斷步驟**：1. 關鍵字規劃工具查量；2. 確認是否已有較廣的字涵蓋。
- **解法**：立即：改用較短的詞組或廣泛比對。中期：讓廣泛比對 / AI Max 涵蓋長尾。
- **預防**：避免超長完全比對。
- **預估恢復時間**：搜尋量回升時自動恢復，無固定時程。
- **證據等級**：Google 官方證實（2453978）。
- **詳見**：§5.3。

### P17. 關鍵字狀態「Rarely shown due to low quality score」

- **症狀**：關鍵字「因品質分數低而很少顯示」。
- **可能原因**：1. 著陸頁不相關或體驗差；2. 文案沒有該關鍵字意涵；3. 預期點閱率低（意圖不符）。
- **診斷步驟**：1. 看三元件哪個「低於平均」；2. 用 05 §14 檢查著陸頁。
- **解法**：立即：移到主題相符的廣告群組、改導最相關頁。中期：改善速度與內容。
- **預防**：單一意圖廣告群組。
- **預估恢復時間**：數天到 2 週（個人經驗）。
- **證據等級**：Google 官方證實（2453978、6167118）；時程為個人經驗。
- **詳見**：§5.9。

### P18. CPC 太高

- **症狀**：平均 CPC 超出轉換價值可承受範圍。
- **可能原因**：1. 高競爭產業（金融、保險、法律）；2. Quality Score 低；3. 無目標的出價策略；4. 廣泛比對 / AI Max 擴到高價查詢。
- **診斷步驟**：1. 拍賣洞察看競爭者；2. 依關鍵字看 CPC 與轉換率；3. 看最貴的 Search terms。
- **解法**：立即：設 tCPA、暫停高價低轉換字、加否定字。中期：改善 Quality Score、改打長尾與比較意圖字。
- **預防**：可負擔 CPC 上限 = 轉換率 × 每次轉換價值。
- **預估恢復時間**：1–2 週觀察。
- **證據等級**：社群共識。
- **詳見**：§5.2、§5.9。

### P19. 轉換追蹤沒資料 / 重複計算

- **症狀**：轉換為 0，或遠高於實際訂單。
- **可能原因**：1. 標記沒觸發（GTM 未發布、Consent Mode 擋下）；2. Google tag 與 GA4 匯入都設主要；3. 感謝頁重新整理重複計，計數設「每次」。
- **診斷步驟**：1. 轉換診斷；2. Tag Assistant 走一次流程；3. 比對後台訂單數。
- **解法**：立即：修觸發、同一事件只留一個主要轉換動作、名單計數改「一次」、購買用交易 ID 去重。中期：主要轉換改用後台訂單離線匯入。
- **預防**：§8.1 測試轉換。
- **預估恢復時間**：修正後 24–48 小時有新資料（不回補）。
- **證據等級**：Google 官方證實（16884284）；原因排序為社群共識。
- **詳見**：§5.1、13 §13.2。

### P20. GA4 與 Google Ads 轉換數不一致

- **症狀**：同期 GA4 Key events 與 Google Ads 轉換差很多。
- **可能原因**：1. Google Ads 歸到點擊日、GA4 歸到轉換日；2. 歸因模式與回溯期不同；3. Google Ads 含模型推估轉換；4. 標記覆蓋或篩選不同。
- **診斷步驟**：1. Google Ads 加「所有轉換（依轉換時間）」欄比較；2. 對齊歸因設定；3. 確認追蹤同一事件。
- **解法**：立即：訂口徑「出價以 Google Ads 為準、跨管道分析以 GA4 為準」。中期：GA4 匯入轉換設為次要。
- **預防**：13 §13.10 固定指標定義。
- **預估恢復時間**：屬口徑差異，無需恢復。
- **證據等級**：Google 官方證實（https://support.google.com/analytics/answer/1034383 ，UA 時期說明，GA4 仍適用屬社群共識）。
- **詳見**：§5.1。

### P21. Consent Mode 導致轉換掉

- **症狀**：導入 CMP 或 Consent Mode 後轉換明顯下降。
- **可能原因**：1. Basic 模式下拒絕者不送任何資料；2. 預設 denied 後 CMP 沒送 update；3. 資料量未達建模門檻。
- **診斷步驟**：1. Tag Assistant 看 default → update；2. 轉換診斷看 Consent Mode 狀態；3. 比對同意率。
- **解法**：立即：修 CMP update；評估改 Advanced 模式（法務確認）。中期：開 Enhanced conversions。
- **預防**：TW 依當地法規設定，不照搬歐盟預設（15 章範本）。
- **預估恢復時間**：修正後至少 7 個完整日才可能看到 uplift 資料，且須達最低資料門檻。
- **證據等級**：Google 官方證實（10000067）。
- **詳見**：§5.1。

### P22. Smart Bidding 學習期表現差

- **症狀**：改策略或新增活動後幾天 CPA 暴增。
- **可能原因**：1. 正常學習；2. 轉換量少或延遲長；3. 同時改太多；4. 轉換追蹤壞了（P19）。
- **診斷步驟**：1. 看出價策略狀態與原因；2. 用 2 個轉換週期或 2 週評估；3. 確認追蹤正常。
- **解法**：立即：同一轉換週期不再改目標、維持預算。中期：整併活動集中轉換。
- **預防**：每次只改一個變數。
- **預估恢復時間**：Learning 最長 7 天；收斂 1–2 個轉換週期。
- **證據等級**：Google 官方證實（13020501）。
- **詳見**：§5.2。

### P23. PMax 吃掉品牌字

- **症狀**：PMax 轉換漂亮，但品牌 Search 曝光下降；搜尋字詞洞察大量品牌字。
- **可能原因**：1. 未設品牌排除；2. 品牌 Search 受預算或目標限制；3. 品牌字非完全比對。
- **診斷步驟**：1. 洞察篩品牌字；2. 品牌 Search 看預算損失；3. 確認比對類型。
- **解法**：立即：PMax 品牌排除、品牌 Search 預算加到不受限、加完全比對與錯字。中期：實驗比較有 / 無品牌排除的總轉換。
- **預防**：先建品牌 Search，再開 PMax。
- **預估恢復時間**：1–2 週。
- **證據等級**：Google 官方證實（13810170、10724817）。
- **詳見**：§5.5、§6.2。

### P24. 無效點擊與退款

- **症狀**：點擊暴增但無轉換；特定地區或時段異常。
- **可能原因**：1. 機器人或點擊農場（Display、搜尋夥伴較常見，社群共識）；2. 競爭者手動點擊；3. 意外或重複點擊。
- **診斷步驟**：1. 加「無效點擊、無效點擊率」欄；2. 報表編輯器「Invalid Activity Credit Report: Search & PMax」；3. GA4 看該流量參與度。
- **解法**：立即：排除 IP 與刊登位置、必要時關搜尋夥伴、用 Click Quality Form 要求調查。中期：改轉換型出價。
- **預防**：Display 不用點擊型出價；監控每日異常。
- **預估恢復時間**：多數即時過濾不收費；事後偵測的以抵免退回（多為帳戶抵免，第三方觀察），時程官方未公布。
- **證據等級**：Google 官方證實（16826168、1704323）；退款形式為社群共識。
- **詳見**：§3.8、09 §8、22 章。

### P25. Search terms 出現大量不相關字

- **症狀**：搜尋字詞報表大量無關查詢在花錢。
- **可能原因**：1. 廣泛比對或 AI Max 擴展過寬（2026-09 自動升級後常見）；2. 否定字只列單一字形；3. 語言設定移除後配到其他語言（P28）。
- **診斷步驟**：1. 依花費排序標記不相關；2. 看比對類型與 AI Max 來源；3. 依語言分群。
- **解法**：立即：加否定字（含單複數、同義詞、各語言變體；錯字不必另加）。中期：AI Max 加品牌控制、URL 排除、文字指引；核心字改完全比對。
- **預防**：每週例行（§8.2）。
- **預估恢復時間**：加否定字後立即生效。
- **證據等級**：Google 官方證實（2453972）；擴展原因為社群共識。
- **詳見**：§5.3、§5.4。

### P26. 自動套用建議亂改帳戶

- **症狀**：出現沒加過的廣泛比對字、目標 CPA 被改、開了 Display 擴展。
- **可能原因**：1. 高風險類型自動套用開著；2. 客戶或業務代表按了「全部套用」。
- **診斷步驟**：1. 變更記錄篩「Google 建議（自動套用）」；2. 查自動套用設定。
- **解法**：立即：關閉高風險類型、用變更記錄還原。中期：MCC 統一設定，與客戶約定建議由代理審核。
- **預防**：每週看建議佇列。
- **預估恢復時間**：還原立即生效；目標被改過需 1–2 個轉換週期恢復成效。
- **證據等級**：Google 官方證實（10279006）。
- **詳見**：§5.12。

### P27. Ad strength 低

- **症狀**：RSA 廣告強度「不佳」或「普通」，客戶擔心成效。
- **可能原因**：1. 標題、說明不足或太像；2. 標題沒含關鍵字；3. 固定位置太多；4. 網站連結少於 6 個。
- **診斷步驟**：1. 看廣告強度的具體建議；2. 數標題、說明、固定位置。
- **解法**：立即：補到 15 則標題、4 則說明，減固定位置，補網站連結。中期：依素材報表的完整成效指標替換表現差的素材。
- **預防**：§5.8 標題分配法。
- **預估恢復時間**：評等立即更新；成效數週觀察。
- **證據等級**：Google 官方證實（廣告強度不影響放送資格與 Ad Rank：9921843）。
- **詳見**：§5.8。

### P28. 語言設定移除後，混語 / 繁中廣告配錯人

- **症狀**：2026-09 後活動出現大量其他語言查詢，或繁中廣告配到簡中查詢，轉換率下降。
- **可能原因**：1. 活動語言設定已移除，改依查詢語言與使用者語言偏好；2. 同一廣告群組混語言，或文案與到達頁語言不同；3. AI Max 文字自訂產生其他語言文案。
- **診斷步驟**：1. Search terms 依語言分群看轉換率；2. 檢查每個廣告群組的文案與到達頁語言。
- **解法**：立即：一個廣告群組一種語言、文案與到達頁一致，把高花費無效語言查詢加否定。中期：依語言拆活動與預算。
- **預防**：§5.10。
- **預估恢復時間**：1–2 週。
- **證據等級**：Google 官方證實（1722078）；混語判定行為為個人經驗，待查證。
- **詳見**：§5.10、10 章。

---

## 8. 本章檢查清單

格式：項目 ｜ 工具 ｜ 合格標準。

### 8.1 開戶與上線前

- [ ] 帳單國家、幣別、時區正確 ｜ 帳戶設定 ｜ 與付款主體一致
- [ ] 付款資料名稱、地址 = 驗證文件；主要 + 備用付款方式 ｜ 帳單 ｜ 一致、≥ 2 個
- [ ] 統編 / TIN 已填；核對首張月結單稅額 ｜ 帳單 → 設定 ｜ 正確
- [ ] 廣告主驗證完成或在期限內進行 ｜ 廣告主驗證 ｜ 已完成
- [ ] ≥ 2 位管理員且啟用兩步驟驗證 ｜ 存取權與安全性 ｜ 符合
- [ ] 產品類別政策檢查（賭博、金融、加密貨幣、醫療、酒精、政治、三振政策） ｜ §3.4、§4.4 ｜ 無禁止項、受限項已認證
- [ ] 賭博推廣站不在 TW 投放 ｜ §3.4.1 ｜ 不投
- [ ] 最終網址以 AdsBot UA 從美國與目標國測試 ｜ curl ｜ 100% 回 200
- [ ] robots.txt 未點名封鎖 AdsBot；顯示網址網域 = 最終網址網域 ｜ robots.txt、curl -IL ｜ 符合
- [ ] 到達頁有關於、聯絡、隱私、退款；聯盟揭露在首個連結前 ｜ 手動 ｜ 齊全
- [ ] 廣告變體頁 noindex 或 canonical 至主頁 ｜ Screaming Frog ｜ 100%
- [ ] 出價集中在 1 個主要轉換目標；同一事件不重複設主要動作；GA4 匯入設次要；Enhanced conversions 開啟 ｜ 目標 → 轉換 ｜ 符合
- [ ] EEA / UK / 瑞士流量有 CMP + Consent Mode ｜ Tag Assistant ｜ default → update 正常
- [ ] 測試轉換一次只計一次 ｜ Tag Assistant ｜ 1 次
- [ ] 品牌 / 非品牌分活動；非品牌加品牌否定；PMax 品牌排除 ｜ 活動設定 ｜ 完成
- [ ] 帳號層級否定清單（含各語言變體） ｜ 共用資料庫 ｜ 已套用
- [ ] 地區選項 Presence；每個廣告群組單一語言 ｜ 活動設定 ｜ 符合
- [ ] 每個廣告群組 ≥ 2 則 RSA、廣告強度良好以上 ｜ 廣告 ｜ 符合
- [ ] 自動套用只開低風險類型 ｜ 建議 → 自動套用 ｜ 已設定
- [ ] 聯盟合約付費搜尋條款已存檔 ｜ 合約 ｜ 已確認

### 8.2 每週

- [ ] 政策管理員的遭拒、受限、申訴 ｜ 政策管理員 ｜ 全部有處理紀錄
- [ ] Search terms 與 PMax 洞察加否定字 ｜ 搜尋字詞 ｜ 不相關花費占比下降
- [ ] 轉換追蹤狀態 ｜ 轉換診斷 ｜ 有效、無異常起落
- [ ] 預算與排名損失 ｜ 搜尋曝光比重 ｜ 主力活動預算損失 < 20%（經驗值）
- [ ] 建議佇列與自動套用變更 ｜ 建議、變更記錄 ｜ 無高風險自動變更
- [ ] 扣款成功、無未付餘額 ｜ 帳單 → 摘要 ｜ 無失敗
- [ ] 無效點擊率 ｜ 無效點擊欄 ｜ 無突增

### 8.3 每月

- [ ] Quality Score 三元件 ｜ 關鍵字欄位 ｜ 主力字無「低於平均」
- [ ] 以 2 個轉換週期評估 CPA / ROAS ｜ 出價策略報表 ｜ 目標 ±20%（經驗值）
- [ ] PMax 品牌字占比與管道成效 ｜ 洞察、管道成效 ｜ 品牌占比 < 5%（經驗值）
- [ ] AI Max 設定與自動升級狀態 ｜ 活動設定 ｜ 品牌控制、URL 排除已設
- [ ] 依完整成效指標替換表現差的素材 ｜ 素材報表 ｜ 已替換
- [ ] GA4 vs Google Ads 差異依固定口徑記錄 ｜ GA4、Google Ads ｜ 已記錄
- [ ] 付費 Search terms 轉成 SEO 題目 ｜ Paid & organic report、GSC ｜ ≥ 5 個
- [ ] 存取權清理 ｜ 存取權與安全性 ｜ 無離職人員
- [ ] 讀 Policy change log 新條目並更新本章 ｜ https://support.google.com/adspolicy/topic/16794025 ｜ 已更新
- [ ] 月結單、稅額、Invalid Activity Credit Report ｜ 帳單、報表編輯器 ｜ 已核對

---

## 9. 參考來源

所有來源查閱日期：2026-11-04；標「2026-11-05 查閱」者以該日為準。

**帳號、付款、驗證、稅務**
- Advertiser verification：https://support.google.com/adspolicy/answer/9703665
- Timelines for Advertiser verification：https://support.google.com/adspolicy/answer/15588490
- About Google Ads account pausing：https://support.google.com/adspolicy/answer/9872152
- Google Ads account suspensions overview：https://support.google.com/adspolicy/answer/2375414 （現轉址至 answer/9841640，2026-11-05 查閱）
- Billing and payment suspensions：https://support.google.com/google-ads/answer/13704200 （2026-11-05 查閱）
- Add a payment method：https://support.google.com/google-ads/answer/2375375
- About payment methods for Google Ads（台灣超商 / 郵局 / 匯款）：https://support.google.com/google-ads/answer/2375433 （2026-11-05 查閱）
- Taiwan-specific Billing Issues：https://support.google.com/google-ads/contact/billing_tw
- Google Play 台灣 5% VAT 與電子發票：https://support.google.com/paymentscenter/answer/9251135
- Daily budget 與每月上限：https://support.google.com/google-ads/answer/2375423
- PPC Land（2024-12-07）台灣指定 Google 為網路廣告平臺：https://ppc.land/taiwan-designates-google-as-regulated-online-advertising-platform-under-anti-fraud-law/

**政策**
- Google Ads policies：https://support.google.com/adspolicy/answer/6008942
- Policy change log 2026：https://support.google.com/adspolicy/topic/16794025
- Policy change log 2025：https://support.google.com/adspolicy/topic/16083443 （2026-11-05 查閱）
- Policy change log 2024（含 2025 年初條目）：https://support.google.com/adspolicy/topic/16090031 （2026-11-05 查閱）
- Misrepresentation 更新（2025-09，含 Dishonest pricing）：https://support.google.com/adspolicy/answer/16502634 （2026-11-05 查閱）
- Government documents and services 更新（2025-09）：https://support.google.com/adspolicy/answer/16561193 （2026-11-05 查閱）
- Abusing the ad network：https://support.google.com/adspolicy/answer/6020954
- Circumventing systems：https://support.google.com/adspolicy/answer/15938075
- Unfair advantage：https://support.google.com/adspolicy/answer/15936768
- Misrepresentation：https://support.google.com/adspolicy/answer/6020955
- Gambling and games：https://support.google.com/adspolicy/answer/6018017 （現轉址至 answer/15132179，2026-11-05 查閱）
- Gambling and Games Policy: Global（2026-08）：https://support.google.com/adspolicy/answer/17258294
- Financial Services Verification 主管機關與生效日：https://support.google.com/adspolicy/answer/12390454
- 金融服務驗證新要求（2026-06）：https://support.google.com/adspolicy/answer/17127726
- Cryptocurrencies：https://support.google.com/adspolicy/answer/14009787
- Healthcare and medicines：https://support.google.com/adspolicy/answer/176031
- Alcohol 國家擴大（2026-07）：https://support.google.com/adspolicy/answer/17230661
- Political content：https://support.google.com/adspolicy/answer/6014595
- Editorial：https://support.google.com/adspolicy/answer/6021546
- Editorial 更新（2026-10）：https://support.google.com/adspolicy/answer/18287059
- Destination requirements：https://support.google.com/adspolicy/answer/6368661
- Destination not working：https://support.google.com/adspolicy/answer/16428019
- Insufficient original content：https://support.google.com/adspolicy/answer/16427718
- Destination requirements 更新（2026-06）：https://support.google.com/adspolicy/answer/17140995 （2026-11-05 查閱）
- Trademarks：https://support.google.com/adspolicy/answer/6118
- Limited ad serving 更新：https://support.google.com/adspolicy/answer/17122370 、https://support.google.com/adspolicy/answer/17344822
- AI labeling（2026-07）：https://support.google.com/adspolicy/answer/17257106
- Appeals limits（2026-07）：https://support.google.com/adspolicy/answer/17251522 （2026-11-05 查閱）
- Strike system：https://support.google.com/adspolicy/answer/10922738 （2026-11-05 查閱）
- Repeat violations 執行程序（振數保留 90 天）：https://support.google.com/adspolicy/answer/10908668 （2026-11-05 查閱）
- Eligible (limited)：https://support.google.com/adspolicy/answer/2684542
- Google special-case crawlers（AdsBot）：https://developers.google.com/crawling/docs/crawlers-fetchers/google-special-case-crawlers

**投放與衡量**
- About Smart Bidding learning：https://support.google.com/google-ads/answer/13020501 （2026-11-05 查閱）
- About conversion goals：https://support.google.com/google-ads/answer/10995103 （2026-11-05 查閱）
- About primary and secondary conversion actions：https://support.google.com/google-ads/answer/11461796 （2026-11-05 查閱）
- Search Engine Roundtable（2026-10-21）Smart Bidding 學習說明改寫：https://seroundtable.com/google-ads-updates-smart-bidding-learning-doc-42345.html
- Enhanced conversions 單一開關與 Data Manager：https://support.google.com/google-ads/answer/16884284 （2026-11-05 查閱）
- Google Ads Developer Blog（2026-05-15）Offline Click Conversion Import 變更：https://ads-developers.googleblog.com/2026/05/changes-to-offline-click-conversion.html （2026-11-05 查閱）
- Google Ads API Feature deprecations：https://developers.google.com/google-ads/api/docs/deprecations （2026-11-05 查閱）
- Upgrade OCI to enhanced conversions for leads：https://support.google.com/google-ads/answer/14274408
- About consent mode：https://support.google.com/google-ads/answer/10000067 （2026-11-05 查閱）
- EU User Consent Policy audit：https://support.google.com/google-ads/answer/16724512
- Google tag gateway：https://support.google.com/google-ads/answer/16214371
- AI Max for Search：https://support.google.com/google-ads/answer/15910187
- Google 部落格 AI Max 升級（2026-04-15，06-11 更新）：https://blog.google/products/ads-commerce/dsa-upgrade-to-ai-max-2026/
- About Performance Max：https://support.google.com/google-ads/answer/10724817
- PMax 與 Search 優先順序：https://support.google.com/google-ads/answer/13810170
- Search Engine Roundtable PMax 否定字 10,000：https://www.seroundtable.com/google-ads-negative-keywords-10000-39044.html
- Video Action Campaigns 升級 Demand Gen：https://support.google.com/google-ads/answer/15110871
- YouTube and Discover Feed ad requirements（2026-08）：https://support.google.com/adspolicy/answer/17455694
- Responsive search ads：https://support.google.com/google-ads/answer/7684791
- Ad strength：https://support.google.com/google-ads/answer/9921843
- RSA 廣告層級素材報表：https://support.google.com/google-ads/answer/9564897 （2026-11-05 查閱）
- Quality Score：https://support.google.com/google-ads/answer/6167118
- Optimization score：https://support.google.com/google-ads/answer/9061546
- Auto-applied recommendations：https://support.google.com/google-ads/answer/10279006
- Keyword status：https://support.google.com/google-ads/answer/2453978
- Negative keywords：https://support.google.com/google-ads/answer/2453972 （2026-11-05 查閱）
- Keyword matching options：https://support.google.com/google-ads/answer/7478529
- Advanced location options：https://support.google.com/google-ads/answer/1722038
- Language targeting（2026-09 變更）：https://support.google.com/google-ads/answer/1722078
- Ads in AI Overviews and AI Mode：https://support.google.com/google-ads/answer/18826097 （2026-11-05 查閱）
- Google 部落格 AI Mode 廣告擴展（2026-10-28）：https://blog.google/products/ads-commerce/ads-in-ai-mode-global/
- Google Marketing Live 2026：https://blog.google/products/ads-commerce/google-marketing-live-2026-collection/ （2026-11-05 查閱）
- Google 部落格 Ask Advisor（2026-05-20）：https://blog.google/products/ads-commerce/ask-advisor/ （2026-11-05 查閱）
- Invalid Activity Credit Report：https://support.google.com/google-ads/answer/16826168
- Credits and adjustments：https://support.google.com/google-ads/answer/1704323
- [UA] Data discrepancies between Google Ads and Analytics：https://support.google.com/analytics/answer/1034383

**SEO 協同**
- 廣告不影響自然排名：https://support.google.com/google-ads/answer/6227161
- Paid and organic report：https://support.google.com/google-ads/answer/3097241
- Google Research（2011）Incremental Clicks Impact Of Search Advertising：https://research.google/pubs/incremental-clicks-impact-of-search-advertising/
