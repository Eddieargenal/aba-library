---
type: agent-prompt
prompt_id: build-new-tool-from-sources
status: operational
created: 2026-05-07
updated: 2026-05-07
---
# Build New Tool from Sources

## When to use
When creating a new tool page from one or more source documents.

## Steps
1. Identify the decision question the tool must answer
2. Identify the lifecycle stage
3. Read all relevant `./01sources/` pages for source metadata and links.
4. If source-derived synthesis is already present in concept/tool/lifecycle pages, use that synthesis as primary content.
5. If required content is missing in synthesis pages, flag ingestion gap explicitly and stop short of inventing content.
6. Define 3-7 decision domains for the tool
7. For each domain:
   - Write the decision question
   - Specify evidence required
   - Define field data points
   - Define collection methods
   - Define respondents/data sources
   - Select or create required field instruments
   - Define analysis method
   - Define scoring rule
   - Define decision threshold
   - Identify data quality checks
   - Identify risks and safeguards
   - Link to source foundation
8. Define overall scoring model (weights per domain, score ranges, decision categories)
9. Define 12 minimum outputs
10. Create the tool page using frontmatter-schema.md
11. Create or link required field instruments
12. Update index.md
13. Update relevant lifecycle page
14. Update relevant concept pages
15. Append to log.md

## Layer rule alignment
- Do not use `../raw/pdf/` or `../raw/extracted/` as direct answer content.
- If synthesis is incomplete, document the specific missing ingestion needed and mark affected sections with `TODO[agent]`.
- Follow `CLAUDE.md` and `schema/query-rules.md` if any prompt text appears to conflict with layer rules.

## Quality check
Before finalizing: verify tool passes schema/tool-quality-standard.md. If any decision question lacks evidence collection instructions, the tool is incomplete.
