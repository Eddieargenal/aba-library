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
3. Read all relevant source pages and raw extracted text
4. Define 3-7 decision domains for the tool
5. For each domain:
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
6. Define overall scoring model (weights per domain, score ranges, decision categories)
7. Define 12 minimum outputs
8. Create the tool page using frontmatter-schema.md
9. Create or link required field instruments
10. Update index.md
11. Update relevant lifecycle page
12. Update relevant concept pages
13. Append to log.md

## Quality check
Before finalizing: verify tool passes schema/tool-quality-standard.md. If any decision question lacks evidence collection instructions, the tool is incomplete.
