---
type: audit-catalog
scope: wiki-master
status: validated
updated: 2026-05-08
title: Wiki Index
sources: ['wiki/index.md']
tags: ['wiki', 'index', 'governance']
---

# Wiki Index

**Audit use only.** Agents doing work navigate via section index files (named `00_*-index.md`). Use this file during ingest (to register new pages) and vault-maintenance (to check for orphans and staleness).

After every ingest: add new pages, update summaries that changed. After every lint: mark stale pages.

---

## Knowledge Base (`memory/categories/`)

| Page | Summary |
|------|---------|
| [[../memory/categories/infrastructure]] | Servers, IPs, Docker networks, VPS config, SSH access |
| [[../memory/categories/decisions]] | Architectural and product decisions with rationale |
| [[../memory/categories/procedures]] | Verified step-by-step technical guides |
| [[../memory/categories/outcomes]] | Lessons learned and post-task retrospectives |
| [[../memory/categories/unresolved]] | Open questions, contradictions, documentation gaps |

---

## Operations (`governance/workflows/`)

Use [[../indexes/workflows]] if you need a workflow router before selecting a specific runbook.

| Page | Summary |
|------|---------|
| [[../governance/workflows/ingest]] | Add a source document and update the wiki |
| [[../governance/workflows/query]] | Answer a question from the wiki with citations |
| [[../governance/workflows/lint]] | Health-check the wiki for stale pages and contradictions |
| [[../governance/workflows/vault-initialization]] | Load vault context at session start |
| [[../governance/workflows/vault-maintenance]] | Keep the vault healthy and self-improving |
| [[../governance/workflows/model-routing]] | Select the right model/mode for a task |
| [[../governance/workflows/coding-tasks]] | Write, edit, debug, or refactor code |
| [[../governance/workflows/document-extraction]] | Extract content from PDFs, images, spreadsheets |
| [[../governance/workflows/odoo-accounting]] | Odoo tasks, accounting reports, chart of accounts |
| [[../governance/workflows/memory-recall]] | Recall previous decisions, facts, or session history |

---

## Tools (`tools/`)

| Page | Summary |
|------|---------|
| [[../tools/hermes]] | Hermes tool capabilities and configuration reference |
| [[../tools/openclaw]] | OpenClaw tool capabilities and configuration reference |
| [[../tools/obsidian]] | Obsidian — markdown wiki and vault management |
| [[../tools/openrouter]] | OpenRouter — model API routing and cost management |
| [[../tools/tailscale]] | Tailscale — zero-config VPN for remote access |
| [[../tools/n8n]] | n8n — workflow automation and webhook orchestration |

---

## Prompts (`prompts/`)

| Page | Summary |
|------|---------|
| [[../prompts/cheap-summary]] | Cheap-mode prompt for summaries and simple lookups |
| [[../prompts/fix-code]] | Fix-mode prompt for small code patches and one-liners |
| [[../prompts/code-debug]] | Code-mode prompt for debugging and implementation |
| [[../prompts/plan-architecture]] | Plan-mode prompt for architecture and complex reasoning |
| [[../prompts/review-output]] | Review prompt for validating agent output |
| [[../prompts/memory-write-review]] | Review prompt before writing to memory |

---

## Governance (`governance/`)

| Page | Summary |
|------|---------|
| [[../governance/00_governance-index]] | Governance entry point — routes to all sub-sections |
| [[../governance/compliance-rules]] | The 10 non-negotiable vault governance rules — canonical reference |
| [[../governance/workflows/lint-plan]] | Self-contained lint routine: checks, output template, log destination |

---

## Diagnosis & Audit (`wiki/diagnosis/`)

| Page | Summary |
|------|---------|
| [[diagnosis/karpathy-vault-quality-diagnosis-2026-05-08]] | 2026-05-08 vault quality diagnosis — findings and action plan |
| [[diagnosis/karpathy-vault-audit-2026-05-09]] | 2026-05-09 first-pass audit — issues found and remediation backlog |

---

## Urban DRR + ABA Knowledge Wiki (`wiki/aba/`)

Standard humanitarian knowledge management evaporates with staff turnover. After thirty years of urban crisis response, the field has produced hundreds of frameworks, tools, and field guides — but most teams still rediscover the same lessons independently because there is no place where that knowledge compounds. This wiki is the answer to that problem.

Instead of retrieving from raw documents at query time and re-deriving the same synthesis on every question, the LLM incrementally builds and maintains a persistent structured wiki that sits between the raw source literature and the operational team. When a new guidance document arrives, the LLM reads it, creates a structured extraction page, and integrates the findings into the existing wiki — updating concept pages, noting where the new evidence reinforces or challenges existing frameworks, flagging contradictions. A practitioner arriving on day one has access to everything learned from every source ever read, already synthesized, already cross-referenced, already contextualized to their decision. **The wiki is a persistent, compounding operational memory. The synthesis is already done.**

The wiki is built in five layers: (1) **raw sources** — immutable PDFs, the evidence floor the LLM reads but never modifies; (2) **raw-content mirror** — markdown text extracts of those PDFs for fast agent reading during ingestion workflows; (3) **extracted sources** — one structured synthesis page per document, with a required `contradicts:` field; (4) **the wiki** — concepts, frameworks, tools, instruments, coordination models, and lifecycle guides compiled from those extractions; (5) **the schema** — the frontmatter rules, promotion gates, and quality thresholds that govern how knowledge earns its place in each layer. The LLM drafts and maintains layers 2–4 entirely. The human curates sources, validates promotions, resolves contradictions, and makes decisions.

Agents navigate primarily via **frontmatter queries, not wikilink traversal**. `scripts/build-index.py` parses all frontmatter and generates `indexes/agent-index.md` — a structured index organized by type and tier. The agent identifies relevant pages from the index, then reads only those 3–5. Token cost stays proportional to question complexity regardless of corpus size. Wikilinks are maintained in page bodies for Obsidian's graph view and human browsing — two navigation contracts for two different consumers. A page with a missing required frontmatter field is a **retrieval blackhole**: it will not surface in agent queries for that category, silently, with no error.

The 13 numbered sections below are the layers of that compiled knowledge, ordered from raw input to actionable output. Navigate via the quick-reference table; read the descriptions to understand how the sections work together.

### Quick reference

| # | Section | Index |
|---|---|---|
| 00 | Overview | [[aba/00-overview/00_overview-index]] |
| 01 | Sources — extracted | [[aba/01-sources/extracted/00_extracted-index]] |
| 01 | Sources — raw | [[aba/01-sources/raw/00_raw-index]] |
| 02 | Concepts | [[aba/02-concepts/00_concepts-index]] |
| 03 | Frameworks | [[aba/03-frameworks/00_frameworks-index]] |
| 04 | Tools | [[aba/04-tools/00_tools-index]] |
| 05 | Field instruments | [[aba/05-field-instruments/00_instruments-index]] |
| 06 | Lifecycle | [[aba/06-lifecycle/00_lifecycle-index]] |
| 07 | Sector applications | [[aba/07-sector-applications/00_sectors-index]] |
| 08 | Coordination | [[aba/08-coordination/00_coordination-index]] |
| 09 | Monitoring & learning | [[aba/09-monitoring-learning/00_monitoring-index]] |
| 10 | Transition & scale | [[aba/10-transition-scale/00_transition-index]] |
| 11 | Patterns | [[aba/11-patterns/00_patterns-index]] |
| 12 | Risks & contradictions | [[aba/12-risks-contradictions/00_risks-index]] |
| — | Outputs — toolkits | [[aba/outputs/toolkits/00_toolkits-index]] |

### Section descriptions

**00 — Overview** — *the wiki's self-model*
The entry point that tells you what the wiki already knows and how to reach it: agent contract, knowledge map, operating model, and reading guide. `AGENTS.md` at the vault root is the single most important file — every agent reads it at session start before doing anything else. In a compounding system, knowing what has been compiled is as important as the compiled content itself; without this, every agent re-derives structure the wiki has already built.
*Who reads it:* Every agent initializing a session; anyone new to the wiki.
*When:* Read at every session open. Update only when the operating model or section structure changes.

**01 — Sources (extracted + raw)** — *where "compile once" happens*
The ingest layer — three sub-layers working together. The **raw/** folder holds immutable PDFs, the evidence floor the LLM reads during ingest but never modifies. The **raw-content/** folder holds markdown text extracts of those PDFs, generated once for fast agent reading during ingestion review — not the synthesis layer. The **extracted/** folder holds one structured synthesis page per document: key findings, methodology notes, citation metadata, and a required `contradicts:` field listing any existing wiki pages this source challenges. An empty `contradicts: []` is a meaningful assertion — the source was checked and found consistent. A missing `contradicts:` field means nobody checked. All claims in every downstream section trace back to an extracted page; after ingest, agents read extracted pages rather than raw PDFs. After updating extracted frontmatter, run `scripts/sync_extracted_frontmatter_to_raw_content.py --apply` to sync agreed metadata into the raw-content mirror.
*Who reads it:* Ingest agents (to compile); any agent needing evidence grounding or citation metadata.
*When:* Read when verifying a claim or checking source coverage. Update whenever a new document is ingested.

**02 — Concepts** — *the accumulated definitional layer*
25 concept pages recording what the entire source library says about each key term — with maturity ratings (`emerging` / `established` / `contested`), source counts, convergence scores, and operationalizability notes. A concept page is created only when a finding appears in ≥2 independent extracted sources; source independence is enforced — two documents citing the same underlying evaluation are not independent. Each concept page carries both a `known_tensions:` frontmatter field (for agent queries) and a `## Known Tensions` body section (for human reading) — both required when tensions exist. The tensions section records where sources genuinely disagree; those disagreements are named and preserved, not resolved artificially. Without this layer, every query about "urban resilience" or "area-based approach" would require re-reading multiple documents to assemble a definition — work the wiki has already done, and keeps current each time a new source is ingested.
*Who reads it:* Any agent or person needing to use a contested term confidently across the full source base.
*When:* Read when a question turns on a definition. Update whenever a new source adds a definition or materially shifts an existing tension.

**03 — Frameworks** — *the structured decision logic layer*
9 Tier 1 operational frameworks and 32 Tier 2 reference frameworks compiled from the concepts layer. **Tier 1** frameworks directly answer field team decisions — each requires ≥2 independent extracted sources, explicit decision logic, defined use conditions, linked field instruments, and documented failure modes. **Tier 2** frameworks summarize the wider DRR and urban resilience literature and inform Tier 1 pages, but are not operational decision tools (no field instrument requirement). Superseded frameworks retain their pages — the evidence chain must remain traceable even when guidance is replaced. Frameworks are what you get when concept-level knowledge is organized into decision logic, covering the full programme arc from appropriateness decision to handover. Rather than re-deriving "how to think about area selection," the answer is already compiled here.
*Who reads it:* Programme designers, technical advisors, tool developers.
*When:* Read before designing or selecting a tool. Update when a new source introduces a framework or a Tier 2 framework accumulates enough field evidence for Tier 1 promotion.

**04 — Tools** — *the actionable layer*
17 operational tools that translate Tier 1 frameworks into field-ready decision procedures — covering the full programme cycle from ABA feasibility through handover. A framework tells you how to think; a tool tells you what to do. Each tool specifies evidence required, collection method, respondents, linked field instruments, analysis steps, scoring threshold, and quality checks — so field teams don't design assessment procedures from scratch. A tool reaches `validated` status only when all `field_instruments` are linked and `data_quality_checks: true` — both conditions are enforced by the weekly lint run. The required `contradicts:` field names any conflicts with other tools or frameworks explicitly, rather than leaving them for the practitioner to discover in the field.
*Who reads it:* Field coordinators, assessment leads, programme managers during assessment and design.
*When:* Read before a field assessment or design session. Update when field use reveals evidence gaps or a new instrument is linked.

**05 — Field instruments** — *the collection layer*
18 data collection instruments — KII guides, observation forms, mapping sheets, household mini-survey, HEVC matrix, stakeholder mapping form, resource inventory, duplication/gap matrix, checklists, and templates — each pre-specifying what to collect, from whom, quality checks, and how results feed back into the tool's analysis. Instruments carry a `can_export_to` field (`kobo`, `excel`, `markdown`, `word`, `pdf`) enabling queries like "which instruments can export to KoboToolbox" — a question that matters for field digitization planning. A single instrument may feed multiple tools. `data_quality_checks: true` is a required lint condition on any validated instrument; an instrument without explicitly defined quality checks is not ready for field use.
*Who reads it:* Field enumerators, assessment leads, data managers.
*When:* Use during data collection. Update when quality checks reveal systematic gaps.

**06 — Lifecycle** — *the sequencing layer*
11 pages mapping the 9-stage ABA programme cycle using the controlled vocabulary slugs that appear in frontmatter across all page types: `appropriateness-decision` → `area-selection` → `neighbourhood-diagnosis` → `joint-prioritization` → `coordination-design` → `integrated-area-strategy` → `implementation-adaptation` → `monitoring-learning` → `transition-handover`. The `lifecycle_stage:` field is the primary frontmatter query axis — a tool, instrument, or framework with a missing field is a retrieval blackhole. This section defines the minimum outputs required before advancing past each gate, maps the tools and instruments serving each stage, and flags known failure modes at each transition.
*Who reads it:* Programme managers and coordinators sequencing work across a full programme cycle.
*When:* Read at each stage transition. Update when a tool is added or a stage's minimum outputs are revised.

**07 — Sector applications** — *the translation layer*
21 sector-specific pages — WASH, shelter, livelihoods, protection, health, education, DRR, urban governance, and more — showing how the generic ABA programme logic maps onto each sector's technical requirements. The compiled logic in sections 02–06 is intentionally sector-agnostic; this layer translates it into sector-specific terms so that sector design doesn't get imported wholesale from a sector silo that ignores area-level dynamics. Currently stubs, to be populated as sector evidence is extracted from sources.
*Who reads it:* Sector technical advisors and cluster leads working within an ABA programme.
*When:* Read during sector design (stages 5–6). Populate stubs as sector evidence accumulates.

**08 — Coordination** — *the multi-actor protocol layer*
19 pages covering coordination architecture, the IASC 2026 area-based coordination (ABC) ToR, actor and responsibility mapping, duplication detection, gap analysis, cluster/area interface, municipal engagement, information management, referral pathways, and decision and meeting templates. This is where the compiled programme logic meets the reality of multiple actors operating in the same area. The IASC 2026 ABC ToR is the authoritative operational definition anchoring this section — so coordination leads don't reinvent that logic for each response. `contradicts:` fields across these pages track where field practice has diverged from or challenged the ToR.
*Who reads it:* Area coordination leads, information managers, cluster liaisons, municipal counterparts.
*When:* Read when establishing or reviewing a coordination platform (stages 5–8). Update when the IASC ToR changes or field experience reveals protocol gaps.

**09 — Monitoring & learning** — *the feedback layer*
11 pages covering the ABA MEL framework, area-level outcome monitoring, resilience indicators, adaptive management triggers, participation quality monitoring, Sendai reporting, outcome harvesting, and learning documentation. This section is where field observations feed back into the system — updating what the wiki knows about what works, which indicators are valid, and where programmes need to adapt. It closes the compounding loop: the wiki doesn't just inform field decisions, it is updated by what field decisions produce. Also links ABA outcomes to Sendai Framework municipal reporting so that obligation isn't reconstructed each cycle.
*Who reads it:* MEL officers, programme managers, adaptive management leads, municipal DRR reporting officers.
*When:* Read during MEL design and at each reassessment cycle. Update when new indicators are validated or reporting requirements change.

**10 — Transition & scale** — *the closure and replication layer*
8 pages covering handover planning, readiness checklist, exit strategy, municipal integration, build-back-better alignment, replication logic, and scale-up frameworks. Handover failure is one of the best-documented risks in ABA programmes — this section compiles what responsible closure looks like: identified responsible actors, maintenance budgets, explicitly transferred risks, and a transition that doesn't undermine local capacity. The replication pages compile what's needed to take a pilot to a second context, so that knowledge isn't rediscovered from scratch. After each completed handover, lessons integrate back here — the checklist and criteria improve with each programme.
*Who reads it:* Programme managers, transition leads, municipal counterparts, donors.
*When:* Read from stage 7 onwards. Update after each completed handover.

**11 — Patterns** — *the distilled wisdom layer*
A repository for validated implementation patterns — recurring solutions to recurring problems, compiled from ≥2 independent field case studies. A pattern is the highest-confidence form of accumulated knowledge in the wiki: it has survived in multiple independent contexts. The same source independence rule that governs concept promotion applies here — two case studies citing the same underlying evaluation are not independent. The bar is intentionally high. Currently empty; it will grow as the source library expands and case study evidence can be synthesized across contexts.
*Who reads it:* Programme designers, technical advisors, agents synthesizing case study evidence.
*When:* Read at design stage. File a new pattern only when the same solution has worked in at least two independent contexts, with evidence base, conditions of applicability, and failure modes documented.

**12 — Risks & contradictions** — *the critical lens layer*
13 pages cataloguing known risks, common misuse patterns, contradictions in the source literature, weak evidence claims, stale guidance, unresolved questions, and evidence gaps. Every compounding knowledge base needs a layer that tracks its own limits. `contradicts:` is a required field on every page in the wiki — not optional, not a footnote. Unresolved contradictions older than 30 days trigger a HIGH-priority lint flag. A contradiction reviewed and classified is more valuable than a clean page that silently ignores a disagreement. Without this section, the wiki would confidently propagate weak or contradicted claims — and grow more dangerous the richer it became.
*Who reads it:* Quality reviewers, protection advisors, programme designers, evaluators — anyone generating an external-facing output.
*When:* Read at design review and before any external output. Update when a new contradiction surfaces, a risk materializes, or a previously unresolved question is settled.

---

## How to Use This Index

- **On query:** Scan the table headers to find the relevant section, then open the 1-3 most relevant pages.
- **On ingest:** After updating wiki pages, add any new rows here and update summaries that changed.
- **On lint:** Pages marked `stale` in their frontmatter should be flagged in the summary column: `⚠️ stale`.

*This file does not catalog `sources/` — raw documents are not wiki pages.*
