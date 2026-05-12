# LLM Wiki Architecture: Humanitarian Area-Based Approaches Knowledge System

## Overview

This Obsidian vault captures, distills, and retrieves humanitarian and disaster risk reduction content focused on area-based approaches. The wiki is designed as a compounding knowledge system where evidence accumulates, contradictions are preserved, and operational guidance improves with each source ingested.

**Core Design Principles:**
- **Evidence traceability**: All claims trace back to extracted sources via required `contradicts:` fields and source independence enforcement
- **Compilation separated from synthesis**: Raw sources remain immutable; structured synthesis happens in dedicated layers
- **Operational decision layers**: Accumulated knowledge translates into field-ready procedures (Frameworks → Tools → Field Instruments)
- **Agent inference over hardcoded guidance**: Lifecycle pages define stage requirements; agents reason about tool application
- **Epistemic humility**: Contradictions are preserved and surfaced explicitly rather than artificially resolved

---

## Section Architecture

### 01 — Sources (extracted + raw)

**Purpose**: The ingest layer where "compile once" happens.

**Structure**:
- `raw/`: Immutable PDFs — the evidence floor agents read during ingest but never modify
- `raw-content/`: Markdown text extracts of PDFs, generated once for fast agent reading during ingestion review (not the synthesis layer)
- `extracted/`: One structured synthesis page per document containing key findings, methodology notes, citation metadata, and required `contradicts:` field

**Key Rules**:
- Every `extracted/` page must have a `contradicts:` field — an empty `contradicts: []` is a meaningful assertion (source was checked and found consistent)
- A missing `contradicts:` field means nobody checked — flagged by weekly lint
- All claims in downstream sections trace back to an `extracted/` page
- After ingest, agents read `extracted/` pages rather than raw PDFs

**Frontmatter Schema (extracted pages)**:
```yaml
***
title: "UNHCR Area-Based Approaches in Urban Settings"
document_type: guidance_document  # evaluation | case_study | guidance_document | academic_paper | field_report
publication_date: 2024-03-15
source_dependencies:
  primary_evaluations: []  # If this IS an evaluation
  cites_evaluations: ["UNHCR-2023-Haiti-Evaluation"]  # Underlying data sources
  cites_case_studies: ["DRC-Goma-2022"]
  based_on_same_data_as: []  # Same field data, different publication
independence_hash: "UNHCR-2023-Haiti-Evaluation|DRC-Goma-2022"  # Auto-generated
contradicts: []  # Or detailed contradiction entries
***
```

**Maintenance**:
- After updating extracted frontmatter, run `scripts/sync_extracted_frontmatter_to_raw_content.py --apply` to sync agreed metadata into the raw-content mirror

**Who reads it**: Ingest agents (to compile); any agent needing evidence grounding or citation metadata

**When**: Read when verifying a claim or checking source coverage. Update whenever a new document is ingested.

---

### 02 — Concepts

**Purpose**: The accumulated definitional layer — what the entire source library says about each key term.

**Structure**: 25+ concept pages recording definitions with maturity ratings (emerging / established / contested), source counts, convergence scores, and operationalizability notes.

**Promotion Rules**:
- A concept page is created only when a finding appears in **≥2 independent extracted sources**
- Source independence is enforced: two documents citing the same underlying evaluation are NOT independent
- Independence verified via `independence_hash` comparison during lint checks

**Contradiction Handling**:
- Each concept page carries both a `known_tensions:` frontmatter field (for agent queries) and a `## Known Tensions` body section (for human reading)
- Both required when tensions exist
- Tensions section records where sources genuinely disagree — disagreements are named and preserved, not resolved artificially

**Frontmatter Schema**:
```yaml
***
concept_slug: urban-resilience
maturity: contested  # emerging | established | contested
source_count: 7
supporting_sources:
  - source-042
  - source-089
  - source-134
convergence_score: 0.62  # 0-1 scale
operationalizable: partial
known_tensions:
  - infrastructure_vs_social_cohesion
  - individual_vs_collective_focus
contradicts: []
***
```

**Value Proposition**: Without this layer, every query about "urban resilience" or "area-based approach" would require re-reading multiple documents to assemble a definition — work the wiki has already done and keeps current with each new source.

**Who reads it**: Any agent or person needing to use a contested term confidently across the full source base

**When**: Read when a question turns on a definition. Update whenever a new source adds a definition or materially shifts an existing tension.

---

### 03 — Frameworks

**Purpose**: The structured decision logic layer.

**Structure**:
- **Tier 1 operational frameworks** (9): Directly answer field team decisions
  - Requirements: ≥2 independent extracted sources, explicit decision logic, defined use conditions, linked field instruments, documented failure modes
- **Tier 2 reference frameworks** (32): Summarize wider DRR and urban resilience literature
  - Inform Tier 1 pages but are not operational decision tools (no field instrument requirement)

**Tier 1 Promotion Requirements**:
- ≥2 independent sources (verified via `independence_hash` comparison)
- Explicit decision logic documented
- Use conditions defined
- Field instruments linked
- Failure modes documented

**Version Control**:
- Superseded frameworks retain their pages — evidence chain must remain traceable even when guidance is replaced
- Use `superseded_by:` frontmatter field to link to replacement

**Frontmatter Schema**:
```yaml
***
framework_slug: area-selection-criteria
framework_tier: 1  # 1 | 2
lifecycle_stage:
  - appropriateness-decision
  - area-selection
decision_question: "Which geographic area should receive ABA programming?"
use_conditions: "Multi-actor response context with coordination capacity"
linked_tools:
  - area-selection-scoring-matrix
  - feasibility-assessment-tool
field_instruments_required: true
failure_modes:
  - "Captures displacement dynamics poorly in fluid contexts"
  - "Requires baseline data often unavailable in rapid onset"
supporting_sources:
  - source-042
  - source-089
contradicts: []
superseded_by: null  # Or framework slug if superseded
***
```

**Value Proposition**: Frameworks organize concept-level knowledge into decision logic, covering the full programme arc from appropriateness decision to handover.

**Who reads it**: Programme designers, technical advisors, tool developers

**When**: Read before designing or selecting a tool. Update when a new source introduces a framework or a Tier 2 framework accumulates enough field evidence for Tier 1 promotion.

---

### 04 — Tools

**Purpose**: The actionable layer — field-ready decision procedures.

**Structure**: 17+ operational tools translating Tier 1 frameworks into field procedures, covering the full programme cycle from ABA feasibility through handover.

**Content**: Each tool specifies:
- Evidence required
- Collection method
- Respondents
- Linked field instruments
- Analysis steps
- Scoring threshold
- Quality checks

**Validation Requirements**:
- Tool reaches `validated` status only when:
  - All `field_instruments` are linked
  - All linked instruments have `validation_status: field_tested` or `validated_multi_context`
  - All linked instruments have `last_field_use` within 24 months
  - `data_quality_checks: true` on all instruments
- Validation enforced by weekly lint run
- Tools with failing instrument validation checks are flagged and cannot claim `validated` status

**Multi-Stage Application**:
- Tools serving multiple lifecycle stages are tagged with array: `lifecycle_stage: [area-selection, coordination-design, monitoring-learning]`
- Agents retrieve tools by stage query and infer application context from stage decision requirements
- Application differences NOT hardcoded in tool pages — agents reason from stage requirements

**Frontmatter Schema**:
```yaml
***
tool_slug: stakeholder-mapping
tool_status: validated  # draft | field_tested | validated
lifecycle_stage:
  - area-selection
  - coordination-design
  - monitoring-learning
primary_output: "Actor inventory with roles, capacities, relationships"
evidence_required: "Key informant interviews, organizational documents"
field_instruments:
  - stakeholder-mapping-kii-guide
  - organizational-document-review-checklist
instrument_validation_check: passing  # Auto-generated by daily sync
last_validation_date: 2025-02-10
data_quality_checks: true
contradicts: []
***
```

**Value Proposition**: A framework tells you how to think; a tool tells you what to do. Field teams don't design assessment procedures from scratch.

**Who reads it**: Field coordinators, assessment leads, programme managers during assessment and design

**When**: Read before a field assessment or design session. Update when field use reveals evidence gaps or a new instrument is linked.

---

### 05 — Field Instruments

**Purpose**: The collection layer — what to collect, from whom, with what quality checks.

**Structure**: 18+ data collection instruments:
- KII guides
- Observation forms
- Mapping sheets
- Household mini-survey
- HEVC matrix
- Stakeholder mapping form
- Resource inventory
- Duplication/gap matrix
- Checklists and templates

**Validation Tracking**:
- Each instrument tracks field use history, contexts validated, adaptations required, and known failure modes
- `validation_status` determines whether tools linking this instrument can claim `validated` status
- Instruments with `last_field_use` >24 months are considered stale and trigger tool validation warnings

**Export Capabilities**:
- `can_export_to:` field enables queries like "which instruments can export to KoboToolbox"
- Matters for field digitization planning

**Frontmatter Schema**:
```yaml
***
instrument_slug: stakeholder-mapping-kii-guide
instrument_type: interview_guide  # observation_form | survey | matrix | checklist
validation_status: validated_multi_context  # draft | field_tested | validated_multi_context
field_use_history:
  - context: "Haiti Port-au-Prince 2024"
    date: 2024-06-15
    programme: "Urban DRR Programme"
    adaptations_required: "Translated to Creole, simplified literacy requirements"
    effectiveness: high
  - context: "Bangladesh Cox's Bazar 2025"
    date: 2025-02-10
    programme: "Rohingya Response ABA"
    adaptations_required: "None—used as-is"
    effectiveness: high
last_field_use: 2025-02-10
validation_expires: 2027-02-10  # 24 months from last use
known_failure_modes:
  - "Requires adaptation for non-literate populations"
  - "Time-intensive in high-insecurity contexts (90+ min per interview)"
data_quality_checks: true
quality_check_procedures:
  - "Spot-check 10% of completed interviews for completeness"
  - "Cross-reference actor lists across multiple KIIs"
can_export_to:
  - kobo
  - excel
  - markdown
contradicts: []
***
```

**Value Proposition**: Pre-specified collection procedures with quality checks mean field teams don't design from scratch. A single instrument may feed multiple tools.

**Who reads it**: Field enumerators, assessment leads, data managers

**When**: Use during data collection. Update when quality checks reveal systematic gaps.

---

### 06 — Lifecycle

**Purpose**: The sequencing layer — the 9-stage ABA programme cycle.

**Structure**: 11 pages mapping programme stages using controlled vocabulary slugs:
1. `appropriateness-decision`
2. `area-selection`
3. `neighbourhood-diagnosis`
4. `joint-prioritization`
5. `coordination-design`
6. `integrated-area-strategy`
7. `implementation-adaptation`
8. `monitoring-learning`
9. `transition-handover`

**Content**: Each lifecycle page defines:
- Stage purpose (decision question)
- Required inputs (what must exist before this stage)
- Minimum outputs (what must be produced before advancing)
- Tools applicable at this stage
- Known failure modes at this transition

**Agent Retrieval Pattern**:
- Lifecycle pages list tools applicable at each stage
- Agents infer tool application from stage decision requirements
- Tools tagged with multiple stages are retrieved appropriately for each context

**Query Axis**:
- `lifecycle_stage:` is the primary frontmatter query axis across all page types
- Tools, instruments, and frameworks with missing `lifecycle_stage:` field are retrieval blackholes (flagged by lint)

**Frontmatter Schema**:
```yaml
***
stage_slug: coordination-design
stage_number: 5
decision_question: "How will multiple actors coordinate in this area?"
required_inputs:
  - actor_inventory_from_area_selection
  - joint_priorities_from_joint_prioritization
minimum_outputs:
  - coordination_architecture
  - responsibility_mapping
  - information_management_protocol
tools_applicable:
  - stakeholder-mapping
  - duplication-detection-matrix
  - coordination-architecture-template
known_failure_modes:
  - "Coordination platform established without municipal buy-in"
  - "Information management protocol not resourced"
***
```

**Bidirectional Consistency Requirement**:
- Every tool in `tools_applicable:` must have that stage in its own `lifecycle_stage:` frontmatter
- Every tool tagged with a lifecycle stage must appear in that stage's `tools_applicable:` list
- Enforced by weekly lint to prevent silent retrieval failures

**Value Proposition**: Without this section, programme managers would reconstruct sequencing logic for each programme.

**Who reads it**: Programme managers and coordinators sequencing work across a full programme cycle

**When**: Read at each stage transition. Update when a tool is added or a stage's minimum outputs are revised.

---

### 07 — Sector Applications

**Purpose**: The translation layer — how generic ABA programme logic maps onto sector-specific technical requirements.

**Structure**: 21+ sector-specific pages:
- WASH
- Shelter
- Livelihoods
- Protection
- Health
- Education
- DRR
- Urban governance
- And more

**Design Philosophy**:
- The compiled logic in sections 02–06 is intentionally sector-agnostic
- This layer translates it into sector-specific terms
- Prevents sector design from being imported wholesale from sector silos that ignore area-level dynamics

**Current Status**: Stubs — to be populated as sector evidence is extracted from sources

**Who reads it**: Sector technical advisors and cluster leads working within an ABA programme

**When**: Read during sector design (stages 5–6). Populate stubs as sector evidence accumulates.

---

### 08 — Coordination

**Purpose**: The multi-actor protocol layer — where programme logic meets the reality of multiple actors in the same area.

**Structure**: 19 pages covering:
- Coordination architecture
- IASC 2026 area-based coordination (ABC) ToR (authoritative operational definition)
- Actor and responsibility mapping
- Duplication detection
- Gap analysis
- Cluster/area interface
- Municipal engagement
- Information management
- Referral pathways
- Decision and meeting templates

**Authoritative Reference**:
- IASC 2026 ABC ToR is the operational definition anchoring this section
- Coordination leads don't reinvent that logic for each response
- `contradicts:` fields track where field practice has diverged from or challenged the ToR

**Value Proposition**: Compiled multi-actor protocols prevent reinvention of coordination architecture in each response.

**Who reads it**: Area coordination leads, information managers, cluster liaisons, municipal counterparts

**When**: Read when establishing or reviewing a coordination platform (stages 5–8). Update when the IASC ToR changes or field experience reveals protocol gaps.

---

### 09 — Monitoring & Learning

**Purpose**: The feedback layer — where field observations feed back into the system.

**Structure**: 11 pages covering:
- ABA MEL framework
- Area-level outcome monitoring
- Resilience indicators
- Adaptive management triggers
- Participation quality monitoring
- Sendai reporting
- Outcome harvesting
- Learning documentation

**Compounding Loop**:
- Field observations update what the wiki knows about what works
- Validates or challenges existing indicators
- Identifies where programmes need to adapt
- Closes the compounding loop: wiki doesn't just inform field decisions, it is updated by what field decisions produce

**Sendai Framework Integration**:
- Links ABA outcomes to Sendai Framework municipal reporting
- Prevents reconstruction of that obligation each cycle

**Who reads it**: MEL officers, programme managers, adaptive management leads, municipal DRR reporting officers

**When**: Read during MEL design and at each reassessment cycle. Update when new indicators are validated or reporting requirements change.

---

### 10 — Transition & Scale

**Purpose**: The closure and replication layer.

**Structure**: 8 pages covering:
- Handover planning
- Readiness checklist
- Exit strategy
- Municipal integration
- Build-back-better alignment
- Replication logic
- Scale-up frameworks

**Handover Requirements**:
- Identified responsible actors
- Maintenance budgets
- Explicitly transferred risks
- Transition that doesn't undermine local capacity

**Replication Logic**:
- What's needed to take a pilot to a second context
- Prevents rediscovery of knowledge from scratch

**Learning Integration**:
- After each completed handover, lessons integrate back here
- Checklist and criteria improve with each programme

**Value Proposition**: Handover failure is one of the best-documented risks in ABA programmes — this section compiles what responsible closure looks like.

**Who reads it**: Programme managers, transition leads, municipal counterparts, donors

**When**: Read from stage 7 onwards. Update after each completed handover.

---

### 11 — Patterns

**Purpose**: The distilled wisdom layer — validated implementation patterns.

**Structure**: Repository for recurring solutions to recurring problems, compiled from ≥2 independent field case studies.

**Promotion Requirements**:
- Pattern requires ≥2 independent field case studies
- Same source independence rule as concept promotion applies
- Two case studies citing the same underlying evaluation are NOT independent
- Bar is intentionally high

**Content Requirements**:
- Evidence base documented
- Conditions of applicability defined
- Failure modes documented

**Current Status**: Empty — will grow as source library expands and case study evidence can be synthesized across contexts

**Value Proposition**: A pattern is the highest-confidence form of accumulated knowledge in the wiki — it has survived in multiple independent contexts.

**Who reads it**: Programme designers, technical advisors, agents synthesizing case study evidence

**When**: Read at design stage. File a new pattern only when the same solution has worked in at least two independent contexts.

---

### 12 — Risks & Contradictions

**Purpose**: The critical lens layer — tracks the wiki's own limits.

**Structure**: 13+ pages cataloguing:
- Known risks
- Common misuse patterns
- Contradictions in source literature
- Weak evidence claims
- Stale guidance
- Unresolved questions
- Evidence gaps

**Core Principle**: Every compounding knowledge base needs a layer that tracks its own limits.

**Contradiction Workflow**:

**Detection** (automated during ingest):
```yaml
contradicts:
  - page: frameworks/tier-1/area-selection-criteria
    field: minimum_population_threshold
    nature: "New source suggests 5,000 minimum vs. existing 10,000"
    flagged_date: 2026-05-12
    status: pending_review
```

**Review** (human judgment required):
- Technical reviewer examines contradiction
- Updates status: `preserved_tension | resolved_supersession | resolved_invalid | under_investigation`
- Documents resolution rationale

**Resolution Outcomes**:

*Preserved tension* (most common):
- Both positions remain in wiki
- Context note added to relevant pages
- `known_tensions:` field updated on concept pages
- Agents cite both positions when queried

*Resolved by supersession*:
- Original page gains `superseded_by:` field or moves to archive
- New guidance becomes canonical
- Resolution note documents change

*Resolved as invalid*:
- Reviewer determines source misinterpreted or methodologically flawed
- Original guidance unchanged
- Resolution note documents reasoning

**Agent Behavior Under Contradiction**:

When `status: preserved_tension`:

Population thresholds vary by settlement type:

- Urban/peri-urban areas: ≥10,000 (Source: IASC 2024)
    
- Rural/dispersed settlements: ≥5,000 (Source: DRC 2025)    

Both thresholds are evidence-based. Your context determines which applies.  
[Ask clarifying question to help user choose]

When `status: pending_review`:

⚠️ Note: A recent source suggests different guidance.  
This is under technical review.

Current operational guidance remains: [existing guidance]  
Check back after [review_deadline] for updated guidance.


**Contradiction Schema**:
```yaml
contradicts:
  - page: concepts/urban-resilience
    field: definition
    nature: "Emphasizes infrastructure vs. social cohesion"
    flagged_date: 2026-05-12
    reviewed_date: 2026-05-18
    status: preserved_tension
    reviewer: eddie_argenal
    resolution_note: "Both dimensions valid—added to known_tensions"
```

**Lint Rules**:
- Missing `contradicts:` field → Page not checked for contradictions
- `status: pending_review` and `flagged_date` >30 days old → HIGH priority flag
- `status: resolved_*` but no `resolution_note:` → Resolution not documented
- `status: preserved_tension` but referenced page lacks corresponding `known_tensions:` entry → Bidirectional link broken

**Value Proposition**: Without this section, the wiki would confidently propagate weak or contradicted claims — and grow more dangerous the richer it became.

**Who reads it**: Quality reviewers, protection advisors, programme designers, evaluators — anyone generating external-facing output

**When**: Read at design review and before any external output. Update when a new contradiction surfaces, a risk materializes, or a previously unresolved question is settled.

---

## Quality Assurance System

### Automated Lint Checks (Cron Schedule)

**Weekly Quality Checks** (Sundays 2 AM CEST):
```bash
0 2 * * 0 /usr/bin/python3 /path/to/wiki/scripts/run_all_lint_checks.py --vault /path/to/obsidian-vault --notify daily-note
```

Checks:
1. **Source independence**: Verifies concept promotion based on independent sources (compares `independence_hash` across supporting sources)
2. **Tool validation status**: Ensures tools claiming `validated` status have all linked instruments validated and current (<24 months)
3. **Unresolved contradictions**: Flags `status: pending_review` contradictions >30 days old
4. **Lifecycle tagging coverage**: Verifies all tools/frameworks have `lifecycle_stage:` fields
5. **Required frontmatter fields**: Checks for missing required fields by page type
6. **Bidirectional consistency**: Ensures lifecycle pages' `tools_applicable` lists match tools' `lifecycle_stage` tags

**Daily Contradiction Review** (Weekdays 9 AM CEST):
```bash
0 9 * * 1-5 /usr/bin/python3 /path/to/wiki/scripts/check_pending_contradictions.py --vault /path/to/obsidian-vault --threshold 7 --notify daily-note
```

**Daily Tool Validation Sync** (Every day 3 AM CEST):
```bash
0 3 * * * /usr/bin/python3 /path/to/wiki/scripts/sync_tool_validation.py --vault /path/to/obsidian-vault --apply
```

### Notification System

Alerts written to Obsidian daily note at `daily-notes/{YYYY-MM-DD}.md`:

```markdown
## 🔴 Wiki Quality Alert

**3** high-priority violations detected.

### Top Issues
- `extracted/source-089.md`: Source independence violation—shares citations with source-042
- `04-tools/area-selection-scoring.md`: Linked instrument not validated
- `02-concepts/urban-resilience.md`: Contradiction pending review for 35 days

[[_lint-dashboard|View full report]]
```

### Quality Dashboard

Dashboard page at `_lint-dashboard.md` provides real-time status via Dataview queries:
- Current pass/fail status
- High-priority violation count
- Medium-priority violation count
- Drill-down into violations by check type
- Links to affected pages

---

## Key Design Decisions

### 1. Source Independence Enforcement

**Rule**: Two documents citing the same underlying evaluation are not independent sources.

**Implementation**:
- `independence_hash` auto-generated from cited evaluations/case studies
- Lint compares hashes before allowing concept promotion
- Human override available with documented justification

**Rationale**: Prevents artificial evidence accumulation from multiple publications of the same data.

---

### 2. Contradiction Preservation Over Resolution

**Rule**: Contradictions require human judgment before resolution. Preserve tensions rather than artificially resolve them.

**Implementation**:
- `contradicts:` field required on every page
- Empty array `contradicts: []` means "checked and found consistent"
- Missing field means "not checked" (lint violation)
- Status workflow: `pending_review → preserved_tension | resolved_supersession | resolved_invalid`

**Rationale**: Humanitarian field is contested; artificial resolution erodes trust. Surfacing tensions explicitly builds credibility.

---

### 3. Agent Inference Over Hardcoded Guidance

**Rule**: Lifecycle pages list applicable tools and define stage requirements. Agents infer tool application from decision context.

**Implementation**:
- Lifecycle pages contain `decision_question`, `required_inputs`, `minimum_outputs`, `tools_applicable`
- Tool pages contain `primary_output`, `evidence_required`, `lifecycle_stage` array
- Agents reason: "Stage requires X decision, tool produces Y output, therefore tool applies to stage by producing Y for decision X"

**Rationale**: Avoids n×m documentation burden. Scales better as tool library grows. Requires reasoning-capable agents (acceptable given Claude-class models in use).

---

### 4. Validation Status Propagation

**Rule**: Tools cannot claim `validated` status unless all linked instruments are validated and current.

**Implementation**:
- Instruments track `validation_status` and `last_field_use`
- Daily sync updates tool `instrument_validation_check` based on linked instrument status
- Lint flags tools claiming `validated` with failing instrument checks

**Rationale**: Prevents "validated tool" label from becoming meaningless. Protects field teams from deploying untested procedures.

---

### 5. Lifecycle Stage as Primary Query Axis

**Rule**: `lifecycle_stage:` field is required on all tools, frameworks, and instruments.

**Implementation**:
- Frontmatter field accepts array: `lifecycle_stage: [area-selection, coordination-design]`
- Lifecycle pages maintain `tools_applicable` lists
- Lint enforces bidirectional consistency

**Rationale**: Enables stage-based retrieval ("show me all tools for coordination-design"). Missing field creates retrieval blackhole.

---

## Agent Behavior Guidelines

### Citation Under Contradiction

When retrieved content includes `contradicts: [status: preserved_tension]`:

1. **Retrieve both contradicted positions** (retrieval ranking automatically includes contradiction pairs)
2. **Surface tension explicitly** in response
3. **Cite each position with source**
4. **Explain nature of disagreement** using `nature:` field from contradiction
5. **Ask clarifying question** to help user choose appropriate position for their context

**Never**:
- Cite one position without mentioning the contradiction
- Present contradiction as agent uncertainty (both positions are valid)
- Arbitrarily recommend one position
- Use "newest source wins" logic

### Validation Status Awareness

When citing tools or instruments:

- Check `instrument_validation_check` status on tools
- If `failing`, note to user: "⚠️ This tool's linked instruments require revalidation"
- If instrument `last_field_use` >24 months, note: "Last field-validated [date]—may require adaptation"
- Never cite `draft` status tools as operational without caveat

### Source Independence in Synthesis

When synthesizing across multiple sources:

- Check `independence_hash` to avoid citing non-independent sources as if they provide independent confirmation
- When two sources cite the same evaluation, acknowledge: "Both Source A and Source B draw from [Evaluation], so represent a single evidence base"

---

## Maintenance Workflows

### Ingest Workflow (New Document)

1. **Extract**: PDF → `raw/` + markdown → `raw-content/`
2. **Synthesize**: Create `extracted/` page with key findings, methodology, citations
3. **Generate independence hash**: Auto-populate `independence_hash` from cited evaluations
4. **Check contradictions**: Agent reviews for conflicts with existing pages
5. **Populate contradicts field**: Either `contradicts: []` or detailed contradiction entries
6. **Sync metadata**: Run `scripts/sync_extracted_frontmatter_to_raw_content.py --apply`

### Concept Promotion Workflow

1. **Trigger**: Finding appears in extracted source
2. **Check independence**: Compare `independence_hash` of new source against existing sources supporting this concept
3. **If independent and count ≥2**: Promote to concept page
4. **If not independent**: Flag for review, document in `12—Risks`

### Tool Validation Update Workflow

1. **Field use completed**: Update instrument's `field_use_history` with new entry
2. **Update validation date**: Set `last_field_use` to completion date
3. **Daily sync runs**: `scripts/sync_tool_validation.py` updates all tools linking this instrument
4. **Tool status auto-updates**: `instrument_validation_check` reflects current state

### Contradiction Resolution Workflow

1. **Detection**: Ingest agent flags contradiction, sets `status: pending_review`
2. **Review**: Human reviewer examines within 30 days (enforced by lint)
3. **Decision**: Update `status` to `preserved_tension | resolved_supersession | resolved_invalid`
4. **Documentation**: Add `resolution_note` explaining rationale
5. **Propagation**: If `preserved_tension`, update `known_tensions` on relevant concept pages

---

## Technical Stack Integration

**Obsidian**: Knowledge vault and human interface
**Python**: Lint scripts, sync scripts, automation
**Cron**: Scheduled quality checks and maintenance
**Dataview**: Dashboard queries and violation surfacing
**Claude/LLM**: Ingest agents, retrieval agents, synthesis agents
**Markdown + YAML**: Universal format for portability

**No external dependencies**: Email/Slack optional; daily note integration recommended for notifications.

---

## Success Metrics

**Knowledge Accumulation**:
- Source count in `extracted/`
- Concept pages promoted (with independent source verification)
- Patterns validated across contexts

**Quality Maintenance**:
- Contradiction resolution time (target: <30 days)
- Percentage of tools with `passing` instrument validation
- Lint pass rate (target: zero high-priority violations)

**Operational Usage**:
- Field instruments deployed and validated
- Tools reaching `validated_multi_context` status
- Lifecycle stage coverage (all stages have operational tools)

**Compounding Loop Closure**:
- Field use history entries on instruments
- Handover lessons integrated into section 10
- MEL findings updating indicator validity in section 09

---

## Version Control and Evolution

**Page Supersession**:
- Superseded pages retain content with `superseded_by:` frontmatter
- Evidence chain remains traceable
- Agent queries retrieve current version but can surface historical context

**Framework Evolution**:
- Tier 2 frameworks promoted to Tier 1 when field evidence accumulates
- Promotion requires updated frontmatter: field instruments linked, failure modes documented

**Vocabulary Control**:
- Lifecycle stage slugs are controlled vocabulary
- New stages require architecture update
- Lint enforces vocabulary consistency

---

## Deployment Context

**User**: Senior humanitarian technical leader building AI-powered knowledge systems
**Use Case**: Rapid context analysis and programme design support for humanitarian ABA programmes
**Geographic Scope**: Multi-country emergency response contexts
**Technical Context**: Proxmox infrastructure, Docker containers, Claude agents, RAG pipelines, Obsidian vault

**Design Constraint**: Must work offline and in low-bandwidth environments after initial sync.

---

## Future Enhancements

**Candidate Additions** (not yet implemented):
- Vector database integration for semantic search
- Multi-language support (French, Spanish, Arabic extraction)
- Field instrument digitization (KoboToolbox export automation)
- Case study pattern mining (automated pattern detection from field reports)
- Municipal integration playbook (sub-section under 10—Transition)

**Not Planned** (deliberately excluded):
- Real-time collaboration (Obsidian sync sufficient)
- Complex workflow orchestration (n8n rejected as unnecessarily complex)
- External service dependencies (maintain offline capability)