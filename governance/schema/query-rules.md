---
type: schema
created: 2026-05-07
updated: 2026-05-12
status: active
---
# Query Rules

## The layer rule — READ THIS FIRST

The wiki has four layers plus one operational mirror with distinct roles:

| Layer | Location | Role | Query use |
|---|---|---|---|
| Raw | `./01-sources/raw/` | Immutable source PDFs | NEVER read for answers |
| Raw-content mirror | `./01-sources/raw-content/` | Markdown text mirror for ingest/review support | NEVER read for answers |
| Extracted source layer | `./01-sources/extracted/` | Structured extraction and source-level metadata | Read for citation/evidence grounding |
| Synthesis | `./00-overview/` through `./12-synthesis/` | Canonical source of truth for domain answers | Always read here first |
| Schema | `governance/schema/`, `governance/aba/CLAUDE.md` | Operating rules | Read when behavior is unclear |

**`01-sources/raw/` and `01-sources/raw-content/` are input/support layers, not answer layers. If synthesis does not contain the answer, flag the gap — do not bypass to raw/raw-content.**

The synthesis pages (e.g., `./02-concepts/`, `./04-tools/`) represent the processed, validated, agent-ready knowledge. Reading raw extracted text bypasses this layer, produces unverified answers, and defeats the purpose of the wiki.

## Before answering any domain question
1. Read index.md
2. Identify the relevant pages in the numbered synthesis sections — concepts, tools, field instruments, lifecycle, risk pages
3. Read those synthesis pages — these are your answer source
4. Use `./01-sources/extracted/` pages for citation metadata and source grounding — not raw/raw-content files
5. Produce practical outputs for technical teams

## When wiki content is insufficient
- Note the gap explicitly in your answer
- State which source has not yet been ingested
- Do not go to `./01-sources/raw/` or `./01-sources/raw-content/` to fill the gap
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
