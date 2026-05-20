# ABA/DRR Field Knowledge Wiki — Version 2.6 Architecture Description

A pattern for building operational knowledge bases for humanitarian response using LLMs.

---

## The Core Idea

Standard humanitarian knowledge management looks like this: a practitioner searches a document library, finds a relevant guide, reads it, and applies their judgment. The next practitioner does the same thing from scratch. Institutional memory does not accumulate — it evaporates with staff turnover. After decades of urban crisis response, the field has produced hundreds of frameworks, tools, and field guides, but most teams still rediscover the same lessons independently.

This design is different. Instead of searching a document library at decision time, the LLM incrementally builds and maintains a **structured wiki** — an interlinked collection of synthesis pages that sits between the raw source literature and the operational team.

When a new guidance document arrives, the LLM does not just index it for retrieval. It:

1. Reads it and creates a **structured extracted source page**.
2. Identifies reusable findings.
3. Routes those findings into the existing wiki:
   - Updating concept pages.
   - Updating framework, tool, field-instrument, and risk pages.
   - Noting where the new evidence reinforces or challenges existing guidance.
   - Flagging contradictions or tensions that field teams need to review.
4. Rebuilds generated indexes so agents can retrieve the new knowledge efficiently.

The knowledge compounds. A practitioner arriving on day one has access to everything learned from every source ever read, already synthesized, cross-referenced, and contextualized to operational decisions.

**Key difference**: the wiki is a **persistent, compounding operational memory**.

- The synthesis is already done.
- Contradictions and tensions are already flagged.
- Decision logic is traced back to its evidence base.
- Field tools and advisory outputs are grounded in the same knowledge graph.

The LLM drafts and maintains the system. The human validates what matters.

---

## One-Sentence Architecture Definition

The ABA/DRR Field Knowledge Wiki is a **markdown-first, frontmatter-governed, JSONL-indexed, offline-capable, multi-agent technical advisory system** that converts curated humanitarian knowledge into field-ready guidance through deterministic graph retrieval, section-level evidence packets, claim-ledger writing, citation/risk review, and partial-repository deployment for low-connectivity field environments.

---

## Architecture Overview

The system has seven major layers:

```text
Layer 7 — Runtime / Deployment Layer
  Cloud, laptop, edge, offline, partial repo modes

Layer 6 — Advisory Agent Layer
  Orchestrator, section retrieval agents, writing agent, reviewers

Layer 5 — Compiled Index Layer
  JSONL graph indexes, section index, evidence index, manifest

Layer 4 — Wiki Synthesis Layer
  Concepts, frameworks, tools, instruments, risks, playbooks

Layer 3 — Extracted Source Layer
  Source-level findings, evidence, tensions, integration map

Layer 2 — Raw Content Mirror
  Markdown extraction of raw PDFs for local reading/tooling

Layer 1 — Raw Sources
  Immutable evidence floor
```

The core architectural principle is:

> **Markdown/frontmatter is the source of truth. JSONL indexes are compiled artifacts. Agents retrieve section-level evidence packets. Writing agents produce final guidance only from validated claims.**

---

# Layer 1 — Raw Sources: Evidence Floor

Raw sources are the immutable evidence base.

They include:

- PDFs of IASC guidance
- IFRC frameworks
- Academic studies
- Evaluation reports
- UN policy documents
- NGO guidance
- Government policy documents
- Field manuals
- Technical standards
- Assessment reports

Raw sources are stored under a path such as:

```text
wiki/aba/01-sources/raw/
```

Rules:

1. Raw sources are never modified by LLMs.
2. Each curated source receives a source or extracted-source page.
3. Raw sources are used for verification, exact wording, and evidence review.
4. Routine advisory answers should use extracted source pages and wiki synthesis pages first, not raw PDFs.

---

# Layer 2 — Raw-Content Mirror

The raw-content mirror is an operational convenience layer.

It contains markdown text extracts generated from raw PDFs and stored in:

```text
wiki/aba/01-sources/raw-content/
```

Purpose:

- Preserve page-level source text in `.md` format.
- Support fast local reading and tooling.
- Allow agents to inspect source text without opening PDFs.
- Improve offline and edge-device usability.

The raw-content mirror does **not** replace raw PDFs and does **not** serve as the synthesis layer.

Frontmatter can be synced from extracted source pages using:

```bash
scripts/sync_extracted_frontmatter_to_raw_content.py --apply
```

Matching strategy:

1. Use `canonical_file` first.
2. Fall back to `source_id`.

Safety rule:

- The script runs in dry-run mode by default.
- `--apply` is required to write changes.

---

# Layer 3 — Extracted Source Pages

Each curated source gets one structured extracted source page.

Location example:

```text
wiki/aba/01-sources/extracted/
```

An extracted source page is a staging layer between raw evidence and wiki synthesis.

It contains:

- Source metadata
- Key findings
- Methodology notes
- Source citations
- Source dependencies
- Reusable findings
- Known tensions
- Contradictions
- Integration map
- Wiki pages updated or proposed
- Human review queue

The extracted source page is **not** the final knowledge layer. It is the source-level staging page from which findings are routed into concepts, frameworks, tools, risks, instruments, or advisory playbooks.

---

## Finding-Level Integration

Every extracted source page should identify reusable findings.

Each finding should include:

```yaml
finding_id:
finding:
finding_type:
lifecycle_stage:
source_pages:
candidate_target_pages:
integration_action:
status:
human_review_required:
```

Example integration actions:

```yaml
integration_action:
  - reinforce
  - extend
  - qualify
  - contradict
  - add_failure_mode
  - add_use_condition
  - add_tool_step
  - add_instrument_question
  - propose_new_page
  - source_only
```

The operating rule is:

> **Every curated source is important. Every extracted finding must be routed. Not every finding becomes a new page.**

---

## Integration Map

Each extracted source page should include an integration map.

Example:

```markdown
## Integration Map

| Finding ID | Finding | Type | Lifecycle Stage | Candidate Target Page | Integration Action | Status |
|---|---|---|---|---|---|---|
| F-001 | Area selection should combine severity, access, and feasibility | method | area-selection | methods/area-selection.md | extend | integrated |
| F-002 | Local government role is underemphasized | risk | coordination-design | risks/local-governance-gap.md | add_tension | pending_review |
```

This tells the system where source knowledge enters the living wiki.

---

# Layer 4 — Wiki Synthesis Layer

The wiki is the structured synthesis layer.

It contains operational knowledge nodes such as:

- Concepts
- Frameworks
- Tools
- Field instruments
- Lifecycle pages
- Coordination models
- Risks
- Known tensions
- Patterns
- Advisory playbooks
- Decision protocols
- Output templates

The LLM drafts and maintains this layer, but promotions, high-risk changes, and contradiction resolution require human approval.

The wiki is where knowledge compounds.

---

## Core Page Types

Recommended core page types:

| Type | Purpose |
|---|---|
| `concept` | Explains an operational idea |
| `framework` | Structures a decision domain or methodology |
| `tool` | Provides a practical method, matrix, checklist, or workflow |
| `field-instrument` | Supports data collection |
| `risk` | Captures risk, caveat, misuse pattern, or failure mode |
| `source` | Documents one curated source |
| `advisory-playbook` | Guides how agents advise on a recurring field problem |
| `decision-protocol` | Provides conditional logic for operational decisions |
| `output-template` | Structures field-ready outputs |
| `synthesis` | Stores downstream analysis or advisory outputs |

---

# Stable ID Graph Schema

The system does not depend on filenames or folder paths for graph identity.

Every page requires a stable `id`.

Example:

```yaml
id: C-resilience
type: concept
title: Resilience
slug: resilience
retrieval_status: usable
```

## ID Prefixes

| Prefix | Page Type |
|---|---|
| `S-` | Source / extracted source |
| `C-` | Concept |
| `F-` | Framework |
| `T-` | Tool |
| `I-` | Field instrument |
| `R-` | Risk |
| `KTN-` | Known tension |
| `P-` | Advisory playbook |
| `D-` | Decision protocol |
| `O-` | Output template / output |
| `EP-` | Evidence packet |
| `PU-` | Proposed update |

Design rule:

> **Relationships must point to stable IDs, not file paths.**

Good:

```yaml
related_risks:
  - R-checklist-misuse
```

Avoid:

```yaml
related_risks:
  - ../06-risks/checklist-misuse-risk.md
```

---

# Explicit Relationship Arrays

Inline wikilinks remain useful for humans in Obsidian, but machine traversal uses frontmatter arrays.

## Universal relationship fields

```yaml
related_concepts:
related_frameworks:
related_tools:
related_risks:
source_basis:
known_tensions:
contradicts:
used_by_playbooks:
output_templates:
```

## Tool-specific fields

```yaml
requires_concepts:
parent_frameworks:
required_inputs:
compatible_instruments:
mitigated_by:
```

## Risk-specific fields

```yaml
risk_applies_to:
mitigated_by:
escalation_triggers:
```

Example tool page:

```yaml
id: T-resilience-milestone-scale
type: tool
title: Resilience Milestone Scale
retrieval_status: usable

requires_concepts:
  - C-resilience
  - C-community
  - C-disaster-risk-reduction

parent_frameworks:
  - F-community-resilience-characteristics

related_risks:
  - R-false-precision
  - R-checklist-misuse
  - R-participation-tokenism

compatible_instruments:
  - I-community-fgd-guide
  - I-key-informant-interview-guide

source_basis:
  - source_id: S-2007-twigg-disaster-resilient-community
    finding_ids:
      - F-010
      - F-011
    pages:
      - 15
```

---

# Section-Level Addressability

Large pages must be readable by section, not only as whole files.

Each important section is declared in frontmatter:

```yaml
sections:
  - id: definition
    anchor: "#definition"
    purpose: "Operational definition"
  - id: field-use
    anchor: "#field-use"
    purpose: "How field teams apply this"
  - id: risks
    anchor: "#risks"
    purpose: "Risks and safeguards"
```

The body should use matching anchors:

```markdown
<a id="definition"></a>

## Definition

<a id="field-use"></a>

## Field Use

<a id="risks"></a>

## Risks
```

This allows agents to request:

```text
C-resilience#field-use
```

instead of reading the full concept page.

---

# Layer 5 — Compiled JSONL Index Layer

The index layer is generated from markdown/frontmatter.

Indexes are **compiled artifacts**, not editable knowledge.

Agents and humans edit markdown. A build process compiles the graph into deterministic `.jsonl` indexes.

Generated indexes:

```text
indexes/current/
  manifest.json
  agent-index.jsonl
  graph-edges.jsonl
  unresolved-edges.jsonl
  section-index.jsonl
  source-evidence-index.jsonl
  lint-report.json
```

## Index Purposes

| Index | Purpose |
|---|---|
| `manifest.json` | Active index build metadata |
| `agent-index.jsonl` | One row per page for fast filtering |
| `graph-edges.jsonl` | Valid graph relationships |
| `unresolved-edges.jsonl` | Ghost nodes and broken references |
| `section-index.jsonl` | Page section line ranges |
| `source-evidence-index.jsonl` | Source → finding → claim evidence map |
| `lint-report.json` | Build diagnostics |

Example `agent-index.jsonl`:

```json
{"id":"C-resilience","type":"concept","title":"Resilience","path":"02-concepts/resilience.md","lifecycle_stage":["neighbourhood-diagnosis","monitoring-learning"],"primary_topics":["resilience","drr"],"retrieval_status":"usable"}
```

Example `graph-edges.jsonl`:

```json
{"from":"T-resilience-milestone-scale","relation":"requires_concept","to":"C-resilience","status":"valid"}
```

Example `section-index.jsonl`:

```json
{"page_id":"C-resilience","section_id":"field-use","path":"02-concepts/resilience.md","start_line":34,"end_line":58}
```

---

# Index Publishing Lifecycle

Indexes are compiled snapshots.

Agents never write indexes directly.

## Build Flow

```text
1. Human or agent edits markdown/frontmatter.
2. Index builder scans markdown files.
3. Validator checks schema, IDs, relationships, and section anchors.
4. New indexes are built in a temporary build folder.
5. If valid, the build is atomically published.
6. If invalid, the system keeps the last-known-good index.
7. Diagnostics are written to lint reports.
```

Folder structure:

```text
indexes/
  current/
    manifest.json
    agent-index.jsonl
    graph-edges.jsonl
    unresolved-edges.jsonl
    section-index.jsonl

  builds/
    2026-05-18T132500Z/
      manifest.json
      agent-index.jsonl
      graph-edges.jsonl
      unresolved-edges.jsonl
      section-index.jsonl
      source-evidence-index.jsonl
      lint-report.json
```

Manifest example:

```json
{
  "build_id": "2026-05-18T132500Z",
  "build_status": "valid_with_warnings",
  "generated_at": "2026-05-18T13:25:00Z",
  "page_count": 241,
  "edge_count": 1632,
  "unresolved_edge_count": 7,
  "critical_error_count": 0,
  "warning_count": 14,
  "active": true
}
```

Operating rule:

> **Every agent pins to one `index_build_id` for the duration of a task.**

This prevents agents from using different graph states during the same advisory run.

---

# Ghost Node and State Drift Handling

A **Ghost Node** is a relationship target that does not resolve to a known local page.

Example:

```yaml
related_risks:
  - R-checklist-misuse
  - R-community-homogeneity
  - R-risk-that-does-not-exist
```

The index builder separates valid edges from unresolved edges.

Valid edge:

```json
{"from":"C-resilience","relation":"related_risk","to":"R-checklist-misuse","status":"valid"}
```

Unresolved edge:

```json
{
  "from": "C-resilience",
  "relation": "related_risk",
  "to": "R-risk-that-does-not-exist",
  "status": "unresolved",
  "reason": "target_id_not_found",
  "severity": "high",
  "source_file": "02-concepts/resilience.md"
}
```

Runtime rule:

> **Retrieval agents traverse only valid edges. Governance agents review unresolved edges.**

Ghost nodes do not break runtime. They enter the repair queue.

---

# Layer 6 — Advisory Agent Layer

The system does not depend on permanent fixed specialist agents.

Instead, it uses temporary **section-level retrieval/synthesis agents**. Their expertise comes from the context they retrieve.

## Advisory Flow

```text
User request
  ↓
Orchestrator
  ↓
Section task decomposition
  ↓
Section retrieval/synthesis agents
  ↓
Evidence packets
  ↓
Packet consolidator
  ↓
Writing agent
  ↓
Citation reviewer
  ↓
Risk reviewer
  ↓
Final field advisory output
```

Example user request:

> “How do we adapt our disaster-risk framework to a highly dense, informal settlement without turning our assessment into a compliance checklist?”

The Orchestrator decomposes this into sections:

| Section | Retrieval/Synthesis Focus |
|---|---|
| Decision framing | What decision is the team making? |
| Framework adaptation | How should the DRR framework be adapted? |
| Informal settlement context | What changes in dense informal settlements? |
| Assessment design | What should the team assess and how? |
| Checklist misuse risk | How to avoid compliance-checklist behavior |
| Inclusion / do-no-harm | How to avoid hidden exclusion or protection risks |
| MEL / indicators | How to avoid false precision |
| Tools / instruments | Which field tools or templates to use |

---

# Evidence Packet Schema

Section agents do not write final advice.

They produce compact evidence packets.

```yaml
packet_id: EP-framework-adaptation-001
section_id: framework-adaptation
section_title: Adapting the DRR Framework
index_build_id: 2026-05-18T132500Z

pages_read:
  - id: F-community-resilience-characteristics
    sections:
      - adaptation-guidance
      - limitations
  - id: R-checklist-misuse
    sections:
      - mitigation

claims:
  - claim_id: C001
    claim: >
      The DRR framework should be treated as an adaptable decision-support structure,
      not as a fixed compliance checklist.
    support:
      - source_id: S-2007-twigg-disaster-resilient-community
        finding_id: F-006
        pages:
          - 11
      - page_id: R-checklist-misuse
        section_id: mitigation
    confidence: high
    use_in_final: true

recommendations:
  - rec_id: R001
    recommendation: >
      Select locally relevant framework dimensions instead of applying every characteristic.
    supported_by:
      - C001

risks:
  - risk_id: RK001
    risk: Checklist misuse
    mitigation: >
      Define the assessment decision first, then select only relevant dimensions.
    supported_by:
      - C001

open_questions:
  - What specific disaster-risk framework is the team using?
  - Is the assessment for design, prioritization, baseline, or reporting?

human_review_flags:
  - If findings will inform targeting, require protection review.

packet_status: complete
```

Packet rule:

> **Every important claim must have support. Every recommendation must link to claim IDs. Every risk must include mitigation.**

---

# Claim Ledger and Writing Agent

The packet consolidator converts evidence packets into a Writer Context Bundle.

## Claim Ledger

```yaml
claim_ledger:
  - claim_id: C001
    approved_for_use: true
    citation_label: "[S-2007-Twigg:F-006:p11]"
  - claim_id: C002
    approved_for_use: true
    citation_label: "[R-checklist-misuse#mitigation]"
```

Writing Agent rule:

> **If a statement is not in the claim ledger, the Writing Agent cannot present it as fact.**

The Writing Agent may:

- simplify;
- organize;
- convert recommendations into field steps;
- improve readability;
- preserve citations.

The Writing Agent may not:

- invent claims;
- add unsupported advice;
- drop caveats;
- cite sources not present in the bundle;
- ignore required risks.

---

# Citation and Risk Review Layer

Before final output, two review passes run.

## Citation Reviewer

Checks:

- every factual claim has a claim ID;
- every claim ID maps to source support;
- citation supports the claim;
- unsupported claims are removed or marked as assumptions;
- overgeneralized claims are caveated.

## Risk Reviewer

Checks:

- checklist misuse risk;
- false precision risk;
- community homogeneity risk;
- protection-sensitive data risk;
- enabling-environment constraints;
- escalation triggers;
- human review requirements.

Final output is not delivered until citation and risk checks pass, or unresolved issues are explicitly surfaced.

---

# Layer 7 — Offline and Edge Runtime Layer

The system supports multiple runtime modes.

| Runtime Mode | Environment | Behavior |
|---|---|---|
| **Full runtime** | HQ/cloud/strong workstation | Full multi-agent loop, full library |
| **Edge laptop runtime** | Field laptop, intermittent connectivity | Partial repo, sequential agents, compact packets |
| **Minimal offline runtime** | Weak device, tiny local model, blackout | Search-first, playbooks, templates, short guidance |
| **No-LLM mode** | No model available | Human-readable emergency playbooks and checklists |

Runtime detection checks:

```yaml
connectivity:
available_ram:
local_model:
context_window:
slice_manifest:
index_manifest:
```

Then selects:

```yaml
runtime_mode: full | edge_laptop | minimal_offline | no_llm
```

---

# Partial Repository Deployment Slices

Field teams do not need to carry the whole library.

They receive a **deployment slice**.

```text
field-repo/
  slice-manifest.json
  wiki/
    concepts/
    frameworks/
    tools/
    field-instruments/
    risks/
    advisory-playbooks/
  sources/
    extracted/
    stubs/
    raw/
      optional/
  indexes/
    current/
  outputs/
    field-advice/
    evidence-packets/
    sync-queue/
  emergency/
```

## Slice Manifest

```json
{
  "slice_id": "urban-flood-informal-settlement-v1",
  "base_library_build_id": "2026-05-18T132500Z",
  "coverage": {
    "decision_domains": [
      "area-based-assessment",
      "community-resilience-assessment",
      "drr-framework-adaptation"
    ],
    "lifecycle_stage": [
      "neighbourhood-diagnosis",
      "joint-prioritization",
      "monitoring-learning"
    ],
    "hazards": [
      "flood",
      "landslide",
      "extreme-heat"
    ]
  },
  "raw_sources_included": false,
  "expected_runtime_mode": "edge_laptop",
  "known_limitations": [
    "Raw PDFs are not included; exact page verification requires later sync.",
    "Not suitable for final donor compliance review."
  ]
}
```

Partial repo rule:

> **Missing out-of-slice nodes are not broken. They are marked `external_missing`.**

Example:

```json
{
  "from": "T-resilience-milestone-scale",
  "relation": "requires_concept",
  "to": "C-participatory-assessment",
  "status": "external_missing",
  "available_in_full_repo": true,
  "severity": "info"
}
```

---

# Token and Agent Budget Adaptation

## Full Runtime

```yaml
max_section_agents: 6-10
max_pages_per_agent: 5-8
max_packet_tokens: 2000
citation_review: full
risk_review: full
```

## Edge Laptop Runtime

```yaml
max_section_agents: 2-4
max_pages_per_agent: 2-4
max_packet_tokens: 800-1500
citation_review: claim-ledger-only
risk_review: checklist-based
parallel_agents: false
```

## Minimal Offline Runtime

```yaml
max_section_agents: 1
max_pages_total: 3
max_packet_tokens: 500-800
max_final_answer_tokens: 1200
citation_review: source-label-only
risk_review: mandatory-risk-checklist
parallel_agents: false
```

Rule:

> **Small local models get fewer agents, fewer pages, smaller packets, shorter answers, and stricter templates.**

---

# Sync and Field Write Policy

Canonical pages are read-mostly on field devices.

Field users and local agents may write:

```text
outputs/field-advice/
outputs/evidence-packets/
outputs/field-notes/
outputs/proposed-library-updates/
```

They should not directly overwrite canonical concept, framework, tool, or risk pages unless explicitly in maintenance mode.

## Field-to-HQ Sync Proposal

```yaml
proposal_id: PU-2026-05-18-001
created_on_device: field-laptop-03
base_library_build_id: 2026-05-18T132500Z
target_page_id: R-checklist-misuse
proposal_type: update_existing_page
reason: "Field team observed checklist misuse during rapid flood assessment planning."
suggested_change: >
  Add warning that donor assessment templates can unintentionally encourage checklist-style use
  unless the team first defines which decisions the assessment will inform.
evidence:
  - field_note_id: FN-2026-05-18-004
review_required: true
status: pending_sync
```

HQ reviews and applies accepted updates.

---

# Emergency No-LLM Mode

The repository must remain useful without any model.

Add:

```text
emergency/
  start-here.md
  rapid-area-assessment-checklist.md
  community-resilience-assessment-checklist.md
  flood-informal-settlement-risk-guide.md
  protection-red-flags.md
  field-output-templates/
```

These files are:

- printable;
- human-readable;
- usable offline;
- independent of API access.

---

# Updated End-to-End Workflow

```text
1. Human curates source.
2. Raw source stored immutably.
3. Raw-content mirror generated.
4. Extracted source page created.
5. Reusable findings identified.
6. Findings routed into concepts, frameworks, tools, risks, and instruments.
7. Frontmatter graph updated.
8. JSONL indexes compiled.
9. Index build published atomically.
10. Field bundle or full repo syncs to device.
11. Field user asks operational question.
12. Orchestrator pins index build and decomposes task.
13. Section agents retrieve relevant sections.
14. Evidence packets are produced.
15. Packet consolidator creates claim ledger.
16. Writing Agent drafts only from approved claims.
17. Citation reviewer checks support.
18. Risk reviewer checks safeguards.
19. Final field advisory output is delivered.
20. Reusable field learning becomes a proposed update.
21. HQ reviews and merges accepted updates.
```

---

# Updated Ingest Workflow

```text
1. Store raw source in raw/.
2. Generate raw-content mirror.
3. Create extracted source page.
4. Identify reusable findings.
5. Build integration map.
6. Query existing graph for target pages.
7. Update existing pages before creating new ones.
8. Record integration status.
9. Run index builder.
10. Review unresolved edges and lint failures.
11. Human reviews flagged contradictions, promotions, and high-risk changes.
```

---

# Updated Query Workflow

```text
1. User asks field question.
2. Orchestrator classifies decision domain and lifecycle stage.
3. Runtime pins active index build.
4. Section tasks are created.
5. Retrieval agents filter agent-index.jsonl.
6. Retrieval agents follow graph-edges.jsonl.
7. Retrieval agents read exact sections via section-index.jsonl.
8. Retrieval agents produce evidence packets.
9. Packet consolidator creates claim ledger.
10. Writing Agent writes only from approved claims.
11. Citation and risk reviewers validate.
12. Final operational guidance is delivered.
```

---

# Updated Lint and Governance Rules

Critical failures:

- Missing stable `id`
- Duplicate `id`
- Invalid YAML
- Missing `type`
- Missing `retrieval_status`
- Missing required `lifecycle_stage`
- Relationship array points to broken local ID
- Required section declared but missing in body
- `contradicts:` missing where required
- `source_basis` missing for usable technical page
- Validated tool missing required field instruments
- Schema change not logged

High warnings:

- Ghost node without proposal
- Out-of-slice node not marked `external_missing`
- Missing related risks on tool
- Missing known tensions where tensions are referenced
- Deprecated page still used in active playbook
- Too many primary topics
- No retrieval questions
- Orphan page with no inbound graph edge

---

# The Human’s Role

Humans remain central.

They:

1. **Curate** sources.
2. **Validate** promotions and high-risk changes.
3. **Resolve** contradictions and contested tensions.
4. **Approve** field-critical guidance when escalation is triggered.
5. **Decide** how outputs are used operationally.
6. **Review** proposed updates from field devices.

The LLM drafts, retrieves, indexes, synthesizes, and packages. Humans validate what matters.

---

# Design Principles

1. Markdown/frontmatter is the source of truth.
2. JSONL indexes are compiled artifacts.
3. Agents never write indexes directly.
4. Stable IDs are used for relationships.
5. File paths can change without breaking the graph.
6. Section anchors enable surgical retrieval.
7. Retrieval agents produce evidence packets, not final prose.
8. The Writing Agent writes only from the claim ledger.
9. Citation and risk review are mandatory before final advisory output.
10. Partial repos are valid operating units.
11. Missing out-of-slice nodes are limitations, not failures.
12. Field devices submit proposed updates, not direct canonical edits.
13. The library must remain useful without an LLM.
14. The system should degrade gracefully under low bandwidth, weak models, or no connectivity.
15. The purpose is operational advice, not document search.

---

# Version History

## Version 2.3 — Updated 2026-05-11

Superseded v2.2. Frontmatter schemas reconciled with actual vault content: region dropped, author/institution separated, source maintenance fields added, field instrument parent tool constraint corrected to plural, concept status/maturity distinction clarified, lifecycle_stage vocabulary expanded to nine stages matching ABA operational model, governance reference updated to `governance/00_index.md`.

## Version 2.4 — Updated 2026-05-12

Superseded v2.3. All section indexes renamed from generic `00_index.md` to descriptive `00_*index.md` names. Governance reference updated accordingly. Librarian skill index-exclusion filter updated to `fname.startswith("00")`.

## Version 2.5 — Updated 2026-05-12

Superseded v2.4. Added `wiki/aba/01-sources/raw-content/` as an operational markdown mirror of raw PDFs. Documented ingest flow updates for raw-content generation and metadata sync. Added `scripts/sync_extracted_frontmatter_to_raw_content.py`.

## Version 2.6 — Updated 2026-05-18

Added stable ID graph schema, explicit relationship arrays, section-level addressability, compiled JSONL indexes, atomic index publishing, ghost node quarantine, evidence packet schema, claim-ledger writing, citation/risk review layer, offline runtime modes, partial repository deployment slices, field-to-HQ proposed update sync, and no-LLM emergency mode.
