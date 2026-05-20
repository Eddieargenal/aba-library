---
id: S-{slug}
type: source
title: "Full Title of Source"
slug: {slug}
retrieval_status: usable
source_id: {slug}
canonical_file: ../raw/{filename}.pdf
source_url: ""
source_url_status: verify
file_type: pdf
source_type: academic           # academic | ngo-guidance | toolkit | policy | report | grey-literature
year: YYYY
author: "Author Name"
institution: "Publishing Institution"
status: extracted
ingest_date: YYYY-MM-DD
ingest_status: success
confidence: high                # high | medium | low
lifecycle_stage:
  - neighbourhood-diagnosis     # list one or more from controlled vocabulary
  # controlled vocab: appropriateness-decision | area-selection | neighbourhood-diagnosis |
  # joint-prioritization | coordination-design | integrated-area-strategy |
  # implementation-adaptation | monitoring-learning | transition-handover
primary_topics:
  - topic-slug
primary_context: generic        # rural | urban | generic | mixed
urban_applicability: direct     # direct | requires-adaptation | not-applicable
urban_adaptation_scope: none    # none | minor | moderate | substantial — derived from Step 11 checklist count
urban_adaptation_notes: none    # one sentence max; none if urban_applicability: direct
institutional_credibility: medium   # high | medium | low | mixed
evidence_quality: medium            # high | medium | low | mixed
composite_authority: medium         # high | medium | low | mixed
comparison_readiness: medium        # high | medium | low | not-ready
related_concepts: []
related_frameworks: []
related_tools: []
related_risks: []
source_basis: []
known_tensions: []
contradicts: []
cited_sources:
  - raw_citation: "Author, A. (Year). Title of key contributing work. Publisher."
    wiki_id: S-slug-if-in-wiki    # omit if source not yet in wiki
    in_wiki: false                 # auto-computed by build-index.py — never set manually
  - raw_citation: "Author, B. (Year). Title of another key framework or guideline."
    in_wiki: false
findings:
  # Compact routing records only — full claim text lives in the body #findings section
  - finding_id: F-001
    finding_type: decision-rule
    # finding_type vocab: concept-definition | framework-component | process-step | tool-description |
    # risk-identification | tension-surface | evidence-gap | field-practice | monitoring-indicator |
    # design-principle | decision-rule | task-seed
    knowledge_layer: decision       # conceptual | diagnostic | operational | decision
    lifecycle_stage:
      - neighbourhood-diagnosis
    source_pages: ["p. 12", "p. 14–16"]
    candidate_target_pages:
      - wiki/aba/09-decision-protocols/example-protocol.md
    integration_action: create-decision-rule
    # integration_action vocab: create-concept | enrich-concept | create-framework | enrich-framework |
    # create-tool | enrich-tool | create-risk | enrich-risk | create-decision-rule | enrich-decision-rule |
    # source_only | flag-for-review
    field_query_trigger: "How do I decide whether to use this approach in an urban post-disaster context?"
    # write not-applicable only for purely conceptual findings with no operational activation
    status: pending
    human_review_required: false
  - finding_id: F-002
    finding_type: concept-definition
    knowledge_layer: conceptual
    lifecycle_stage:
      - neighbourhood-diagnosis
    source_pages: ["p. 23"]
    candidate_target_pages:
      - source_only
    integration_action: source_only
    field_query_trigger: not-applicable
    status: pending
    human_review_required: true
sections:
  - id: summary
    anchor: "#summary"
    purpose: "Author background, document type, scope, production method, lifecycle coverage, primary context, urban applicability, authority"
  - id: key-concepts
    anchor: "#key-concepts"
    purpose: "Concept and framework objects extracted from the source, cross-referenced by object ID"
  - id: methods-and-tools
    anchor: "#methods-and-tools"
    purpose: "Method and tool objects extracted from the source, cross-referenced by object ID"
  - id: lifecycle-coverage
    anchor: "#lifecycle-coverage"
    purpose: "Per-stage coverage; direct vs incidental distinguished"
  - id: known-tensions
    anchor: "#known-tensions"
    purpose: "Explicit tensions, self-identified limitations, internal contradictions, urban applicability gaps"
  - id: decision-logic
    anchor: "#decision-logic"
    purpose: "All decision rule objects with condition, recommendation, and field_query_trigger — no decision logic may appear only in methods or principles"
  - id: findings
    anchor: "#findings"
    purpose: "Full finding content: claim statement, object ID reference, routing rationale — mirrors frontmatter findings: routing records"
  - id: task-seeds
    anchor: "#task-seeds"
    purpose: "Task seed objects identifying operational questions this source can help answer"
  - id: integration-map
    anchor: "#integration-map"
    purpose: "Machine-scannable routing table for Agent 09 — derived from frontmatter findings, contains no new information"
created: YYYY-MM-DD
updated: YYYY-MM-DD
---

<a id="summary"></a>
## Summary

[Author background and institutional affiliation. Document type (academic paper, NGO guidance note, toolkit, policy document, report). What the document covers and what it does not. How it was produced (field research, literature review, case studies, expert consultation, or combination). Which ABA/DRR lifecycle stages it most directly addresses. Primary context (rural/urban/generic/mixed) and urban applicability assessment. Composite authority judgment and basis.]

<a id="key-concepts"></a>
## Key Concepts

[All concept and framework objects extracted in Step 8. For each: brief description and reference by object_id. Tag each `conceptual`.]

**S-{slug}-CONCEPT-001: [Concept Name]** (`conceptual`)
[One paragraph description. See object S-{slug}-CONCEPT-001 for full field contract.]

**S-{slug}-FRAMEWORK-001: [Framework Name]** (`conceptual`)
[One paragraph description. See object S-{slug}-FRAMEWORK-001 for full field contract.]

<a id="methods-and-tools"></a>
## Methods and Tools

[All method and tool objects extracted in Step 8. For each: brief description and reference by object_id. Tag each `diagnostic` or `operational`.]

**S-{slug}-TOOL-001: [Tool Name]** (`diagnostic`)
[One paragraph description including inputs, procedure, and outputs. See object S-{slug}-TOOL-001 for full field contract.]

**S-{slug}-METHOD-001: [Method Name]** (`operational`)
[One paragraph description. See object S-{slug}-METHOD-001 for full field contract.]

<a id="lifecycle-coverage"></a>
## Lifecycle Coverage

[For each lifecycle stage the document addresses, describe: what guidance, evidence, or tools it provides; how direct vs incidental the coverage is; any limitations.]

- **neighbourhood-diagnosis**: [coverage description]
- **joint-prioritization**: [coverage description or "not covered — incidental reference only"]

<a id="known-tensions"></a>
## Known Tensions

[Tensions, contradictions, contested positions, and urban applicability gaps. Do not resolve — preserve for later agents. Include urban checklist items that were flagged in Step 11. If none: "None identified."]

<a id="decision-logic"></a>
## Decision Logic

[Every decision rule object extracted in Step 8, listed with object_id, condition, recommendation, and field_query_trigger. No decision logic may appear only in methods, principles, or implementation logic descriptions — it must appear here. If none: "None identified — source contains no conditional logic."]

**S-{slug}-RULE-001: [Rule Name]**
- **Condition:** [when this rule applies]
- **Recommendation:** [what to do]
- **Exception:** [when this rule does not apply, or "none"]
- **Field query trigger:** [plain-language question a field coordinator would ask under operational pressure]

<a id="findings"></a>
## Findings

[Full finding content for each routing record in frontmatter findings:. Group thematically if >5 findings. For each finding, include the full claim text, object ID cross-reference, and routing rationale. Do not introduce claims not in the frontmatter routing records.]

**F-001** (`decision-rule` / `decision` layer)
[Full claim statement — specific, attributable, and falsifiable. → see S-{slug}-RULE-001]
*Routing rationale:* [One sentence: why this target page and this integration action.]

**F-002** (`concept-definition` / `conceptual` layer)
[Full claim statement. Source only — no suitable target page exists yet.]
*Routing rationale:* No current synthesis page covers this concept; flagged for human review.

<a id="task-seeds"></a>
## Task Seeds

### S-{slug}-SEED-001: [Plain-language field question]
- **Task type:** assessment
- **Contributing objects:** S-{slug}-TOOL-001, S-{slug}-RULE-001
- **Contributing findings:** F-001, F-003
- **Coverage:** partial
- **Gaps:** [What this source does not provide that a complete task note would need]
- **Priority:** high

<a id="integration-map"></a>
## Integration Map

*Derived lookup table — contains no information not already in the frontmatter findings: routing records. Update the frontmatter finding first; then update this table to match.*

| finding_id | label | type | layer | lifecycle | target | action | status |
|---|---|---|---|---|---|---|---|
| F-001 | Brief label (5 words max) | decision-rule | decision | neighbourhood-diagnosis | `09-decision-protocols/example.md` | create-decision-rule | pending |
| F-002 | Brief label (5 words max) | concept-definition | conceptual | neighbourhood-diagnosis | source_only | source_only | pending |
