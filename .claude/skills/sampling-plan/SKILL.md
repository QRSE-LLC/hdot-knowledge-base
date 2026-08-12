---
name: sampling-plan
description: Build the sampling and testing plan for a material or pay item on an HDOT job - which tests are required, at what frequency, sample size, sample location, and which LABS office reviews the submittal. Use when someone names a material or pay item and asks what testing it needs, how many samples for a given quantity, what to submit, or asks for a testing plan for an upcoming operation. Triggers on "what testing do I need", "how many samples for", "sampling plan", "what do I submit for", "testing requirements for".
---

# Sampling plan

Turn a material or pay item into the testing an inspector actually has to perform and submit.

## Steps

1. **Identify the material and the reviewing discipline.** Route to the right file in
   `raw/materials-testing/sampling-testing-guide/` (`01` bituminous, `02` geotechnical,
   `03` structural, `04` other). If given a pay item number, check
   `raw/materials-testing/master-material-list/` for the division to find the certification class
   and reviewing office.

2. **Pull every required test for that material.** Read the full item. Materials have multiple
   sub-tests — a single aggregate carries gradation, sand equivalent, L.A. abrasion, and more,
   each with its own frequency. Do not report only the first one.

3. **Check the notes.** Read `raw/materials-testing/sampling-testing-guide/00-general-notes.md`
   for every note the item references:
   - **Note 6G** makes field compaction frequency a preliminary guide, finalized by the PE.
   - **Note 4S** can cut plant gradation frequency to about 1/5.
   - **Note 3** waives a test for an established source already being tested.
   - **Note 2** verification testing applies only when the contract specifies contractor QC.
   - **Note 5S** sets the preferred concrete sampling locations, in order.

4. **Apply the quantity.** Compute the expected number of samples and show the arithmetic.
   Respect stated minimums and maximums ("minimum 1 per day", "not less than 1 per project").
   If the quantity falls under a small-quantity threshold, use that column instead and say so.
   Watch units — cubic yards, square feet, and lineal feet all appear, and the source PDF's
   superscript exponents can be displaced by text extraction.

5. **Check the contract tier.** Special Provisions can tighten any frequency and are not in this
   repo. Say so, and name what to confirm from the contract.

6. **Add what gets submitted.** From `raw/materials-testing/qualifications/`: samples go to LABS
   under a JC transmittal, the sampler must be FSTQP qualified for that material class, and
   qualification lapses without an IA evaluation in the last 12 months. For HWY-LB items, a COC
   requires test results attached.

## Output

Keep it field-usable. A short table, then the qualifiers.

| Test | Frequency | Sample size | Location | Spec |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |

Then, briefly:

- **For your quantity:** the sample count, with the arithmetic shown.
- **Notes that change this:** any that apply, named.
- **Submit:** form, reviewing office (LB / LG / LS / LR), sampler qualification needed.
- **Contract check:** what to confirm in the Special Provisions or with the PE.

## Rules

- Quote frequencies verbatim, including "approximately."
- Cite the file and item number for every row.
- Never invent a test, frequency, or sample size. If the guide does not list it, say so.
- Compaction frequencies are always provisional. Name the PE.

## Related

- `wiki/concepts/concept-materials-acceptance-and-verification.md`
- `wiki/concepts/concept-material-certification-and-submittals.md`
- `wiki/concepts/concept-compaction-testing.md`
- `wiki/concepts/concept-sampler-qualification.md`
