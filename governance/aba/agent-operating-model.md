---
type: overview
status: active
version: 2.7
created: 2026-05-07
updated: 2026-05-18
---

# Agent Operating Model (v2.7)

## Operating Principles

- Pin one `index_build_id` for the full advisory run.
- Retrieve by stable IDs and section spans, not broad file scans.
- Produce evidence packets before narrative drafting.
- Write only from approved claim-ledger claims.
- Require citation and risk review before release.

## Runtime Modes

- `full`
- `edge_laptop`
- `minimal_offline`
- `no_llm`

Mode requirements:
- Respect section/task ceilings set by orchestrator.
- Use `emergency/` assets in `no_llm` mode.
- Keep outputs concise under constrained runtime modes.

## Required Advisory Flow

1. Orchestrator classifies decision domain and lifecycle stage.
2. Orchestrator pins `index_build_id` from `indexes/current/manifest.json`.
3. Retrieval agents filter candidates via `agent-index.jsonl`.
4. Retrieval agents traverse valid edges via `graph-edges.jsonl`.
5. Retrieval agents resolve section spans via `section-index.jsonl`.
6. Section agents produce evidence packets (`EP-*`).
7. Consolidator merges packets into claim ledger.
8. Writing agent drafts from approved claims only.
9. Citation reviewer verifies claim-to-source support.
10. Risk reviewer validates safeguards and escalation triggers.
11. Final advisory output is stored in `outputs/field-advice/`.

## Evidence Packet Minimum

Each packet must include:
- `packet_id`
- `section_id`
- `index_build_id`
- `pages_read`
- `claims` with support
- `recommendations` linked to claim IDs
- `risks` with mitigation linked to claim IDs
- `open_questions`
- `human_review_flags`
- `packet_status`

## Claim-Ledger Rule

The writing agent may not introduce facts absent from the approved claim ledger.
Unsupported statements must be removed or clearly marked as assumptions.

## Index Build and Publish Contract

- Build with `scripts/build-index.py`.
- Build outputs to `indexes/builds/<build_id>/`.
- Publish to `indexes/current/` only if critical lint errors are zero.
- Unresolved edges remain quarantined in `unresolved-edges.jsonl`.

## Field Runtime Write Policy

Field-side and runtime writes are restricted to:
- `outputs/field-advice/`
- `outputs/evidence-packets/`
- `outputs/field-notes/`
- `outputs/proposed-library-updates/`
- `outputs/sync-queue/`

Canonical pages in `wiki/aba/` are not directly overwritten from field workflows.

## Sync and Promotion Flow

1. Field updates are packaged as `PU-*` proposals.
2. Proposals enter `outputs/sync-queue/`.
3. HQ review evaluates proposals at Gate D.
4. Approved canonical edits trigger index rebuild.

## Failure and Escalation Behavior

- Critical lint failure: block publish.
- Missing evidence support: block claim usage.
- High-risk contradiction/tension: escalate to human review gate.
- Runtime constraints exceeded: reduce scope and declare limitations.
