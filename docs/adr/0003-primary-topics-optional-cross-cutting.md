---
status: accepted
date: 2026-06-20
depends-on: ADR-0002
---

# Cross-cutting topics are an optional controlled field; primary_topics stays free-text

Cross-cutting themes that span lifecycle stages and tiers (e.g. `relational-trust`, `compound-risk`, `co-design`) live in a dedicated, optional field **`cross_cutting_topics`**, validated against a controlled vocabulary **only when present** — never required, absence never flagged. The pre-existing **`primary_topics`** field is left as **free-text keywords** (count-capped only, not vocabulary-validated).

## Why a thematic facet at all, and why optional

Under ADR-0002's facets-first ranker, the three controlled axes (`lifecycle_stage`, `implementation_tier`, `promotion_stage`) do the structural relevance work and BM25-over-body recovers thematic recall. A *required* controlled thematic facet was rejected: it duplicates what BM25 gives, while adding a standing governance surface that drifts (terms applied inconsistently or omitted), and governance drift is a named failure mode of this system. The one case the facet still earns its keep is cross-cutting queries the axes can't express — "everything related to relational trust" — so the field is retained, optional and targeted.

## Why a new field rather than overloading `primary_topics`

Implementation surfaced that `primary_topics` already carries a meaning: every existing page uses it as general free-text keywords. Redefining it as a controlled cross-cutting facet stomped that meaning and produced 82 false-positive lint warnings on existing pages. Rather than overload one field with two concepts — the exact trap avoided for `promotion_stage` vs `retrieval_status` and `implementation_tier` vs the promotion ladder — we split them: `cross_cutting_topics` is the controlled themed facet; `primary_topics` remains uncontrolled keywords.

## Consequence

Two fields, two rules: `rule_cross_cutting_topics_vocab` validates `cross_cutting_topics` when present (warn on unknown value, never on absence); `rule_primary_topics` only caps `primary_topics` length. A small controlled vocabulary (`CROSS_CUTTING_TOPICS_VOCAB`) exists for the themed facet and grows as cross-cutting query patterns emerge.
