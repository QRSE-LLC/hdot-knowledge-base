# Phase 3 Guide — Day 3 Validation and Close-Out

**Written:** 2026-05-21  
**Phase:** Day 3 of 3  
**Status:** Q&A validation complete; gap patched; POC ready to close

---

## What Day 3 Accomplished

1. **Q&A validation test** — ran 5 realistic HDOT contract administration questions against the wiki only (no returning to raw PDFs)
2. **Gap identified and patched** — one partial answer found; `105-control-of-work.md` updated
3. **Phase 3 guide written** — this file
4. **Final POC summary written** — `outputs/drafts/poc-summary.md`
5. **Reflect skill run** — session handoff written

---

## Validation Test Results

### Scoring Key

| Rating | Meaning |
|--------|---------|
| ✅ Full | Wiki contained the specific answer with correct spec reference |
| ⚠️ Partial | Wiki pointed in the right direction but required cross-page inference |
| ❌ Gap | Wiki could not answer; must return to raw PDFs |

### Results

| Q | Question (abbreviated) | Rating |
|---|------------------------|--------|
| 1 | Basalt DSC — 12-hour notice + entitlement | ✅ Full |
| 2 | Field order, no price, scope dispute — obligations + deadlines | ✅ Full |
| 3 | LD calculation and waiver conditions | ✅ Full |
| 4 | Force account documentation + markup structure | ✅ Full |
| 5 | HMA paving weather restrictions + Inspector authority | ⚠️ Partial → **patched** |

**Final score: 5/5 after gap patch (4/5 before)**

---

## The One Gap Found

**Q5 — Inspector stop-work authority chain**

The wiki correctly stated:
- §401.03(A): no HMA placement on wet surfaces; no placement <50°F and falling; may apply at 40°F and rising
- §105.01: Inspector is "for inspection only — cannot alter contract or waive provisions"

What was missing: the explicit workflow — Inspector observes violation → notifies RE → RE issues stop-work under §105.12. A reader who only read `401-hot-mix-asphalt-pavement.md` would know the spec was violated but wouldn't know exactly who has authority to stop the work and how.

**Fix applied:** Added a QRSE Notes bullet to `105-control-of-work.md` (line 54) spelling out the three-step chain with spec references.

---

## What the Validation Test Proved About the Wiki

### Strengths

1. **The QRSE Notes sections are doing the most work.** Nearly every full answer came from a QRSE Notes bullet, not just the spec reference table. The decision to add practice-oriented commentary was the right call.
2. **Cross-linking works.** Every full answer required navigating 2–3 pages. The `[[wiki links]]` between pages made those connections visible and followable.
3. **The concept pages outperform the division pages for Q&A.** Concept pages like `concept-differing-site-conditions` and `concept-force-account` are written to answer "what do I do when X happens" — that framing maps directly to how the questions were posed.
4. **The Division 100 coverage is solid.** 7 of 18 pages cover Division 100 procedures, which are the most commonly applicable provisions. These carried 4 of the 5 questions.

### Weaknesses

1. **Cross-page inference gaps.** The Q5 gap was caused by relevant facts being on two different pages with no sentence bridging them. More "See also" notes connecting specific provisions would reduce this.
2. **Division 400+ coverage is thin.** The wiki has only 4 pavement pages (401, 404, 411, 415). Q5 worked because it was fundamentally a control-of-work question. A question purely about HMA mix design, compaction tolerances, or density testing would likely produce a ❌ gap.
3. **No procedural how-to pages.** The wiki has no entries in `wiki/procedures/`. Questions that require a step-by-step workflow (e.g., "how do I process a force account claim from start to finish") require reading multiple pages and assembling the procedure yourself. A procedures layer would fix this.
4. **Open questions remain open.** The 10 items in `indexes/open-questions.md` were not resolved during the POC. Three are flagged High priority and relate to escalation thresholds for Disputed Work and the Contractor certification penalty framework.

---

## Lessons Learned for a Full Build

1. **Start with concept pages.** They produce more Q&A value per hour of work than division summary pages. The division pages are useful for "what does this section cover?" questions; concept pages answer "what do I do?" questions.

2. **Write the QRSE Notes section first.** The spec references and key terms can be filled in later; the QRSE Notes are where institutional knowledge lives. On this POC, those notes were written last and they're the best part.

3. **Add a procedures layer.** `wiki/procedures/` is empty. A full build should include procedure pages like:
   - `procedure-processing-a-claim.md`
   - `procedure-force-account-daily-documentation.md`
   - `procedure-time-extension-request.md`
   These are just narrativizations of what the spec requires, but having them in a single page is very high-value for field staff.

4. **Cross-reference gaps at the point of use.** When a wiki page mentions a workflow that crosses into another section, add the cross-reference inline (e.g., "Inspector must notify the RE — see [[105-control-of-work]] §105.12") rather than only at the bottom of the page.

5. **The 119 raw Markdown files are the foundation.** All wiki content was synthesized from those files. The raw Markdown quality was good — OCR artifacts were minimal and the structure was preserved. A full build should keep those files current with any Special Provisions issued for each project.

---

## What Was Not Done (Deferred or Out of Scope)

- `wiki/procedures/` — never populated (Priority 5 in Phase 2; out of scope for POC)
- `wiki/cross-references/` — never populated (same)
- Division 500 pages (503, 511) — skipped Day 2; still not done
- Open questions in `indexes/open-questions.md` — 10 items unresolved
- Special Provisions indexing — the inputs include Special Provisions files that were not processed

---

## Day 3 File Changes

| File | Change |
|------|--------|
| `wiki/divisions/105-control-of-work.md` | Added Inspector stop-work authority chain to QRSE Notes |
| `outputs/drafts/phase-3-guide.md` | Created (this file) |
| `outputs/drafts/poc-summary.md` | Created (final summary) |
| `outputs/drafts/day3-reflect.md` | Created (reflect skill output) |
