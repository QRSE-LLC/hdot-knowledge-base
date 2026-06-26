# Obsidian Knowledge Base - Spec — Todo

## Plan

Test-run the LLM-assisted knowledge base workflow using the 2005 HDOT Standard Specifications and Special Provisions. Three days, solo. Prove the system works end-to-end: ingest → wiki → search.

**Stack:** Obsidian (UI) + local Markdown files + Git (version control)
**Source material:** 2005 HDOT Standard Specifications for Road and Bridge Construction + Special Provisions

---

## Day 1 — Setup + Ingest (2026-05-20)

- [ ] Set up Obsidian vault folder structure (raw/, wiki/, outputs/, indexes/)
- [ ] Add source documents to `inputs/` (PDFs, any existing Markdown exports)
- [ ] Convert / clip key sections of Standard Specs to Markdown → `raw/`
- [ ] Create `indexes/source-index.md` — log every source with type, topic, status
- [ ] Pick 3–5 priority divisions to start (e.g., Division 100 General, Division 200 Earthwork, Division 500 Surfacing)

## Day 2 — Build the Wiki (2026-05-21)

- [ ] Create wiki pages for each priority division (1 page per major section)
- [ ] Each page must include: Summary, Key Terms, Referenced Sections, Related Pages
- [ ] Create `indexes/concept-index.md` — linked list of all concepts and terms
- [ ] Create `indexes/glossary.md` — definitions for spec terms, abbreviations
- [ ] Link pages bidirectionally (at least 3 cross-links per page)
- [ ] Create `indexes/open-questions.md` — gaps, ambiguous language, items needing lookup

## Day 3 — Test + Validate (2026-05-22)

- [ ] Run 5 test questions against the wiki (e.g., "What does the spec say about compaction testing?")
- [ ] Evaluate: can I get a useful answer without reading the raw PDF?
- [ ] Identify any structural gaps
- [ ] Produce `outputs/drafts/search-test-results.md` — Q&A log with ratings
- [ ] Write `tasks/lessons.md` — what worked, what didn't, what to change before scaling

## Completed

- [x] Project folder scaffolded (2026-05-20)
- [x] Scope of work written (2026-05-20)
- [x] README, CLAUDE.md, todo filled in (2026-05-20)

## Review

_After Day 3, summarize: did the search/Q&A work? What would you change before handing to interns?_
