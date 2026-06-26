# Scope of Work: QRSE Knowledge Base — Proof of Concept

**Project:** Obsidian Knowledge Base — Spec (Test Run)
**Date:** 2026-05-20
**Author:** Grant
**Status:** Draft
**Timeline:** 3 days (2026-05-20 through 2026-05-22)

---

## 1. Purpose

This is a solo proof-of-concept to test whether the LLM-assisted knowledge base workflow described in recent R&D research can be applied to QRSE's existing technical documentation — specifically, the 2005 HDOT Standard Specifications for Road and Bridge Construction and associated Special Provisions.

The test run is deliberately narrow. The goal is not to build the final system. The goal is to answer one question:

> **Can a structured Markdown wiki, built from raw spec documents using an LLM, support fast and accurate search and Q&A by the end of three days?**

If yes, the same workflow becomes the template for broader rollout (intern program, subscription products, internal training).

---

## 2. Source Material

| Source | Type | Scope |
|--------|------|-------|
| 2005 HDOT Standard Specifications for Road and Bridge Construction | PDF | Full document; prioritize Divisions 100–600 |
| Special Provisions (project-specific) | PDF / Word | Representative samples; 2–3 examples |

All source material goes into `inputs/` (read-only). Processed Markdown exports go into `raw/`.

---

## 3. System Design

### Stack

| Component | Tool | Rationale |
|-----------|------|-----------|
| UI / viewer | Obsidian | Local-first, Markdown-native, graph view, plugin ecosystem |
| Storage | Local folder (this project) | Total data control, no cloud dependency |
| Version control | Git | Rollback, audit trail, safe experimentation |
| LLM | Claude Code (this session) | Reads/writes all wiki content |

### Folder Structure (Obsidian Vault)

```
2026-05_Obsidian_Knowledge_Base_Spec/
├── inputs/                  ← Source PDFs and documents (read-only)
├── raw/                     ← Markdown exports of source material
│   ├── division-100/
│   ├── division-200/
│   └── ...
├── wiki/                    ← Compiled knowledge (LLM-maintained)
│   ├── concepts/            ← Definitions, terms, technical concepts
│   ├── divisions/           ← One page per spec division
│   ├── procedures/          ← How-to summaries (testing, inspection, etc.)
│   └── cross-references/    ← Connections across divisions
├── indexes/
│   ├── source-index.md      ← Every ingested source logged
│   ├── concept-index.md     ← All wiki concepts, linked
│   ├── glossary.md          ← Terms and abbreviations
│   └── open-questions.md    ← Gaps, ambiguities, items needing lookup
├── outputs/
│   ├── drafts/              ← Work in progress (including this file)
│   └── final/
└── tasks/
    ├── todo.md
    └── lessons.md
```

### Wiki Page Template

Every page in `wiki/` must follow this format:

```markdown
# [Title]

## Summary
One paragraph: what this is, where it appears in the specs, why it matters.

## Key Terms
- **[Term]:** Definition as used in the 2005 Standard Specs

## Spec References
- Section X.X.X — [brief description]
- Section X.X.X — [brief description]

## QRSE Notes
How QRSE encounters or applies this in practice (field notes, common issues, inspection tips).

## Related Pages
- [[Linked Page 1]]
- [[Linked Page 2]]

## Source
Based on: `raw/division-XXX/section-XXXX.md`
```

---

## 4. Scope of Work by Day

### Day 1 — Setup + Raw Ingest (2026-05-20)

**Goal:** Vault is running, source material is captured, first five sections are Markdown.

Tasks:
- Open this project folder as an Obsidian vault
- Add source PDFs to `inputs/`
- Use PDF-to-Markdown conversion (or Obsidian Web Clipper for web sources) to export key sections into `raw/`
- Priority sections to ingest first:
  - Division 100 — General Provisions
  - Division 102 — Bidding Requirements and Conditions
  - Division 200 — Earthwork
  - Division 501 — Hot Mix Asphalt (HMA)
  - Division 601 — Structures (intro sections)
- Log all sources in `indexes/source-index.md`

**Definition of done:** At least 5 sections are in `raw/` and logged in the source index.

---

### Day 2 — Wiki Build (2026-05-21)

**Goal:** 15–25 structured wiki pages exist, are linked, and the concept index is populated.

Tasks:
- For each ingested section, create one wiki page following the template above
- Create cross-reference links between related pages
- Build `indexes/concept-index.md` — all concepts organized by category
- Build `indexes/glossary.md` — definitions for all terms appearing in the wiki
- Log any unclear, ambiguous, or missing content in `indexes/open-questions.md`

Target pages (examples):
- `wiki/divisions/division-100-general-provisions.md`
- `wiki/concepts/differing-site-conditions.md`
- `wiki/concepts/liquidated-damages.md`
- `wiki/procedures/payment-for-extra-work.md`
- `wiki/concepts/material-certification.md`
- `wiki/procedures/compaction-testing.md`

**Definition of done:** 15+ linked wiki pages, concept index complete, glossary seeded.

---

### Day 3 — Test + Validate (2026-05-22)

**Goal:** Confirm the system can answer real questions without reading the raw PDF.

Test questions (run all five, log results):
1. What is the standard specification for compaction of subgrade material?
2. What are the contractor's obligations when a differing site condition is encountered?
3. How is payment calculated for extra work under the standard specs?
4. What defines substantial completion, and what are the consequences of not meeting it?
5. What special provisions typically modify Division 500 (Surfacing) for HDOT projects?

For each question, record:
- What the wiki says
- Was the answer complete, partial, or missing?
- What source sections were referenced?
- Rating: 1–5 (1 = had to go back to the PDF; 5 = answered fully from wiki alone)

Outputs:
- `outputs/drafts/search-test-results.md` — Q&A log with ratings
- `tasks/lessons.md` — What worked, what failed, what to change

**Definition of done:** All 5 questions answered and rated; lessons written.

---

## 5. Success Criteria

| Criterion | Minimum | Target |
|-----------|---------|--------|
| Wiki pages created | 10 | 20+ |
| Sections ingested to `raw/` | 5 | 10+ |
| Test questions answered from wiki alone | 3/5 | 5/5 |
| Average Q&A rating | 3.0 | 4.0+ |
| Lessons documented for scaling | Yes | Yes |

---

## 6. What This Is Not

- Not a client deliverable
- Not a production system
- Not a complete documentation of all 2005 Standard Specs
- Not designed for multiple users or shared access (yet)

---

## 7. Next Steps (if proof of concept succeeds)

1. Expand to all divisions of the 2005 Standard Specs
2. Add Special Provisions library (organized by project type)
3. Add QRSE field notes and inspection checklists as a second source layer
4. Extend to other documents (AASHTO, FHWA guidance, HDOT Design Criteria)
5. Define intern roles and replicate this workflow with the team
6. Evaluate subscription product potential (e.g., change order evaluation, NEPA support)

---

*End of Scope of Work*
