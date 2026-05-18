---
type: agent-prompt
prompt_id: ingest-new-source
status: operational
created: 2026-05-07
updated: 2026-05-12
---
# Ingest New Source

## When to use
When a new document needs to be added to the wiki.

## Steps
1. Read the document (or its metadata if not yet extracted)
2. Determine canonical filename: YYYY-org-author-short-title.ext
3. Copy raw PDF to `./01-sources/raw/` with canonical filename
4. Generate or update markdown text extract at `./01-sources/raw-content/[canonical-stem].raw-extract.md`
5. Record original filename and URL in source page metadata
6. Create/update source page in `./01-sources/extracted/` using `frontmatter-schema.md`
7. Run `scripts/sync_extracted_frontmatter_to_raw_content.py --apply`
8. Identify lifecycle stages this source applies to
9. Update affected concept pages (add source to source_count, link)
10. Update affected tool pages (add to source_foundation)
11. Update affected lifecycle pages (add source link)
12. Update affected field instruments if source implies data collection methods
13. Check for contradictions with existing sources → update `./12-risks-contradictions/known-contradictions.md` when needed
14. Run `scripts/build-index.py` to regenerate `indexes/agent-index.md`
15. Append entry to `memory/runtime/logs/log.md` using format: `## [YYYY-MM-DD] ingest | Source title`
16. Commit changes

## Output
- Raw PDF placed in `01-sources/raw/`
- Raw-content markdown extract created/updated
- Source page in `01-sources/extracted/` created/updated
- Raw-content frontmatter synced from extracted source page
- Concept/tool/lifecycle pages updated
- `indexes/agent-index.md` regenerated
- log appended
- Git commit (if available)
