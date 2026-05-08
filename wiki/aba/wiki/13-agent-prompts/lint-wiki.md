---
type: agent-prompt
prompt_id: lint-wiki
status: operational
created: 2026-05-07
updated: 2026-05-07
---
# Lint Wiki

## When to use
Periodically to check wiki quality.

## Steps
1. Read schema/lint-rules.md for the full rule list
2. For each rule, check the relevant pages
3. If automation scripts are unavailable, run [[./13agent-prompts/run-manual-lint-checklist]]
4. Record findings in outputs/wiki-lint-report.md
5. Append lint entry to log.md: ## [YYYY-MM-DD] lint | Wiki quality pass

## Checks to run
1. Orphan pages (no inbound links)
2. Source pages not linked to concept/tool/lifecycle
3. Tool pages without field instruments
4. Decision questions without evidence requirements
5. Field instruments not linked to tools
6. Uncited claims
7. Contradictions between sources
8. Superseded guidance
9. Lifecycle stages without tools
10. Coordination pages without duplication/gap logic
11. DRR guidance without HEVC logic
12. Participation guidance without safeguards
13. Transition pages without responsible actor/budget/maintenance
14. Tools without scoring rules
15. Instruments without data quality checks
16. Empty placeholder pages

## Hard rule
Flag any tool page that asks diagnostic questions but does not define evidence collection.
