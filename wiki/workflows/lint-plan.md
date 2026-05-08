---
type: workflow
status: validated
updated: 2026-05-08
title: Wiki Lint Plan
sources: ['workflows/lint.md', 'SCHEMA.md']
tags: ['lint', 'workflow', 'governance']
---

# Lint Plan for Wiki Quality Governance

Purpose: Provide a self-contained, repeatable lint routine for the Karpathy llm-wiki vault.

Inputs:
- wiki/index.md
- memory/runtime/logs/log.md
- memory/categories/* md pages
- SCHEMA.md

Checks (in order):
1) Frontmatter canonicalization check for wiki/index.md (single frontmatter block with required fields).
2) Missing required frontmatter keys in pages (title, updated, sources, tags, type, status, etc.).
3) Broken wikilinks: links to non-existent pages.
4) Orphan pages: pages not reachable from wiki/index.md and without inbound wikilinks.
5) Stale pages: pages past thresholds defined in SCHEMA.md (in a separate thresholds reference).
6) Cross-link health: ensure at least two wikilinks per page and cross-links back.
7) Source drift: recompute sha256 for raw sources where applicable and flag drift.
8) Log hygiene: ensure log entries are appended-only and include proper metadata.
9) Governance traceability: verify that new pages cite vault governance rules.
10) Summarize results in a lint report and append to memory/runtime/logs/log.md.

Output: A structured lint report file (markdown) and an updated log entry.

Run cadence:
- Per ingest batch: after ingest, run lint-plan.md
- Periodic cadence: monthly, or after major schema changes.

Templates for lint output (copy into report):
```
## Lint Report [YYYY-MM-DD]
### Summary
- Total pages scanned: N
- Issues found: N

### Details
- [path/to/file.md] issue description

### Remediation plan
- ...
```

---

See also: [[../index]] · [[../../SCHEMA]] · [[../../workflows/lint]] · [[../vault-compliance-rules]]
