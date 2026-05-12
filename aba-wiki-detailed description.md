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

Standard humanitarian knowledge management looks like this: a practitioner searches a document library, finds a relevant guide, reads it, and applies their judgment. The next practitioner does the same thing from scratch. Institutional memory does not accumulate — it evaporates with staff turnover. After decades of urban crisis response, the field has produced hundreds of frameworks, tools, and field guides, but most teams still rediscover the same lessons independently.

This design is different. Instead of searching a document library at decision time, the LLM incrementally builds and maintains a **structured wiki** — an interlinked collection of synthesis pages that sits between the raw source literature and the operational team.

When a new guidance document arrives, the LLM does not just index it for retrieval. It:

1. Reads it and creates a **structured extracted source page**.  
2. Integrates the findings into the existing wiki:
   - Updating concept pages.  
   - Noting where the new evidence reinforces or challenges existing frameworks and tools.  
   - Flagging contradictions that field teams need to review.  

The knowledge compounds. A practitioner arriving on day one has access to everything learned from every source ever read, already synthesized, already cross‑referenced, already contextualized to their decision.

**Key difference**: the wiki is a **persistent, compounding operational memory**.

- The synthesis is already done.  
- The contradictions are already flagged.  
- The decision logic is already traced back to its evidence base.  

The LLM drafts and maintains all of it. The human validates what matters.

---

## Architecture Overview

The system follows the layered architecture shown in the “LLM → Wiki → Outputs” graphic:

1. **Layer 4 – Raw sources**  
2. **Layer 3 – Extracted sources**  
3. **Layer 2 – The Wiki (concepts, frameworks, tools, instruments, lifecycle)**  
4. **Layer 1 – Outputs (decision memos, slide decks, field guides)**  
5. **Cross‑cutting layers**: LLM role, human governance checkpoints, navigation/query layer.

### Layer 4 — Raw Sources (Evidence Floor)

- Curated literature base: PDFs of IASC guidance, IFRC frameworks, academic studies, evaluation reports, UN policy documents, NGO guidance, etc.  
- Stored under something like `wiki/aba/01-sources/raw/`.  
- **Immutable**: the LLM reads from them during ingest but never modifies them.  
- This is the **evidence floor**.

### Raw-Content Mirror (Operational Convenience Layer)

- Markdown text extracts generated from raw PDFs and stored in `wiki/aba/01-sources/raw-content/`.  
- Preserve page‑level source text in `.md` format for fast local reading and agent tooling.  
- Not the synthesis layer and do not replace extracted source pages.  
- Frontmatter is synced from extracted source pages using:

```bash
scripts/sync_extracted_frontmatter_to_raw_content.py --apply
```

- Matching strategy: use `canonical_file` first, with `source_id` as fallback.  
- The script runs in dry‑run mode by default; `--apply` is required to write.

### Layer 3 — Extracted Sources

- One **LLM-generated structured page per document**.  
- Contains:
  - Key findings  
  - Methodology notes  
  - Source citations and dependencies  
  - A required `contradicts:` field listing any existing wiki pages this source challenges  

The `contradicts:` field is **required on every extracted source page**:

- An empty array `[]` is a meaningful assertion: the source was checked and found consistent.  
- A missing `contradicts:` field means nobody checked — lint treats this as a critical failure.  

This layer makes the corpus scalable: the LLM reads extracted pages rather than raw PDFs for subsequent queries and synthesis.

### Layer 2 — The Wiki (Synthesis Layer)

The **wiki** is the structured synthesis layer — an interconnected knowledge graph (Obsidian-style) with nodes for:

- Concepts  
- Decision frameworks (Tier 1 and Tier 2)  
- Operational tools  
- Field instruments  
- Lifecycle stages  
- Coordination models  
- Patterns (once validated)  
- Known risks and contradictions  

The LLM drafts and maintains this layer, but promotions and critical status changes require human approval (see Governance).

Every concept page has:

- A `known_tensions:` field in frontmatter, and  
- A `## Known Tensions` body section.  

Contradictions are **first-class objects**, not footnotes. They are:

- Required in `contradicts:` fields on extracted, concept, framework, and tool pages.  
- Tracked and escalated when unresolved for more than 30 days.  
- Preserved as tensions unless a human explicitly supersedes or invalidates them.

### Layer 1 — Outputs

Top layer: curated, purpose-built materials for field use, such as:

- Decision memos  
- Slide decks  
- Field guides  
- Proposal sections, training materials, internal analyses  

Outputs draw **only from the wiki and extracted sources**, never directly from raw PDFs. They are downstream products and not the canonical data store.

---

## The Schema Layer

The schema is captured in:

- `AGENTS.md` at the vault root  
- A library of operational prompts and governance docs  

These define:

- Frontmatter schemas  
- Promotion gates  
- Quality thresholds  
- Agent roles and responsibilities  

**AGENTS.md is the single most important file** — every agent reads it first.

---

## Query Architecture: Frontmatter-First, Wikilink-Second

The agent’s primary navigation mechanism is **frontmatter queries**, not wikilink traversal.

- Frontmatter is structured data.  
- A Python script can query it in milliseconds without reading page bodies.  
- Token usage stays low: parse all frontmatter blocks, then read only the 3–5 relevant pages.

### Example Query Model

```text
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

### Dual-Layer Navigation Contract

| Layer      | Consumer | Purpose                                             |
|-----------|----------|-----------------------------------------------------|
| Frontmatter | Agents / scripts | Machine-readable, fast, structured retrieval      |
| Wikilinks | Humans   | Graph view, browsing, and sense‑making in Obsidian |

- Wikilinks are maintained in page bodies for Obsidian graph view and human navigation.  
- The agent **does not** traverse wikilinks at query time; it:
  1. Runs frontmatter queries (often via an index).  
  2. Reads only the resulting pages.

---

## Frontmatter Schema

**Frontmatter completeness is the highest-priority compliance requirement.**

A page with a missing `lifecycle_stage:` or `contradicts:` field is a **retrieval blackhole**:

- It will not surface in frontmatter-based queries for that category.  
- This failure is silent — no error, just missing content.  

The lint system treats missing required fields as **CRITICAL**.

### Source Page

One page per raw document. Created during ingest. Updated on review.

```yaml
***
type: source
source_id:           # canonical-filename-without-ext — e.g. 2017-sanderson-sitko-urban-aba-guide
title:               # full document title
author:              # "Name1; Name2"
institution:         # e.g. "World Vision / Stronger Cities Consortium (published by IIED)"
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
confidence:          # high | medium | low — quality of evidence (not model confidence)
review_cycle:        # annual | biennial | as-needed
last_reviewed:       # YYYY-MM-DD
next_review:         # YYYY-MM-DD

lifecycle_stage:     # list — from controlled vocabulary
primary_topics:      # list — controlled topic terms for agent queries
tags:                # list — free-form Obsidian tags for graph navigation

contradicts:         # [] or list of wiki page slugs — REQUIRED, empty array if checked and clear
wiki_pages:          # list of wiki pages updated during ingest
notes:               # 1–2 sentence summary of relevance and key claims

created:             # YYYY-MM-DD
updated:             # YYYY-MM-DD
***
```

### Tool Page

One page per operational tool. Tier 1 only. Must have linked field instruments before status reaches `validated`.

```yaml
***
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
***
```

### Field Instrument Page

One page per data collection instrument. An instrument may feed multiple tools.

```yaml
***
type: field-instrument
instrument_id:                 # short-name slug — e.g. household-mini-survey
title:                         # full instrument name
format:                        # form | checklist | guide | matrix | survey | dashboard
can_export_to:                 # list — markdown | excel | kobo | word | pdf

related_tools:                 # list of tool_ids that use this instrument
required_for_decision_domains: # list — decision domains this instrument feeds

lifecycle_stage:               # list — from controlled vocabulary
primary_users:                 # list

data_quality_checks:           # true | false — whether DQ checks are explicitly defined
status:                        # draft | tested | validated

validation_status:             # draft | field_tested | validated_multi_context
field_use_history:             # list of field uses (context, date, adaptations, effectiveness)
last_field_use:                # YYYY-MM-DD
validation_expires:            # YYYY-MM-DD
known_failure_modes:           # list of known limitations

created:                       # YYYY-MM-DD
updated:                       # YYYY-MM-DD
***
```

### Concept Page

One page per operational concept. Promoted from findings once ≥2 **independent** sources confirm.

```yaml
***
type: concept
title:                    # concept name

status:                   # draft | active | archived — editorial state
maturity:                 # emerging | established | contested — epistemic state

source_count:             # N — number of independent supporting sources
related_tools:            # list of tool_ids
related_frameworks:       # list of framework slugs
related_concepts:         # list of concept slugs
related_lifecycle_stages: # list — from controlled vocabulary

known_tensions:           # [] or list of tension slugs — expanded in ## Known Tensions
contradicts:              # [] or list of slugs in direct logical conflict
used_by_outputs:          # [] or list of output slugs

created:                  # YYYY-MM-DD
updated:                  # YYYY-MM-DD
***
```

- `known_tensions:` in frontmatter holds slugs for query purposes.  
- The actual descriptions live in the `## Known Tensions` body section.  
- Both are **required** when tensions exist.

### Framework Page

```yaml
***
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
***
```

- Tier 1 frameworks use `status: active`.  
- Tier 2 frameworks use `status: reference`.  
- A superseded framework retains its page — the evidence chain must remain traceable even when guidance is replaced.

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
status:                 # draft | final

created:                # YYYY-MM-DD
updated:                # YYYY-MM-DD
***
```

---

## Controlled Vocabulary

**Lifecycle stages** — use slugs in frontmatter. These map to nine ABA operational stages:

| Slug                   | Stage                                      |
|------------------------|--------------------------------------------|
| appropriateness-decision | 0. Appropriateness decision               |
| area-selection         | 1. Area selection and boundary definition  |
| neighbourhood-diagnosis| 2. Area profile and systems diagnosis      |
| joint-prioritization   | 3. Joint prioritization                    |
| coordination-design    | 4. Area coordination design                |
| integrated-area-strategy | 5. Integrated area strategy              |
| implementation-adaptation | 6. Implementation and adaptation        |
| monitoring-learning    | 7. Monitoring and learning                 |
| transition-handover    | 8. Transition and handover                |

Other vocabularies:

- `source_type` — `iasc-guidance | ifrc-framework | un-policy | academic | field-evaluation | ngo-guidance | government-policy`  
- `format` (field instruments) — `form | checklist | guide | matrix | survey | dashboard`  
- `can_export_to` — `markdown | excel | kobo | word | pdf`  
- `maturity` — `emerging | established | contested`  
- `confidence` — `high | medium | low`  
- `status` (editorial) — `draft | active | archived | superseded | reference`

---

## Quality Tiers

- **Tier 1 — Operational frameworks**  
  - Directly answer field team decisions.  
  - Require ≥2 **independent** extracted sources, explicit decision logic, defined use conditions, linked field instruments, and documented failure modes.

- **Tier 2 — Reference frameworks**  
  - Summarize the wider DRR and urban resilience literature.  
  - Inform Tier 1 pages but are not operational decision tools.  
  - No field instrument requirement.

---

## Promotion Gates

| Promotion                         | Requirement                                      | Who decides                      |
|----------------------------------|--------------------------------------------------|----------------------------------|
| Finding → concept page           | Appears in ≥2 independent extracted sources      | LLM proposes, human approves     |
| Concept → Tier 1 framework       | Defined decision logic + explicit use conditions | Human approves                   |
| Tier 1 → linked tool/instrument  | Field-applicable scoring + known failure modes   | Human approves                   |
| Tool → validated status          | All `field_instruments` linked + `data_quality_checks: true` and instruments validated/current | Human approves |

**Source independence rule**:  
Two documents citing the same underlying evaluation are **not independent**. The LLM must verify distinct evidence bases (using `source_dependencies` and `independence_hash`) before flagging a promotion for human review.

---

## Contradictions as First-Class Objects

- Every **extracted source** page carries a required `contradicts:` field.  
- Every **concept** page has a required `known_tensions:` field and `## Known Tensions` body section.  
- Every **tool** and **framework** page carries `contradicts:`.  
- Lint hunts for **missing** `contradicts:` fields, not just wrong values.  

Contradictions that cannot be resolved at the evidence level are escalated as promotion-gate decisions and documented with:

```yaml
contradicts:
  - page: frameworks/tier-1/area-selection-criteria
    field: minimum_population_threshold
    nature: "New source suggests 5,000 minimum vs. existing 10,000"
    flagged_date: 2026-05-12
    reviewed_date: 2026-05-18
    status: preserved_tension     # or resolved_supersession | resolved_invalid
    reviewer: eddie_argenal
    resolution_note: "Both thresholds valid—context dependent"
```

A contradiction reviewed and classified is more valuable than a clean page that silently ignores a disagreement.

---

## Navigation and Index Generation

### Agent Index: `scripts/build-index.py`

- Parses all frontmatter and emits `indexes/agent-index.md` — a structured, LLM-readable index organized by type and tier.  
- Each entry shows: file path, title, `lifecycle_stage`, status, `source_count` or `contradicts` count.  
- Runs automatically as the final step of every ingest.  
- Not hand-curated — generated from frontmatter.

The agent:

1. Reads `indexes/agent-index.md` to identify relevant pages.  
2. Reads only those pages.  

Query cost stays proportional to question complexity regardless of corpus size.

### Scale Threshold

When corpus exceeds ~80 sources or ~200 pages, a local search tool (e.g. `qmd` or similar) is required. This upgrade is:

- Schema-defined, and  
- Logged in `governance/schema/changelog.md` when crossed.

### Human Layer: Obsidian

- Dataview queries against the same frontmatter fields serve human navigation.  
- The graph view is only as rich as the wikilinks in page bodies — wikilinks must be maintained even though the agent does not traverse them for retrieval.

---

## Operations

### Ingest Workflow

1. LLM stores raw PDF in `wiki/aba/01-sources/raw/` (immutable evidence floor).  
2. LLM generates/updates markdown raw extract in `wiki/aba/01-sources/raw-content/`.  
3. LLM creates extracted source page with all required frontmatter — `contradicts:` explicitly set.  
4. LLM runs:

   ```bash
   scripts/sync_extracted_frontmatter_to_raw_content.py --apply
   ```

   to copy agreed metadata from extracted pages into matching raw‑content files.

5. LLM updates affected concept, framework, and tool pages — adds cross-links and wikilinks.  
6. LLM appends to `memory/runtime/logs/log.md` using:

   ```text
   ## [YYYY-MM-DD] ingest | Source title
   ```

7. LLM runs `scripts/build-index.py` to regenerate `indexes/agent-index.md`.  
8. Human reviews the extracted page and any flagged contradictions.  
9. Human approves or rejects promotion proposals.

### Query Workflow

1. LLM runs frontmatter query against the agent index.  
2. Reads only relevant pages (extracted + wiki).  
3. Synthesizes answer with `source_id` citations and explicit handling of contradictions.  
4. Answers that reveal new reusable connections are filed as `type: synthesis` under `wiki/aba/outputs/internal/`.

### Lint Workflow

- Runs weekly via cron.  
- Output filed to `wiki/aba/outputs/internal/lint-report-YYYY-MM-DD.md`.  
- Mandatory reading at the start of the next session — the LLM clears the compliance queue before new work.

**Critical lint checks:**

- Missing required frontmatter fields per page type (**CRITICAL — retrieval blackhole**)  
- `contradicts:` field absent on any source, tool, framework, or concept page (**CRITICAL**)  
- `field_instruments: []` on any tool with `status: validated` (**CRITICAL**)  
- `governance/schema/changelog.md` not updated after a schema change (**CRITICAL**)  
- `data_quality_checks: false` on any validated field instrument (**HIGH**)  
- `source_count < 2` on any Tier 1 concept page (**HIGH**)  
- Unresolved `pending_review` contradictions older than 30 days (**HIGH**)  
- Orphan pages with no inbound wikilinks (**MEDIUM**)

---

## The Human’s Role

- **Curate** — source the right documents, decide what enters the corpus.  
- **Validate** — approve promotions, resolve contradictions, evolve the schema.  
- **Decide** — ask operational questions, integrate outputs into real decisions.

The LLM’s job is everything else.  
Quality-affecting decisions require human judgment. Everything else is automated.

---

## API and Tooling

- Local REST API (e.g. via `obsidian-local-rest-api` plugin) enables:
  - `scripts/build-index.py` and lint runner to read/write vault files without an interactive agent session.  
  - External pipelines to create extracted source pages on document arrival.  

- **Raw-content metadata sync script**:  
  `scripts/sync_extracted_frontmatter_to_raw_content.py`  
  - Purpose: copy agreed frontmatter subset from `wiki/aba/01-sources/extracted/*.md` to matching `wiki/aba/01-sources/raw-content/*.md`.  
  - Matching: via `canonical_file` (fallback `source_id`).  
  - Safety: dry-run by default; `--apply` required for writes.

- Agents (e.g. Claude Code) can also access the vault directly via filesystem when running locally.

---

## Governance

- Schema changes logged in `governance/schema/changelog.md` — **unlogged change = critical failure**.  
- `governance/00_governance-index.md` is the authoritative governance reference — routes to all sub-documents.  
- A “librarian” skill (e.g. `.claude/commands/librarian.md`) is injected at every agent session start.  
- Weekly lint cadence — compliance queue clears before new work.

Librarian skill session protocol:

- **Open**:
  - Read `memory/current-handoff.md`  
  - Read lint queue  
  - Clear compliance items  
  - Begin task  

- **Close**:
  - Update `memory/current-handoff.md`  
  - Update `governance/schema/changelog.md` if schema changed  
  - Run lint  
  - Run `scripts/build-index.py`  
  - Append to `memory/runtime/logs/log.md`

---

## Version History

- **Version 2.3 — updated 2026-05-11**  
  Supersedes v2.2. Frontmatter schemas reconciled with actual vault content: region dropped (global lessons, context adaptation deferred); author/institution separated; source maintenance fields added; field instrument parent tool constraint corrected to plural; concept status/maturity distinction clarified; lifecycle_stage vocabulary expanded to 9 stages matching ABA operational model; governance reference updated to `governance/00_index.md`.

- **Version 2.4 — updated 2026-05-12**  
  Supersedes v2.3. All section indexes renamed from generic `00_index.md` to descriptive `00_*index.md` names (e.g. `governance/00_governance-index.md`, `wiki/aba/02-concepts/00_concepts-index.md`). Governance reference updated accordingly. Librarian skill index‑exclusion filter updated to `fname.startswith("00")`.

- **Version 2.5 — updated 2026-05-12**  
  Supersedes v2.4.  
  Added `wiki/aba/01-sources/raw-content/` as an operational markdown mirror of raw PDFs. Documented ingest flow updates for raw-content generation and metadata sync. Added `scripts/sync_extracted_frontmatter_to_raw_content.py` to tooling, including dry‑run/apply behavior and canonical‑file‑first matching with `source_id` fallback.
