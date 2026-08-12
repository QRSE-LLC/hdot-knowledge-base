# Materials and testing conversion

Regenerates `raw/materials-testing/` from the source PDFs.

The source PDFs are excluded from the repo per `.gitignore` (redistribution-restricted) and
live in the Drive workshop. Point the script at a local copy to re-run.

```
pdftotext -layout <source>.pdf <name>.txt      # poppler; -layout preserves column alignment
python3 convert_guides.py <txt-dir> <out-repo> <source-dir>
```

## Fidelity rules

- Data rows are preserved verbatim inside fenced blocks, with original column alignment.
- Only repeated page-header and footer boilerplate is stripped.
- Nothing is paraphrased or re-tabulated, so a citation can be checked against the source PDF.
- Known limitation: superscript unit exponents (cubic yards, square feet) can be displaced onto
  their own line by text extraction. Documented in
  `raw/materials-testing/sampling-testing-guide/00-general-notes.md` and logged as open
  question 12. Do not auto-splice these - the displaced line can also carry overflow text from
  an adjacent column, so a naive fix corrupts real data.
