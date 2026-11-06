#!/usr/bin/env python3
"""在 SEO 知識庫中查關鍵字或列印指定小節，只回傳需要的片段，避免整章載入 context。

用法：
  kb_lookup.py <關鍵字> [更多關鍵字...]        # 全文搜尋，回傳「章節 §小節 + 前後行」
  kb_lookup.py --section "24 §6"               # 列印某章某小節全文（§ 可省略，24 6 亦可）
  kb_lookup.py --section "12 H5"               # 第 12 章的狀況編號（A1–J5、E13、H5…）
  kb_lookup.py --symptom <症狀關鍵字>           # 查 00 §6 症狀快速查找表
  kb_lookup.py --toc 10                        # 列出某章目錄
選項：--context N（前後行數，預設 6）、--max N（最多幾筆，預設 12）、--all-hits（不去重）
"""
import os, re, sys, glob, argparse

KB = os.environ.get("SEO_KB") or os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "references", "kb")

def chapter_files(include_readme=False):
    files = sorted(glob.glob(os.path.join(KB, "[0-9][0-9]-*.md")))
    files = [f for f in files if "完整版" not in f]
    if not include_readme:
        files = [f for f in files if "README" not in f]
    return files

def chapter_file(num):
    num = str(num).zfill(2)
    if num == "00":
        for f in chapter_files():
            if "快速啟動指南" in f: return f
    for f in chapter_files():
        if os.path.basename(f).startswith(num + "-"):
            return f
    sys.exit(f"找不到第 {num} 章")

HEAD = re.compile(r"^(#{1,4})\s+(.*)")

def iter_sections(path):
    """yield (level, title, start_line, end_line, lines)"""
    lines = open(path, encoding="utf-8").read().splitlines()
    heads = [(i, len(m.group(1)), m.group(2).strip()) for i, l in enumerate(lines) if (m := HEAD.match(l))]
    for k, (i, lvl, title) in enumerate(heads):
        end = len(lines)
        for j, l2, _ in heads[k + 1:]:
            if l2 <= lvl:
                end = j; break
        yield lvl, title, i, end, lines

def section_label(path, line_no):
    """回傳該行所屬的最近小節標題鏈，例如 '24 §6 法規紅線'"""
    lines = open(path, encoding="utf-8").read().splitlines()
    chain = {}
    for i in range(line_no, -1, -1):
        m = HEAD.match(lines[i])
        if m:
            lvl = len(m.group(1))
            if lvl not in chain and all(l > lvl for l in chain):
                chain[lvl] = m.group(2).strip()
            if lvl == 2 or lvl == 1 and chain:
                if lvl == 1: break
    parts = [chain[l] for l in sorted(chain) if l >= 2]
    return " > ".join(parts)

def chap_num(path):
    return os.path.basename(path)[:2]

def cmd_search(words, ctx, maxn, dedup):
    pats = [re.compile(re.escape(w), re.I) for w in words]
    hits = 0; seen = set()
    for f in chapter_files():
        lines = open(f, encoding="utf-8").read().splitlines()
        for i, l in enumerate(lines):
            if all(p.search(l) for p in pats):
                label = section_label(f, i)
                key = (f, label)
                if dedup and key in seen: continue
                seen.add(key)
                hits += 1
                print(f"\n### [{chap_num(f)}] {label}  （{os.path.basename(f)}:{i+1}）")
                lo, hi = max(0, i - ctx), min(len(lines), i + ctx + 1)
                for j in range(lo, hi):
                    mark = "➜ " if j == i else "  "
                    print(mark + lines[j])
                if hits >= maxn:
                    print(f"\n（已達 {maxn} 筆上限，加 --max 或縮小關鍵字）"); return
    if hits == 0:
        print("查無結果。試試同義詞、英文術語，或 --symptom 查症狀表。")

def cmd_section(spec):
    m = re.match(r"\s*(\d{1,2})\s*[§ ]*\s*(.+?)\s*$", spec)
    if not m: sys.exit("格式：--section \"24 §6\" 或 \"12 H5\"")
    num, sub = m.group(1), m.group(2)
    path = chapter_file(num)
    sub_norm = sub.replace("§", "").strip()
    cands = []
    for lvl, title, s, e, lines in iter_sections(path):
        t = title.strip()
        # 匹配 "8.1 ..."、"8. ..."、"H5. ..."、"(11) ..."
        if re.match(rf"^{re.escape(sub_norm)}(\.|\s|$|\))", t) or re.match(rf"^\({re.escape(sub_norm)}\)", t) \
           or t.startswith(sub_norm + ".") or t.startswith(sub_norm + " "):
            cands.append((lvl, title, s, e, lines))
    if not cands:
        # 退而求其次：標題含該字串
        for lvl, title, s, e, lines in iter_sections(path):
            if sub_norm.lower() in title.lower():
                cands.append((lvl, title, s, e, lines))
    if not cands: sys.exit(f"第 {num} 章找不到小節 {sub}；用 --toc {num} 看目錄")
    lvl, title, s, e, lines = cands[0]
    print(f"# [{num}] {title}  （{os.path.basename(path)}:{s+1}-{e}）\n")
    print("\n".join(lines[s:e]).rstrip())

def cmd_symptom(words):
    path = chapter_file("00")
    lines = open(path, encoding="utf-8").read().splitlines()
    in_tab = False; found = 0
    pats = [re.compile(re.escape(w), re.I) for w in words]
    for l in lines:
        if l.startswith("## 6."): in_tab = True; continue
        if in_tab and l.startswith("## "): break
        if in_tab and l.startswith("|") and all(p.search(l) for p in pats) and "第一站" not in l:
            print(l); found += 1
    if not found:
        print("症狀表無此關鍵字，改用全文搜尋：")
        cmd_search(words, 6, 12, True)
    else: print("\n（欄位：症狀 | 第一站 | 接著看。用 --section 印出第一站的小節）")

def cmd_toc(num):
    path = chapter_file(num)
    for lvl, title, s, e, _ in iter_sections(path):
        if lvl <= 3: print("  " * (lvl - 1) + title)

if __name__ == "__main__":
    ap = argparse.ArgumentParser(add_help=False)
    ap.add_argument("words", nargs="*")
    ap.add_argument("--section"); ap.add_argument("--symptom", nargs="+"); ap.add_argument("--toc")
    ap.add_argument("--context", type=int, default=6); ap.add_argument("--max", type=int, default=12)
    ap.add_argument("--all-hits", action="store_true"); ap.add_argument("-h", "--help", action="store_true")
    a = ap.parse_args()
    if a.help or (not a.words and not a.section and not a.symptom and not a.toc):
        print(__doc__); sys.exit(0)
    if not os.path.isdir(KB): sys.exit(f"知識庫路徑不存在：{KB}（可用環境變數 SEO_KB 指定）")
    if a.section: cmd_section(a.section)
    elif a.symptom: cmd_symptom(a.symptom)
    elif a.toc: cmd_toc(a.toc)
    else: cmd_search(a.words, a.context, a.max, not a.all_hits)
