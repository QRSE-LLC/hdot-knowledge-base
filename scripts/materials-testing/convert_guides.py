#!/usr/bin/env python3.13
"""Convert QRSE's HDOT reference PDFs into a Claude-navigable markdown repo.

Fidelity rules:
  - Data rows are preserved VERBATIM inside fenced blocks (column alignment intact).
  - Only repeated page-header/footer boilerplate is stripped.
  - Nothing is paraphrased, re-tabulated, or "cleaned up" -> citations stay trustworthy.
"""
import re, sys, pathlib, subprocess, textwrap

SP = pathlib.Path(sys.argv[1])          # scratchpad with extracted .txt
REPO = pathlib.Path(sys.argv[2])        # repo root to write
SRC = pathlib.Path(sys.argv[3])         # Material Cert. Project dir (source PDFs)

STG = SP / "Spec05-pro-ka-KC106.04b_Sampling_Testing_Guide_for_Acceptance_and_Verification_dated-05-16-25.txt"
MML = SP / "master-material-list.txt"
HOWTO = SP / "How to meet material and sampling testing requirements.txt"

# ---------- boilerplate that repeats on every printed page ----------
JUNK_EXACT = {
    "VERIFICATION", "SPECIFICATION", "TESTING", "QUANTITIES", "FOR SMALL",
    "SAMPLE LOCATION", "SAMPLE SIZE", "REMARKS", "MATERIALS/TESTS",
    "ACCEPTANCE SAMPLING &", "SAMPLING & TESTING", "(See Note 1)",
    "(ONLY if specified in", "contract, See Note 2)", "SAMPLING &",
    "July 2023", "ACCEPTANCE SAMPLING &  TESTING",
}
JUNK_SUB = (
    "SAMPLING AND TESTING GUIDE FOR ACCEPTANCE AND VERIFICATION",
    "Master Material Certification List",
)

def is_junk(line: str) -> bool:
    s = line.strip()
    if not s:
        return False
    if s in JUNK_EXACT:
        return True
    for j in JUNK_SUB:
        if j in s:
            return True
    # a lone page number
    if re.fullmatch(r"\d{1,3}", s):
        return True
    # header fragments that only ever appear in the column banner
    if re.fullmatch(r"(MATERIALS/TESTS|NO\.|ACCEPTANCE SAMPLING &|SAMPLING & TESTING)\s*", s):
        return True
    return False

def squeeze(lines):
    """drop junk + collapse runs of blank lines"""
    out, blank = [], 0
    for ln in lines:
        if is_junk(ln):
            continue
        if not ln.strip():
            blank += 1
            if blank > 1:
                continue
        else:
            blank = 0
        out.append(ln.rstrip())
    while out and not out[0].strip():
        out.pop(0)
    while out and not out[-1].strip():
        out.pop()
    return out

def fence(lines):
    return "```text\n" + "\n".join(lines) + "\n```"

# ---------- load sampling guide ----------
raw = STG.read_text(encoding="utf-8").splitlines()

DISCIPLINES = [
    ("01-bituminous-hwy-lb.md",   "Bituminous (HWY-LB)",   "asphalt concrete, tack coat, slurry seal, paving fabric, pavement markings"),
    ("02-geotechnical-hwy-lg.md", "Geotechnical (HWY-LG)", "subgrade, embankment, backfill, aggregate base and subbase, underdrains"),
    ("03-structural-hwy-ls.md",   "Structural (HWY-LS)",   "concrete, cement, reinforcing steel, pipe, guardrail, structural metals"),
    ("04-other-hwy-lr.md",        "HWY-LR",                "conduits, conductors, signals, lighting, signs, planting, detectable warnings"),
]
# locate discipline header line numbers (0-indexed)
disc_at = [i for i, l in enumerate(raw) if "SAMPLING AND TESTING GUIDE FOR ACCEPTANCE AND VERIFICATION" in l]
# notes block starts at first "Note 1." at column 0-ish
notes_at = next(i for i, l in enumerate(raw) if re.match(r"^Note 1\.", l.strip()))

bounds = []
for n, start in enumerate(disc_at):
    end = disc_at[n + 1] if n + 1 < len(disc_at) else notes_at
    bounds.append((start, end))

ITEM_RE = re.compile(r"^\s*(\d{1,2})\.\s+([A-Z][A-Z0-9 ,&'’\-\(\)/\.]+?)(?:\s{2,}|$)")

def split_items(lines):
    """-> [(num, title, [body lines])]"""
    idx = []
    for i, l in enumerate(lines):
        m = ITEM_RE.match(l)
        if m and len(m.group(2).strip()) > 3:
            idx.append((i, m.group(1), m.group(2).strip()))
    items = []
    for k, (i, num, title) in enumerate(idx):
        j = idx[k + 1][0] if k + 1 < len(idx) else len(lines)
        items.append((num, title, lines[i:j]))
    return items

# Spec section numbers are 1xx-8xx, optionally .NN. Must NOT be part of a larger
# number (1,000 -> 000) and must NOT be a quantity ("250 tons", "500 gals").
SPEC_RE = re.compile(r"(?<![\d,.])([1-8]\d{2}(?:\.\d{2})?)(?![\d.])")
UNIT_AFTER = re.compile(
    r"^\s*(tons?|lbs?|gals?|qts?|yd|yds|ft|cu|sq|in\.|lin|lineal|markers|percent|%|"
    r"cubic|square|bags?|sets?|specimens?|feet|inch(es)?|days?|months?|years?)\b",
    re.I,
)

def spec_refs(lines):
    """spec section numbers appearing in a block, excluding quantities"""
    found = set()
    for l in lines:
        for m in SPEC_RE.finditer(l):
            if UNIT_AFTER.match(l[m.end(): m.end() + 16]):
                continue
            found.add(m.group(1))
    return sorted(found, key=lambda s: (len(s), s))

REPO_REF = REPO / "reference" / "sampling-testing-guide"
REPO_REF.mkdir(parents=True, exist_ok=True)

written = []
for (fname, disc, blurb), (s, e) in zip(DISCIPLINES, bounds):
    body = squeeze(raw[s:e])
    items = split_items(body)
    parts = [
        "---",
        'source_document: "Sampling and Testing Guide for Acceptance and Verification"',
        'source_file: "source-pdfs/Sampling-and-Testing-Guide-for-Acceptance-and-Verification.pdf"',
        f'discipline: "{disc}"',
        'guide_revision: "July 2023 (QRSE copy dated 05-16-25)"',
        'issued_by: "HDOT Materials Testing and Research Branch (LABS)"',
        f'covers: "{blurb}"',
        "---",
        "",
        f"# Sampling and Testing Guide - {disc}",
        "",
        f"Acceptance and verification sampling frequencies for {blurb}.",
        "",
        "**How to read each item.** Columns in the preserved tables below are, left to right:",
        "`MATERIALS/TESTS` · `SPECIFICATION NO.` · `ACCEPTANCE SAMPLING & TESTING` ·",
        "`SAMPLING & TESTING FOR SMALL QUANTITIES` · `VERIFICATION SAMPLING & TESTING (only if specified in contract)` ·",
        "`SAMPLE LOCATION` · `SAMPLE SIZE` · `REMARKS`.",
        "",
        "> Qualifiers in [`00-general-notes.md`](00-general-notes.md) (Notes 1, 2, 3, 4S, 5S, 6G) change these",
        "> frequencies in specific situations. Always check the notes an item references before answering.",
        "",
        "---",
        "",
    ]
    for num, title, blines in items:
        specs = spec_refs(blines)
        parts.append(f"## Item {num}. {title}")
        parts.append("")
        if specs:
            parts.append(f"*Specification sections referenced:* {', '.join(specs)}")
            parts.append("")
        parts.append(fence(squeeze(blines)))
        parts.append("")
    (REPO_REF / fname).write_text("\n".join(parts) + "\n", encoding="utf-8")
    written.append((fname, len(items)))

# ---------- notes file (the critical qualifiers) ----------
notes_body = squeeze(raw[notes_at:])
notes_md = [
    "---",
    'source_document: "Sampling and Testing Guide for Acceptance and Verification"',
    'section: "General Notes"',
    'guide_revision: "July 2023 (QRSE copy dated 05-16-25)"',
    "---",
    "",
    "# Sampling and Testing Guide - General Notes",
    "",
    "These notes **qualify the frequencies** in the discipline tables. An answer that quotes a",
    "frequency without checking the note it references can be wrong. Summary of what each does:",
    "",
    "| Note | What it changes |",
    "|---|---|",
    "| **1** | Spec numbers listed are the common references only; for non-standard items consult LABS. |",
    "| **2** | Verification sampling applies **only when the contract specifies** contractor QC in the acceptance program (and FHWA approves it on federal-aid work). Sets the 1-to-1-for-first-5 rule. |",
    "| **3** | Test not required if the same source is already being tested on other projects (established source). |",
    "| **4S** | Plant-technician gradation testing can cut the sampling schedule to about **1/5**, supplemented by contractor QC results. |",
    "| **5S** | Defines the preferred concrete sampling locations, in order of preference. |",
    "| **6G** | Field compaction frequency is a **preliminary guide only** - it must be made project specific and documented by the **Project Engineer**. Also sets the sand-cone correlation and monthly sample-card requirements. |",
    "",
    "> **Note 6G is the most commonly misquoted item in this guide.** Compaction frequencies in the",
    "> geotechnical tables are a starting point, not a fixed requirement. Defer to the Project Engineer.",
    "",
    "---",
    "",
    "## Notes, verbatim",
    "",
    fence(notes_body),
    "",
]
(REPO_REF / "00-general-notes.md").write_text("\n".join(notes_md) + "\n", encoding="utf-8")

# ---------- sampler qualifications ----------
howto = squeeze(HOWTO.read_text(encoding="utf-8").splitlines())
qdir = REPO / "reference" / "qualifications"
qdir.mkdir(parents=True, exist_ok=True)
(qdir / "sampler-certification-and-forms.md").write_text("\n".join([
    "---",
    'source_document: "How to Meet Material Sampling and Testing Requirements"',
    'source_file: "source-pdfs/How-to-Meet-Material-Sampling-and-Testing-Requirements.pdf"',
    'applies_to: "Hawaii DOT and County Federal Aid Projects"',
    'source_revision: "Revised 2/14/2017"',
    "---",
    "",
    "# Sampler Qualifications, Forms, and Labs",
    "",
    "Covers four things an inspector gets asked about constantly:",
    "",
    "1. **Being a qualified sampler** - FSTQP certification by material class, and the annual IA evaluation.",
    "2. **How many samples to take** - points to the Sampling and Testing Guide plus contract requirements.",
    "3. **Which forms, when** - the JC (job control) transmittal / sample card.",
    "4. **Which lab may do acceptance testing.**",
    "",
    "Key durations to get right: **certification is good for 5 years**, but qualification lapses if you have",
    "not passed an IA evaluation or the FSTQP exam **within the last 12 months**.",
    "",
    "---",
    "",
    "## Source, verbatim",
    "",
    fence(howto),
    "",
]) + "\n", encoding="utf-8")

# ---------- master material list, split by spec division ----------
mml = squeeze(MML.read_text(encoding="utf-8").splitlines())
# Section headers sit in a right-hand column: "<indent>NNN    Title ...   UNIT"
# Titles are MIXED CASE, and a pay-unit column trails them.
DIVH = re.compile(r"^\s*([1-8]\d{2})\s{3,}([A-Z][^\s].*?)\s*$")
UNIT_TAIL = re.compile(
    r"\s{2,}((LS|CY|SY|CF|LF|EA|TON|FA|INCIDENTAL|GAL|SF|MGAL)"
    r"(\s*(,|or)\s*(LS|CY|SY|CF|LF|EA|TON|FA|INCIDENTAL|GAL|SF|MGAL))*)\s*$",
    re.I,
)

def clean_title(t: str) -> str:
    t = UNIT_TAIL.sub("", t)
    return re.sub(r"\s{2,}", " ", t).strip()

marks = []
for i, l in enumerate(mml):
    m = DIVH.match(l)
    if not m:
        continue
    title = clean_title(m.group(2))
    # a real header has a wordy title, not a stray code/number fragment
    if len(title) < 5 or not re.search(r"[A-Za-z]{3}", title):
        continue
    marks.append((i, m.group(1), title))
mdir = REPO / "reference" / "master-material-list"
mdir.mkdir(parents=True, exist_ok=True)

DIV_FILES = [("200", "200-earthwork.md", "Earthwork, excavation, embankment, backfill"),
             ("300", "300-bases-and-pavements.md", "Bases, subbases, asphalt pavements"),
             ("400", "400-pavements-and-surface.md", "Pavement surfacing and treatments"),
             ("500", "500-structures.md", "Bridges, concrete structures, structural metals"),
             ("600", "600-incidentals.md", "Drainage, guardrail, fencing, signs, signals, lighting"),
             ("700", "700-materials.md", "Material property requirements by material type")]

preamble = mml[: marks[0][0]] if marks else mml
buckets = {d: [] for d, _, _ in DIV_FILES}
for k, (i, num, title) in enumerate(marks):
    j = marks[k + 1][0] if k + 1 < len(marks) else len(mml)
    div = num[0] + "00"
    if div in buckets:
        buckets[div].append((num, title, mml[i:j]))

for div, fname, blurb in DIV_FILES:
    secs = buckets.get(div) or []
    if not secs:
        continue
    parts = [
        "---",
        'source_document: "Master Material Certification List"',
        'source_file: "source-pdfs/HWY-L-Master-Material-List.pdf"',
        f'spec_division: "{div}"',
        'source_revision: "rev. 5-11-18"',
        f'covers: "{blurb}"',
        "---",
        "",
        f"# Master Material Certification List - Division {div}",
        "",
        f"{blurb}. Maps **pay item / material → what certification or sampling is required → reviewing office**.",
        "",
        "Certification codes: **APL** approved product list · **COC** certificate of compliance ·",
        "**LAB** laboratory sample · **DA** designer approval. Reviewing offices are **LB** bituminous,",
        "**LG** geotechnical, **LS** structural, **LR** other.",
        "",
        "> This list is **a guide only**. The contract governs: standard plans, standard specifications,",
        "> special provisions, and project plans all take precedence over this list.",
        "> For HWY-LB, every COC requires test results.",
        "",
        "---",
        "",
    ]
    for num, title, blines in secs:
        parts += [f"## Section {num} - {title}", "", fence(squeeze(blines)), ""]
    (mdir / fname).write_text("\n".join(parts) + "\n", encoding="utf-8")

(mdir / "00-how-to-use-and-disclaimers.md").write_text("\n".join([
    "---",
    'source_document: "Master Material Certification List"',
    'section: "Preamble and disclaimers"',
    'source_revision: "rev. 5-11-18"',
    "---",
    "",
    "# Master Material Certification List - How to Use It",
    "",
    "Read these disclaimers before quoting anything from this list. It is explicitly **a guide**,",
    "prepared from information available at its issue date, and the contract documents override it.",
    "",
    fence(preamble),
    "",
]) + "\n", encoding="utf-8")

print("sampling guide files:", written)
print("mml divisions:", [(d, len(buckets.get(d) or [])) for d, _, _ in DIV_FILES])
