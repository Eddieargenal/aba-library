---
status: accepted
date: 2026-06-20
---

# Promotion stage is a first-class axis, distinct from retrieval status

A page's **epistemic validation** (how well-evidenced the knowledge claim is) and its **publishability** (whether it is safe and appropriate to surface) are independent facts, but the v2.7 schema modelled only the latter (`retrieval_status` ∈ usable/limited/deprecated/draft). The Atomic Task Design framework's promotion ladder (finding → concept → framework → tool → validated) is the missing axis. We add a dedicated field, **`promotion_stage`**, carrying the ladder position, rather than overloading `retrieval_status`.

## Why

A page can be `retrieval_status: usable` but `promotion_stage: finding` — safe to surface, low epistemic weight. Or `retrieval_status: limited` but `promotion_stage: validated` — well-tested knowledge with narrow applicability. Merging the two would make the retrieval ranker unable to distinguish a published raw finding from a validated tool, which is exactly the signal it most needs.

## The four classification axes

This decision makes explicit that pages are classified on four independent axes (the framework's own frontmatter conflated #3 and #4):

| Axis | Field | Question it answers | Values |
|---|---|---|---|
| Epistemic validation | `promotion_stage` | How validated is the claim? | finding / concept / framework / tool / validated |
| Publishability | `retrieval_status` | Safe + appropriate to surface? | usable / limited / deprecated / draft |
| Operational applicability | `lifecycle_stage` | When in the NA process does it apply? | the 9 ABA stages |
| Implementation tier | `implementation_tier` | Which actor tier does it serve? | design / execution / synthesis / all |

## Naming

`promotion_stage`, not `trust_tier` — "tier" is already the three-tier operating model (design / execution / synthesis). Two things named "tier" in one schema collide in prompts and navigation. The axis is the promotion *ladder*; the field names the *position* on it.

## Ranking implications (the reason this axis exists)

- `promotion_stage` is the retrieval ranker's **primary trust signal** — higher-validated knowledge outranks raw findings.
- `retrieval_status` **gates inclusion** (don't surface `deprecated`/`draft`).
- `lifecycle_stage` and `implementation_tier` **filter applicability**.
- Retrieving a candidate page **mandates graph expansion** to its `contradicts:` links and exception flags — the graph is load-bearing for synthesis-tier integration, not decorative.

## Considered and rejected

Overloading `retrieval_status` with tier values (cheaper, no new field) was rejected: it re-merges two axes the framework explicitly separates, and destroys the ranker's trust signal.

## Consequences

- Adds a fourth axis: more schema surface and frontmatter maintenance per page.
- Requires a migration: existing pages need `promotion_stage` (and `implementation_tier`) assigned; `lifecycle_stage` must be purged of tier values like `design`/`execution`/`synthesis`.
- The aging policy (30-day HIGH / 90-day block-ingest) is a **computed lint check** over `last_reviewed` + unresolved `contradicts:` entries — never a trusted frontmatter string.
