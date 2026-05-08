---
type: agent-prompt
prompt_id: ingest-new-source
status: operational
created: 2026-05-07
updated: 2026-05-07
---
# Ingest New Source

## When to use
When a new document needs to be added to the wiki.

## Steps
1. Read the document (or its metadata if not yet extracted)
2. Determine canonical filename: YYYY-org-author-short-title.ext
3. Copy document to ../raw/pdf/ with canonical filename
4. Record original filename and URL in source page metadata
5. Create source page in ./01sources/ using frontmatter-schema.md
6. Identify lifecycle stages this source applies to
7. Update affected concept pages (add source to source_count, link)
8. Update affected tool pages (add to source_foundation)
9. Update affected lifecycle pages (add source link)
10. Update affected field instruments if source implies data collection methods
11. Check for contradictions with existing sources → update ./12risks-contradictions/known-contradictions.md
12. Update index.md
13. Append entry to log.md using format: ## [YYYY-MM-DD] ingest | Source title
14. Commit changes

## Output
- Source page created
- Concept/tool/lifecycle pages updated
- index.md updated
- log.md appended
- Git commit (if available)
