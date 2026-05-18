---
type: overview
status: active
created: 2026-05-07
updated: 2026-05-18
---
# Agent Operating Model (v2.6)

## Operating Rules

- Pin one `index_build_id` per advisory run.
- Retrieve by section IDs using `section-index.jsonl`.
- Produce section-level evidence packets before drafting prose.
- Writing agent may use only approved claims from the claim ledger.
- Citation and risk review must pass before final advisory output.

## Required Advisory Flow

1. Orchestrator classifies decision domain and lifecycle stage.
2. Retrieval agents read filtered pages via `agent-index.jsonl` + `graph-edges.jsonl`.
3. Section agents produce evidence packets (`EP-*`).
4. Consolidator builds claim ledger.
5. Writer drafts from claim ledger only.
6. Citation reviewer validates support.
7. Risk reviewer checks safeguards/escalation triggers.
8. Output is published.

## Field Runtime Write Policy

Field devices write only to:
- `outputs/field-advice/`
- `outputs/evidence-packets/`
- `outputs/field-notes/`
- `outputs/proposed-library-updates/`

Canonical synthesis pages are read-mostly outside maintenance workflows.
