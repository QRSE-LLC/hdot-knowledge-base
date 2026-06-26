from docx import Document
from docx.shared import Pt, RGBColor, Inches, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import copy

OUTPUT_PATH = "obsidian-knowledge-base-spec-scope-of-work.docx"

# Colors
DARK_BLUE = RGBColor(0x1F, 0x38, 0x64)
BLACK = RGBColor(0x00, 0x00, 0x00)
GRAY = RGBColor(0xD9, 0xD9, 0xD9)

doc = Document()

# ── Page setup: US Letter, 1-inch margins ─────────────────────────────────────
section = doc.sections[0]
section.page_width  = 12240
section.page_height = 15840
for attr in ("left_margin","right_margin","top_margin","bottom_margin"):
    setattr(section, attr, Inches(1))

# ── Helpers ───────────────────────────────────────────────────────────────────

def set_font(run, size=11, bold=False, color=BLACK):
    run.font.name = "Arial"
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.color.rgb = color

def heading(doc, text, size=14, space_before=240, space_after=120):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(space_before / 20)
    p.paragraph_format.space_after  = Pt(space_after  / 20)
    r = p.add_run(text)
    set_font(r, size=size, bold=True, color=DARK_BLUE)
    return p

def body(doc, text, space_before=6, space_after=6):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after  = Pt(space_after)
    r = p.add_run(text)
    set_font(r)
    return p

def bullet(doc, text, bold_prefix=None):
    p = doc.add_paragraph(style="List Bullet")
    p.paragraph_format.space_before = Pt(3)
    p.paragraph_format.space_after  = Pt(3)
    if bold_prefix:
        rb = p.add_run(bold_prefix)
        set_font(rb, bold=True)
        r = p.add_run(text)
        set_font(r)
    else:
        r = p.add_run(text)
        set_font(r)
    return p

def hr(doc):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after  = Pt(4)
    pPr = p._p.get_or_add_pPr()
    pBdr = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), "6")
    bottom.set(qn("w:space"), "1")
    bottom.set(qn("w:color"), "AAAAAA")
    pBdr.append(bottom)
    pPr.append(pBdr)
    return p

def timeline_table(doc, rows):
    table = doc.add_table(rows=1 + len(rows), cols=2)
    table.style = "Table Grid"
    # Header
    hdr = table.rows[0]
    for i, txt in enumerate(("Phase", "Duration")):
        cell = hdr.cells[i]
        cell.paragraphs[0].clear()
        run = cell.paragraphs[0].add_run(txt)
        set_font(run, bold=True)
        tc = cell._tc
        tcPr = tc.get_or_add_tcPr()
        shd = OxmlElement("w:shd")
        shd.set(qn("w:fill"), "D9D9D9")
        shd.set(qn("w:val"), "clear")
        tcPr.append(shd)
    # Data rows
    for ri, (phase, duration) in enumerate(rows):
        row = table.rows[ri + 1]
        for ci, txt in enumerate((phase, duration)):
            row.cells[ci].paragraphs[0].clear()
            run = row.cells[ci].paragraphs[0].add_run(txt)
            set_font(run)
    return table

# ── Title block ───────────────────────────────────────────────────────────────
title_p = doc.add_paragraph()
title_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
title_p.paragraph_format.space_before = Pt(0)
title_p.paragraph_format.space_after  = Pt(6)
tr = title_p.add_run("Scope of Work: Obsidian Knowledge Base — Proof of Concept")
set_font(tr, size=18, bold=True)

for line in ("Prepared by: QRSE", "Date: 2026-05-20", "Version: 1.0"):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after  = Pt(2)
    r = p.add_run(line)
    set_font(r, size=11)

hr(doc)

# ── 1. Project Overview ───────────────────────────────────────────────────────
heading(doc, "Project Overview")
body(doc,
    "This is a solo internal R&D effort to validate whether an LLM-assisted knowledge base "
    "workflow can be applied to QRSE's existing technical documentation. The 2005 HDOT Standard "
    "Specifications for Road and Bridge Construction and associated Special Provisions serve as "
    "the test dataset. Over three days, Grant will ingest source documents, compile a structured "
    "Markdown wiki in Obsidian, and demonstrate functional search and Q&A capability against the "
    "compiled content — without returning to the source PDFs."
)

hr(doc)

# ── 2. Objectives ─────────────────────────────────────────────────────────────
heading(doc, "Objectives")
objectives = [
    "Establish a local-first, cloud-independent knowledge base infrastructure using Obsidian and plain Markdown files",
    "Ingest priority sections of the 2005 HDOT Standard Specifications (Divisions 100–600) into a structured raw document store",
    "Compile a linked wiki of 15–25 structured pages covering key spec concepts, divisions, and procedures",
    "Demonstrate functional search and Q&A capability against the compiled wiki",
    "Produce a lessons-learned record to inform scaling of this workflow to the QRSE intern program and internal training",
]
for obj in objectives:
    bullet(doc, obj)

hr(doc)

# ── 3. Tasks & Responsibilities ───────────────────────────────────────────────
heading(doc, "Tasks & Responsibilities")

phases = [
    ("Phase 1 — Setup & Configuration", [
        "Configure the Obsidian vault using the project folder as the root, establishing the raw/, wiki/, indexes/, and outputs/ directory structure.",
        "Define and document the standard wiki page template to ensure consistent formatting across all compiled pages.",
    ]),
    ("Phase 2 — Data Ingest", [
        "Collect the 2005 HDOT Standard Specifications PDF and representative Special Provisions samples and place them in the read-only inputs/ directory.",
        "Convert priority spec sections (Divisions 100, 102, 200, 501, 601) from PDF to Markdown and store in raw/ using subdivision naming conventions.",
        "Log every ingested source in indexes/source-index.md with document type, topic area, date, and ingestion status.",
    ]),
    ("Phase 3 — Wiki Compilation", [
        "Generate one structured wiki page per ingested section using the standard template (Summary, Key Terms, Spec References, QRSE Notes, Related Pages, Source).",
        "Establish bidirectional cross-reference links between related wiki pages, with a minimum of three links per page.",
        "Build indexes/concept-index.md as a categorized, linked inventory of all concepts covered in the wiki.",
        "Build indexes/glossary.md with definitions for all technical terms and abbreviations appearing in the wiki.",
        "Document content gaps, ambiguous language, and items requiring further research in indexes/open-questions.md.",
    ]),
    ("Phase 4 — Validation", [
        "Run five pre-defined test questions against the wiki and rate each answer on a 1–5 completeness scale (5 = fully answered from wiki alone, no PDF required).",
        "Produce outputs/drafts/search-test-results.md documenting each question, the wiki's answer, source sections referenced, and the rating.",
        "Write tasks/lessons.md capturing what worked, what failed, and recommendations for scaling the system to broader use.",
    ]),
]

for phase_name, tasks in phases:
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after  = Pt(2)
    r = p.add_run(phase_name)
    set_font(r, size=11, bold=True)
    for task in tasks:
        bullet(doc, task)

hr(doc)

# ── 4. Deliverables ───────────────────────────────────────────────────────────
heading(doc, "Deliverables")
deliverables = [
    "Configured Obsidian vault with defined folder structure (raw/, wiki/, indexes/, outputs/)",
    "Source index (indexes/source-index.md) logging all ingested documents with status",
    "15–25 structured, cross-linked wiki pages covering key spec divisions, concepts, and procedures",
    "Concept index (indexes/concept-index.md) and glossary (indexes/glossary.md)",
    "Search and Q&A test log (outputs/drafts/search-test-results.md) with five rated test questions",
    "Lessons learned document (tasks/lessons.md) with recommendations for scaling to the intern program",
]
for d in deliverables:
    bullet(doc, d)

hr(doc)

# ── 5. Timeline ───────────────────────────────────────────────────────────────
heading(doc, "Timeline")
timeline_rows = [
    ("Start Date",                       "2026-05-20"),
    ("Day 1 — Setup + Raw Ingest",       "1 day (2026-05-20)"),
    ("Day 2 — Wiki Build",               "1 day (2026-05-21)"),
    ("Day 3 — Test + Validate",          "1 day (2026-05-22)"),
    ("Estimated Completion",             "2026-05-22"),
]
timeline_table(doc, timeline_rows)

hr(doc)

# ── 6. Supervision & Support ──────────────────────────────────────────────────
heading(doc, "Supervision & Support")
body(doc,
    "This is a solo internal R&D effort led by Grant with no external oversight requirements. "
    "Claude Code serves as the primary LLM tool for all wiki compilation, indexing, and content "
    "generation tasks. Progress is self-tracked via tasks/todo.md, with a lessons-learned review "
    "completed at the close of Day 3."
)

hr(doc)

# ── 7. Expected Outcomes ──────────────────────────────────────────────────────
heading(doc, "Expected Outcomes")
outcomes = [
    "A validated, repeatable workflow for converting raw technical documents into a searchable Markdown knowledge base",
    "Demonstrated proof that LLM-compiled wikis can reduce time-to-answer for spec-related questions without returning to source PDFs",
    "A tested vault structure and wiki page template ready to hand to summer interns for broader rollout",
    "An identified roadmap for extending the system to other QRSE document types (AASHTO, FHWA guidance, HDOT Design Criteria)",
    "A foundation for future subscription product development — including change order evaluation and NEPA support — built on structured internal knowledge",
]
for o in outcomes:
    bullet(doc, o)

hr(doc)

# ── Assumptions ───────────────────────────────────────────────────────────────
heading(doc, "Assumptions", size=11)
assumptions = [
    "Source PDFs (2005 HDOT Standard Specifications and Special Provisions) are available and accessible in the inputs/ folder at project start.",
    "\"Special Provisions\" refers to project-specific amendments to the standard specs; 2–3 representative examples will be used rather than a complete library.",
    "All work is performed locally; no cloud storage, shared drives, or third-party knowledge platforms are used.",
    "This SOW covers the proof-of-concept phase only; a separate SOW will be prepared for any broader rollout to interns or the full team.",
]
for a in assumptions:
    bullet(doc, a)

doc.save(OUTPUT_PATH)
print(f"Saved: {OUTPUT_PATH}")
