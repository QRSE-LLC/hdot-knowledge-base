"""
Reorganize raw/ folder:
  1. Rename all generic filenames (section-XXX) to descriptive slugs from TOC titles
  2. Reorganize Division 600 into topic subfolders
  3. Update H1 headers inside each file to match corrected TOC titles
  4. Rewrite source-index.md with updated paths
"""

import pathlib
import re
import shutil
from datetime import date

BASE     = pathlib.Path("/Users/grantwork/Library/CloudStorage/GoogleDrive-grantdraperqrse@gmail.com/My Drive/2026-05_Obsidian_Knowledge_Base_Spec")
RAW      = BASE / "raw"
IDX_FILE = BASE / "indexes" / "source-index.md"

# ── Exact titles from the Table of Contents ───────────────────────────────────
TOC_TITLES = {
    "101": "Terms, Abbreviations, and Definitions",
    "102": "Reserved",
    "103": "Reserved",
    "104": "Scope of Work",
    "105": "Control of Work",
    "106": "Material Restrictions and Requirements",
    "107": "Legal Relations and Responsibility to Public",
    "108": "Prosecution and Progress",
    "109": "Measurement and Payment",
    "201": "Clearing and Grubbing",
    "202": "Removal of Structures and Obstructions",
    "203": "Excavation and Embankment",
    "204": "Excavation and Backfill for Miscellaneous Facilities",
    "205": "Excavation and Backfill for Bridge and Retaining Structures",
    "206": "Excavation and Backfill for Drainage Facilities",
    "207": "Ditch and Channel Excavation",
    "208": "Leveling Surfaces",
    "209": "Temporary Water Pollution, Dust, and Erosion Control",
    "210": "Dressing of Shoulders",
    "211": "Exploratory Work at Structure Footings",
    "301": "Hot Mix Asphalt Base Course",
    "304": "Aggregate Base Course",
    "305": "Aggregate Subbase Course",
    "306": "Untreated Permeable Base Course",
    "310": "Brooming Off",
    "312": "Hot Mix Glassphalt Base Course",
    "313": "Permeable Separator",
    "314": "Controlled Low-Strength Material (CLSM) for Utilities and Structures",
    "401": "Hot Mix Asphalt Pavement",
    "404": "Slurry Seal",
    "407": "Tack Coat",
    "411": "Portland Cement Concrete Pavement",
    "412": "Paving Fabric",
    "414": "Reconstruction of Weakened Pavement Areas",
    "415": "Cold Planing of Existing Pavement",
    "420": "Primer for Untreated Permeable Base Course",
    "501": "Steel Structures",
    "502": "Timber Structures",
    "503": "Concrete Structures",
    "504": "Prestressed Concrete Members",
    "505": "Piling",
    "506": "Bearing and Expansion Plates",
    "507": "Railings",
    "508": "Cement Rubble Masonry",
    "511": "Drilled Shafts",
    "601": "Structural Concrete",
    "602": "Reinforcing Steel",
    "603": "Culverts and Storm Drains",
    "604": "Manholes, Inlets, and Catch Basins",
    "605": "Underdrains",
    "606": "Guardrail",
    "607": "Chain Link Fences and Gates",
    "610": "Reinforced Concrete Driveways",
    "611": "Hand-Laid Riprap",
    "612": "Grouted Rubble Paving",
    "613": "Centerline and Reference Survey Monuments",
    "614": "Street Survey Monuments",
    "616": "Irrigation System",
    "617": "Planting Soil",
    "619": "Planting",
    "620": "Dust Control",
    "622": "Roadway and Sign Lighting System",
    "623": "Traffic Signal System",
    "624": "Water System",
    "625": "Sewer System",
    "626": "Manholes and Valve Boxes for Water and Sewer Systems",
    "628": "Shotcrete",
    "629": "Pavement Markings",
    "630": "Traffic Control Guide Signs",
    "631": "Traffic Control Regulatory, Warning, and Miscellaneous Signs",
    "632": "Markers",
    "633": "Falsework Lighting",
    "634": "Portland Cement Concrete Sidewalks",
    "635": "Hot Mix Asphalt Sidewalks",
    "637": "Slotted Drains",
    "638": "Portland Cement Concrete Curb and Gutter",
    "639": "Asphalt Concrete Curb and Gutter",
    "640": "Lined Drainage Ditch and Concrete Spillways",
    "641": "Hydro-Mulch Seeding",
    "642": "Landscape Maintenance",
    "643": "Maintenance of Existing Landscape Areas",
    "644": "Repairing of Existing Sprinkler System",
    "645": "Work Zone Traffic Control",
    "646": "Geocomposite Drain",
    "647": "Fiber Optic Cable",
    "648": "Field-Posted Drawings",
    "649": "Pressure Grout",
    "650": "Curb Ramps",
    "653": "Concrete Culvert Lining",
    "654": "Restrainers",
    "655": "Dumped Riprap",
    "656": "Drilling Holes and Installing Dowel Reinforcing Bars",
    "692": "Voluntary Partnering",
    "693": "Terminal Impact Attenuator",
    "698": "Training",
    "699": "Mobilization",
    "701": "Hydraulic Cement",
    "702": "Bituminous Materials",
    "703": "Aggregates",
    "704": "Masonry Units",
    "705": "Joint Materials for Concrete Structures",
    "706": "Concrete, Clay, and Plastic Pipe",
    "707": "Metal Pipe",
    "708": "Paints",
    "709": "Reinforcing Steel, Wire Rope, and Prestressing Steel",
    "710": "Guardrail Materials",
    "711": "Concrete Curing Materials and Admixtures",
    "712": "Miscellaneous Materials",
    "713": "Structural Steel and Related Materials",
    "714": "Structural Timber and Related Materials",
    "715": "Aluminum",
    "716": "Geotextiles",
    "717": "Cullet and Cullet-Made Materials",
    "718": "Steel Fasteners",
    "722": "Chain Link Fence Materials",
    "750": "Traffic Control Sign and Marker Materials",
    "755": "Pavement Marking Materials",
    "760": "Roadway and Sign Lighting System Materials",
    "770": "Traffic Signal Materials",
}

# ── Division 600 topic subfolder assignments ──────────────────────────────────
DIV600_SUBFOLDERS = {
    "concrete":               ["601","602","628","649","654","656"],
    "drainage":               ["603","604","605","611","637","640","646","653","655"],
    "roadway-features":       ["606","607","610","612","634","635","638","639","650","693"],
    "survey":                 ["613","614"],
    "signing-traffic-control":["629","630","631","632","645","648"],
    "lighting-electrical":    ["622","623","633","647"],
    "landscaping":            ["616","617","619","620","641","642","643","644"],
    "utilities":              ["624","625","626"],
    "administrative":         ["692","698","699"],
}
SEC_TO_SUB600 = {sec: sub for sub, secs in DIV600_SUBFOLDERS.items() for sec in secs}

# ── Helpers ───────────────────────────────────────────────────────────────────
OCR_SECTIONS = {"401","411","603","604","605","637","640","645","646","648","649","655","707"}

DIV_NAMES = {
    "division-100": "General Provisions",
    "division-200": "Earthwork",
    "division-300": "Base Courses",
    "division-400": "Pavements",
    "division-500": "Structures",
    "division-600": "Incidental Construction",
    "division-700": "Materials",
}

def to_slug(title):
    s = title.lower()
    s = re.sub(r'[^a-z0-9\s]', '', s)
    s = re.sub(r'\s+', '-', s.strip())
    s = re.sub(r'-+', '-', s)
    return s

def target_path(sec, current_div):
    title  = TOC_TITLES.get(sec, sec)
    slug   = to_slug(title)
    fname  = f"{sec}-{slug}.md"

    if current_div == "division-600":
        sub = SEC_TO_SUB600.get(sec)
        if sub:
            return RAW / "division-600" / sub / fname
    return RAW / current_div / fname

# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    moves   = []   # (old_path, new_path, sec, title)
    no_move = []   # already correctly named and placed

    for md in sorted(RAW.rglob("*.md")):
        current_div = md.parent.name if md.parent.parent == RAW else md.parent.parent.name
        if current_div not in DIV_NAMES:
            continue  # skip TEMPLATE.md or stray files

        sec_m = re.match(r'^(\d+)', md.stem)
        if not sec_m:
            continue
        sec = sec_m.group(1)

        new_path = target_path(sec, current_div if md.parent.parent == RAW else "division-600")
        if new_path == md:
            no_move.append(md.name)
        else:
            title = TOC_TITLES.get(sec, sec)
            moves.append((md, new_path, sec, title))

    print(f"Files to move/rename: {len(moves)}")
    print(f"Files already correct: {len(no_move)}")
    print()

    # Create all needed directories
    needed_dirs = set(m[1].parent for m in moves)
    for d in sorted(needed_dirs):
        d.mkdir(parents=True, exist_ok=True)
        print(f"  mkdir  {d.relative_to(BASE)}")

    print()

    # Move and update H1 header in each file
    for old_path, new_path, sec, title in moves:
        content = old_path.read_text(encoding="utf-8")
        # Fix H1: replace first line
        lines = content.split("\n")
        lines[0] = f"# {sec} — {title}"
        content = "\n".join(lines)
        new_path.write_text(content, encoding="utf-8")
        old_path.unlink()
        print(f"  MOVE  {old_path.relative_to(RAW)}  →  {new_path.relative_to(RAW)}")

    # Clean up empty Division 600 flat folder (if all files moved out)
    div600_flat = RAW / "division-600"
    leftover = [f for f in div600_flat.iterdir() if f.is_file()]
    if not leftover:
        print(f"\n  division-600/ flat files all moved — subfolders only remain")

    print(f"\nRebuilding source index...")
    rebuild_index()
    print("Done.")


def rebuild_index():
    # Collect all files grouped by division (and subfolder for 600)
    entries = []  # (sec_int, sec, title, pages, method, rel_path, div_display)

    for md in sorted(RAW.rglob("*.md")):
        # Determine display division
        parts = md.relative_to(RAW).parts
        if len(parts) == 2:
            div_key = parts[0]   # division-XXX/file.md
            sub     = None
        elif len(parts) == 3:
            div_key = parts[0]   # division-600/subfolder/file.md
            sub     = parts[1]
        else:
            continue

        if div_key not in DIV_NAMES:
            continue

        sec_m = re.match(r'^(\d+)', md.stem)
        if not sec_m:
            continue
        sec = sec_m.group(1)
        title = TOC_TITLES.get(sec, md.stem)

        content = md.read_text(encoding="utf-8")
        pages_m = re.search(r'\*\*Pages:\*\*\s+(\d+)', content)
        pages   = pages_m.group(1) if pages_m else "?"
        method  = "OCR" if sec in OCR_SECTIONS else ("Word (.doc)" if sec == "613" else "Text")

        entries.append((int(sec), sec, title, pages, method, str(md.relative_to(BASE)), div_key, sub))

    entries.sort(key=lambda x: x[0])

    lines = [
        "# Source Index",
        "",
        f"> **Project:** QRSE Knowledge Base — Proof of Concept  ",
        f"> **Source:** 2005 HDOT Standard Specifications for Road and Bridge Construction  ",
        f"> **Total sections:** {len(entries)}  ",
        f"> **Last updated:** {date.today().isoformat()}  ",
        f"> **Status legend:** `Raw Extracted` = Markdown in raw/ · `Wiki Page Created` = wiki/ page exists",
        "",
        "---",
        "",
    ]

    # Group by division
    from itertools import groupby
    for div_key, group in groupby(entries, key=lambda x: x[6]):
        label = DIV_NAMES[div_key]
        rows  = list(group)
        lines.append(f"## {div_key.replace('-', ' ').title()} — {label}")
        lines.append("")

        if div_key == "division-600":
            # Sub-group by subfolder
            sub_groups = {}
            for row in rows:
                sub = row[7] or "other"
                sub_groups.setdefault(sub, []).append(row)
            for sub in ["concrete","drainage","roadway-features","survey",
                        "signing-traffic-control","lighting-electrical",
                        "landscaping","utilities","administrative"]:
                if sub not in sub_groups:
                    continue
                sub_label = sub.replace("-", " ").title()
                lines.append(f"### {sub_label}")
                lines.append("")
                lines.append("| Section | Title | Pages | Method | Raw File | Status |")
                lines.append("|---------|-------|-------|--------|----------|--------|")
                for _, sec, title, pages, method, rel, *_ in sub_groups[sub]:
                    lines.append(f"| {sec} | {title} | {pages} | {method} | [{rel}]({rel}) | `Raw Extracted` |")
                lines.append("")
        else:
            lines.append("| Section | Title | Pages | Method | Raw File | Status |")
            lines.append("|---------|-------|-------|--------|----------|--------|")
            for _, sec, title, pages, method, rel, *_ in rows:
                lines.append(f"| {sec} | {title} | {pages} | {method} | [{rel}]({rel}) | `Raw Extracted` |")
            lines.append("")

    lines += [
        "---",
        "",
        "## Skipped / Not Converted",
        "",
        "| File | Reason |",
        "|------|--------|",
        "| `E_Table_of_Contents.pdf` | No section number — table of contents only |",
        "",
        "## Missing from Inputs",
        "",
        "| Section | Title | Reason |",
        "|---------|-------|--------|",
        "| 696 | Field Office and Project Site Laboratory | Listed in TOC but no source file found in inputs/ |",
        "",
        "---",
        "",
        f"*Index titles verified against official 2005 HDOT Standard Specifications Table of Contents.*  ",
        f"*Last updated: {date.today().isoformat()}*",
    ]

    IDX_FILE.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
