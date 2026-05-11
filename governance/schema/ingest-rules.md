---
type: schema
created: 2026-05-07
updated: 2026-05-11
status: active
---
# Ingest Rules

A source is NOT fully ingested until it appears in:
1. One source page (./01-sources/extracted/)
2. At least one concept page (./02-concepts/)
3. At least one lifecycle page (./06-lifecycle/)
4. Any relevant tool or field instrument page

## Ingest sequence
1. Read spreadsheet: identify lifecycle stage, tool/method, purpose, source, year, URL, notes
2. Match to PDF in ../raw/pdf/
3. Copy PDF with canonical naming convention
4. Record original filename and URL in source page metadata
5. Extract PDF text to ../raw/extracted/ as a .md file (e.g. ../raw/extracted/<canonical-name>.md). All files in this vault must use .md — never .txt. (SKIP: mark as TODO if extraction not available)
6. Create/update source page in ./01-sources/extracted/
7. Update relevant concept pages
8. Update relevant framework pages
9. Update relevant tool pages
10. Update relevant field instrument pages
11. Update relevant lifecycle pages
12. Update risks/contradictions if source contains cautions, limitations, or tensions
13. Update index.md
14. Append to log.md
15. Commit if git available

## Status values
- not-started: source identified but not yet processed
- copied: PDF exists in ../raw/pdf/
- extracted: text extracted to ../raw/extracted/<canonical-name>.md
- ingested: source page created and linked
- reviewed: content verified for accuracy
