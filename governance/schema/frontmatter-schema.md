---
type: schema
created: 2026-05-07
updated: 2026-05-18
status: active
version: 2.6
---

# Frontmatter Schema — v2.6

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
status:
ingest_date:
ingest_status:
confidence:
findings:
```

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
