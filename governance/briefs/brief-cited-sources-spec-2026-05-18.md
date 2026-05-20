---
type: brief
status: active
created: 2026-05-18
---

# Brief: Cited Sources Spec + Extracted Source Format Implementation

## Planner Metadata
- Planning tier: 1
- Planner team size: 1 (all context available from session)
- Date: 2026-05-18
- Recommended execution team size: 3

## Objective

Implement the `cited_sources:` field and the full extracted source output spec across all governing infrastructure: schema, index builder, template, agent prompt, skill, and the Twigg dry-run page. When done, any agent running agent-08 will produce a v2.6-compliant extracted source page with a 7-section body, structured findings, and a populated `cited_sources:` block, and the index builder will auto-compute `in_wiki` for each cited source.

## Deliverables

1. `governance/schema/frontmatter-schema.md` — `cited_sources:` added to Source Page Required Extensions
2. `scripts/build-index.py` — `cited_sources` carried through to page_rows in `agent-index.jsonl`; `in_wiki` auto-computed per entry
3. `governance/schema/ingest-rules.md` — v2.5 paths removed; finding completeness and `cited_sources` requirements added
4. `governance/schema/page-types.md` — v2.5 folder references replaced with v2.7 structure
5. `governance/templates/v26/extracted-source-template.md` — full 7-section rewrite with example findings and `cited_sources` block
6. `governance/aba/prompts/agent-08-extracted-source-agent.md` — full output contract replacing 12-bullet stub
7. `governance/aba/librarian/SKILL.md` + `~/.claude/skills/librarian/SKILL.md` — `cited_sources` rule added to EXTRACT and INGEST operations
8. `wiki/aba/01-sources/extracted/2009_twigg-ucl_disaster-resilient-community.md` — `cited_sources:` block populated with key contributing sources from the document

## Context

### `cited_sources:` Schema

Each entry tracks a key contributing source cited by the document (not every footnote — only sources that materially shaped the findings). Structure:

```yaml
cited_sources:
  - raw_citation: "Author (Year) Title — brief description of why it's key"
    wiki_id: S-slug-if-known   # include only when the source is known to be in wiki
    in_wiki: false             # auto-computed by build-index.py; never hand-set
```

Rules:
- `raw_citation`: free text, consistent with how the document cites it; should be recognizable
- `wiki_id`: include only when you know the source is in the wiki — omit entirely otherwise; the index builder will not create ghost nodes from this field
- `in_wiki`: **never set manually**; always auto-computed by the index builder by checking `wiki_id` against `id_to_page`
- Selectivity: key contributing sources only — primary frameworks, foundational research, major guidelines the document builds on or explicitly applies

### Use of `cited_sources` for ingestion prioritization

`in_wiki: true` means the cited source is already processed. When a candidate document cites mostly sources already in wiki, its marginal evidence contribution is lower — can be deprioritized. This score is derivable from the index (count `in_wiki: true` / total `cited_sources` entries per source page).

### Extracted source body spec (7 sections)

All seven sections required; all must have frontmatter `sections:` entry and matching `<a id="..."></a>` anchor in body.

| Section ID | Anchor | Purpose |
|---|---|---|
| `summary` | `#summary` | Author background, document type, scope, how it was produced, coverage in ABA/DRR lifecycle |
| `key-concepts` | `#key-concepts` | Definitions and frameworks introduced or heavily used by the document |
| `methods-and-tools` | `#methods-and-tools` | Methods, tools, instruments, processes the document describes or applies |
| `lifecycle-coverage` | `#lifecycle-coverage` | Which lifecycle stages the document addresses and how |
| `known-tensions` | `#known-tensions` | Tensions, contradictions, or contested positions the document surfaces |
| `findings` | `#findings` | YAML findings list rendered as prose/table (same findings as frontmatter `findings:`) |
| `integration-map` | `#integration-map` | Table mapping each finding to candidate target page, integration action, and status |

### Finding schema (10 required fields)

```yaml
findings:
  - finding_id: F-NNN
    finding: "Exact claim statement, specific and attributable"
    finding_type: <see enum below>
    lifecycle_stage: [<controlled vocab>]
    source_pages: ["p. N", "p. N–N"]
    candidate_target_pages: ["wiki/aba/0X-.../page.md"]  # or ["source_only"]
    integration_action: <see enum below>
    status: pending
    human_review_required: false
    routing_rationale: "Why this target page and action"
```

`finding_type` enum: `concept-definition`, `framework-component`, `process-step`, `tool-description`, `risk-identification`, `tension-surface`, `evidence-gap`, `field-practice`, `monitoring-indicator`, `design-principle`

`integration_action` enum: `create-concept`, `enrich-concept`, `create-framework`, `enrich-framework`, `create-tool`, `enrich-tool`, `create-risk`, `enrich-risk`, `source_only`, `flag-for-review`

### build-index.py change scope

In the `page_rows` construction block (lines ~280–289), add `cited_sources` processing after the existing row dict is built:

```python
if ptype == "source":
    raw_cited = fm.get("cited_sources", []) or []
    cited_out = []
    for entry in raw_cited:
        if not isinstance(entry, dict):
            continue
        wiki_id = entry.get("wiki_id")
        in_wiki = wiki_id in id_to_page if wiki_id else False
        cited_out.append({
            "raw_citation": entry.get("raw_citation"),
            "wiki_id": wiki_id,
            "in_wiki": in_wiki,
        })
    row["cited_sources"] = cited_out
```

Note: this block runs after `id_to_page` is fully built (the for-loop over pages populates id_to_page as it goes — ensure the cited_sources computation happens after the full pass, or handle the two-pass requirement). The current loop builds `id_to_page` incrementally, so `in_wiki` for later pages may miss early-scanned IDs. **Implementation decision**: two-pass approach — first pass builds `id_to_page`, second pass (already existing for edges) is where `cited_sources` should be resolved. Add cited_sources resolution in the edge-resolution pass (after the main for-loop).

### ingest-rules.md fixes

Replace the entire file. Changes:
- Step 4: `06-lifecycle/` → `02-concepts/`, `03-frameworks/`, `04-tools/`, `05-field-instruments/`
- Step 5: Add finding completeness requirement (all 10 fields present, `status: pending`)
- Step 5: Add `cited_sources:` requirement (key contributing sources populated)
- Step 9: `scripts/sync_extracted_frontmatter_to_raw_content.py` → remove (script no longer exists in v2.7)
- Step 9: `python3 scripts/build-index.py` → keep
- Remove reference to `indexes/agent-index.md`
- Update Source Status Values to match current schema

### page-types.md fixes

Replace the Extension Section Types list entirely:
- Remove: `06-lifecycle/`, `07-sector-applications/`, `08-coordination/`, `09-monitoring-learning/`, `10-transition-scale/`, `11-patterns/`, `12-risks-contradictions/`
- Replace with v2.7 folder list from CLAUDE.md: `06-risks/`, `07-known-tensions/`, `08-advisory-playbooks/`, `09-decision-protocols/`, `10-output-templates/`, `11-slice-specs/`, `12-synthesis/`
- Add corresponding page types: `risk`, `known-tension`, `advisory-playbook`, `decision-protocol`, `output-template`, `slice-spec`, `synthesis`
- Remove reference to `sync_extracted_frontmatter_to_raw_content.py`

## Hard Constraints

- Never hand-set `in_wiki:` on any page — it must be auto-computed
- Never include every footnote in `cited_sources:` — key contributing sources only
- `cited_sources:` goes in frontmatter under Source Page Required Extensions, not as a graph edge field
- The Twigg page must not be moved or reclassified — it is the dry-run validation artifact
- Both SKILL.md copies must be updated in sync: vault copy and `~/.claude/skills/librarian/SKILL.md`
- Do not modify `agent-index.jsonl` or any compiled index artifact directly
- Do not change the finding schema — 10 fields are locked

## Soft Constraints

- Keep agent-08 prompt tightly bounded — it is instructions for an LLM agent, not documentation
- Template example findings should use realistic (not trivial) content so it is actionable as a model
- ingest-rules.md and page-types.md rewrites should be minimal — fix only the wrong paths and add the missing rules; preserve structure

## Known Unknowns Resolved

| Question | Finding | Confidence |
|---|---|---|
| Where does cited_sources live in the index? | page_rows in agent-index.jsonl (per-page, not per-finding) | High — confirmed by reading build-index.py lines 280–289 |
| Two-pass or one-pass for in_wiki? | Two-pass: first pass builds id_to_page; cited_sources in_wiki resolved after full scan, in the edge-resolution pass | High — current code already does this for edges |
| Does in_wiki create graph edges? | No — it is bibliographic metadata, not a relationship edge | High — agreed in session |
| How selective is cited_sources? | Key contributing sources only — primary frameworks, foundational research, major guidelines the doc builds on | High — agreed in session |
| How many sections in extracted source body? | 7: summary, key-concepts, methods-and-tools, lifecycle-coverage, known-tensions, findings, integration-map | High — validated by Twigg dry run |
| What files are v2.5 stale? | ingest-rules.md (wrong folder paths, references deleted scripts), page-types.md (old extension section folders) | High — confirmed by reading both files |

## Unresolved Questions

None that block execution.

## Work Units

### WU-1: Schema + Script Changes
- **Objective**: Update frontmatter-schema.md, build-index.py, ingest-rules.md, page-types.md
- **Inputs**:
  - `/Users/eddieargenal/Documents/obsidian-vault/governance/schema/frontmatter-schema.md`
  - `/Users/eddieargenal/Documents/obsidian-vault/scripts/build-index.py`
  - `/Users/eddieargenal/Documents/obsidian-vault/governance/schema/ingest-rules.md`
  - `/Users/eddieargenal/Documents/obsidian-vault/governance/schema/page-types.md`
- **Output**: 4 files updated; no new files created
- **Dependencies**: None — can run first
- **Complexity tier**: Tier 2
- **Validation method**:
  - Run `python3 scripts/build-index.py` from vault root — must produce 0 critical errors
  - Check `indexes/current/agent-index.jsonl` — Twigg row must include `cited_sources: []` (or populated entries if Twigg already has the field)
  - Verify `ingest-rules.md` contains no reference to `06-lifecycle/`, `indexes/agent-index.md`, or `sync_extracted_frontmatter_to_raw_content.py`
  - Verify `page-types.md` contains no reference to `06-lifecycle/`, `12-risks-contradictions/`

**frontmatter-schema.md change**: In the `## Source Page Required Extensions` block, add `cited_sources:` after `findings:`:

```yaml
findings:
cited_sources:
```

Also add a `## cited_sources Entry Schema` subsection:

```markdown
## `cited_sources` Entry Schema

```yaml
cited_sources:
  - raw_citation: "Author (Year) Title"
    wiki_id: S-slug        # omit if source not yet in wiki
    in_wiki: false         # auto-computed by build-index.py — never set manually
```

Rules:
- Include key contributing sources only (primary frameworks, foundational research, major guidelines)
- `in_wiki` is always auto-computed — hand-set values will be overwritten
```

**build-index.py change**: Add `cited_sources` resolution in the edge-resolution pass (after the main `for page in pages:` loop). In the post-loop section (~line 317, after `id_to_page` is fully built), insert:

```python
# Resolve cited_sources in_wiki after full id_to_page scan
for row in page_rows:
    if row.get("type") == "source":
        # Find the page to read its frontmatter
        page_obj = id_to_page.get(row["id"])
        if page_obj:
            raw_cited = page_obj.frontmatter.get("cited_sources", []) or []
            cited_out = []
            for entry in raw_cited:
                if not isinstance(entry, dict):
                    continue
                wiki_id = entry.get("wiki_id")
                in_wiki = bool(wiki_id and wiki_id in id_to_page)
                cited_out.append({
                    "raw_citation": entry.get("raw_citation"),
                    "wiki_id": wiki_id,
                    "in_wiki": in_wiki,
                })
            row["cited_sources"] = cited_out
```

### WU-2: Template + Agent-08 Rewrite
- **Objective**: Replace the minimal extracted-source-template.md with the full 7-section spec; replace the agent-08 stub with a complete output contract
- **Inputs**:
  - `/Users/eddieargenal/Documents/obsidian-vault/governance/templates/v26/extracted-source-template.md`
  - `/Users/eddieargenal/Documents/obsidian-vault/governance/aba/prompts/agent-08-extracted-source-agent.md`
  - This brief (for body section spec, finding schema, cited_sources schema)
- **Output**: 2 files rewritten
- **Dependencies**: WU-1 (frontmatter-schema.md must be updated first so the template is consistent with it)
- **Complexity tier**: Tier 2
- **Validation method**:
  - Template must have all 7 `sections:` entries in frontmatter with id, anchor, purpose
  - Template must have all 7 `<a id="..."></a>` anchors in body
  - Template must include a `cited_sources:` block with at least one example entry showing all three fields
  - Template `findings:` must include at least one fully-populated example entry showing all 10 fields
  - Agent-08 prompt must state all 10 finding fields, all 7 body sections, `cited_sources` selectivity rule, and Gate A criteria
  - Run `python3 scripts/build-index.py` after filling the template with stub data — must produce 0 critical errors

**Template required sections block**:
```yaml
sections:
  - id: summary
    anchor: "#summary"
    purpose: "Author background, document type, scope, production method, ABA/DRR lifecycle coverage"
  - id: key-concepts
    anchor: "#key-concepts"
    purpose: "Definitions and frameworks introduced or heavily used by the document"
  - id: methods-and-tools
    anchor: "#methods-and-tools"
    purpose: "Methods, tools, instruments, and processes the document describes or applies"
  - id: lifecycle-coverage
    anchor: "#lifecycle-coverage"
    purpose: "Which lifecycle stages the document addresses and how"
  - id: known-tensions
    anchor: "#known-tensions"
    purpose: "Tensions, contradictions, or contested positions surfaced by the document"
  - id: findings
    anchor: "#findings"
    purpose: "Structured reusable findings (mirrors frontmatter findings: list)"
  - id: integration-map
    anchor: "#integration-map"
    purpose: "Routing table: finding → candidate target page → integration action → status"
```

**Agent-08 prompt structure** (replace entire file content with):
- Role and objective
- Inputs (raw-content mirror, human seed brief, extracted-source-template)
- Output contract section (exact frontmatter fields required)
- Finding schema (all 10 fields, with enums)
- `cited_sources` rule (key sources only; never set `in_wiki`)
- Body section contract (all 7 sections with anchor requirement)
- Constraints (do not update synthesis pages, do not route findings, Gate A)
- Gate A criteria (what triggers human review flag: contested findings, data quality issues, missing source pages)
- Acceptance criteria (checklist)

### WU-3: SKILL.md Update + Twigg Backfill
- **Objective**: Add `cited_sources` rule to SKILL.md EXTRACT and INGEST operations; populate `cited_sources:` on the Twigg page
- **Inputs**:
  - `/Users/eddieargenal/Documents/obsidian-vault/governance/aba/librarian/SKILL.md`
  - `~/.claude/skills/librarian/SKILL.md`
  - `/Users/eddieargenal/Documents/obsidian-vault/wiki/aba/01-sources/extracted/2009_twigg-ucl_disaster-resilient-community.md`
  - The Twigg raw-content file for sourcing cited works
- **Output**: 3 files updated (both SKILL.md copies + Twigg page)
- **Dependencies**: WU-1 (schema must be updated before populating Twigg)
- **Complexity tier**: Tier 2
- **Validation method**:
  - Both SKILL.md copies must be byte-identical after update
  - SKILL.md EXTRACT operation must state the `cited_sources` rule
  - SKILL.md INGEST operation must include `cited_sources` in the ingest checklist
  - Twigg page `cited_sources:` must have at least 3 entries (the document heavily cites Twigg 2007, IFRC, HFA)
  - Run `python3 scripts/build-index.py` — Twigg row in `agent-index.jsonl` must have `cited_sources` array with `in_wiki` field populated
  - `in_wiki: false` for all Twigg cited_sources entries (no cited sources are currently in the wiki)

**SKILL.md EXTRACT operation addition** (add to the checklist under extract/ingest steps):
```
- cited_sources: populate with key contributing sources only (primary frameworks, foundational research, major guidelines the document explicitly builds on or applies). Never include every footnote. Never set in_wiki — always auto-computed.
```

**Twigg cited_sources candidates** (key contributing sources to populate — derive from reading raw-content mirror):
- Twigg (2007) first edition of this guidance note
- IFRC World Disasters Report 2004 (community-centred approaches)
- Hyogo Framework for Action 2005–2015 (HFA) — the primary policy framework the document maps to
- UNISDR (various) — Sendai precursors
- Additional primary sources that shaped the 167 characteristics framework

## Risks and Mitigations

| Risk | Likelihood | Mitigation |
|---|---|---|
| Two-pass cited_sources resolved against incomplete id_to_page | Low — id_to_page is fully built before edge-resolution pass | Insert cited_sources resolution after the main page loop, in the same block as edge resolution |
| Template example findings become prescriptive/limiting | Medium | Use realistic but generic placeholder text; note in template that content is illustrative |
| Agent-08 prompt too long, dilutes instruction priority | Medium | Use numbered contract sections with bold field names; put Gate A criteria last |
| SKILL.md copies diverge silently | Low — both must be written in the same operation | Explicitly copy vault version to install path as final step |
| Twigg cited_sources incomplete | Low | Read raw-content mirror for bibliography section before populating |

## Acceptance Criteria

- [ ] `python3 scripts/build-index.py` runs clean — 0 critical errors
- [ ] Twigg row in `indexes/current/agent-index.jsonl` has `cited_sources` array
- [ ] Each `cited_sources` entry has `raw_citation`, `wiki_id` (or null), `in_wiki`
- [ ] `governance/schema/frontmatter-schema.md` contains `cited_sources:` in Source Page Required Extensions
- [ ] `governance/templates/v26/extracted-source-template.md` has 7 sections in frontmatter and 7 anchors in body
- [ ] `governance/aba/prompts/agent-08-extracted-source-agent.md` states all 10 finding fields and all 7 body sections
- [ ] `governance/schema/ingest-rules.md` contains no reference to `06-lifecycle/` or `indexes/agent-index.md`
- [ ] `governance/schema/page-types.md` contains no reference to `06-lifecycle/` or `12-risks-contradictions/`
- [ ] Both SKILL.md copies are identical
- [ ] `memory/current-handoff.md` updated with session close state
- [ ] `memory/runtime/logs/log.md` appended with operation entry

## Execution Command

```
/execute-with-agent-team governance/briefs/brief-cited-sources-spec-2026-05-18.md 3
```
