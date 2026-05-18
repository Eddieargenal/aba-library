---
type: overview
status: operational
version: 2.7
created: 2026-05-07
updated: 2026-05-18
---

# Agent Contract (Canonical)

This contract defines non-negotiable operating behavior for all agents working in this vault.
If instructions conflict, follow precedence below.

## Rule Precedence

1. `governance/aba/agent-contract.md` (this file)
2. `AGENTS.md` and `governance/aba/CLAUDE.md` (must remain aligned)
3. `governance/schema/*.md` (schema, lint, naming, query rules)
4. `governance/aba/prompts/agent-*.md`
5. Page-local notes/TODO markers

## Architecture Scope (v2.7)

Agents operate within this canonical wiki architecture:

- `wiki/aba/01-sources/raw/` (immutable evidence)
- `wiki/aba/01-sources/raw-content/` (source mirrors)
- `wiki/aba/01-sources/extracted/` (finding-level extraction)
- `wiki/aba/02-concepts/` to `wiki/aba/12-synthesis/` (canonical synthesis graph)
- `indexes/current/` and `indexes/builds/` (compiled index artifacts)
- `outputs/` (runtime output artifacts)

## Hard Rules

- Never modify files in `wiki/aba/01-sources/raw/`.
- Never use file paths as graph identity; use stable IDs.
- Never hand-edit compiled index artifacts in `indexes/current/` or `indexes/builds/`.
- Never publish final advisory guidance without citation and risk review.
- Never present unsupported claims as facts.
- Never overwrite canonical pages from field sync queues without Gate D approval.

## Domain Query Contract

1. Pin one `index_build_id` from `indexes/current/manifest.json`.
2. Retrieve via `agent-index.jsonl` and `graph-edges.jsonl`.
3. Resolve section spans via `section-index.jsonl`.
4. Build evidence packets (`EP-*`) before drafting advisory prose.
5. Draft final guidance only from approved claim-ledger claims.

If required content is missing, explicitly report the gap and propose ingest/routing work.

## Ingest and Routing Contract

1. Curate source in `01-sources/raw/`.
2. Create or refresh raw-content mirror.
3. Produce extracted source page with findings and integration map.
4. Route findings into existing pages first.
5. Create `PU-*` proposals for high-risk or review-gated changes.
6. Rebuild indexes with `scripts/build-index.py`.
7. Publish only when critical lint errors are zero.

## Mandatory Quality Controls

- Lint policy: `governance/schema/lint-rules.md`.
- Tool quality standard: `governance/schema/tool-quality-standard.md`.
- All critical lint failures block publish.
- High warnings may publish only with explicit visibility.

## Human Review Gates

- Gate A: extracted source review
- Gate B: routing/proposal review
- Gate C: field-critical advisory review
- Gate D: field update promotion review

## Runtime Output Policy

Agents may write runtime artifacts only to:

- `outputs/field-advice/`
- `outputs/evidence-packets/`
- `outputs/field-notes/`
- `outputs/proposed-library-updates/`
- `outputs/sync-queue/`

Canonical wiki pages are read-mostly unless explicitly in approved maintenance workflows.

## Prohibited Behaviors

- Fabricating evidence, citations, or confidence levels
- Hiding contradictions/tensions to produce false consensus
- Treating draft/stub pages as validated guidance
- Bypassing review gates for high-risk decisions
- Mixing archived prompts into active operations
