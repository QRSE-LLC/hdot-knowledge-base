# Phase 2 Guide: Wiki Page Build

**Project:** QRSE Knowledge Base — Proof of Concept
**Phase:** Day 2 (2026-05-21)
**Goal:** 15–25 structured, cross-linked wiki pages built from raw source files, with concept index and glossary seeded.

---

## Before You Start

Confirm from Day 1:
- [ ] Obsidian vault is open and all folders are visible
- [ ] `raw/` is populated (119 sections across 7 divisions)
- [ ] `indexes/source-index.md`, `concept-index.md`, `glossary.md`, `open-questions.md` exist
- [ ] `wiki/TEMPLATE.md` exists

Estimated time: 4–6 hours

---

## How Day 2 Works

You are not going to wiki-page all 119 sections today. That would produce shallow output. Instead:

**Target: 15–25 high-quality, well-linked pages.**

Claude reads each raw file and generates a structured wiki page using the template. Your job is to direct which sections to do, review the output, and flag anything that needs correction or has a gap worth noting.

Think of it as two parallel tracks running at the same time:

| Track | What | Where |
|-------|------|-------|
| **Division pages** | One page per spec section — what it covers, key terms, how QRSE uses it | `wiki/divisions/` |
| **Concept pages** | One page per key concept that cuts across sections — deeper, more useful for Q&A | `wiki/concepts/` |

Division pages give breadth. Concept pages give depth. Both are needed.

---

## Step 1 — Understand the Wiki Folder Structure

```
wiki/
├── TEMPLATE.md          ← Master template — copy for every new page
├── divisions/           ← One page per spec section (e.g., Section 104, Section 401)
├── concepts/            ← Key concepts that span sections (e.g., Differing Site Conditions)
├── procedures/          ← Step-by-step processes (e.g., How to evaluate a change order)
└── cross-references/    ← Pages linking multiple related sections together
```

**Naming convention:**

| Folder | Filename format | Example |
|--------|----------------|---------|
| `divisions/` | `NNN-title.md` | `104-scope-of-work.md` |
| `concepts/` | `concept-title.md` | `concept-differing-site-conditions.md` |
| `procedures/` | `proc-title.md` | `proc-change-order-evaluation.md` |
| `cross-references/` | `xref-title.md` | `xref-hma-pavement-all-sections.md` |

---

## Step 2 — Priority Order

Work in this order. Division 100 first — it governs every other section and is the most relevant to QRSE's contract administration work.

### Priority 1 — Division 100: General Provisions (9 section pages)

These sections set the rules for every HDOT contract. Start here.

| Section | Title | File |
|---------|-------|------|
| 101 | Terms, Abbreviations, and Definitions | `raw/division-100/101-terms-abbreviations-and-definitions.md` |
| 104 | Scope of Work | `raw/division-100/104-scope-of-work.md` |
| 105 | Control of Work | `raw/division-100/105-control-of-work.md` |
| 106 | Material Restrictions and Requirements | `raw/division-100/106-material-restrictions-and-requirements.md` |
| 107 | Legal Relations and Responsibility to Public | `raw/division-100/107-legal-relations-and-responsibility-to-public.md` |
| 108 | Prosecution and Progress | `raw/division-100/108-prosecution-and-progress.md` |
| 109 | Measurement and Payment | `raw/division-100/109-measurement-and-payment.md` |

Skip 102 and 103 — they are reserved (1 page each, no content).

### Priority 2 — Key Concepts from Division 100 (6–8 concept pages)

These are the subsections most relevant to QRSE's daily work. Build concept pages for each.

| Concept | Source subsection |
|---------|------------------|
| Differing Site Conditions | 104.08 |
| Contract Change Orders | 104.04 |
| Methods of Price Adjustment | 104.06 |
| Liquidated Damages | 108.08 |
| Force Account | 109.06 |
| Disputes and Claims | 107.15 |
| Shop Drawings and Submittals | 105.02–105.03 |

### Priority 3 — Division 400: Pavements (4–5 section pages)

Pavements are the most common work type on HDOT projects.

| Section | Title | File |
|---------|-------|------|
| 401 | Hot Mix Asphalt Pavement | `raw/division-400/401-hot-mix-asphalt-pavement.md` |
| 411 | Portland Cement Concrete Pavement | `raw/division-400/411-portland-cement-concrete-pavement.md` |
| 404 | Slurry Seal | `raw/division-400/404-slurry-seal.md` |
| 415 | Cold Planing of Existing Pavement | `raw/division-400/415-cold-planing-of-existing-pavement.md` |

### Priority 4 — Division 500: Structures (if time permits)

| Section | Title | File |
|---------|-------|------|
| 503 | Concrete Structures | `raw/division-500/503-concrete-structures.md` |
| 511 | Drilled Shafts | `raw/division-500/511-drilled-shafts.md` |

---

## Step 3 — How to Create a Wiki Page

**For each section:**

1. Tell Claude: *"Build a wiki page for Section [number] — [title]"*
2. Claude reads the raw file and generates the page using the template
3. Review the output — check Summary, Key Terms, QRSE Notes
4. Save the file to the correct folder with the correct filename
5. Update `indexes/concept-index.md` — change `[ ]` to `[x]` for that section

**What a good wiki page looks like:**

| Element | Strong | Weak |
|---------|--------|------|
| Summary | Explains what this means in practice for an HDOT project | Restates the section title |
| Key Terms | Defines terms as the spec actually uses them | Copies dictionary definitions |
| Spec References | Lists the specific subsections that matter | Just lists the parent section |
| QRSE Notes | Mentions real risks, common contractor issues, field observations | Left blank or generic |
| Related Pages | Links to at least 3 other wiki pages by `[[wiki link]]` | 0–1 links, or links to raw files |

**Minimum requirements per page:**
- At least 3 `[[wiki links]]` to other pages
- At least 2 Key Terms defined
- QRSE Notes section is not blank

---

## Step 4 — Build the Glossary as You Go

Every time a defined term appears in a wiki page, add it to `indexes/glossary.md`.

Format:
```markdown
| Term | Definition | Section Reference |
|------|------------|-------------------|
| Differing Site Condition | A subsurface or latent physical condition at the site that differs materially from those indicated in the contract documents | 104.08 |
| Force Account | Method of payment for extra work based on actual cost of labor, equipment, and materials plus overhead and profit allowances | 109.06 |
```

Target: at least 20 terms in the glossary by end of Day 2.

---

## Step 5 — Log Open Questions

Every time you hit something ambiguous, missing, or worth following up on, add it to `indexes/open-questions.md`.

Examples of what belongs there:
- A spec section that references another section not in our `raw/` files
- Language that seems contradictory between two sections
- A QRSE Notes item that needs someone with field experience to verify
- A concept that probably warrants a wiki page but you didn't have time for

---

## Step 6 — Linking Pages

Every wiki page must link to at least 3 other pages using Obsidian's `[[double bracket]]` syntax.

**In Obsidian:** type `[[` and start typing a page name — it will autocomplete from your vault.

Good linking patterns:
- A **Division page** links to its most important **concept pages**
- A **concept page** links to related **division pages** and other **concept pages**
- A **procedure page** links to the **division pages** it draws from

Example link chain:
```
Section 108 — Prosecution and Progress
  → [[concept-liquidated-damages]]
  → [[concept-contract-time]]
  → [[104-scope-of-work]]
  → [[proc-change-order-evaluation]]
```

---

## Day 2 Definition of Done

Before closing out:

- [ ] At least 7 Division 100 section pages created in `wiki/divisions/`
- [ ] At least 6 concept pages created in `wiki/concepts/`
- [ ] Every page has at least 3 `[[wiki links]]`
- [ ] `indexes/concept-index.md` updated with `[x]` for every completed page
- [ ] `indexes/glossary.md` has at least 20 terms
- [ ] `indexes/open-questions.md` has at least 5 entries
- [ ] At least 15 total wiki pages exist

---

## What Comes Next

Day 3 picks up from here with validation. You will run 5 test questions against the wiki and rate how well it answers them without returning to the raw PDFs. The strength of Day 3 depends entirely on how well-linked and detailed the Day 2 wiki pages are — vague summaries and missing links will show up immediately in the Q&A test.

---

*Guide version 1.0 — 2026-05-20*
