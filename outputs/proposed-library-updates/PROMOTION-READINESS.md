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

## Remaining stubs by type (11, all single-source → ceiling `limited`)

Promoted so far (now rankable at `limited`): `resilience-framework`, the 4
Young Foundation concepts, both neighbourhood frameworks, and the 5 tools
(`assess-community-resilience-level`, `conduct-vca-with-characteristics`,
`customize-resilience-framework`, `local-public-realm-mapping-tool`,
`measure-resilience-progress`).

| type | slug | target |
|---|---|---|
| concept | enabling-environment | ⚠️ target **already exists** — merge, don't create |
| risk | neighbourhood-governance-capture | wiki/aba/06-risks/neighbourhood-governance-capture.md |
| risk | neighbourhood-governance-fragmentation | wiki/aba/06-risks/neighbourhood-governance-fragmentation.md |
| risk | resilience-conflict-gap | wiki/aba/06-risks/resilience-conflict-gap.md |
| decision-protocol | introduce-resilience-framework | wiki/aba/09-decision-protocols/introduce-resilience-framework.md |
| decision-protocol | neighbourhood-governance-selection | wiki/aba/09-decision-protocols/neighbourhood-governance-selection.md |
| decision-protocol | neighbourhood-scale-selection | wiki/aba/09-decision-protocols/neighbourhood-scale-selection.md |
| decision-protocol | post-disaster-resilience-priorities | wiki/aba/09-decision-protocols/post-disaster-resilience-priorities.md |
| decision-protocol | prioritize-resilience-interventions | wiki/aba/09-decision-protocols/prioritize-resilience-interventions.md |
| decision-protocol | refine-indicators-from-characteristics | wiki/aba/09-decision-protocols/refine-indicators-from-characteristics.md |
| decision-protocol | service-devolution-conditions | wiki/aba/09-decision-protocols/service-devolution-conditions.md |

## Recommended sequence

1. **Concepts first** (foundational; other types reference them).
2. Resolve the `enabling-environment` merge case separately (its page exists).
3. Then frameworks → tools → decision-protocols → risks, promoting where the
   single source genuinely supports the claim.
4. **To lift any topic to `usable`:** ingest a corroborating second source, then
   re-promote at `--status usable`.
