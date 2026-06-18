

## Purpose
Build and maintain concept pages in 02-concepts/ using material drawn
exclusively from extracted source files in 01-sources/extracted/. Concepts
are identified incrementally as sources arrive, held in a candidate queue
before any page is created, and promoted through human-reviewed maturity
gates based on evidence quality — not source count alone.

The process serves three primary user personas:
- Field team lead: needs to know what a concept obliges them to do
  differently today
- Programme designer: needs to know when and how to apply a concept
  across a project lifecycle
- Researcher/reviewer: needs to trace claims to specific sources and
  understand where definitions are contested

Success criteria:
- Every concept page answers "what does this oblige me to do differently?"
  in the Practical Implications section
- Every claim traces to a specific source file and page reference
- No concept page contains a claim that cannot be linked to a user need
If a process step cannot be linked to one of these personas or criteria,
it is a candidate for removal.

---

## File Structure

    02-concepts/
      [concept-slug].md         Readable concept summaries — human-curated

    02-concepts/archive/
      [concept-slug].md         Deprecated concepts — searchable, not active

    02-concepts/versions/
      [slug]-YYYY-MM-DDTHHMMSS.md   Timestamped pre-change snapshots

    system/
      concept-candidates.md          Pending concepts awaiting human review
      concept-candidates-cold.md     Candidates inactive >90 days
      concept-candidates-duplicate-check.md   Near-duplicate candidates
      concept-inventory.generated.md Regenerated metadata — never edited manually
      concept-governance-log.md      Human decisions — never overwritten by workflow
      concept-relationships.md       Relationship map between concepts
      concept-cleanup-queue.md       Active flags requiring review
      concept-deferred.md            Overdue cleanup items — searchable, no reminders
      concept-change-log.md          Record of every automated modification
      concept-health.md              Generated triage report — see Scale section

Integrity rule for generated files:
Every generated file carries a checksum in its first line:
    <!-- checksum: [hash] generated: YYYY-MM-DDTHHMMSS -->
If a generated file is manually edited, checksum fails at next ingest.
System alerts: "Generated file modified manually — regenerate from sources?"
Generated files contain generated data only.
Human decision files contain human decisions only.
Where both types must coexist (concept-candidates.md), use in-file
section markers:
    <!-- auto-generated --> ... <!-- /auto-generated -->
    <!-- human-decision --> ... <!-- /human-decision -->

---

## Maturity Model

Maturity is expressed on two independent dimensions stored separately
in frontmatter. A derived human-friendly label is generated from them.

Evidence strength:
- single-source   — one extracted source defines or uses the concept
- multi-source    — two or more sources; independence assessed
- triangulated    — three or more independent sources confirmed

Consensus state:
- stable     — sources agree on meaning and application
- emerging   — sources partially agree; some variation in framing
- contested  — sources disagree on meaning, referent, or validity

Derived maturity label (generated, not manually assigned):

| Evidence Strength | Consensus State | Derived Label |
|---|---|---|
| single-source | any | provisional |
| multi-source | stable or emerging | supported |
| multi-source | contested | contested |
| triangulated | stable or emerging | supported |
| triangulated | contested | contested |

Deprecated is a lifecycle state, not a maturity level.
It is set explicitly through the retirement workflow.

Frontmatter fields:

    evidence_strength: [single-source | multi-source | triangulated]
    consensus_state: [stable | emerging | contested]
    maturity: [provisional | supported | contested]   # derived — do not edit manually

---

## Evidence Quality Rubric
Used at every maturity gate. Scores recorded in the promotion case block.

For each factor, assess: low / medium / high

Source authority:
- low    — informal practitioner note, grey literature, undated
- medium — practitioner guide, NGO evaluation, working paper
- high   — peer-reviewed study, systematic review, authoritative
           inter-agency standard (e.g., SPHERE)

Source independence:
- confirmed         — evidence bases clearly distinct
- likely-independent — no shared citations found; not confirmed
- unknown           — cannot assess from extracted content
- likely-dependent  — shares citations or underlying evaluation

Definition clarity:
- low    — term used without definition or with ambiguous framing
- medium — definition present but partial or context-dependent
- high   — precise, bounded definition with stated scope

Operational usefulness:
- low    — concept is descriptive only; no action implied
- medium — concept implies action but conditions are unclear
- high   — concept directly changes what a practitioner does;
           conditions stated

Currency:
- current — most recent source within 5 years
- aging   — most recent source 5–10 years ago
- stale   — most recent source >10 years ago, or predates a known
            field evolution

Contestation depth:
- low    — no conflation, misuse, or validity challenges documented
- medium — conflation or misuse documented; no validity challenges
- high   — validity challenges documented from one or more sources

Minimum combinations for evidence-strength promotion:

    single-source → multi-source:
      Independence: likely-independent or confirmed
      At least two factors at medium or high
      No factor assessed that actively blocks (e.g., likely-dependent
      independence alone does not block if three other factors are high,
      but adds a visible caveat)

    multi-source → triangulated:
      Independence: confirmed for at least two of three sources
      At least three factors at high
      Currency: current or aging (stale blocks triangulated)

Independence as a gate:
Independence is a strong criterion, not a hard binary block.
- confirmed or likely-independent: promotion proceeds normally
- unknown: promotion proceeds with visible caveat on concept page
- likely-dependent: promotion proceeds only if three or more other
  factors are high; caveat added; third independent source recommended
Record independence_assessment in frontmatter.

---

## Ingest Mode
Runs on every new source added to 01-sources/extracted/

### Step 1 — Extract Concept Candidates
Read the new extracted source file. From the # Key concepts section,
extract every concept candidate. Record:
- Concept name (term before the colon)
- Definition as stated
- Source filename and page reference

### Step 2 — Similarity Check Before Queue Entry
Before adding a candidate to the queue, run a lightweight deduplication
check against existing concept slugs and detected_labels in inventory:
- Normalise labels: lowercase, remove punctuation, stem key terms
- If normalised label matches existing slug or known variant exactly:
  treat as existing concept (proceed to Step 3)
- If similarity is high (token overlap >70% or Levenshtein distance <3):
  add to concept-candidates-duplicate-check.md with suggested merge
  target; do not add to main candidate queue
- If no match: add to main candidate queue

### Step 3 — Check Each Candidate Against the Concept Inventory

Candidate flagged as near-duplicate:
- Hold in concept-candidates-duplicate-check.md
- Surface at session open for human review: merge, create separately,
  or reject

Concept does not exist in vault:
- Do NOT create a concept page automatically
- Add to system/concept-candidates.md:

    <!-- auto-generated -->
    slug: [proposed-concept-slug]
    label: [term as stated in source]
    source: [filename]
    page: [p. X]
    definition: "[as stated]"
    detected: YYYY-MM-DD
    status: pending
    <!-- /auto-generated -->

Concept exists in vault:
- Determine update type (see Update Types below)
- Apply minor evidence adds automatically with full logging in
  concept-change-log.md (citation adds, source_count increment)
- Flag definition variants and contested meanings for human review
- Any change to the # Definition section requires human review —
  no exceptions
- Set rewrite_triggered_by and compute update_impact (see below)
- Update concept-inventory.generated.md

Concept exists as contested:
- Record new source evidence in the Evidence Base section
- Do not attempt to resolve the contest automatically
- Flag in concept-cleanup-queue.md for human review

### Step 4 — Compute Update Impact
Replace binary rewrite_triggered_by flag with a structured update_summary:

    update_summary:
      triggered_by: [source-filename]
      change_types:
        minor_citation_adds: [n]
        definition_variants: [n]
        contested_meanings: [n]
        new_sources_added: [n]
        validity_challenges: [n]
      update_impact: [low | medium | high | critical]   # computed
      rewrite_priority: [none | low | high | urgent]    # derived from impact;
                                                         # human override requires comment

Impact computation:
- low      — citation adds only
- medium   — definition variant added; no meaning change
- high     — contested meaning found; definition section affected
- critical — validity challenge found; or independence assessment
             changed to likely-dependent

### Step 5 — Update Generated Inventory
Regenerate system/concept-inventory.generated.md in full.
Fields per concept:

    slug:
    evidence_strength:
    consensus_state:
    maturity:           # derived
    source_count:
    last_seen: YYYY-MM-DD
    source_files: [list]
    detected_labels: [list]
    independence_assessment:
    update_summary:     # latest only
    concept_health:     # see Scale section

File opens with checksum line. Never edited manually.

### Step 6 — Update Change Log
For every automated modification in this ingest, append to
concept-change-log.md:

    date: YYYY-MM-DD
    source_ingested: [filename]
    concept: [slug]
    change_type: [minor-citation | definition-variant | contested-meaning |
                  source-count-increment | inventory-update]
    before: "[affected snippet or field value]"
    after: "[new snippet or field value]"
    triggered_by: [source-filename]

### Step 7 — Close Ingest
Surface the following at next session open:
- New candidates in concept-candidates.md
- Near-duplicates in concept-candidates-duplicate-check.md
- Flagged items in concept-cleanup-queue.md
- Concepts with update_impact high or critical
Stop. Do not create concept pages or change Definition sections without
human review.

---

## Review Mode
Runs at session open. Human reviews queues before any new work begins.

### Candidate Queue Review
For each pending entry, LLM presents:

    CANDIDATE: [proposed-slug]
    Label as stated: "[term]"
    Source: [filename, p. X]
    Definition: "[as stated]"
    Near-duplicate check: [none | possible match: [existing-slug]]

    Review questions:
    - Is this concept meaningful and distinct?
    - Is it a duplicate or near-duplicate of an existing concept?
    - Does it belong inside an existing concept page instead?
    - Is the label consistent with how the source uses it?
    - Is this concept useful enough to maintain?
    - Does it answer a question one of the three user personas would ask?

    Proposed action: [create provisional | merge into existing |
                      create as split candidate | reject | defer]
    Awaiting decision.

Human options:
- Approve — LLM creates provisional concept page
- Merge — candidate folded into existing page as a variant
- Split candidate — existing concept flagged for splitting (see below)
- Reject — removed from queue; reason logged in governance log
- Defer — stays in queue with review_due date set

Candidates inactive for >90 days are moved to concept-candidates-cold.md
and removed from the active queue. They remain searchable and can be
revived by moving back to the active queue.

All decisions logged in concept-governance-log.md:

    date: YYYY-MM-DD
    concept: [slug]
    decision: [approved | merged | rejected | deferred | split-flagged]
    reviewer: [name]
    reason: "[brief note]"

### Cleanup Queue Review
Two-stage escalation — no content is ever automatically deleted:

Stage 1: Item flagged in concept-cleanup-queue.md with:

    flag_date: YYYY-MM-DD
    review_due: YYYY-MM-DD
    reason: "[why flagged]"
    impact: [low | medium | high]

At review_due, if not reviewed: status changes to overdue.
Item is surfaced prominently at next session open.

Stage 2: If still unreviewed after 2× the original review period:
item moves to concept-deferred.md. No reminders. Searchable.
Does not block any workflow.

No content is ever automatically archived or deleted.
A human must always confirm one of five outcomes:
1. validate  — content is correct; flag removed
2. revise    — LLM drafts revision; human approves before page changes
3. merge     — content belongs in another page
4. archive   — page moved to 02-concepts/archive/; redirect stub left
               in 02-concepts/; inventory updated
5. delete    — permanent removal; requires explicit human command;
               logged in governance log; no undo

Low-impact items deferred twice are moved to concept-deferred.md and
removed from the active queue. They do not count as resolved — they
are deprioritised.

---

## Update Types
Terminology clarification:
- Promotion applies exclusively to maturity-level changes
- Update applies to evidence adds, source counts, and non-definition changes

| Update Type | Trigger | Review Required | Action |
|---|---|---|---|
| Minor evidence add | New citation supports existing definition | None | Auto-applied; logged in change log |
| Source count increment | New source references concept | None | Auto-applied; inventory updated |
| Definition variant | Same concept, different formulation | Yes — definition section change | Flag for review; hold until approved |
| Contested meaning | Same label, different referent | Yes — high impact | Flag as contested; add to cleanup queue |
| Validity challenge | Source argues concept is not useful | Yes — critical impact | Flag immediately; surface at next session open |
| Maturity change | Evidence quality justifies promotion | Yes — human approval required | Promotion mode triggered after approval |
| Structural rewrite | Major synthesis or page format changes | Yes — human approval required | Full-file pass after approval |

Any change to the # Definition section requires human review.
No exceptions.

---

## Promotion Mode
Runs only when human approves a maturity change from the review queue.

### Step 1 — Save Snapshot
Before any change to the concept page, save a timestamped copy:

    02-concepts/versions/[slug]-YYYY-MM-DDTHHMMSS.md

### Step 2 — LLM Presents Promotion Case
LLM presents evidence quality rubric scores and promotion case:

    MATURITY CHANGE CANDIDATE: [concept-slug]
    Current: evidence_strength=[x] consensus_state=[x] maturity=[x]
    Proposed: evidence_strength=[x] consensus_state=[x] maturity=[x]

    Evidence Quality Rubric:
    - Source authority:       [low | medium | high] — [brief note]
    - Source independence:    [confirmed | likely-independent | unknown |
                               likely-dependent] — [brief note]
    - Definition clarity:     [low | medium | high] — [brief note]
    - Operational usefulness: [low | medium | high] — [brief note]
    - Currency:               [current | aging | stale] — [brief note]
    - Contestation depth:     [low | medium | high] — [brief note]

    Minimum combination met: [yes | no | with caveat]
    Caveat (if any): "[e.g., independence unknown — third source recommended]"

    Sources:
    - [Source A, year] — definition: "..." (p. X)
    - [Source B, year] — definition: "..." (p. X)

    Blocking conditions: [none | list]
    Proposed action: rewrite to [evidence_strength / consensus_state]
    Awaiting confirmation.

Human options:
- Approve — proceed to targeted pass
- Block — set promotion_blocked_by: [reason]; log in governance log
- Redirect — human provides instruction

### Step 3 — Focused Full-File Pass
Scoped to three high-signal sections for routine promotion:
- # Key concepts
- # Summary
- # Operational implications OR # DRR implications
  (choose based on concept's primary user persona)

Full collection from all 10 sections is reserved for an explicit
deep-dive mode that the human requests. It is not triggered
automatically by a maturity change.

Negative-space tracking: record only when one of two conditions applies:
a) The undefined usage contradicts a definition from another source
b) The undefined usage would cause a field team to take a materially
   different and likely harmful action
All other undefined usages noted silently in source-level remarks only
— not surfaced to concept page or cleanup queue.

### Step 4 — Draft Revision and Diff Review
LLM drafts the revised concept page. Before the new version becomes
active, present a diff to the human for approval:
- Side-by-side display of # Definition and # Evidence Base sections
  (before and after)
- Summary of all other changes
Human approves diff → new version becomes active page
Human rejects or redirects → snapshot restored; changes discarded

### Step 5 — Rewrite Concept Page In Place
Do not delete the existing page. Enrich and promote it.

Map collected material to concept page sections precisely:

| Collected From | Maps To Concept Page Section |
|---|---|
| # Key concepts | # Definition |
| # Summary | # Why It Matters |
| # Claims worth citing | # Evidence Base |
| # Limitations / cautions | # How This Concept Is Contested or Misused |
| # Coordination implications | # Practical Implications for Field Teams |
| # DRR implications | # Why It Matters (additional bullets) |
| # Operational implications | # Practical Implications for Field Teams |
| # Tools or methods extracted | # Practical Implications (tool references) |
| # Field data collection implications | # Practical Implications |
| # Project lifecycle relevance | # Why It Matters (lifecycle sub-bullets) |

Do not collect from sections that have no home in the concept page structure.

For existing claims:
- If supported by source material: add citation, retain content
- If unsupported: add to concept-cleanup-queue.md with flag_date,
  review_due, and impact level
  Do not delete without human review and explicit decision

### Step 6 — Log the Change
Append to concept-change-log.md:

    date: YYYY-MM-DD
    concept: [slug]
    change_type: maturity-promotion
    previous: evidence_strength=[x] consensus_state=[x]
    new: evidence_strength=[x] consensus_state=[x]
    sources: [list]
    rubric_scores: [summary]
    approved_by: [reviewer]
    snapshot: versions/[slug]-[timestamp].md

---

## Concept Page Structure
Concept pages contain readable summaries only.
Governance state lives in system/ files.
Relationships live in concept-relationships.md.
Tool details live in 04-tools/.

Auto-collected evidence and human-curated sections are separated
by in-file markers where both appear:
    <!-- auto-generated --> ... <!-- /auto-generated -->
    <!-- human-decision --> ... <!-- /human-decision -->

Frontmatter:

    ---
    type: concept
    status: active
    evidence_strength: [single-source | multi-source | triangulated]
    consensus_state: [stable | emerging | contested]
    maturity: [provisional | supported | contested]   # derived — do not edit
    source_count: [n]
    source_independence: [confirmed | likely-independent | unknown | likely-dependent]
    evidence_currency: [current | aging | stale]
    oldest_source: YYYY
    newest_source: YYYY
    currency_note: "[flag if evidence predates a known field evolution]"
    promotion_blocked_by: null
    update_summary:
      update_impact: [low | medium | high | critical]
      rewrite_priority: [none | low | high | urgent]
    created: YYYY-MM-DD
    updated: YYYY-MM-DD
    ---

### # Definition
One paragraph maximum. State the concept as precisely as sources allow.

Convergent sources:
Single authoritative definition. Primary source cited. Most citable
formulation as blockquote:

    > "Direct quote or close paraphrase" — Author (year, p. X)

Partially convergent:
Core shared definition, then variants:

    > Variants across sources:
    > - [Source A (year)]: "..." (p. X)
    > - [Source B (year)]: "..." (p. X)

Contested:
State the contested territory directly. Name each position by source.
Do not synthesize into false consensus.

Provisional pages:
State single-source definition and add:

    > Single-source concept — definition reflects [Source, year] only.
    > Treat as provisional until corroborated.

Independence caveat (add when independence_assessment is unknown
or likely-dependent):

    > Independence unconfirmed — claims may share an underlying evidence
    > base. A third independent source is recommended before treating
    > this as strongly supported.

Do not invent a synthetic definition that no source states.

### # Why It Matters for Urban DRR and Response
2–4 bullets. State what error, misallocation, or coordination failure
this concept prevents when correctly applied. Include lifecycle relevance
where sources specify it.
Derive from: # Summary, # DRR implications, # Operational implications.
Do not restate the definition.
Each bullet must answer a question one of the three user personas would ask.

### # Evidence Base

<!-- auto-generated -->
Organised by source. For each contributing source:

    [Short source label, year]
    - 2–4 bullets from Key concepts, Claims worth citing, Summary.
      Each bullet cites a page.

If same point confirmed across sources:
Cite primary; note "Confirmed in [Source B], [Source C]."

Negative-space entries (only when meaningful — contradicts another
source definition, or would cause materially different harmful action):
- "[Source] uses this concept without definition — [why this matters] (p. X)"
<!-- /auto-generated -->

### # How This Concept Is Contested or Misused
3–5 bullets. Required at every maturity level.

- Common conflation: [what people wrongly equate this with] —
  [why that's wrong per sources]
- Scope limit: [condition under which concept does not apply] —
  [source + page]
- Contested definition: [specific disagreement between sources]

If none documented:
"No conflation or misuse documented in current source set — revisit
as additional sources are ingested."

### # Challenges to Validity
Record when a source argues the concept itself is not useful,
overused, or harmful.

- [Source, year]: argues [summary of challenge] (p. X)

If none documented:
"No validity challenges documented in current source set."

### # Practical Implications for Field Teams
4–6 bullets. Derive from # Operational implications,
# Field data collection implications, # Coordination implications,
# Tools or methods extracted.
Each bullet answers: what does a field practitioner need to do
differently because of this concept?
Where a source attaches a tool, name it. Tool details in 04-tools/.

### # Open Questions
2–4 bullets. State what this concept cannot yet answer.
Do not guess at answers.

Provisional pages: note what a second source would need to confirm
or challenge to enable promotion to supported.

### # Links to Source Pages
- [[../01-sources/extracted/FILENAME]] — [one-line note on contribution]

List every extracted file that defined or substantially used this concept.

---

## Relationships Registry: system/concept-relationships.md
All concept-to-concept relationships stored here, not on concept pages.

    concept-a → concept-b
    type: [prerequisite | component | adjacent | contested-overlap]
    note: "[one line from source material justifying the link]"
    source: [filename, p. X]

Only link concepts that sources explicitly connect.

---

## Concept Retirement Workflow
For concepts that are merged, split, or no longer useful.

### Deprecation
Human sets status: deprecated on concept page.
30-day cooldown begins. Page displays:

    > DEPRECATED — this concept is scheduled for retirement.
    > Reason: [reason]. Effective: [date + 30 days].
    > See: [[replacement-concept-slug]] (if applicable)

At cooldown end, cleanup queue item created:
"Archive deprecated concept [slug]?"

Human confirms: page moves to 02-concepts/archive/
Redirect stub left in 02-concepts/[slug].md:

    ---
    type: redirect
    deprecated: YYYY-MM-DD
    replaced_by: [slug or null]
    reason: "[brief note]"
    ---
    This concept has been deprecated. See [[replacement-concept-slug]].

Inventory updated. Governance log entry created.
Deletion (permanent removal) requires separate explicit human command.
Logged in governance log. No undo.

### Concept Splitting
Triggered when a concept's detected labels diverge into two clearly
separate meanings as more sources arrive.

Flagged during cleanup queue review as: split candidate
LLM presents split proposal:

    SPLIT CANDIDATE: [original-slug]
    Reason: "[detected label divergence — brief description]"

    Proposed split:
    Concept A: [new-slug-a]
      - Label: "[term]"
      - Evidence: [sources that support this meaning]
    Concept B: [new-slug-b]
      - Label: "[term]"
      - Evidence: [sources that support this meaning]

    Original concept: deprecated and cross-referenced to both new concepts.
    Awaiting approval.

Human approves: two new provisional pages created; original deprecated.
Human rejects: split flag removed; concept retained as contested.

---

## Scale and Triage

### Concept Health Metric
Generated in concept-inventory.generated.md and summarised in
system/concept-health.md. Flags:

- source_count > 15: flag for possible splitting or summary condensation
- evidence_currency: stale: flag for review
- consensus_state: contested + no cleanup item: flag as untracked contest
- update_impact: critical + no human review within 14 days: escalate

### Automated House-Keeping (safe — never deletes data)

Candidate queue:
- Entries inactive >90 days: moved to concept-candidates-cold.md
- Removed from active queue; revivable on request

Cleanup queue:
- Low-impact items deferred twice: moved to concept-deferred.md
- Removed from active queue; do not count as resolved

These rules reorganise visibility only. No data is deleted.

---

## Error Recovery

### Versioning
Before any automated change to a concept page, a timestamped snapshot
is saved to 02-concepts/versions/[slug]-YYYY-MM-DDTHHMMSS.md

### Change Log
Every automated modification appended to concept-change-log.md:

    date: YYYY-MM-DD
    source_ingested: [filename]
    concept: [slug]
    change_type: [minor-citation | definition-variant | contested-meaning |
                  source-count-increment | inventory-update | maturity-promotion]
    before: "[affected snippet or field value]"
    after: "[new snippet or field value]"
    triggered_by: [source-filename]

### Diff Review
After any promotion rewrite, a diff of # Definition and # Evidence Base
is presented to the human before the new version becomes the active page.
Human must approve the diff. On rejection, snapshot is restored.

### Checksum Integrity
Generated files carry a checksum header. If a generated file is manually
edited, checksum fails at next ingest. System alerts and offers to
regenerate from sources.

---

## Promotion Checklist
Before finalising a promoted concept page:
- [ ] Snapshot saved before changes applied
- [ ] Evidence quality rubric completed and scores recorded in change log
- [ ] Definition traces to extracted source with page reference
- [ ] Provisional pages marked with single-source caveat
- [ ] Independence caveat added where independence_assessment is
      unknown or likely-dependent
- [ ] All contested definitions named by source, not papered over
- [ ] Negative-space entries recorded only when meaningful
- [ ] "How this concept is contested or misused" substantive or
      explicitly attested as empty
- [ ] "Challenges to validity" present — even if empty by attestation
- [ ] No claims from general knowledge without source file backing
- [ ] source_count matches actual count of contributing files
- [ ] evidence_strength and consensus_state set correctly
- [ ] maturity derived correctly from the two dimensions — not manually set
- [ ] evidence_currency set; currency_note added if aging or stale
- [ ] Concept page contains no governance state, tool details, or
      relationship map
- [ ] update_summary reset after promotion complete
- [ ] Diff reviewed and approved by human
- [ ] concept-inventory.generated.md regenerated
- [ ] concept-governance-log.md updated
- [ ] concept-change-log.md updated
- [ ] concept-health.md regenerated

---

## What Not to Do
- Do not create concept pages automatically — every new concept goes
  to the candidate queue first
- Do not use source count as the sole maturity criterion — assess
  evidence quality using the rubric
- Do not change the # Definition section without human review
- Do not store human decisions in generated files
- Do not store generated data in human decision files
- Do not run a full-file pass for minor evidence adds — reserve for
  maturity changes and structural rewrites
- Do not embed tool details or relationship maps in concept pages
- Do not record negative space for every implied use — only when it
  contradicts another source or implies a harmful action
- Do not auto-archive or auto-delete flagged content — always require
  human confirmation
- Do not skip the diff review before a promotion rewrite becomes active
- Do not write concept definitions from general knowledge
- Do not merge contested definitions into false consensus
- Do not treat existing concept pages as authoritative — treat them
  as drafts to be validated against extracted sources
- Do not skip versioning before any automated page modification