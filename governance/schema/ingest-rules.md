---
type: schema
created: 2026-05-07
updated: 2026-05-12
status: active
---
# Ingest Rules

A source is fully ingested only when all of the following are true:
1. Raw PDF is present in `wiki/aba/01-sources/raw/`
2. Markdown text extract exists in `wiki/aba/01-sources/raw-content/`
3. Extracted source page exists in `wiki/aba/01-sources/extracted/`
4. At least one synthesis page was updated (`02-concepts/`, `03-frameworks/`, `04-tools/`, `05-field-instruments/`, or `06-lifecycle/`)
5. `indexes/agent-index.md` has been regenerated

## Ingest Sequence

1. Determine canonical filename (`YYYY-org-author-short-title.pdf`)
2. Place raw PDF in `wiki/aba/01-sources/raw/`
3. Generate or update markdown text extract in `wiki/aba/01-sources/raw-content/[canonical-stem].raw-extract.md`
4. Create or update extracted source page in `wiki/aba/01-sources/extracted/`
5. Ensure extracted source frontmatter is complete per `frontmatter-schema.md`
6. Run `python3 scripts/sync_extracted_frontmatter_to_raw_content.py --apply`
7. Update affected concept/framework/tool/instrument/lifecycle pages
8. Update contradictions/risk pages when required
9. Run `python3 scripts/build-index.py`
10. Append ingest entry to `memory/runtime/logs/log.md`

## Source Status Values

- `not-started`: source identified but not yet processed
- `extracted`: source page drafted from document evidence
- `ingested`: extracted page completed and linked into synthesis layer
- `reviewed`: source reviewed/validated for maintenance cycle

## Raw-content Status Notes

- `raw-content` files are operational mirrors of raw PDFs
- They may carry synced metadata frontmatter but are not the synthesis layer
- They should not be cited as the canonical answer source in domain queries
