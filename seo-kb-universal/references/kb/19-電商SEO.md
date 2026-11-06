# 19 電商 SEO

> 版本：1.0 ｜ 更新日期：2026-11-03 ｜ 適用：所有 SEO 網站專案 ｜ 撰寫：Claude

## 本章摘要

1. 電商 SEO 的核心是「爬取預算 × 重複內容 × 商業意圖」三者的取捨：類別頁承接商業關鍵字，產品頁承接長尾與交易，其餘（篩選、排序、站內搜尋、變體）一律控制。
2. Product 結構化資料在 2026 年分為兩種 rich result：Merchant listings（可直接購買的單一商品頁，必須 `Offer` 且價格 > 0）與 Product snippets（評測 / 比價頁，可 `AggregateOffer`）；2026-07 新增 `category`、`validFrom` / `validThrough` 促銷期間。
3. Google 建議「結構化資料 + Merchant Center feed 並用」；Merchant Center 免費商品資訊預設開啟；2026-09 中旬第三方追蹤到 EEA 免費商品資訊自 Google Search 消失（與 DMA 有關），Google 無正式公告、官方文件仍描述 EEA 可透過 CSS 投放免費商品資訊；EEA 以外不受影響。
4. 缺貨與下架頁的決策依「是否會回補、是否有替代品、是否有外部連結 / 流量」分流：保留（200 + OutOfStock）、301 到最接近替代、或 410。
5. Shopify / WooCommerce / Magento 各有結構性限制（Shopify 的 collections 路徑重複與 robots.txt.liquid、WooCommerce 的參數與屬性頁、Magento 的 layered navigation 與 URL rewrites），上線前即需設定。

## 目錄

1. [適用範圍](#1-適用範圍)
2. [電商網站架構](#2-電商網站架構)
3. [類別頁優化](#3-類別頁優化)
4. [產品頁優化](#4-產品頁優化)
5. [分面導覽與爬取控制（電商特有決策）](#5-分面導覽與爬取控制電商特有決策)
6. [缺貨與下架頁處理](#6-缺貨與下架頁處理)
7. [季節性與促銷頁的常態 URL 策略](#7-季節性與促銷頁的常態-url-策略)
8. [Product 結構化資料：Merchant listings 與 Product snippets](#8-product-結構化資料merchant-listings-與-product-snippets)
9. [Google Merchant Center 免費商品資訊與 SEO](#9-google-merchant-center-免費商品資訊與-seo)
10. [評論與 UGC](#10-評論與-ugc)
11. [重複內容：製造商描述與多通路](#11-重複內容製造商描述與多通路)
12. [站內搜尋頁](#12-站內搜尋頁)
13. [國際電商（簡述）](#13-國際電商簡述)
14. [Shopify / WooCommerce / Magento 設定要點與限制](#14-shopify--woocommerce--magento-設定要點與限制)
15. [電商 CWV 特有問題](#15-電商-cwv-特有問題)
16. [狀況 → 解法表](#16-狀況--解法表)
17. [本章檢查清單](#17-本章檢查清單)
18. [參考來源](#18-參考來源)

---

## 1. 適用範圍

| 專案類型 | 適用程度 | 說明 |
|---|---|---|
| 電商（自營、D2C、零售、B2B 型錄） | 核心 | 全章 |
| 流量站 / 聯盟內容站 | 中 | 第 8 節 Product snippets（可用 `AggregateOffer`）、第 10、11 節；不適用 Merchant listings（非賣家） |
| 企業官網（型錄不線上販售） | 中 | 架構、產品頁、Product snippets |
| 本地零售 | 中 | 第 9 節本地庫存；GBP 店內商品詳見 17 |
| SaaS | 低 | 定價頁 `Offer` 詳見 06 |

通則不重複：URL 與分面（03、04）、結構化資料語法（06）、hreflang（10）、CWV（04）、演算法與 Reviews system（07）。

---

## 2. 電商網站架構

### 2.1 層級與 URL

**規範**：首頁 → 類別 → 子類別 → 產品，任何產品距首頁 ≤ 3 次點擊；URL 用描述性文字、全小寫、連字號、無 session / 追蹤參數；產品 URL 不含類別路徑（`/products/{slug}/`），避免同一產品因多類別產生多 URL。

**為什麼**：Google 電商 URL 指南建議「描述性路徑優於數字 ID」（`/product/black-t-shirt-with-a-white-collar` 優於 `/product/3243`）、不要連結到 session ID / 時間戳 / 使用者相對值（`location=nearby`）、同一內容多 URL 浪費爬取資源、大小寫不敏感的伺服器應統一為單一大小寫（來源：developers.google.com/search/docs/specialty/ecommerce/designing-a-url-structure-for-ecommerce-sites，查閱 2026-11-03）。

**怎麼做**：
```
/                                首頁
/c/{category}/                   類別（如 /c/running-shoes/）
/c/{category}/{subcategory}/     子類別（如 /c/running-shoes/trail/）
/p/{product-slug}/               產品（不帶類別路徑）
/brands/{brand}/                 品牌頁（品牌 × 類別可建 /brands/{brand}/{category}/，需有搜尋量）
/collections/{theme}/            主題 / 情境集合（如 /collections/gifts-under-1000/）
/search?q=                       站內搜尋（noindex）
```
- 麵包屑固定用產品「主類別」一條，加 `BreadcrumbList`（詳見 06）。
- 子類別須有獨立搜尋需求且產品數 ≥ 8–10（實務門檻）；不足者併回上層以篩選處理。
- 品牌 × 類別交叉頁只在有搜尋量時建立（「Nike 跑鞋」），否則以篩選呈現並 canonical 回品牌頁。

**驗收方式**：≥ 95% 產品頁爬取深度 ≤ 3；GSC「重複網頁，Google 選擇的標準網頁與使用者不同」趨近 0。

**常見錯誤**：產品 URL 帶類別路徑造成 `/c/a/p/x` 與 `/c/b/p/x` 重複；2 個產品也建子類別；品牌頁只有 Logo 牆。

### 2.2 內部連結

**規範**：類別頁以文字連結連到子類別、熱銷、相關類別；產品頁連回主類別、同系列、搭配、替代品；不靠純 JavaScript 載入的「推薦商品」承擔內部連結。

**為什麼**：Google 電商站結構指南強調用 `<a href>` 連結與導覽讓 Google 辨識重要頁面，Google 不點按鈕或觸發使用者事件（來源：developers.google.com/search/docs/specialty/ecommerce/help-google-understand-your-ecommerce-site-structure，查閱 2026-11-03）。

**怎麼做**：伺服器端輸出「熱門子類別」「同類別熱銷」區塊；Screaming Frog 找 inlinks < 3 的產品頁補連結；XML sitemap 分檔（products / categories / brands / collections，各 ≤ 50,000 URL、≤ 50MB），只收 canonical、可索引、200 的 URL。

---

## 3. 類別頁優化

### 3.1 文案位置與內容

**規範**：上方 1–2 句定位文 + 產品格 → 下方 200–500 字選購指南（子類別、品牌、規格解說、FAQ）；不以 `display:none` 塞字；不為字數湊字。

**為什麼**：類別頁承接「跑鞋」「女用登山包」等商業關鍵字，是自然流量主要入口；純 SEO 文字牆不符 Helpful content 評估（詳見 05、07）。Google 要求空類別頁 noindex 或 404（來源：URL structure 指南，查閱 2026-11-03）。

**怎麼做**：Title `{類別關鍵字}｜{特色}｜{品牌}` ≤ 60 字元；H1 = 類別名；首屏保留產品格（第一張產品圖給 `fetchpriority="high"`）；下方 H2 分段「如何選擇」「熱門品牌」「規格說明」「FAQ」（`FAQPage` rich result 自 2026-05 起完全停用，移除標記、FAQ 保留為可見內容）；0 產品類別暫時 `noindex`、永久 404 / 410 並移除內部連結。

**驗收方式**：GSC 類別頁目標查詢排名與點閱率；文案在 Rich Results Test 已轉譯 HTML 中可見。

**常見錯誤**：1,500 字文案放最上方把產品推到第二屏；所有類別同一模板替換關鍵字。

### 3.2 分頁（Pagination）

**規範**：每一頁獨立 URL（`?page=2`）、自我 canonical、可索引（不 noindex、不 canonical 回第一頁）、以 `<a href>` 連到上一頁 / 下一頁 / 首頁；「載入更多」或無限捲動必須有對應的分頁 URL 後備。

**為什麼**：Google 明示不再使用 `rel="next"` / `rel="prev"`；不要把分頁 canonical 指向第一頁；頁碼不可放 `#` 片段；無限捲動需有可爬取連結，並可用 sitemap 或 Merchant Center feed 協助發現產品（來源：developers.google.com/search/docs/specialty/ecommerce/pagination-and-incremental-page-loading，查閱 2026-11-03）。

**怎麼做**：`?page=1` 與無參數 URL 擇一並全站一致；第 2 頁起 Title 加「第 N 頁」；選購指南文案只放第 1 頁；超過最後一頁回 404。

**驗收方式**：GSC 中 `?page=2` 為「已建立索引」或至少「已檢索」；產品頁 inlinks 不只來自 sitemap。

### 3.3 排序與每頁數量參數

**規範**：`?sort=`、`?per_page=`、`?view=` 等同內容參數：canonical 指向預設 URL，大站再以 robots.txt 阻擋；內部連結不帶這些參數。Google 建議對篩選與替代排序變體用 `noindex` 或 robots.txt（來源：pagination 指南）。

**怎麼做**（robots.txt 範例，依實際參數名調整）：
```
User-agent: *
Disallow: /*?*sort=
Disallow: /*?*per_page=
Disallow: /*&sort=
```
注意：被 robots.txt 阻擋的 URL 上的 canonical / noindex 不會被讀到；若這些 URL 已被索引，先用 noindex 清除再阻擋（詳見 04）。

---

## 4. 產品頁優化

### 4.1 標題與 H1

**規範**：Title = `{品牌} {產品名} {關鍵規格}｜{站名}`；H1 = 完整產品名；不塞「免運 / 特價 / 2026」等易過期詞。產品查詢多為「品牌 + 型號 / 規格」；過長或堆砌的 Title 會被 Google 重寫（詳見 05）。

### 4.2 描述與規格

**規範**：每個產品 ≥ 150–300 字自寫描述（用途、適合誰、差異、情境）+ HTML 規格表（`<table>` / `<dl>`，不是圖片，key 全站統一）+ 製造商原文（可摺疊但在 DOM 內）。

**為什麼**：製造商描述在數百個零售站重複，無法成為被選為 canonical 的理由（第 11 節）；文字規格可被擷取進 Shopping 知識面板與 AI 摘要（詳見 08）。

**怎麼做**：優先寫流量 / 營收前 20% SKU；其餘模板 + 變數但保證每頁有可區分的實質資訊；程序化做法詳見 11。

### 4.3 圖片與影片

**規範**：每產品 ≥ 3 張圖（白底 / 情境 / 細節），主圖提供 1:1、4:3、16:9；檔名與 alt 描述產品與角度；圖片可爬取（CDN 路徑不被 robots.txt 阻擋）；影片用 `VideoObject` 或嵌 YouTube（詳見 06）。

**為什麼**：Merchant listing 要求 `image` 必填且可爬取，建議多張高解析度並提供三種比例（來源：developers.google.com/search/docs/appearance/structured-data/merchant-listing，查閱 2026-11-03）；Images 與 Lens 的商品標註依賴這些圖。

**驗收方式**：GSC「Merchant listings」無「圖片無法擷取」錯誤。

### 4.4 Q&A、評論、庫存狀態

- **Q&A**：顧客提問 + 官方回答是獨特內容來源，伺服器端輸出；不對整頁同時加 `FAQPage` 與 `Product`。
- **評論**：顯示真實評論（作者、日期、文字）；`aggregateRating` 僅在頁面可見且一致時標記；合規詳見第 10 節。
- **庫存**：頁面明示「有貨 / 缺貨 / 預購 / 補貨日」並對應 `Offer.availability`（`InStock`、`OutOfStock`、`PreOrder`、`BackOrder`、`LimitedAvailability`）；缺貨不隱藏價格（Merchant listing 需有效價格）。

### 4.5 變體（SKU）與 canonical

**規範**：
1. 變體採「同一頁 + 參數 / 路徑切換」（single-page）或「每變體獨立頁」（multi-page）二擇一，全站一致。
2. Single-page：`ProductGroup.url` 為不帶變體參數的 canonical；每個變體仍可透過自己的 URL（`?variant=123`）預選並顯示正確圖片、價格、庫存、購買鈕；變體 URL canonical 指向主 URL。
3. Multi-page：每頁獨立 canonical，`ProductGroup` 不填 `url`，每頁重複完整 `ProductGroup` 並以 `url` 參照其他變體。
4. 只有變體有獨立搜尋需求（「iPhone 17 256GB 黑」）且差異可見時才用 multi-page 並可索引。

**為什麼**：Google URL 指南：變體有自己 URL 時 canonical 指向主產品；以可選參數識別時不帶參數者為 canonical。Product variants 文件規定上述兩種模式，每變體需唯一 `sku` / `gtin` 並滿足 Merchant listing 必填；`variesBy` 僅支援 color、size、suggestedAge、suggestedGender、material、pattern（來源：developers.google.com/search/docs/appearance/structured-data/product-variants，查閱 2026-11-03）。

**怎麼做（single-page JSON-LD 骨架）**：
```json
{
  "@context": "https://schema.org",
  "@type": "ProductGroup",
  "name": "Trail Runner X",
  "url": "https://example.com/p/trail-runner-x/",
  "brand": {"@type": "Brand", "name": "Example"},
  "productGroupID": "TRX",
  "variesBy": ["https://schema.org/size", "https://schema.org/color"],
  "hasVariant": [
    {
      "@type": "Product",
      "sku": "TRX-BLK-42",
      "name": "Trail Runner X – Black – EU 42",
      "image": "https://example.com/img/trx-black-1x1.jpg",
      "color": "Black",
      "size": "EU 42",
      "offers": {
        "@type": "Offer",
        "url": "https://example.com/p/trail-runner-x/?variant=TRX-BLK-42",
        "price": 3290, "priceCurrency": "TWD",
        "availability": "https://schema.org/InStock"
      }
    }
  ]
}
```

**驗收方式**：Rich Results Test 對主 URL 與變體 URL 都偵測到 Merchant listing；GSC 無「重複網頁」警告集中在變體 URL。

**常見錯誤**：每個顏色一頁但內容只差一個字，全部可索引；變體用 `#color=red` 片段（Google 不索引片段）；主 URL 顯示的是「缺貨變體」導致 Google 抓到 OutOfStock。

---

## 5. 分面導覽與爬取控制（電商特有決策）

通則（robots.txt、canonical、noindex、參數處理）詳見 03、04；本節只講電商要做的決策。

### 5.1 哪些分面頁可以索引

**規範**：建立「分面索引決策矩陣」，僅當同時滿足以下 4 條件才讓某分面組合可索引：(1) 有可驗證搜尋量（KD / 月量在 02 的門檻之上）；(2) 產品數 ≥ 5；(3) 單一分面（最多兩個分面，且順序固定）；(4) 能給獨特 Title / H1 / 一段文案。其餘一律：canonical 指向類別頁 + robots.txt 阻擋（大站）或 noindex（小站）。

**為什麼**：Google 分面導覽指南：多數情況「沒有好理由允許爬取篩選後的項目」，robots.txt 阻擋立即節省資源；`rel="canonical"` 與 `nofollow` 是軟訊號，長期效果不如阻擋；若需讓分面可爬，用 `&` 分隔參數、路徑型分面固定順序並防重複、空結果或無意義組合回 404 而非轉址通用頁（來源：developers.google.com/search/docs/crawling-indexing/crawling-managing-faceted-navigation，查閱 2026-11-03）。

**怎麼做**：盤點所有分面與 URL 形式 → 以關鍵字資料定白名單（「類別 × 品牌」「類別 × 顏色」可；「類別 × 價格 × 尺寸」不可）→ 白名單改乾淨 URL（`/c/running-shoes/nike/`）並入 sitemap → 其餘保持參數並阻擋；價格、尺寸、評分、排序、每頁數量、多選分面永不索引。

**驗收方式**：GSC「已被 robots.txt 封鎖」穩定、「已檢索 – 尚未建立索引」不持續成長；日誌中 Googlebot 參數 URL 請求 < 10%（實務目標）。

### 5.2 爬取預算的電商指標

| 指標 | 目標（實務） | 工具 |
|---|---|---|
| Googlebot 每日請求中 HTTP 200 且 canonical 的比例 | ≥ 80% | 伺服器日誌 / GSC 檢索統計 |
| 新上架產品被首次檢索時間 | ≤ 48 小時 | 日誌 + sitemap `lastmod` |
| 產品頁「已檢索尚未索引」占比 | < 10% | GSC |
| 參數 URL 請求占比 | < 10% | 日誌 |

加速新品發現：sitemap 正確 `lastmod`、首頁 / 類別頁「新品」區塊、Merchant Center feed（Google 明示 feed 可協助產品發現）。

---

## 6. 缺貨與下架頁處理

### 6.1 決策樹

**規範**：
1. **暫時缺貨**：保留頁面 200，顯示缺貨 / 到貨日 / 到貨通知與替代品，`availability` 改 `OutOfStock` 或 `BackOrder`；不 noindex、不移出 sitemap。
2. **永久下架、有直接替代**：301 到替代產品頁（不是類別或首頁），新頁註明「取代 XX」。
3. **永久下架、無替代、有外部連結 / 流量**：保留 200，標示「已停售」並列同類推薦，`availability: Discontinued`；6–12 個月流量歸零再轉 410。
4. **永久下架、無替代、無連結 / 流量**：410（404 亦可，索引處理相同），移出 sitemap 與內部連結。
5. 變體缺貨：主頁預設顯示有貨變體；全部缺貨才依上述處理。

**為什麼**：Google 對 404 / 410 索引處理相同（詳見 04）；轉址到首頁或不相關頁會成 soft 404（分面導覽指南：回 404 而非轉址通用頁）；保留缺貨頁是因 Merchant listing 需正確 `availability`，且長尾查詢仍帶流量。

**怎麼做**：CMS 建「產品狀態」欄位（active / out_of_stock / discontinued_redirect / discontinued_keep / removed）自動決定 HTTP 狀態、schema、sitemap、內部連結；缺貨頁仍顯示價格（Merchant listing 需 > 0）、到貨通知、3–6 個替代品（SSR）；缺貨 > 90 天的 SKU 每月進入永久下架審核。

**驗收方式**：GSC「軟性 404」趨近 0；Merchant Center 無「價格 / 庫存不符」；無 301 鏈。

**常見錯誤**：缺貨就 noindex（回補後要重新累積排名）；下架全 301 到首頁；大量 404 但外部連結仍指向。

---

## 7. 季節性與促銷頁的常態 URL 策略

**規範**：週期性活動用不含年份 / 日期的常態 URL（`/sale/black-friday/`、`/collections/christmas-gifts/`），活動後保留 200 並改為「下次預告 + 全年優惠 + 相關類別」，不刪、不 noindex、不換 URL。連結與歷史訊號累積在 URL 上，每年建 `/black-friday-2026/` 等於歸零；Google 強調長期穩定 URL（來源：URL structure 指南）。

**怎麼做**：活動前 4–8 週更新常態頁（Title 可加年份，URL 不變）；活動期間內部連結放首頁與導覽，非活動期收到頁尾；一次性活動結束後 301 到最接近的常態頁；促銷價 `Offer.price` 為現價、`priceType: StrikethroughPrice` 為原價，期間用 `validFrom` + `validThrough` / `priceValidUntil`（2026-07-07 新增 Sale duration，來源：Merchant listing 文件）；倒數與限時字樣不放 Title / meta。

**驗收方式**：常態活動頁 GSC 曝光呈年度週期而非每年從零；外部連結累積在同一 URL。

---

## 8. Product 結構化資料：Merchant listings 與 Product snippets

完整屬性與 JSON-LD 範本詳見 06；本節只列 2026 年電商必須知道的規則與變動。

### 8.1 兩種 rich result 的差異

| 項目 | Merchant listings（商家商品資訊） | Product snippets（產品摘要） |
|---|---|---|
| 適用頁面 | 顧客可「直接在此頁購買」的單一產品頁（含同產品變體） | 單一產品的評測 / 比價頁（含同產品多變體；內容站、聯盟站）；多商品清單 / 彙整頁不具資格 |
| `offers` | 必須是 `Offer`（不接受 `AggregateOffer`），價格 > 0 | 可 `Offer` 或 `AggregateOffer`；也可無 offer 而僅有 `review` / `aggregateRating` |
| 必填 Product | `name`、`image`、`offers`（`price` 或 `priceSpecification.price` + `priceCurrency`） | `name` + 至少一個：`review`、`aggregateRating`、`offers` |
| 解鎖功能 | Shopping 知識面板、Popular Products、價格下降通知、產品輪播、Images / Lens 標註 | 搜尋結果的評分 / 價格 / 庫存摘要 |
| GSC 報表 | Merchant listings | Product snippets |
| 不符資格 | 類別頁、只連到其他賣家的頁、禁限制商品（槍械、菸草 / 電子煙、娛樂性藥物、賭博） | 同一般結構化資料準則 |

來源：developers.google.com/search/docs/appearance/structured-data/merchant-listing（查閱 2026-11-03）。

### 8.2 2026 年重要變動（來源：Google Search Central 文件更新紀錄，查閱 2026-11-03）

| 日期 | 變動 | 影響 |
|---|---|---|
| 2026-05-20 | Merchant listing 與 Product variants 文件新增 `hasAdultConsideration`，對應 Merchant Center 的 adult 屬性 | 成人 / 限制級商品需標記 |
| 2026-07-07 | 新增 `Product.category` 用法：純文字自訂分類，或 `CategoryCode`（`inCodeSet` 指向 Google Product Taxonomy、`codeValue` 填 ID 或 `>` 分隔路徑） | 與 Merchant Center `google_product_category` 對齊，提高分類正確性 |
| 2026-07-07 | 新增「Sale duration」：`validFrom` 搭配 `validThrough` 或 `priceValidUntil`（ISO 8601），開始日 ≤ 結束日；`priceValidUntil` 不適用於 `PriceSpecification` 節點 | 促銷價可帶期間，對齊 `sale_price_effective_date` |
| 2026-07-24 | Review snippet 指南新增：不得包含假評論或未揭露誘因的評論（頁面與標記皆然） | 產品頁評論模組與 `review` 標記的合規（第 10 節） |

### 8.3 Merchant listing 的關鍵規則（容易出錯處）

1. **價格**：現價不可帶 `priceType` 或 `validForMemberTier`；劃線原價 `priceType: StrikethroughPrice`（`ListPrice` 過渡期仍接受）；會員價用 `validForMemberTier` 且不可同時有 `priceType`，兩者皆有會被忽略。
2. **一 URL 一幣別**；`Offer.url` 只能一個。
3. **運費 `OfferShippingDetails`**：`deliveryTime`、`shippingDestination.addressCountry`、`shippingRate`（與 offer 同幣別）必填；免運填 `0`；天數為非負整數 `DAY`；區域代碼僅支援 US、AU、JP。
4. **退貨 `MerchantReturnPolicy`**：`applicableCountry`、`returnPolicyCategory` 必填；有限天數需 `merchantReturnDays`；產品層級覆蓋組織層級（詳見 06）。
5. **識別碼**：`gtin` 不可為 URL；`isbn` 僅限 `Book`；`sku` 無空白；`brand.name` 只能一個。
6. **可見性**：標記的價格、庫存、評分須與頁面一致，否則 manual action（詳見 07）。
7. 汽車需 `["Product", "Car"]` 雙類型。

### 8.4 Product snippets（內容站 / 聯盟站適用）

- 評測頁：`Product` + `review`（`author`、`reviewRating`、`datePublished`）+ 可選 `aggregateRating`；多賣家比價用 `AggregateOffer`（`lowPrice`、`highPrice`、`offerCount`、`priceCurrency`）。
- 評測內容須符合 Reviews system（親身體驗、量化、優缺點 `positiveNotes` / `negativeNotes`），詳見 07。
- 「最佳 XX」等多商品清單頁：一般 Product rich result（merchant listing 與 product snippet）限單一產品頁或同產品多變體頁；清單頁可用 `ItemList` + `Product` 標記幫助 Google 理解，但不因此取得 Product rich result 資格，也不把整頁標成一個 `Product`（review 須針對單一項目）；beta carousel 另有地區與功能規則（詳見 06 §2）（來源：https://developers.google.com/search/docs/appearance/structured-data/product-snippet ，查閱 2026-11-03）。

**驗收方式**：GSC「Merchant listings」/「Product snippets」無錯誤且「有效」≈ 可索引產品頁數；Merchant Center 無「結構化資料不符」警告。

**常見錯誤**：類別頁標 `Product`；賣家頁用 `AggregateOffer`；`priceValidUntil` 過期未更新。

---

## 9. Google Merchant Center 免費商品資訊與 SEO

### 9.1 關係與策略

**規範**：所有電商都要有 Merchant Center 帳號並開啟免費商品資訊（free listings，預設開啟），同時維持頁面結構化資料；feed 與頁面資料（價格、庫存、標題）必須一致，並開啟 Merchant Center「自動更新」以在偵測到網站差異時以網站為準。

**為什麼**：Google 建議「結構化資料 + Merchant Center 並用」：前者強化頁面理解與 rich result，後者解鎖 Shopping 分頁並給更多控制；大型或頻繁更新的目錄用排程 feed 或 Merchant API，並開啟自動更新避免價格 / 庫存落差（來源：developers.google.com/search/docs/specialty/ecommerce/share-your-product-data-with-google，查閱 2026-11-03）。免費商品資訊可出現在 Search、Shopping、Maps、Images、Lens、YouTube、Gemini；新帳號預設開啟；開啟只代表「允許」，是否顯示取決於資料品質（來源：support.google.com/merchants/answer/13889434，查閱 2026-11-03）。

**免費資訊的基本要求**（同上來源）：必填 `id`、`title`、`link`、`image_link`、`price`、`description`、`availability`；條件必填 `condition`、`brand`、`gtin`（有則必填）或 `mpn`、`multipack`、`bundle`，服飾加 `color`、`size`、`age_group`、`gender` 與 `item_group_id`；需設定退貨政策與運費（AU、JP、US 與多數歐洲國家強制）；有 schema 時 Google 會對應屬性並以 GSC 檢查；即使無 feed 或 schema，Google 也可能從爬取頁面自動建立商品資料（可用 robots meta 控制）。

**怎麼做**：< 1,000 SKU 且變動少 → 自動 feed（網站爬取）+ 結構化資料；> 1,000 SKU 或每日變價 → 排程 feed 或 Merchant API。Feed `title` 與頁面 Title 對齊，`description` 用自寫描述，`google_product_category` 與 schema `category` 一致；`link` 填 canonical URL（不帶追蹤參數）；本地零售啟用 local inventory 並連結 GBP（詳見 17）；每週檢查「診斷」：遭拒、價格 / 庫存不符、圖片品質、缺 GTIN。

### 9.2 2026 年政策變動

| 日期 | 變動 | 來源 |
|---|---|---|
| 2026-07-15 公告、2026-09 生效 | Shopping ads 與 free listings 政策合併為單一「Shopping policies」，Google 聲明無新增實質要求、無更嚴執法；部分僅適用 Shopping ads 的條款會明確標示 | support.google.com/merchants/answer/17263064（查閱 2026-11-03） |
| 2026-09 中旬 | EEA 境內 Google Search 的免費商品資訊與「熱門產品」輪播被移除（追蹤工具顯示 2 日內下降 90–100%），Google Ads Liaison 回應與 DMA 有關；付費 Shopping ads 不受影響；EEA 以外（含台灣、東南亞）不受影響 | Search Engine Roundtable 2026-09-18、PPC Land 等第三方報導（查閱 2026-11-03）。官方未說明：Merchant Center「Free listings」說明頁（13889434）與 Search Central 文件更新紀錄均無 EEA 移除條目，說明頁仍寫 Search rich results「全球可用」；CSS 文件（12652686）仍寫「If you'd like to place products in free listings, you can do so through any CSS in Europe」（查閱 2026-11-03） |
| 既有 | Comparison Shopping Service（CSS）計畫適用 21 個國家（官方清單已包含瑞士與英國，不等同 EEA）；在這些國家 Shopping ads 與免費商品資訊可透過任一 CSS 投放；Google Shopping 本身也是一個 CSS，不代表必須另購第三方 CSS 服務 | support.google.com/merchants/answer/12652686（查閱 2026-11-03） |

**對專案的意義**：依第三方追蹤，歐洲市場的免費商品資訊 Search 流量於 2026-09 中旬消失（Google 無正式公告）；頁面結構化資料驅動的 Merchant listing rich result 是否同受影響，Google 官方未說明（Merchant Center 說明頁、Search Central 文件更新紀錄與 merchant-listing 文件都沒有 EEA 相關條目，2026-11-03 查閱）；只能用資料驗證：Merchant Center「成效 → 免費商品資訊」與 GSC「搜尋外觀 → Merchant listings」比對 9 月前後曲線。

---

## 10. 評論與 UGC

**規範**：
1. 只收真實購買者評論（購買驗證），顯示作者、日期、評分、文字；允許負評，不篩選。
2. 有報酬 / 折扣 / 免費商品的評論必須在評論旁清楚顯著揭露，schema `review` 不收錄未揭露的誘因評論。
3. `aggregateRating` 只計自家收集、頁面可見的評論；不匯入 Amazon / 蝦皮 / Google 評分。
4. 評論以伺服器端 HTML 輸出；「載入更多」有可爬取後備。
5. UGC 連結加 `rel="ugc nofollow"`；垃圾 UGC 有審核 SOP（詳見 07）。

**為什麼**：review snippet 指南（2026-07-24 更新）：評論須基於真實經驗；換取利益者必須清楚揭露；不得有假評論或未揭露誘因的評論；不得匯集其他網站評論；建議只接受附文字與作者名的評分；review 須針對單一項目（來源：developers.google.com/search/docs/appearance/structured-data/review-snippet，查閱 2026-11-03）。違規導致結構化資料 manual action。Merchant Center 的 Product Ratings 另有評論 feed 規範（本章不展開）。

**怎麼做**：出貨後 7–14 天自動 email 一次邀請所有買家；評論模組顯示「已驗證購買」、預設「最新」或「最有幫助」排序、可篩負評；UGC 圖片壓縮與延遲載入；第三方評論 App（Judge.me、Yotpo、Trustpilot）的 schema 不得與主題重複產生兩組 `aggregateRating`。

**驗收方式**：Rich Results Test 只偵測一組 `Product` 與 `aggregateRating`；GSC 無「評分不可見」警告。

**常見錯誤**：「留評送折扣碼」未揭露（違反 2026-07 規則與多國消費者法）；把蝦皮評分搬到官網 schema；評論只由 JavaScript 載入且未被轉譯。

---

## 11. 重複內容：製造商描述與多通路

**規範**：
1. 製造商描述可保留在「原廠說明」摺疊區，但每頁至少 150 字自寫段落與站內獨有資訊（實測、搭配、尺寸實穿、在地運送 / 保固、FAQ）。
2. 多通路（官網 + 蝦皮 + Amazon）同描述時，官網差異化放在「品牌官方」訊號：`Organization` + `brand`、保固、完整規格、教學、評論。
3. 同集團多站賣同款：各站自寫；無法時以主站為可索引版本，其他站跨網域 canonical 或 noindex。
4. 不用 AI 大量改寫製造商描述充當獨特內容（規模化內容濫用詳見 07）。

**為什麼**：Google 不懲罰重複內容本身，但會從相同版本中選一個 canonical（可能是別人的站）；獨特實用資訊是被選為 canonical 與排名的依據（詳見 05、07）。

**怎麼做**：依營收分級：A 級（前 20%）全自寫 + 影片 + FAQ；B 級（20–60%）模板 + 4–6 個獨特欄位；C 級（長尾）製造商描述 + 規格表，必要時 noindex 到有流量再補。

**驗收方式**：Siteliner / Screaming Frog 近似重複 < 20%；GSC「重複網頁，Google 選擇的標準網頁與使用者不同」為 0。

---

## 12. 站內搜尋頁

**規範**：站內搜尋頁（`/search?q=`）加 `noindex, follow`，內部連結不指向搜尋 URL。robots.txt `Disallow: /search` 只限制抓取、不保證移除索引，且與 noindex 同時設會讓 Google 讀不到 noindex——要讓已索引的頁面被移除，必須允許抓取並提供 noindex。做法：既有站先 noindex 直到 GSC 顯示已移除，再視爬取預算決定是否加 Disallow；全新站（搜尋頁從未被索引）可直接 Disallow（來源：https://developers.google.com/search/docs/crawling-indexing/block-indexing ，查閱 2026-11-03）。有穩定搜尋需求且無對應類別的搜尋詞，改建可索引的策展「集合頁」（`/collections/{term}/`）。搜尋頁可無限生成、與類別重複，spam policy 將自動生成的搜尋結果頁列為低品質（詳見 07），並會吃掉爬取預算。

**怎麼做**：每月匯出 GA4 `view_search_results` 前 200 搜尋詞 → 比對類別 / 集合頁 → 無則評估建集合頁（需策展文案與固定產品規則）。

**驗收方式**：GSC 以 `/search` 篩選為 0 索引；集合頁有獨立 Title 與曝光。

---

## 13. 國際電商（簡述）

詳見 10；電商特有：
1. 一 URL 一幣別，不依 IP 切換幣別；用 ccTLD / 子目錄 / 子網域分市場並各自 hreflang。
2. 不依 IP 自動 301（Googlebot 多自美國爬取），用提示橫幅。
3. 每市場各自的 Merchant Center 目標國家 / 語言 feed、運費與退貨政策（`shippingDestination`、`applicableCountry`）。
4. 東南亞市場：行動優先，COD 與分期資訊是轉換要素，應在產品頁可見；語言依 GSC 實際查詢決定。
5. Shopify Markets、WooCommerce 多幣別外掛、Magento store view 都要檢查 hreflang 與獨立 canonical 是否正確輸出。

---

## 14. Shopify / WooCommerce / Magento 設定要點與限制

### 14.1 Shopify

| 項目 | 現況（查閱 2026-11-03） | 做法 |
|---|---|---|
| URL 結構 | 固定前綴 `/collections/`、`/products/`、`/pages/`、`/blogs/`，無法移除 | 接受；handle 自訂 |
| collections 路徑重複 | 從集合點入產生 `/collections/{c}/products/{p}`，自動 canonical 到 `/products/{p}`，但 Googlebot 仍可能爬取甚至索引 | 改主題產品卡片連結用 `product.url \| within` 移除版本，直接輸出 `/products/{handle}` |
| robots.txt | 2021-06-18 起可用 `robots.txt.liquid` 自訂（官方文件未提方案限制；Shopify 列為「不支援的客製」，Support 不協助）；官方說明頁列出的預設阻擋：`/admin`、`/cart`、`/checkout`、`/checkouts/`、`/account`、`/orders`、`/collections/*+*`（篩選）、`/collections/*sort_by*`（排序），其餘以店內現行 `/robots.txt` 輸出為準 | 用 Liquid 迴圈 `robots.default_groups` 加減規則，不用純文字整段覆寫（官方「強烈不建議」）；發布前先存一份現行 `/robots.txt` 比對 |
| sitemap | 自動生成、自動更新（新增產品／集合／頁面／圖片／文章時），官方未提供編輯功能；含產品（主圖）、集合、頁面、文章，多網域各有獨立 sitemap | 要移出 sitemap：產品設為 Unlisted（同時移出站內搜尋與 Catalog），或對產品／頁面／文章設 `seo.hidden` metafield = 1（同時 noindex 並移出站內搜尋）；只加 noindex meta 不會移出 sitemap |
| 標籤頁 | `/collections/all/{tag}` 自動生成且可索引 | 無搜尋需求則依 `current_tags` 加 `noindex` |
| 篩選 | Search & Discovery 產生 `?filter.v.option.color=`，預設已阻擋 | 可索引分面改獨立集合頁 |
| 結構化資料 | 主題內建 `Product` JSON-LD 常缺 `shippingDetails`、`hasMerchantReturnPolicy`、`ProductGroup` | 改主題或 App；避免重複輸出 |
| 變體 | `?variant={id}` 單頁切換，canonical 自動回主 URL（single-page 模式） | 主 URL 預設顯示有貨變體 |
| 國際 | Shopify Markets 自動 hreflang | 檢查各市場 canonical 獨立 |
| 速度 | 主題 + App 腳本堆疊是 CWV 主因 | 定期清 App；Liquid 無法控制 App 載入順序 |
| 下架 | 刪除後 404；需手動「URL 轉址」 | 下架前先建轉址 |
| 限制 | 無法改 `/products/` 前綴、自訂 sitemap；Plus 以下無法改 checkout | 事前告知 |

### 14.2 WooCommerce（WordPress）

| 項目 | 現況 | 做法 |
|---|---|---|
| URL | 官方預設 base：產品 `/product/`（使用非 plain 固定網址時；plain 時為 ID 網址）、分類 `/product-category/`、標籤 `/product-tag/`；「設定 → 固定網址」可改為 shop base、shop base + 分類或自訂 base，產品 base 不得與分類／標籤 base 相同 | 上線前決定，之後不改 |
| canonical | WordPress 核心 `rel_canonical()` 在所有單篇（含 product CPT）輸出自身 URL 的 canonical；WooCommerce 核心無額外 canonical 邏輯，分類／標籤／分頁與帶參數 URL 的 canonical 靠 SEO 外掛 | 裝 Yoast / Rank Math 後由外掛接手；確認只輸出一份 |
| sitemap | WordPress 5.5 起核心 `/wp-sitemap.xml` 自動含公開 CPT（含 product）與分類法（每檔 2,000 筆）；Yoast 等外掛會停用核心 sitemap 改用自家 | 只保留一份；用外掛排除已 noindex 的屬性／標籤頁 |
| 參數 | `?orderby=`、`?min_price=`、`?filter_color=`、`?add-to-cart=` | `add-to-cart` 加 `nofollow` 並在 robots.txt 阻擋；分頁 `?paged=` 保留 |
| 屬性 / 標籤頁 | 「可封存」屬性產生 `/color/red/`；標籤頁預設可索引 | 用 Yoast / Rank Math 對屬性、標籤、空分類設 noindex；有搜尋需求的屬性可留 |
| 結構化資料 | 核心輸出基本 `Product` JSON-LD；SEO 外掛可能再輸出一份 | 只保留一份；`ProductGroup` 需外掛或自訂 |
| 變體 | `?attribute_pa_color=red` 單頁預選，canonical 回主 URL | 同 single-page 模式 |
| 速度 | 外掛堆疊、無快取、jQuery、Cart fragments AJAX | 頁面 / 物件快取、非購物頁關閉 cart fragments、WebP / AVIF |
| 站內搜尋 | `/?s=&post_type=product` | 外掛設 noindex；待 GSC 顯示已移除後再視爬取預算以 robots.txt 阻擋 `/?s=`（全新站可直接阻擋；詳見第 12 節） |
| 下架 | 改草稿回 404；用 Redirection / SEO 外掛建 301 / 410 | 下架 SOP |
| 限制 | 效能與安全依賴主機與外掛；> 50k SKU 資料庫負擔重 | 大站評估 Headless 或 Magento |

### 14.3 Magento / Adobe Commerce

| 項目 | 現況 | 做法 |
|---|---|---|
| URL rewrites | `Catalog → SEO → Use Categories Path for Product URLs`（預設 No；官方：「By default, Commerce does not include the category path in product URLs」） | 維持 No，避免多路徑重複 |
| canonical | `Use Canonical Link Meta Tag For Categories / Products`（預設皆 No：Magento 2 原始碼 `Magento/Catalog/etc/config.xml` 的 `category_canonical_tag` / `product_canonical_tag` = 0；Adobe 官方建議兩者都開） | 一定設 Yes（改前先取消 Use system value） |
| Layered navigation | 產生 `?color=5&size=12&price=` 參數，預設可爬 | 可索引分面改寫為路徑；其餘 noindex（擴充）+ robots.txt；`product_list_order` / `limit` / `dir`、`mode` 一律阻擋 |
| 多 store view | 多語 / 多幣；hreflang 需擴充或自訂 | 每個 store view 獨立 canonical 與 hreflang |
| sitemap | 內建生成器（可排程、分檔） | 排除 noindex 項目 |
| 結構化資料 | 預設無完整 `Product` JSON-LD | 擴充或自訂模板輸出 Merchant listing 必填 |
| 速度 | Full Page Cache（Varnish）、Hyvä 主題大幅改善 Luma 的 CWV | 新專案優先 Hyvä |
| 搜尋 | `/catalogsearch/result/?q=` | noindex；待 GSC 顯示已移除後再視需要 robots 阻擋（全新站可直接阻擋；詳見第 12 節） |
| 下架 | 停用回 404；URL rewrite 建 301 | 停用前建轉址 |

---

## 15. 電商 CWV 特有問題

門檻（來源：web.dev，查閱 2026-11-03；通則詳見 04）：LCP ≤ 2.5 s、INP ≤ 200 ms、CLS ≤ 0.1，以 CrUX 75 百分位為準。電商特有肇因與解法：

| 問題 | 典型肇因 | 解法 |
|---|---|---|
| LCP 慢 | 主圖 lazy-load、無 `srcset`、放在 JS 輪播內才插入 | 首屏主圖 `loading="eager"` + `fetchpriority="high"` + preload；輪播第一張 SSR；`srcset`；WebP / AVIF；CDN |
| CLS 高 | 圖片無寬高、促銷橫幅 / Cookie 列 / 推薦商品晚插入、字體切換、評分星星 JS 注入 | 圖片給尺寸或 `aspect-ratio`；橫幅預留空間；預載字型；評分與價格 SSR |
| INP 差 | 變體選擇器 / 加入購物車觸發大量 JS；聊天、A/B、個人化、熱圖佔用主執行緒；篩選即時重算 | 變體切換用輕量 JS 並拆長任務；第三方腳本互動後或閒置時載入；篩選改伺服器端或 debounce |
| 第三方腳本 | 電商頁常載 20–40 個第三方腳本 | 每季審核移除 90 天無用者；追蹤改 server-side GA4；評論 / 推薦小工具改 SSR 或 lazy iframe |
| 大量圖片 | 評論圖、顏色縮圖、推薦 | 非首屏 `loading="lazy"`；縮圖專屬小尺寸；UGC 限制尺寸並轉 WebP |
| App 堆疊（Shopify） | 每個 App 注入腳本與 CSS | 定期移除；Shopify 網站速度報告 + PageSpeed Insights |

**驗收方式**：GSC「核心網頁生命力」良好 URL ≥ 90%（實務目標）；類別頁與產品頁模板各抽 5 頁測 PageSpeed Insights；CrUX 以頁面群組檢視。

---

## 16. 狀況 → 解法表

| 症狀 | 可能原因 | 診斷步驟 | 解法 | 預防 |
|---|---|---|---|---|
| 產品頁沒有價格 / 評分 rich result | 不符 Merchant listing（類別頁、`AggregateOffer`、價格 0、圖片不可爬）；標記與可見內容不符；多組 `Product` 衝突 | Rich Results Test；GSC Merchant listings / Product snippets 報表錯誤；檢查主題 + App 是否雙輸出 | 修正為單一 `Offer`、價格 > 0、圖片可爬；移除重複 schema；確保可見一致 | 上線前模板級測試；每週看 GSC 報表 |
| GSC「已檢索 – 目前尚未建立索引」暴增 | 分面 / 排序參數被爬、薄產品頁、站內搜尋頁、分頁過深 | GSC 範例 URL 分類；伺服器日誌看 Googlebot 請求分布 | 阻擋參數、noindex 搜尋頁、合併薄頁、加強內部連結到高價值頁 | 第 5 節決策矩陣 |
| 類別頁被產品頁或篩選頁取代排名 | 類別頁內容薄 / 無文案；分面頁可索引且更精準匹配；canonical 混亂 | GSC 查詢 → 看排名 URL；檢查分面頁 canonical | 類別頁補文案與內部連結；分面頁 canonical 到類別或 noindex；或承認分面頁更適合並正式化為乾淨 URL | 分面白名單 |
| Google 索引了 `/collections/x/products/y` 而非 `/products/y`（Shopify） | 內部連結全指向 collections 版本，canonical 為軟訊號 | Screaming Frog 看 inlinks 指向哪個版本 | 改主題連結輸出 `/products/` 版本；sitemap 只含 canonical | 建站時即改 |
| 大量產品下架後流量與排名下滑 | 404 無轉址、外部連結失效、類別頁產品減少變薄 | Ahrefs 看 404 頁的反向連結；GSC 404 報表 | 有連結 / 流量者 301 到替代或保留為「已停售」頁；更新類別頁 | 第 6 節狀態欄位自動化 |
| 促銷結束後活動頁流量歸零、隔年重新開始 | 每年新 URL；活動頁結束即刪除 | 看 GSC 歷史 URL | 建常態 URL，舊年份 URL 301 過去；保留頁面內容 | 第 7 節 |
| Merchant Center 大量商品「價格不符」遭拒 | feed 與頁面價格 / 幣別不同步；頁面依 IP 顯示不同價；結構化資料為舊價 | 對照 feed、頁面、JSON-LD 三者；用美國 IP 檢查 | 開啟自動更新；一 URL 一幣別；feed 更新頻率提高或用 API | 單一價格來源（PIM / ERP 同步） |
| 評論 rich result 消失並收到結構化資料 manual action | 自我服務評論、未揭露誘因、匯集外站評論、評分不可見、評分無評論文字 | GSC「手動操作」；對照 review snippet 指南 | 移除違規評論與標記；加入揭露；只標自家可見評論；提出重新審查 | 第 10 節 |
| EEA 市場免費商品資訊流量 2026-09 後消失 | Google 因 DMA 移除 EEA 的免費商品資訊與熱門產品輪播 | Merchant Center 成效 → 免費商品資訊 依國家篩選 | 無法恢復；轉向 Merchant listing rich result（若仍顯示）、Shopping ads、類別頁自然排名、CSS 合作 | 分散流量來源 |
| 新品上架 1 週仍未被索引 | 無內部連結（只在 sitemap）、`lastmod` 不更新、爬取預算被參數吃掉、JS 才渲染的產品格 | GSC 網址檢查；日誌看是否被爬 | 首頁 / 類別「新品」區伺服器端連結；sitemap `lastmod` 正確；Merchant Center feed 提交；清理參數爬取 | 第 5.2 指標 |
| 變體頁互相競爭、Google 顯示缺貨變體 | multi-page 變體薄內容；主 URL 預設變體缺貨 | GSC 查詢對應多個變體 URL；檢查主 URL 的 `availability` | 改 single-page + `ProductGroup`；主 URL 預設有貨變體；只有獨立搜尋需求的變體獨立頁 | 第 4.5 節 |
| 類別頁 LCP > 4 s | 主圖 lazy-load、第三方腳本、輪播 JS | PageSpeed Insights 的 LCP 元素診斷；Chrome DevTools Performance | 第 15 節 | 每季 CWV 審核 |
| 站內搜尋頁被大量索引 | 無 noindex、內部連結指向搜尋結果（如「熱門搜尋」區塊） | GSC 以 `search` 篩選 | 先 noindex（允許抓取）直到 GSC 顯示已移除，再視需要 robots 阻擋；熱門搜尋改連集合頁 | 第 12 節 |
| 製造商描述導致官網排在蝦皮 / Amazon 之後 | 內容相同，第三方權威更高 | 搜尋產品名看 SERP | A 級 SKU 自寫內容 + 影片 + FAQ + 品牌訊號；B / C 級分級處理 | 第 11 節 |
| 國家站被 Google 視為重複或互相 canonical | 相同語言內容未做 hreflang、IP 轉址擋住 Googlebot | GSC 國際指定報表；用美國 IP 測試 | 完整 hreflang + 各自 canonical；取消 IP 強制轉址 | 詳見 10 |

---

## 17. 本章檢查清單

**架構**
- [ ] 產品 URL 不含類別路徑；類別 / 子類別 / 品牌頁有明確規則；產品深度 ≤ 3
- [ ] 子類別產品數 ≥ 8–10 才獨立；空類別 noindex 或 404
- [ ] XML sitemap 分檔、只含 canonical / 200 / 可索引、`lastmod` 真實
- [ ] 內部連結為伺服器端 `<a href>`；產品頁 inlinks ≥ 3

**類別頁**
- [ ] 首屏保留產品格；下方 200–500 字真實選購指南
- [ ] 分頁各自 URL、自我 canonical、可索引、`<a href>` 串接；無限捲動有後備
- [ ] 排序 / 每頁數量參數 canonical 到預設並阻擋

**產品頁**
- [ ] Title 含品牌 + 產品 + 規格；自寫描述 ≥ 150 字；規格為 HTML 表格
- [ ] ≥ 3 張可爬取圖片，提供 1:1 / 4:3 / 16:9
- [ ] 變體模式全站一致；`ProductGroup` 正確；主 URL 預設有貨變體
- [ ] 庫存狀態可見且與 `availability` 一致；缺貨仍顯示價格

**分面與爬取**
- [ ] 分面索引白名單文件化；白名單用乾淨 URL；其餘阻擋 / noindex
- [ ] 價格、尺寸、評分、排序、多選分面永不索引
- [ ] 空結果 / 無效組合回 404；日誌中參數 URL 占比 < 10%

**缺貨 / 下架 / 活動**
- [ ] CMS 有產品狀態欄位自動決定 HTTP / schema / sitemap
- [ ] 下架轉址只到直接替代；無替代則保留或 410
- [ ] 活動頁常態 URL、不含年份、活動後保留

**結構化資料與 Merchant Center**
- [ ] Merchant listing：`Offer`（非 `AggregateOffer`）、價格 > 0、`image`、`availability`、`shippingDetails`、`hasMerchantReturnPolicy`
- [ ] 促銷用 `StrikethroughPrice` + `validFrom` / `validThrough`；`category` 對齊 Google Product Taxonomy；全頁一組 `Product`
- [ ] Merchant Center 免費商品資訊開啟、feed 與頁面一致、自動更新開啟、運費與退貨設定；GSC 報表每週檢查

**評論 / 內容 / 搜尋 / 平台 / CWV**
- [ ] 評論邀請全員、無篩選；誘因評論顯著揭露；不匯入外站評分；評論 SSR
- [ ] 製造商描述分級；A 級 SKU 全自寫
- [ ] 搜尋頁 noindex（既有站待移除後再阻擋，新站可直接阻擋）；高需求搜尋詞轉集合頁
- [ ] 平台特有設定完成（Shopify collections 連結；Woo 參數與屬性頁；Magento canonical 與 URL path）
- [ ] 模板 LCP ≤ 2.5 s、INP ≤ 200 ms、CLS ≤ 0.1；第三方腳本季度審核

---

## 18. 參考來源

- Google Search Central — Ecommerce SEO guides 總覽：https://developers.google.com/search/docs/specialty/ecommerce（查閱 2026-11-03）
- Google — Designing a URL structure for ecommerce sites：https://developers.google.com/search/docs/specialty/ecommerce/designing-a-url-structure-for-ecommerce-sites（查閱 2026-11-03）
- Google — Pagination, incremental page loading, and their impact on Google Search：https://developers.google.com/search/docs/specialty/ecommerce/pagination-and-incremental-page-loading（查閱 2026-11-03）
- Google — Share your product data with Google：https://developers.google.com/search/docs/specialty/ecommerce/share-your-product-data-with-google（查閱 2026-11-03）
- Google — Managing crawling of faceted navigation URLs：https://developers.google.com/search/docs/crawling-indexing/crawling-managing-faceted-navigation（查閱 2026-11-03）
- Google — Merchant listing (Product, Offer) structured data（含 2026-05-20 `hasAdultConsideration`、2026-07-07 `category` 與 Sale duration）：https://developers.google.com/search/docs/appearance/structured-data/merchant-listing（查閱 2026-11-03）
- Google — Product variant (ProductGroup) structured data：https://developers.google.com/search/docs/appearance/structured-data/product-variants（查閱 2026-11-03）
- Google — Review snippet structured data（2026-07-24 新增假評論 / 未揭露誘因條款）：https://developers.google.com/search/docs/appearance/structured-data/review-snippet（查閱 2026-11-03）
- Google Search Central — Documentation updates（2026 變更紀錄）：https://developers.google.com/search/updates（查閱 2026-11-03）
- Google Merchant Center — Free listings for products：https://support.google.com/merchants/answer/13889434（查閱 2026-11-03）
- Google Merchant Center — Update to Google's Shopping ads and free listing policies（2026-07-15 公告、2026-09 生效）：https://support.google.com/merchants/answer/17263064（查閱 2026-11-03）
- web.dev — Core Web Vitals thresholds（LCP 2.5 s / INP 200 ms / CLS 0.1）：https://web.dev/articles/vitals（查閱 2026-11-03）
- Search Engine Roundtable — Google Search drops free product listings from EEA（2026-09-18）：https://www.seroundtable.com/google-drops-free-product-listings-eea-42113.html（查閱 2026-11-03；Google 無正式公告）
- Search Engine Roundtable — Google adds product category & sale duration to merchant listing doc（2026-07）：https://seroundtable.com/google-product-category-sale-duration-merchant-listing-41637.html（查閱 2026-11-03）
- Search Engine Roundtable — Google review snippets prohibits fake or undisclosed incentivized reviews（2026-07）：https://seroundtable.com/google-review-snippets-guidelines-update-41754.html（查閱 2026-11-03）
- Shopify Help Center — Editing robots.txt.liquid：https://help.shopify.com/en/manual/promoting-marketing/seo/editing-robots-txt（查閱 2026-11-03）
- Shopify.dev — Customize robots.txt.liquid：https://shopify.dev/docs/storefronts/themes/seo/robots-txt（查閱 2026-11-03）
- Shopify Help Center — Finding your sitemap：https://help.shopify.com/en/manual/promoting-marketing/seo/find-site-map（查閱 2026-11-03）
- Shopify Help Center — Hiding a page from search engines（Unlisted、`seo.hidden`）：https://help.shopify.com/en/manual/promoting-marketing/seo/hide-a-page-from-search-engines（查閱 2026-11-03）
- Shopify.dev — Liquid `within` filter（集合路徑產品 URL 的重複內容警告）：https://shopify.dev/docs/api/liquid/filters/within（查閱 2026-11-03）
- Shopify Blog — How to set canonical URLs on Shopify（2025-08-14；第一方主題預設全頁輸出 `canonical_url`）：https://www.shopify.com/blog/set-canonical-url-shopify（查閱 2026-11-03）
- Search Engine Journal — Shopify sites can now edit their robots.txt file（2021-06-18）：https://www.searchenginejournal.com/shopify-sites-can-now-edit-their-robots-txt-file/411036/（查閱 2026-11-03）
- WooCommerce Docs — Permalinks：https://woocommerce.com/document/woocommerce-seo/permalinks/（查閱 2026-11-03）
- WordPress Core — New XML Sitemaps Functionality in WordPress 5.5：https://make.wordpress.org/core/2020/07/22/new-xml-sitemaps-functionality-in-wordpress-5-5/（查閱 2026-11-03）
- WordPress Developer Reference — `rel_canonical()`：https://developer.wordpress.org/reference/functions/rel_canonical/（查閱 2026-11-03）
- Adobe Commerce — Catalog URLs（Use Categories Path 預設）：https://experienceleague.adobe.com/en/docs/commerce-admin/catalog/catalog/catalog-urls（查閱 2026-11-03）
- Adobe Commerce — Meta data（canonical 建議）：https://experienceleague.adobe.com/en/docs/commerce-admin/marketing/seo/meta-data（查閱 2026-11-03）
- Magento 2 原始碼 — `app/code/Magento/Catalog/etc/config.xml`（canonical 預設 0）：https://github.com/magento/magento2/blob/2.4-develop/app/code/Magento/Catalog/etc/config.xml（查閱 2026-11-03）
