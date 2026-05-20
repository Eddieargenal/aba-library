<a id="findings"></a>
## Findings

```yaml
findings:

  # ─── C-W1: Conceptual Layer ───────────────────────────────────────────────────

  - finding_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-F-001
    object_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-FRAMEWORK-001
    finding: "Urban Context Analysis Thematic Framework — A systems-thinking framework of five interconnected thematic areas (politics/governance, social/cultural, economic, service delivery, space/settlements) with Do No Harm and gender equality as cross-cutting analytical lenses, used to structure all phases of urban displacement context analysis. → S-2017-iied-urban-context-analysis-toolkit-guidance-note-FRAMEWORK-001"
    knowledge_layer: conceptual
    source_pages: "pp. 16–19, Step 3, Table 3, Figure 3"
    field_query_trigger: not-applicable
    candidate_target_pages:
      - wiki/aba/03-frameworks/urban-context-analysis-framework.md
    integration_action: create-framework
    routing_rationale: No existing urban context analysis framework page; this is the primary analytical framework of the source and warrants its own framework page.
    human_review_required: false

  - finding_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-F-002
    object_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-TYPOLOGY-001
    finding: "Urban Displacement Crisis Typology — A four-category classification of urban displacement crises (conflict→IDP, conflict→refugee, conflict within city, natural hazard within/to city) that frames which analysis questions and stakeholder configurations are most salient. → S-2017-iied-urban-context-analysis-toolkit-guidance-note-TYPOLOGY-001"
    knowledge_layer: conceptual
    source_pages: "p. 15, Table 2"
    field_query_trigger: not-applicable
    candidate_target_pages:
      - wiki/aba/02-concepts/urban-displacement-crisis-typology.md
    integration_action: create-concept
    routing_rationale: Standalone typology not present in wiki; distinct from DRR risk typologies and warrants its own concept page for cross-referencing in advisory work.
    human_review_required: false

  - finding_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-F-003
    object_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-CONCEPT-001
    finding: "Urban Context Analysis — A structured inquiry into why urban crisis response faces specific constraints by analysing political, economic, social, service delivery, and spatial factors; answers 'why' questions rather than 'what' needs questions. → S-2017-iied-urban-context-analysis-toolkit-guidance-note-CONCEPT-001"
    knowledge_layer: conceptual
    source_pages: "pp. 7–9, pp. 34"
    field_query_trigger: not-applicable
    candidate_target_pages:
      - wiki/aba/02-concepts/urban-context-analysis.md
    integration_action: create-concept
    routing_rationale: Core concept of the source; no existing wiki page; enables cross-referencing from area-based-approach and assessment method pages.
    human_review_required: false

  - finding_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-F-004
    object_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-CONCEPT-002
    finding: "Sub-Area as Unit of Analysis — A geographically-bounded community within a city (neighbourhood or settlement) defined by administrative or physical boundaries combined with social analysis considerations, serving as the primary spatial unit for primary data collection in urban context analysis. → S-2017-iied-urban-context-analysis-toolkit-guidance-note-CONCEPT-002"
    knowledge_layer: conceptual
    source_pages: "pp. 15–16, Step 2"
    field_query_trigger: not-applicable
    candidate_target_pages:
      - wiki/aba/02-concepts/sub-area-unit-of-analysis.md
    integration_action: create-concept
    routing_rationale: Directly extends Parker & Maynard 2015 sub-area definition with operational specificity; no existing concept page; foundational for ABA geographic targeting guidance.
    human_review_required: false

  - finding_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-F-005
    object_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-CONCEPT-003
    finding: "Context Analysis vs Needs Assessment Distinction — Context analysis answers 'why' (systemic/structural factors) and is not a substitute for needs assessment which answers 'what' (visible effects and service gaps); both are required and non-interchangeable. → S-2017-iied-urban-context-analysis-toolkit-guidance-note-CONCEPT-003"
    knowledge_layer: conceptual
    source_pages: "pp. 8–9"
    field_query_trigger: not-applicable
    candidate_target_pages:
      - wiki/aba/02-concepts/context-analysis-vs-needs-assessment.md
      - wiki/aba/07-known-tensions/context-analysis-vs-needs-assessment-tension.md
    integration_action: create-concept
    routing_rationale: Explicitly stated conceptual boundary; creates potential known tension when practitioners conflate the two; warrants its own concept page and a tension flag.
    human_review_required: false

  - finding_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-F-006
    object_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-CONCEPT-004
    finding: "Entry Point Identification — The identification of practical opportunities where external actors can engage with existing urban systems and actors to support crisis response, grounded in power relations and stakeholder interests rather than technical ideals alone. → S-2017-iied-urban-context-analysis-toolkit-guidance-note-CONCEPT-004"
    knowledge_layer: conceptual
    source_pages: "pp. 8–9, 34"
    field_query_trigger: not-applicable
    candidate_target_pages:
      - wiki/aba/02-concepts/entry-point-identification.md
    integration_action: create-concept
    routing_rationale: Explicitly defined as the terminal output purpose of context analysis; appears in ABA literature (Parker & Maynard 2015, Sanderson & Sitko 2017) — IIED 2017 provides most explicit operational definition; high integration value for advisory work.
    human_review_required: false

  - finding_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-F-007
    object_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-PRINCIPLE-001
    finding: "Do No Harm Principle — Cross-cutting principle requiring that all programme activities, data collection, and analysis avoid increasing community tensions or undermining existing local systems; integrated throughout all 10 steps of the context analysis. → S-2017-iied-urban-context-analysis-toolkit-guidance-note-PRINCIPLE-001"
    knowledge_layer: conceptual
    source_pages: "pp. 17–18, Step 3"
    field_query_trigger: not-applicable
    candidate_target_pages:
      - wiki/aba/02-concepts/do-no-harm-principle.md
    integration_action: create-concept
    routing_rationale: Cross-cutting principle referenced throughout source; no existing concept page; foundational for risk and safeguard routing across multiple sources.
    human_review_required: false

  - finding_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-F-008
    object_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-PRINCIPLE-002
    finding: "Gender Equality Analytical Lens — Cross-cutting examination of disparities between women and men in responsibilities, resource access, and decision-making, integrated throughout all five thematic areas of the context analysis framework. → S-2017-iied-urban-context-analysis-toolkit-guidance-note-PRINCIPLE-002"
    knowledge_layer: conceptual
    source_pages: "pp. 17–18, Step 3"
    field_query_trigger: not-applicable
    candidate_target_pages:
      - wiki/aba/02-concepts/gender-equality-analytical-lens.md
    integration_action: create-concept
    routing_rationale: Distinct from gender equality as a programme objective; this is a methodological principle for how analysis is conducted; no existing page; relevant for any advisory work involving gender-disaggregated data collection.
    human_review_required: false

  # ─── C-W3a: Methods ───────────────────────────────────────────────────────────

  - finding_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-F-009
    object_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-METHOD-001
    finding: "Urban Context Analysis Process — A 3-phase, 10-step iterative method (preparation, data collection, analysis/documentation) providing a structured workflow from initial scoping to findings communication for urban displacement contexts. → S-2017-iied-urban-context-analysis-toolkit-guidance-note-METHOD-001"
    knowledge_layer: diagnostic
    source_pages: "pp. 10–11, Figure 2, p. 34"
    field_query_trigger: "How do I structure a context analysis in an urban displacement crisis to understand systemic power, service, and governance dynamics before programme design?"
    candidate_target_pages:
      - wiki/aba/04-tools/urban-context-analysis-process.md
    integration_action: create-tool
    routing_rationale: Primary method of the source; 10-step structured workflow merits its own tool page to enable cross-referencing with other assessment methods in the wiki.
    human_review_required: false

  - finding_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-F-010
    object_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-METHOD-002
    finding: "Desk Review Method — Secondary data synthesis conducted 2–3 weeks before primary data collection to identify existing knowledge, gaps, and analytical entry points for an urban context analysis. → S-2017-iied-urban-context-analysis-toolkit-guidance-note-METHOD-002"
    knowledge_layer: diagnostic
    source_pages: "pp. 20–21, Step 4"
    field_query_trigger: "How do I conduct a desk review of secondary data to map existing knowledge and identify gaps before primary data collection in an urban humanitarian context analysis?"
    candidate_target_pages:
      - wiki/aba/04-tools/desk-review-method-urban-context-analysis.md
    integration_action: create-tool
    routing_rationale: Standard desk review method adapted specifically for urban context analysis; sequencing dependency (RULE-007) and template (TOOL-002) make it a standalone tool entry.
    human_review_required: false

  - finding_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-F-011
    object_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-METHOD-003
    finding: "Key Informant Interview (KII) Method — Semi-structured interviews at sub-area and city-wide levels with government, civil society, private sector, and community actors, informed by stakeholder analysis to identify key positions and individuals. → S-2017-iied-urban-context-analysis-toolkit-guidance-note-METHOD-003"
    knowledge_layer: diagnostic
    source_pages: "pp. 24–25, Step 5"
    field_query_trigger: "How do I plan and conduct key informant interviews with government, civil society, and community actors to map power dynamics and service delivery in an urban displacement context?"
    candidate_target_pages:
      - wiki/aba/04-tools/key-informant-interview-method.md
    integration_action: create-tool
    routing_rationale: KII is a named method with specific urban adaptation guidance (snowball sampling, difficult stakeholders); merits its own tool page linked to TOOL-005 (question guides) and TOOL-004 (data collection plan).
    human_review_required: false

  - finding_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-F-012
    object_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-METHOD-004
    finding: "Focus Group Discussion (FGD) Method — Structured discussions with affected populations (displaced and host) conducted in gender-separated groups with same-sex facilitators to surface community-level dynamics in urban sub-areas. → S-2017-iied-urban-context-analysis-toolkit-guidance-note-METHOD-004"
    knowledge_layer: diagnostic
    source_pages: "pp. 24–26, Step 5"
    field_query_trigger: "How do I facilitate focus group discussions with displaced and host community populations in urban sub-areas while managing protection risks and ensuring gender-disaggregated data?"
    candidate_target_pages:
      - wiki/aba/04-tools/focus-group-discussion-method-urban.md
    integration_action: create-tool
    routing_rationale: FGD method with gender-separation rule (RULE-001) and protection protocol (SAFE-001) specific to urban displacement contexts; linked to TOOL-005 (FGD guides 5A-5B).
    human_review_required: false

  - finding_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-F-013
    object_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-METHOD-005
    finding: "Stakeholder Analysis / Actor Mapping Method — Systematic identification and analysis of actors by type, mandate, level, interests, influence, and relationships to inform partnership strategy and coordination planning in urban humanitarian responses. → S-2017-iied-urban-context-analysis-toolkit-guidance-note-METHOD-005"
    knowledge_layer: diagnostic
    source_pages: "pp. 22–23, pp. 29–31"
    field_query_trigger: "How do I map and analyze key stakeholders to understand actor interests, influence, and relationships for programming and coordination in an urban humanitarian response?"
    candidate_target_pages:
      - wiki/aba/04-tools/stakeholder-analysis-actor-mapping.md
    integration_action: create-tool
    routing_rationale: Cross-phase method (used in Steps 4 and 7); emphasis on 'difficult stakeholders' and protection dynamics is urban-specific; merits a tool page cross-referenced with TOOL-003 (matrix instrument).
    human_review_required: false

  - finding_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-F-014
    object_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-METHOD-006
    finding: "Participatory Validation Workshop Method — A one- to two-facilitator workshop with 15–20 diverse stakeholders to challenge, refine, and build shared ownership of preliminary context analysis findings. → S-2017-iied-urban-context-analysis-toolkit-guidance-note-METHOD-006"
    knowledge_layer: diagnostic
    source_pages: "pp. 31–32, Step 8"
    field_query_trigger: "How do I run a validation workshop to challenge and refine urban context analysis findings with diverse stakeholders before finalizing the report?"
    candidate_target_pages:
      - wiki/aba/04-tools/participatory-validation-workshop-method.md
    integration_action: create-tool
    routing_rationale: Distinct from data collection workshops; occurs post-analysis for validation; includes gender considerations (RULE-011); linked to TOOL-009 (agenda instrument).
    human_review_required: false

  - finding_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-F-015
    object_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-METHOD-007
    finding: "Systems-Thinking Analytical Approach — An analytical method examining interconnections between urban thematic areas (politics, social, economic, service delivery, space) rather than each theme in isolation, enabling identification of systemic drivers rather than proximate causes. → S-2017-iied-urban-context-analysis-toolkit-guidance-note-METHOD-007"
    knowledge_layer: diagnostic
    source_pages: "pp. 16–17, Step 3"
    field_query_trigger: "How do I apply systems-thinking analysis to understand how political, economic, social, and spatial factors interact to shape urban crisis response effectiveness?"
    candidate_target_pages:
      - wiki/aba/03-frameworks/urban-context-analysis-framework.md
    integration_action: enrich-framework
    routing_rationale: Systems-thinking is the analytical logic behind FRAMEWORK-001; better routed as an enrichment to the framework page than a standalone tool to avoid duplication.
    human_review_required: false

  - finding_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-F-016
    object_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-METHOD-008
    finding: "Snowball/Referral Sampling Method — A technique used during KIIs and FGDs where each interviewee refers additional participants, enabling teams to reach marginalized or hard-to-access groups that would not appear through gatekeeper-managed sampling. → S-2017-iied-urban-context-analysis-toolkit-guidance-note-METHOD-008"
    knowledge_layer: diagnostic
    source_pages: "p. 27, Step 6"
    field_query_trigger: "How do I use referral sampling to identify and reach marginalized or hard-to-access groups during primary data collection for urban context analysis?"
    candidate_target_pages:
      - wiki/aba/04-tools/snowball-referral-sampling-method.md
    integration_action: create-tool
    routing_rationale: Addresses RISK-001 (sampling bias); specifically recommended to counter gatekeeper dependence in urban displacement contexts; brief description merits a short tool entry cross-referencing RISK-001.
    human_review_required: false

  # ─── C-W3b: Tools ─────────────────────────────────────────────────────────────

  - finding_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-F-017
    object_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-TOOL-001
    finding: "Tool 1 — Workplan and Budget Template — A planning instrument illustrating a 14-day in-country data collection schedule with associated budget categories for urban context analysis. → S-2017-iied-urban-context-analysis-toolkit-guidance-note-TOOL-001"
    knowledge_layer: diagnostic
    source_pages: "pp. 12–13, Step 1"
    field_query_trigger: "How do I plan and budget a 2–4 week urban humanitarian context analysis for a displacement crisis, including team composition and logistics costs?"
    candidate_target_pages:
      - wiki/aba/04-tools/iied-2017-urban-context-analysis-tool-1-workplan.md
    integration_action: create-tool
    routing_rationale: Standalone planning instrument; part of the 10-tool IIED Urban Context Analysis Toolkit; externally accessible (IRC Box link); merits a tool stub with link.
    human_review_required: false

  - finding_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-F-018
    object_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-TOOL-002
    finding: "Tool 2 — Desk Review Summary Template — A secondary data collection template with structured guidance on potential sources per sub-theme of the thematic framework for use 2–3 weeks before fieldwork. → S-2017-iied-urban-context-analysis-toolkit-guidance-note-TOOL-002"
    knowledge_layer: diagnostic
    source_pages: "pp. 20–21, Step 4"
    field_query_trigger: "What secondary data should I collect, document, and analyse before conducting field interviews for an urban humanitarian context analysis in a displacement setting?"
    candidate_target_pages:
      - wiki/aba/04-tools/iied-2017-urban-context-analysis-tool-2-desk-review-summary.md
    integration_action: create-tool
    routing_rationale: Structured desk review instrument aligned to FRAMEWORK-001 sub-themes; operationalises METHOD-002 and RULE-007; externally accessible.
    human_review_required: false

  - finding_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-F-019
    object_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-TOOL-003
    finding: "Tool 3 — Stakeholder Analysis Matrix — A multi-column matrix for listing, categorizing, and ranking stakeholders by type, level, role, interests, influence, and engagement strategy; updated iteratively across Steps 4 and 7. → S-2017-iied-urban-context-analysis-toolkit-guidance-note-TOOL-003"
    knowledge_layer: diagnostic
    source_pages: "pp. 22–23, pp. 29–31"
    field_query_trigger: "How do I map and analyze key stakeholders — government, civil society, private sector, and difficult actors — for a humanitarian programme in an urban displacement context?"
    candidate_target_pages:
      - wiki/aba/04-tools/iied-2017-urban-context-analysis-tool-3-stakeholder-matrix.md
    integration_action: create-tool
    routing_rationale: The instrument operationalising METHOD-005; cross-phase use (Steps 4 and 7); includes 'difficult stakeholder' column not present in generic actor-mapping tools.
    human_review_required: false

  - finding_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-F-020
    object_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-TOOL-004
    finding: "Tool 4 — Data Collection Plan Template — A two-tab planning matrix covering sub-area sampling (4A) and city-wide sampling (4B), including interviewer, translator, logistics, and meeting planning for urban context analysis fieldwork. → S-2017-iied-urban-context-analysis-toolkit-guidance-note-TOOL-004"
    knowledge_layer: diagnostic
    source_pages: "p. 24, Step 5"
    field_query_trigger: "How do I plan data collection logistics — who to interview, with what sampling approach — across multiple sub-areas and city-wide for an urban humanitarian context analysis?"
    candidate_target_pages:
      - wiki/aba/04-tools/iied-2017-urban-context-analysis-tool-4-data-collection-plan.md
    integration_action: create-tool
    routing_rationale: Operationalises IMPL-001 (team composition) and IMPL-004 (training); two-tab structure explicitly separates sub-area from city-wide sampling; externally accessible.
    human_review_required: false

  - finding_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-F-021
    object_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-TOOL-005
    finding: "Tools 5A–5G — KII and FGD Question Guides — A seven-instrument set of semi-structured interview and focus group guides covering displaced populations, host communities, influential stakeholders, service providers, labour/business, local government, and NGO service providers. → S-2017-iied-urban-context-analysis-toolkit-guidance-note-TOOL-005"
    knowledge_layer: diagnostic
    source_pages: "pp. 24–26, Step 5"
    field_query_trigger: "What interview and focus group questions should I use with displaced populations, host communities, local government, and service providers during an urban context analysis field assessment?"
    candidate_target_pages:
      - wiki/aba/05-field-instruments/iied-2017-urban-context-analysis-kii-fgd-guides.md
    integration_action: create-field-instrument
    routing_rationale: Seven-instrument set constitutes field instruments (questionnaires/question guides); routes to 05-field-instruments/ rather than 04-tools/; template content is externally hosted (IRC Box links).
    human_review_required: false

  - finding_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-F-022
    object_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-TOOL-006
    finding: "Tool 6 — KII and FGD Debrief Template — A two-sheet daily and mid-collection synthesis instrument mapping sub-area findings to the thematic framework and tracking local service providers; bridges data collection (Step 6) and analysis (Step 7). → S-2017-iied-urban-context-analysis-toolkit-guidance-note-TOOL-006"
    knowledge_layer: diagnostic
    source_pages: "pp. 27–28, Step 6"
    field_query_trigger: "How do I track and synthesize daily interview findings across urban sub-areas to identify data gaps and adjust data collection mid-way through a context analysis?"
    candidate_target_pages:
      - wiki/aba/04-tools/iied-2017-urban-context-analysis-tool-6-debrief-template.md
    integration_action: create-tool
    routing_rationale: Operationalises IMPL-005 (daily debrief process); explicit bridge between data collection and analysis phases; externally accessible.
    human_review_required: false

  - finding_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-F-023
    object_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-TOOL-007
    finding: "Tool 7 — Key Findings Analysis Template — A multi-column matrix for consolidating primary and secondary data findings by sub-area, theme, gender, population type, and age group, with columns for cross-area comparison, risk, and programming implications; includes optional Tool 7B dividers/connectors tab. → S-2017-iied-urban-context-analysis-toolkit-guidance-note-TOOL-007"
    knowledge_layer: diagnostic
    source_pages: "pp. 29–30, Step 7"
    field_query_trigger: "How do I synthesize and compare qualitative findings across multiple urban sub-areas, population groups, and gender to identify key patterns for humanitarian programme design?"
    candidate_target_pages:
      - wiki/aba/04-tools/iied-2017-urban-context-analysis-tool-7-key-findings.md
    integration_action: create-tool
    routing_rationale: Primary analysis instrument; multi-column cross-area comparison structure is distinctive; operationalises RULE-006 (triangulation) and PRINCIPLE-002 (gender lens); externally accessible.
    human_review_required: false

  - finding_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-F-024
    object_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-TOOL-008
    finding: "Tool 8 — Programme Implications Template — A five-table instrument translating context analysis findings and stakeholder analysis into programming opportunities, partnerships, advocacy issues, risk mitigation approaches, and connector strategies. → S-2017-iied-urban-context-analysis-toolkit-guidance-note-TOOL-008"
    knowledge_layer: diagnostic
    source_pages: "p. 31, Step 7"
    field_query_trigger: "How do I translate urban context analysis findings into specific programming opportunities, risk mitigation strategies, and partnership recommendations for a humanitarian response?"
    candidate_target_pages:
      - wiki/aba/04-tools/iied-2017-urban-context-analysis-tool-8-programme-implications.md
    integration_action: create-tool
    routing_rationale: Terminal output instrument; operationalises CONCEPT-004 (entry point identification); translates 'why' analysis into 'what to do' — critical bridge to programme design; externally accessible.
    human_review_required: false

  - finding_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-F-025
    object_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-TOOL-009
    finding: "Tool 9 — Urban Analysis Validation Workshop — A one-day workshop instrument with agenda and facilitation guidance for 15–20 diverse participants to challenge and refine preliminary context analysis findings. → S-2017-iied-urban-context-analysis-toolkit-guidance-note-TOOL-009"
    knowledge_layer: diagnostic
    source_pages: "pp. 31–32, Step 8"
    field_query_trigger: "How do I organise and facilitate a participatory validation workshop to refine and build ownership of urban context analysis findings with key stakeholders?"
    candidate_target_pages:
      - wiki/aba/04-tools/iied-2017-urban-context-analysis-tool-9-validation-workshop.md
    integration_action: create-tool
    routing_rationale: Operationalises METHOD-006; includes RULE-011 trigger (women-only working groups); externally accessible.
    human_review_required: false

  - finding_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-F-026
    object_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-TOOL-010
    finding: "Tool 10 — Urban Context Analysis Final Report Outline — A table of contents and methodological summary tables for an internal context analysis report, with explicit guidance on internal vs external report framing. → S-2017-iied-urban-context-analysis-toolkit-guidance-note-TOOL-010"
    knowledge_layer: diagnostic
    source_pages: "pp. 32–33, Step 9"
    field_query_trigger: "What structure and sections should a final report for an urban humanitarian context analysis follow, and how do I document the methodology for internal use?"
    candidate_target_pages:
      - wiki/aba/04-tools/iied-2017-urban-context-analysis-tool-10-final-report-outline.md
    integration_action: create-tool
    routing_rationale: Terminal documentation instrument; operationalises RULE-012 (internal-only when sensitive); IMPL-006 (dissemination); externally accessible.
    human_review_required: false

  # ─── C-W2: Decision Rules ─────────────────────────────────────────────────────

  - finding_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-F-027
    object_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-RULE-001
    finding: "Separate FGDs by Gender/Age Rule — Plan separate FGDs for men, women, adolescent boys, and adolescent girls with same-sex facilitators; adolescents are less likely to share openly in mixed-gender groups. → S-2017-iied-urban-context-analysis-toolkit-guidance-note-RULE-001"
    knowledge_layer: decision
    source_pages: "p. 25, Step 5"
    field_query_trigger: "How should focus groups be structured to ensure adolescents and women share openly during urban displacement data collection?"
    candidate_target_pages:
      - wiki/aba/09-decision-protocols/fgd-gender-age-separation-protocol.md
    integration_action: create-decision-rule
    routing_rationale: Stated planning requirement for FGD design; applies to all contexts using METHOD-004; warrants a decision protocol entry for advisory use.
    human_review_required: false

  - finding_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-F-028
    object_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-RULE-002
    finding: "Context Analysis Reassessment Trigger Rule — Reassess context analysis validity when findings are more than 6–9 months old, when significant crisis change occurs, when new data collection is planned, or when a new proposal requires deeper information. → S-2017-iied-urban-context-analysis-toolkit-guidance-note-RULE-002"
    knowledge_layer: decision
    source_pages: "p. 33, 'When to update'"
    field_query_trigger: "How do we determine whether our existing urban context analysis findings are still valid for programme design decisions?"
    candidate_target_pages:
      - wiki/aba/09-decision-protocols/context-analysis-reassessment-trigger.md
    integration_action: create-decision-rule
    routing_rationale: Four-trigger decision rule for a high-stakes operational decision (when to redo analysis); supports SEED-003; 6-9 month threshold should be flagged as practitioner rule-of-thumb without evidence base.
    human_review_required: false

  - finding_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-F-029
    object_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-RULE-003
    finding: "Partner Inclusion Restriction Rule — Be careful about including new local partners in context analysis data collection when significant conflict or protection dynamics are present; assess bias risk and protection risk to partner staff before including. → S-2017-iied-urban-context-analysis-toolkit-guidance-note-RULE-003"
    knowledge_layer: decision
    source_pages: "p. 14, 'Joint analysis and partnerships'"
    field_query_trigger: "Should we include local partner organisations in urban context analysis data collection when there are active conflict or displacement protection concerns?"
    candidate_target_pages:
      - wiki/aba/09-decision-protocols/partner-inclusion-in-context-analysis.md
    integration_action: create-decision-rule
    routing_rationale: Conditional rule modifying IMPL-003 (joint analysis design); addresses RISK-003 (partner bias); requires human judgment on context-specific risk levels — flag accordingly.
    human_review_required: true

  - finding_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-F-030
    object_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-RULE-004
    finding: "Do No Harm Data Collection Rule — Apply Do No Harm analysis throughout data collection to ensure activities do not increase community tensions, undermine existing service systems, or expose participants to harm. → S-2017-iied-urban-context-analysis-toolkit-guidance-note-RULE-004"
    knowledge_layer: decision
    source_pages: "pp. 17–18, Step 3; pp. 27–28, Step 6"
    field_query_trigger: "How do we ensure our urban data collection activities do not increase community tensions or create protection risks for participants?"
    candidate_target_pages:
      - wiki/aba/09-decision-protocols/do-no-harm-data-collection-checklist.md
    integration_action: create-decision-rule
    routing_rationale: Operationalises PRINCIPLE-001 at data collection stage; closely related to RULE-005 (data protection) and RULE-012 (sensitive report); merits a standalone decision checklist.
    human_review_required: false

  - finding_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-F-031
    object_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-RULE-005
    finding: "Participant Data Protection Rule — Anonymize interview notes, limit storage access to a few persons, and destroy notes after analysis when retention is not required; informed consent required at every data collection event. → S-2017-iied-urban-context-analysis-toolkit-guidance-note-RULE-005"
    knowledge_layer: decision
    source_pages: "p. 28, 'Protection considerations and data collection'"
    field_query_trigger: "What data protection protocols should govern our interview notes and FGD records during urban context analysis to protect participants?"
    candidate_target_pages:
      - wiki/aba/09-decision-protocols/participant-data-protection-protocol.md
    integration_action: create-decision-rule
    routing_rationale: Operationalises SAFE-001 as a decision rule; directly connected to RISK-002 (exposure risk); standard humanitarian data protection practice with urban-specific emphasis.
    human_review_required: false

  - finding_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-F-032
    object_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-RULE-006
    finding: "Triangulation Requirement Rule — Triangulate all qualitative findings from multiple sources before concluding analysis; single-informant or single-source data is insufficient for context analysis conclusions. → S-2017-iied-urban-context-analysis-toolkit-guidance-note-RULE-006"
    knowledge_layer: decision
    source_pages: "p. 30, Tip 'Triangulate information'"
    field_query_trigger: "How do we validate qualitative findings from key informant interviews and focus groups before finalising our urban context analysis?"
    candidate_target_pages:
      - wiki/aba/09-decision-protocols/qualitative-triangulation-requirement.md
    integration_action: create-decision-rule
    routing_rationale: Stated as essential analytical quality control; addresses risk of single-perspective bias in urban heterogeneous settings; mitigates RISK-001 (sampling bias) at analysis stage.
    human_review_required: false

  - finding_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-F-033
    object_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-RULE-007
    finding: "Desk Review Before Fieldwork Rule — Complete desk review 2–3 weeks before primary data collection to allow time to revise the data collection plan based on identified gaps; starting fieldwork without desk review wastes resources on already-documented information. → S-2017-iied-urban-context-analysis-toolkit-guidance-note-RULE-007"
    knowledge_layer: decision
    source_pages: "pp. 20–21, Step 4"
    field_query_trigger: "When in the urban context analysis timeline should we complete the desk review relative to starting field data collection?"
    candidate_target_pages:
      - wiki/aba/09-decision-protocols/desk-review-sequencing-rule.md
    integration_action: create-decision-rule
    routing_rationale: Sequencing dependency embedded in METHOD-001; becomes a standalone decision rule because violating it undermines data collection efficiency and quality.
    human_review_required: false

  - finding_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-F-034
    object_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-RULE-008
    finding: "Question Guide Adaptation Rule — Adapt question guides for every context analysis by removing irrelevant questions, adding context-specific questions, and validating with country staff; never use default templates without adaptation. → S-2017-iied-urban-context-analysis-toolkit-guidance-note-RULE-008"
    knowledge_layer: decision
    source_pages: "pp. 25–26"
    field_query_trigger: "How should we modify the standard question guides for our specific urban displacement context before starting data collection?"
    candidate_target_pages:
      - wiki/aba/09-decision-protocols/question-guide-adaptation-protocol.md
    integration_action: create-decision-rule
    routing_rationale: Applies to all seven Tools 5A-5G; stated as a mandatory requirement; operationalises IMPL-007 (question guide adaptation) as an enforceable decision rule.
    human_review_required: false

  - finding_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-F-035
    object_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-RULE-009
    finding: "Gender-Only Analysis Toolkit Selection Rule — If the organisation seeks only gender equality analysis, conduct a dedicated in-depth gender analysis rather than the full urban context analysis toolkit. → S-2017-iied-urban-context-analysis-toolkit-guidance-note-RULE-009"
    knowledge_layer: decision
    source_pages: "p. 17, footnote 5"
    field_query_trigger: "Should we use this urban context analysis toolkit if our primary objective is a dedicated gender equality analysis?"
    candidate_target_pages:
      - wiki/aba/09-decision-protocols/assessment-tool-selection-gender-only.md
    integration_action: create-decision-rule
    routing_rationale: Toolkit scoping rule limiting appropriate use case; prevents misapplication; relevant for programme design decisions about which assessment tool to deploy.
    human_review_required: false

  - finding_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-F-036
    object_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-RULE-010
    finding: "Participatory Planning Workshop Trigger Rule — Conduct an optional participatory data collection planning workshop when analysis is conducted in formal partnership with other organisations or when staff have limited local community knowledge. → S-2017-iied-urban-context-analysis-toolkit-guidance-note-RULE-010"
    knowledge_layer: decision
    source_pages: "p. 25"
    field_query_trigger: "Should we run a stakeholder planning workshop before urban data collection when working with local partner organisations or unfamiliar areas?"
    candidate_target_pages:
      - wiki/aba/09-decision-protocols/participatory-planning-workshop-trigger.md
    integration_action: create-decision-rule
    routing_rationale: Conditional trigger for an optional preparatory step; distinct from validation workshop (RULE-011); overlaps with RULE-003 when partnership is also a protection concern.
    human_review_required: false

  - finding_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-F-037
    object_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-RULE-011
    finding: "Women-Only Validation Workshop Groups Rule — Designate women-only working groups with documented outputs during validation workshops in contexts where women face obstacles to participating in mixed-group discussions. → S-2017-iied-urban-context-analysis-toolkit-guidance-note-RULE-011"
    knowledge_layer: decision
    source_pages: "p. 32, Step 8"
    field_query_trigger: "How should we structure validation workshop groups to ensure women's perspectives are captured in contexts where mixed-gender participation is constrained?"
    candidate_target_pages:
      - wiki/aba/09-decision-protocols/fgd-gender-age-separation-protocol.md
    integration_action: enrich-decision-rule
    routing_rationale: Extends RULE-001 (gender-separated FGDs) to the validation workshop phase; route as enrichment to the same gender-separation decision protocol rather than a duplicate entry.
    human_review_required: false

  - finding_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-F-038
    object_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-RULE-012
    finding: "Sensitive Findings Internal-Only Report Rule — Produce an internal-only context analysis report when findings contain sensitive or commercially confidential information; clarify whether external summary reports are also required before starting to write. → S-2017-iied-urban-context-analysis-toolkit-guidance-note-RULE-012"
    knowledge_layer: decision
    source_pages: "p. 33, Step 9"
    field_query_trigger: "What should govern decisions about whether to produce internal-only versus externally shareable reports from urban context analysis?"
    candidate_target_pages:
      - wiki/aba/09-decision-protocols/context-analysis-report-sensitivity-protocol.md
    integration_action: create-decision-rule
    routing_rationale: Operationalises RULE-005 (data protection) at report stage; LESSON-003 (Maiduguri) illustrates the dual-document solution; protects participant confidentiality in sensitive urban contexts.
    human_review_required: false

  - finding_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-F-039
    object_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-RULE-013
    finding: "Culturally-Matched Team Composition Rule — Recruit interviewers and facilitators from the same social, ethnic, and gender groups as target participants to build trust, reduce identity-masking, and improve data quality. → S-2017-iied-urban-context-analysis-toolkit-guidance-note-RULE-013"
    knowledge_layer: decision
    source_pages: "p. 13, Table 1; p. 28, Dar es Salaam case"
    field_query_trigger: "How should we compose the data collection team to ensure trust and effective communication with displaced populations in urban context analysis?"
    candidate_target_pages:
      - wiki/aba/09-decision-protocols/team-composition-cultural-matching-rule.md
    integration_action: create-decision-rule
    routing_rationale: Stated as 'essential' — strongest normative language in source; Dar es Salaam case (LESSON-002) provides direct evidence base; directly addresses RISK-002 (identity masking).
    human_review_required: false

  # ─── C-W4: Operational Layer ──────────────────────────────────────────────────

  - finding_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-F-040
    object_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-IMPL-001
    finding: "Team Composition and Roles — Structured team for urban context analysis comprising a team lead, support/logistics member(s), and a data collection team with local language competencies; translators typically required for some team members. → S-2017-iied-urban-context-analysis-toolkit-guidance-note-IMPL-001"
    knowledge_layer: operational
    source_pages: "p. 13, Table 1, Step 1"
    field_query_trigger: "How should I structure and staff a team to conduct an urban context analysis in a displacement crisis, including roles for team lead, data collectors, and translators?"
    candidate_target_pages:
      - wiki/aba/04-tools/urban-context-analysis-process.md
    integration_action: enrich-tool
    routing_rationale: Team composition is an implementation detail best documented as enrichment to METHOD-001 tool page; connected to RULE-013 (cultural matching) and SAFE-002.
    human_review_required: false

  - finding_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-F-041
    object_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-IMPL-002
    finding: "Sub-Area Selection and Prioritization — A criteria-based approach for selecting city sub-areas using vulnerability comparison, existing programming, knowledge gaps, security/access, and government/UN request as prioritization criteria. → S-2017-iied-urban-context-analysis-toolkit-guidance-note-IMPL-002"
    knowledge_layer: operational
    source_pages: "pp. 15–16, Step 2"
    field_query_trigger: "How do I prioritize and select which neighbourhoods or sub-areas of a city to include in a rapid urban context analysis when resources limit how many areas I can cover?"
    candidate_target_pages:
      - wiki/aba/02-concepts/sub-area-unit-of-analysis.md
    integration_action: enrich-concept
    routing_rationale: Provides operational criteria for sub-area selection; best routed as enrichment to CONCEPT-002 (sub-area unit of analysis) page which will contain selection guidance.
    human_review_required: false

  - finding_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-F-042
    object_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-IMPL-003
    finding: "Joint/Partner Analysis Design — Decisions on when and how to include local/international partners in context analysis, governed by protection dynamics, bias risk, and complementarity of expertise. → S-2017-iied-urban-context-analysis-toolkit-guidance-note-IMPL-003"
    knowledge_layer: operational
    source_pages: "p. 14, 'Joint analysis and partnerships'"
    field_query_trigger: "When conducting an urban context analysis in partnership with other organisations, how do I decide whether and in which phases to include local partners, and what safeguards are needed to manage bias and protection risks?"
    candidate_target_pages:
      - wiki/aba/09-decision-protocols/partner-inclusion-in-context-analysis.md
    integration_action: enrich-decision-rule
    routing_rationale: Implementation logic for partner inclusion; best routed as enrichment to RULE-003 decision protocol, which is the decision gate for partner inclusion.
    human_review_required: false

  - finding_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-F-043
    object_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-IMPL-004
    finding: "Data Collection Team Training and Orientation — A minimum half- to full-day orientation covering toolkit purpose, desk review findings, question guide review with local language agreement, role-play, and tool piloting in city areas. → S-2017-iied-urban-context-analysis-toolkit-guidance-note-IMPL-004"
    knowledge_layer: operational
    source_pages: "pp. 25–26"
    field_query_trigger: "How do I prepare a data collection team for urban context analysis fieldwork, including language preparation, tool adaptation, and protection training?"
    candidate_target_pages:
      - wiki/aba/04-tools/urban-context-analysis-process.md
    integration_action: enrich-tool
    routing_rationale: Training protocol is an implementation step within METHOD-001; best as enrichment to the process tool page; includes protection discussion requirement from RULE-004.
    human_review_required: false

  - finding_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-F-044
    object_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-IMPL-005
    finding: "Daily Debrief and Mid-Collection Review — Structured daily and mid-collection team synthesis using Tool 6 to compare findings across interviewers, identify gaps, refine sampling, and adjust interview guides while still in the field. → S-2017-iied-urban-context-analysis-toolkit-guidance-note-IMPL-005"
    knowledge_layer: operational
    source_pages: "pp. 27–28, Step 6"
    field_query_trigger: "How do I structure daily and mid-collection team debriefs during urban context analysis fieldwork to maintain data quality and adjust sampling while in the field?"
    candidate_target_pages:
      - wiki/aba/04-tools/iied-2017-urban-context-analysis-tool-6-debrief-template.md
    integration_action: enrich-tool
    routing_rationale: Operationalises TOOL-006 (debrief template); documents the procedural logic for using the debrief tool mid-fieldwork; enriches the tool page with step-by-step guidance.
    human_review_required: false

  - finding_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-F-045
    object_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-IMPL-006
    finding: "Findings Communication and Dissemination — Internal stakeholders receive the full analysis report; external stakeholders receive an anonymized summary where feasible, ensuring informed consent commitments are respected and no protection risks to community members. → S-2017-iied-urban-context-analysis-toolkit-guidance-note-IMPL-006"
    knowledge_layer: operational
    source_pages: "pp. 33–34, Step 10"
    field_query_trigger: "How should I share urban context analysis findings with internal programme staff and external stakeholders while protecting participant confidentiality and respecting informed consent commitments?"
    candidate_target_pages:
      - wiki/aba/04-tools/urban-context-analysis-process.md
      - wiki/aba/09-decision-protocols/context-analysis-report-sensitivity-protocol.md
    integration_action: enrich-tool
    routing_rationale: Implementation logic for Step 10 communication; references RULE-012, LESSON-003 (Maiduguri dual-document model), and RULE-005; enriches the process tool page.
    human_review_required: false

  - finding_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-F-046
    object_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-IMPL-007
    finding: "Question Guide Adaptation and Contextualization — A four-step process: (1) eliminate irrelevant questions, (2) add context-specific questions, (3) validate with country staff, (4) discuss protection risks with team before fieldwork. → S-2017-iied-urban-context-analysis-toolkit-guidance-note-IMPL-007"
    knowledge_layer: operational
    source_pages: "pp. 25–26"
    field_query_trigger: "How do I adapt standardized KII and FGD question guides for a specific urban displacement context before fieldwork, including what to remove, add, and validate?"
    candidate_target_pages:
      - wiki/aba/05-field-instruments/iied-2017-urban-context-analysis-kii-fgd-guides.md
    integration_action: enrich-field-instrument
    routing_rationale: Provides the procedural logic for adapting Tools 5A-5G; operationalises RULE-008 (adaptation requirement); best as enrichment to the field instrument page.
    human_review_required: false

  # ─── C-W5: Evidence Layer ─────────────────────────────────────────────────────

  - finding_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-F-047
    object_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-RISK-001
    finding: "Sampling Bias from Key Powerholder Dependence — Relying on community gatekeepers to organize FGD/KII participation systematically excludes marginalized groups; urban heterogeneity makes this risk more acute than in rural settings. → S-2017-iied-urban-context-analysis-toolkit-guidance-note-RISK-001"
    knowledge_layer: diagnostic
    source_pages: "p. 27, Step 6"
    field_query_trigger: "What sampling strategies should we use to avoid systematic exclusion of marginalized groups when gatekeepers control access to FGD/KII participants?"
    candidate_target_pages:
      - wiki/aba/06-risks/sampling-bias-powerholder-dependence.md
    integration_action: create-risk
    routing_rationale: Structural risk in urban humanitarian data collection; mitigated by METHOD-008 (snowball sampling), RULE-006 (triangulation), SAFE-002 (culturally-matched team).
    human_review_required: false

  - finding_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-F-048
    object_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-RISK-002
    finding: "Protection Risk from Data Collection Exposure — Urban displaced populations (especially refugees) may mask nationality/identity to avoid deportation; data collection activities can inadvertently expose individuals to harm if protection protocols are not applied. → S-2017-iied-urban-context-analysis-toolkit-guidance-note-RISK-002"
    knowledge_layer: diagnostic
    source_pages: "pp. 26, 28"
    field_query_trigger: "What protection risks should we anticipate when conducting data collection with displaced populations who may be concealing their identity or legal status?"
    candidate_target_pages:
      - wiki/aba/06-risks/data-collection-exposure-risk-displaced-populations.md
    integration_action: create-risk
    routing_rationale: Urban-specific risk with direct evidence from Dar es Salaam pilot (LESSON-002); mitigated by SAFE-001 and SAFE-002; high consequence if unmitigated.
    human_review_required: false

  - finding_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-F-049
    object_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-RISK-003
    finding: "Partner Bias in Joint Context Analysis — Local partner participation in joint analysis can introduce systematic bias in data collection or interpretation, or create confidentiality breaches, that cannot always be mitigated through team composition. → S-2017-iied-urban-context-analysis-toolkit-guidance-note-RISK-003"
    knowledge_layer: diagnostic
    source_pages: "pp. 14, 28"
    field_query_trigger: "How should we assess and mitigate the risk that local partner organisations introduce systematic bias into joint urban context analysis data collection?"
    candidate_target_pages:
      - wiki/aba/06-risks/partner-bias-joint-analysis-risk.md
    integration_action: create-risk
    routing_rationale: Addressed by RULE-003 (partner restriction) and IMPL-003 (joint analysis design); named risk in source; relevant for coordination-heavy urban response contexts.
    human_review_required: false

  - finding_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-F-050
    object_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-RISK-004
    finding: "Context Analysis Staleness Risk — Urban context analysis findings older than 6–9 months may no longer accurately reflect programming realities in dynamic crisis settings, leading to programme design based on invalid assumptions. → S-2017-iied-urban-context-analysis-toolkit-guidance-note-RISK-004"
    knowledge_layer: diagnostic
    source_pages: "p. 33"
    field_query_trigger: "How do we identify when an existing urban context analysis has become too outdated to rely on for new programme design decisions?"
    candidate_target_pages:
      - wiki/aba/06-risks/context-analysis-staleness-risk.md
    integration_action: create-risk
    routing_rationale: Mitigated by RULE-002 (reassessment trigger); 6-9 month threshold is a practitioner heuristic without supporting evidence from pilots.
    human_review_required: false

  - finding_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-F-051
    object_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-LESSON-001
    finding: "Dar es Salaam Sub-Area Selection Lesson — Pre-existing knowledge of displaced population locations (Burundian and Congolese concentrations) enabled IRC to focus sub-area selection on three high-relevance areas; without this prior knowledge, relevant areas would have been missed. → S-2017-iied-urban-context-analysis-toolkit-guidance-note-LESSON-001"
    knowledge_layer: operational
    source_pages: "p. 16"
    field_query_trigger: "What prior knowledge about displaced population geography should we collect before selecting sub-areas for urban context analysis?"
    candidate_target_pages:
      - wiki/aba/02-concepts/sub-area-unit-of-analysis.md
    integration_action: enrich-concept
    routing_rationale: Substantiates IMPL-002 (sub-area selection criteria) and CONCEPT-002; enrich the sub-area concept page with this field evidence.
    human_review_required: false

  - finding_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-F-052
    object_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-LESSON-002
    finding: "Dar es Salaam Identity Masking Lesson — Burundian and Congolese refugees refused to disclose nationality due to deportation risk; having a Congolese team member was critical to navigating access and protection concerns during data collection. → S-2017-iied-urban-context-analysis-toolkit-guidance-note-LESSON-002"
    knowledge_layer: operational
    source_pages: "p. 28"
    field_query_trigger: "How should we compose a data collection team to maintain access to populations that conceal their identity or legal status due to protection fears?"
    candidate_target_pages:
      - wiki/aba/06-risks/data-collection-exposure-risk-displaced-populations.md
    integration_action: enrich-risk
    routing_rationale: Provides direct field evidence for RISK-002; demonstrates that SAFE-002 and RULE-013 are operationally necessary, not optional; high generalizability.
    human_review_required: false

  - finding_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-F-053
    object_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-LESSON-003
    finding: "Maiduguri Dual-Document Lesson — IRC produced a public external brief alongside the sensitive internal context analysis report to communicate findings to wider stakeholders who had not participated in the analysis, enabling knowledge transfer without compromising confidentiality. → S-2017-iied-urban-context-analysis-toolkit-guidance-note-LESSON-003"
    knowledge_layer: operational
    source_pages: "p. 33"
    field_query_trigger: "How should we communicate context analysis findings to external stakeholders when the internal report contains sensitive political or protection-related information?"
    candidate_target_pages:
      - wiki/aba/09-decision-protocols/context-analysis-report-sensitivity-protocol.md
    integration_action: enrich-decision-rule
    routing_rationale: Operationalises RULE-012 by demonstrating the dual-document solution; enriches the decision protocol page with a concrete practice model.
    human_review_required: false

  - finding_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-F-054
    object_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-ASM-001
    finding: "Country Presence Assumption — The toolkit assumes the implementing organisation has been operating in the city or country for at least several months and can dedicate approximately two weeks to in-country data collection; not designed for first-entry rapid response. → S-2017-iied-urban-context-analysis-toolkit-guidance-note-ASM-001"
    knowledge_layer: conceptual
    source_pages: "pp. 9, 12"
    field_query_trigger: not-applicable
    candidate_target_pages:
      - wiki/aba/02-concepts/urban-context-analysis.md
    integration_action: enrich-concept
    routing_rationale: Scope limitation of the toolkit; enriches CONCEPT-001 with applicability boundaries; critical for advisory work recommending the toolkit.
    human_review_required: false

  - finding_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-F-055
    object_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-ASM-002
    finding: "Representative Sampling Assumption — The toolkit assumes adequate diversity of participants can be achieved through deliberate sampling design; this assumption may not hold in high-insecurity contexts with structural access barriers. → S-2017-iied-urban-context-analysis-toolkit-guidance-note-ASM-002"
    knowledge_layer: conceptual
    source_pages: "pp. 25–27"
    field_query_trigger: not-applicable
    candidate_target_pages:
      - wiki/aba/06-risks/sampling-bias-powerholder-dependence.md
    integration_action: enrich-risk
    routing_rationale: Creates TNS-001 tension with RISK-001; enriches the sampling bias risk page with the toolkit's own assumption about its capability, flagging the internal tension.
    human_review_required: false

  - finding_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-F-056
    object_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-ASM-003
    finding: "Optional Final Report Assumption — A final written report is not mandatory; validation workshop outputs may suffice to complete the context analysis, though this creates risk that findings are not durably documented. → S-2017-iied-urban-context-analysis-toolkit-guidance-note-ASM-003"
    knowledge_layer: conceptual
    source_pages: "p. 32, Step 9"
    field_query_trigger: not-applicable
    candidate_target_pages:
      - wiki/aba/02-concepts/urban-context-analysis.md
    integration_action: enrich-concept
    routing_rationale: Creates ambiguity about what constitutes 'completion'; enriches CONCEPT-001 with scope limitation note; advisory work should flag the institutional knowledge risk of skipping the written report.
    human_review_required: false

  - finding_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-F-057
    object_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-SAFE-001
    finding: "Data Collection Protection Protocol — Informed consent at every data collection event; notes contain only general references to interview type and location (no identifiable information); secure storage limited to few persons; notes destroyed after analysis unless retention required. → S-2017-iied-urban-context-analysis-toolkit-guidance-note-SAFE-001"
    knowledge_layer: operational
    source_pages: "p. 28"
    field_query_trigger: "What safeguards should govern the handling of interview notes and participant data during and after urban context analysis fieldwork?"
    candidate_target_pages:
      - wiki/aba/09-decision-protocols/participant-data-protection-protocol.md
    integration_action: enrich-decision-rule
    routing_rationale: Operationalises RULE-005; provides the procedural safeguard specification; enriches the data protection decision protocol.
    human_review_required: false

  - finding_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-F-058
    object_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-SAFE-002
    finding: "Culturally-Matched Team Composition Safeguard — Recruit interviewers and facilitators from the same community, ethnic, and gender groups as target participants; stated as essential (not optional) in source; directly addresses identity-masking risk in urban displaced populations. → S-2017-iied-urban-context-analysis-toolkit-guidance-note-SAFE-002"
    knowledge_layer: operational
    source_pages: "p. 13, Table 1; p. 28"
    field_query_trigger: "How should I staff a data collection team to maintain access to populations that conceal their identity due to protection concerns in urban displacement contexts?"
    candidate_target_pages:
      - wiki/aba/09-decision-protocols/team-composition-cultural-matching-rule.md
    integration_action: enrich-decision-rule
    routing_rationale: Safeguard version of RULE-013; enriches the cultural-matching decision protocol with the specific procedural safeguard specification from IMPL-001 and the Dar es Salaam case.
    human_review_required: false

  - finding_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-F-059
    object_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-TNS-001
    finding: "Sampling Representativeness Tension — ASM-002 assumes representative sampling is achievable through deliberate design; RISK-001 identifies structural bias from powerholder access control as a risk that deliberate design may not overcome; source does not resolve this tension. → S-2017-iied-urban-context-analysis-toolkit-guidance-note-TNS-001"
    knowledge_layer: conceptual
    source_pages: "pp. 25–27"
    field_query_trigger: not-applicable
    candidate_target_pages:
      - wiki/aba/07-known-tensions/sampling-representativeness-vs-structural-access-barriers.md
    integration_action: create-risk
    routing_rationale: Methodological tension embedded in the toolkit's design; flagged in C-W5 as unresolved; routes to known-tensions folder.
    human_review_required: true

  # ─── C-W6: Task Seeds ─────────────────────────────────────────────────────────

  - finding_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-F-060
    object_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-SEED-001
    finding: "Urban Context Analysis Pre-Programme Design Task — How should a humanitarian organisation approach context analysis before programme design in an urban displacement setting? → S-2017-iied-urban-context-analysis-toolkit-guidance-note-SEED-001"
    knowledge_layer: operational
    source_pages: "pp. 7–11, 34"
    field_query_trigger: not-applicable
    candidate_target_pages:
      - wiki/aba/02-concepts/urban-context-analysis.md
      - wiki/aba/04-tools/urban-context-analysis-process.md
    integration_action: create-concept
    routing_rationale: High-priority seed pointing to the CONCEPT-001 and METHOD-001 pages to be created; high coverage, actionable with existing objects.
    human_review_required: false

  - finding_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-F-061
    object_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-SEED-002
    finding: "Context Analysis for Area-Based Programme Design Task — How does urban context analysis support the design of area-based humanitarian programmes? → S-2017-iied-urban-context-analysis-toolkit-guidance-note-SEED-002"
    knowledge_layer: operational
    source_pages: "pp. 8–9, 15–16"
    field_query_trigger: not-applicable
    candidate_target_pages:
      - wiki/aba/02-concepts/sub-area-unit-of-analysis.md
      - wiki/aba/02-concepts/entry-point-identification.md
    integration_action: create-concept
    routing_rationale: High-priority seed requiring cross-source synthesis; coverage partial — routes to sub-area and entry-point concept pages.
    human_review_required: false

  - finding_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-F-062
    object_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-SEED-003
    finding: "Context Analysis Update Decision Protocol Task — When and under what conditions should a humanitarian organisation update or redo its urban context analysis? → S-2017-iied-urban-context-analysis-toolkit-guidance-note-SEED-003"
    knowledge_layer: decision
    source_pages: "p. 33"
    field_query_trigger: not-applicable
    candidate_target_pages:
      - wiki/aba/09-decision-protocols/context-analysis-reassessment-trigger.md
    integration_action: create-decision-rule
    routing_rationale: High-priority seed directly served by RULE-002 and RISK-004; routes to the reassessment trigger decision protocol.
    human_review_required: false

  - finding_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-F-063
    object_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-SEED-004
    finding: "Urban Context Analysis Toolkit Inventory Task — What tools and instruments are available for conducting urban context analysis in a displacement setting, and how are they used? → S-2017-iied-urban-context-analysis-toolkit-guidance-note-SEED-004"
    knowledge_layer: diagnostic
    source_pages: "pp. 10–11, 34"
    field_query_trigger: not-applicable
    candidate_target_pages:
      - wiki/aba/04-tools/urban-context-analysis-process.md
      - wiki/aba/05-field-instruments/iied-2017-urban-context-analysis-kii-fgd-guides.md
    integration_action: create-tool
    routing_rationale: High-priority seed; all 10 tools have individual target pages; full coverage but requires external access to IRC Box links for actual template content.
    human_review_required: false

  - finding_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-F-064
    object_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-SEED-005
    finding: "Partner Inclusion Decision Task — How should a humanitarian organisation decide whether to include local partners in a context analysis, and what risks does joint analysis introduce? → S-2017-iied-urban-context-analysis-toolkit-guidance-note-SEED-005"
    knowledge_layer: decision
    source_pages: "p. 14"
    field_query_trigger: not-applicable
    candidate_target_pages:
      - wiki/aba/09-decision-protocols/partner-inclusion-in-context-analysis.md
    integration_action: create-decision-rule
    routing_rationale: Medium-priority seed; served by RULE-003, RULE-010, RISK-003, IMPL-003; routes to partner inclusion decision protocol.
    human_review_required: false

  - finding_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-F-065
    object_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-SEED-006
    finding: "Urban Data Collection Risks and Mitigations Task — What are the key data collection risks in urban humanitarian assessments, and how can they be mitigated? → S-2017-iied-urban-context-analysis-toolkit-guidance-note-SEED-006"
    knowledge_layer: operational
    source_pages: "pp. 26–28"
    field_query_trigger: not-applicable
    candidate_target_pages:
      - wiki/aba/06-risks/sampling-bias-powerholder-dependence.md
      - wiki/aba/06-risks/data-collection-exposure-risk-displaced-populations.md
    integration_action: create-risk
    routing_rationale: Medium-priority seed; served by RISK-001, RISK-002, SAFE-001, SAFE-002, LESSON-002; routes to two new risk pages.
    human_review_required: false

  - finding_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-F-066
    object_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-SEED-007
    finding: "Sub-Area Definition and Selection Task — How should urban humanitarian actors define and select sub-areas for context analysis and programme targeting? → S-2017-iied-urban-context-analysis-toolkit-guidance-note-SEED-007"
    knowledge_layer: operational
    source_pages: "pp. 15–16"
    field_query_trigger: not-applicable
    candidate_target_pages:
      - wiki/aba/02-concepts/sub-area-unit-of-analysis.md
    integration_action: create-concept
    routing_rationale: High-priority seed connecting CONCEPT-002, IMPL-002, LESSON-001; routes to sub-area concept page with selection criteria.
    human_review_required: false

  - finding_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-F-067
    object_id: S-2017-iied-urban-context-analysis-toolkit-guidance-note-SEED-008
    finding: "Context Analysis vs Needs Assessment Relationship Task — What is the relationship between context analysis and needs assessment, particularly when resources are constrained and both cannot be conducted fully? → S-2017-iied-urban-context-analysis-toolkit-guidance-note-SEED-008"
    knowledge_layer: conceptual
    source_pages: "pp. 8–9"
    field_query_trigger: not-applicable
    candidate_target_pages:
      - wiki/aba/02-concepts/context-analysis-vs-needs-assessment.md
      - wiki/aba/07-known-tensions/context-analysis-vs-needs-assessment-tension.md
    integration_action: create-concept
    routing_rationale: Routes to CONCEPT-003 page and a known tension page; source addresses substitution question explicitly.
    human_review_required: false
```

---

<a id="task-seeds"></a>
## Task Seeds

**SEED-001** `S-2017-iied-urban-context-analysis-toolkit-guidance-note-SEED-001`
*Urban Context Analysis Pre-Programme Design*
How should a humanitarian organisation approach context analysis before programme design in an urban displacement setting?
- **Priority:** high | **Type:** planning | **Layer:** operational
- **Coverage:** full | **Contributing objects:** CONCEPT-001, FRAMEWORK-001, TYPOLOGY-001, METHOD-001, TOOL-001, ASM-001
- **Target page:** `wiki/aba/02-concepts/urban-context-analysis.md` / `wiki/aba/04-tools/urban-context-analysis-process.md`
- **Gaps:** toolkit not designed for rapid-onset response; assumes 2-week preparation time; no guidance for access-restricted settings where tools cannot be completed

**SEED-002** `S-2017-iied-urban-context-analysis-toolkit-guidance-note-SEED-002`
*Context Analysis for Area-Based Programme Design*
How does urban context analysis support the design of area-based humanitarian programmes?
- **Priority:** high | **Type:** planning | **Layer:** operational
- **Coverage:** partial | **Contributing objects:** CONCEPT-002, CONCEPT-004, FRAMEWORK-001, IMPL-002, METHOD-001, LESSON-001
- **Target page:** `wiki/aba/02-concepts/sub-area-unit-of-analysis.md` / `wiki/aba/02-concepts/entry-point-identification.md`
- **Gaps:** source describes context analysis inputs but does not connect outputs to ABA programme cycle phases or community mobilisation logic; cross-source synthesis required

**SEED-003** `S-2017-iied-urban-context-analysis-toolkit-guidance-note-SEED-003`
*Context Analysis Update Decision Protocol*
When and under what conditions should a humanitarian organisation update or redo its urban context analysis?
- **Priority:** high | **Type:** monitoring | **Layer:** decision
- **Coverage:** full | **Contributing objects:** RULE-002, RISK-004, ASM-001
- **Target page:** `wiki/aba/09-decision-protocols/context-analysis-reassessment-trigger.md`
- **Gaps:** no structured decision matrix; no guidance for who triggers reassessment; no guidance for resource-constrained settings where full redo is not feasible

**SEED-004** `S-2017-iied-urban-context-analysis-toolkit-guidance-note-SEED-004`
*Urban Context Analysis Toolkit Inventory*
What tools and instruments are available for conducting urban context analysis in a displacement setting, and how are they used?
- **Priority:** high | **Type:** assessment | **Layer:** diagnostic
- **Coverage:** full | **Contributing objects:** TOOL-001–010, METHOD-001
- **Target page:** `wiki/aba/04-tools/urban-context-analysis-process.md` / `wiki/aba/05-field-instruments/iied-2017-urban-context-analysis-kii-fgd-guides.md`
- **Gaps:** actual template content for all 10 tools hosted externally (IRC Box.com); Tools 5A-5G question guide text not reproduced in source

**SEED-005** `S-2017-iied-urban-context-analysis-toolkit-guidance-note-SEED-005`
*Partner Inclusion Decision*
How should a humanitarian organisation decide whether to include local partners in a context analysis, and what risks does joint analysis introduce?
- **Priority:** medium | **Type:** coordination | **Layer:** decision
- **Coverage:** full | **Contributing objects:** RULE-003, RULE-010, RISK-003, IMPL-003, LESSON-002
- **Target page:** `wiki/aba/09-decision-protocols/partner-inclusion-in-context-analysis.md`
- **Gaps:** no guidance on multi-actor coordination mandates (UN cluster system); no guidance on partner withdrawal mid-analysis; limited guidance for competitive partner dynamics

**SEED-006** `S-2017-iied-urban-context-analysis-toolkit-guidance-note-SEED-006`
*Urban Data Collection Risks and Mitigations*
What are the key data collection risks in urban humanitarian assessments, and how can they be mitigated?
- **Priority:** medium | **Type:** assessment | **Layer:** operational
- **Coverage:** partial | **Contributing objects:** RISK-001, RISK-002, SAFE-001, SAFE-002, LESSON-002, RULE-004, RULE-005
- **Target page:** `wiki/aba/06-risks/sampling-bias-powerholder-dependence.md` / `wiki/aba/06-risks/data-collection-exposure-risk-displaced-populations.md`
- **Gaps:** no quantitative representativeness thresholds; no digital data collection security; limited guidance when no community-matched team members are available

**SEED-007** `S-2017-iied-urban-context-analysis-toolkit-guidance-note-SEED-007`
*Sub-Area Definition and Selection*
How should urban humanitarian actors define and select sub-areas for context analysis and programme targeting?
- **Priority:** medium | **Type:** planning | **Layer:** operational
- **Coverage:** partial | **Contributing objects:** CONCEPT-002, IMPL-002, RULE-003, LESSON-001, TOOL-004
- **Target page:** `wiki/aba/02-concepts/sub-area-unit-of-analysis.md`
- **Gaps:** no spatial delineation methodology; assumes prior organisational knowledge of displacement concentrations; no guidance for contexts without reliable spatial data or maps

**SEED-008** `S-2017-iied-urban-context-analysis-toolkit-guidance-note-SEED-008`
*Context Analysis vs Needs Assessment Relationship*
What is the relationship between urban context analysis and sector needs assessments — can one substitute for the other?
- **Priority:** medium | **Type:** coordination | **Layer:** conceptual
- **Coverage:** partial | **Contributing objects:** CONCEPT-003, CONCEPT-001, ASM-003, RULE-002
- **Target page:** `wiki/aba/02-concepts/context-analysis-vs-needs-assessment.md` / `wiki/aba/07-known-tensions/context-analysis-vs-needs-assessment-tension.md`
- **Gaps:** no sequencing decision framework; no guidance for resource-constrained settings where only one can be done; no practical guidance on how findings from each feed into the other

---

<a id="integration-map"></a>
## Integration Map

> All IDs share prefix `S-2017-iied-urban-context-analysis-toolkit-guidance-note-`. Short forms used below for readability.

| finding_id | object_id | label | type | layer | target (short) | action | status |
|---|---|---|---|---|---|---|---|
| F-001 | FRAMEWORK-001 | Urban CA Thematic Framework | FRAMEWORK | conceptual | 03-frameworks/urban-context-analysis-framework | create-framework | proposed |
| F-002 | TYPOLOGY-001 | Urban Displacement Crisis Typology | TYPOLOGY | conceptual | 02-concepts/urban-displacement-crisis-typology | create-concept | proposed |
| F-003 | CONCEPT-001 | Urban Context Analysis | CONCEPT | conceptual | 02-concepts/urban-context-analysis | create-concept | proposed |
| F-004 | CONCEPT-002 | Sub-Area Unit of Analysis | CONCEPT | conceptual | 02-concepts/sub-area-unit-of-analysis | create-concept | proposed |
| F-005 | CONCEPT-003 | CA vs Needs Assessment | CONCEPT | conceptual | 02-concepts/context-analysis-vs-needs-assessment | create-concept | proposed |
| F-006 | CONCEPT-004 | Entry Point Identification | CONCEPT | conceptual | 02-concepts/entry-point-identification | create-concept | proposed |
| F-007 | PRINCIPLE-001 | Do No Harm Principle | PRINCIPLE | conceptual | 02-concepts/do-no-harm-principle | create-concept | proposed |
| F-008 | PRINCIPLE-002 | Gender Equality Analytical Lens | PRINCIPLE | conceptual | 02-concepts/gender-equality-analytical-lens | create-concept | proposed |
| F-009 | METHOD-001 | Urban CA Process (3-phase 10-step) | METHOD | diagnostic | 04-tools/urban-context-analysis-process | create-tool | proposed |
| F-010 | METHOD-002 | Desk Review Method | METHOD | diagnostic | 04-tools/desk-review-method-urban-context-analysis | create-tool | proposed |
| F-011 | METHOD-003 | Key Informant Interview Method | METHOD | diagnostic | 04-tools/key-informant-interview-method | create-tool | proposed |
| F-012 | METHOD-004 | Focus Group Discussion Method | METHOD | diagnostic | 04-tools/focus-group-discussion-method-urban | create-tool | proposed |
| F-013 | METHOD-005 | Stakeholder Analysis / Actor Mapping | METHOD | diagnostic | 04-tools/stakeholder-analysis-actor-mapping | create-tool | proposed |
| F-014 | METHOD-006 | Participatory Validation Workshop Method | METHOD | diagnostic | 04-tools/participatory-validation-workshop-method | create-tool | proposed |
| F-015 | METHOD-007 | Systems-Thinking Analytical Approach | METHOD | diagnostic | 03-frameworks/urban-context-analysis-framework | enrich-framework | proposed |
| F-016 | METHOD-008 | Snowball/Referral Sampling | METHOD | diagnostic | 04-tools/snowball-referral-sampling-method | create-tool | proposed |
| F-017 | TOOL-001 | Workplan and Budget Template | TOOL | diagnostic | 04-tools/iied-2017-...tool-1-workplan | create-tool | proposed |
| F-018 | TOOL-002 | Desk Review Summary Template | TOOL | diagnostic | 04-tools/iied-2017-...tool-2-desk-review-summary | create-tool | proposed |
| F-019 | TOOL-003 | Stakeholder Analysis Matrix | TOOL | diagnostic | 04-tools/iied-2017-...tool-3-stakeholder-matrix | create-tool | proposed |
| F-020 | TOOL-004 | Data Collection Plan Template | TOOL | diagnostic | 04-tools/iied-2017-...tool-4-data-collection-plan | create-tool | proposed |
| F-021 | TOOL-005 | KII/FGD Question Guides (5A–5G) | TOOL | diagnostic | 05-field-instruments/iied-2017-...kii-fgd-guides | create-field-instrument | proposed |
| F-022 | TOOL-006 | KII/FGD Debrief Template | TOOL | diagnostic | 04-tools/iied-2017-...tool-6-debrief-template | create-tool | proposed |
| F-023 | TOOL-007 | Key Findings Analysis Template | TOOL | diagnostic | 04-tools/iied-2017-...tool-7-key-findings | create-tool | proposed |
| F-024 | TOOL-008 | Programme Implications Template | TOOL | diagnostic | 04-tools/iied-2017-...tool-8-programme-implications | create-tool | proposed |
| F-025 | TOOL-009 | Validation Workshop Tool | TOOL | diagnostic | 04-tools/iied-2017-...tool-9-validation-workshop | create-tool | proposed |
| F-026 | TOOL-010 | Final Report Outline | TOOL | diagnostic | 04-tools/iied-2017-...tool-10-final-report-outline | create-tool | proposed |
| F-027 | RULE-001 | Separate FGDs by Gender/Age | RULE | decision | 09-decision-protocols/fgd-gender-age-separation-protocol | create-decision-rule | proposed |
| F-028 | RULE-002 | CA Reassessment Trigger | RULE | decision | 09-decision-protocols/context-analysis-reassessment-trigger | create-decision-rule | proposed |
| F-029 | RULE-003 | Partner Inclusion Restriction | RULE | decision | 09-decision-protocols/partner-inclusion-in-context-analysis | create-decision-rule | proposed |
| F-030 | RULE-004 | Do No Harm Data Collection | RULE | decision | 09-decision-protocols/do-no-harm-data-collection-checklist | create-decision-rule | proposed |
| F-031 | RULE-005 | Participant Data Protection | RULE | decision | 09-decision-protocols/participant-data-protection-protocol | create-decision-rule | proposed |
| F-032 | RULE-006 | Triangulation Requirement | RULE | decision | 09-decision-protocols/qualitative-triangulation-requirement | create-decision-rule | proposed |
| F-033 | RULE-007 | Desk Review Before Fieldwork | RULE | decision | 09-decision-protocols/desk-review-sequencing-rule | create-decision-rule | proposed |
| F-034 | RULE-008 | Question Guide Adaptation | RULE | decision | 09-decision-protocols/question-guide-adaptation-protocol | create-decision-rule | proposed |
| F-035 | RULE-009 | Gender-Only Analysis Tool Selection | RULE | decision | 09-decision-protocols/assessment-tool-selection-gender-only | create-decision-rule | proposed |
| F-036 | RULE-010 | Participatory Planning Workshop Trigger | RULE | decision | 09-decision-protocols/participatory-planning-workshop-trigger | create-decision-rule | proposed |
| F-037 | RULE-011 | Women-Only Validation Workshop Groups | RULE | decision | 09-decision-protocols/fgd-gender-age-separation-protocol | enrich-decision-rule | proposed |
| F-038 | RULE-012 | Sensitive Findings Internal-Only Report | RULE | decision | 09-decision-protocols/context-analysis-report-sensitivity-protocol | create-decision-rule | proposed |
| F-039 | RULE-013 | Culturally-Matched Team Composition | RULE | decision | 09-decision-protocols/team-composition-cultural-matching-rule | create-decision-rule | proposed |
| F-040 | IMPL-001 | Team Composition and Roles | IMPL | operational | 04-tools/urban-context-analysis-process | enrich-tool | proposed |
| F-041 | IMPL-002 | Sub-Area Selection and Prioritization | IMPL | operational | 02-concepts/sub-area-unit-of-analysis | enrich-concept | proposed |
| F-042 | IMPL-003 | Joint/Partner Analysis Design | IMPL | operational | 09-decision-protocols/partner-inclusion-in-context-analysis | enrich-decision-rule | proposed |
| F-043 | IMPL-004 | Team Training and Orientation | IMPL | operational | 04-tools/urban-context-analysis-process | enrich-tool | proposed |
| F-044 | IMPL-005 | Daily Debrief and Mid-Collection Review | IMPL | operational | 04-tools/iied-2017-...tool-6-debrief-template | enrich-tool | proposed |
| F-045 | IMPL-006 | Findings Communication and Dissemination | IMPL | operational | 04-tools/urban-context-analysis-process | enrich-tool | proposed |
| F-046 | IMPL-007 | Question Guide Adaptation Process | IMPL | operational | 05-field-instruments/iied-2017-...kii-fgd-guides | enrich-field-instrument | proposed |
| F-047 | RISK-001 | Sampling Bias — Powerholder Dependence | RISK | diagnostic | 06-risks/sampling-bias-powerholder-dependence | create-risk | proposed |
| F-048 | RISK-002 | Protection Risk — Data Collection Exposure | RISK | diagnostic | 06-risks/data-collection-exposure-risk-displaced-populations | create-risk | proposed |
| F-049 | RISK-003 | Partner Bias in Joint Analysis | RISK | diagnostic | 06-risks/partner-bias-joint-analysis-risk | create-risk | proposed |
| F-050 | RISK-004 | Context Analysis Staleness | RISK | diagnostic | 06-risks/context-analysis-staleness-risk | create-risk | proposed |
| F-051 | LESSON-001 | Dar es Salaam Sub-Area Selection | LESSON | operational | 02-concepts/sub-area-unit-of-analysis | enrich-concept | proposed |
| F-052 | LESSON-002 | Dar es Salaam Identity Masking | LESSON | operational | 06-risks/data-collection-exposure-risk-displaced-populations | enrich-risk | proposed |
| F-053 | LESSON-003 | Maiduguri Dual-Document | LESSON | operational | 09-decision-protocols/context-analysis-report-sensitivity-protocol | enrich-decision-rule | proposed |
| F-054 | ASM-001 | Country Presence Assumption | ASM | conceptual | 02-concepts/urban-context-analysis | enrich-concept | proposed |
| F-055 | ASM-002 | Representative Sampling Assumption | ASM | conceptual | 06-risks/sampling-bias-powerholder-dependence | enrich-risk | proposed |
| F-056 | ASM-003 | Optional Final Report Assumption | ASM | conceptual | 02-concepts/urban-context-analysis | enrich-concept | proposed |
| F-057 | SAFE-001 | Data Collection Protection Protocol | SAFE | operational | 09-decision-protocols/participant-data-protection-protocol | enrich-decision-rule | proposed |
| F-058 | SAFE-002 | Culturally-Matched Team Safeguard | SAFE | operational | 09-decision-protocols/team-composition-cultural-matching-rule | enrich-decision-rule | proposed |
| F-059 | TNS-001 | Sampling Representativeness Tension | TNS | conceptual | 07-known-tensions/sampling-representativeness-vs-structural-access-barriers | create-risk | proposed |
| F-060 | SEED-001 | Urban CA Pre-Programme Design Task | SEED | operational | 02-concepts/urban-context-analysis | create-concept | proposed |
| F-061 | SEED-002 | CA for ABA Programme Design Task | SEED | operational | 02-concepts/sub-area-unit-of-analysis | create-concept | proposed |
| F-062 | SEED-003 | CA Update Decision Protocol Task | SEED | decision | 09-decision-protocols/context-analysis-reassessment-trigger | create-decision-rule | proposed |
| F-063 | SEED-004 | Toolkit Inventory Task | SEED | diagnostic | 04-tools/urban-context-analysis-process | create-tool | proposed |
| F-064 | SEED-005 | Partner Inclusion Decision Task | SEED | decision | 09-decision-protocols/partner-inclusion-in-context-analysis | create-decision-rule | proposed |
| F-065 | SEED-006 | Data Collection Risks Task | SEED | operational | 06-risks/sampling-bias-powerholder-dependence | create-risk | proposed |
| F-066 | SEED-007 | Sub-Area Selection Task | SEED | operational | 02-concepts/sub-area-unit-of-analysis | create-concept | proposed |
| F-067 | SEED-008 | CA vs Needs Assessment Task | SEED | conceptual | 02-concepts/context-analysis-vs-needs-assessment | create-concept | proposed |

### Source-Level Synthesis

**Total objects extracted:** 67 (across all workers)

**Distribution by type:**
| Type | Count |
|---|---|
| FRAMEWORK | 1 |
| TYPOLOGY | 1 |
| CONCEPT | 4 |
| PRINCIPLE | 2 |
| METHOD | 8 |
| TOOL | 10 |
| RULE | 13 |
| IMPL | 7 |
| RISK | 4 |
| LESSON | 3 |
| ASM | 3 |
| SAFE | 2 |
| TNS | 1 |
| SEED | 8 |
| **Total** | **67** |

**Key integration priority:** High — this source introduces the most complete urban context analysis methodology in the wiki. Top integration actions: (1) create `wiki/aba/02-concepts/urban-context-analysis.md`; (2) create `wiki/aba/03-frameworks/urban-context-analysis-framework.md`; (3) create `wiki/aba/04-tools/urban-context-analysis-process.md`; (4) create 13 decision protocol entries in `wiki/aba/09-decision-protocols/`; (5) create `wiki/aba/05-field-instruments/iied-2017-urban-context-analysis-kii-fgd-guides.md`.

**Comparison readiness:** medium — framework, typology, and concept objects are comparable to Parker & Maynard 2015, Sanderson & Sitko 2017, and GlobalCluster 2019 definitions. Sub-area definition (CONCEPT-002) directly extends Parker & Maynard 2015. Entry point identification (CONCEPT-004) complements Sanderson & Sitko 2017 ABA definition. Full COMP objects deferred to Writer assembly.

**Gate A items:** 2 findings flagged human_review_required: true — F-029 (RULE-003, partner inclusion restriction: requires contextual judgment not fully specified in source) and F-059 (TNS-001, sampling representativeness tension: unresolved methodological contradiction).
