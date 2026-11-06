# review：單篇內容審稿

目標：在發佈前把一篇文章（Markdown、HTML 或已上線 URL）對照 KB 的內容規範、答案優先規範、政策與市場規則，給出可直接修改的清單。

## 步驟

1. 取得內容：本機檔案直接讀；URL 用 `site_audit.py <url> --no-extra` 先拿 title / meta / H1 / JSON-LD / 語言偵測，再用 `get_page_text` 或抓 HTML 讀正文。
2. 讀規範（只讀需要的）：
   ```bash
   python3 "<SKILL_DIR>/scripts/kb_lookup.py" --section "05 9"      # 內容自評清單
   python3 "<SKILL_DIR>/scripts/kb_lookup.py" --section "05 1"      # Title；--section "05 2" meta；"05 3" 標題層級
   python3 "<SKILL_DIR>/scripts/kb_lookup.py" --section "21 4"      # 答案優先寫作（資訊型 / How-to / 比較型必讀）
   python3 "<SKILL_DIR>/scripts/kb_lookup.py" --section "14 C"      # 每篇內容發佈前檢查清單
   ```
   依內容類型加讀：混語或多語 `--section "25 3"`；聯盟評測 `--section "09 9"` 與 07 §4 thin affiliation；時效型 `--section "20 20.5"`（日期）；AdSense 站 `--section "22 2.2"` 與 `"22 2.4"`（內容政策與受限類別）；博弈相關主題 `--section "22 2"`；台灣內容 `--section "24 3"` 與 `"24 6"`；其他市場 `--section "25 6"`。
3. 逐項對照，產出評分表。重點看：搜尋意圖與標題是否一致（前 40 字）、首段是否 40–80 字直接回答、是否有第一手或在地資料（不是彙整 SERP）、作者與日期、內鏈到樞紐頁、FAQ 是否頁上可見、專有名詞英文與在地語並列一次、廣告位是否擋住首段。
4. 政策紅線出現時（博彩推廣、盜版、誹謗風險、宗教族群、皇室），標 P1 並引用章節，不要只提醒「注意」。
5. 給修改建議時直接改寫標題、首段與 meta 的範例，不只描述問題。

## 輸出格式

```
## 審稿：<標題>
| 項目 | 結果 | 說明 | 章節 |
（意圖對齊、Title、Meta、H1 與層級、首段答案、原創與 E-E-A-T、結構（表格 / 步驟 / FAQ）、內鏈、日期與更新、結構化資料、語言與混語、廣告與政策）
## P1 必改
## 建議改寫
- Title：原 → 新
- 首段：原 → 新
- Meta：原 → 新
## 發佈前清單（14 §C 未勾項目）
```
