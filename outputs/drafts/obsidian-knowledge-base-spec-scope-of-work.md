# Scope of Work: Obsidian Knowledge Base — Proof of Concept

**Prepared by:** QRSE
**Date:** 2026-05-20
**Version:** 1.0

---

## Project Overview

This is a solo internal R&D effort to validate whether an LLM-assisted knowledge base workflow can be applied to QRSE's existing technical documentation. The 2005 HDOT Standard Specifications for Road and Bridge Construction and associated Special Provisions serve as the test dataset. Over three days, Grant will ingest source documents, compile a structured Markdown wiki in Obsidian, and demonstrate functional search and Q&A capability against the compiled content — without returning to the source PDFs.

---

## Objectives

- Establish a local-first, cloud-independent knowledge base infrastructure using Obsidian and plain Markdown files
- Ingest priority sections of the 2005 HDOT Standard Specifications (Divisions 100–600) into a structured raw document store
- Compile a linked wiki of 15–25 structured pages covering key spec concepts, divisions, and procedures
- Demonstrate functional search and Q&A capability against the compiled wiki
- Produce a lessons-learned record to inform scaling of this workflow to the QRSE intern program and internal training

---

## Tasks & Responsibilities

**Phase 1 — Setup & Configuration**

- Configure the Obsidian vault using the project folder as the root, establishing the `raw/`, `wiki/`, `indexes/`, and `outputs/` directory structure
- Define and document the standard wiki page template to ensure consistent formatting across all compiled pages

**Phase 2 — Data Ingest**

- Collect the 2005 HDOT Standard Specifications PDF and representative Special Provisions samples and place them in the read-only `inputs/` directory
- Convert priority spec sections (Divisions 100, 102, 200, 501, 601) from PDF to Markdown and store in `raw/` using subdivision naming conventions
- Log every ingested source in `indexes/source-index.md` with document type, topic area, date, and ingestion status

**Phase 3 — Wiki Compilation**

- Generate one structured wiki page per ingested section using the standard template (Summary, Key Terms, Spec References, QRSE Notes, Related Pages, Source)
- Establish bidirectional cross-reference links between related wiki pages, with a minimum of three links per page
- Build `indexes/concept-index.md` as a categorized, linked inventory of all concepts covered in the wiki
- Build `indexes/glossary.md` with definitions for all technical terms and abbreviations appearing in the wiki
- Document content gaps, ambiguous language, and items requiring further research in `indexes/open-questions.md`

**Phase 4 — Validation**

- Run five pre-defined test questions against the wiki and rate each answer on a 1–5 completeness scale (5 = fully answered from wiki alone, no PDF required)
- Produce `outputs/drafts/search-test-results.md` documenting each question, the wiki's answer, source sections referenced, and the rating
- Write `tasks/lessons.md` capturing what worked, what failed, and recommendations for scaling the system to broader use

---

## Deliverables

- Configured Obsidian vault with defined folder structure (`raw/`, `wiki/`, `indexes/`, `outputs/`)
- Source index (`indexes/source-index.md`) logging all ingested documents with status
- 15–25 structured, cross-linked wiki pages covering key spec divisions, concepts, and procedures
- Concept index (`indexes/concept-index.md`) and glossary (`indexes/glossary.md`)
- Search and Q&A test log (`outputs/drafts/search-test-results.md`) with five rated test questions
- Lessons learned document (`tasks/lessons.md`) with recommendations for scaling to the intern program

---

## Timeline

- **Start Date:** 2026-05-20
- **Day 1 — Setup + Raw Ingest:** 1 day (2026-05-20)
- **Day 2 — Wiki Build:** 1 day (2026-05-21)
- **Day 3 — Test + Validate:** 1 day (2026-05-22)
- **Estimated Completion:** 2026-05-22

---

## Supervision & Support

This is a solo internal R&D effort led by Grant with no external oversight requirements. Claude Code serves as the primary LLM tool for all wiki compilation, indexing, and content generation tasks. Progress is self-tracked via `tasks/todo.md`, with a lessons-learned review completed at the close of Day 3.

---

## Expected Outcomes

- A validated, repeatable workflow for converting raw technical documents into a searchable Markdown knowledge base
- Demonstrated proof that LLM-compiled wikis can reduce time-to-answer for spec-related questions without returning to source PDFs
- A tested vault structure and wiki page template ready to hand to summer interns for broader rollout
- An identified roadmap for extending the system to other QRSE document types (AASHTO, FHWA guidance, HDOT Design Criteria)
- A foundation for future subscription product development — including change order evaluation and NEPA support — built on structured internal knowledge

---

**Assumptions:**
- Source PDFs (2005 HDOT Standard Specifications and Special Provisions) are available and accessible in the `inputs/` folder at project start.
- "Special Provisions" refers to project-specific amendments to the standard specs; 2–3 representative examples will be used rather than a complete library.
- All work is performed locally; no cloud storage, shared drives, or third-party knowledge platforms are used.
- This SOW covers the proof-of-concept phase only; a separate SOW will be prepared for any broader rollout to interns or the full team.
