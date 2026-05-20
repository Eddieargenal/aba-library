---
type: schema
created: 2026-05-07
updated: 2026-05-19
status: active
version: 2.7
---

# Frontmatter Schema — v2.7

This vault now follows the ABA/DRR v2.6 architecture.

## Global Required Fields (all canonical wiki pages)

```yaml
id:
type:
title:
slug:
retrieval_status:
lifecycle_stage:
primary_topics:
related_concepts:
related_frameworks:
related_tools:
related_risks:
source_basis:
known_tensions:
contradicts:
used_by_playbooks:
output_templates:
sections:
created:
updated:
```

## Stable ID Prefixes

- `S-` source / extracted source
- `C-` concept
- `F-` framework
- `T-` tool
- `I-` field instrument
- `R-` risk
- `KTN-` known tension
- `P-` advisory playbook
- `D-` decision protocol
- `O-` output template / output
- `EP-` evidence packet
- `PU-` proposed update
- `SS-` slice spec

## Additional Tool Fields

```yaml
requires_concepts:
parent_frameworks:
required_inputs:
compatible_instruments:
mitigated_by:
```

## Additional Risk Fields

```yaml
risk_applies_to:
mitigated_by:
escalation_triggers:
```

## Source Page Required Extensions

```yaml
source_id:
canonical_file:
source_url:
source_url_status:
file_type:
source_type:
year:
author:
institution:
status:
ingest_date:
ingest_status:
confidence:
primary_context:
urban_applicability:
urban_adaptation_scope:
urban_adaptation_notes:
institutional_credibility:
evidence_quality:
composite_authority:
comparison_readiness:
findings:
cited_sources:
```

## `cited_sources` Entry Schema

```yaml
cited_sources:
  - raw_citation: "Author (Year) Title"
    wiki_id: S-slug        # omit if source not yet in wiki
    in_wiki: false         # auto-computed by build-index.py — never set manually
```

Rules:
- Include key contributing sources only (primary frameworks, foundational research, major guidelines the document builds on or applies)
- `wiki_id`: include only when the source is known to be in the wiki; omit entirely otherwise
- `in_wiki` is always auto-computed by the index builder — hand-set values will be overwritten

## `findings:` Compact Routing Record Schema

The `findings:` frontmatter list holds routing records only — not full finding content. Full content (claim statement, routing rationale, object references) lives in the body `#findings` section.

Every frontmatter finding entry must have exactly these 10 fields:

```yaml
findings:
  - finding_id: F-001
    finding_type: concept-definition
    knowledge_layer: conceptual
    lifecycle_stage: [neighbourhood-diagnosis]
    source_pages: ["p. 12"]
    candidate_target_pages:
      - wiki/aba/02-concepts/example-concept.md
    integration_action: enrich-concept
    field_query_trigger: "How do I assess..."   # write not-applicable for purely conceptual findings
    status: pending
    human_review_required: false
```

### `finding_type` controlled vocabulary
`concept-definition` / `framework-component` / `process-step` / `tool-description` / `risk-identification` / `tension-surface` / `evidence-gap` / `field-practice` / `monitoring-indicator` / `design-principle` / `decision-rule` / `task-seed`

### `knowledge_layer` controlled vocabulary
`conceptual` / `diagnostic` / `operational` / `decision`

Single-layer rule: assign the one layer that dominates. The combination `operational, decision` is the only permitted two-layer assignment and must be justified in one sentence.

### `integration_action` controlled vocabulary
`create-concept` / `enrich-concept` / `create-framework` / `enrich-framework` / `create-tool` / `enrich-tool` / `create-risk` / `enrich-risk` / `create-decision-rule` / `enrich-decision-rule` / `source_only` / `flag-for-review`

## Source Page Authority and Context Fields

```yaml
# Context
primary_context: rural | urban | generic | mixed
urban_applicability: direct | requires-adaptation | not-applicable
urban_adaptation_scope: none | minor | moderate | substantial
urban_adaptation_notes: "one sentence or 'none'"

# Authority
institutional_credibility: high | medium | low | mixed
evidence_quality: high | medium | low | mixed
composite_authority: high | medium | low | mixed

# Comparison readiness
comparison_readiness: high | medium | low | not-ready
```

Urban adaptation scope is always derived from the Step 11 checklist count: 0=none, 1–2=minor, 3–4=moderate, 5–7=substantial. Never set manually.

## `sections` Contract

Every listed section must have:
- an entry in frontmatter with `id`, `anchor`, `purpose`
- a matching body anchor, e.g. `<a id="field-use"></a>`

## Lifecycle Controlled Vocabulary

- `appropriateness-decision`
- `area-selection`
- `neighbourhood-diagnosis`
- `joint-prioritization`
- `coordination-design`
- `integrated-area-strategy`
- `implementation-adaptation`
- `monitoring-learning`
- `transition-handover`

## Retrieval Status Values

- `usable`
- `limited`
- `deprecated`
- `draft`

## Additional Known-Tension Fields

```yaml
tension_between:
tension_type:
resolution_status:
```

## Additional Advisory-Playbook Fields

```yaml
decision_domain:
lifecycle_stages:
entry_conditions:
exit_conditions:
```

## Additional Decision-Protocol Fields

```yaml
decision_type:
trigger_conditions:
decision_logic:
escalation_path:
```

## Additional Field-Instrument Fields

```yaml
instrument_format:
parent_tools:
data_quality_checks:
respondent_type:
```

## Additional Slice-Spec Fields

```yaml
slice_id:
decision_domains:
hazards:
expected_runtime_mode:
raw_sources_included:
```

## Authoring Rule

Relationships must point to stable IDs, not file paths.
