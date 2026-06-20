# ABA/DRR Field Knowledge Wiki

A self-maintaining knowledge vault for urban disaster-risk-reduction and the area-based / Neighborhood Approach. Field practice and literature enter as evidence, climb a promotion ladder as they are validated, and are retrieved by analysts to produce sourced operational guidance.

## Language

### Classification axes

Every page is classified on four **independent** axes. Keeping them separate is load-bearing; see ADR-0001.

**Promotion stage** (`promotion_stage`):
A page's position on the promotion ladder — how validated the knowledge claim is. One of: finding, concept, framework, tool, validated.
_Avoid_: trust tier, maturity, status (all overloaded).

**Retrieval status** (`retrieval_status`):
Whether a page is safe and appropriate to surface. One of: usable, limited, deprecated, draft. Independent of how validated it is.
_Avoid_: status (bare), visibility.

**Lifecycle stage** (`lifecycle_stage`):
When in the Neighborhood Approach decision process a page applies — the nine ABA stages (e.g. `area-selection`, `neighbourhood-diagnosis`). NOT the operating tiers.
_Avoid_: phase, tier, stage (bare).

**Implementation tier** (`implementation_tier`):
Which actor tier a page serves — design, execution, synthesis, or all. A different axis from lifecycle stage.
_Avoid_: tier (bare), role, lifecycle.

**Cross-cutting topics** (`cross_cutting_topics`):
An optional, controlled tag set for themes that span lifecycle stages and tiers (e.g. `relational-trust`, `compound-risk`, `co-design`). NOT one of the four axes and NOT required — validated against a controlled vocabulary only when present; absence is never flagged. Carries the queries the axes can't express; BM25-over-body covers the rest.
_Avoid_: tags, categories, primary topics (that's the free-text field).

**Primary topics** (`primary_topics`):
Free-text keywords on a page. Uncontrolled and optional (only its count is capped). Distinct from **cross-cutting topics** — keywords describe a page; cross-cutting topics are a controlled retrieval facet.
_Avoid_: cross-cutting topics, themes, facet.

### Promotion ladder

The path a knowledge claim climbs as field evidence accumulates. The stages are also page types.

**Finding**:
An extracted, sourced knowledge unit. The entry rung; lowest epistemic weight. An **atomic task** enters here.

**Concept**:
A finding that appears in ≥2 independent sources or field validations.

**Framework**:
A Tier-1 page with defined decision logic and explicit field-testable use conditions.

**Tool**:
A framework operationalized with field-applicable scoring criteria and documented failure modes. "Validated" once all instruments are linked and exception flags reviewed.

### The three-tier operating model

Cognitive demand is distributed across three tiers so no single actor carries the whole system.

**Design tier**:
Where methodological intelligence is concentrated — instruments, protocols, standards. Must include local co-designers, not only central experts. Corresponds to the wiki's framework/tool layers (where the promotion ladder terminates).

**Execution tier**:
Where bounded **atomic tasks** are performed in the field. Feeds the wiki via findings and exception flags.

**Synthesis tier**:
The integrative function that compares structured outputs, reconciles contradictions, and discriminates strong from weak signals. It **consumes the wiki** through the advisory pipeline. It is a specialized integrator, not a super-generalist.
_Avoid_: super-generalist, super-expert.

### Atomic task framework

**Atomic task**:
An implementation unit whose judgment requirements have been reduced — via standards, protocols, and tools — to the minimum needed for reliable execution.
_Avoid_: subtask, step.

**Codifiability**:
The boundary test for atomicity: only expertise that can be structured into standards belongs in the execution tier. Non-codifiable judgment (political, relational, strategic) belongs in design or synthesis.

**Exception flag**:
A documented anomaly or relational/contextual signal raised by an executor. Travels upward to the synthesis tier; in the wiki it becomes `contradicts:` / `known_tensions:` content. The system's adaptive nervous system — not a sign of failure.
_Avoid_: error, bug, issue.

**Escalation trigger**:
A defined indication that an issue exceeds a task's boundary and requires synthesis-tier review.

**Design capture**:
The primary structural threat: protocol designers without local legitimacy scaling flawed assumptions efficiently.

### Retrieval

**Advisory pipeline**:
The query path the synthesis tier uses: classify the question, retrieve candidate pages, pull section spans, assemble **evidence packets** with claim support, draft a sourced answer.

**Candidate page**:
A page returned by the ranker as relevant to a query, before section/evidence extraction. The ranker scores candidate pages and expands each to its contradictions and exception flags.

**Expansion set**:
The contradictions, known tensions, and exception flags pulled in for the top candidate pages — the material the synthesis tier reconciles. Distinct from the candidate set.

**Graph degree**:
A page's inbound-link count, precomputed at index time as a centrality proxy: more inbound links means more load-bearing. Used as the ranker's final tiebreaker.
_Avoid_: weight, importance, rank.

## Flagged ambiguities

- **"tier"** is overloaded: the **implementation tier** (design/execution/synthesis) is a different axis from a promotion stage like "Tier-1 framework". Use `implementation_tier` for the former; say "framework page" / `promotion_stage` for the latter. Never write a bare "tier".
- **"status"** is overloaded: `retrieval_status` (publishability) ≠ `promotion_stage` (validation). Never write a bare "status" in a page context.
- A framework document's `status: "Tier 1 Framework — pending field validation"` string is **advisory only**; the lint derives aging and the index derives validation. Don't trust the string.

## Example dialogue

> **Analyst (synthesis tier):** "For area selection in a contested informal settlement — what's our strongest guidance?"
> **Wiki:** "Three candidate pages. Highest `promotion_stage` is a *tool* — `retrieval_status: limited`, so surfaced with a caution: it's validated but narrow to flood contexts. Two *findings* back it; one carries an unresolved exception flag via `contradicts:`."
> **Analyst:** "Why is the tool ranked above the findings if it's only `limited`?"
> **Wiki:** "Promotion stage is the trust signal; retrieval status only gated inclusion. The findings are `usable` but lower on the ladder. The flagged contradiction is yours to reconcile — that's the synthesis tier's job, not mine."
