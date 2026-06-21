---
status: accepted
date: 2026-06-21
---

# Contradiction detection: a deterministic disclosure rule now, semantic detection deferred

Whole-graph contradiction handling is implemented as a **deterministic graph lint
rule** (`rule_contradiction_disclosure`) that enforces **mutual disclosure of
`contradicts` edges**: if page A declares `contradicts: B` but B does not declare
`contradicts: A`, B is silently omitting the tension and the build emits a
warning (`undisclosed_contradiction:{B}:{A}`) on B's page. Semantic detection of
*latent* contradictions — two pages making divergent claims with no edge between
them — is **deferred**.

## Why a deterministic rule now

The non-negotiable is "no silent contradiction suppression." A deterministic rule
gives that teeth for the case it can prove: a contradiction disclosed on one side
but hidden on the other. It is zero-cost, runs every build, is fully testable, and
is **dormant until the graph carries `contradicts` edges** — so it does not flood
the current sparse vault (verified: 0 such warnings today). It is the scaffold the
populated graph will need, in place before the content arrives.

## Why not a semantic/LLM pass now

Detecting *undisclosed* contradictions — divergent claims with no author-supplied
edge at all — requires NLP/LLM judgement. That is non-deterministic, costly, and
finds essentially nothing on a graph of two rankable pages. Building it now would
be speculative; its value appears only once there is a populated graph to find
contradictions in (#13).

## Scope

- Covers the `contradicts` relation. `known_tensions` is left out for now — its
  directionality is less clear-cut, and forcing symmetry there risks false
  positives.
- The rule enforces disclosure of **author-supplied** edges; it does not infer new
  contradictions. Surfacing edge-less contradictions is the deferred semantic step.
- The warning enters the repair queue (like ghost nodes). Wiring the advisory
  pipeline to **block advisory output** until an open `undisclosed_contradiction`
  is resolved is a follow-on integration, not part of this rule.

## Consequence

Author-supplied contradictions must be mutual or they surface as a warning. The
detection approach is now recorded and the scaffold is live.

**Revisit when:** the vault is substantially populated (#13). At that point add a
periodic agent pass to surface *latent* (edge-less) contradictions across related
pages, and consider gating advisory output on unresolved disclosures.
