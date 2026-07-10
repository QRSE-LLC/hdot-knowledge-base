"""
OCR conversion for scanned PDFs that had no extractable text.
Uses macOS Vision framework via ocrmac.
"""

import fitz
import pathlib
import re
import tempfile
import os
from ocrmac import ocrmac

BASE = pathlib.Path("/Users/grantwork/Library/CloudStorage/GoogleDrive-grantdraperqrse@gmail.com/My Drive/2026-05_Obsidian_Knowledge_Base_Spec")
INPUT_DIR = BASE / "inputs" / "2005 Standard Specs"
OUTPUT_BASE = BASE / "raw"

SKIPPED = [
    "401C__Hot_Mix_Asphalt__HMA__Pavements__Print.pdf",
    "411B__Portland_Cement_Concrete_Pavement__Print.pdf",
    "603A__Culverts_and_Storm_Drains__Print.pdf",
    "604C__Manholes_Inlets_and_Catch_Basins__Print.pdf",
    "605A__Underdrains__Print.pdf",
    "637A__Slotted_Drains__Print.pdf",
    "640A__Lined_Drainage_Ditch_and_Concrete_Spillways_Print.pdf",
    "645C__Traffic_Control_Work_Zone__Print.pdf",
    "646A__Geocomposite_Drain__Print.pdf",
    "648A__Field-Posted_Drawings.pdf",
    "649A__Pressure_Grout.pdf",
    "655A__Dumped_Riprap__Print.pdf",
    "707A__Metal-Pipe__Print.pdf",
]


def division_folder(section_num: int) -> str:
    if section_num < 200:   return "division-100"
    elif section_num < 300: return "division-200"
    elif section_num < 400: return "division-300"
    elif section_num < 500: return "division-400"
    elif section_num < 600: return "division-500"
    elif section_num < 700: return "division-600"
    else:                   return "division-700"


def parse_stem(stem: str):
    m = re.match(r'^(\d+)', stem)
    if not m:
        return None, stem
    section_str = m.group(1)
    rest = stem[m.end():]
    rest = re.sub(r'^[A-Z]+', '', rest)
    rest = re.sub(r'^[_\-]+', '', rest)
    rest = re.sub(r'[_\s\-]*(From[_\s\-]+\w+)?[_\s\-]*Print\s*$', '', rest, flags=re.IGNORECASE)
    rest = re.sub(r'\s*\(\d+\)\s*$', '', rest)
    rest = re.sub(r'[_\-]+', ' ', rest).strip()
    rest = re.sub(r'\s{2,}', ' ', rest)
    title = rest if rest else f"Section {section_str}"
    return section_str, title


def ocr_pdf(pdf_path: pathlib.Path) -> tuple[str, int]:
    doc = fitz.open(str(pdf_path))
    page_texts = []
    total = len(doc)

    with tempfile.TemporaryDirectory() as tmpdir:
        for i, page in enumerate(doc):
            print(f"    OCR page {i+1}/{total}...", end="\r", flush=True)
            mat = fitz.Matrix(2.0, 2.0)
            pix = page.get_pixmap(matrix=mat)
            img_path = os.path.join(tmpdir, f"page_{i:04d}.png")
            pix.save(img_path)
            annotations = ocrmac.OCR(img_path, recognition_level='accurate').recognize()
            text = "\n".join([a[0] for a in annotations if a[0].strip()])
            if text.strip():
                page_texts.append(text.strip())

    print()  # newline after progress
    return "\n\n".join(page_texts), total


def main():
    ok = errors = 0

    for filename in SKIPPED:
        pdf_path = INPUT_DIR / filename
        if not pdf_path.exists():
            print(f"  MISSING  {filename}")
            continue

        stem = pdf_path.stem
        section_str, title = parse_stem(stem)
        if not section_str:
            print(f"  SKIP     {filename} (no section number)")
            continue

        section_num = int(section_str)
        div_folder = OUTPUT_BASE / division_folder(section_num)
        div_folder.mkdir(parents=True, exist_ok=True)

        slug = re.sub(r'\s+', '-', title.lower())
        slug = re.sub(r'[^a-z0-9\-]', '', slug)
        slug = re.sub(r'-{2,}', '-', slug).strip('-')
        out_name = f"{section_str}-{slug}.md" if slug else f"{section_str}.md"
        out_path = div_folder / out_name

        print(f"  OCR  {filename}")
        try:
            text, pages = ocr_pdf(pdf_path)
            if not text.strip():
                print(f"  WARN  Still no text after OCR — may be blank/diagram-only pages")
                errors += 1
                continue

            md = f"""# {section_str} — {title}

> **Source:** 2005 HDOT Standard Specifications for Road and Bridge Construction
> **File:** `inputs/2005 Standard Specs/{pdf_path.name}`
> **Pages:** {pages}
> **Extraction:** OCR (Vision)

---

{text}
"""
            out_path.write_text(md, encoding="utf-8")
            print(f"  OK   →  raw/{division_folder(section_num)}/{out_name}  ({pages}pp, {len(text):,} chars)\n")
            ok += 1

        except Exception as e:
            print(f"  ERROR  {filename}  —  {e}\n")
            errors += 1

    print(f"{'─'*60}")
    print(f"Done.  Converted: {ok}   Errors/Warn: {errors}")


if __name__ == "__main__":
    main()
