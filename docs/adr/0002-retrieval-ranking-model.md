---
status: accepted
date: 2026-06-20
depends-on: ADR-0001
---

# Retrieval ranking: facets-first, lexical tiebreaker, degree centrality

The retrieval ranker that serves the synthesis tier scores candidate pages with structured facets doing the precision work and a pure-Python BM25 score acting only as an intra-tier tiebreaker. Graph expansion to a page's contradictions and tensions is ranked by precomputed degree centrality. Every step is deterministic, zero-pip, and works in all four runtime modes (`full / edge_laptop / minimal_offline / no_llm`).

## The pipeline

```
1. Filter:  lifecycle_stage ∩ implementation_tier match the query context
2. Gate:    retrieval_status ∈ {usable, limited}        (drop deprecated/draft)
3. Order:   promotion_stage DESC → BM25 DESC → graph-degree DESC
4. Expand:  pull contradicts: + known_tensions: + exception flags for the top N
5. Return:  candidate set + expansion set to the synthesis agent
```

## Why facets-first, not lexical-first

The synthesis tier almost always queries within a known context (a specific decision stage, actor tier, decision type) — that maps to facets, not to free-text search. The controlled axes (`lifecycle_stage`, `implementation_tier`, `promotion_stage`) do the precision work and resolve most queries to a small candidate set with no text scoring at all. BM25 only breaks ties *within a single `promotion_stage`*; with no query text it falls through to degree centrality.

## Why not semantic embeddings

Rejected on a hard constraint, not on merit: embeddings need a model + library at query time, which breaks the `no_llm` and `minimal_offline` runtime modes and violates the zero-pip posture. Semantic re-ranking may later be added behind a seam as a `full`-mode-only enhancement; it is never the floor.

## Centrality

Graph centrality is **degree-based** (inbound-link count) and **precomputed at index time** into `graph-edges.jsonl`. A page with many inbound links is treated as more load-bearing. Pure Python, zero runtime cost.

## Consequences

- **Hard prerequisite: the ADR-0001 migration.** Steps 1–3 read `promotion_stage` and `implementation_tier` (net-new) and a cleaned `lifecycle_stage` (tier values purged). The ranker is inert until pages carry these.
- **Two new build artifacts:** a BM25 term index (built at index time from title + section/body text) and inbound-degree counts on edges. Both follow the existing deterministic, golden-testable compiler pattern.
- BM25 is ~50 lines of stdlib — no new dependency.
