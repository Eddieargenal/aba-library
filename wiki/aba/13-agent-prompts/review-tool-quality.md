---
type: agent-prompt
prompt_id: review-tool-quality
status: operational
created: 2026-05-07
updated: 2026-05-07
---
# Review Tool Quality

## When to use
When auditing a tool page for completeness and quality.

## Steps
1. Read schema/tool-quality-standard.md
2. For each decision question in the tool, check all 10 required fields
3. Check that field instruments are linked and populated
4. Check that scoring rules are defined
5. Check that source foundation is cited
6. Record findings: pass / fail per criterion per question
7. Write findings to outputs/wiki-lint-report.md
8. If tool fails: note exactly what is missing using TODO[agent] format

## Pass criteria
All 10 required fields present for each decision question.
Field instruments linked and non-empty.
Scoring rule defined.
Source foundation cited.
