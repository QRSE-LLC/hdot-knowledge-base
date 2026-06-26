# Phase 1 Guide: Vault Setup + Raw Ingest

**Project:** QRSE Knowledge Base — Proof of Concept
**Phase:** Day 1 (2026-05-20)
**Goal:** Vault is running, source documents are organized, and at least 5 spec sections are converted to Markdown and logged.

---

## Before You Start

You need:
- [ ] Obsidian installed — download free at [obsidian.md](https://obsidian.md)
- [ ] The 2005 HDOT Standard Specifications PDF
- [ ] 2–3 Special Provisions samples (any project-specific amendments you have on hand)
- [ ] A PDF viewer that allows text selection and copy (Preview, Adobe, or browser)

Estimated time: 3–5 hours

---

## Step 1 — Open the Project as an Obsidian Vault

1. Open Obsidian
2. On the home screen, click **Open folder as vault**
3. Navigate to and select this folder:
   ```
   My Drive/2026-05_Obsidian_Knowledge_Base_Spec/
   ```
4. Click **Open**

Obsidian will treat this entire project folder as your vault. All existing files (README.md, tasks/, outputs/) will be visible in the left sidebar.

> **Why this folder?** Everything stays in one place — your Markdown files, source docs, and outputs are all visible and searchable inside Obsidian's interface.

---

## Step 2 — Create the Knowledge Base Folder Structure

In Obsidian's left sidebar, right-click and create the following folders. (You can also do this in Finder — Obsidian reflects changes automatically.)

```
2026-05_Obsidian_Knowledge_Base_Spec/
├── raw/
│   ├── division-100/
│   ├── division-102/
│   ├── division-200/
│   ├── division-501/
│   └── division-601/
├── wiki/
│   ├── concepts/
│   ├── divisions/
│   ├── procedures/
│   └── cross-references/
└── indexes/
```

The `inputs/`, `outputs/`, `tasks/`, and `notes/` folders already exist — leave them as-is.

**What each folder is for:**

| Folder | Purpose |
|--------|---------|
| `inputs/` | Source PDFs — read-only, never edit these |
| `raw/` | Markdown exports of source material — one subfolder per division |
| `wiki/` | Compiled knowledge pages — LLM-maintained, structured |
| `indexes/` | Index and reference files — source log, concept map, glossary |
| `outputs/` | Finished documents, test results, guides (like this one) |

---

## Step 3 — Add Source Documents to `inputs/`

Copy your source PDFs into the `inputs/` folder:

```
inputs/
├── 2005-HDOT-Standard-Specifications.pdf
├── special-provision-sample-1.pdf     ← or .docx
├── special-provision-sample-2.pdf
└── special-provision-sample-3.pdf
```

**Naming convention:** lowercase, hyphens, no spaces. Keep names descriptive but short.

> These files are **read-only reference**. You will never edit them. All working content goes into `raw/` or `wiki/`.

---

## Step 4 — Convert Spec Sections to Markdown

This is the core task of Day 1. You are extracting text from the PDF and saving it as `.md` files in `raw/`.

### Priority sections (do these five first)

| Division | Title | Save to |
|----------|-------|---------|
| Division 100 | General Provisions | `raw/division-100/` |
| Division 102 | Bidding Requirements and Conditions | `raw/division-102/` |
| Division 200 | Earthwork | `raw/division-200/` |
| Division 501 | Hot Mix Asphalt (HMA) | `raw/division-501/` |
| Division 601 | Structures (intro sections only) | `raw/division-601/` |

### How to convert (choose one method)

**Option A — Copy and paste (simplest, works for any PDF)**

1. Open the PDF in Preview or your browser
2. Select the text of one section
3. Create a new `.md` file in the correct `raw/` subfolder
4. Paste the text and clean up obvious formatting issues (extra line breaks, page headers, etc.)
5. Add a one-line header at the top:
   ```markdown
   # Division 100 — General Provisions
   > Source: 2005 HDOT Standard Specifications, pp. XX–XX
   ```

**Option B — Python script (faster for long sections)**

Run this from Terminal to extract a page range as text:

```bash
python3 - <<'EOF'
import pdfplumber, pathlib

pdf_path = "inputs/2005-HDOT-Standard-Specifications.pdf"
out_path = "raw/division-100/division-100-raw.md"
pages = range(0, 30)  # adjust page range for each division

with pdfplumber.open(pdf_path) as pdf:
    text = "\n\n".join(pdf.pages[i].extract_text() for i in pages if pdf.pages[i].extract_text())

pathlib.Path(out_path).write_text(f"# Division 100 — General Provisions\n> Source: 2005 HDOT Standard Specifications\n\n{text}")
print(f"Saved {len(text):,} characters to {out_path}")
EOF
```

Check if `pdfplumber` is installed first:
```bash
python3 -c "import pdfplumber; print('ready')"
```
If not: `pip3 install pdfplumber`

**Option C — Obsidian Web Clipper (for web-based content only)**

If any spec sections are available on the HDOT website, use the [Obsidian Web Clipper](https://obsidian.md/clipper) browser extension to clip directly to a `raw/` subfolder.

### File naming inside `raw/`

One file per major section or subsection. Use this pattern:

```
raw/division-100/division-100-raw.md          ← full raw export
raw/division-100/section-101-definitions.md   ← if you split by section
raw/division-200/division-200-earthwork.md
raw/division-501/division-501-hma.md
```

Keep raw files close to the source text. Don't clean or summarize here — that's what the wiki is for.

---

## Step 5 — Create the Source Index

Create this file: `indexes/source-index.md`

Use this template — add one row per file you ingested:

```markdown
# Source Index

| ID | File | Type | Division | Date Added | Status | Notes |
|----|------|------|----------|------------|--------|-------|
| S01 | 2005-HDOT-Standard-Specifications.pdf | PDF | All | 2026-05-20 | Partial | Divs 100, 102, 200, 501, 601 extracted |
| S02 | special-provision-sample-1.pdf | PDF | TBD | 2026-05-20 | Queued | |
| S03 | special-provision-sample-2.pdf | PDF | TBD | 2026-05-20 | Queued | |
```

**Status options:** `Queued` → `In Progress` → `Raw Extracted` → `Wiki Page Created`

Update this file every time you add or process a source. It becomes your single source of truth for what's been ingested.

---

## Step 6 — Create Placeholder Index Files

Create these three empty files now so you have them ready for Day 2:

**`indexes/concept-index.md`**
```markdown
# Concept Index

_Populated on Day 2._

## Construction & Materials
## Contract & Payment
## Earthwork & Grading
## Environmental & Permits
## Inspection & Testing
## Structures
```

**`indexes/glossary.md`**
```markdown
# Glossary

_Populated on Day 2._

| Term | Definition | Source |
|------|------------|--------|
| | | |
```

**`indexes/open-questions.md`**
```markdown
# Open Questions

_Add items here as you encounter gaps, ambiguous language, or missing content._

| # | Question | Division | Priority | Status |
|---|----------|----------|----------|--------|
| | | | | |
```

---

## Step 7 — Create the Wiki Page Template

Create this file: `wiki/TEMPLATE.md`

This is the master template every wiki page must follow. Copy it when creating new pages on Day 2.

```markdown
# [Page Title]

**Type:** [Division / Concept / Procedure / Cross-Reference]
**Division:** [e.g., Division 100]
**Section:** [e.g., 102.03]

---

## Summary

One paragraph: what this is, where it appears in the specs, and why it matters for construction or contract administration.

---

## Key Terms

- **[Term]:** Definition as used in the 2005 HDOT Standard Specifications
- **[Term]:** Definition

---

## Spec References

- Section X.X — [brief description of what this section covers]
- Section X.X — [brief description]

---

## QRSE Notes

How QRSE encounters or applies this in practice: field observations, common contractor issues, inspection focus areas, risks to watch for.

---

## Related Pages

- [[Related Page 1]]
- [[Related Page 2]]
- [[Related Page 3]]

---

## Source

> Based on: `raw/division-XXX/filename.md`
> Original: `inputs/2005-HDOT-Standard-Specifications.pdf`, pp. XX–XX
```

---

## Day 1 Definition of Done

Before you close out, confirm all of these:

- [ ] Obsidian vault is open and all folders are created
- [ ] Source PDFs are in `inputs/`
- [ ] At least 5 raw Markdown files exist in `raw/` (one per priority division)
- [ ] `indexes/source-index.md` is created and populated
- [ ] `indexes/concept-index.md`, `glossary.md`, `open-questions.md` created as placeholders
- [ ] `wiki/TEMPLATE.md` created
- [ ] You can navigate the vault in Obsidian and see all files in the sidebar

If you finish early, start on Division 300 (Bases) or Division 400 (Drainage) as bonus raw extractions.

---

## What Comes Next

Day 2 picks up from here. For every raw file you created today, you'll generate one structured wiki page using the template above. The goal by end of Day 2 is 15+ linked pages with a populated concept index and glossary.

---

*Guide version 1.0 — 2026-05-20*
