---
type: agent-prompt
prompt_id: update-crosslinks
status: operational
created: 2026-05-07
updated: 2026-05-07
---
# Update Cross-Links

## When to use
After adding new pages or after a major ingestion pass, to ensure wiki pages are interconnected.

## Steps
1. For each new page: identify which concept, tool, lifecycle, and source pages it should link to
2. For each referenced concept/tool/source: add a link back to the new page
3. Update index.md with the new page entry
4. Check for orphan pages (no inbound links)
5. Run lint check for orphan pages (see lint-wiki.md)
6. Append to log.md: ## [YYYY-MM-DD] crosslinks | Updated cross-links for [pages]
