---
type: schema
created: 2026-05-07
updated: 2026-05-11
status: active
---
# Query Rules

## The three-layer rule — READ THIS FIRST

The wiki has three layers with distinct roles:

| Layer | Location | Role | Query use |
|---|---|---|---|
| Raw | `../raw/pdf/`, `../raw/extracted/` | Ingest input only — immutable source documents | NEVER read for answers |
| Synthesis | `./00-overview/` through `./12-risks-contradictions/` | Canonical source of truth for all answers | Always read here first |
| Schema | `governance/schema/`, `governance/aba/CLAUDE.md` | Operating rules | Read when behavior is unclear |

**`../raw/` files are input to the wiki, not output from it. If the wiki synthesis does not contain the answer, flag the gap — do not go to `../raw/` to find it.**

The synthesis pages (e.g., `./02-concepts/`, `./04-tools/`) represent the processed, validated, agent-ready knowledge. Reading raw extracted text bypasses this layer, produces unverified answers, and defeats the purpose of the wiki.

## Before answering any domain question
1. Read index.md
2. Identify the relevant pages in the numbered synthesis sections — concepts, tools, field instruments, lifecycle, risk pages
3. Read those synthesis pages — these are your answer source
4. Use `./01sources/` pages for citation metadata (author, year, page number) only — not as answer content
5. Produce practical outputs for technical teams

## When wiki content is insufficient
- Note the gap explicitly in your answer
- State which source has not yet been ingested
- Do not go to `../raw/extracted/` or `../raw/pdf/` to fill the gap
- Do not fabricate evidence
- Flag what ingestion is needed to complete the answer

## When a user asks for a tool
Do NOT provide only conceptual advice. Every tool response must include:
- Decision question
- Evidence needed
- Field data points
- Collection method
- Respondent/source
- Instrument
- Analysis rule
- Decision threshold
- Data quality check
- Risks and safeguards

## When a query produces reusable synthesis
File it back into the wiki in the appropriate section.
Append a query entry to log.md.

## If a page is incomplete (contains TODO markers)
- Note the gap explicitly
- Use available source pages for partial answers
- Do not fabricate evidence or tools
- Flag what additional ingestion is needed
