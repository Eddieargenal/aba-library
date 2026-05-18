---
title: ABA/DRR Field Knowledge Wiki — Summary Description
type: summary-description
status: active
created: 2026-05-12
updated: 2026-05-12
---

---
title: ABA/DRR Field Knowledge Wiki
type: architecture-document
doc_id: wiki-architecture-v3
version: "3.0"
status: active
created: 2026-05-11
updated: 2026-05-12
authors: ["Eddie Argenal"]
tags: [wiki, aba, drr, llm, knowledge-management, architecture, governance]
corpus_role: governance
related_docs:
  - AGENTS.md
  - governance/aba/CLAUDE.md
  - governance/schema/frontmatter-schema.md
  - governance/schema/changelog.md
  - indexes/agent-index.md
---

# ABA/DRR Field Knowledge Wiki

A compounding operational memory for urban disaster risk reduction and area-based humanitarian response — built and maintained by LLMs on top of Obsidian.

---

## Part 1 — The Concept

### The Problem

Standard humanitarian knowledge management looks like this: a practitioner searches a document library, finds a relevant guide, reads it, and applies their judgment. The next practitioner does the same thing from scratch. Institutional memory doesn't accumulate — it evaporates with staff turnover. After thirty years of urban crisis response, the field has produced hundreds of frameworks, tools, and field guides, but most teams still rediscover the same lessons independently. The same questions get answered again and again: Is an area-based approach appropriate here? How do we draw boundaries? How do we coordinate without duplicating? How do we hand over without abandoning?

### The Solution

Instead of retrieving from raw documents at query time and re-deriving the same synthesis on every question, the LLM incrementally builds and maintains a persistent wiki — a structured, interlinked collection of markdown files that sits between the raw source literature and the operational team. When a new guidance document arrives, the LLM doesn't just index it for retrieval. It reads it, extracts the key findings, and integrates them into the existing wiki — updating concept pages, revising framework summaries, noting where the new evidence reinforces or challenges existing synthesis, and flagging contradictions that field teams need to resolve. The knowledge is compiled once and then kept current, not re-derived on every query.

This is the key difference: **the wiki is a persistent, compounding operational memory.** The cross-references are already there. The contradictions have already been flagged. The synthesis already reflects everything that's been read. The wiki keeps getting richer with every source added and every question asked.

The LLM writes and maintains all of it. You curate the sources, validate what matters, and ask the right questions. In practice: LLM agent open on one side, Obsidian open on the other. The LLM edits wiki pages based on the conversation; you browse the results in real time — following links, checking the graph view, reading the updated pages. **Obsidian is the IDE. The LLM is the programmer. The wiki is the codebase.**

### Why This Works

The tedious part of maintaining a humanitarian knowledge base is not the reading or the thinking — it's the bookkeeping. Updating cross-references, keeping concept summaries current when new evidence arrives, noting when a 2013 World Bank framework has been partly superseded by 2026 IASC guidance, maintaining consistency across dozens of pages. Teams abandon wikis because the maintenance burden grows faster than the value. LLMs don't get bored, don't forget to update a cross-reference, and can touch 15 files in one pass. The wiki stays maintained because the labor cost of maintenance is reduced substantially. 

The human's job is to curate sources, direct the analysis, validate what the LLM proposes, resolve contradictions the LLM can't resolve alone, and make the actual programme decisions. The LLM's job is everything else.

The idea is related in spirit to Vannevar Bush's Memex (1945) — a personal, curated knowledge store with associative trails between documents. Bush's vision was closer to this than to what the web became: private, actively curated, with the connections between documents as valuable as the documents themselves. The part he couldn't solve was who does the maintenance. The LLM handles that.

In the humanitarian sector specifically, this matters because the cost of rediscovery is measured in programme quality and sometimes in lives. Thirty years of field practice on neighbourhood-level coordination, boundary legitimacy, participatory design, and handover have produced hard-won lessons that exist in scattered PDFs read by people who left the sector. This wiki is an attempt to make those lessons findable, synthesized, and current — so the next practitioner starts where the last one left off.

### Known LLM Failure Modes

This architecture was designed with specific LLM weaknesses in mind. Understanding them is part of operating the system correctly:

- **False consensus on contradictions** — LLMs synthesize toward agreement by default. Without a structural `contradicts:` field requirement, genuine disagreements in the literature get quietly smoothed over. The contradiction architecture exists to prevent this.
- **Silent frontmatter omissions** — LLMs omit required fields without warning. A missing `lifecycle_stage:` doesn't cause an error; it causes a page to be invisible to queries. The lint CRITICAL checks exist specifically for this failure mode.
- **Governance drift mid-session** — LLMs follow behavioral contracts at session start and drift from them under task pressure. The librarian skill session protocol and the Stop hook exist to enforce close discipline even when the agent deprioritizes it.
- **Non-independent source conflation** — LLMs may treat two documents that cite the same underlying evaluation as independent. The source independence rule in promotion gates exists to catch this.

---

## Part 2 — Getting Started

### If You Are New to This Wiki

Read in this order:
1. **This document** — understand the system architecture and your role
2. **`AGENTS.md`** (vault root) — the behavioral contract every agent reads first; defines routing, workflows, and operating rules
3. **`governance/aba/CLAUDE.md`** — ABA-specific operating rules for the LLM
4. **`memory/current-handoff.md`** — what was done in the last session and what needs doing next
5. **`indexes/agent-index.md`** — the current state of the corpus: what's been ingested, what's in progress, what's missing

Do not begin any work — ingestion, querying, or editing — before reading `memory/current-handoff.md` and clearing any open compliance items from the lint queue.

### If You Are a New Agent Session

MANDATORY SESSION OPEN PROTOCOL:

1. Read memory/current-handoff.md
    
2. Read outputs/internal/ for any uncleared lint reports
    
3. Clear all CRITICAL compliance items before beginning new work
    
4. Confirm indexes/agent-index.md is current (check log.md for last build-index run)
    
5. Begin assigned task



---

## Part 3 — Architecture

### The Five Layers

**Raw sources** — `wiki/aba/01-sources/raw/`
The curated literature base: PDFs of IASC guidance, IFRC frameworks, ALNAP evaluations, academic studies, and field guides. Immutable — the LLM reads from them during ingest but never modifies them. This is the evidence floor. Currently 22 documents spanning 2009–2026.

**Raw-content mirror** — `wiki/aba/01-sources/raw-content/`
Markdown text extracts generated from raw PDFs for fast local reading and agent tooling. These are operational convenience files — not the synthesis layer. They do not replace extracted source pages. Frontmatter is synced from extracted source pages using `scripts/sync_extracted_frontmatter_to_raw_content.py --apply`. **Trust hierarchy: extracted source page is authoritative; raw-content mirror is derived.**

**Extracted sources** — `wiki/aba/01-sources/extracted/`
One LLM-generated structured page per document (currently 22 pages). Each records: key concepts and definitions, methodology notes, key claims with page references, and a required `contradicts:` field. An empty `contradicts: []` is a meaningful assertion — the source was checked and found consistent. A missing field means nobody checked. This layer makes the corpus scalable: agents read extracted pages rather than raw PDFs on every query.

**The wiki** — `wiki/aba/` sections 00–12
The synthesis layer. 13 numbered sections, each with a `00_*-index.md` entry point:

| # | Section | What it contains |
|---|---|---|
| 00 | Overview | Agent contract, operating model, knowledge map |
| 01 | Sources | Extracted evidence pages + raw inventory |
| 02 | Concepts | 25 concept pages |
| 03 | Frameworks | 9 Tier 1 operational + 32 Tier 2 reference frameworks |
| 04 | Tools | 17 step-by-step operational tools |
| 05 | Field instruments | 18 data collection instruments |
| 06 | Lifecycle | 9-stage programme cycle with minimum outputs per gate |
| 07 | Sector applications | 21 sector pages (WASH, shelter, livelihoods, protection, health, DRR, and more) |
| 08 | Coordination | 19 pages: ABC modality, actor mapping, duplication detection, referral pathways |
| 09 | Monitoring & learning | 11 MEL and adaptive management pages |
| 10 | Transition & scale | 8 handover and scale-up pages |
| 11 | Patterns | Validated implementation patterns (empty — threshold not yet met) |
| 12 | Risks & contradictions | 13 risk registers, misuse patterns, known contradictions, stale guidance |

**Sector (07) and Coordination (08) pages** follow the same frontmatter schema as concept pages. They carry `contradicts:`, `known_tensions:`, `related_tools:`, `related_frameworks:`, and `lifecycle_stage:`. They are Tier 2 by default unless explicitly promoted to Tier 1 by human decision logged in `governance/schema/changelog.md`.

**The schema** — `AGENTS.md` + `governance/`
The operating rules. `AGENTS.md` at vault root is the single most important file — every agent reads it first. `governance/aba/CLAUDE.md` holds ABA-specific rules. `governance/schema/frontmatter-schema.md` defines required fields and controlled vocabulary per page type. `governance/schema/changelog.md` logs every schema change — unlogged schema change = CRITICAL failure.

---

## Part 4 — Frontmatter Schema

Frontmatter completeness is the highest-priority compliance requirement. A missing required field is a **retrieval blackhole**: the page will not surface in agent queries for that category, silently, with no error.

### Source Page

```yaml
***
type: source
source_id:           # canonical-filename-without-ext e.g. 2017-sanderson-sitko-urban-aba-guide
title:               # full document title
authors_or_orgs:     # list — e.g. [IASC, OCHA]
year:                # YYYY or range e.g. 2017-2019
canonical_file:      # ../raw/[canonical-filename].pdf
original_filename:   # original filename from source_metadata.csv
source_url:          # full URL or "unknown"
source_matrix_row:   # row number(s) in source_metadata.csv
status:              # not-started | copied | extracted | ingested | reviewed
relevance:           # one sentence — why this source matters to the wiki
primary_topics:      # list — e.g. [urban-response, area-based-approach, coordination]
region:              # MENA | LAC | SSA | SEA | global | ISO-3166-1-alpha-3
source_type:         # iasc-guidance | ifrc-framework | un-policy | academic | field-evaluation | ngo-guidance | government-policy
reliability_tier:    # 1 | 2
lifecycle_stage:     # list — from controlled vocabulary
contradicts:         # REQUIRED — [] if none, list of wiki slugs if any
used_for:            # list of tool_ids or framework slugs that cite this source
confidence:          # high | medium | low
created:             # YYYY-MM-DD
updated:             # YYYY-MM-DD
***
```

### Tool Page

```yaml
***
type: tool
tool_id:                  # tool-NN-short-name e.g. tool-01-area-selection-matrix
title:                    # full tool name
tier:                     # 1
status:                   # draft | tested | validated
lifecycle_stage:          # list — from controlled vocabulary
primary_users:            # list — e.g. [programme-officer, field-coordinator, cluster-lead]
source_foundation:        # list of source_ids — min 2 independent sources for Tier 1
field_instruments:        # list of instrument_ids — REQUIRED before validated status
related_concepts:         # list of concept page slugs
related_frameworks:       # list of framework slugs
related_lifecycle_pages:  # list of lifecycle page slugs
region:                   # list — applicable regions
used_by_outputs:          # [] or list of output slugs
contradicts:              # REQUIRED — [] if none
created:                  # YYYY-MM-DD
updated:                  # YYYY-MM-DD
***
```

### Field Instrument Page

```yaml
***
type: field-instrument
instrument_id:                 # short-name e.g. area-selection-scoring-matrix
title:                         # full instrument name
format:                        # form | checklist | guide | matrix | survey | dashboard
can_export_to:                 # list — markdown | excel | kobo | word | pdf
related_tool:                  # tool_id of parent tool — exactly one
required_for_decision_domains: # list
lifecycle_stage:               # list — from controlled vocabulary
primary_users:                 # list
data_quality_checks:           # true | false
status:                        # draft | tested | validated
created:                       # YYYY-MM-DD
updated:                       # YYYY-MM-DD
***
```

### Concept Page

```yaml
***
type: concept
title:                    # concept name
status:                   # draft | stable | contested
maturity:                 # emerging | established | contested
source_count:             # N — number of independent sources supporting this concept
related_tools:            # list of tool_ids
related_frameworks:       # list of framework slugs
related_concepts:         # list of related concept slugs
related_lifecycle_stages: # list — from controlled vocabulary
region:                   # list
known_tensions:           # REQUIRED — [] if none, list of tension descriptions if any
contradicts:              # REQUIRED — [] if none
used_by_outputs:          # [] or list of output slugs
created:                  # YYYY-MM-DD
updated:                  # YYYY-MM-DD
***
```

### Framework Page

```yaml
***
type: framework
framework_id:             # slug e.g. 2017-neighborhood-diagnosis-framework
title:                    # full framework name
tier:                     # 1 | 2
status:                   # draft | active | superseded
lifecycle_stage:          # list — from controlled vocabulary
source_foundation:        # list of source_ids
related_tools:            # list of tool_ids
related_concepts:         # list of concept slugs
related_frameworks:       # list of framework slugs
region:                   # list
used_by_outputs:          # [] or list of output slugs
superseded_by:            # slug of replacement framework, or null
contradicts:              # REQUIRED — [] if none
created:                  # YYYY-MM-DD
updated:                  # YYYY-MM-DD
***
```

### Synthesis / Output Page

```yaml
***
type: synthesis
output_id:              # short slug
title:                  # full title
output_class:           # internal | external
format:                 # analysis | comparison | decision-memo | proposal-section | slide-deck | training-material
source_foundation:      # list of source_ids
frameworks_used:        # list of framework slugs
tools_used:             # list of tool_ids
concepts_used:          # list of concept slugs
lifecycle_stage:        # list
region:                 # list
status:                 # draft | final
created:                # YYYY-MM-DD
updated:                # YYYY-MM-DD
***
```

### Controlled Vocabulary

**`lifecycle_stage`** — `appropriateness-decision` · `area-selection` · `neighbourhood-diagnosis` · `joint-prioritization` · `coordination-design` · `integrated-area-strategy` · `implementation-adaptation` · `monitoring-learning` · `transition-handover`

**`maturity`** — `emerging` · `established` · `contested`

**`format` (field instruments)** — `form` · `checklist` · `guide` · `matrix` · `survey` · `dashboard`

**`can_export_to`** — `markdown` · `excel` · `kobo` · `word` · `pdf`

**`confidence`** — `high` · `medium` · `low`

**`status`** — `draft` · `active` · `ingested` · `validated` · `archived` · `superseded` · `reference`

**`source_type`** — `iasc-guidance` · `ifrc-framework` · `un-policy` · `academic` · `field-evaluation` · `ngo-guidance` · `government-policy`

**`region`** — `MENA` · `LAC` · `SSA` · `SEA` · `global` · ISO 3166-1 alpha-3 country code

---

## Part 5 — Quality Tiers

**Tier 1 — Operational frameworks** directly answer field team decisions: Is an ABA appropriate? How do we select target areas? How do we design a joint prioritization process? Each Tier 1 page defines decision logic, evidence requirements, use conditions, known failure modes, and linked field instruments. Requires ≥2 independent extracted sources and an explicit synthesis thesis.

**Tier 2 — Reference frameworks** summarize the wider DRR, urban resilience, and humanitarian coordination literature. They inform Tier 1 pages but are not operational decision tools. Sector (07) and Coordination (08) pages are Tier 2 by default.

---

## Part 6 — Promotion Gates

The LLM proposes every promotion. The human approves quality-affecting decisions.

| Promotion | Requirement | Human review criteria | Who decides |
|---|---|---|---|
| Finding → concept page | Appears in ≥2 independent extracted sources | Are the sources genuinely independent? Does the finding hold across both? | LLM proposes, human approves |
| Concept → Tier 1 framework | Defined decision logic + explicit use conditions | Is the decision logic unambiguous? Are use conditions field-testable? | Human approves |
| Tier 1 → linked tool | Field-applicable scoring criteria + known failure modes | Can a field coordinator use this without additional guidance? Are failure modes operationally realistic? | Human approves |
| Tool → `validated` status | All `field_instruments` linked + `data_quality_checks: true` | Have instruments been reviewed for completeness? Are DQ checks realistic for field conditions? | Human approves |

**Source independence rule:** Two documents citing the same underlying evaluation are not independent. The LLM must verify distinct evidence bases before flagging a promotion for human review. If independence cannot be confirmed, the promotion is blocked pending a third source.

---

## Part 7 — Contradictions as First-Class Objects

Every page type carries a required `contradicts:` frontmatter field. Every concept page additionally requires a `known_tensions:` frontmatter field and a `## Known Tensions` body section. The lint check treats a missing `contradicts:` field as CRITICAL.

A contradiction reviewed and classified is more valuable than a clean page that silently ignores a disagreement. The wiki would grow more dangerous the richer it became if it didn't track its own limits.

**Contradiction aging policy:** Unresolved contradictions older than 30 days are flagged HIGH in lint. Unresolved contradictions older than 90 days are escalated to CRITICAL and block new ingest in the affected topic area until resolved.

---

## Part 8 — Query Architecture

### Frontmatter-First, Wikilink-Second

The agent's primary navigation mechanism is frontmatter queries, not wikilink traversal. Parse all frontmatter blocks to find relevant pages, then read only those 3–5. Token cost stays proportional to question complexity regardless of corpus size.

```python
# All tools for joint prioritization
type == "tool" AND lifecycle_stage contains "joint-prioritization"

# Sources contradicting a specific concept
type == "source" AND contradicts contains "concept-urban-resilience"

# Contested concepts with thin evidence
type == "concept" AND maturity == "contested" AND source_count <= 2

# Field instruments exportable to KoboToolbox
type == "field-instrument" AND can_export_to contains "kobo"

# Tools with no linked field instruments
type == "tool" AND field_instruments == []

# Sources ingested but not yet reviewed
type == "source" AND status == "ingested"

# Multi-field: MENA tools with post-2018 evidence
type == "tool" AND region contains "MENA" AND lifecycle_stage contains "neighbourhood-diagnosis"
```

### Dual-Layer Navigation Contract

| Layer | Consumer | Purpose |
|---|---|---|
| Frontmatter queries | Agent | Machine-readable, fast, structured retrieval |
| Wikilinks | Obsidian graph view + human browsing | Visualization and human navigation |

Wikilinks are maintained in page bodies so the Obsidian graph view stays meaningful. The agent does not traverse wikilinks at query time. A page with a missing `lifecycle_stage:` or `contradicts:` field is a retrieval blackhole — it will not surface in agent queries for that category, silently, with no error.

---

## Part 9 — Operations

### Ingest

You add a new source PDF to `wiki/aba/01-sources/raw/` and ask the LLM to process it.

1. Store raw PDF (immutable evidence floor)
2. Generate markdown extract in `raw-content/` (page-level text mirror)
3. Create extracted source page with all required frontmatter — `contradicts:` explicitly set
4. Run `scripts/sync_extracted_frontmatter_to_raw_content.py --apply`
5. Update affected concept, framework, and tool pages — add cross-links and wikilinks
6. Append to `memory/runtime/logs/log.md`: `## [YYYY-MM-DD] ingest | Source title`
7. Run `scripts/build-index.py` to regenerate `indexes/agent-index.md`
8. Human reviews extracted page and any flagged contradictions
9. Human approves or rejects promotion proposals

A single source typically touches 10–20 wiki pages. Ingesting one at a time and staying involved is recommended — read the extracted page, check the concept updates, guide the LLM on what to emphasize.

### Query

Ask questions against the wiki. The LLM runs a frontmatter query against `indexes/agent-index.md`, reads only the relevant 3–5 pages, and synthesizes an answer with `source_id` citations. Answers that reveal new connections can be filed to `outputs/` as `type: synthesis` pages — explorations compound in the knowledge base.

### Lint

Weekly. Filed to `outputs/lint-report-YYYY-MM-DD.md`. Compliance items cleared before any new work at next session start.

**CRITICAL — fix before any new work:**
- Missing required frontmatter fields per page type (retrieval blackhole)
- `contradicts:` absent on any source, tool, framework, or concept page
- `field_instruments: []` on any tool with `status: validated`
- `governance/schema/changelog.md` not updated since last schema change

**HIGH — clear within the session:**
- `data_quality_checks: false` on any validated field instrument
- `source_count < 2` on any Tier 1 concept page
- Unresolved contradictions older than 30 days
- Orphan pages with no inbound wikilinks
- Tools without linked field instruments

---

## Part 10 — Page Versioning Policy

**Update in place** when: content is refined, cross-references are added, or minor corrections are made. Git history is the audit trail.

**Create a new page and mark old as `superseded`** when: a framework is substantively replaced by newer guidance, a tool's decision logic changes materially, or a concept's maturity classification changes from `established` to `contested`. Add `superseded_by: [new-slug]` to the old page. The evidence chain must remain traceable even when guidance is retired.

**Never delete pages.** Mark `status: archived` for content no longer relevant but retaining historical value. Deletion breaks evidence chains and contradicts the compounding memory model.

---

## Part 11 — Indexing and Logging

**`indexes/agent-index.md`** — Generated by `scripts/build-index.py` from all page frontmatter. Not hand-curated. Organized by page type, each entry showing: file path, title, `lifecycle_stage`, `status`, and key metadata. Regenerated automatically as the final step of every ingest. Currently covers 123 pages across 5 types.

**`memory/runtime/logs/log.md`** — Append-only chronological record: ingests, queries, lint passes, schema changes. Format: `## [YYYY-MM-DD] type | description`. Grep-parseable: `grep "^## \[" log.md | tail -10`.

**`memory/current-handoff.md`** — Session-to-session continuity. Filled at session close: what was done, governance decisions made, open items requiring human action, next session priorities. Read at session open before any other work.

---

## Part 12 — Scale Threshold

When the corpus exceeds **~80 sources or ~200 pages**, the index file alone is insufficient — context cost of reading it grows to the point where it consumes too much of the agent's working window. At that threshold:

1. Deploy a local search engine — `qmd` (BM25/vector hybrid, on-device) is recommended
2. Log the upgrade in `governance/schema/changelog.md`
3. Update `AGENTS.md` to route queries through the search tool rather than the index file directly
4. The `build-index.py` script gets more selective filters — not a different tool, just a smarter query against the same frontmatter

This upgrade is schema-defined, not optional, and must be logged when the threshold is crossed.

---

## Part 13 — Tooling

**`scripts/build-index.py`** — Parses all frontmatter, emits `indexes/agent-index.md`. Standard library only; no external dependencies. Runs after every ingest.

**`scripts/sync_extracted_frontmatter_to_raw_content.py`** — Copies agreed metadata fields from extracted pages to matching raw-content pages. Matching strategy: `canonical_file` path, fallback to `source_id`. Dry-run by default; `--apply` required for writes.

**`obsidian-local-rest-api` plugin** — HTTPS REST API at `localhost:27124`. Enables automation scripts and n8n ingest pipelines to read/write vault files outside active Claude Code sessions. Claude Code accesses the vault directly via filesystem during active sessions; the REST API serves automated workflows between sessions.

**`obsidian-semantic-mcp` plugin** — Bridges the REST API to Claude Code and Hermes as native tool calls. Consolidates vault operations into AI-optimized tools.

**Obsidian Dataview plugin** — Runs queries over page frontmatter for human navigation. The same structured frontmatter that powers agent queries powers Dataview tables: tools by lifecycle stage, concepts by maturity, sources by confidence, instruments by export capability.

**Obsidian graph view** — The best way to see the shape of the wiki: what's connected, which pages are hubs, which are orphans. Wikilinks are maintained specifically so this view stays meaningful.

---

## Part 14 — Governance

- Schema changes logged in `governance/schema/changelog.md` — unlogged change = CRITICAL failure
- `governance/library-governance_guide.md` is the authoritative governance reference — all other copies are explicit references, not duplicates
- Librarian skill at `.claude/commands/librarian.md` is injected at every agent session start
- Weekly lint cadence — compliance queue clears before new work begins
- Wiki is a git repo — every session ends with a commit

**Librarian skill session protocol:**

| Phase | Steps |
|---|---|
| **Open** | Read `memory/current-handoff.md` → read lint queue in `outputs/internal/` → clear all CRITICAL items → begin task |
| **Close** | Fill `memory/current-handoff.md` → update `governance/schema/changelog.md` if schema changed → run lint → run `build-index.py` → append to `memory/runtime/logs/log.md` → git commit |

---

## The Human's Role

- **Curate** — source the right documents; decide what enters the corpus
- **Validate** — approve promotions, review extracted pages, resolve contradictions that require human judgment
- **Ask** — direct analysis, ask operational questions, make actual decisions
- **Evolve the schema** — as the wiki matures, the schema evolves; log every change in `governance/schema/changelog.md`

The LLM's job is everything else. Quality-affecting decisions require human judgment. Everything else is automated.

---

*Version 3.0 — updated 2026-05-12. Supersedes v2.2 (2026-05-11). Gaps addressed: onboarding path, per-page-type frontmatter schema, promotion gate human review criteria, LLM failure modes, page versioning policy, sector/coordination page classification, scale threshold moved to main architecture, raw-content trust hierarchy clarified.*