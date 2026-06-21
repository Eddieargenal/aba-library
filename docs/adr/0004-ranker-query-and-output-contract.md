---
status: accepted
date: 2026-06-21
depends-on: ADR-0002
---

# Retrieval ranker: query and output contract

ADR-0002 fixed the ranking *algorithm*; this fixes the *interface* the synthesis tier calls. The ranker is a pure `rank(query, index) -> RankResult` plus a thin `load_index(dir) -> index` loader (mirroring the compiler: pure core, I/O shell).

## Query — structured, all optional

```
{ lifecycle_stage?, implementation_tier?, text?, k? }
```
The analyst already knows their context, so facets are first-class inputs, not inferred. **Free-text-only (parse to facets) was rejected** for the same reason as embeddings: it needs NLP/heuristics at query time, breaking `no_llm`/`minimal_offline`. `text` feeds BM25 only; any omitted field imposes no constraint.

## Candidate universe — ladder pages only

Only pages carrying a `promotion_stage` are candidates. This makes the `promotion_stage` ordering well-defined and honours "ground answers in synthesis pages, not raw sources" — sources are reached as evidence downstream, never ranked as answers.

## Matching semantics

- Omitted query facet → no constraint on that axis.
- `lifecycle_stage`: page matches if its stage list **intersects** the requested stage(s).
- `implementation_tier`: page matches if `page.tier == query.tier` **or** `page.tier == "all"` (an `all` page is universally relevant).
- Facet filters AND'd, AND'd with the gate `retrieval_status ∈ {usable, limited}`.

## Output — explainable

`RankResult` carries two sets (per ADR-0002):
- **candidates** — ordered records with `id, title, type, path` plus the sort components `promotion_stage, bm25_score, inbound_degree`, so the consuming agent can trace *why* each ranked.
- **expansion** — a separate set of `{from, relation, to, to_title}` for the top-`k` candidates, following `contradicts` and `known_tension` edges. This is the material the synthesis tier reconciles.

## Consequence

The `promotion_stage` ordinal needs a defined order (`finding < concept < framework < tool < validated`); added to the schema as an ordered sequence alongside the existing set.
