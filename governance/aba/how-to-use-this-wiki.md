---
type: overview
status: active
created: 2026-05-07
updated: 2026-06-21
---
# How to Use This Wiki

This is the 30-second onboarding for the ABA/DRR library. There are two ways an agent
uses it: **querying** (answer a question) and **contributing** (ingest, lint, build,
promote). Pick your path.

---

## Path A — Query the library (answer a question)

You do **not** read prose to find an answer. You query the compiled index, then read
only the handful of pages it returns.

1. **Try it from the shell** (fastest):
   ```bash
   python3 scripts/ranker.py --text "resilience" --lifecycle area-selection --k 5
   ```
   Flags: `--text` (BM25 over title+body), `--lifecycle STAGE` (repeatable),
   `--tier TIER`, `--k` (top-K), `--index` (defaults to `indexes/current`).
   Run `python3 scripts/ranker.py --help` for the live contract.

2. **Or call it in Python** (run from the repo root):
   ```python
   import sys; sys.path.insert(0, "scripts")
   from ranker import load_index, rank
   result = rank({"text": "resilience", "lifecycle_stage": ["area-selection"]},
                 load_index("indexes/current"))
   ```
   `rank()` returns ranked candidate pages plus automatic contradiction / known-tension
   expansion, scored by BM25 + facets + graph degree.

3. **Read the pages it returns**, then ground every claim in their `source_basis`.

The index it reads lives in `indexes/current/`: `agent-index.jsonl` (every page with its
facets — `lifecycle_stage`, `implementation_tier`, `promotion_stage`, `retrieval_status`),
`term-index.json`, `graph-edges.jsonl`, `section-index.jsonl`, and
`source-evidence-index.jsonl`. You learn one interface (the ranker over the index), not
94 documents.

---

## Path B — Contribute (ingest, lint, build, promote)

Read **only the one file your task needs** — never load the whole governance folder.

1. **`AGENTS.md`** (repo root) — the v2.7 operating guide and the AGENT-QUICKSTART at its
   top. Read this first if you are new.
2. **`governance/00_governance-index.md`** — routing map: a Section Map table from
   task type → the single file to read, with explicit "Read When / Do NOT Read When".
3. From there, the one task-scoped file:
   - **Schema / frontmatter contract** → `scripts/schema.py` (every controlled vocab,
     required-field table, ID prefix, and edge type — the whole data model in one file)
     and `governance/schema/`.
   - **Step sequences** (ingest, lint, query, build) → `governance/workflows/` and the
     prompt pack `governance/aba/prompts/agent-*`.
   - **Behavioral contract** → `governance/aba/agent-contract.md`.

After any content change, rebuild with `python3 scripts/build-index.py` and publish only
when `critical_error_count` is 0 in `indexes/current/manifest.json`.

---

## Current state (as of 2026-06-21 build)

The library is **populated, not stubbed**. The active build (`indexes/current/`) indexes
**47 pages** with 0 critical lint errors:

- 22 extracted source pages (`01-sources/extracted/`) — PDF text extraction is **done**
- 7 concepts, 2 frameworks, 5 tools, 3 risks, 7 decision-protocols, 1 overview

Open work is tracked as warnings in `lint-report.json` (orphan pages, unresolved edges,
pending findings) — not as missing content. Check
`indexes/current/manifest.json` for the live counts and `health` block.

---

## Quality expectations

- Tool pages specify how to collect and analyze evidence, not just what to ask.
- Every claim in an answer must trace to a page's `source_basis`.
- Never answer without checking the source foundation; surface gaps rather than
  fabricating coverage.
