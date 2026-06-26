# Obsidian Knowledge Base - Spec — Lessons learned

> Record any corrections from Grant during this project. At project close, review and merge anything broadly applicable into `../../_QRSE_Library/lessons-learned.md`.

## Lessons

_Format: short title — what happened — the rule to follow next time._

- **Concept pages first** — Division summary pages (like `104-scope-of-work.md`) provided breadth, but the concept pages (like `concept-differing-site-conditions.md`) were what actually answered the Q&A test questions. On the next build, prioritize concept pages over division pages when the goal is Q&A usability. Build at least one concept page for every 2 division pages.

- **QRSE Notes are the highest-value section** — every full answer in the Q&A test came from a QRSE Notes bullet, not the spec references or key terms tables. The spec references give locatability; the QRSE Notes give actionability. Write QRSE Notes as if briefing a new staff member on what to watch for — not as spec summaries.

- **Output filenames must match the todo.md exactly** — the Day 3 todo called for `outputs/drafts/search-test-results.md`. I produced `phase-3-guide.md` instead, which contained the Q&A content but under a different name. This broke the plan-vs-actual match and required cleanup. When a deliverable has a specific planned filename, use that name.

- **Cross-page gaps need inline bridges, not just related-pages links** — the Q5 gap (Inspector stop-work authority) came from a fact on `401-hot-mix-asphalt-pavement.md` requiring a separate fact from `105-control-of-work.md` with no sentence connecting them. Adding inline bridging text ("Inspector must notify the RE — see [[105-control-of-work]] §105.12") at the point of use would have prevented this without needing a gap patch.

- **The reflect skill runs at session end, not project end** — CLAUDE.md says to run `reflect` before closing out. On Day 2 this was deferred to Day 3 because "the project wasn't done yet." That's wrong — reflect captures the state at the end of each session so the next session has a handoff. It should have been run at the end of Day 2.
