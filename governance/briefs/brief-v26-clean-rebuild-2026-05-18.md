---
type: brief
status: active
created: 2026-05-18
updated: 2026-05-18
---

# v2.6 Clean Rebuild Plan

## Objective

Rebuild synthesis layers from sources using ABA/DRR v2.6 architecture.

## Steps

1. Archive legacy v2.5 synthesis content.
2. Recreate clean canonical folders and indexes.
3. Enforce v2.6 schema/templates with stable IDs and section anchors.
4. Compile JSONL indexes to `indexes/builds/<build_id>/`.
5. Publish atomically to `indexes/current/` only on critical-pass.
6. Migrate extracted sources and new synthesis pages to strict v2.6 fields.
7. Rebuild concept/framework/tool/risk layers from routed findings.

## Completion Criteria

- `critical_error_count: 0` in lint report.
- `indexes/current/manifest.json` points to latest valid build.
- All canonical pages contain stable IDs and declared section anchors.
- Relationship arrays resolve to valid local IDs.
