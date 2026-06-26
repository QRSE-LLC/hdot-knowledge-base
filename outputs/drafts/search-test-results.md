# Q&A Validation Test Results

**Project:** QRSE Obsidian Knowledge Base — Proof of Concept  
**Date:** 2026-05-21  
**Tester:** Grant (solo)  
**Method:** Questions posed against wiki only — no returning to raw PDFs or source documents

---

## Scoring Key

| Rating | Meaning |
|--------|---------|
| ✅ Full | Wiki contained the specific answer with the correct spec reference |
| ⚠️ Partial | Wiki pointed in the right direction but required cross-page inference or was missing a specific procedural step |
| ❌ Gap | Wiki could not answer — must return to raw PDFs |

---

## Question 1

**"A contractor discovers hard basalt rock 4 feet below the surface where the boring log showed soil. What must they do in the next 12 hours, and what are they entitled to claim?"**

**Target pages:** `concept-differing-site-conditions`, `104-scope-of-work`, `concept-disputes-and-claims`

**Answer from wiki:**

This is a **Type I Differing Site Condition** — the wiki explicitly defines Type I as "boring log showed soil; actual conditions are decomposed lava rock" (near-identical to the question scenario).

Required actions within 12 hours:
- Give **verbal notice to the Resident Engineer** by 10:00 AM of the next working day (per §104.08 — the 12-hour clock or next-day 10 AM, whichever is later)
- Engineer is notified and investigates site conditions

Required within 5 days:
- Submit **written notice of potential claim** to Engineer

Entitlement:
- If conditions are found to materially differ: **equitable adjustment in contract price and/or time** via change order
- Adjustment is priced per §104.06 (force account or negotiated fixed price most common)
- No claim allowed after final payment (§104.08(C))
- No claim if Contractor had pre-bid knowledge of the condition

Additional: The Contractor must maintain **contemporaneous records** from notice date (§107.15(B)).

**Rating: ✅ Full answer**

**Pages that answered it:** `concept-differing-site-conditions` (primary), `104-scope-of-work` (notice clock), `concept-disputes-and-claims` (records requirement)

---

## Question 2

**"The Engineer issues a field order directing extra work but doesn't include a price. The contractor disagrees with the scope. What are their obligations and deadlines?"**

**Target pages:** `104-scope-of-work`, `concept-contract-change-orders`, `concept-disputes-and-claims`

**Answer from wiki:**

Contractor obligations:
1. **Continue working** — §107.15(C) and §107.15(H) require the Contractor to proceed despite disputes; stopping = grounds for termination for default
2. **Protest the Field Order within 3 days of receipt** — §104.03 explicitly; missing this deadline waives claim rights
3. **Submit a change proposal within 15 days** — §104.05

If no price agreed:
- Engineer can unilaterally impose **force account** (Method 5, §104.06) — no Contractor consent required
- Contractor must work efficiently or Engineer can stop work and change methods

**No payment until CCO is issued** (§104.04) — even if force account is imposed, the CCO must be executed before payment flows.

Formal claim escalation if unresolved:
- Submit formal claim within **180 days** of potential claim notice

**Rating: ✅ Full answer**

**Pages that answered it:** `concept-contract-change-orders` (3-day protest, no pay without CCO), `104-scope-of-work` (15-day proposal deadline), `concept-disputes-and-claims` (continue-work obligation)

---

## Question 3

**"A contractor is 15 days past the contract completion date. The State wants to assess liquidated damages. Walk through how LDs are calculated and when they can be waived."**

**Target pages:** `concept-liquidated-damages`, `108-prosecution-and-progress`, `101-terms-abbreviations-and-definitions`

**Answer from wiki:**

Calculation:
- LDs = days late × daily rate set in contract Special Provisions
- For 15 days: **15 × (project-specific rate)** = total LDs assessed
- LDs are deducted from monies due; no lawsuit required to collect
- Note: the exact dollar rate is project-specific and requires the Special Provisions — the wiki correctly flags this

Secondary LD: **Punchlist LD = 20% of primary LD rate** for failure to complete punchlist after substantial completion

Waiver windows (§108.08) — LDs are suspended during:
1. Date of substantial completion → date punchlist is delivered (State can't charge for its own delay in issuing list)
2. Date punchlist complete → date of final inspection
3. Date of final inspection → date of final acceptance

Full elimination via time extension (§108.05):
- Contractor can eliminate LD exposure by obtaining approved time extensions for State-caused changes, force majeure, permit delays, material delivery delays, suspension of work
- Extensions only granted for **critical path** delays — float is not compensable
- Contractor must request time extension in writing within **5 working days** of delay event or loses the right

**Rating: ✅ Full answer**

**Pages that answered it:** `concept-liquidated-damages` (primary), `108-prosecution-and-progress` (time extension deadlines and critical path)

---

## Question 4

**"The Contractor wants to use force account to bill for extra work. What documentation must be submitted, what costs are allowed, and what is the markup structure?"**

**Target pages:** `concept-force-account`, `concept-methods-of-price-adjustment`, `109-measurement-and-payment`

**Answer from wiki:**

Documentation:
- **State Force Account Form** completed by Contractor each day
- **Inspector signs the form that same day** — non-negotiable; unsigned forms = unverifiable costs = no payment
- Submit original + 2 copies with invoices and backup to Engineer
- For idle equipment: written notification at start of standby period; weekly list every Monday of idle equipment with dates, times, and reasons

Allowable cost components and markups:
| Category | Markup |
|----------|--------|
| Labor (wages + fringe) | +15% O&P |
| Materials (invoice cost) | +15% O&P |
| Equipment (Blue Book or actual shop rate, lower of two) | No markup |
| Subcontractors | +7% |
| Insurance/taxes | +6% |
| State excise tax | At actual rate |
| Bond premium | At actual rate, max 1% |

Not allowable: small tools (≤$500), overtime without prior written Engineer approval, breakdown idle time, pricing/negotiation costs, financing costs

Markup tier structure (§109.05):
- Max 3 markup tiers total
- GC → Sub 1 → Sub 2 example: Sub 2 charges $10K + 15% = $11,500; Sub 1 passes through + 7% = $12,305; GC passes through + 7% = $13,166

Equipment idle/standby = 50% of computed Blue Book rate when idle due to State-caused delays

**Rating: ✅ Full answer**

**Pages that answered it:** `concept-force-account` (documentation + allowable costs), `concept-methods-of-price-adjustment` (tier markup example)

---

## Question 5

**"A Contractor submits HMA paving on a wet surface at 48°F air temperature. The Inspector wants to stop the work. What spec provisions apply and what are the Inspector's authorities?"**

**Target pages:** `401-hot-mix-asphalt-pavement`, `105-control-of-work`, `106-material-restrictions-and-requirements`

**Answer from wiki:**

Applicable spec provisions:
- **§401.03(A) — Wet surface:** No HMA placement on wet surfaces. Absolute prohibition — no temperature qualifier. **This is a clear violation regardless of temperature.**
- **§401.03(A) — Temperature:** No placement when temp is **<50°F and falling**. At 40°F and rising, placement is allowed. At 48°F the answer depends on direction: 48°F falling = violation; 48°F rising = allowed by spec.
- At the stated facts (48°F AND wet surface): **both conditions are potentially non-compliant; the wet surface alone is sufficient to stop the work**

Inspector authority:
- §105.01: Inspector is "for inspection only — cannot alter contract or waive provisions"
- **Inspectors cannot independently halt work.** The stop-work authority flows through the Resident Engineer under §105.12

Correct field sequence (added to `105-control-of-work.md` after gap identified):
1. Inspector observes the violation (wet surface, 48°F conditions)
2. Inspector immediately notifies the Resident Engineer
3. RE issues stop-work direction under §105.12

**Pre-patch rating: ⚠️ Partial** — weather and wet surface provisions were fully answerable from 401.03(A); the Inspector stop-work chain required cross-page inference between `401` and `105`

**Post-patch rating: ✅ Full** — `105-control-of-work.md` updated with explicit three-step chain

**Gap fix applied:** Added QRSE Notes bullet to `105-control-of-work.md` (§105.01, §105.12) making the Inspector → RE → stop-work sequence explicit

---

## Overall Score

| Q | Pre-patch | Post-patch |
|---|-----------|------------|
| 1 | ✅ | ✅ |
| 2 | ✅ | ✅ |
| 3 | ✅ | ✅ |
| 4 | ✅ | ✅ |
| 5 | ⚠️ | ✅ |
| **Total** | **4/5** | **5/5** |

**Conclusion:** The wiki passes the validation test. A QRSE staff member can answer all 5 realistic contract administration questions directly from the wiki without returning to the source PDFs. The one gap found was minor (a cross-page authority chain) and was patched in under 5 minutes.

---

*Test conducted 2026-05-21 — Day 3 of 3-day POC sprint*
