# Claude instructions for this repo

This repo is a Markdown knowledge base of official Hawai'i Department of Transportation (HDOT) Highways Division reference material, maintained by QRSE LLC. See `README.md` for what's in it.

## Working conventions

- `raw/` holds source-derived Markdown, organized by division/section. Treat as read-only source material — don't edit it to "improve" it; if the source text is wrong, note that in the relevant wiki page instead.
- `wiki/divisions/` and `wiki/concepts/` are the compiled reference pages. Each page should include: a summary, key terms, references back to the exact spec section(s), links to related pages, and a practice-notes section for anything a QRSE contract administrator would need to know that isn't obvious from the spec text alone.
- `indexes/` must stay in sync with `wiki/` — when a page is added, update `indexes/source-index.md` and `indexes/concept-index.md` accordingly.
- Log anything ambiguous, contradictory, or unverifiable in `indexes/open-questions.md` with a priority (High/Medium/Low) rather than guessing.

## Accuracy

This content informs real contract-administration decisions. Don't state something as fact if the source document is unclear, outdated, or conflicting — flag it instead. Always prefer the official Special Provisions for a given project over the general Standard Specifications where the two might differ.
