# 22 AdSense 完整規範與問題排解

> 版本：1.1 ｜ 更新日期：2026-11-05 ｜ 適用：所有使用 AdSense 的網站 ｜ 撰寫：Claude

## 本章摘要

1. 本章是 AdSense 的正典位置：申請、驗證、付款、稅務、政策、版位、收益、無效流量、問題排解都以本章為準；09 只保留摘要，聯播網門檻、RPM、CWV、聯盟、付費牆仍在 09。
2. 申請只看三件事：自有高品質原創內容、能存取 HTML、遵守計畫政策，年滿 18 歲；**官方沒有流量、文章數、網域年齡門檻**。繁體中文在支援語言清單內，高棉文、寮文、緬甸文不在清單內（§1.1）。
3. 2026 年的重大變更：身分驗證門檻依所在地改為 USD 0（新帳號可能要先驗證才能放廣告，以帳號通知為準）；TCF v2.3 自 2026-03-01 強制；Auto ads 的 ad load 滑桿 2026-04-16 移除、改為 advanced settings；vignette 新觸發條件 2026-03-09 自動開啟、返回鍵觸發 2026-06-15 起取消；Offerwall 2026-04-13 全面開放；TCF 錯誤 2026-10-15 移入 Policy center（§1.5、§2.6、§3）。
4. 賭博內容：Publisher Restrictions 的 Online gambling 只針對「讓使用者參與線上真錢賭博」的內容，且**對位於美國、英國等 18 國的使用者不適用**（§2）。
5. 帳號是最大的資產：自點、買點擊型流量、付費流量導到滿版廣告頁（arbitrage）都可能導致永久停用；暫時停用不可申訴，永久停用的申訴只有一次實質機會（§5）。

## 目錄

1. [帳號與申請](#1-帳號與申請)
2. [政策全覽](#2-政策全覽)
3. [版位與功能規範](#3-版位與功能規範)
4. [收益優化](#4-收益優化)
5. [無效流量與帳號安全](#5-無效流量與帳號安全)
6. [問題排解（P1–P29）](#6-問題排解p1p29)
7. [本章檢查清單](#7-本章檢查清單)
8. [參考來源](#8-參考來源)

---

## 1. 帳號與申請

### 1.1 申請資格與支援語言

**規範**：申請前同時滿足：(1) 網站內容為自有、高品質、原創且有讀者；(2) 能存取網站 HTML 原始碼；(3) 全站符合 AdSense 計畫政策與 Google Publisher Policies；(4) 申請人年滿 18 歲；(5) 網站主要語言在支援清單內；(6) 一人只有一個 AdSense 帳號。

**為什麼**：
- 資格頁（https://support.google.com/adsense/answer/9724 ，查閱 2026-11-04）只列上述內容；未滿 18 歲由家長或監護人以其帳號申請、款項付給該成年人。頁面**未列**流量、網站年齡或特定國家等待期。
- 支援語言（https://support.google.com/adsense/answer/9727 ，查閱 2026-11-04）含 Chinese (traditional)、Chinese (simplified)、Filipino、English、Thai、Vietnamese、Indonesian、Malay 等約 50 種。清單未列 Cebuano、Ilocano、Khmer、Lao、Burmese。2026-11-05 再查：Thai、Bengali (Bangla)、Tamil 在清單內；Nepali、Sinhala 不在清單內（市場評估見 25 章）。
- 「Placing Google ad code on pages with content primarily in an unsupported language is not permitted」：主要語言不支援的頁面不得放廣告碼，申請會以 Unsupported language 拒絕（https://support.google.com/adsense/answer/81904 ，查閱 2026-11-04）。
- 一個發布者只能有一個帳號（同上 answer/81904 的 Duplicate account）。

**怎麼做**：
1. 頁面：Privacy Policy 是官方要求，須揭露資料收集與使用，並告知第三方可能使用 cookie、web beacon 或 IP 位址（https://support.google.com/publisherpolicies/answer/10502938 ，查閱 2026-11-05），建議一併說明如何退出個人化廣告。About、Contact、Terms，以及內容站的 Editorial Policy 與作者頁是網站經營建議，官方資格頁未列為申請要件（https://support.google.com/adsense/answer/9724 ，查閱 2026-11-05）。
2. 內容：經驗值 20–30 篇以上的實質原創文章（非官方門檻），首頁與分類頁都有內容、無空分類與「coming soon」。
3. 網站可從任何 IP、任何地區存取；robots.txt、WAF、Cloudflare 不擋 AdSense 爬蟲（Mediapartners-Google）。
4. 已有 AdSense 帳號者，新站一律「在同一帳號加網站」，不要再開帳號。

**驗收方式**：Sites 頁狀態為 Ready；Policy center 無 Policy issue，Regulatory issue 與 Advertiser preference 已檢視（2025-04-22 起 Must fix 標籤由這三類取代，https://support.google.com/adsense/answer/15918799 ，查閱 2026-11-05）。

**常見錯誤**：以為要 1,000 訪客或 6 個月網齡才可申請（傳言）；用家人名義另開第二個帳號；語言不在支援清單的站直接申請。

### 1.2 申請流程與網站連結方式

**規範**：依「註冊 → 新增網站 → 連結網站 → 完成帳號設定（付款資料、身分驗證）→ Request review」的順序操作；網站在 Getting ready 期間不移除、不重送。

**為什麼**：連結網站現行流程有三種方式：AdSense code snippet（放在 `<head>`）、Ads.txt code snippet（放進根目錄的 ads.txt）、Meta tag（放在 `<head>`，適合不想在首頁放 AdSense 程式碼時使用）（https://support.google.com/adsense/answer/7584263 ，查閱 2026-11-05）；網站未就緒的疑難排解頁另提供替代方式：在 Search Console 驗證網站所有權（https://support.google.com/adsense/answer/12176698 ，查閱 2026-11-05）；Getting ready 期間「Don't remove and resubmit」，否則會延誤（https://support.google.com/adsense/answer/12170222 ，查閱 2026-11-04）。

**怎麼做**：
1. 用長期使用、已開兩步驟驗證的 Google 帳號註冊；付款資料的姓名與身分證件完全一致（§1.5）。
2. 選一種連結方式：Astro / 靜態站最簡單是 `<head>` 放 AdSense 程式碼；不想在首頁放程式碼可改 Meta tag 或 Ads.txt code snippet；連結卡住時可用已驗證的 Search Console 所有權。ads.txt 可在核准前先放（它本身就是連結方式之一）。
3. 完成帳號設定後按 Request review。

**驗收方式**：Sites 頁從 Requires review 變為 Getting ready。

**常見錯誤**：程式碼放在 `<body>` 某個元件內、只在部分模板輸出；審核期間改版或換主機導致 404。

### 1.3 網站審核狀態與時程

| 狀態（後台英文） | 意思 | 你要做的事 |
|---|---|---|
| Requires review | 尚未審核，或網站久未活動需重新審核 | 完成帳號設定後按 Request review |
| Getting ready | AdSense 正在檢查網站；也可能在等付款設定等其他任務 | 等待；不要移除後重送 |
| Needs attention | 有問題要修，後台會列具體原因 | 依原因修正後再 Request review（§6 P1–P6） |
| Ready | 可以放廣告 | 持續遵守政策 |

官方時程：審核「usually takes a few days, but in some cases can take 2-4 weeks」（answer/12170222，查閱 2026-11-04）。ads.txt 有獨立狀態：Not applicable（平台代管）、Not found、Unauthorized（pub ID 不在檔內，廣告請求會被拒）、Authorized（§2.7）。

### 1.4 子網域、子目錄與新站加入

**規範**：Sites 頁只新增「網域」；子網域與子目錄不另外新增，只有列在 Public Suffix List 的子網域（如 `site.appspot.com`）與平台夥伴網站（如 `site.blogspot.com`）可以單獨當作網站。

**為什麼**：2023-03-20 起，既有網站底下的子網域不能再在 Sites 頁新增或管理，原有子網域項目被移除「will not impact ad serving or your earnings」，子網域的封鎖設定提升到網域層級（https://support.google.com/adsense/answer/12170421 ，查閱 2026-11-04）。子目錄官方未說明，實務上隨網域核准（社群共識）。

**怎麼做**：
1. 新網域：Sites → 新增網站 → 連結 → Request review，每個網域各自審核。
2. 已核准網域的新子網域（如 `blog.example.com`）：同樣的 pub ID 程式碼即可，內容仍須合規；ads.txt 放在根網域（§2.7）。
3. 新語言子目錄（如 `/tl/`）：確認語言在支援清單內。

**驗收方式**：新網域 Ready；子網域頁面在報表「網站」維度出現收益。

**常見錯誤**：把 `blog.example.com` 當成新網站申請而卡住；以為子網域可以逃避主網域的政策處置。

### 1.5 身分驗證、PIN 與地址驗證

**規範**：收到驗證通知當天就處理；付款資料姓名、證件姓名、證件國家三者一致；PIN 寄送地址用可長期收信、正確完整、與帳號國家相符的地址。

**為什麼**：
- 門檻（https://support.google.com/adsense/answer/1709871 ，查閱 2026-11-05）：USD 表列身分驗證 **USD 0**、地址驗證 USD 10、選擇付款方式 USD 10、付款門檻 USD 100；變更說明寫「Depending on your location」，身分驗證 USD 0 依所在地而定，實際依帳號通知辦理。Search Engine Roundtable（2026-09-23）報導說明頁寫「Starting June 2026, you may need to verify your identity before your account can start showing ads」；但身分驗證說明頁（https://support.google.com/adsense/answer/11608017 ，查閱 2026-11-04）仍寫 USD 10，兩頁不一致，以後台通知為準。
- 身分驗證：45 天內完成，否則停止放廣告；線上方式由 Persona 做臉部比對（約 10 分鐘），或證件 + 實體 PIN（2–4 週）；證件須與付款資料同國、同姓名，嘗試次數有限（answer/11608017）。
- 地址 PIN：6 位數、國際平信、無追蹤號碼，通常 3 週送達；自 PIN 產生起 4 個月內輸入，逾期或輸入錯誤 3 次就停止放廣告；可申請補寄，第 4 次補寄 3 週仍未到改走 PIN troubleshooter（https://support.google.com/adsense/answer/157667 ，查閱 2026-11-04）。

**怎麼做**：
1. 官方要求地址正確、最新、位於帳號所選國家或地區，且能收普通郵件；並建議用當地語言文字填寫（https://support.google.com/adsense/answer/1348257 ，查閱 2026-11-05）。台灣地址用當地語言文字寫完整地址。
2. 第一張 PIN 寄出 3 週未到就申請補寄，不要等到 4 個月邊緣。
3. 姓名錯誤先改付款資料再重來，不要用他人證件。

**驗收方式**：Payments → Verification 顯示已完成；無「付款暫停」橫幅。

**常見錯誤**：付款資料用暱稱或英文名與證件不同；PIN 寄到租屋處已搬家；把 PIN 輸入在錯的帳號。

### 1.6 付款門檻、時程與付款方式

| 項目 | 規則（查閱 2026-11-04） | 來源 |
|---|---|---|
| 付款門檻 | USD 100（其他幣別頁內另列；TWD 未見於該頁表格） | answer/1709871 |
| 月結時程 | 每月 3 日結算上月收益；20 日前完成付款資料變更與解除暫停；21–26 日付款（遇假日順延） | https://support.google.com/adsense/answer/7164703 |
| 到帳時間 | EFT 最多 7 個工作天；電匯最多 15 個工作天；支票 2–4 週 | answer/7164703 |
| 台灣可用方式 | 支票、電匯；EFT 與 Hyperwallet 不提供 | https://support.google.com/adsense/answer/1714397 |
| 2025–2026 變更 | Hyperwallet 開放美國（2025-02）、中國與阿根廷（2025-10）、拉美加勒比（2026-06）；歐元支票 2026-08-07 停用；台灣不在擴充名單 | AdSense 公告頁 |

**規範**：台灣帳號的官方可用方式是支票與電匯（https://support.google.com/adsense/answer/1714397 ，查閱 2026-11-05）；本文建議用電匯（wire transfer）到能收外幣的帳戶，並在 20 日前確認無付款暫停。電匯手續費與匯差依銀行而定（經驗值：選外幣帳戶並比較中轉行費用）。

### 1.7 稅務資訊

**規範**：後台要求時（依所在地與適用情況，並非所有發布者都需要）在 Payments → Manage tax info 提交美國稅務資訊，表單依稅務身分與收入性質判定；當地稅務（台灣）由自己或會計師處理，Google 不提供稅務建議。

**為什麼**：
- 美國：標題為 Contracting entity is Google LLC 的說明頁寫，Google 依美國國稅法 Chapter 3 向「all monetizing publishers」收集稅務資訊，對「revenue from buyers in the U.S.」扣繳；申請協定優惠須提供外國或美國 TIN（https://support.google.com/adsense/answer/1322037 ，查閱 2026-11-05）。另一頁則明言「Not all publishers are required to provide tax information」，是否須提供依所在地而定（https://support.google.com/adsense/answer/2490070 ，查閱 2026-11-05）；實際以後台要求為準。
- 扣繳率：未提供有效表單時，一般預設 30%；部分未提供文件、被推定為美國人士的情況為 24%；實際稅率取決於收入類型、稅務身分與協定資格，且只有來自美國的收入會被扣繳（https://support.google.com/paymentscenter/answer/10349995 ，查閱 2026-11-05）。網路常見「未提交 24%、提交未主張協定 30%」的二分法不成立。
- 新加坡：說明頁有新加坡稅籍居留的段落，但寫明其狀態目前「does not result in account limitations」，也不影響付款與扣繳；文件審查最長 7 個工作天（https://support.google.com/adsense/answer/14131950 ，查閱 2026-11-04）。
- 台灣：財政部 2025-09-10 發布網紅（網路創作者）營業稅作業規範，平台分潤依觀眾所在地判斷，台灣觀眾部分屬營業稅課稅範圍（一般稅率 5%、查定課徵小規模營業人 1%），境外觀眾部分可適用零稅率，輔導期至 2026-06-30；未達稅籍登記條件的個人改依執行業務所得課綜合所得稅（公視新聞與數位時代報導，查閱 2026-11-04）。AdSense 網站廣告收入是否完全比照：**待查證**（以財政部原文與會計師意見為準）。

**怎麼做**：回答後台的稅務問題以判定表單：W-9 適用美國人士；W-8BEN、W-8BEN-E 分別適用符合條件的非美國個人、實體；另有 W-8ECI 等（answer/1322037，查閱 2026-11-05）。台灣居民能否主張協定優惠：**待查證**，由稅務顧問判斷。表單每次變更姓名、地址後重新提交。

**驗收方式**：Tax info 狀態 Accepted；付款明細沒有非預期的扣繳列。

**常見錯誤**：非美國人士用 W-9（W-9 適用美國人士）；稅務姓名與付款資料不一致導致 Declined；以為「收入來自 Google 新加坡就不用在台灣報稅」。

### 1.8 營收分成與按曝光計費

- AdSense for content：發布者取得「80% of the revenue, after the advertiser platform takes its fee」；廣告主經 Google Ads 購買時，發布者約得 68%（https://support.google.com/adsense/answer/180195 ，查閱 2026-11-04）。
- 2023-11 公告、2024 年起 AdSense 由主要按點擊改為按曝光計費（Google 官方部落格 https://blog.google/products/adsense/evolving-how-publishers-monetize-with-adsense/ ，查閱 2026-11-05）；廣告主仍可能按點擊或轉換付費。官方未說明 CTR 對收益的影響，也未提供影響因素排序（§4.4）。
- Search ads（AdSense for Search）分成：官方頁未公開數字，**待查證**。

### 1.9 AdSense for Search（Search ads）

站內搜尋可用 Programmable Search Engine 搭配 Search ads 變現；2024-11-15 起 Custom Search Ads 改名為 Search ads，Related search for Auto ads、Related search for content pages 歸入 AFS Product-Integrated Features（PIF，是一組功能類型，不是新名稱），Search ads 只能用在三種明確搜尋意圖來源；2025-04-22 起 AFS 不再支援行動 App；2025-11-01 起，流量從你可控制的來源（含合作的第三方聯播網、服務或聯盟，不限付費購買）進入 Related search for content pages 時，必須以 `referrerAdCreative` 參數傳入廣告或連結來源精確、完整的創意文字（逐字），否則屬違規（https://support.google.com/adsense/answer/9336650 ，查閱 2026-11-05）。內容站一般不需要 AFS。

---

## 2. 政策全覽

### 2.1 政策層級地圖

| 層級 | 範圍 | 違反後果 | 來源 |
|---|---|---|---|
| AdSense Program policies | 無效點擊、鼓勵點擊、流量來源、廣告行為、版位、網站行為 | 警告、限制、暫停、停用 | https://support.google.com/adsense/answer/48182 |
| Ad placement policies | 自動重新整理、彈窗、軟體內廣告、標籤 | 停用廣告放送 | https://support.google.com/adsense/answer/1346295 |
| Google Publisher Policies | 內容政策、行為政策、隱私政策、其他標準（含 Search 垃圾政策、Better Ads、ads.txt、制裁） | 頁面 / 網站停用或限制放送 | https://support.google.com/publisherpolicies/answer/10502938 |
| Google Publisher Restrictions | 可放廣告但需求受限的內容 | Restricted ad serving，Google Ads 廣告不投放 | https://support.google.com/publisherpolicies/answer/10437795 |
| EU User Consent Policy | EEA / UK / 瑞士同意 | Restricted ad personalization | https://support.google.com/adsense/answer/13554116 |

政策變更紀錄：AdSense（https://support.google.com/adsense/answer/9336650）與 Publisher Policies（https://support.google.com/publisherpolicies/answer/10852414），每季讀一次。

### 2.2 AdSense 計畫政策重點

| 類別 | 規則（查閱 2026-11-04） | 後果 |
|---|---|---|
| 無效點擊與曝光 | 任何理由都不得點自己的廣告；不得以任何方式人為增加點擊或曝光 | 扣款、限制、暫停、停用 |
| 鼓勵點擊 | 非獎勵版位（non-rewarded inventory）不得補償使用者看廣告或搜尋（查閱 2026-11-05）；獎勵廣告例外，須符合獎勵單元政策：使用者自願選擇、事先揭露、不得提供直接金錢獎勵（https://support.google.com/adsense/answer/9121589 ，查閱 2026-11-05）；廣告標籤只能用「Advertisements」或「Sponsored Links」；不得用「Favorite Sites」「推薦閱讀」等誤導標題 | 警告 → 停用 |
| 流量來源 | 禁止 paid-to-click、paid-to-surf、autosurf、click-exchange、垃圾郵件、他站的不當廣告、軟體觸發的彈窗或轉址；接收付費廣告流量的網站須符合 Landing Page Quality 精神 | 無效流量扣款、停用 |
| 廣告行為 | 可修改廣告碼，但不得人為提高成效或損害廣告主 | 限制放送 |
| 版位 | 不得放在彈窗、pop-under、Email、軟體；不得放在以私人通訊為主的畫面（2024-08 起）；不得未經使用者要求重新整理頁面或元素；網站彈窗不得超過 3 個 | 停用放送 |
| 網站行為 | 易於導覽；不得改變使用者偏好、轉址到不想去的網站、自動下載 | 停用 |
| Sensitive events | 突發重大事件期間，Google 可限制相關內容變現（2024-02-09 起） | 限制放送 |

### 2.3 Google Publisher Policies 四大類

| 類別 | 項目（https://support.google.com/publisherpolicies/answer/10502938 ，查閱 2026-11-04） |
|---|---|
| 內容政策 | 非法內容、智慧財產權濫用、危險或貶損、虐待動物、不實陳述（誤導、不可靠且有害的主張、欺騙行為、操弄媒體）、助長不誠實行為、露骨色情、性交易、郵購新娘、家庭內容中的成人主題、兒少性剝削 |
| 行為政策 | 不誠實的聲明、廣告干擾、廣告空間價值（無內容畫面、脫離情境的廣告、複製內容、廣告多於內容）、不支援語言 |
| 隱私政策 | 個人化廣告、隱私揭露、Google 網域 cookie、識別使用者、裝置與位置資料、COPPA |
| 其他標準 | Google 網頁搜尋垃圾政策、濫用體驗、惡意軟體、Better Ads Standards、授權廣告空間（ads.txt）、制裁法規遵循 |

個人化廣告政策禁止依使用者在賭博、成人、政府機關網站的活動做目標設定；這是對廣告技術使用方的限制，不是禁止賭博資訊站放廣告。

### 2.4 Publisher Restrictions 與敏感類別封鎖

**規範**：受限內容可以放 AdSense，但要預期需求少、RPM 低；不要把受限內容與一般內容混在同一頁，以免整頁被標記。

**為什麼**：被標記的內容「fewer advertising sources will be eligible to bid」，有時完全沒有廣告，且 Google Ads 廣告不會投放（answer/10437795，查閱 2026-11-04）。受限類別：性相關內容、驚悚內容、爆炸物、槍械與零件、其他武器、菸草、娛樂性毒品、酒類販售或濫用、線上賭博、處方藥、未核准藥物與補充品、被 Google Play 下架的 App；另有「廣告遮蓋內容 / 內容遮蓋廣告」兩項行為限制與影片廣告限制（2026-10-22 起移除 Accompanying Content 須在頁面主體載入、sticky 播放器須從主內容開始兩項要求）。

**怎麼做**：Brand safety → Blocking controls → Sensitive categories：Restricted 類（Gambling & Betting (18+)、Alcohol）預設封鎖；Standard 類（Dating、Get rich quick、Astrology 等）預設允許，可自行封鎖（https://support.google.com/adsense/answer/164131 ，查閱 2026-11-04）。Video Games（2025-05-15）與 Significant Skin Exposure（2025-07-30）已從封鎖控制移除。

**驗收方式**：Policy center 無非預期的 Restricted ad serving；封鎖類別清單有紀錄理由。

**常見錯誤**：為了品牌形象一口氣封鎖十幾個類別，導致競價變少、RPM 下降（§4.2）。

### 2.6 隱私與同意

**規範**：有 EEA、英國、瑞士流量者，使用 Google 認證、整合 IAB TCF 的 CMP（可直接用 AdSense 的 Privacy & messaging），TCF 版本須為 v2.3；有美國流量者設定 US state regulations 訊息；所有市場的隱私權政策都揭露 Google 與第三方 cookie。

**為什麼**：
- EEA / UK 自 2024-01-16、瑞士自 2024-07-31，投放個人化廣告須用 Google 認證 CMP；未用認證 CMP 的流量只能拿非個人化或限制型廣告；EEA / UK 的 Search Ads 請求未用認證 CMP 時，可選擇實作 `ivt` 參數，允許僅供無效流量偵測的 cookie 與本機儲存（官方提醒收益可能下降），認證 CMP 與 `ivt` 都沒有時才完全不放送（https://support.google.com/adsense/answer/13554116 ，查閱 2026-11-05）。
- 所有發布者與 CMP 須於 2026-03-01 前改用 **TCF v2.3**（不再是 v2.2）；不符者的廣告請求可能被降為限制型廣告或丟棄，新增錯誤碼 1.4（Disclosed vendors 區段缺漏或未含 Google）；2026-10-15 起 TCF 錯誤改列在 Policy center 的「Regulatory issue」；2026-09-11 新增「Maximize message coverage」，在請求缺 TC string 時由 Google CMP 補收同意（AdSense 公告頁，查閱 2026-11-04）。
- 美國：US state regulations 訊息支援 IAB GPP，AdSense 讀取 US National、California、Colorado、Connecticut、Florida、Virginia 字串，使用者選擇退出時觸發 RDP（restricted data processing）；2025-10-06 支援 GPP National v2；Indiana、Kentucky、Rhode Island 2026-01-01 生效；GPC 訊號在多州直接觸發 RDP（https://support.google.com/adsense/answer/10961479 與公告頁，查閱 2026-11-04）。
- 2026-05-18 推出 Tag for age treatment（TFAT），取代 TFCD / TFUA 並新增 TEEN 選項。
- 台灣（個人資料保護法）沒有 Google 指定 CMP 的要求，但 Publisher Policies 的隱私揭露政策全球適用。

**怎麼做**：Privacy & messaging → European regulations 建立訊息（Google CMP 已是認證 CMP，TCF CMP ID 300）→ 開 Maximize message coverage → US state regulations 選「所有目前與未來支援的州」。用第三方 CMP 者確認已升級 TCF v2.3。

**驗收方式**：Policy center 無 Regulatory issue；報表以國家篩選 EEA 時，「Restricted ad personalization」狀態消失。

**常見錯誤**：用自製 cookie 橫幅；第三方 CMP 未升級 v2.3 導致 2026-03 起歐洲收益掉；在同意前就載入廣告碼卻沒送 TC string。

### 2.7 ads.txt 與 sellers.json

**規範**：根網域 `https://example.com/ads.txt` 回應 HTTP 200、純文字、UTF-8，含 `google.com, pub-XXXXXXXXXXXXXXXX, DIRECT, f08c47fec0942fa0`；接其他聯播網時把對方提供的列一併加入，不刪 Google 列。

**為什麼**：
- 缺 pub ID 時狀態為 Unauthorized，廣告請求會被拒、造成收益損失；更新需「a few days」，流量少的網站「up to a month」（https://support.google.com/adsense/answer/7532444 、answer/12171244，查閱 2026-11-04）。
- 爬取從根網域開始：`www.example.com/ads.txt` 只有在 `example.com/ads.txt` 轉址過去時才會被讀；最多跟隨一次跨出原根網域的 HTTP 轉址，同一原始根網域內可多次轉址（https://support.google.com/adsense/answer/9785052 ，查閱 2026-11-05）；HTTP 與 HTTPS 都要可存取；robots.txt 若擋 `/ads` 會被忽略（https://support.google.com/adsense/answer/7679060 ，查閱 2026-11-04）。
- sellers.json：可選 Confidential 或 Transparent，Transparent 顯示付款資料的個人或公司名稱；設定跨 AdSense / AdMob / Ad Manager 共用，最長 7 天反映（https://support.google.com/adsense/answer/9889911 ，查閱 2026-11-04）。

**怎麼做**：Astro 放在 `public/ads.txt`；WordPress 用外掛或根目錄檔案；Cloudflare 規則不要對 `/ads.txt` 做挑戰，也不要讓轉址跨出根網域超過一次；改完在 Sites 頁按 Check for updates。

**驗收方式**：`curl -I https://example.com/ads.txt` 回 200、`content-type: text/plain`；Sites 頁 ads.txt 為 Authorized。

**常見錯誤**：檔案放在子目錄；用 Word 編輯產生全形逗號或 BOM；轉址跨出原根網域超過一次（同根網域內的 `example.com` → `www` 多次轉址官方支援）；子網域另放 ads.txt 但根網域沒有。

### 2.8 AI 生成、聯盟、爬取與自動產生內容

**規範**：AI 可以輔助寫作，但每頁都要人工審閱、補上第一手資料或觀點；不得在自動產生、未經人工審閱或策展的頁面放廣告；聯盟內容只能是站內少數，或本身提供明顯附加價值。

**為什麼**：
- 無內容畫面政策：「Don't place ads on automatically generated content without manual review or curation」（https://support.google.com/publisherpolicies/answer/11112688 ，查閱 2026-11-04）。
- 複製內容政策列出：鏡像、框架、爬取或改寫他站內容而無附加價值；未經人工審閱的自動產生內容；同義詞替換後重貼；專門嵌入他站影片或圖片而無實質附加價值的網站（https://support.google.com/publisherpolicies/answer/11190248 ，查閱 2026-11-04）。
- Publisher Policies 把 Google 網頁搜尋垃圾政策納入其他標準，scaled content abuse 等違規也會影響變現（詳見 07 §5、11）。
- 拒絕原因 Content quality issues 寫明不要在自動產生頁放廣告碼、聯盟內容保持少數（answer/81904）。
- 官方沒有「禁止 AI 內容」的 AdSense 專文；2026-07-13 起 Google 會標示 AI 生成的廣告素材，屬廣告主端，與發布者內容無關。

**怎麼做**：AI 產線依 11 §9 SOP；程序化頁要有該頁獨有資料，模板文字比例低；不轉貼官方新聞稿全文，只摘要並加分析。

**驗收方式**：抽 20 頁，每頁能指出「別處沒有的內容」；Policy center 無 Valuable inventory 類問題。

**常見錯誤**：每期結果頁只有號碼表與固定模板段落；翻譯他站文章當原創。

### 2.9 Better Ads 與廣告實作政策

Better Ads Standards 已是 Publisher Policies 的一部分；違規格式清單、行動版密度 30% 定義、2026-01-14 新增四類與 Chrome 執行狀態詳見 09 §7。2026-09-15 Chrome 在 CrUX 新增 Ad Count、Ad Density、Ad Weight 等實驗性廣告指標，官方說明不屬於 Core Web Vitals、沒有門檻，也未與 Better Ads 執行掛鉤（https://developer.chrome.com/blog/crux-ad-metrics ，查閱 2026-11-04）；可用來監控自己網站的實際廣告密度。

---

## 3. 版位與功能規範

### 3.1 Auto ads 格式與 2026 設定

**規範**：Auto ads 以 overlay 格式（Anchor、Vignette、Side rail）為基礎，in-page 格式（Banner、Multiplex）用 advanced settings 控制數量與間距；手動版位所在區域用 Excluded areas 排除，避免疊加。

**為什麼**：現行設定（https://support.google.com/adsense/answer/9305577 ，查閱 2026-11-04）：
- Intent-driven formats：Ad intents（links、anchors、chips 可分別關閉）。
- Overlay formats：Anchor ads、Vignette ads、Side rail ads；2025-05-20 起可選 anchor 位置（上、下、兩者）與 side rail 左右；2026-05-21 起可收合的 anchor 擴及寬度 > 1000px 的桌機，設定改名為 dynamic anchor ads。
- In-page formats：Banner ads、Multiplex ads。
- Banner advanced settings（2026-04-16 取代 ad load 滑桿，舊設定自動換算為近似值，官方建議檢查）：Maximum number of ads on a page、Minimum distance between ads on a page、Find more ad placements on article pages、Allow Google to optimize existing ads（https://support.google.com/adsense/answer/16683740 ，查閱 2026-11-04）。

**怎麼做**：
1. 內容站起手：Anchor（下方）+ Vignette + Side rail（桌機）開；Banner 開，Maximum number 先設保守值，Minimum distance 設大，Find more placements 先關；Multiplex 開於文末。
2. 手動版位的容器加 Excluded areas，或把手動版位放在 Auto ads 不會插入的位置。
3. 改設定後用 Auto ads 實驗跑 14 天比較（§4.3）。

**驗收方式**：行動版每屏最多 1 個 in-page 廣告；CLS < 0.1；Page RPM 不低於改動前。

**常見錯誤**：沿用 2026-04 前的 ad load 印象（滑桿已不存在）；Auto ads 全開又加 6 個手動版位；排除頁面時漏掉隱私權政策、聯絡頁等無內容頁。

### 3.2 Vignette 觸發條件與返回鍵

**規範**：檢查 Overlay formats → Advanced settings 的「Allow additional triggers for vignette ads」，依網站型態決定是否保留；不要用任何方式讓返回鍵觸發廣告或轉址。

**為什麼**（https://support.google.com/adsense/answer/16853623 與公告頁，查閱 2026-11-04）：
- 既有觸發：重新顯示分頁或視窗、點擊瀏覽器網址列（僅桌機）、在新分頁開同站頁面後切換過去。
- 新觸發（2026-03-09 未退出者自動開啟）：讀到主文章結尾後往上捲或停留（行動 5 秒 / 桌機 10 秒）、閒置 30 秒以上後再互動、按返回鍵。
- 因 Google 搜尋的 back button hijacking 垃圾政策（2026-06-15 起執行，詳見 07 §5.4），AdSense 自 2026-06-15 起返回鍵不再觸發 vignette。
- 關閉此設定也會關閉既有觸發條件。

**怎麼做**：一般內容站保留預設並觀察使用者回訪率；使用者常在同一頁等待更新的網站，「閒置 30 秒後互動」觸發可能讓體驗很差，建議用 Auto ads 實驗比較開與關。

**驗收方式**：手機實測一輪觸發情境；GA4 跳出率與回訪率無惡化。

**常見錯誤**：自製 history.pushState 攔截返回鍵顯示廣告（屬垃圾政策違規）。

### 3.3 手動廣告單元

**規範**：手動單元（display、in-feed、in-article、multiplex）放在主要內容區，容器預留高度；標籤只用「Advertisements」或「Sponsored Links」；與按鈕、下載鍵、導覽、播放鍵保持距離。

**為什麼**：版位政策要求小心放置於連結、播放、下載、導覽按鈕附近以免誤點；不得偽裝廣告或把旁邊內容做成像廣告；不得未經使用者要求重新整理頁面或元素（answer/1346295，查閱 2026-11-04）。

**怎麼做**：內容站配置與 CWV 預留尺寸見 09 §6、§7.2 與 15 §11.3。

**驗收方式**：Policy center 無 Confirmed Click 狀態；行動版密度 < 30%（目標 15–20%）。

**常見錯誤**：廣告貼著「下一期」「查看更多結果」按鈕；在結果自動更新時重新 push 廣告（屬自動重新整理）。

### 3.4 Ad balance、密度與內容廣告比例

- Ad balance 已於 2020-05-20 從所有帳號退場（Google 公告，ppc.land / Search Engine Roundtable 報導；是否所有帳號都已完成退場，現行官方頁無法確認，**待查證**）；現在控制數量的工具是 §3.1 的 advanced settings 與封鎖控制。
- 內容廣告比例：不得「more ads or paid promotional material than publisher-content」；空白、頁首頁尾、站內連結不算內容（https://support.google.com/publisherpolicies/answer/11169917 ，查閱 2026-11-04）。
- 「每頁 3 個廣告」上限 2016 年已取消；密度上限依 Better Ads（09 §7）。

### 3.5 Offerwall、Ad intents、Search ads

| 功能 | 重點（查閱 2026-11-04） | 建議 |
|---|---|---|
| Offerwall | 2026-04-13 於 Privacy & messaging 全面開放；使用者看獎勵廣告換取存取權（時數或頁數），可設頻率（https://support.google.com/adsense/answer/13866332）；Offerwall optimization：2025-12-10 起開關顯示 On，一個月檢視期內仍沿用手動頻率，未退出者 2026-01-10 起由它取代手動頻率（https://support.google.com/adsense/answer/16776170 ，查閱 2026-11-05） | 新聞、長文、工具頁可測；使用者急著看的資訊，不建議擋在 Offerwall 後 |
| Ad intents | 在內文產生 links、anchors、chips，點擊開啟含廣告及 Gemini 生成內容的對話框（2026-06-30 起自動加入 Gemini 生成內容）；歷史變更：2025-05-21 曾推出可選顯示 display 廣告（點擊以 AFC 分成計），現行說明頁未再提及；可用 `google-anno-skip` class 排除區塊（https://support.google.com/adsense/answer/13844047 ，查閱 2026-11-05） | 在號碼表、免責聲明、法務頁加 `google-anno-skip`；Gemini 內容可能與你的頁面重複資訊，觀察停留時間 |
| Search ads | 見 §1.9 | 內容站多半不需要 |

### 3.6 AMP、單頁應用、無限捲動、懶載入

- AMP：AdSense 仍提供 AMP 相容的 `amp-ad` 單元，預設 responsive（https://support.google.com/adsense/answer/9274230 ，查閱 2026-11-04）；AMP 與非 AMP 不混用同一段程式碼。
- 單頁應用（SPA，如 Astro View Transitions、Next.js 客戶端導覽）與無限捲動：**AdSense 官方說明未找到專文，待查證**。安全做法（社群共識）：每次使用者導覽到新內容時，插入新的 `<ins>` 再 push 一次；不得對既有單元計時重新整理（違反「未經使用者要求重新整理」）；無限捲動每段新內容要有足量文字再放廣告。Auto ads 在客戶端導覽後不一定重新掃描，SPA 站以手動單元為主較可控（社群共識）。
- 懶載入：官方警告初始隱藏的單元可能永遠不發出請求（https://support.google.com/adsense/answer/10762946 ，查閱 2026-11-04）；自行以 IntersectionObserver 在接近視窗時插入廣告碼屬社群做法，官方未明文支援（**待查證**），且不要用 `display:none` 先藏再顯示（09 §6）。

### 3.7 CWV 與 CSP

- CWV 與預留尺寸：詳見 09 §6、12 H3、15 §11.3，本章不重複。
- CSP：AdSense 只支援 strict CSP（每次請求產生 nonce + `'strict-dynamic'`），官方範例為 `object-src 'none'; script-src 'nonce-{random}' 'unsafe-inline' 'unsafe-eval' 'strict-dynamic' https: http:; base-uri 'none'; report-uri ...`；不支援網域白名單，建議先用 `Content-Security-Policy-Report-Only` 測試；CSP 是選用，但一旦使用就必須符合指引（https://support.google.com/adsense/answer/16283098 ，查閱 2026-11-04；範本見 15 §12）。Astro 靜態輸出要靠 主機的 PHP 層或 edge 產生 nonce，純靜態 HTML 無法每次產生新 nonce。

---

## 4. 收益優化

### 4.1 不違規就能拉高 RPM 的槓桿

**規範**：優先順序為「流量品質與國家組合 > 可視度 > 版位位置 > 廣告數量 > 封鎖控制」，每次只改一項並用實驗或前後 14 天比較。

**為什麼**：2024 年起發布者改按曝光收款，廣告主仍可能按點擊或轉換付費（§1.8）；官方未提供可視度、競價深度、CTR 的影響力排序，本節順序為經驗值；增加版位的邊際收益遞減且傷 CWV（09 §5.1）。

**怎麼做**：
1. 可視度：把首屏下第一個單元移到使用者一定會捲到的位置；sticky 側欄（桌機）；文末 multiplex。
2. Auto ads advanced settings 只微調一個值。
3. 內容端：提高 Tier 1 與高 CPC 主題比例（25 §5）；Q4 前補強購物、金融、保險、匯款類內容。
4. 開 CMP 與 Maximize message coverage，收回 EEA 個人化廣告（§2.6）。
5. 不做：放大廣告標籤、加箭頭、在內容中寫「點廣告支持我們」。

**驗收方式**：Page RPM、Active View viewable 上升，Page CTR 沒有異常飆高。

**常見錯誤**：同時改五個設定，無法判斷哪個有效；看到 CTR 下降就加廣告。

### 4.2 封鎖控制

| 控制 | 規則（查閱 2026-11-04） | 建議 |
|---|---|---|
| Advertiser URLs | 最多 500 個網址，封鎖頂層網域也封鎖其子目錄，24 小時內生效（https://support.google.com/adsense/answer/164657） | 只封鎖競爭對手、詐騙、明顯不當者 |
| Sensitive categories | §2.4 | Restricted 維持預設；Standard 只封品牌明顯衝突者 |
| Authorized Buyers | 2025-11-06 取代舊的 Ad networks 控制，新買方預設允許 | 不要整批封鎖 |
| Ad review center | 逐則檢視與封鎖廣告素材 | 收到使用者檢舉時用 |
| Share full IP address | 2026-06-01 起可把完整 IP 傳給所有需求來源 | 依隱私政策與法務判斷；開啟前更新隱私權政策 |

### 4.3 實驗與 Auto optimize

實驗類型：Auto ads experiments、Blocking controls experiments、Search style experiments（https://support.google.com/adsense/answer/45030 ，查閱 2026-11-04）；blocking controls 實驗一次只能跑一個。Auto optimize 2025-05-09 起可逐站設定，預設以 50% 流量測試（第三方整理，**待查證**現行比例）；可封鎖不想被測試的實驗類型（例如 vignette）。規則：實驗至少 14 天、避開月初月底與大型事件。

### 4.4 報表判讀

| 指標 | 定義與判讀 |
|---|---|
| Page RPM | 收益 ÷ 網頁瀏覽 × 1,000；比較網站與月份的主指標 |
| Impression RPM | 收益 ÷ 廣告曝光 × 1,000；看單一曝光價值，版位變多時常下降 |
| Active View viewable | 可視曝光比例；按曝光計費後與收益高度相關，目標 ≥ 60%（經驗值） |
| CPC / Page CTR | 官方未說明按曝光計費後兩者對收益的影響；廣告主仍可能按點擊或轉換付費（§1.8），本文當輔助指標看（經驗值）；CTR 突增要查無效流量（§5.1） |
| Ad requests / Coverage | 2026-06-23 起 Multiplex 格內每則廣告各算一次請求，請求數與涵蓋率會變，曝光與收益不受影響 |
| 已退場 | Ad sessions 等工作階段指標 2025-09-23 退場，改用 GA4 |
| 新增 | 2025-09-26 起報表可拆流量來源（直接流量與熱門平台） |

注意：2026-02-12 至 02-18 iOS 的 anchor 關閉鍵被隱藏，官方承認該期間 CTR 暫時偏高（公告頁，查閱 2026-11-04）；比較歷史資料時排除此區間。

### 4.6 何時轉向 Ad Manager / MCM / 其他聯播網

門檻與路徑見 09 §4。判斷原則（經驗值）：月瀏覽數穩定在 30 萬以上、有 Tier 1 流量或想接直售與 header bidding 時，評估 GAM + MCM 夥伴；Tier 1 premium sessions 達標時申請 Journey。轉換前保留 AdSense 帳號良好狀態，MCM 夥伴審核會看帳號歷史。

---

## 5. 無效流量與帳號安全

### 5.1 無效流量來源與預防

**規範**：自己與團隊不點廣告；開發、測試、內部裝置不載入廣告碼；每日看 Page CTR 與國家分布；發現可疑流量主動通報。

**為什麼**：無效流量指可能人為提高廣告主成本或發布者收益的點擊與曝光，含蓄意與意外；來源包括發布者點自己的廣告、同一或多位使用者重複點擊或曝光、鼓勵點擊、機器人與欺騙性軟體；**即使是第三方在你不知情下造成，責任仍在發布者**（https://support.google.com/adsense/answer/16737 ，查閱 2026-11-04）。懷疑有可疑點擊時用 Invalid clicks contact form 通報，但不需要每次誤點自己的廣告都回報（https://support.google.com/adsense/answer/1348754 ，查閱 2026-11-04）。

**怎麼做**：環境變數控制只在正式網域輸出廣告碼；內部 IP 與登入的編輯帳號不輸出；Cloudflare bot 管理封鎖資料中心 ASN 的異常流量；GA4 建立「單一國家 CTR × 3」告警（13 §13.9）。

**驗收方式**：報表無「Invalid traffic」扣款列；Page CTR 穩定在自家歷史基線內。

**常見錯誤**：在手機上反覆刷自己的網站頁面；讓家人「幫忙看看廣告」；購買 Traffic Exchange 流量衝數字。

### 5.2 廣告放送限制（Ad serving limits）

官方說明：限制可能是「while we get to know you and evaluate your traffic quality」的暫時評估，或因無效流量疑慮；系統自動檢討，「can't say how long this will take」，通常影響少於 30 天，部分案例更久；帳號仍可登入，Policy center 有細節（https://support.google.com/adsense/answer/9437976 ，查閱 2026-11-04）。Policy center 另有「Limited ad serving」狀態（https://support.google.com/adsense/answer/11066888 ，查閱 2026-11-04）。處理見 §6 P10。

### 5.3 扣款、暫時停用、永久停用與申訴

| 狀態 | 官方規則（查閱 2026-11-04） | 可否申訴 |
|---|---|---|
| 無效流量扣款 | 每月 3 日結算時扣除，部分扣款不會逐項列出（answer/7164703） | 不可，只能改善流量 |
| 暫時停用（suspension） | 分政策違規與無效流量兩類，期間寫在通知信；廣告停止、網站審核暫停、自動付款暫停；期間發現新問題可提前關閉（https://support.google.com/adsense/answer/2659114） | 「account suspensions are unappealable」 |
| 永久停用（disabled，無效流量） | 30 天款項暫扣，之後可領未判定無效的部分；用 invalid activity appeal form 申訴，須說明非自己或負責之人造成；決定後「further appeals may not be considered」；駁回後不得再參加 AdSense；復權後最多 48 小時恢復放送（https://support.google.com/adsense/answer/57153） | 可，實務上只有一次實質機會 |

**申訴成功率因素**（社群共識，Google 未公布成功率）：能提出具體證據（伺服器日誌、異常 IP / ASN、referrer、時間點）指出第三方來源；已採取的技術措施（封鎖、移除付費流量、內部不載入廣告碼）；帳號歷史乾淨。只寫「我沒有點」的申訴幾乎都被駁回。

### 5.4 流量來源與付費導流（arbitrage）

**規範**：不買點擊型、自動瀏覽、交換、彈窗與推播流量；付費社群或搜尋廣告只導向內容充足、廣告少的頁面；**不以「買流量 → 賺廣告差價」為商業模式**。

**為什麼**：
- 計畫政策禁止 PTC、autosurf、click-exchange、垃圾郵件、軟體觸發的彈窗或轉址；接收付費廣告流量的網站須符合 Landing Page Quality 精神（answer/48182）。
- 廣告主端：Google Ads 的 Insufficient original content 政策把「以 arbitrage 等方式導流到廣告多於原創內容、幾乎沒有原創內容或廣告過多的目的地」列為拒登例子（https://support.google.com/adspolicy/answer/16427718 ，查閱 2026-11-04）；用 Google Ads 導流到 AdSense 頁同時受兩邊政策約束。
- AFS：流量從你可控制的來源（含合作聯播網、服務或聯盟）進入 Related search for content pages 時，須傳 referrerAdCreative（§1.9）。

**怎麼做**：社群自然分享（Facebook 社團、Messenger）可以；FB / TikTok 廣告推內容頁時，到達頁廣告密度降到最低、關閉 vignette 測試；每個付費活動用 UTM 並在 AdSense 報表比對該期間 CTR 與無效流量扣款。

**驗收方式**：付費活動期間 Page CTR 不高於自然流量基線 2 倍（經驗值）；無扣款。

**常見錯誤**：買低價流量到滿版廣告頁；使用彈窗聯播網的流量交換。

### 5.5 帳號安全

用專屬 Google 帳號、開兩步驟驗證（Passkey 或安全金鑰）；Account → Access and authorization 用最小權限加使用者，離職立即移除；不要把 AdSense 帳號借給他人的網站使用（同一 pub ID 出現在不合規網站會連帶處置）；定期看 Sites 頁是否出現陌生網域（他人盜用你的廣告碼時，在 Sites 頁停用該網站的廣告放送）。

---

## 6. 問題排解（P1–P29）

每個狀況用第 12 章固定結構。證據等級：Google 官方證實 / 社群共識 / 個人經驗。恢復時間未有官方數字者為社群共識，使用前依專案實況調整。

| 類別 | 編號 |
|---|---|
| 申請與審核 | P1–P6、P26、P29（不支援語言見 25 §2） |
| ads.txt 與放送 | P7–P10、P22、P23 |
| 政策與處置 | P11–P15、P27、P28 |
| 帳號、驗證、付款、稅務 | P16–P19 |
| 收益與數據 | P20、P21、P24、P25 |

### P1. 申請被拒：Low value content

- **症狀**：Sites 頁 Needs attention，原因為 Low value content；或 Policy center 顯示 Valuable inventory 類問題。
- **可能原因**：(1) 薄內容、同模板大量頁；(2) AI 量產未審；(3) 改寫或翻譯他站；(4) 聯盟頁占多數；(5) 索引率低，Google 看到的內容太少。
- **診斷步驟**：GSC 比對已索引頁 vs 總頁；用 05 §14 評分表抽 10 篇；統計聯盟頁、模板頁比例；確認有作者與編輯政策。
- **解法**：刪除或合併薄頁、空分類；程序化頁補獨有資料（§2.8）；補到 20–30 篇實質原創文章（經驗值）；修正後至少等 1–2 週再送，不要原樣反覆重送。
- **預防**：先做內容再申請；新站上線即依 11 的品質門檻控管。
- **預估恢復時間**：重送後數天到 2–4 週回覆（官方）；內容真的不足時常需 1–3 個月補內容（社群共識）。
- **證據等級**：Google 官方證實（拒絕類別、無數量門檻）；篇數與時程為社群共識。

### P2. 申請被拒或停止放送：Site down or unavailable

- **症狀**：審核結果為 Site down or unavailable，或報表出現爬蟲錯誤。
- **可能原因**：主機慢或當機；WAF / Cloudflare 擋 AdSense 爬蟲；robots.txt 封鎖；地區或 IP 限制；登入牆；多重轉址；需 POST 才能看到內容；DNS 問題（https://support.google.com/adsense/answer/10035 ，查閱 2026-11-04）。
- **診斷步驟**：從海外節點 curl 首頁與文章；查 WAF 日誌中 Mediapartners-Google；檢查 robots.txt；確認 `example.com` 到正式網址只有一次轉址。
- **解法**：允許 AdSense 爬蟲通過 WAF；移除地區封鎖；修轉址鏈；換穩定主機。
- **預防**：上線檢查清單加入「AdSense 爬蟲可存取」；Cloudflare 新規則先用 log 模式。
- **預估恢復時間**：修好後重送，數天到 2–4 週（官方審核時程）。
- **證據等級**：Google 官方證實。

### P3. Policy violations：Valuable inventory: No content

- **症狀**：Policy center 或審核結果指出無內容畫面上有廣告。
- **可能原因**：廣告出現在感謝頁、錯誤頁、登入頁、搜尋結果空頁、純導覽頁；Auto ads 插到這些頁面。
- **診斷步驟**：Policy center 看被點名的 URL；檢查 Auto ads 的 Excluded pages。
- **解法**：這些頁面不輸出廣告碼或加入 Excluded pages；修正後 Request review。
- **預防**：模板層建立「可放廣告頁型」白名單。
- **預估恢復時間**：審查通過後 1–2 天恢復（社群共識）。
- **證據等級**：Google 官方證實（answer/11112688）。

### P4. Policy violations：Valuable inventory: Under construction

- **症狀**：審核被拒，原因為網站建構中或內容不足。
- **可能原因**：空分類、「coming soon」、只有程式碼的測試頁、首頁只有佔位文字。
- **診斷步驟**：爬全站找字數極少的頁；檢查導覽中的空分類。
- **解法**：隱藏或 noindex 空分類；首頁放實質內容。
- **預防**：分類在有 ≥ 3 篇內容時才進選單。
- **預估恢復時間**：修完重送，數天到 2–4 週（官方審核時程）。
- **證據等級**：Google 官方證實（Insufficient content，answer/81904）。

### P5. Policy violations：Valuable inventory: Screen-scraped / replicated content

- **症狀**：審核或 Policy center 指出複製或爬取內容。
- **可能原因**：轉貼新聞稿、RSS 全文聚合、翻譯他站、嵌入他站影片為主、同義詞改寫。
- **診斷步驟**：抽 20 段文字搜尋原句；統計外部嵌入比例。
- **解法**：移除或改寫為原創分析；轉載只摘要並加評論；被點名頁先移除廣告碼再申請審查。
- **預防**：AI 產線禁止「改寫他站」任務；保留素材來源紀錄。
- **預估恢復時間**：1–4 週（社群共識）。
- **證據等級**：Google 官方證實（answer/11190248）。

### P6. Getting ready 卡很久

- **症狀**：狀態停在 Getting ready 超過 4 週。
- **可能原因**：帳號設定未完成（付款資料、身分驗證）；程式碼未偵測到；網站流量太少、爬蟲資料不足；系統排隊。
- **診斷步驟**：Home 頁看是否有未完成任務；檢視原始碼確認 `<head>` 有程式碼；確認爬蟲可存取（P2）。
- **解法**：完成所有帳號任務；確認連結方式有效；**不要移除再重送**（官方明言會延誤）；超過 4 週可到 AdSense 社群發文附網址詢問（社群共識）。
- **預防**：申請前完成付款資料與身分驗證準備。
- **預估恢復時間**：官方為數天到 2–4 週；部分案例更久（社群共識）。
- **證據等級**：Google 官方證實（狀態定義與勿重送）；超過 4 週的處理為社群共識。

### P7. ads.txt「Earnings at risk」或 Unauthorized

- **症狀**：後台頂端警示要求修正 ads.txt；Sites 頁 ads.txt 為 Unauthorized。
- **可能原因**：檔案沒有你的 pub ID；pub ID 打錯；改用其他聯播網時覆蓋掉 Google 列。
- **診斷步驟**：瀏覽器開 `https://根網域/ads.txt`；比對後台 pub ID。
- **解法**：加入 `google.com, pub-…, DIRECT, f08c47fec0942fa0`；按 Check for updates。
- **預防**：部署流程鎖定 ads.txt，不被建置覆蓋。
- **預估恢復時間**：數天，流量少的網站最長約 1 個月（官方）。
- **證據等級**：Google 官方證實。

### P8. ads.txt Not found 或格式錯誤

- **症狀**：狀態 Not found；檔案存在但未被驗證。
- **可能原因**：放在子目錄或子網域；回應 404 / 403 / 軟 404；轉址跨出原根網域超過一次；robots.txt 擋；非 UTF-8 或含全形字元；只在 HTTPS 可存取。
- **診斷步驟**：`curl -IL http://example.com/ads.txt` 與 https 版本，看狀態碼與每一段轉址的目的地；十六進位檢查 BOM。
- **解法**：放在根網域、回 200、純文字；導向原始根網域以外最多一次 HTTP 轉址，同根網域內可多次；修 robots.txt。
- **預防**：監控工具每日檢查 `/ads.txt` 回應碼。
- **預估恢復時間**：數天到 1 個月（官方）。
- **證據等級**：Google 官方證實（answer/7679060、9785052，查閱 2026-11-05）。

### P9. 廣告不顯示或空白

- **症狀**：版位空白、只有預留空間；新網站核准後仍無廣告。
- **可能原因**：網站未 Ready；帳號在 Ad serving limit；頁面受 Publisher restriction；新頁尚未被爬（官方說新頁可能有幾分鐘低廣告量）；容器初始隱藏；CSP 擋腳本；廣告攔截器；EEA 無同意。
- **診斷步驟**：Sites 與 Policy center 狀態；DevTools Console 看 CSP 或 `adsbygoogle` 錯誤；無痕、關攔截器、不同國家測試。
- **解法**：依原因處理；修 CSP 為 strict（§3.7）；不要用 `display:none` 先藏廣告。
- **預防**：上線前用測試頁確認廣告請求成功。
- **預估恢復時間**：設定問題修正後數分鐘到 48 小時（社群共識）。
- **證據等級**：Google 官方證實（爬蟲與隱藏單元說明）；部分為社群共識。

### P10. 廣告放送受限（Ad serving limited）

- **症狀**：後台橫幅顯示廣告放送受限；曝光大減但帳號正常。
- **可能原因**：新帳號評估期；流量品質疑慮（無效流量比例高、來源異常）。
- **診斷步驟**：Policy center 看原因；報表拆流量來源與國家；GA4 看是否有異常 referrer。
- **解法**：繼續正常經營與累積自然流量；停掉所有付費與可疑流量；封鎖 bot；不要為了測試一直重新整理自己的頁。
- **預防**：新站前 1–2 個月只靠自然流量（經驗值）。
- **預估恢復時間**：通常少於 30 天，部分更久，系統自動解除（官方）。
- **證據等級**：Google 官方證實。

### P11. 無效流量扣款

- **症狀**：月結收益明顯少於預估；明細出現 Invalid traffic 扣款。
- **可能原因**：自點、bot、付費低品質流量、點擊轟炸、版面誤點。
- **診斷步驟**：找 CTR 異常的日期、國家、頁面；對照伺服器日誌的 IP / ASN / UA；檢查是否在付費活動期間。
- **解法**：停可疑流量；封鎖來源；修誤點版面；用 Invalid clicks contact form 通報第三方攻擊。
- **預防**：§5.1 全部；每日 CTR 告警。
- **預估恢復時間**：扣款不退；改善後下個月起正常（社群共識）。
- **證據等級**：Google 官方證實（扣款機制與責任歸屬）。

### P12. 帳號暫時停用或永久停用

- **症狀**：收到 suspended 或 disabled 通知；廣告全部停止。
- **可能原因**：累積無效流量；重複或嚴重政策違規；關聯帳號被停用。
- **診斷步驟**：讀通知判斷是「暫時停用（有期間）」還是「永久停用」；查原因類別。
- **解法**：暫時停用：不能申訴，期間修正問題並等待；永久停用：在 30 天款項暫扣期內備妥證據，用 invalid activity appeal form 一次寫完整（來源、措施、數據）。
- **預防**：§5 全部。
- **預估恢復時間**：暫時停用依通知期間；永久停用申訴多數不成功，復權後最多 48 小時恢復放送（官方）。
- **證據等級**：Google 官方證實（流程）；成功率為社群共識。

### P13. Policy center：Policy issue、Ad serving disabled、Restricted ad serving

- **症狀**：Policy center 出現 Policy issue，狀態為 Ad serving disabled、Restricted ad serving 或 Ad serving at risk（有執行日期）。
- **可能原因**：內容政策違規（成人、危險、不實、版權）；行為政策（廣告空間價值、不支援語言）；UGC 留言區。
- **診斷步驟**：Fix → Issue details 看頁面與原因；分頁層級與網站層級（answer/11066888）。
- **解法**：修正或移除違規內容；或移除該頁廣告碼（7–10 天後從 Policy center 消失，不需審查）；修完後 Start review process → Request review，每個網站各自申請。
- **預防**：每週看 Policy center；UGC 預設審核。
- **預估恢復時間**：審查數天到數週；多次被駁回會暫時無法再申請（官方未給天數）。
- **證據等級**：Google 官方證實（https://support.google.com/adsense/answer/7003627）。

### P14. Publisher restrictions 造成限制放送

- **症狀**：Policy center 顯示 Restricted ad serving，類別為 Online gambling、Alcohol、Shocking content 等；RPM 遠低於同類頁。
- **可能原因**：內容屬受限類別或被自動分類；頁面含酒類販售、投注聯盟連結。
- **診斷步驟**：確認類別與 URL；對照 §2 定義。
- **解法**：受限屬實：不需修正（非必改），但可把受限內容與一般內容分頁；判斷錯誤：申請審查並說明。
- **預防**：受限主題獨立分類；不混放投注 CTA。
- **預估恢復時間**：審查數天到數週（社群共識）。
- **證據等級**：Google 官方證實（受限不需修正但放送受限）。

### P15. CMP / 同意訊息問題導致 EEA 收益下降

- **症狀**：EEA / UK 收益驟降；Policy center 出現 Regulatory issue 或 Restricted ad personalization；TCF 錯誤碼。
- **可能原因**：第三方 CMP 未升級 TCF v2.3（2026-03-01 起）；Disclosed vendors 缺 Google（錯誤 1.4）；CMP 故障沒送 TC string；同意前就載入廣告。
- **診斷步驟**：Policy center → Regulatory issue 的 TCF 錯誤；用 EEA IP 開頁檢查 `__tcfapi`。
- **解法**：升級 CMP 或改用 Google CMP；開 Maximize message coverage；修正 vendor 清單。
- **預防**：CMP 版本列入季度檢查（14 §F）。
- **預估恢復時間**：修正後數天（社群共識）。
- **證據等級**：Google 官方證實（AdSense 公告 2026-03-02、2026-09-11、2026-10-15）。

### P16. PIN 收不到

- **症狀**：達 USD 10 後 3 週以上未收到 PIN 信。
- **可能原因**：地址格式錯、郵局投遞失敗、搬家、信件被丟棄。
- **診斷步驟**：Payments → 地址是否正確完整、與帳號國家相符；PIN 產生日期（4 個月期限）。
- **解法**：修正地址後申請補寄；第 4 次補寄 3 週仍未到，用 PIN troubleshooter；4 個月期限前一定要處理。
- **預防**：用可靠收件地址，信箱貼姓名。
- **預估恢復時間**：每次寄送約 3 週（官方）。
- **證據等級**：Google 官方證實（answer/157667）。

### P17. 身分驗證失敗

- **症狀**：驗證被拒、次數用完，或 45 天期限將到。
- **可能原因**：照片模糊反光、證件過期、證件國家與付款資料不同、姓名不一致。
- **診斷步驟**：比對付款資料與證件姓名、國家。
- **解法**：修正付款資料後重新開始；次數用完用 identity verification contact form。
- **預防**：開戶時就用證件上的正式姓名。
- **預估恢復時間**：線上驗證約 10 分鐘；PIN 方式 2–4 週（官方）。
- **證據等級**：Google 官方證實（answer/11608017）。

### P18. 付款被暫停（Payment hold）

- **症狀**：達 USD 100 但 21–26 日未付款；Payments 頁有暫停說明。
- **可能原因**：身分或地址未驗證；未選付款方式；稅務資訊未提交或被拒；帳號暫停或停用；20 日後才改資料。
- **診斷步驟**：Payments 頁逐項看暫停原因。
- **解法**：在每月 20 日前解除所有暫停；電匯資料（SWIFT、帳戶名）與付款資料一致。
- **預防**：每月 15 日例行檢查 Payments 頁。
- **預估恢復時間**：在當月 20 日或之前解除暫停、餘額達門檻並符合條件，當月 21–26 日付款；20 日後解除順延到下月週期（官方，answer/7164703，查閱 2026-11-05）。
- **證據等級**：Google 官方證實（answer/7164703）。

### P19. 稅務資訊問題

- **症狀**：Tax info 狀態 Action Required 或 Declined；付款出現扣繳。
- **可能原因**：表單選錯（W-9 / W-8BEN / W-8BEN-E）；未填 TIN 卻主張協定；姓名不一致；上傳文件模糊或過期。
- **診斷步驟**：看 Declined 原因；比對姓名與地址。
- **解法**：回答後台稅務問題重新判定表單（W-9 適用美國人士；W-8BEN、W-8BEN-E 分別適用符合條件的非美國個人、實體；另有 W-8ECI 等）；需要 TRC 時向當地稅務機關申請；台灣當地申報找會計師。
- **預防**：開戶當月就完成稅務資訊。
- **預估恢復時間**：文件審查最長 7 個工作天（官方）。
- **證據等級**：Google 官方證實（answer/14131950、1322037；扣繳率見 paymentscenter answer/10349995，查閱 2026-11-05）。

### P20. 收益驟降

- **症狀**：Page RPM 或總收益單週下跌 30% 以上。
- **可能原因**（依機率）：季節（1 月、農曆年後）；流量國家組合改變；Policy center 新處置；TCF / CMP 問題；Auto ads 設定改變（2026-04-16 ad load 換算、vignette 觸發變更）；Chrome Better Ads 過濾；報表定義改變（2026-06-23 Multiplex 請求計算）。
- **診斷步驟**：先確認 GA4 流量是否同跌；再看國家、裝置、廣告格式報表；Policy center；GSC Ad Experience Report；AdSense 公告頁同期變更。
- **解法**：對症處理；季節性不需動站。
- **預防**：每月 RPM 矩陣（09 §5）；訂閱 AdSense 公告。
- **預估恢復時間**：設定或政策問題修正後數天；季節性依月份（社群共識）。
- **證據等級**：社群共識（診斷順序）；個別變更日期為 Google 官方證實。

### P21. RPM 太低

- **症狀**：Page RPM 長期低於同市場經驗值（見 09 §5）。
- **可能原因**：流量以低 CPC 國家為主；主題低價；可視度低；版位都在無人捲到的位置；封鎖過多；Restricted ad serving。
- **診斷步驟**：國家報表；Active View；封鎖控制清單；Policy center。
- **解法**：§4.1 的順序調整；增加高 CPC 主題；評估 GAM + MCM（09 §4）。
- **預防**：選題階段就評估 RPM（02、09 §5）。
- **預估恢復時間**：版位調整 2–4 週見效；內容結構調整 3–6 個月（社群共識）。
- **證據等級**：社群共識。

### P22. Auto ads 不出現

- **症狀**：開了 Auto ads 但頁面沒有廣告或只有 anchor。
- **可能原因**：程式碼未放在所有頁；頁面被列入 Excluded pages；內容太短沒有合適位置；Maximum number 設太低；SPA 客戶端導覽後未重新掃描；Auto ads 剛開啟需時間。
- **診斷步驟**：檢查每個模板的 `<head>`；Ads → By site 設定與後台預覽；確認 Excluded pages 與 advanced settings 的值。
- **解法**：補程式碼；調整 advanced settings；SPA 改用手動單元（§3.6）。
- **預防**：改模板後檢查程式碼輸出。
- **預估恢復時間**：設定後數小時到 1 天（社群共識）。
- **證據等級**：社群共識。

### P23. Auto ads 太多、版面混亂或 vignette 過頻

- **症狀**：手機一屏兩個以上廣告；使用者抱怨插頁太多；CLS 變差。
- **可能原因**：Find more ad placements 開啟；Maximum number 偏高；手動單元與 Auto ads 疊加；新 vignette 觸發 2026-03-09 自動開啟。
- **診斷步驟**：Auto ads 預覽；行動版實測；看 vignette 設定。
- **解法**：降低 Maximum number、加大 Minimum distance；手動區域加 Excluded areas；評估關閉「Allow additional triggers for vignette ads」。
- **預防**：每次 AdSense 公告新格式時檢查是否自動啟用。
- **預估恢復時間**：設定變更即時到數小時（社群共識）。
- **證據等級**：Google 官方證實（設定項目）；體驗判斷為個人經驗。

### P24. CLS 被廣告拖累

詳見 12 H3（症狀、原因、診斷、解法完整版）。本章補充：2026-05-21 起 dynamic anchor 擴及桌機，若自製 sticky 與 Google anchor 並存要擇一；Auto ads 的 Banner 可用 Excluded areas 禁止插入首屏。證據等級：Google 官方證實。

### P25. Search Console 與 AdSense 流量數字對不起來

- **症狀**：GSC 點擊、GA4 工作階段、AdSense 網頁瀏覽三者差很多。
- **可能原因**：定義不同（GSC 只算 Google 搜尋點擊；AdSense 只算有廣告碼且發出請求的網頁瀏覽）；廣告攔截器；同意拒絕；非 Google 流量；AMP 或快取頁；部分頁未放廣告碼；bot 被 AdSense 過濾。
- **診斷步驟**：同一日期、同一頁比較；AdSense 報表依網址維度；GA4 篩 Organic Search。
- **解法**：不追求一致，追蹤比例是否穩定；比例突變才調查（可能是程式碼遺失或 bot）。
- **預防**：13 章監測儀表板固定三者比例。
- **預估恢復時間**：不適用。
- **證據等級**：社群共識（GA4 與 AdSense 差異 15% 內為經驗值）。

### P26. 子網域或新網站加入

- **症狀**：新網站無法新增、子網域不能新增、新網站卡審核。
- **可能原因**：嘗試把子網域當網站新增（2023-03 後不支援）；新網域需獨立審核。
- **診斷步驟**：確認是網域、PSL 子網域或平台夥伴網站（§1.4）。
- **解法**：子網域直接放同一程式碼；新網域走 §1.2 流程。
- **預防**：多語言或多市場優先用子目錄（10 §1）。
- **預估恢復時間**：新網域審核數天到 2–4 週（官方）。
- **證據等級**：Google 官方證實（answer/12170421）。

### P27. 版權投訴（DMCA）

- **症狀**：收到 Google 轉來的著作權通知；Policy center 出現 Intellectual property abuse；頁面被停用廣告。
- **可能原因**：使用未授權圖片、影片、PDF、轉載文章；UGC 上傳盜版；嵌入盜版影片。
- **診斷步驟**：查通知中的 URL 與權利人；檢查素材授權紀錄。
- **解法**：移除侵權素材；若確有授權，透過 Google 法律移除流程提出反通知（https://support.google.com/legal/answer/3110420 ，查閱 2026-11-04）；修正後在 Policy center 申請審查。
- **預防**：圖片只用自製、授權或官方提供素材並保存授權紀錄。
- **預估恢復時間**：移除後審查數天到數週（社群共識）。
- **證據等級**：Google 官方證實（智慧財產權濫用政策）；流程時程為社群共識。

### P28. 成人或賭博內容被誤判

- **症狀**：健康衛教、藝術、賭博相關資訊頁被標為 Sexual content 或 Online gambling。
- **可能原因**：關鍵字與圖片被自動分類；頁面有博弈廣告橫幅或聯盟連結；UGC 留言。
- **診斷步驟**：確認標記是 Policy issue（必改）還是 Publisher restriction（非必改）；對照 §2 定義逐條檢查頁面。
- **解法**：移除可能觸發的元素（投注連結、聳動圖片）；Request review 時說明頁面性質。若只是 Online gambling 受限，且目標市場在例外國家，當地使用者本來就不受限，可評估是否值得申請。
- **預防**：賭博相關資訊頁固定加「18+、僅供資訊」的說明區（不放在廣告旁）；成人相關衛教用中性用語與圖片。
- **預估恢復時間**：審查數天到數週（社群共識）。
- **證據等級**：Google 官方證實（定義與國家例外）；誤判處理為社群共識。

### P29. 重複帳號（Duplicate account）

- **症狀**：申請被拒，原因為已有帳號。
- **可能原因**：同一人、同一付款資料曾開過帳號（含 YouTube 建立的 AdSense 帳號）。
- **診斷步驟**：用所有 Google 帳號登入 AdSense 查找。
- **解法**：關閉重複帳號並在主帳號確認，網站改加到主帳號（answer/81904）。
- **預防**：全公司只用一個帳號管理所有網站。
- **預估恢復時間**：關閉後重新申請，數天到數週（社群共識）。
- **證據等級**：Google 官方證實。

## 7. 本章檢查清單

- [ ] 申請人 18 歲以上；全公司只有一個 AdSense 帳號（§1.1）。
- [ ] 網站主要語言在支援清單內（§1.1）。
- [ ] Privacy Policy 已上線且含 Google 與第三方 cookie 揭露（官方要求）；About、Contact、Terms、Editorial Policy 依網站經營建議備妥（§1.1）。
- [ ] 無空分類、無建置中頁、無自動產生未審內容、聯盟頁為少數（§2.8）。
- [ ] AdSense 爬蟲可從任何地區存取；robots.txt、WAF 不擋（P2）。
- [ ] 連結方式擇一完成；Getting ready 期間不重送（§1.2）。
- [ ] 付款資料姓名與證件一致；身分驗證於 45 天內完成；PIN 地址可收信（§1.5）。
- [ ] 台灣帳號已設定付款方式（官方可用支票、電匯；本文建議電匯）；每月 20 日前無付款暫停（§1.6）。
- [ ] 後台要求提交美國稅務資訊時，適用表單狀態 Accepted；當地稅務已諮詢會計師（§1.7）。
- [ ] `ads.txt` 在根網域、200、純文字、Authorized（§2.7）。
- [ ] EEA / UK / 瑞士：認證 CMP、TCF v2.3、Maximize message coverage；美國：US state regulations 訊息（§2.6）。
- [ ] 賭博相關頁無投注 CTA 與聯盟連結；Gambling & Betting (18+) 類別設定有紀錄（§2）。
- [ ] Auto ads advanced settings 已檢查（2026-04-16 換算值）；vignette 額外觸發已決定開或關（§3.1–§3.2）。
- [ ] 廣告標籤僅用 Advertisements / Sponsored Links；無自動重新整理；與按鈕保持距離（§3.3）。
- [ ] 使用 CSP 時為 strict CSP（§3.7）。
- [ ] 每週看 Policy center；每月看 AdSense 公告與政策變更紀錄（§2.1）。
- [ ] 開發與內部環境不輸出廣告碼；每日 CTR 告警；無購買點擊型流量（§5）。
- [ ] Google 帳號開兩步驟驗證；使用者權限最小化；Sites 頁無陌生網域（§5.5）。

## 8. 參考來源

（查閱日期皆為 2026-11-04；標 2026-11-05 者為本次複查或新增）

**帳號、申請、付款、稅務**
- AdSense Help — Eligibility requirements：https://support.google.com/adsense/answer/9724（查閱 2026-11-05）
- AdSense Help — Supported languages：https://support.google.com/adsense/answer/9727
- AdSense Help — Your AdSense account wasn't approved（拒絕原因、重複帳號、不支援語言）：https://support.google.com/adsense/answer/81904
- AdSense Help — Connect your site to AdSense（AdSense code snippet、Ads.txt code snippet、Meta tag）：https://support.google.com/adsense/answer/7584263（查閱 2026-11-05）
- AdSense Help — What to do when your site is not ready to show ads（Search Console 所有權替代方式）：https://support.google.com/adsense/answer/12176698（查閱 2026-11-05）
- AdSense Help — Site status / ads.txt status：https://support.google.com/adsense/answer/12170222
- AdSense Help — Sites（網域、PSL 子網域、平台夥伴）：https://support.google.com/adsense/answer/12170421
- AdSense Help — Fix AdSense crawler issues：https://support.google.com/adsense/answer/10035
- AdSense Help — Thresholds（身分 USD 0 依所在地而定、地址 USD 10、付款 USD 100）：https://support.google.com/adsense/answer/1709871（查閱 2026-11-05）
- AdSense Help — Verify your identity（45 天、Persona）：https://support.google.com/adsense/answer/11608017
- AdSense Help — PIN verification（3 週、4 個月）：https://support.google.com/adsense/answer/157667
- AdSense Help — How to request a replacement PIN（地址要求、當地語言文字）：https://support.google.com/adsense/answer/1348257（查閱 2026-11-05）
- Search Engine Roundtable — Google AdSense Drops Identity Verification Threshold To $0（2026-09-23）：https://www.seroundtable.com/google-adsense-identity-verification-threshold-42143.html
- AdSense Help — Payment timelines：https://support.google.com/adsense/answer/7164703（查閱 2026-11-05）
- AdSense Help — Forms of payment by location：https://support.google.com/adsense/answer/1714397（查閱 2026-11-05）
- AdSense Help — Contracting entity is Google LLC（美國稅表、TIN）：https://support.google.com/adsense/answer/1322037（查閱 2026-11-05）
- AdSense Help — Submit your US tax info to Google：https://support.google.com/adsense/answer/2490070（查閱 2026-11-05）
- Google Payments Center Help — US tax information reporting & withholding（預設扣繳率）：https://support.google.com/paymentscenter/answer/10349995（查閱 2026-11-05）
- AdSense Help — Tax information（新加坡、TRC）：https://support.google.com/adsense/answer/14131950
- AdSense Help — Revenue share：https://support.google.com/adsense/answer/180195
- Google Blog — Evolving how publishers monetize with AdSense（2023-11）：https://blog.google/products/adsense/evolving-how-publishers-monetize-with-adsense/（查閱 2026-11-05）
- 公視新聞 — 財政部網紅營業稅作業規範（2025-09）：https://news.pts.org.tw/article/770049
- 數位時代 — 網紅稅報導：https://www.bnext.com.tw/article/84444/influencer-tax-taiwan-revenue

**政策**
- AdSense Program policies：https://support.google.com/adsense/answer/48182（查閱 2026-11-05）
- AdSense Help — Policies for ad units that offer rewards：https://support.google.com/adsense/answer/9121589（查閱 2026-11-05）
- AdSense Help — Ad placement policies：https://support.google.com/adsense/answer/1346295
- AdSense policy change log：https://support.google.com/adsense/answer/9336650（查閱 2026-11-05）
- AdSense Announcements：https://support.google.com/adsense/announcements/9189068
- AdSense Help — Policy center 標籤更新（2025-04-22，Must fix 改為三類標籤）：https://support.google.com/adsense/answer/15918799（查閱 2026-11-05）
- Google Publisher Policies：https://support.google.com/publisherpolicies/answer/10502938（查閱 2026-11-05）
- Google Publisher Restrictions（Online gambling 例外國家）：https://support.google.com/publisherpolicies/answer/10437795
- Google Publisher Policies change log：https://support.google.com/publisherpolicies/answer/10852414
- Publisher Policies — Ads on screens without publisher-content：https://support.google.com/publisherpolicies/answer/11112688
- Publisher Policies — Replicated content：https://support.google.com/publisherpolicies/answer/11190248
- Publisher Policies — More ads than publisher-content：https://support.google.com/publisherpolicies/answer/11169917
- Google Ads Policy — Gambling and games（台灣）：https://support.google.com/adspolicy/answer/6018017、https://support.google.com/adspolicy/answer/15132179（查閱 2026-11-05）
- Authorized Buyers Help — Release notes（2026-08-10 預告、2026-08-24 賭博政策更新）：https://support.google.com/authorizedbuyers/answer/16818027（查閱 2026-11-05）
- Authorized Buyers Help — Policy（賭博允許國家清單）：https://support.google.com/authorizedbuyers/answer/7450776（查閱 2026-11-05）
- Google Ads Policy — Insufficient original content（arbitrage）：https://support.google.com/adspolicy/answer/16427718
- ppc.land — Google drops certification for gambling ads in 37 markets on Authorized Buyers（第三方；寫 2026-08-10 生效、37 市場，與官方 2026-08-24、國家表不同，以官方為準，查閱 2026-11-05）：https://ppc.land/google-drops-certification-for-gambling-ads-in-37-markets-on-authorized-buyers/
- AdSense Help — Sensitive categories：https://support.google.com/adsense/answer/164131
- AdSense Help — EU user consent / 認證 CMP：https://support.google.com/adsense/answer/13554116（查閱 2026-11-05）
- AdSense Help — US state regulations messages：https://support.google.com/adsense/answer/10961479
- AdSense Help — Ads.txt guide：https://support.google.com/adsense/answer/7532444
- AdSense Help — Fix ads.txt issues：https://support.google.com/adsense/answer/12171244
- AdSense Help — Ensure your ads.txt files can be crawled：https://support.google.com/adsense/answer/7679060（查閱 2026-11-05）
- AdSense Help — Ads.txt FAQs（轉址規則）：https://support.google.com/adsense/answer/9785052（查閱 2026-11-05）
- AdSense Help — sellers.json：https://support.google.com/adsense/answer/9889911
- Google Legal Help — 法律移除要求：https://support.google.com/legal/answer/3110420

**版位、功能、收益**
- AdSense Help — Auto ads settings：https://support.google.com/adsense/answer/9305577
- AdSense Help — Auto ads banner advanced settings（2026-04-16）：https://support.google.com/adsense/answer/16683740
- AdSense Help — Vignette triggers：https://support.google.com/adsense/answer/16853623
- AdSense Help — Offerwall：https://support.google.com/adsense/answer/13866332
- AdSense Help — Offerwall optimization：https://support.google.com/adsense/answer/16776170（查閱 2026-11-05）
- AdSense Help — Ad intents：https://support.google.com/adsense/answer/13844047（查閱 2026-11-05）
- AdSense Help — AMP display ad unit：https://support.google.com/adsense/answer/9274230
- AdSense Help — Unfilled / hidden ad units：https://support.google.com/adsense/answer/10762946
- AdSense Help — CSP：https://support.google.com/adsense/answer/16283098
- AdSense Help — Block advertiser URLs（500）：https://support.google.com/adsense/answer/164657
- AdSense Help — Run experiments：https://support.google.com/adsense/answer/45030
- Chrome for Developers — New ad metrics in CrUX（2026-09-15）：https://developer.chrome.com/blog/crux-ad-metrics
- ppc.land — Google to retire Ad Balance in AdSense（2020-05-20）：https://ppc.land/google-to-retire-ad-balance-in-adsense/

**無效流量與帳號**
- AdSense Help — Invalid traffic：https://support.google.com/adsense/answer/16737
- AdSense Help — Report invalid clicks：https://support.google.com/adsense/answer/1348754
- AdSense Help — Ad serving limits：https://support.google.com/adsense/answer/9437976
- AdSense Help — Ad serving statuses：https://support.google.com/adsense/answer/11066888
- AdSense Help — Policy center：https://support.google.com/adsense/answer/7003627
- AdSense Help — Account suspension：https://support.google.com/adsense/answer/2659114
- AdSense Help — Account disabled for invalid traffic：https://support.google.com/adsense/answer/57153
