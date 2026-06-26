"""
Convert all PDFs in inputs/2005 Standard Specs/ to Markdown files in raw/
Organizes output by division subfolder (division-100 through division-700)
"""

import pdfplumber
import pathlib
import re
import sys

BASE = pathlib.Path("/Users/grantwork/Library/CloudStorage/GoogleDrive-grantdraperqrse@gmail.com/My Drive/2026-05_Obsidian_Knowledge_Base_Spec")
INPUT_DIR = BASE / "inputs" / "2005 Standard Specs"
OUTPUT_BASE = BASE / "raw"


def division_folder(section_num: int) -> str:
    if section_num < 200:   return "division-100"
    elif section_num < 300: return "division-200"
    elif section_num < 400: return "division-300"
    elif section_num < 500: return "division-400"
    elif section_num < 600: return "division-500"
    elif section_num < 700: return "division-600"
    else:                   return "division-700"


def parse_stem(stem: str):
    """Return (section_num_str, clean_title) from a filename stem."""
    m = re.match(r'^(\d+)', stem)
    if not m:
        return None, stem.replace("_", " ").replace("-", " ").strip()

    section_str = m.group(1)
    rest = stem[m.end():]

    # Strip letter suffix (e.g. 'A', 'B', 'C', 'D', 'E') right after the number
    rest = re.sub(r'^[A-Z]+', '', rest)
    # Strip leading separators
    rest = re.sub(r'^[_\-]+', '', rest)
    # Strip trailing __Print, _Print, __From_Parsons, etc.
    rest = re.sub(r'[_\s\-]*(From[_\s\-]+\w+)?[_\s\-]*Print\s*$', '', rest, flags=re.IGNORECASE)
    rest = re.sub(r'\s*\(\d+\)\s*$', '', rest)   # trailing (1), (2) etc.
    # Normalise separators → spaces
    rest = re.sub(r'[_\-]+', ' ', rest).strip()
    rest = re.sub(r'\s{2,}', ' ', rest)

    title = rest if rest else f"Section {section_str}"
    return section_str, title


def pdf_to_md(pdf_path: pathlib.Path) -> tuple[str, int]:
    """Extract text from all pages, return (markdown_text, page_count)."""
    pages = []
    with pdfplumber.open(str(pdf_path)) as pdf:
        count = len(pdf.pages)
        for page in pdf.pages:
            text = page.extract_text()
            if text and text.strip():
                pages.append(text.strip())
    return "\n\n".join(pages), count


def main():
    pdfs = sorted(INPUT_DIR.glob("*.pdf"))
    print(f"Found {len(pdfs)} PDF files\n")

    ok = skipped = errors = 0

    for pdf_path in pdfs:
        stem = pdf_path.stem
        section_str, title = parse_stem(stem)

        if section_str is None:
            print(f"  SKIP  {pdf_path.name}  (no section number)")
            skipped += 1
            continue

        section_num = int(section_str)
        div_folder = OUTPUT_BASE / division_folder(section_num)
        div_folder.mkdir(parents=True, exist_ok=True)

        # Output filename: e.g. 101-terms-abbreviation-and-definitions.md
        slug = re.sub(r'\s+', '-', title.lower())
        slug = re.sub(r'[^a-z0-9\-]', '', slug)
        slug = re.sub(r'-{2,}', '-', slug).strip('-')
        out_name = f"{section_str}-{slug}.md" if slug else f"{section_str}.md"
        out_path = div_folder / out_name

        try:
            text, pages = pdf_to_md(pdf_path)
            if not text.strip():
                print(f"  EMPTY {pdf_path.name}  (no extractable text)")
                skipped += 1
                continue

            md = f"""# {section_str} — {title}

> **Source:** 2005 HDOT Standard Specifications for Road and Bridge Construction
> **File:** `inputs/2005 Standard Specs/{pdf_path.name}`
> **Pages:** {pages}

---

{text}
"""
            out_path.write_text(md, encoding="utf-8")
            print(f"  OK    {pdf_path.name}  →  raw/{division_folder(section_num)}/{out_name}  ({pages}pp)")
            ok += 1

        except Exception as e:
            print(f"  ERROR {pdf_path.name}  —  {e}")
            errors += 1

    print(f"\n{'─'*60}")
    print(f"Done.  Converted: {ok}   Skipped: {skipped}   Errors: {errors}")


if __name__ == "__main__":
    main()
