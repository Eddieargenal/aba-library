---
type: overview
status: operational
created: 2026-05-07
updated: 2026-05-07
---
# Agent Contract (Canonical)

This page is the single source of truth for how agents must operate in this wiki.  
If instructions conflict across files, follow this contract.

## Rule precedence
1. `./00overview/agent-contract.md` (this page)
2. `CLAUDE.md` and `schema/*.md`
3. `./13agent-prompts/*.md`
4. Page-local notes and TODO markers

## Layer discipline (hard rule)
- `../raw/pdf/` and `../raw/extracted/` are ingest input layers only.
- `wiki/` is the canonical answer layer.
- `schema/` defines behavior and quality rules.
- Never use `../raw/` files as direct answer content for domain queries.

## Domain query workflow
1. Read `index.md`.
2. Identify relevant lifecycle stage(s).
3. Read relevant `wiki/` pages (concepts, tools, lifecycle, coordination, risk pages).
4. Use `./01sources/` pages for citation metadata and traceability.
5. Produce practical outputs with explicit evidence and decision logic.
6. If reusable synthesis emerges, write it back into the wiki and append `log.md`.

## Incomplete-content behavior
- If a needed page is draft/TODO, state the gap explicitly.
- Do not fill gaps by bypassing synthesis and reading `../raw/` as answer content.
- Record what ingestion/update is required to close the gap.

## Tool response minimum (hard rule)
For tool-oriented answers, include:
- Decision question
- Evidence needed
- Field data points
- Collection method
- Respondent/data source
- Instrument
- Analysis rule
- Decision threshold
- Data quality checks
- Risks and safeguards
- Source foundation

## Quality and lint obligations
- Use `schema/tool-quality-standard.md` for pass/fail tool quality.
- Use `schema/lint-rules.md` for wiki lint criteria.
- Run `./13agent-prompts/run-manual-lint-checklist.md` when automation is unavailable.

## Prohibited behaviors
- Fabricating evidence or citations
- Presenting stubs as validated guidance
- Skipping risk/contradiction checks for high-impact recommendations
- Ignoring known stale/superseded guidance

