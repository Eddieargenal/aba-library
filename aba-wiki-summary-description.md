---
title: ABA/DRR Field Knowledge Wiki — Summary Description
type: summary-description
status: active
created: 2026-05-12
updated: 2026-05-12
---

# ABA/DRR Field Knowledge Wiki

A compounding operational memory for urban disaster risk reduction and area-based humanitarian response — built and maintained by LLMs on top of Obsidian.

---

## The core idea

Standard humanitarian knowledge management looks like this: a practitioner searches a document library, finds a relevant guide, reads it, and applies their judgment. The next practitioner does the same thing from scratch. Institutional memory doesn't accumulate — it evaporates with staff turnover. After thirty years of urban crisis response, the field has produced hundreds of frameworks, tools, and field guides, but most teams still rediscover the same lessons independently. The same questions get answered again and again: Is an area-based approach appropriate here? How do we draw boundaries? How do we coordinate without duplicating? How do we hand over without abandoning?

The idea here is different. Instead of retrieving from raw documents at query time and re-deriving the same synthesis on every question, the LLM **incrementally builds and maintains a persistent wiki** — a structured, interlinked collection of markdown files that sits between the raw source literature and the operational team. When a new guidance document arrives, the LLM doesn't just index it for later retrieval. It reads it, extracts the key findings, and integrates them into the existing wiki — updating concept pages, revising framework summaries, noting where the new evidence reinforces or challenges existing synthesis, and flagging contradictions that field teams need to resolve. The knowledge is compiled once and then *kept current*, not re-derived on every query.

This is the key difference: **the wiki is a persistent, compounding operational memory.** The cross-references are already there. The contradictions have already been flagged. The synthesis already reflects everything that's been read. The wiki keeps getting richer with every source added and every question asked.

The LLM writes and maintains all of it. You curate the sources, validate what matters, and ask the right questions. In practice: LLM agent open on one side, Obsidian open on the other. The LLM edits wiki pages based on the conversation; you browse the results in real time — following links, checking the graph view, reading the updated pages. Obsidian is the IDE. The LLM is the programmer. The wiki is the codebase.

---

## Architecture

There are five layers plus one operational mirror.

**Raw sources** — `wiki/aba/01-sources/raw/`
The curated literature base: PDFs of IASC guidance, IFRC frameworks, ALNAP evaluations, academic studies, and field guides. Immutable — the LLM reads from them during ingest but never modifies them. This is the evidence floor. Currently 22 documents spanning 2009–2026, from Twigg's disaster-resilient community guidance to the IASC 2026 area-based coordination Terms of Reference.

**Raw-content mirror** — `wiki/aba/01-sources/raw-content/`
Markdown text extracts generated from raw PDFs, stored for fast local reading and agent tooling. Not the synthesis layer — these files do not replace extracted source pages. They are an operational convenience for ingestion and review workflows. Frontmatter is synced from extracted source pages using `scripts/sync_extracted_frontmatter_to_raw_content.py --apply`.

**Extracted sources** — `wiki/aba/01-sources/extracted/`
One LLM-generated structured page per document (22 pages). Each page records: key concepts and definitions found in the source, methodology notes, key claims with page references, and a required `contradicts:` frontmatter field listing any existing wiki pages this source challenges. An empty `contradicts: []` is a meaningful assertion — the source was checked and found consistent. A missing field means nobody checked. This layer is what makes the corpus scalable: agents read extracted pages rather than raw PDFs on every subsequent query.

**The wiki** — `wiki/aba/` sections 00–12
The synthesis layer. Structured pages for concepts, decision frameworks, operational tools, field instruments, lifecycle stages, sector applications, coordination models, MEL frameworks, transition guides, implementation patterns, and known risks. The LLM drafts and maintains this layer entirely. 13 numbered sections, each with a `00_*-index.md` entry point:

| # | Section | What it contains |
|---|---|---|
| 00 | Overview | Agent contract, operating model, knowledge map |
| 01 | Sources | Extracted evidence pages + raw inventory |
| 02 | Concepts | 25 concept pages (area-based approach, urban resilience, neighbourhood concept, risk calculation, and more) |
| 03 | Frameworks | 9 Tier 1 operational frameworks + 32 Tier 2 reference frameworks |
| 04 | Tools | 17 step-by-step operational tools |
| 05 | Field instruments | 18 data collection instruments (KII guides, forms, matrices, checklists) |
| 06 | Lifecycle | 9-stage programme cycle with minimum outputs at each gate |
| 07 | Sector applications | 21 sector pages (WASH, shelter, livelihoods, protection, health, DRR, and more) |
| 08 | Coordination | 19 pages: ABC modality, actor mapping, duplication detection, referral pathways |
| 09 | Monitoring & learning | 11 MEL and adaptive management pages |
| 10 | Transition & scale | 8 handover and scale-up pages |
| 11 | Patterns | Validated implementation patterns (empty — threshold not yet met) |
| 12 | Risks & contradictions | 13 risk registers, misuse patterns, known contradictions, stale guidance |

**The schema** — `AGENTS.md` + `governance/`
The operating rules that make the LLM a disciplined wiki maintainer rather than a generic chatbot. `AGENTS.md` at the vault root is the single most important file — every agent reads it first. `governance/aba/CLAUDE.md` holds ABA-specific operating rules. `governance/schema/frontmatter-schema.md` defines the required fields and controlled vocabulary for each page type. `governance/schema/changelog.md` logs every schema change. The schema evolves as the wiki matures — every change is versioned.

---

## Promotion gates

Knowledge earns its place in each layer through explicit promotion gates. The LLM proposes; the human approves.

| Promotion | Requirement |
|---|---|
| Finding → concept page | Appears in ≥2 independent extracted sources |
| Concept → Tier 1 framework | Defined decision logic + explicit use conditions |
| Tier 1 framework → linked tool | Field-applicable scoring criteria + known failure modes |
| Tool → `validated` status | All `field_instruments` linked + `data_quality_checks: true` |

**Source independence rule:** Two documents citing the same underlying evaluation are not independent. Distinct evidence bases are required before a promotion is flagged for human review.

---

## Contradictions as first-class objects

Every page type carries a required `contradicts:` frontmatter field. Every concept page additionally requires a `known_tensions:` frontmatter field and a `## Known Tensions` body section. These are not footnotes — they are structural. The lint check treats a missing `contradicts:` field as a CRITICAL failure.

A contradiction reviewed and classified is more valuable than a clean page that silently ignores a disagreement. The wiki would grow more dangerous the richer it became if it didn't track its own limits.

---

## Operations

**Ingest.** You add a new source PDF to `wiki/aba/01-sources/raw/` and ask the LLM to process it. The flow:
1. Store raw PDF (immutable evidence floor)
2. Generate/update markdown extract in `raw-content/` (page-level text mirror)
3. Create extracted source page with all required frontmatter — `contradicts:` explicitly set
4. Run `scripts/sync_extracted_frontmatter_to_raw_content.py --apply` to copy agreed metadata fields to raw-content
5. Update affected concept, framework, and tool pages — add cross-links and wikilinks
6. Append to `memory/runtime/logs/log.md` using format `## [YYYY-MM-DD] ingest | Source title`
7. Run `scripts/build-index.py` to regenerate `indexes/agent-index.md`
8. Human reviews extracted page and any flagged contradictions
9. Human approves or rejects promotion proposals

A single source typically touches 10–20 wiki pages. Ingesting one at a time and staying involved is recommended — read the extracted page, check the concept updates, guide the LLM on what to emphasize. Batch ingestion is possible but loses the collaborative synthesis that makes the wiki richer.

**Query.** Ask questions against the wiki. The LLM runs a frontmatter query against `indexes/agent-index.md` to identify relevant pages, reads only those 3–5, and synthesizes an answer with `source_id` citations. Answers can be filed back into `wiki/aba/outputs/internal/` as `type: synthesis` pages — a comparison you asked for, a connection you discovered, an analysis you needed. This way explorations compound in the knowledge base just like ingested sources do.

**Lint.** Weekly. The LLM health-checks the wiki and files a report to `wiki/aba/outputs/internal/lint-report-YYYY-MM-DD.md`. At the start of the next session, compliance items are cleared before new work begins.

Critical lint checks (CRITICAL — fix before any new work):
- Missing required frontmatter fields — retrieval blackhole
- `contradicts:` absent on any source, tool, framework, or concept page
- `field_instruments: []` on any tool with `status: validated`
- `governance/schema/changelog.md` not updated since last schema change

High-priority checks (HIGH — clear within the session):
- `data_quality_checks: false` on any validated field instrument
- `source_count < 2` on any Tier 1 concept page
- Unresolved contradictions older than 30 days
- Orphan pages with no inbound wikilinks

---

## Frontmatter-first query architecture

The agent's primary navigation mechanism is **frontmatter queries, not wikilink traversal**. Frontmatter is structured data — parse all frontmatter blocks to find relevant pages, then read only those 3–5. Token cost stays proportional to question complexity regardless of corpus size.

Example queries the architecture supports:

```
# All tools that apply to joint prioritization
type == "tool" AND lifecycle_stage contains "joint-prioritization"

# Sources that contradict a specific concept page
type == "source" AND contradicts contains "concept-urban-resilience"

# Concepts with low source count and contested maturity
type == "concept" AND maturity == "contested" AND source_count <= 2

# Field instruments that can export to KoboToolbox
type == "field-instrument" AND can_export_to contains "kobo"

# Tools with no linked field instruments
type == "tool" AND field_instruments == []
```

Wikilinks are maintained in page bodies for Obsidian's graph view and human browsing — a different navigation contract for a different consumer. The agent does not traverse wikilinks at query time.

A page with a missing `lifecycle_stage:` or `contradicts:` field is a **retrieval blackhole**: it will not surface in agent queries for that category, silently, with no error.

---

## Controlled vocabulary

Frontmatter uses controlled vocabulary slugs for machine-readable queries.

**`lifecycle_stage`** — the 9 ABA programme stages:
`appropriateness-decision` · `area-selection` · `neighbourhood-diagnosis` · `joint-prioritization` · `coordination-design` · `integrated-area-strategy` · `implementation-adaptation` · `monitoring-learning` · `transition-handover`

**`maturity`** (concepts): `emerging` · `established` · `contested`

**`format`** (field instruments): `form` · `checklist` · `guide` · `matrix` · `survey` · `dashboard`

**`can_export_to`** (field instruments): `markdown` · `excel` · `kobo` · `word` · `pdf`

**`confidence`** (sources): `high` · `medium` · `low`

**`status`** (editorial): `draft` · `active` · `ingested` · `validated` · `archived` · `superseded` · `reference`

---

## Indexing and logging

**`indexes/agent-index.md`** is content-oriented. Generated by `scripts/build-index.py` from all page frontmatter — not hand-curated. Organized by page type (sources, concepts, frameworks, tools, field instruments), each entry showing file path, title, `lifecycle_stage`, `status`, and key metadata. The agent reads this first on any query to identify relevant pages, then drills into those pages. Regenerated automatically as the final step of every ingest. Currently covers 123 pages across 5 types.

**`memory/runtime/logs/log.md`** is chronological — an append-only record of what happened and when: ingests, queries, lint passes, schema changes. Each entry starts with `## [YYYY-MM-DD] type | description`, making the log grep-parseable. The log gives a timeline of the wiki's evolution and helps agents understand what's been done recently.

**`memory/current-handoff.md`** carries session-to-session continuity. Filled at the close of every session: what was done, governance decisions made, open items requiring human action, and next session priorities. Read at the start of every session before any other work.

---

## Tooling

**`scripts/build-index.py`** — parses all frontmatter and emits `indexes/agent-index.md`. Runs after every ingest. Standard library only; no external dependencies.

**`scripts/sync_extracted_frontmatter_to_raw_content.py`** — copies agreed metadata fields from `wiki/aba/01-sources/extracted/*.md` to matching `wiki/aba/01-sources/raw-content/*.raw-extract.md`. Matching strategy: `canonical_file` path (fallback to `source_id`). Dry-run by default; explicit `--apply` required for writes.

**`obsidian-local-rest-api` plugin** — HTTPS REST API at `localhost:27124`. Enables automation scripts and n8n ingest pipelines to read/write vault files outside of an active Claude Code session. Claude Code accesses the vault directly via the filesystem during active sessions; the REST API serves automated workflows that run between sessions.

**Obsidian Dataview plugin** — runs queries over page frontmatter for human navigation. The same structured frontmatter that powers agent queries also powers Dataview tables: tools by lifecycle stage, concepts by maturity, sources by confidence rating, instruments by export capability.

**Obsidian graph view** — the best way to see the shape of the wiki: what's connected to what, which pages are hubs, which are orphans. Wikilinks in page bodies are maintained specifically so the graph view stays meaningful for human navigation.

---

## Tips specific to this wiki

- **Obsidian Web Clipper** converts web articles about urban DRR, humanitarian coordination, and ABA practice to markdown for fast ingest into raw sources.
- **Source_id convention**: the canonical source_id equals the raw PDF filename without extension, with underscores converted to hyphens — e.g. `2017-sanderson-sitko-urban-area-based-approaches-post-disaster-guide`. All extracted pages, tools, frameworks, and concepts reference sources by this slug. Never invent a slug; derive it from the filename.
- **The `contradicts:` field is not optional.** An empty array `[]` means "checked and clear." A missing field means "nobody checked." The lint run enforces this distinction.
- **Superseded frameworks keep their pages.** When a framework is replaced by newer guidance, mark it `status: superseded` and add `superseded_by:`. The evidence chain must remain traceable even when guidance is retired.
- **The wiki is a git repo.** Every session ends with a commit. You get version history, the ability to diff what changed across a session, and a full audit trail of how the synthesis evolved.
- **Scale threshold**: when the corpus exceeds ~80 sources or ~200 pages, a local search engine (e.g. `qmd` with BM25/vector hybrid) will be needed to supplement the index file. This upgrade is schema-defined and logged in `governance/schema/changelog.md` when the threshold is crossed.

---

## Why this works

The tedious part of maintaining a humanitarian knowledge base is not the reading or the thinking — it's the bookkeeping. Updating cross-references, keeping concept summaries current when new evidence arrives, noting when a 2013 World Bank framework has been partly superseded by 2026 IASC guidance, maintaining consistency across dozens of pages. Teams abandon wikis because the maintenance burden grows faster than the value. LLMs don't get bored, don't forget to update a cross-reference, and can touch 15 files in one pass. The wiki stays maintained because the cost of maintenance is near zero.

The human's job is to curate sources, direct the analysis, validate what the LLM proposes, resolve contradictions the LLM can't resolve alone, and make the actual programme decisions. The LLM's job is everything else.

The idea is related in spirit to Vannevar Bush's Memex (1945) — a personal, curated knowledge store with associative trails between documents. Bush's vision was closer to this than to what the web became: private, actively curated, with the connections between documents as valuable as the documents themselves. The part he couldn't solve was who does the maintenance. The LLM handles that.

In the humanitarian sector specifically, this matters because the cost of rediscovery is measured in programme quality and sometimes in lives. Thirty years of field practice on neighbourhood-level coordination, boundary legitimacy, participatory design, and handover have produced hard-won lessons that exist in scattered PDFs read by people who left the sector. This wiki is an attempt to make those lessons findable, synthesized, and current — so the next practitioner starts where the last one left off.

---

## The human's role

- **Curate** — source the right documents; decide what enters the corpus
- **Validate** — approve promotions, review extracted pages, resolve contradictions that require human judgment
- **Ask** — direct analysis, ask operational questions, make actual decisions
- **Evolve the schema** — as the wiki matures, the schema evolves; log every change in `governance/schema/changelog.md`

The LLM's job is everything else. Quality-affecting decisions require human judgment. Everything else is automated.
