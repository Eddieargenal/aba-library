---
type: schema
created: 2026-05-07
updated: 2026-05-18
status: active
version: 2.6
---

# Lint Rules — v2.6

## Critical Failures

- Missing `id`
- Duplicate `id`
- Invalid YAML frontmatter
- Missing `type`
- Missing `retrieval_status`
- Missing required `lifecycle_stage`
- Relationship field points to missing local ID
- Declared `sections` anchor missing in page body
- Missing `source_basis` for `retrieval_status: usable` technical pages

## High Warnings

- Ghost node not linked to proposal workflow
- No related risks on tool pages
- Missing known tensions when tensions are discussed in body
- Orphan page with no inbound edge
- Deprecated page still linked by active playbook/protocol
- Excessive `primary_topics` breadth

## Runtime Safety Rule

Retrieval agents traverse only valid edges from `graph-edges.jsonl`.
Unresolved edges are isolated in `unresolved-edges.jsonl`.
