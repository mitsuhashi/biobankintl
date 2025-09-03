from bs4 import BeautifulSoup, NavigableString
import xlsxwriter
import re

# HTML_PATH = "intl.html"
# XLSX_PATH = "intl.xlsx"

#HTML_PATH = "intl_jp.html"
#XLSX_PATH = "intl_jp.xlsx"

HTML_PATH = "intl_jp_5-6.html"
XLSX_PATH = "intl_jp_5-6.xlsx"


def normalize_color(value: str | None) -> str | None:
    if not value:
        return None
    s = value.strip().lower()
    m = re.match(r"rgba?\s*\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)", s)
    if m:
        r, g, b = [int(m.group(i)) for i in (1, 2, 3)]
        return f"#{r:02X}{g:02X}{b:02X}"
    m = re.match(r"^#([0-9a-f]{3}|[0-9a-f]{6})$", s, re.I)
    if m:
        hx = m.group(1)
        if len(hx) == 3:
            hx = "".join(ch * 2 for ch in hx)
        return f"#{hx.upper()}"
    named = {
        "black":"black","white":"white","red":"red","blue":"blue",
        "green":"green","gray":"gray","grey":"gray","yellow":"yellow",
        "orange":"orange","purple":"purple","navy":"navy"
    }
    return named.get(s, None)

def parse_cell_runs(tag):
    """セル内を（text, bold, color）の連続runsに分解"""
    runs = []

    def push(text, bold=False, color=None):
        if not text:
            return
        if runs and runs[-1]['bold'] == bold and runs[-1]['color'] == color:
            runs[-1]['text'] += text
        else:
            runs.append({'text': text, 'bold': bold, 'color': normalize_color(color)})

    def walk(node, bold=False, color=None):
        if isinstance(node, NavigableString):
            t = str(node)
            if t:
                push(t, bold, color)
            return

        if node.name in ("br",):
            push("\n", bold, color)
            return

        b = bold or (node.name in ("b", "strong", "th"))
        c = color

        if node.name == "font" and node.get("color"):
            c = node.get("color")

        st = node.get("style", "") or ""
        if re.search(r"font-weight\s*:\s*bold", st, flags=re.I) or \
           re.search(r"font-weight\s*:\s*(\d+)", st, flags=re.I):
            m = re.search(r"font-weight\s*:\s*(\d+)", st, flags=re.I)
            if m:
                try:
                    if int(m.group(1)) >= 600:
                        b = True
                except ValueError:
                    pass
            else:
                b = True
        m = re.search(r"color\s*:\s*([^;]+)", st, flags=re.I)
        if m:
            c = m.group(1).strip()

        for child in node.children:
            walk(child, b, c)

    walk(tag, bold=False, color=None)
    return runs

def runs_to_rich_args(runs, workbook):
    """
    xlsxwriter.write_rich_string に渡す *args を作成。
    先頭は必ず非空文字列にする（空文字は禁止）。先頭が装飾付きならゼロ幅スペースで開始。
    """
    if not runs:
        return None

    args = []
    fmt_cache = {}

    def get_fmt(bold, color):
        key = (bool(bold), color or "")
        if key in fmt_cache:
            return fmt_cache[key]
        fmt_args = {}
        if bold:
            fmt_args["bold"] = True
        if color:
            fmt_args["color"] = color
        fmt = workbook.add_format(fmt_args) if fmt_args else None
        fmt_cache[key] = fmt
        return fmt

    # 先頭が装飾付きなら不可視のゼロ幅スペースで開始（Excelの空文字禁止を回避）
    first_has_style = bool(runs[0]['bold'] or runs[0]['color'])
    if first_has_style:
        args.append("\u200b")  # zero-width space

    for run in runs:
        text = run['text']
        # 空文字はスキップ（Excelで警告になるため）
        if text == "":
            continue
        fmt = get_fmt(run['bold'], run['color'])
        if fmt:
            args.append(fmt)
            args.append(text)
        else:
            if args and isinstance(args[-1], str):
                args[-1] += text
            else:
                args.append(text)

    # 念のため、最後がフォーマットで終わらないようチェック
    if args and not isinstance(args[-1], str):
        args.append("")

    # 先頭がまだ文字列でない場合の安全装置
    if not args or not isinstance(args[0], str):
        args = ["\u200b"] + args

    return args

def convert_html_to_xlsx(html_path, xlsx_path):
    with open(html_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")

    tables = soup.find_all("table")
    if not tables:
        raise RuntimeError("No <table> found")

    wb = xlsxwriter.Workbook(xlsx_path)

    for t_idx, table in enumerate(tables, start=1):
        ws = wb.add_worksheet(f"Table{t_idx}")
        current_row = 0

        # ---- thead（ヘッダ） ----
        thead = table.find("thead")
        if thead:
            for tr in thead.find_all("tr"):
                cells = tr.find_all(["td", "th"])
                for c, td in enumerate(cells):
                    runs = parse_cell_runs(td)
                    args = runs_to_rich_args(runs, wb)
                    if not args:
                        continue
                    if len(args) == 1 and isinstance(args[0], str):
                        ws.write(current_row, c, args[0])
                    else:
                        ws.write_rich_string(current_row, c, *args)
                current_row += 1

        # 1行目固定
        ws.freeze_panes(1, 0)

        # ---- tbody or 残りの tr（データ） ----
        body_rows = table.find_all("tbody")
        if body_rows:
            trs = []
            for tbody in body_rows:
                trs.extend(tbody.find_all("tr"))
        else:
            trs = [tr for tr in table.find_all("tr") if tr.find_parent("thead") is None]

        for tr in trs:
            cells = tr.find_all(["td", "th"])
            for c, td in enumerate(cells):
                runs = parse_cell_runs(td)
                args = runs_to_rich_args(runs, wb)
                if not args:
                    continue
                if len(args) == 1 and isinstance(args[0], str):
                    ws.write(current_row, c, args[0])
                else:
                    ws.write_rich_string(current_row, c, *args)
            current_row += 1

    wb.close()
    print(f"Saved: {xlsx_path}")

if __name__ == "__main__":
    convert_html_to_xlsx(HTML_PATH, XLSX_PATH)
    print(f"Saved: {XLSX_PATH}")
