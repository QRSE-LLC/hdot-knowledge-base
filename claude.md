# Claude instructions for Obsidian Knowledge Base - Spec

## How to load context

This project inherits global rules and context from the QRSE library.

**At the start of every session, read these in order:**

1. `../_QRSE_Library/my-rules.md` — non-negotiable rules
2. `../_QRSE_Library/README.md` — boot sequence pointing to the rest of the global context
3. `./README.md` — this project's metadata and status
4. `./tasks/todo.md` — active work
5. `./tasks/lessons.md` — project-specific corrections
6. `../_QRSE_Library/lessons-learned.md` — global corrections

Only override a global rule here if there's a specific reason for this project.

## Project-specific scope

- **In scope:** 2005 HDOT Standard Specifications for Road and Bridge Construction; associated Special Provisions; vault setup; Markdown wiki compilation; index and search capability
- **Out of scope:** Any other source documents; client deliverables; intern training; subscription product design; multi-user collaboration features
- **Hard constraints:** 3-day timeline (2026-05-20 through 2026-05-22); solo work (Grant only); all data stays local — no cloud tools, no third-party knowledge platforms; Obsidian + plain Markdown + Git only

## Project-specific rules

(Add anything here that only applies to this project — e.g. "all dollar figures rounded to nearest $1k", "use the client's terminology not ours", "do not contact the client directly".)

## Outputs

- All work-in-progress goes in `outputs/drafts/`.
- Approved final versions go in `outputs/final/`.
- Never write outside this project folder.

## End-of-session

Run the `reflect` skill before closing out so the next session has a handoff file.
