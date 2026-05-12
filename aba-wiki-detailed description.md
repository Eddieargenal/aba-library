---
title: ABA/DRR Field Knowledge Wiki
type: architecture-document
doc_id: wiki-architecture-v2
version: "2.5"
status: active
created: 2026-05-11
updated: 2026-05-12
authors: ["Eddie Argenal"]
tags: [wiki, aba, drr, llm, knowledge-management, architecture]
corpus_role: governance
related_docs: [governance/00_governance-index.md, governance/schema/changelog.md, AGENTS.md]
---

# ABA/DRR Field Knowledge Wiki

A pattern for building operational knowledge bases for humanitarian response using LLMs.

---

## The Core Idea

Standard humanitarian knowledge management looks like this: a practitioner searches a document library, finds a relevant guide, reads it, and applies their judgment. The next practitioner does the same thing from scratch. Institutional memory doesn't accumulate — it evaporates with staff turnover. After thirty years of urban crisis response, the field has produced hundreds of frameworks, tools, and field guides, but most teams still rediscover the same lessons independently.

The idea here is different. Instead of searching a document library at decision time, the LLM incrementally builds and maintains a structured wiki — an interlinked collection of synthesis pages that sits between the raw source literature and the operational team. When a new guidance document arrives, the LLM doesn't just index it for retrieval. It reads it, creates a structured extraction page, and integrates the findings into the existing wiki — updating concept pages, noting where the new evidence reinforces or challenges existing frameworks, and flagging contradictions that field teams need to resolve. The knowledge compounds. A practitioner arriving on day one has access to everything learned from every source ever read, already synthesized, already cross-referenced, already contextualized to their decision.

This is the key difference: **the wiki is a persistent, compounding operational memory.** The synthesis is already done. The contradictions are already flagged. The decision logic is already traced back to its evidence base. The LLM drafts and maintains all of it. The human validates what matters.

---

## Architecture

There are four primary layers plus one operational mirror.

**Raw sources** — the curated literature base. PDFs of IASC guidance, IFRC frameworks, academic studies, evaluation reports. Immutable. The LLM reads from them during ingest but never modifies them. This is the evidence floor.

**Raw-content mirror** — markdown text extracts generated from raw PDFs and stored in `wiki/aba/01-sources/raw-content/`. These files preserve page-level source text in `.md` format for fast local reading and agent tooling. They are not the synthesis layer and do not replace extracted source pages; they are an operational convenience layer for ingestion and review workflows. Frontmatter is synced from extracted source pages using `scripts/sync_extracted_frontmatter_to_raw_content.py`.

**Extracted sources** — one LLM-generated structured page per document. Key findings, methodology notes, source citations, and a `contradicts:` frontmatter field listing any existing wiki pages this source challenges. The `contradicts:` field is required on every extracted source page — an empty array `[]` is a meaningful assertion that the source was checked and found consistent. A missing field means nobody checked. This layer is what makes the corpus scalable: the LLM reads the extracted page rather than the raw PDF on every subsequent query.

**The wiki** — the synthesis layer. Structured pages for concepts, decision frameworks, operational tools, field instruments, lifecycle stages, coordination models, and known risks. The LLM drafts and maintains this layer entirely. Every concept page has a `known_tensions:` frontmatter field and a `## Known Tensions` body section. Contradictions are first-class objects, not footnotes.

**The schema** — `AGENTS.md` at the vault root plus a library of operational prompts. Defines the frontmatter schema, promotion gates, and quality thresholds that govern how knowledge earns its place in each layer. `AGENTS.md` is the single most important file — every agent reads it first.

---

## Query Architecture: Frontmatter-First, Wikilink-Second

The agent's primary navigation mechanism is **frontmatter queries, not wikilink traversal**. Frontmatter is structured data — a Python script can query it in milliseconds without the agent reading any page content. The token cost difference is significant: parse all frontmatter blocks to find relevant pages, then read only those 3–5.

The query model:

```python
# "find all tools that apply to joint prioritization"
pages where lifecycle_stage contains "joint-prioritization"
       and type == "tool"

# "find all sources that contradict concept-X"
pages where contradicts contains "concept-X"

# "find everything related to a specific framework"
pages where related_frameworks contains "2017-neighbourhood-diagnosis-framework"
       or source_foundation contains "2017-neighbourhood-diagnosis-framework"

# "which field instruments can export to KoboToolbox?"
pages where type == "field-instrument"
       and can_export_to contains "kobo"

# "which concepts have low source count and contested maturity?"
pages where type == "concept"
       and maturity == "contested"
       and source_count <= 2

# "which tools have no linked field instruments?"
pages where type == "tool"
       and field_instruments == []

# "which sources have been ingested but not yet reviewed?"
pages where type == "source"
       and status == "ingested"
```

**The dual-layer navigation contract:**

| Layer | Consumer | Purpose |
|---|---|---|
| Frontmatter | Agent queries | Machine-readable, fast, structured retrieval |
| Wikilinks | Obsidian graph view + human browsing | Visualization and human navigation |

Wikilinks are maintained in page bodies for the Obsidian graph view and human navigation. The agent does not traverse wikilinks at query time — it runs frontmatter queries and reads the resulting pages directly.

---

## Frontmatter Schema

Frontmatter completeness is the highest-priority compliance requirement. A page with a missing `lifecycle_stage:` or `contradicts:` field is a **retrieval blackhole** — it will not surface in agent queries for that category, silently, with no error. The lint check treats missing required fields as CRITICAL failures.

---

### Source Page

One page per raw document. Created during ingest. Updated on review.

```yaml
---
type: source
source_id:           # canonical-filename-without-ext — e.g. 2017-sanderson-sitko-urban-aba-guide
title:               # full document title
author:              # individual author(s) — e.g. "David Sanderson; Pamela Sitko"
institution:         # publishing organization — e.g. "World Vision / Stronger Cities Consortium (published by IIED)"
year:                # YYYY
canonical_file:      # ../raw/[canonical-filename].pdf
source_url:          # full URL or "unknown"
source_url_status:   # verified | verify | broken
file_type:           # pdf | markdown | xlsx
source_type:         # iasc-guidance | ifrc-framework | un-policy | academic | field-evaluation | ngo-guidance | government-policy
foundational:        # true | false — cited by ≥3 frameworks or foundational to the ABA evidence base
status:              # not-started | extracted | ingested | reviewed
ingest_date:         # YYYY-MM-DD
ingest_status:       # success | partial | failed
confidence:          # high | medium | low — quality of extraction: high=direct field evidence, medium=practitioner judgment, low=theoretical or untested
review_cycle:        # annual | biennial | as-needed
last_reviewed:       # YYYY-MM-DD
next_review:         # YYYY-MM-DD
lifecycle_stage:     # list — from controlled vocabulary
primary_topics:      # list — controlled topic terms for agent queries
tags:                # list — free-form Obsidian tags for graph navigation
contradicts:         # [] or list of wiki page slugs — REQUIRED, empty array if checked and clear
wiki_pages:          # list of wiki pages updated during ingest
notes:               # one-paragraph summary of relevance and key claims
created:             # YYYY-MM-DD
updated:             # YYYY-MM-DD
---
```

---

### Tool Page

One page per operational tool. Tier 1 only. Must have linked field instruments before status reaches `validated`.

```yaml
---
type: tool
tool_id:                  # tool-NN-short-name — e.g. tool-02-area-selection-matrix
title:                    # full tool name
tier:                     # 1
status:                   # draft | tested | validated
lifecycle_stage:          # list — from controlled vocabulary
primary_users:            # list — e.g. [programme-officer, field-coordinator, cluster-lead]
source_foundation:        # list of source_ids — min 2 independent sources for Tier 1
field_instruments:        # list of instrument_ids — REQUIRED before validated status
related_concepts:         # list of concept slugs
related_frameworks:       # list of framework slugs
related_lifecycle_pages:  # list of lifecycle page slugs
used_by_outputs:          # [] or list of output slugs
contradicts:              # [] or list of slugs where this tool's logic conflicts
created:                  # YYYY-MM-DD
updated:                  # YYYY-MM-DD
---
```

---

### Field Instrument Page

One page per data collection instrument. An instrument may feed multiple tools.

```yaml
---
type: field-instrument
instrument_id:                 # short-name slug — e.g. household-mini-survey
title:                         # full instrument name
format:                        # form | checklist | guide | matrix | survey | dashboard
can_export_to:                 # list — markdown | excel | kobo | word | pdf
related_tools:                 # list of tool_ids that use this instrument
required_for_decision_domains: # list — decision domains this instrument feeds
lifecycle_stage:               # list — from controlled vocabulary
primary_users:                 # list
data_quality_checks:           # true | false — whether DQ checks are explicitly defined in page body
status:                        # draft | tested | validated
created:                       # YYYY-MM-DD
updated:                       # YYYY-MM-DD
---
```

---

### Concept Page

One page per operational concept. Promoted from findings once ≥2 independent sources confirm.

```yaml
---
type: concept
title:                    # concept name
status:                   # draft | active | archived — editorial state
maturity:                 # emerging | established | contested — epistemic state
source_count:             # N — number of independent sources supporting this concept
related_tools:            # list of tool_ids that operationalize this concept
related_frameworks:       # list of framework slugs
related_concepts:         # list of related concept slugs
related_lifecycle_stages: # list — from controlled vocabulary
known_tensions:           # [] or list of tension slugs — expanded in ## Known Tensions body section
contradicts:              # [] or list of slugs in direct logical conflict
used_by_outputs:          # [] or list of output slugs
created:                  # YYYY-MM-DD
updated:                  # YYYY-MM-DD
---
```

`known_tensions:` in frontmatter holds slugs for query purposes. The actual tension descriptions live in a `## Known Tensions` section in the page body. Both are required when tensions exist.

---

### Framework Page

```yaml
---
type: framework
framework_id:             # slug — e.g. 2017-neighbourhood-diagnosis-framework
title:                    # full framework name
tier:                     # 1 | 2
status:                   # draft | active | superseded | reference
lifecycle_stage:          # list — from controlled vocabulary
source_foundation:        # list of source_ids
related_tools:            # list of tool_ids
related_concepts:         # list of concept slugs
related_frameworks:       # list of framework slugs
used_by_outputs:          # [] or list of output slugs
superseded_by:            # framework slug or null
contradicts:              # [] or list of slugs
created:                  # YYYY-MM-DD
updated:                  # YYYY-MM-DD
---
```

Tier 1 frameworks use `status: active`. Tier 2 frameworks use `status: reference`. A superseded framework retains its page — the evidence chain must remain traceable even when guidance is replaced.

---

### Synthesis / Output Page

```yaml
---
type: synthesis
output_id:              # short slug
title:                  # full title
output_class:           # internal | external
format:                 # analysis | comparison | decision-memo | proposal-section | slide-deck | training-material
source_foundation:      # list of source_ids drawn on
frameworks_used:        # list of framework slugs
tools_used:             # list of tool_ids
concepts_used:          # list of concept slugs
lifecycle_stage:        # list
status:                 # draft | final
created:                # YYYY-MM-DD
updated:                # YYYY-MM-DD
---
```

---

## Controlled Vocabulary

**`lifecycle_stage`** — use slugs in frontmatter. Maps to the nine ABA operational stages:

| Slug | Stage |
|---|---|
| `appropriateness-decision` | 0. Appropriateness decision |
| `area-selection` | 1. Area selection and boundary definition |
| `neighbourhood-diagnosis` | 2. Area profile and systems diagnosis |
| `joint-prioritization` | 3. Joint prioritization |
| `coordination-design` | 4. Area coordination design |
| `integrated-area-strategy` | 5. Integrated area strategy |
| `implementation-adaptation` | 6. Implementation and adaptation |
| `monitoring-learning` | 7. Monitoring and learning |
| `transition-handover` | 8. Transition and handover |

**`source_type`** — `iasc-guidance` · `ifrc-framework` · `un-policy` · `academic` · `field-evaluation` · `ngo-guidance` · `government-policy`

**`format` (field instruments)** — `form` · `checklist` · `guide` · `matrix` · `survey` · `dashboard`

**`can_export_to`** — `markdown` · `excel` · `kobo` · `word` · `pdf`

**`maturity`** — `emerging` · `established` · `contested`

**`confidence`** — `high` · `medium` · `low`

**`status` (editorial)** — `draft` · `active` · `archived` · `superseded` · `reference`

---

## Quality Tiers

**Tier 1 — Operational frameworks** directly answer field team decisions. Require ≥2 independent extracted sources, explicit decision logic, defined use conditions, linked field instruments, and known failure modes.

**Tier 2 — Reference frameworks** summarize the wider DRR and urban resilience literature. Inform Tier 1 pages but are not operational decision tools. No field instrument requirement.

---

## Promotion Gates

| Promotion | Requirement | Who decides |
|---|---|---|
| Finding → concept page | Appears in ≥2 independent extracted sources | LLM proposes, human approves |
| Concept → Tier 1 framework | Defined decision logic + explicit use conditions | Human approves |
| Tier 1 → linked tool/instrument | Field-applicable scoring criteria + known failure modes | Human approves |
| Tool → `validated` status | All `field_instruments` linked + `data_quality_checks: true` | Human approves |

**Source independence rule:** Two documents citing the same underlying evaluation are not independent. The LLM must verify distinct evidence bases before flagging a promotion for human review.

---

## Contradictions as First-Class Objects

- Every extracted source page carries a required `contradicts:` field
- Every concept page has a required `known_tensions:` frontmatter field and a `## Known Tensions` body section
- Every tool and framework page carries `contradicts:`
- Lint hunts for missing `contradicts:` fields, not just wrong values
- Contradictions unresolvable at the evidence level are escalated as promotion-gate decisions

A contradiction reviewed and classified is more valuable than a clean page that silently ignores the disagreement.

---

## Navigation and Index Generation

### Agent Index: `scripts/build-index.py`

`scripts/build-index.py` parses all frontmatter and emits `indexes/agent-index.md` — a structured, LLM-readable index organized by `type` and `tier`. Each entry shows: file path, title, `lifecycle_stage`, `status`, `source_count` or `contradicts` count. Runs automatically as the final step of every ingest. Not hand-curated — generated from frontmatter.

The agent reads `indexes/agent-index.md` to identify relevant pages, then reads only those pages. Query cost stays proportional to question complexity regardless of corpus size.

### Scale Threshold

When corpus exceeds ~80 sources or ~200 pages, a local search tool (qmd or equivalent) is required. This upgrade is schema-defined and logged in `governance/schema/changelog.md` when crossed.

### Human Layer: Obsidian

Dataview queries against the same frontmatter fields serve human navigation. The graph view is only as rich as the wikilinks in page bodies — wikilinks must be maintained even though the agent does not traverse them for retrieval.

---

## Operations

**Ingest.**
1. LLM stores raw PDF in `wiki/aba/01-sources/raw/` (immutable evidence floor)
2. LLM generates/updates markdown raw extract in `wiki/aba/01-sources/raw-content/` (page-level text mirror)
3. LLM creates extracted source page with all required frontmatter — `contradicts:` explicitly set
4. LLM runs `scripts/sync_extracted_frontmatter_to_raw_content.py --apply` to copy agreed metadata fields from extracted pages into matching raw-content files
5. LLM updates affected concept, framework, and tool pages — adds cross-links and wikilinks
6. LLM appends to `memory/runtime/logs/log.md` using format `## [YYYY-MM-DD] ingest | Source title`
7. LLM runs `scripts/build-index.py` to regenerate `indexes/agent-index.md`
8. Human reviews extracted page and any flagged contradictions
9. Human approves or rejects promotion proposals

**Query.** LLM runs frontmatter query against agent index → reads only relevant pages → synthesizes answer with `source_id` citations. Answers that reveal new connections are filed to `wiki/aba/outputs/internal/` as synthesis pages with `type: synthesis`.

**Lint.** Weekly. Filed to `wiki/aba/outputs/internal/lint-report-YYYY-MM-DD.md`. Mandatory reading at the start of the next session — the LLM clears the compliance queue before taking on new work.

Critical lint checks:
- Missing required frontmatter fields per page type **(CRITICAL — retrieval blackhole)**
- `contradicts:` field absent on any source, tool, framework, or concept page **(CRITICAL)**
- `field_instruments: []` on any tool with `status: validated` **(CRITICAL)**
- `governance/schema/changelog.md` not updated since last schema change **(CRITICAL)**
- `data_quality_checks: false` on any validated field instrument **(HIGH)**
- `source_count < 2` on any Tier 1 concept page **(HIGH)**
- Unresolved contradictions older than 30 days **(HIGH)**
- Orphan pages with no inbound wikilinks **(MEDIUM)**

---

## The Human's Role

- **Curate** — source the right documents, decide what enters the corpus
- **Validate** — approve promotions, resolve contradictions, evolve the schema
- **Ask** — direct analysis, ask operational questions, make actual decisions

The LLM's job is everything else. Quality-affecting decisions require human judgment. Everything else is automated.

---

## API and Tooling

Local REST API via **obsidian-local-rest-api** plugin (HTTPS `localhost:27124`) enables:
- `scripts/build-index.py` and lint runner to read/write vault files without a Claude Code session
- n8n ingest pipelines to create extracted source pages on document arrival
- Native vault tool calls from Claude Code and other agents

**Raw-content metadata sync script:** `scripts/sync_extracted_frontmatter_to_raw_content.py`
- Purpose: copy the agreed frontmatter subset from `wiki/aba/01-sources/extracted/*.md` to matching `wiki/aba/01-sources/raw-content/*.raw-extract.md`
- Matching strategy: `canonical_file` path (fallback to `source_id` when canonical metadata is malformed)
- Safety: dry-run by default; explicit `--apply` required for writes

Claude Code accesses the vault directly via the filesystem during active sessions. The REST API serves automated pipelines and tooling that run outside of agent sessions.

---

## Governance

- Schema changes logged in `governance/schema/changelog.md` — unlogged change = critical failure
- `governance/00_governance-index.md` is the authoritative governance reference — routes to all sub-documents
- Librarian skill at `.claude/commands/librarian.md` injected at every agent session start
- Weekly lint cadence — compliance queue clears before new work begins

**Librarian skill session protocol:**

*Open:* Read `memory/current-handoff.md` → read lint queue → clear compliance items → begin task

*Close:* Fill `memory/current-handoff.md` → update `governance/schema/changelog.md` if schema changed → run lint → run `scripts/build-index.py` → append to `memory/runtime/logs/log.md`

---

*Version 2.3 — updated 2026-05-11. Supersedes v2.2. Frontmatter schemas reconciled with actual vault content: region dropped (global lessons, context adaptation deferred); author/institution separated; source maintenance fields added; field instrument parent tool constraint corrected to plural; concept status/maturity distinction clarified; lifecycle_stage vocabulary expanded to 9 stages matching ABA operational model; governance reference updated to governance/00_index.md.*

*Version 2.4 — updated 2026-05-12. Supersedes v2.3. All section indexes renamed from generic `00_index.md` to descriptive `00_*-index.md` names (e.g. `governance/00_governance-index.md`, `wiki/aba/02-concepts/00_concepts-index.md`). Governance reference updated accordingly. Librarian skill index-exclusion filter updated to `fname.startswith("00_")` pattern.*

*Version 2.5 — updated 2026-05-12. Supersedes v2.4. Added `wiki/aba/01-sources/raw-content/` as an operational markdown mirror of raw PDFs. Documented ingest flow updates for raw-content generation and metadata sync. Added `scripts/sync_extracted_frontmatter_to_raw_content.py` to tooling, including dry-run/apply behavior and canonical-file-first matching with source_id fallback.*
