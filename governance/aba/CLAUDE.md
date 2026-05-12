---
type: agent-guide
status: active
updated: 2026-05-12
---
# Urban DRR + ABA LLM Wiki Operating Rules

You maintain a local git-backed LLM Wiki for urban disaster risk reduction and area-based emergency response.

The wiki has four layers plus one operational mirror:
1. `./01-sources/raw/` = immutable source PDFs — **ingest input only, never queried for answers**
2. `./01-sources/raw-content/` = markdown text mirror of raw PDFs (operational convenience for extraction/review, not synthesis)
3. `./01-sources/extracted/` + `./00-overview/` through `./12-risks-contradictions/` = extracted evidence + synthesis sections — **canonical source of truth for domain answers**
4. `governance/schema/` + `governance/aba/CLAUDE.md` = operating rules

**File format rule: ALL files in this vault must use .md extension.** Never create `.txt`, `.csv`, or other non-markdown artifacts inside the vault.

## Layer discipline — critical

`./01-sources/raw/` and `./01-sources/raw-content/` are ingest inputs/support artifacts. They are never the answer layer for domain queries.

When answering a domain question:
- Read numbered section pages (`./00-overview/` through `./12-risks-contradictions/`) — these are the answer source
- Read `./01-sources/extracted/` pages for citation metadata and evidence grounding
- Never answer from `./01-sources/raw/` or `./01-sources/raw-content/`
- If `wiki/` content is insufficient, flag the gap and state what ingestion is needed — do not bypass the synthesis layer

Never modify raw sources.

Always read indexes/agent-index.md before answering domain questions.

## When ingesting a source

- Add/confirm raw PDF in `./01-sources/raw/`
- Generate/update markdown extract in `./01-sources/raw-content/`
- Create or update the source page in `./01-sources/extracted/`
- Run `scripts/sync_extracted_frontmatter_to_raw_content.py --apply` to sync agreed metadata into raw-content extracts
- Update affected concept pages in ./02-concepts/
- Update affected tool pages in ./04-tools/
- Update lifecycle pages in ./06-lifecycle/
- Update field instruments in ./05-field-instruments/ if the source implies data collection methods
- Update ./12-risks-contradictions/ if claims conflict or require caution
- Update indexes/agent-index.md (run scripts/build-index.py)
- Append to log.md
- Commit if git is available

## When creating a tool

For every decision question, you must include ALL of the following:
- evidence required
- field data points
- collection method
- respondent/source
- field instrument
- analysis method
- scoring or decision threshold
- data quality checks
- risks and safeguards
- source foundation

A tool FAILS quality review if it only lists questions without showing how field teams collect and analyze the evidence.

## When querying

- Search indexes/agent-index.md first
- Read relevant wiki pages before answering
- Use source pages for citation support
- Produce practical outputs for technical teams
- If new reusable synthesis emerges, file it back into the wiki

## When linting

Detect and report:
- Orphan pages (no inbound links)
- Uncited claims
- Stale or contradicted claims
- Tools without field instruments
- Field instruments not linked to tools
- Lifecycle stages without minimum outputs
- Coordination guidance without duplication/gap logic
- DRR guidance without hazard/exposure/vulnerability/capacity logic
- Participation guidance without inclusion and protection safeguards
- Transition guidance without responsible actor, maintenance, budget, and unresolved risk logic
- Tool pages that ask diagnostic questions but don't define evidence collection
- Field instruments without data quality checks
- Empty placeholder pages

## Tool quality standard

A tool page PASSES quality review only if it includes, for each decision question:
1. Evidence required
2. Field data points
3. Collection method
4. Respondent or data source
5. Field instrument
6. Analysis method
7. Scoring or decision threshold
8. Data quality checks
9. Risks and safeguards
10. Source foundation
