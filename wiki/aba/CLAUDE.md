# Urban DRR + ABA LLM Wiki Operating Rules

You maintain a local git-backed LLM Wiki for urban disaster risk reduction and area-based emergency response.

The wiki has three layers:
1. ../raw/ = immutable source documents and extracted text — **ingest input only, never queried for answers**
2. `./00-overview/` through `./13-agent-prompts/` = numbered synthesis sections — **canonical source of truth for all answers**
3. schema/ + CLAUDE.md = operating rules

**File format rule: ALL files in this vault must use .md extension.** This includes extracted source text in ../raw/extracted/. Never create .txt, .csv, or other formats — Obsidian only renders .md files.

## Layer discipline — critical

`../raw/` files are input to the wiki. They are never the answer to a query.

When answering a domain question:
- Read numbered section pages (`./00-overview/` through `./13-agent-prompts/`) — these are the answer source
- Read `./01sources/` pages for citation metadata only (author, year, page)
- Never open `../raw/extracted/` or `../raw/pdf/` to answer a question
- If `wiki/` content is insufficient, flag the gap and state what ingestion is needed — do not bypass the synthesis layer

Never modify raw sources.

Always read index.md before answering domain questions.

## When ingesting a source

- Create or update the source page in ./01sources/
- Update affected concept pages in ./02concepts/
- Update affected tool pages in ./04tools/
- Update lifecycle pages in ./06lifecycle/
- Update field instruments in ./05field-instruments/ if the source implies data collection methods
- Update ./12risks-contradictions/ if claims conflict or require caution
- Update index.md
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

- Search index.md first
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
