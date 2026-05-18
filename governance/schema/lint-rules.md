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
- Declared `sections` anchor missing in page body (`section_error:missing_anchor:{id}`)
- `sections:` field present but not a list (`sections_not_list`)
- Missing `source_basis` for `retrieval_status: usable` technical pages

## High Warnings

- Ghost node not linked to proposal workflow (`ghost_node:{target_id}`) — relationship target ID not found in local graph; enters repair queue, does not block publish
- No related risks on tool pages
- Missing known tensions when tensions are discussed in body
- Orphan page with no inbound edge (`orphan_page:{page_id}`)
- Deprecated page still linked by active playbook/protocol
- Excessive `primary_topics` breadth
- Page has no `sections:` frontmatter declaration (`missing_sections`)
- Source page missing explicit `id:` field; ID derived from `source_id:` (`derived_source_id:{derived_id}`)
- Source page missing explicit `retrieval_status:`; value derived from `status:` (`derived_retrieval_status:{value}`)

## Runtime Safety Rule

Retrieval agents traverse only valid edges from `graph-edges.jsonl`.
Unresolved edges are isolated in `unresolved-edges.jsonl`.
Ghost nodes do not block publish; they enter the governance repair queue.
