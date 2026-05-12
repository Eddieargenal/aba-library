---
type: schema
created: 2026-05-07
updated: 2026-05-12
---

# Frontmatter Schema — Authoritative Reference

This file is the authoritative schema for all wiki page types. Agents creating or editing pages must conform to these schemas exactly. The schema is derived from `aba-wiki-detailed description.md` v2.5.

**CRITICAL fields** — missing these creates silent retrieval blackholes:
- `lifecycle_stage:` — must use slugs from the controlled vocabulary (not human-readable strings)
- `contradicts:` — required on source, tool, concept, and framework pages; use `[]` if checked and clear (empty array is a meaningful assertion; a missing field means nobody checked)
- `known_tensions:` — required on concept pages; use `[]` if none

---

## Source Page

One page per raw document. Created during ingest. Updated on review.

```yaml
type: source
source_id:           # canonical-filename-without-ext — e.g. 2017-sanderson-sitko-urban-area-based-approaches-post-disaster-guide
title:               # full document title
author:              # individual author(s) only — e.g. "David Sanderson; Pamela Sitko"
institution:         # publishing organization — e.g. "World Vision / Stronger Cities Consortium (published by IIED)"
year:                # YYYY
canonical_file:      # ../raw/[canonical-filename].pdf
source_url:          # full URL or "unknown"
source_url_status:   # verified | verify | broken
file_type:           # pdf | markdown | xlsx
source_type:         # iasc-guidance | ifrc-framework | un-policy | academic | field-evaluation | ngo-guidance | government-policy
foundational:        # true | false — cited by ≥3 frameworks or foundational to the ABA evidence base
status:              # not-started | extracted | ingested | reviewed
ingest_date:         # YYYY-MM-DD
ingest_status:       # success | partial | failed
confidence:          # high | medium | low — quality of extraction
review_cycle:        # annual | biennial | as-needed
last_reviewed:       # YYYY-MM-DD
next_review:         # YYYY-MM-DD
lifecycle_stage:     # list — slugs from controlled vocabulary (CRITICAL)
primary_topics:      # list — controlled topic terms for agent queries
tags:                # list — free-form Obsidian tags for graph navigation
contradicts:         # [] or list of wiki page slugs — REQUIRED (CRITICAL)
wiki_pages:          # list of wiki pages updated during ingest
notes:               # one-paragraph summary of relevance and key claims
created:             # YYYY-MM-DD
updated:             # YYYY-MM-DD
```

---

## Raw-content Source Mirror Page

Operational mirror in `wiki/aba/01-sources/raw-content/`. Not part of the synthesis answer layer.

```yaml
type: source_raw_extract
zone: raw-content
status:              # copied from matching extracted source page
title:               # copied from extracted source page
author:              # copied from extracted source page
institution:         # copied from extracted source page
year:                # copied from extracted source page
source_id:           # copied from extracted source page
source_type:         # copied from extracted source page
source_url:          # copied from extracted source page
file_type:           # copied from extracted source page
canonical_file:      # copied from extracted source page
created:             # copied from extracted source page
updated:             # copied from extracted source page
ingest_date:         # copied from extracted source page
ingest_status:       # copied from extracted source page
confidence:          # copied from extracted source page
```

Population rule: use `scripts/sync_extracted_frontmatter_to_raw_content.py` (dry-run by default, `--apply` to write).

---

## Tool Page

One page per operational tool. Tier 1 only. Must have linked field instruments before status reaches `validated`.

```yaml
type: tool
tool_id:                  # tool-NN-short-name — e.g. tool-02-area-selection-matrix
title:                    # full tool name
tier:                     # 1
status:                   # draft | tested | validated
lifecycle_stage:          # list — slugs from controlled vocabulary (CRITICAL)
primary_users:            # list — e.g. [programme-officer, field-coordinator, cluster-lead]
source_foundation:        # list of source_ids — min 2 independent sources for Tier 1
field_instruments:        # list of instrument_ids — REQUIRED before validated status; use [] if none yet
related_concepts:         # list of concept slugs
related_frameworks:       # list of framework slugs
related_lifecycle_pages:  # list of lifecycle page slugs
used_by_outputs:          # [] or list of output slugs
contradicts:              # [] or list of slugs where this tool's logic conflicts (CRITICAL)
created:                  # YYYY-MM-DD
updated:                  # YYYY-MM-DD
```

---

## Field Instrument Page

One page per data collection instrument. An instrument may feed multiple tools.

```yaml
type: field-instrument
instrument_id:                 # short-name slug — e.g. household-mini-survey
title:                         # full instrument name
format:                        # form | checklist | guide | matrix | survey | dashboard
can_export_to:                 # list — markdown | excel | kobo | word | pdf
related_tools:                 # list of tool_ids that use this instrument
required_for_decision_domains: # list — decision domains this instrument feeds
lifecycle_stage:               # list — slugs from controlled vocabulary (CRITICAL)
primary_users:                 # list — e.g. [field-enumerator, programme-officer]
data_quality_checks:           # true | false — whether DQ checks are explicitly defined in page body
status:                        # draft | tested | validated
created:                       # YYYY-MM-DD
updated:                       # YYYY-MM-DD
```

---

## Concept Page

One page per operational concept. Promoted from findings once ≥2 independent sources confirm.

```yaml
type: concept
title:                    # concept name
status:                   # draft | active | archived — editorial state
maturity:                 # emerging | established | contested — epistemic state
source_count:             # N — number of independent sources supporting this concept
related_tools:            # list of tool_ids that operationalize this concept
related_frameworks:       # list of framework slugs
related_concepts:         # list of related concept slugs
related_lifecycle_stages: # list — slugs from controlled vocabulary
known_tensions:           # [] or list of tension slugs — expanded in ## Known Tensions body section (CRITICAL)
contradicts:              # [] or list of slugs in direct logical conflict (CRITICAL)
used_by_outputs:          # [] or list of output slugs
created:                  # YYYY-MM-DD
updated:                  # YYYY-MM-DD
```

Note: `known_tensions:` in frontmatter holds slugs for query purposes. Actual tension descriptions live in a `## Known Tensions` section in the page body. Both are required when tensions exist.

---

## Framework Page

```yaml
type: framework
framework_id:             # slug — e.g. 2017-area-selection-framework
title:                    # full framework name
tier:                     # 1 | 2
status:                   # draft | active | superseded | reference
lifecycle_stage:          # list — slugs from controlled vocabulary (CRITICAL)
source_foundation:        # list of source_ids
related_tools:            # list of tool_ids
related_concepts:         # list of concept slugs
related_frameworks:       # list of framework slugs
used_by_outputs:          # [] or list of output slugs
superseded_by:            # framework slug or null
contradicts:              # [] or list of slugs (CRITICAL)
created:                  # YYYY-MM-DD
updated:                  # YYYY-MM-DD
```

Tier 1 frameworks use `status: active`. Tier 2 frameworks use `status: reference`. A superseded framework retains its page — the evidence chain must remain traceable.

---

## Synthesis / Output Page

```yaml
type: synthesis
output_id:              # short slug
title:                  # full title
output_class:           # internal | external
format:                 # analysis | comparison | decision-memo | proposal-section | slide-deck | training-material
source_foundation:      # list of source_ids drawn on
frameworks_used:        # list of framework slugs
tools_used:             # list of tool_ids
concepts_used:          # list of concept slugs
lifecycle_stage:        # list — slugs from controlled vocabulary
status:                 # draft | final
created:                # YYYY-MM-DD
updated:                # YYYY-MM-DD
```

---

## Controlled Vocabulary

### `lifecycle_stage` slugs

Use these exact slugs in all frontmatter `lifecycle_stage:` and `related_lifecycle_stages:` fields. Never use human-readable strings like "1. Area selection and boundary definition" — they are invisible to frontmatter queries.

| Slug | Stage |
|---|---|
| `appropriateness-decision` | Stage 0: Appropriateness decision |
| `area-selection` | Stage 1: Area selection and boundary definition |
| `neighbourhood-diagnosis` | Stage 2: Area profile and systems diagnosis |
| `joint-prioritization` | Stage 3: Joint prioritization |
| `coordination-design` | Stage 4: Area coordination design |
| `integrated-area-strategy` | Stage 5: Integrated area strategy |
| `implementation-adaptation` | Stage 6: Implementation and adaptation |
| `monitoring-learning` | Stage 7: Monitoring and learning |
| `transition-handover` | Stage 8: Transition and handover |

### `source_type`
`iasc-guidance` · `ifrc-framework` · `un-policy` · `academic` · `field-evaluation` · `ngo-guidance` · `government-policy`

### `format` (field instruments)
`form` · `checklist` · `guide` · `matrix` · `survey` · `dashboard`

### `can_export_to`
`markdown` · `excel` · `kobo` · `word` · `pdf`

### `maturity` (concepts)
`emerging` · `established` · `contested`

### `confidence` (sources)
`high` · `medium` · `low`

### `status` (editorial — varies by page type)
- Sources: `not-started` · `extracted` · `ingested` · `reviewed`
- Tools / Field instruments: `draft` · `tested` · `validated`
- Concepts: `draft` · `active` · `archived`
- Frameworks: `draft` · `active` · `superseded` · `reference`
- Synthesis: `draft` · `final`

### `source_url_status`
`verified` · `verify` · `broken`

---

## Lint Checks (CRITICAL)

The following missing fields are treated as CRITICAL failures — they create silent retrieval blackholes:

- Missing `lifecycle_stage:` on any source, tool, concept, framework, or field instrument page
- Missing or absent `contradicts:` on any source, tool, concept, or framework page
- Missing `known_tensions:` on any concept page
- `field_instruments: []` on any tool with `status: validated`
- `data_quality_checks: false` on any field instrument with `status: validated`
- `source_count < 2` on any concept with `maturity: established`
