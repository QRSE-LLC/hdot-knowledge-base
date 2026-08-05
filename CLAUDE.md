# Claude instructions for this repo

This repo is a Markdown knowledge base of official Hawai'i Department of Transportation (HDOT) Highways Division reference material, maintained by QRSE LLC. See `README.md` for what's in it.

## Working conventions

- `raw/` holds source-derived Markdown, organized by division/section. Treat as read-only source material — don't edit it to "improve" it; if the source text is wrong, note that in the relevant wiki page instead.
- `wiki/divisions/` and `wiki/concepts/` are the compiled reference pages. Each page should include: a summary, key terms, references back to the exact spec section(s), links to related pages, and a practice-notes section for anything a QRSE contract administrator would need to know that isn't obvious from the spec text alone.
- `indexes/` must stay in sync with `wiki/` — when a page is added, update `indexes/source-index.md` and `indexes/concept-index.md` accordingly.
- Log anything ambiguous, contradictory, or unverifiable in `indexes/open-questions.md` with a priority (High/Medium/Low) rather than guessing.

## Accuracy

This content informs real contract-administration decisions. Don't state something as fact if the source document is unclear, outdated, or conflicting — flag it instead. Always prefer the official Special Provisions for a given project over the general Standard Specifications where the two might differ.

## The materials and testing area

`raw/materials-testing/` holds official HDOT materials guides that are not part of the Standard Specifications. They answer the questions the spec book leaves open — the specs say a material must comply, these say how it gets proven.

- `sampling-testing-guide/` — acceptance and verification sampling frequencies, split by LABS discipline (`01` bituminous, `02` geotechnical, `03` structural, `04` other). **`00-general-notes.md` holds Notes 1, 2, 3, 4S, 5S, and 6G, which qualify every table. Read the notes an item references before quoting a frequency.**
- `master-material-list/` — the Master Material Certification List by spec division, mapping pay item to required certification (COC / LAB / APL / DA) and reviewing office (LB / LG / LS / LR).
- `qualifications/` — sampler certification (FSTQP), annual IA evaluations, JC forms, and which labs may perform acceptance testing.

Same rule as the rest of `raw/` — treat it as read-only source material.

## Answering questions from this repo

Beyond authoring, this repo is used to answer questions from QRSE field and CM staff, including from Slack. Answer at the level of a senior inspector: give the usable answer, then show where it comes from.

### Document hierarchy

This extends the accuracy rule above. HDOT contract documents override each other in a fixed order, and getting it wrong is the fastest way to be confidently wrong:

| Priority | Document | Where |
|---|---|---|
| 1 (highest) | Project **Special Provisions** and project plans | not in this repo — see below |
| 2 | **Standard Specifications** (2005) | `raw/division-*/` |
| 3 | Standard Plans | not yet loaded |
| 4 | **Sampling and Testing Guide**, **Master Material Certification List** | `raw/materials-testing/` |
| 5 (lowest) | 1973 Construction Manual | not yet loaded; dated, superseded where it conflicts |

The Master Material List states this itself: standard plans, standard specifications, special provisions, and project plans all take precedence over it.

**Special Provisions are not currently in this repo.** For a project-specific question, give the general requirement, cite it, and say plainly that the contract's Special Provisions govern and are not loaded here. Never infer one contract's provisions from another's.

### Citation discipline

- Cite the file and the section or item number for every substantive claim. No pointer, no answer.
- Never invent a spec section, pay item number, frequency, or rate. If it is not in the loaded documents, say so.
- Quote numbers exactly as written. "1 per approximately every 1,500 cu. yd." keeps its "approximately."
- In `raw/materials-testing/sampling-testing-guide/`, a lone `2` or `3` on its own line is a displaced cubic or square exponent from PDF extraction, not a stray data point. See the extraction note in `00-general-notes.md`, and state units in words (cubic yards, square feet) rather than repeating a bare digit.

### When to defer to the Project Engineer

Saying "confirm with the PE" is a correct answer, not a failure. Do it when:

- The question is about **field compaction frequency**. Note 6G makes those values a preliminary guide that the PE must finalize and document. This is the most commonly misquoted item in the Guide.
- The requirement is set by the contract — application rates, mix designs, tolerances, payment.
- The item is non-standard. Note 1 directs those to LABS.
- The documents conflict, or only a partial answer exists. Log it in `indexes/open-questions.md`.

### Terminology

The branch is now **LABS**. Older source documents say "MTRB" or "Materials Testing and Research Branch" — quote source text verbatim, but use LABS in your own wording.
