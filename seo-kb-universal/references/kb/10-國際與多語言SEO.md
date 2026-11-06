# 10 國際與多語言 SEO

> 版本：1.2 ｜ 更新日期：2026-11-05 ｜ 適用：所有 SEO 網站專案 ｜ 撰寫：Claude

## 本章摘要

1. URL 結構決策：預設用 **gTLD + 子目錄**（`example.com/tw/`、`/ja/`），除非有強烈的本地品牌／法規理由才用 ccTLD；子網域只在技術上必須分離時使用；URL 參數不可用。
2. hreflang 是「同內容不同語言／地區版本」的互指宣告，三種實作（HTML、HTTP header、sitemap）等價；必須雙向互指、自指、含 `x-default`、用 ISO 639-1 + ISO 3166-1 Alpha-2（不可只有地區碼、不可用 `es-419`、`UK` 要寫 `GB`）。
3. Google 判定語言只看**可見內文**，不看 `lang`、URL、hreflang；因此混語頁面要讓主要語言明確，並為同主題分別做純語言版本。
4. 禁止依 IP 自動轉址：Googlebot 主要從美國抓、不帶 `Accept-Language`，自動轉址會讓它看不到其他版本；用建議橫幅 + 語言切換器。
5. 機器翻譯未經人工審校的大量頁面落在 scaled content abuse 範圍；每個語言版本都要「在地化」（貨幣、單位、法規、文化、關鍵字）而不只是翻譯。

## 目錄

1. [URL 結構選擇決策樹](#1-url-結構選擇決策樹)
2. [hreflang 完整規範](#2-hreflang-完整規範)
3. [Google 的地理定位訊號](#3-google-的地理定位訊號)
4. [語言偵測與自動轉址的禁忌](#4-語言偵測與自動轉址的禁忌)
5. [翻譯 vs 在地化與機器翻譯政策風險](#5-翻譯-vs-在地化與機器翻譯政策風險)
7. [貨幣、時區、單位、日期格式](#7-貨幣時區單位日期格式)
8. [各市場搜尋引擎差異](#8-各市場搜尋引擎差異)
9. [多語言 sitemap 範本](#9-多語言-sitemap-範本)
10. [多語言站的內部連結與語言切換器](#10-多語言站的內部連結與語言切換器)
11. [國際站 → 狀況解法表](#11-國際站--狀況解法表)
12. [本章檢查清單](#12-本章檢查清單)
13. [參考來源](#13-參考來源)

---

## 1. URL 結構選擇決策樹

**規範**：新專案預設採 `gTLD + 子目錄`；只有在「需要獨立品牌／法規要求／既有 ccTLD 資產」三者之一成立時才用 ccTLD；子網域僅用於技術隔離（不同平台、不同團隊）。

**為什麼**（Google 官方 Managing multi-regional sites，查閱 2026-11-03）：

| 結構 | 範例 | 優點 | 缺點 |
|---|---|---|---|
| ccTLD | `example.tw` | 地理定位最強、使用者信任、主機位置無關 | 貴、可能有註冊資格限制、每個網域只能定位一國、權重不共享、每站都要從頭建 |
| 子網域 | `tw.example.com` | 設定簡單、可在 GSC 設定國家定位、可用不同主機 | 使用者分不清是語言還是國家；Google 傾向視為較獨立的資產，權重共享弱於子目錄 |
| 子目錄 | `example.com/tw/` | 設定與維護最簡單、權重共享、一個主機 | 使用者從 URL 看不出定位；只能一個主機位置；日後拆分較難 |
| URL 參數 | `example.com?loc=tw` | 無 | **Google 不建議**：難以分段、使用者看不懂 |

Google 將 `.com`、`.org`、`.eu`、`.asia`，以及被視為通用的 ccTLD（`.tv`、`.me`、`.co`、`.io`、`.ai` 等）都當 gTLD 處理，需在 GSC 或以 hreflang 明示定位。

**決策樹**：
1. 是否只有一種語言、面向全球？→ gTLD 單站，不需 hreflang（除非有地區版本）。
2. 內容是否「同語言、不同地區」（如 en-GB / en-SG / en-US）？→ 子目錄 + hreflang 語言-地區碼 + 各目錄在 GSC 設國家定位。
3. 內容是否「不同語言」（en / ja / zh-Hant）？→ 子目錄 + hreflang 語言碼（可不帶地區）。
4. 是否受當地法規要求本地網域（如中國 ICP、某些金融業）？→ ccTLD。
5. 既有 ccTLD 已有權重？→ 保留並以 hreflang 連結，不要為了「統一」硬遷移。
6. 是否需要讓某市場能被整體出售、或由另一團隊獨立營運？→ 子網域或 ccTLD（詳見 11 的擴張策略）。

**驗收方式**：所有語言／地區版本在 GSC 建立對應資產（網域資產或子目錄 URL 前置字元資產），國際指定報告無錯誤。

**常見錯誤**：用 `.tw` 放英文全球內容又想在美國排名；子目錄用 `/en/` 卻在 GSC 定位到單一國家；同一語言不同地區做成完全相同內容（詳見第 5 節）。

---

## 2. hreflang 完整規範

### 2.1 適用情境與不適用情境

**規範**：只有當「同一內容存在多個語言或地區版本」時才用 hreflang；單一語言、單一市場的站不加。

Google 列出的三種適用情境：主內容相同、只翻譯模板（UGC 站）；同語言的小幅地區差異（貨幣、運費、法規）；完整翻譯。

### 2.2 三種實作方式（等價，擇一，不要混用）

**HTML `<head>`**（每個版本都要列出自己與所有其他版本，整組在每頁完全相同）：

```html
<link rel="alternate" hreflang="en-us" href="https://example.com/us/sim-registration/" />
<link rel="alternate" hreflang="ja" href="https://example.com/ja/sim-registration/" />
<link rel="alternate" hreflang="en-sg" href="https://example.com/sg/sim-registration/" />
<link rel="alternate" hreflang="zh-hant-tw" href="https://example.com/tw/sim-registration/" />
<link rel="alternate" hreflang="en" href="https://example.com/sim-registration/" />
<link rel="alternate" hreflang="x-default" href="https://example.com/sim-registration/" />
```

**HTTP Link header**（非 HTML 檔如 PDF）：

```
Link: <https://example.com/us/guide.pdf>; rel="alternate"; hreflang="en-us",
      <https://example.com/ja/guide.pdf>; rel="alternate"; hreflang="ja",
      <https://example.com/guide.pdf>; rel="alternate"; hreflang="x-default"
```

**Sitemap**（大型站首選，見第 9 節範本）。

### 2.3 規則清單

| 規則 | 說明 | 來源 |
|---|---|---|
| 自指 | 每個版本必須列出自己 | Google：「Each language version must list itself as well as all other language versions.」 |
| 雙向互指 | A 指 B，B 必須指回 A，否則整組被忽略；新增語言時要更新所有既有頁 | Google |
| 完整 URL | 含協定與網域（`https://…`），不可相對路徑 | Google |
| 跨網域可用 | 不同網域（ccTLD 之間）可以互指，但各網域需在 GSC 驗證 | Google |
| 語言碼 | ISO 639-1 兩碼（`en`、`ja`、`zh`、`ko`、`vi`、`id`、`ms`） | Google |
| 地區碼 | 選用，ISO 3166-1 Alpha-2（`TW`、`SG`、`US`、`GB`）；**只有地區碼無語言碼無效**；`UK`、`EU`、`UN` 等保留碼無效 | Google |
| 文字（script）碼 | ISO 15924：`zh-Hant`、`zh-Hans`、`zh-Hant-TW`；`zh-TW` 可由地區推導文字 | Google |
| 不支援 | `es-419`（拉丁美洲）等非標準碼 | Google |
| 大小寫 | 不區分，慣例地區碼大寫 | Google |
| `x-default` | 指向「無匹配語言／地區時」的後備頁，通常是語言選擇頁或全球英文版；每組建議有 | Google |
| 不混用屬性 | `<link>` 上不要同時放 `media` 等其他屬性 | Google |
| `<head>` 必須合法 | hreflang 標籤前若有未閉合元素被瀏覽器移到 `<body>`，會失效；用渲染後 HTML 驗證 | Google |
| 與 canonical 的關係 | hreflang 指向的 URL 必須是各自的 canonical；A 的 canonical 指向 B 又 hreflang 互指，會互相矛盾 | 實務 |
| 與 noindex 的關係 | `noindex` 頁不要放進 hreflang 組 | 實務 |
| 數量上限 | 官方未定；sitemap 中的 `xhtml:link` 不計入 50,000 URL 上限 | Google |
| 語言偵測 | Google **不用** hreflang 或 `lang` 屬性判斷頁面語言 | Google |
| 翻譯程度 | 只翻模板、主內容未翻的版本會被視為重複；這時仍可用 hreflang，但用 canonical 合併是更安全的選擇 | Google |

### 2.4 語言－地區碼對照（本知識庫常用）

| 市場 | 建議碼 | 說明 |
|---|---|---|
| 台灣繁中 | `zh-Hant-TW` 或 `zh-TW` | 兩者 Google 都接受；全站一致 |
| 香港繁中 | `zh-Hant-HK` | |
| 簡中 | `zh-Hans` 或 `zh-CN` | |
| 新加坡英文 | `en-SG` | |
| 馬來西亞 | `ms-MY`、`en-MY` | |
| 印尼 | `id-ID` | |
| 越南 | `vi-VN` | |
| 全球英文 | `en` | 無地區 = 所有英文使用者的 catch-all |
| 後備 | `x-default` | |

**驗收方式**：GSC「國際指定」報告（舊版仍可用）無「沒有回傳標記」錯誤；用 Screaming Frog 的 hreflang 報告檢查「缺少自指」「無回傳」「不一致的 canonical」；抽 10 組用 hreflang 驗證工具。

**常見錯誤**：只有地區碼 `hreflang="tw"`；寫 `en-UK`；改版後舊語言頁被刪但其他頁仍指向它（404）；分頁（page 2、3）互指錯誤；hreflang 指向帶 UTM 的 URL。

---

## 3. Google 的地理定位訊號

**規範**：每個地區版本至少具備 3 個一致的地理訊號：URL 結構／GSC 定位、hreflang 地區碼、本地化內容（貨幣、地址、電話、法規）。

**為什麼**（Google 官方，查閱 2026-11-03）：
- ccTLD：最強，直接綁定國家。
- GSC 國際指定（International Targeting）：**國家定位設定已於 2022-09 從 Search Console 移除（已變更）**，報告只剩 hreflang 錯誤檢查；gTLD 想定位國家，現在只能靠 hreflang 地區碼與本地化內容訊號（ccTLD 仍自動定位）。
- hreflang 地區碼。
- 伺服器 IP：弱訊號，因 CDN 普及而不可靠。
- 其他：本地地址與電話、本地語言與貨幣、來自本地網站的連結、Business Profile。
- **被忽略**：`geo.position`、`geo.region`、`distribution` 等 meta 標籤。

**取捨**：對單一國家定位會「犧牲其他地區的排名」；流量站若要同時吃本地與海外的英文流量，不要把英文版定位到單一國家，改用 `en`（全球）+ 本地語言版（如 `zh-TW`）。

**驗收方式**：用 VPN 或 Google 搜尋的 `&gl=tw&hl=zh-TW` 參數檢查各市場顯示的版本是否正確。

---

## 4. 語言偵測與自動轉址的禁忌

**規範**：禁止依 IP、`Accept-Language` 或 cookie **自動 301/302 轉址**到語言版本；允許的做法是顯示可關閉的建議橫幅、並在每頁提供語言切換器。每個語言版本必須有獨立 URL。

**為什麼**（Google 官方）：
- Googlebot 主要用美國 IP 抓取且**不送 `Accept-Language`**；自動轉址會讓它只看到英文／美國版，其他版本永遠抓不到。
- 「Don't use IP analysis to adapt your content.」——IP 定位不可靠（VPN、行動網路、CDN）。
- Locale-adaptive pages（同 URL 依地區回傳不同內容）：Google 雖有地理分散抓取（非美 IP），但不保證抓齊，官方建議改用獨立 URL + hreflang；若堅持 locale-adaptive，必須把 Googlebot 當該國一般使用者處理（例如封鎖美國使用者就同樣封鎖美國 IP 的 Googlebot），且 robots 規則在各地區一致。
- Google 判斷語言靠**可見內容**，不看 `lang` 屬性、URL、hreflang；每頁應單一語言（內容與導覽一致），避免左右對照翻譯。

**怎麼做**：
1. 首次造訪顯示橫幅：「看起來您在台灣，要切換到繁體中文版嗎？」，記住選擇（cookie），**不自動轉址**。
2. 若商業上必須轉址（例如法規），只對使用者（非驗證過的 Googlebot）轉，並確保轉址目標頁 hreflang 完整、`x-default` 指向語言選擇頁——這是 Google 容忍但不建議的做法。
3. `x-default` 指向不轉址的語言選擇頁或全球版。
4. 翻譯只翻模板時，主內容語言仍是判斷依據；UGC 站不要讓同一則英文內容出現在 `/ja/` 下。

**驗收方式**：用 URL 檢查工具「測試線上網址」看各語言 URL 是否回傳該語言內容；伺服器日誌確認 Googlebot 沒被 302。

**常見錯誤**：WordPress 外掛的「自動依瀏覽器語言轉址」預設開啟；Cloudflare Worker 依國家重寫內容；`x-default` 指向會轉址的首頁。

---

## 5. 翻譯 vs 在地化與機器翻譯政策風險

**規範**：每個語言版本必須經過（1）母語或雙語編輯審校、（2）關鍵字在地化（不是翻譯關鍵字）、（3）事實在地化（價格、法規、品牌、可得性）；純機器翻譯未經人審的頁面不得索引。

**為什麼**：
- Google spam policies 的 scaled content abuse 例子包含「scraping… including through synonymizing, **translating**, or other obfuscation techniques」；舊版自動產生內容政策更直接點名「text translated by an automated tool without human review or curation before publishing」。大量 MT 頁 = 高風險。
- Google 的 generative AI content 指引要求「manually factcheck and review all AI-generated content」，MT 視同 AI 產出。
- 翻譯的關鍵字常不是當地人的搜尋用語（例如台灣「悠遊卡」vs 直譯「EasyCard 卡」）。

**怎麼做**（在地化流程）：
1. 關鍵字：在目標語言重新做關鍵字研究（Keyword Planner 設定國家＋語言；Google Trends 比較用語；查當地論壇用詞）（詳見 02）。
2. 翻譯：MT 初稿（DeepL／LLM）→ 母語編輯審校 → 事實在地化（價格、貨幣、店家、法規、聯絡方式）→ 在地化 SEO（title、meta、H 標籤、圖片 alt、內部連結錨文字）。
3. 不翻譯的部分：品牌名、產品型號、程式碼；專有名詞第一次出現保留英文。
4. 標示：若使用 MT 且已人審，可在頁尾說明「本文由 〔語言〕原文翻譯並經編輯審校」；未審校版本一律 `noindex` 或不發布。
5. 版本差異：同語言不同地區（en-US vs en-SG）必須有實質差異（價格、供應商、法規），否則用 canonical 合併並只保留一個，再用 hreflang 指向——完全相同的內容做多地區版本是浪費抓取預算且可能被視為重複。

**驗收方式**：抽 10 頁由母語者評「像不像當地人寫的」（5 分制 ≥ 4）；在地化關鍵字的曝光在 GSC 以國家篩選後上升；未人審頁面數為 0。

**常見錯誤**：WordPress 外掛一鍵 MT 翻譯 5,000 頁並索引；翻譯 title 超長（中文字寬）；把美元價格直接翻成新台幣但沒換算；日期格式沒換。

---

## 7. 貨幣、時區、單位、日期格式

**規範**：每個地區版本的貨幣、單位、日期、電話、地址格式必須符合當地慣例，並在結構化資料中用標準碼（ISO 4217 貨幣、ISO 8601 日期）。

| 項目 | 做法 | 範例 |
|---|---|---|
| 貨幣 | 顯示當地貨幣符號與 ISO 碼；`Offer.priceCurrency` 用 ISO 4217；換算價註明匯率日期 | NT$1,200（TWD）；S$39（SGD） |
| 日期 | 顯示用當地慣例；`datePublished` / `dateModified` 用 ISO 8601 含時區 | US：November 3, 2026；TW：2026年11月3日；`2026-11-03T09:00:00+08:00` |
| 時區 | 內容中的時間標註時區（TST = UTC+8）；活動用 `Event.startDate` 含時差 | 「10:00 AM TST」 |
| 單位 | TW 公制；US 英制 | 提供雙單位：「5 ft 4 in (163 cm)」 |
| 電話 | E.164 於結構化資料；顯示用當地格式 | `+886 2 1234 5678` |
| 地址 | 當地順序；`PostalAddress` 結構化 | TW：郵遞區號、縣市、鄉鎮市區、路街、門牌、樓層 |
| 數字 | 千分位與小數點依地區（TW/SG 同英文慣例） | 1,299.50 |
| 語言切換後的格式 | 格式跟隨**地區**而非語言（台灣的英文版與繁中版都用 NT$ 與同樣日期） | |

**驗收方式**：抽查每個地區版本 10 頁的價格、日期、電話格式；Rich Results Test 無貨幣／日期格式警告。

**常見錯誤**：全站共用一個 `priceCurrency: USD`；`dateModified` 沒時區導致 Google 以 UTC 解讀而「發布日期」顯示差一天。

---

## 8. 各市場搜尋引擎差異

查閱日期 2026-11-03；市占數據來自 StatCounter（2026-04 至 06 快照）與二手報導，會隨月份變動。

| 市場 | 主要引擎與市占 | 技術差異 | 對策 |
|---|---|---|---|
| 全球／台灣／東南亞 | Google 約 91%；Bing 約 4.7% | — | 以 Google 為主；Bing Webmaster Tools + IndexNow 兼顧（ChatGPT 搜尋依賴 Bing，詳見 08） |
| 日本 | Google 約 59%、Bing 約 33%、Yahoo! Japan 約 6%（StatCounter 2026-06；Yahoo! Japan 使用 Google 的搜尋技術） | Yahoo! Japan 結果近似 Google；Bing 在日本桌機占比高 | Google 優化即可覆蓋 Yahoo! Japan；Bing 要另外提交 |
| 韓國 | Naver 約 32–42%、Google 約 47–53%（兩種統計口徑差異大） | Naver 以自家內容生態（Blog、Cafe、知識 iN、Smart Store）為主，外部網站排名弱；支援 hreflang 有限 | 要進韓國市場需經營 Naver Blog／Smart Store；Naver Search Advisor 提交 |
| 俄羅斯 | Yandex 約 73% | 支援 hreflang；重視行為訊號與地區（Yandex.Webmaster 設地區）；對 Cyrillic 網域友善 | Yandex.Webmaster 驗證；地區設定；Yandex Metrica |
| 中國 | Baidu 約 45%、Bing 約 23%、Haosou 約 18%（StatCounter 2026-04；CNNIC 口徑 Baidu 約 60%） | **不支援 hreflang**；需 ICP 備案與境內主機才有穩定排名；偏好簡中、`.cn`；JS 渲染弱；重視百度站長平台提交與熊掌號等自家產品 | 獨立簡中站、ICP、境內 CDN；`meta name="applicable-device"`；用 canonical 而非 hreflang |
| Bing（全球） | — | 支援 hreflang，但也讀 `<meta http-equiv="content-language">`；索引偏好清楚的 `lang` 屬性 | 兩者都放；IndexNow |
| 其他 | Seznam（捷克）、DuckDuckGo（用 Bing） | — | Bing 優化覆蓋 DuckDuckGo |

## 9. 多語言 sitemap 範本

**規範**：語言版本 ≥ 3 或頁數 ≥ 1,000 的站，用 sitemap 實作 hreflang（集中管理、不增加 HTML 體積）；每個 `<url>` 列出所有版本（含自己）；sitemap 依語言拆檔並用 sitemap index 彙整；只放 canonical、可索引、回 200 的 URL。

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xhtml="http://www.w3.org/1999/xhtml">

  <url>
    <loc>https://example.com/sim-registration/</loc>
    <lastmod>2026-11-01T09:00:00+08:00</lastmod>
    <xhtml:link rel="alternate" hreflang="en" href="https://example.com/sim-registration/"/>
    <xhtml:link rel="alternate" hreflang="en-us" href="https://example.com/us/sim-registration/"/>
    <xhtml:link rel="alternate" hreflang="ja" href="https://example.com/ja/sim-registration/"/>
    <xhtml:link rel="alternate" hreflang="zh-hant-tw" href="https://example.com/tw/sim-registration/"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="https://example.com/sim-registration/"/>
  </url>

  <url>
    <loc>https://example.com/us/sim-registration/</loc>
    <lastmod>2026-11-01T09:00:00+08:00</lastmod>
    <xhtml:link rel="alternate" hreflang="en" href="https://example.com/sim-registration/"/>
    <xhtml:link rel="alternate" hreflang="en-us" href="https://example.com/us/sim-registration/"/>
    <xhtml:link rel="alternate" hreflang="ja" href="https://example.com/ja/sim-registration/"/>
    <xhtml:link rel="alternate" hreflang="zh-hant-tw" href="https://example.com/tw/sim-registration/"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="https://example.com/sim-registration/"/>
  </url>

  <!-- /ja/ 與 /tw/ 版本同樣各自列出完整一組 -->

</urlset>
```

規則：
- 必須宣告 `xmlns:xhtml`。
- 每個 `<url>` 的 `xhtml:link` 組要完全相同（含自己）。
- sitemap 只能包含它所在目錄的子孫 URL；跨網域的 hreflang 需在各網域各自的 sitemap 宣告且各網域都在 GSC 驗證（或用 robots.txt 的 `Sitemap:` 指令做跨網域提交）。
- `lastmod` 只在內容實際更新時改；Google 已表示會忽略不可信的 `lastmod`。
- 自動化：由 CMS 的翻譯關聯表生成，不要手工維護；每日重建並在 GSC 監看「已找到 / 已索引」比例。

sitemap index 範例與 robots.txt 範本詳見 15-技術實作範本.md。

---

## 10. 多語言站的內部連結與語言切換器

**規範**：語言切換器必須是**可抓取的 `<a href>` 連結**，指向「同一頁的對應語言版本」（不是各語言首頁），以當地語言顯示語言名稱，放在所有頁的固定位置；各語言版本的內部連結只連到同語言頁面（除非該語言沒有對應頁）。

**為什麼**：
- Google 要求「provide a way for users to pick their region or language from every page」，且語言切換器是 Googlebot 發現其他版本的主要路徑之一（hreflang 只是宣告，不是連結）。
- 用 JS `onclick` 或 `<select>` 做的切換器 Googlebot 不會跟隨。
- 跨語言的內部連結會把 PageRank 分散到使用者不會看的版本，並讓語言判定混亂。

**怎麼做**：
1. 切換器：`<a href="https://example.com/ja/sim-registration/" hreflang="ja" lang="ja">日本語</a>`；語言名稱用該語言自稱（日本語、繁體中文、English），可加國旗但不要只用國旗（國旗代表國家不代表語言）。
2. 若某頁沒有對應語言版本：切換器指向該語言的最近上層（分類頁）並標示「此頁尚無日本語版」，不要指向 404 或自動 fallback 到英文而不告知。
3. 導覽、頁尾、麵包屑、相關文章全部語言內閉環；共用的全站元件（如頁尾）依語言輸出。
4. 新語言上線：先完成核心頁（首頁、分類、Top 100 文章）再開放索引，避免大量「只有模板翻譯」的頁面。
5. 多語言站的 `rel="canonical"` 一律自指（各語言自己的 URL）。

**驗收方式**：Screaming Frog 以各語言目錄爬取，檢查外連到其他語言目錄的內部連結比例 < 5%（切換器除外）；切換器連結在原始 HTML 可見。

**常見錯誤**：切換器指向各語言首頁；用 `<select onchange>`；英文版文章的「相關文章」推薦中文版。

---

## 11. 國際站 → 狀況解法表

| 症狀 | 可能原因 | 診斷步驟 | 解法 | 預防 |
|---|---|---|---|---|
| GSC 顯示「hreflang 沒有回傳標記」 | 單向指向；某版本 noindex／404／canonical 指向別處 | 檢查被指向 URL 的狀態碼、canonical、是否自指 | 修成雙向、自指；移除 noindex 頁 | sitemap 自動生成 |
| 兩個語言版本互相吃掉排名（cannibalization） | hreflang 無效，Google 視為重複；或同語言不同地區內容相同 | 搜尋結果看哪個版本出現；檢查 hreflang 是否被忽略 | 修 hreflang；同語言相同內容用 canonical 合併 | 第 5 節版本差異規範 |
| 新語言上線後整站流量下滑 | 大量 MT 薄頁被視為 scaled content；抓取預算被稀釋 | GSC 索引報告看新語言頁的「已檢索但未索引」比例；核心更新時間對照 | 未審校頁 `noindex`；分批人審後再開放 | 分階段上線 |
| 簡中版在百度無排名 | 無 ICP、境外主機、hreflang 無效、JS 渲染 | 百度站長平台抓取診斷 | 獨立 `.cn` 站＋ICP＋境內 CDN；SSR | 中國市場專案前評估 |
| 語言版本被 Google 判為另一語言 | 混語 50/50；導覽與內文語言不同；模板未翻 | URL 檢查工具看 Google 偵測語言（無直接欄位，用搜尋結果語言標籤旁證） | 讓主要語言 ≥ 80%；翻模板 | 25 §3 寫作規範 |
| Googlebot 被自動轉址到英文版 | IP／Accept-Language 轉址 | 日誌看 Googlebot 的 302；URL 檢查工具 | 關閉自動轉址，改橫幅 | 第 4 節 |
| hreflang 在 HTML 中但被忽略 | `<head>` 被未閉合標籤破壞；hreflang 放在 `<body>` | 看「已轉譯的 HTML」中 hreflang 是否仍在 `<head>` | 修 HTML；改用 sitemap | HTML 驗證納入 CI |
| 多個 ccTLD 權重各自為政、都難起來 | 權重不共享、各站內容少 | 比較各站外鏈與索引數 | 合併為 gTLD 子目錄（301 + hreflang）；保留本地品牌的只留主要市場 | 第 1 節決策樹 |
| 單一社群平台被政府封鎖，流量一夜歸零 | 分發過度集中 | 看流量來源占比 | 立即改走已註冊平台與即時通訊、Email、push；搜尋流量當底 | 任一渠道占比不超過 50%（12 I5） |

---

## 12. 本章檢查清單

- [ ] URL 結構依決策樹選定並記錄理由；無 URL 參數式語言切換。
- [ ] 每個語言／地區版本有獨立 URL、自指 canonical、在 GSC 建立資產。
- [ ] hreflang：自指 + 雙向 + `x-default`；語言碼 ISO 639-1、地區碼 ISO 3166-1（`GB` 非 `UK`）；無只有地區碼的值。
- [ ] hreflang 實作擇一（HTML / header / sitemap），sitemap 版本由 CMS 自動生成。
- [ ] 無 IP / Accept-Language 自動轉址；有可關閉的建議橫幅；`x-default` 指向不轉址頁。
- [ ] 每頁單一主要語言 ≥ 80%；混語市場依查詢語言分版本（25 §3）。
- [ ] 所有翻譯頁經母語審校；關鍵字、價格、法規、聯絡方式在地化；未審校頁 `noindex`。
- [ ] 貨幣、日期、時區、單位、電話格式依地區；結構化資料用 ISO 碼與含時區的 ISO 8601。
- [ ] 語言切換器為可抓取 `<a href>`，指向同頁對應版本，語言名稱用自稱。
- [ ] 內部連結語言內閉環（跨語言 < 5%）。
- [ ] 目標市場若含日本／韓國／俄羅斯／中國，已處理對應引擎（Bing、Naver、Yandex、Baidu）的提交與限制。
- [ ] GSC 國際指定報告與 Screaming Frog hreflang 報告每月檢查一次。
- [ ] 進入新市場前查 25 章：主要語言是否在 AdSense 支援清單（22 §1.1）、第一分發平台、query 語言軌、在地編碼與字型、法規紅線。
- [ ] 任一分發渠道占流量不超過 50%；Email、push、直接造訪有保底機制。

## 13. 參考來源

（查閱日期皆為 2026-11-03）

- Google Search Central — Tell Google about localized versions of your page（hreflang）：https://developers.google.com/search/docs/specialty/international/localized-versions
- Google Search Central — Managing multi-regional and multilingual sites：https://developers.google.com/search/docs/specialty/international/managing-multi-regional-sites
- Google Search Central — How Google crawls locale-adaptive pages：https://developers.google.com/search/docs/specialty/international/locale-adaptive-pages
- Google Search Central — Spam policies（scaled content abuse：translation 作為混淆手法）：https://developers.google.com/search/docs/essentials/spam-policies
- Google Search Central — Google Search's guidance about AI-generated content：https://developers.google.com/search/docs/fundamentals/using-gen-ai-content
- Google — AI Mode 支援語言（含 Chinese Traditional）：https://support.google.com/websearch/answer/16011537
- StatCounter Global Stats — Search engine market share（Asia / Japan / 各國）：https://gs.statcounter.com/search-engine-market-share
- ISO 639-1 語言碼、ISO 3166-1 Alpha-2 地區碼、ISO 15924 文字碼（標準參照）
- Bing Webmaster — IndexNow：https://www.indexnow.org/
- Digital Applied — Search engine market share 2026 global data（韓國 Naver 口徑差異的二手整理）：https://www.digitalapplied.com/blog/search-engine-market-share-2026-global-data

（以下查閱日期 2026-11-05）

- Google — AI Overviews 支援國家與語言：https://support.google.com/websearch/answer/14901683
- Google AdSense — 支援的發布商語言：https://support.google.com/adsense/answer/9727
- Google AdSense — 各國付款方式：https://support.google.com/adsense/answer/1714397
