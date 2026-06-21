# Promotion-Readiness Worklist (#13)

Audit of the remaining `PU-` proposed-update stubs in this folder, generated from
their frontmatter. This is the Gate-D worklist: each row is a human decision to
publish (or not).

## Key constraint: every remaining stub is single-source

All stubs rest on **one** source, so the promotion ceiling is **`limited`**
(rankable, but not `usable`). Reaching `usable` requires ingesting a second
independent source for that topic — the single-source ceiling. Until then,
promoting a stub makes it appear in retrieval at `limited` trust.

## How to promote one (Gate D)

The mechanical transform is automated by `scripts/promote_stub.py` (dry-run by
default). A human still chooses **whether** to publish and the two ladder axes:

```
python3 scripts/promote_stub.py <stub-path> --status limited \
    --promotion-stage <finding|concept|framework|tool|validated> \
    --implementation-tier <design|execution|synthesis|all> --apply --remove-stub
```

Then rebuild: `python3 scripts/build-index.py`. The page becomes rankable.
**Worked example already done:** `resilience-framework` (concept / synthesis /
limited) — now returned by the ranker.

## Remaining stubs: 0 — the promotion sweep is complete ✅

All 23 PU- stubs have been resolved: **22 promoted** to `limited` (4 concepts,
2 frameworks, 5 tools, 3 risks, 7 decision-protocols, + `resilience-framework`),
and **`enabling-environment`** retired as redundant (its page already existed and
already cited the source finding).

The vault went from **2 rankable pages to 24**. Every promoted page is at
`limited` (single-source ceiling). Decision-protocols carry `orphan_page`
warnings by design — they are invoked by advisory-playbooks, which do not exist
yet; inbound links arrive when that layer is authored.

## What remains for #13 (not stub promotion)

1. **Lift topics to `usable`:** every promoted page is single-source. Ingest a
   corroborating second source for a topic, then re-promote at `--status usable`.
2. **Author advisory-playbooks** that invoke the decision-protocols (clears their
   orphan warnings, and builds the operational layer).
3. **Enrich inbound links** further as the graph matures.
