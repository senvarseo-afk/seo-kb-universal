# market：新市場評估（台灣與任何其他市場）

目標：一頁市場簡報，回答「語言能不能變現、人在哪裡、怎麼被看到、技術要求、紅線、值不值得」。

## 步驟

1. 目標是台灣，或讀者主要用繁體中文：
   ```bash
   python3 "<SKILL_DIR>/scripts/kb_lookup.py" --toc 24                  # 台灣市場速查目錄
   python3 "<SKILL_DIR>/scripts/kb_lookup.py" --section "24 2"          # 搜尋現況
   python3 "<SKILL_DIR>/scripts/kb_lookup.py" --section "24 4"          # 社群與渠道
   python3 "<SKILL_DIR>/scripts/kb_lookup.py" --section "24 5"          # 變現
   python3 "<SKILL_DIR>/scripts/kb_lookup.py" --section "24 6"          # 法規紅線
   ```
2. 其他市場：讀通用框架，並明說知識庫沒有該國數據：
   ```bash
   python3 "<SKILL_DIR>/scripts/kb_lookup.py" --section "25 1"          # 評估流程
   python3 "<SKILL_DIR>/scripts/kb_lookup.py" --section "25 2"          # 語言與變現門檻
   python3 "<SKILL_DIR>/scripts/kb_lookup.py" --section "25 4"          # 渠道盤點
   python3 "<SKILL_DIR>/scripts/kb_lookup.py" --section "25 6"          # 法規與平台風險
   python3 "<SKILL_DIR>/scripts/kb_lookup.py" --section "10 8"          # 各市場搜尋引擎
   ```
   用可用的網路搜尋工具查 DataReportal、StatCounter、Google 支援語言清單與當地法規。查不到時列為待查證，不要用別國數字代替。
3. 語言合規是第一道門：主要語言不在 AdSense 清單時，先處理語言結構或變現方式，這不是 RPM 問題，是能不能放廣告的問題（25 §2）。
4. 共通判斷用 22 章的支援語言、08 章的 AI 搜尋現況、11 §17 的渠道評分。
5. 把「社群主張」與「查證」分開呈現，RPM 一律加註「以自家報表為準」。

## 輸出格式

```
## <國家> 市場簡報（依 24 或 25 章，整合日期 …）
| 項目 | 結論 | 證據等級 |
| 語言與 AdSense 合規 | | 查證 |
| 網路人口 / Google 市占 | | 查證 |
| 第一分發平台與在地渠道順序 | | 社群主張 |
| query 語言軌 | | 社群主張 |
| 技術要求（字型編碼、slug、首屏大小、hreflang） | | 社群主張 + KB 規範 |
| RPM 區間 | | 社群主張，以自家報表為準 |
| 法規紅線 | | 查證 |
| 值不值得做 | | Claude 判斷 |
## 起步順序（3–5 步）
## 待驗證（上線後用自家數據回填 00 §9.6）
```
