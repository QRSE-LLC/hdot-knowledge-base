# Obsidian Knowledge Base - Spec

> Copy this template into a new dated folder (e.g. `2026-05_HCDA_Wahiawa_Proposal`) when starting a project. Fill in the placeholders below.

## Project metadata

| Field | Value |
|-------|-------|
| **Project name** | Obsidian Knowledge Base - Spec |
| **Client** | QRSE (internal) |
| **Project type** | Internal (proposal / internal / report / pricing / other) |
| **Deadline** | 2026-05-31 |
| **Project lead** | Grant |
| **Status** | Planning |
| **Created** | 2026-05-20 |

## What this project is

A solo 3-day test run of the LLM-assisted knowledge base workflow, using the 2005 HDOT Standard Specifications for Road and Bridge Construction and associated Special Provisions as the source dataset. The goal is to prove the system: ingest raw documents, compile a structured Markdown wiki in Obsidian, and have a working search/Q&A capability against the specs by end of Day 3. This is an internal R&D proof of concept — not a client deliverable. If it works, this becomes the template for the broader intern/team knowledge base effort.

## Deliverables

- [ ] Obsidian vault with defined folder structure
- [ ] Raw documents ingested into `raw/` (PDF → Markdown for key sections)
- [ ] 15–25 structured wiki pages covering key spec concepts and divisions
- [ ] Master index and concept index files
- [ ] Working search / Q&A demonstrated against the wiki
- [ ] Short "lessons learned" note for scaling to interns

## Team

- **Lead:** Grant
- **Contributors:** (solo)

## Key dates

- Kickoff: 2026-05-20
- Internal review: 2026-05-22
- Final delivery: 2026-05-22

## Folder map

```
Obsidian Knowledge Base - Spec/
├── README.md           ← This file (project metadata, status)
├── claude.md           ← Project-specific Claude instructions (inherits from library)
├── inputs/             ← Source material — RFPs, source docs, attachments. Read-only.
├── outputs/
│   ├── drafts/         ← Work in progress
│   └── final/          ← Approved, delivered versions
├── tasks/
│   ├── todo.md         ← Active checklist
│   └── lessons.md      ← Project-specific lessons (merge into library at end)
└── notes/              ← Scratch, meeting notes, voice memos
```

## Boot sequence for Claude

When starting a session in this project, Claude should:

1. Read `claude.md` in this folder.
2. Read `../_QRSE_Library/README.md` and follow its boot sequence for global context.
3. Check `tasks/todo.md` for status.
4. Skim `tasks/lessons.md` and `../_QRSE_Library/lessons-learned.md` for relevant prior corrections.
