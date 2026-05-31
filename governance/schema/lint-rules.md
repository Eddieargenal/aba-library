---
type: schema
created: 2026-05-07
updated: 2026-05-31
status: active
version: 2.7
---

# Lint Rules — v2.7

Enforced by `scripts/build-index.py`. Critical failures block atomic publish to
`indexes/current/`; warnings are recorded in `lint-report.json` and do not block.

## Critical Failures (block publish)

- Missing `id`
- Duplicate `id`
- Invalid YAML frontmatter
- Missing `type`
- Missing `title`
- Missing `retrieval_status`
- `retrieval_status` not in controlled vocabulary (`invalid_retrieval_status:{value}`)
- Missing required `lifecycle_stage`
- Missing `source_basis` on a `retrieval_status: usable` technical page
  (`missing_source_basis_usable`) — technical = concept, framework, tool,
  field-instrument, risk, decision-protocol
- Declared `sections` anchor missing in page body (`section_error:missing_anchor:{id}`)
- `sections:` field present but not a list (`sections_not_list`)

## High Warnings (recorded, do not block)

- Relationship field points to a target ID not in the local graph
  (`ghost_node:{target_id}`) — the edge is isolated in `unresolved-edges.jsonl`
  and enters the governance repair queue. **This is a warning, not a critical
  failure**: a partial repo legitimately references out-of-slice nodes.
- Orphan page with no inbound edge (`orphan_page:{page_id}`)
- `lifecycle_stage` value not in controlled vocabulary (`invalid_lifecycle_stage:{value}`)
- `id` prefix does not match page type (`id_prefix_mismatch:{id}:expected:{prefix}`)
- Usable tool page with no `related_risks` (`tool_missing_related_risks`)
- `primary_topics` breadth exceeds limit (`excessive_primary_topics:{count}`, limit 6)
- Deprecated page still linked by an active playbook/protocol
  (`deprecated_target_linked:{target_id}`)
- Page has no `sections:` frontmatter declaration (`missing_sections`)
- Source page missing explicit `id:`; derived from `source_id:` (`derived_source_id:{id}`)
- Source page missing explicit `retrieval_status:`; derived from `status:` (`derived_retrieval_status:{value}`)

## Routing Report (`routing-report.json`)

Separate from lint. Lists every source finding that is still **open** — i.e. its
`status` is not terminal (`integrated`/`done`/`complete`/`resolved`/`source_only`)
**or** one of its `candidate_target_pages` does not yet exist on disk. This surfaces
the source→synthesis handoff that the graph alone cannot signal: a vault of pure
source pages builds cleanly yet may carry a large unrouted findings backlog.

`manifest.json` exposes `pending_finding_count`; the report adds
`unrouted_finding_count` (findings with at least one missing target page) and the
full `pending_findings` list.

## Runtime Safety Rule

Retrieval agents traverse only valid edges from `graph-edges.jsonl`.
Unresolved edges are isolated in `unresolved-edges.jsonl`.
Ghost nodes do not block publish; they enter the governance repair queue.

## Controlled Vocabularies

Single source of truth is `scripts/schema.py`; the prose docs mirror it inside
```schema:<key>``` blocks that `scripts/check-schema.py` verifies. The builder validates:

```schema:retrieval_status
usable
limited
deprecated
draft
```

```schema:lifecycle_stage
appropriateness-decision
area-selection
neighbourhood-diagnosis
joint-prioritization
coordination-design
integrated-area-strategy
implementation-adaptation
monitoring-learning
transition-handover
```

```schema:id_prefix
S- source
C- concept
F- framework
T- tool
I- field-instrument
R- risk
KTN- known-tension
P- advisory-playbook
D- decision-protocol
O- output-template
SS- slice-spec
OVR- overview
```
