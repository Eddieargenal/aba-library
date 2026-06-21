---
type: agent-guide
status: active
version: 2.7
updated: 2026-05-18
---

# ABA/DRR Field Knowledge Wiki — v2.7 Operating Guide

## AGENT-QUICKSTART (read this first — 30 seconds)

Two paths. Pick one.

- **To answer a question** → query the compiled index, don't read prose. Run
  `python3 scripts/ranker.py --text "your query" --lifecycle <stage> --k 5`
  (or in Python from repo root: `import sys; sys.path.insert(0, "scripts"); from ranker
  import load_index, rank`). It returns ranked pages + contradiction/known-tension
  expansion. Read only those pages, then ground every claim in their `source_basis`.
  Index lives in `indexes/current/` (`agent-index.jsonl` carries the facets:
  `lifecycle_stage`, `implementation_tier`, `promotion_stage`, `retrieval_status`).
- **To contribute** (ingest, lint, build, promote) → open
  `governance/00_governance-index.md`, find your task in the Section Map, and read the
  **one** file it routes you to. Never load the whole governance folder. The entire data
  model (vocabs, required fields, ID prefixes, edge types) is in `scripts/schema.py`.

Rules that never bend: **never claim without `source_basis`**, never hand-edit compiled
index files, never modify raw sources. After content changes, rebuild with
`python3 scripts/build-index.py` and publish only when `critical_error_count` is 0.

Current state: the library is **populated, not stubbed** — the active build indexes 47
pages (22 sources, 7 concepts, 2 frameworks, 5 tools, 3 risks, 7 decision-protocols) with
0 critical errors. Full onboarding: `governance/aba/how-to-use-this-wiki.md`.

---

## Mission

This vault is a persistent, compounding operational memory for urban DRR and area-based response.
Agents draft and maintain the system; humans validate high-risk decisions and promotions.

## Canonical Architecture (v2.7)

### Knowledge Layer (`wiki/aba`)

- `00-overview/`
- `01-sources/raw/` (immutable source files)
- `01-sources/raw-content/` (markdown mirrors of raw files)
- `01-sources/extracted/` (structured extracted source pages)
- `02-concepts/`
- `03-frameworks/`
- `04-tools/`
- `05-field-instruments/`
- `06-risks/`
- `07-known-tensions/`
- `08-advisory-playbooks/`
- `09-decision-protocols/`
- `10-output-templates/`
- `11-slice-specs/`
- `12-synthesis/`

### Compiled Index Layer

- `indexes/builds/<build_id>/` (immutable builds)
- `indexes/current/` (active build)

Required index artifacts:
- `manifest.json`
- `agent-index.jsonl`
- `graph-edges.jsonl`
- `unresolved-edges.jsonl`
- `section-index.jsonl`
- `source-evidence-index.jsonl`
- `lint-report.json`

### Runtime / Operations Layer

- `outputs/field-advice/`
- `outputs/evidence-packets/`
- `outputs/field-notes/`
- `outputs/proposed-library-updates/`
- `outputs/sync-queue/`
- `emergency/`
- `field-repo/` (slice packaging target)

### Governance Layer

- `governance/schema/` (authoritative schema + lint contracts)
- `governance/schema-registry.md`
- `governance/id-registry.md`
- `governance/human-review-gates.md`
- `governance/aba/prompts/` (active prompt pack)

## Source of Truth Rules

1. Markdown + frontmatter is canonical knowledge.
2. JSONL indexes are generated artifacts.
3. Agents never hand-edit compiled index files.
4. Stable IDs are graph identity; file paths are not.
5. All vault artifacts must be `.md` except generated JSON/JSONL index outputs.

## Stable ID Prefixes

Canonical page-id prefixes — verified against `scripts/schema.py:ID_PREFIX_BY_TYPE`:

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

Runtime-only prefixes (not page ids, not validated by the index builder): `EP-` evidence packet, `PU-` proposed update.

## Layer Discipline (Critical)

- `wiki/aba/01-sources/raw/` and `raw-content/` are ingest/evidence support layers only.
- Domain answers must be grounded in extracted/synthesis pages plus indexed evidence.
- If synthesis coverage is missing, surface the gap and propose ingest/routing updates.
- Never modify raw source files.

## Query and Advisory Flow (v2.7)

1. Pin one `index_build_id` from `indexes/current/manifest.json`.
2. Classify decision domain and lifecycle stage.
3. Retrieve through `agent-index.jsonl` + `graph-edges.jsonl`.
4. Retrieve section spans from `section-index.jsonl`.
5. Build evidence packets (`EP-*`) with claim support.
6. Consolidate claim ledger.
7. Draft final output from approved claims only.
8. Run citation review.
9. Run risk review.
10. Store output under `outputs/field-advice/`.

## Runtime Modes

- `full`
- `edge_laptop`
- `minimal_offline`
- `no_llm`

Rules:
- Respect runtime ceilings by mode.
- Use `emergency/` assets for `no_llm`.

## Ingest and Routing Flow

1. Curate raw source in `01-sources/raw/`.
2. Create/update raw-content mirror.
3. Create extracted source page with findings and integration map.
4. Route findings into existing pages first.
5. Create `PU-` proposals for changes needing review.
6. Rebuild indexes via `scripts/build-index.py`.
7. Publish only if critical lint errors are zero.

## Human Review Gates

- Gate A: extracted source review
- Gate B: routing/proposal review
- Gate C: field-critical advisory review
- Gate D: field update promotion review

## Lint and Publish Rules

Critical failures block publish. High warnings may publish with visibility.
Canonical lint policy: `governance/schema/lint-rules.md`.

## Prompt Policy

Active prompt set:
- `governance/aba/prompts/agent-01-*.md` through `agent-20-*.md`
- index: `governance/aba/prompts/00_prompts-index.md`

Legacy prompts are archival only:
- `archive/prompts/aba-legacy-v25/`

## Session Protocol

Open:
1. Read `memory/current-handoff.md`.
2. Read `indexes/current/manifest.json` and latest `lint-report.json`.
3. Resolve CRITICAL issues before new advisory work.

Close:
1. Update `memory/current-handoff.md`.
2. If schema changed, update `governance/schema/changelog.md`.
3. Rebuild indexes (`scripts/build-index.py`).
4. Append operation log in `memory/runtime/logs/log.md`.

## Quick Routing

| Task | Canonical File(s) |
|---|---|
| Architecture and operating rules | `AGENTS.md`, `governance/aba/CLAUDE.md` |
| Schema contract | `governance/schema/frontmatter-schema.md` |
| Lint policy | `governance/schema/lint-rules.md` |
| Prompt catalog | `governance/aba/prompts/00_prompts-index.md` |
| Ingest | `governance/aba/prompts/agent-07-raw-source-mirror-agent.md`, `agent-08-extracted-source-agent.md`, `agent-09-finding-routing-agent.md` |
| Advisory orchestration | `governance/aba/prompts/agent-10-advisory-orchestrator-agent.md` |
| Lint and graph validation | `governance/aba/prompts/agent-06-lint-and-graph-validator-agent.md` |
| Index build | `scripts/build-index.py` |
| Field slice packaging | `governance/aba/prompts/agent-17-slice-builder-agent.md` |
| Field sync proposal flow | `governance/aba/prompts/agent-18-field-sync-agent.md`, `agent-19-hq-sync-review-agent.md` |

## Non-Negotiables

- No fabricated evidence.
- No unsupported claims in final guidance.
- No direct canonical overwrite from field sync queues.
- No silent contradiction suppression.
- No manual edits to compiled index artifacts.
