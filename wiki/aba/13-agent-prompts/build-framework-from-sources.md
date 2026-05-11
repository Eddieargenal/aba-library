---
type: agent-prompt
prompt_id: build-framework-from-sources
status: operational
created: 2026-05-11
updated: 2026-05-11
---

# Build Framework from Sources

## When to use
When a lifecycle decision point exists that is not yet covered by an operational framework in `03-frameworks/`, or when an existing framework stub contains `TODO[agent]` placeholders. Use this prompt to build a Karpathy-style decision framework grounded in already-ingested source material.

Do NOT create a new framework if:
- An existing framework already answers the same atomic question (check `03-frameworks/00_index.md` first)
- The required source material has not been ingested (run `extract-source-from-pdf` and `ingest-new-source` first)
- The decision logic belongs inside a tool page rather than a framework page (frameworks explain *why* a decision is made; tools provide the *instruments* to make it)

---

## Step 1: Orient

Read these files before writing anything:

1. `/wiki/aba/03-frameworks/00_index.md` — confirm the framework does not already exist and identify the lifecycle stage slot
2. `/wiki/aba/03-frameworks/2017-aba-appropriateness-decision-framework.md` — the gold standard; study every section before writing
3. The existing stub file if one exists (required by the Write tool before overwriting)
4. `/wiki/aba/02-concepts/00_index.md` — identify which concept pages are relevant to this framework's domains

---

## Step 2: Identify the atomic question

Every framework answers exactly one decision question that a field team faces at a specific lifecycle stage. Write it as a single sentence before doing anything else.

Good atomic questions:
- "Given a candidate pool of urban areas, which should be prioritized for ABA programming?"
- "During implementation, when is a change in plan justified and how should it be made accountable?"

Bad atomic questions (too broad, multiple questions, or not a decision):
- "How should we think about coordination in urban settings?"
- "What is an area-based approach and when is it used?"

If you cannot write the atomic question in one sentence, the framework scope is not tight enough. Narrow it before proceeding.

---

## Step 3: Read source evidence

Read the relevant extracted source files in `01-sources/extracted/`. For each source, extract:
- Specific methods, tools, or frameworks described (with page references)
- Direct quotes that support decision branches or scoring rationale
- Case examples that validate or complicate the framework logic
- Explicit conditions, thresholds, or criteria stated in the source

Do not invent content. Every decision domain and every branch in the decision logic must trace to at least one ingested source. If evidence is missing for a domain, mark it `TODO[evidence gap: describe what is missing]` rather than filling it with general knowledge.

Read the relevant concept pages in `02-concepts/`. These define the theoretical vocabulary your framework's domains use — you link to them in `## Concept anchoring`, not re-explain them inline.

---

## Step 4: Define decision domains

Decision domains are the named dimensions of the atomic question. Each domain:
- Has a short bold label (2–5 words)
- States what it assesses and why it matters
- Maps to at least one ingested source
- Is distinct from other domains (no overlap)

Aim for 4–7 domains. Fewer than 4 suggests the question is too narrow for a framework; more than 8 risks overlap and scoring dilution.

The gold standard uses 9 domains with Domain 1 as a prerequisite gate (not scored). Use a gate structure when one condition must be true before scoring is meaningful.

---

## Step 5: Choose and write decision logic

Choose the logic type that fits the decision:

**Option A — Weighted scoring table** (use when all domains contribute continuously to the same decision)
- Assign weights summing to 100%
- Score each domain 0–4
- Define 4–5 score tiers with named decisions (e.g., "Full ABA justified", "Hybrid recommended")
- State the maximum score and how to calculate it
- Apply EFL Basics First override: any life-safety domain scoring ≥ 3 must be addressed regardless of total score

**Option B — If/then branching** (use when decisions are categorical rather than continuous)
- Define 2–3 primary axes (e.g., host-government engagement level × actor density)
- Write explicit branches: if [condition A] AND [condition B] → [decision X]
- Cover all combinations; no branch should end in "use judgment"

**Option C — Gate/readiness model** (use when all conditions must pass before proceeding)
- Define binary gates (pass/fail) with named minimum thresholds per gate
- State the rule: all gates must pass; any failure blocks progression
- Name the responsible party and resolution path for each failed gate

Hybrid logic is allowed (e.g., a gate check followed by weighted scoring for passing items). State the sequence explicitly.

**Decision logic must be specific.** A section that says "consider the severity of needs" is not decision logic. A section that says "score severity 0–4 where 4 = imminent life-safety threat affecting >30% of area population" is decision logic.

---

## Step 6: Write red flags / override conditions

Red flags are hard stops that override the scoring result — even a high score does not justify proceeding if a red flag applies. Each red flag must:
- State the condition precisely
- State why it overrides (what goes wrong if ignored)

Write at least 3 red flags. Draw from source-documented failure cases or IASC protection standards where available.

---

## Step 7: Write failure modes

Failure modes describe when the framework itself breaks — when its assumptions do not hold and its output becomes unreliable or misleading. These are NOT the same as red flags (which are conditions to check before using the framework). Failure modes are structural limits of the framework logic.

Each failure mode follows this pattern:
- **Breaks when:** [the condition that invalidates the framework] — [why the output becomes unreliable]

Write at least 3 failure modes. Think through:
- What context makes the scoring weights wrong?
- What data condition makes the evidence inputs untrustworthy?
- What institutional condition causes the framework to be applied without integrity?
- What does the framework assume about sequential or stable conditions that may not hold?

---

## Step 8: Write concept anchoring

For each relevant concept page in `02-concepts/`, write one line:
- The wikilink: `[[../02-concepts/concept-name]]`
- Which decision domain this concept underlies (not a general description of the concept)

Example:
```
- [[../02-concepts/risk-calculation]] — underlies Domain 2 (risk severity); the hazard × exposure × vulnerability logic defines what a high-severity score means
```

Do not list concepts that are background reading. Only list concepts whose definitions directly shape how a domain is assessed or how the decision logic works.

---

## Step 9: Write the framework file

Use this exact structure and frontmatter:

```markdown
---
type: framework
status: active
lifecycle_stage: "N. Stage name"
related_tools:
  - tool-XX-name
related_concepts:
  - concept-name-1
  - concept-name-2
source_foundation:
  - source-file-name-1
  - source-file-name-2
created: YYYY-MM-DD
updated: YYYY-MM-DD
---

# [Framework Name]

## Atomic question
[One sentence — the exact decision this framework resolves]

## Why this decision matters
[2–3 sentences: what goes wrong if this decision is skipped, made poorly, or made without this framework?]

## Prerequisites
- From prior lifecycle stage: [specific outputs needed as inputs]
- Minimum evidence standard: [what data must exist before applying this framework]

## Decision domains
1. **Domain Name** — [what it assesses and why it matters] *(gate — not scored)* [if applicable]
2. **Domain Name** — [what it assesses and why it matters]
...

## Decision logic
[Weighted table, if/then branches, or gate model — written specifically, not vaguely]

## Red flags / override conditions
- [Condition]: [why this overrides the score]
...

## Failure modes
- **Breaks when:** [condition] — [why the output is unreliable]
...

## Concept anchoring
- [[../02-concepts/concept-name]] — [which domain this underlies and how]
...

## Tool instantiation
- This framework is operationalized by: [[../04-tools/tool-XX-name]]
- That tool provides: [what the tool adds that the framework does not — field instruments, scoring sheets, facilitation protocols, etc.]

## Source foundation
- [[../01-sources/extracted/source-file-name]] — [one sentence: what specific evidence this source contributes]
...
```

Wikilink format rules:
- Concepts: `[[../02-concepts/filename-without-extension]]`
- Tools: `[[../04-tools/filename-without-extension]]`
- Sources: `[[../01-sources/extracted/filename-without-extension]]`

Do not use absolute paths or full filenames with `.md` extension in wikilinks.

---

## Step 10: Update the index and tool back-links

**Update `03-frameworks/00_index.md`:**
Add an entry for the new framework in the Tier 1 table in lifecycle order. Format:
```
| [[framework-filename-without-extension]] | **What:** [one sentence]. **Why:** [one sentence]. **When/How:** [one sentence on when to use it and which tools it connects to]. |
```

**Add a backing-framework link to the driven tool page:**
In the tool page that this framework operationalizes, add or update:
```markdown
## Backing framework
This tool operationalizes: [[../03-frameworks/framework-filename-without-extension]]
```
Insert this section after the tool's `## Purpose` section.

---

## Layer rule alignment

- Do not open `../raw/` files to answer questions or populate content. Extracted source pages in `01-sources/extracted/` are the evidence layer.
- If a concept or source page does not exist for evidence you need, document the gap with `TODO[ingestion gap: describe what is missing]` and flag it for ingestion.
- If the framework overlaps with an existing framework, document the boundary explicitly in `## Why this decision matters` rather than duplicating logic.

---

## Quality checklist (must pass before committing)

- [ ] Atomic question is one sentence and names a single decision
- [ ] All 10 sections present with substantive content (no TODO placeholders)
- [ ] Decision logic is specific: has a table, branching rules, or gate thresholds — not vague guidance
- [ ] At least 3 red flags with reasons
- [ ] At least 3 failure modes using "Breaks when:" format
- [ ] Concept anchoring maps each concept to a specific domain (not just listed)
- [ ] Tool instantiation includes a wikilink to an existing tool page
- [ ] Source foundation includes a wikilink and one-line evidence summary per source
- [ ] All wikilinks use the correct relative path format
- [ ] Frontmatter: `status: active`, `lifecycle_stage` filled, `related_concepts` and `source_foundation` match body content
- [ ] `03-frameworks/00_index.md` updated with a Tier 1 entry
- [ ] Driven tool page updated with `## Backing framework` section
