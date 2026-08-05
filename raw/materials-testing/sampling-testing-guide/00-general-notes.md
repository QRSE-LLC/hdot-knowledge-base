# Sampling and Testing Guide - General Notes

> **Source:** Sampling and Testing Guide for Acceptance and Verification (HDOT LABS)
> **File:** `inputs/materials-testing/Sampling-and-Testing-Guide-for-Acceptance-and-Verification.pdf`
> **Revision:** July 2023 (QRSE copy dated 2025-05-16)

---

These notes **qualify the frequencies** in the discipline tables. An answer that quotes a
frequency without checking the note it references can be wrong. Summary of what each does:

| Note | What it changes |
|---|---|
| **1** | Spec numbers listed are the common references only; for non-standard items consult LABS. |
| **2** | Verification sampling applies **only when the contract specifies** contractor QC in the acceptance program (and FHWA approves it on federal-aid work). Sets the 1-to-1-for-first-5 rule. |
| **3** | Test not required if the same source is already being tested on other projects (established source). |
| **4S** | Plant-technician gradation testing can cut the sampling schedule to about **1/5**, supplemented by contractor QC results. |
| **5S** | Defines the preferred concrete sampling locations, in order of preference. |
| **6G** | Field compaction frequency is a **preliminary guide only** - it must be made project specific and documented by the **Project Engineer**. Also sets the sand-cone correlation and monthly sample-card requirements. |

> **Note 6G is the most commonly misquoted item in this guide.** Compaction frequencies in the
> geotechnical tables are a starting point, not a fixed requirement. Defer to the Project Engineer.

## A text-extraction artifact to read around

The discipline files were converted from the source PDF with a layout-preserving text
extractor. In the original PDF, quantities like **1,500 yd³** or **1,000 ft²** sit in a
narrow table cell and wrap across two printed lines, with the superscript exponent (`2` or
`3`) sitting slightly off the text baseline. The extractor sometimes drops that exponent onto
its own line - and that line can also catch wrapped overflow text from a neighboring column.

You will see this as a lone `2` or `3` between a line ending in a number like `1,500` and a
following line starting with `yd` or `ft`. **Read the exponent as belonging to the nearest
`yd`/`ft` token, not to whatever else shares its line.** For example:

```text
1 per approximately every 1,500           N/A                1 to 1 for first 5
                                                            3                                                          acceptance tests, 1
                                                          yd per type, per project
                                                                                                                       per 10 thereafter
```

reads as **"1 per approximately every 1,500 yd³ per type, per project"** - the sampling
frequency for structural backfill - with `1 to 1 for first 5 acceptance tests, 1 per 10
thereafter` as the separate, unrelated verification-column text that happens to wrap onto the
same rows. The tables are preserved exactly as extracted so citations stay checkable against
`source-pdfs/`; this note exists so the wrapping does not get mistaken for missing data or
read as a stray, meaningless number. When quoting a quantity, state the unit as cubic yards
or square feet in your own words rather than repeating the bare digit.

---

## Notes, verbatim

```text
Note 1.   Specification Nos. shown are the common references encountered in most construction projects. For non-standard items, consult the Materials Testing & Research Branch.

Note 2.   Sampling and testing performed by the State or County to validate contractor test data when Contractor Quality Control sampling and testing are used in the Materials
          Acceptance Program. This is allowed only when specified in the contract documents and approved by FHWA for federal aid projects.
          When the Contractor Quality Control (QC) test data is utilized by HDOT or its designated agent in the acceptance determination, HDOT or its designated agent shall perform
          verification sampling and testing. The Contractor's QC sampling and testing frequency shall not be less than the acceptance sampling and testing frequency. The verification
          testing by HDOT or its agent should be performed at a frequency of 1 to 1 for the first 5 QC tests, and not less than 10 percent of the acceptance frequency in the quality
          assurance plan thereafter. If statistical comparisons of the QC test data against HDOT or its agent's test data indicates dissimilarity, the verification sampling and testing
          frequency should revert back to 1 to 1.

Note 3.   Not required if the same source is being used on other projects and test is being made. Not necessary to duplicate the test for the sake of the record. The actual test results
          may be used anywhere they are applicable. (Established Source with Acceptable Quality Control/System Basis)

Note 4S. When gradation is being determined by a qualified plant technician at the plant, the guide schedule for gradation and sand equivalent as sampled by the plant inspector may be
         reduced to approximately 1/5. However, the schedule should be supplemented with the contractor's quality control results.

Note 5S. One of the following locations listed in order of preference: (a) Belt from weigh hopper to central or transit mixer; (b) Belt which feeds batch plant bins immediately preceding the
         weigh hopper, (c) Discharge gate of weigh hopper, (d) Discharge gates of bins feeding the weigh hopper at the batch plant. The location and method of sampling are to be
         determined and agreed upon by the Engineer and the Contractor. Once selected, the location and method of sampling are not to be changed during the life of the project, or so
         long as there is no change in Plant’s configuration or operation.

Note 6G. The field compaction testing frequency for soils and aggregate materials is provided as a preliminary guide and should be project specific, finalized and documented by the
         Project Engineer. If necessary, consult the HDOT project Geotechnical Engineer or Materials Testing and Research Branch for the recommended testing frequency.

          Compact each lift to approximately 6 inches thick. Perform density test every other lift. For every fifty (50) field compaction tests, performed by nuclear gauge method or e-
          gauge method OR every 6 months, whichever comes first, perform one sand cone test (in accordance with HDOT TM 1-00 and TM 3-00) side by side testing with e-gauge or
          nuclear gauge. Test result should be within 3% compaction.
          If there is uncertainty of testing frequency, perform compaction test every other lift per 300 lineal ft or 1,000 ft2

          Submit a sample card of compaction testing monthly and at the end of the project. The following shall be provided in each sample card:
          1. pdf file of compaction summary of the month for record,
          2. Excel file of compaction summary of the month for data consolidation. All numbering shall be sequential and cumulative throughout the project.
          3. Sand cone test results.
          4. If e-gauge or nuclear gauge is used, include additional information as indicated in HWY-L website and/or e-gauge or nuclear gauge guide.
          5. All maximum density test results used in the sample card from Laboratory Proctor Tests.
```
