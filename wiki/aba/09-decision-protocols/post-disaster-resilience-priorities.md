---
id: D-post-disaster-resilience-priorities
type: decision-protocol
title: Select minimum resilience Characteristics as post-disaster recovery milestones
slug: post-disaster-resilience-priorities
retrieval_status: limited
lifecycle_stage:
- transition-handover
- implementation-adaptation
primary_topics:
- resilience
- recovery
related_concepts:
- C-resilience-framework
related_frameworks: []
related_tools:
- T-measure-resilience-progress
related_risks: []
source_basis:
- source_id: S-2009-twigg-ucl-disaster-resilient-community
  object_id: S-2009-twigg-ucl-disaster-resilient-community-RULE-006
known_tensions: []
contradicts: []
used_by_playbooks: []
output_templates: []
decision_type: post-disaster recovery prioritisation
trigger_conditions:
- immediate post-disaster context
- full Characteristics set is unrealistic
escalation_path: response/recovery lead
sections:
- id: trigger
  anchor: "#trigger"
  purpose: Conditions that activate this protocol
- id: decision-logic
  anchor: "#decision-logic"
  purpose: Conditional decision logic and branching rules
- id: escalation
  anchor: "#escalation"
  purpose: Escalation triggers and human review requirements
created: '2026-06-21'
updated: '2026-06-21'
promotion_stage: tool
implementation_tier: design
---

<a id="trigger"></a>
## Trigger Conditions

Use this protocol in the **immediate aftermath of a disaster**, deciding what
resilience-building to focus on first. Twigg is explicit that *"the ideal state of
resilience outlined in the Characteristics is far removed from the condition of a
community that has just suffered a disaster"* (Twigg 2009, p. 15, §4.1.2(b) "After
disaster"). The full set of 167 Characteristics describes a goal — *"the highest level
of resilience that is realistically attainable"* (p. 19, §4.3.5) — so applying it
wholesale as a recovery target is unrealistic. It activates when **both** conditions
hold: an immediate post-disaster / relief-and-recovery context, and the full
Characteristics set being infeasible. *"A week after the flood — what resilience goals
are realistic?"*

> Scope note: the source gives no standalone recovery framework. It treats post-disaster
> priorities through its "After disaster" guidance (p. 15) and the recovery
> characteristics in Thematic Area 5 — Component "Emergency response and recovery"
> (pp. 41–43). This protocol grounds itself in those.

<a id="decision-logic"></a>
## Decision Logic

**Core rule.** Do not apply the full Characteristics ideal as your recovery target.
Instead, **select a relatively small set of key or minimum Characteristics**
"specifically associated with community recovery following a disaster" — Twigg's example
is *"access to a clean, reliable water supply"* — as a **first step towards greater
resilience**, via "a careful, deliberative process" rather than a quick checklist
(p. 15). How the Characteristics inform what to prioritise first:

- **Anchor on immediate recovery needs, sector by sector.** The source points to the
  Myanmar Red Cross / IFRC / Danish Red Cross "resilience profiles" developed after
  Cyclone Nargis: indicators **per sector** (e.g. water and sanitation, shelter), each a
  **minimum resilience "package"** for that sector at a point in time after the disaster
  (p. 15). Prioritise the sectors where basic functions are most disrupted.
- **Draw the candidate set from Thematic Area 5's recovery characteristics.** These
  live under "Emergency response and recovery": actions reaching all affected members
  and prioritised according to needs; community/locally-led recovery planning;
  psychosocial support; and incorporation of DRR into recovery plans (pp. 41–43) — a
  source-grounded menu of "what first."
- **Use the "key / minimum Characteristics" method.** A reduced set follows the §4.3.3
  logic for "key" or "minimum" Characteristics chosen for current DRR priorities — but
  the source insists this be "deliberative and inclusive," context-related, and **not
  assumed necessary** by default (pp. 18–19).
- **Track progress with milestones, not a single yes/no.** Define intermediate steps
  from the current state toward each chosen Characteristic and agree stage indicators;
  the Nargis "minimum package" approach "has something in common with the various
  'milestones' initiatives" (p. 15; §4.3.5, p. 19). Pairs with T-measure-resilience-progress.

**Guardrail.** Treat the minimum set as a starting point, not a ceiling: "nobody should
be satisfied with minimum standards," and a fixed select list risks managers forgetting
other significant aspects of resilience (pp. 19–20, §4.3.3).

<a id="escalation"></a>
## Escalation

Seek senior (response/recovery lead) judgement when:

- **The deliberative selection cannot reach consensus.** Agreeing a minimum/key set
  "might be difficult to reach consensus about" (p. 19); unresolved disagreement
  escalates rather than being settled by imposing a list from the top (§4.3.3).
- **Life-safety or basic-needs gaps conflict with the chosen milestones** — when the
  first-step characteristics (clean water, shelter, food security) cannot all be pursued
  at once and trade-offs across affected groups are needed, given the principle that
  response and recovery should "reach all affected members of community and [be]
  prioritised according to needs" (pp. 41–43).
- **The context falls outside tested ground.** There is "no field experience yet" of a
  dedicated post-disaster Characteristics set, so the guidance is provisional (p. 15),
  and the framework's consensus assumptions may not hold in conflict-affected or
  fragmented settings (p. 15, §4.1.2(c)). Escalate rather than force-fit.

> **Evidence note.** Single-source protocol grounded only in Twigg 2009,
> *Characteristics of a Disaster-Resilient Community* (object RULE-006), so it sits at
> `limited` trust. The post-disaster rule and Cyclone Nargis "minimum resilience
> package" come from p. 15 (§4.1.2(b)); the key/minimum-Characteristics method and
> "minimum standards" guardrail from pp. 18–20 (§4.3.3); milestones from p. 19 (§4.3.5);
> recovery characteristics from Thematic Area 5, pp. 41–43. The source notes there is no
> field experience of a dedicated post-disaster Characteristics set, so the rule is
> provisional. A second source would be needed to promote beyond `limited`.
