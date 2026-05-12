---
type: governance
status: active
created: 2026-05-11
updated: 2026-05-11
---

# Output Provenance Standard

*Part of the Knowledge Library Governance Framework v2.0. See [[governance/00_governance-index]] for all governance sub-documents.*

---

## Two Output Classes

**External outputs** — toolkits, decision memos, donor proposals, slide decks, training materials that leave the vault:

```yaml
output_id:
title:
output_type: decision_memo | toolkit | proposal_section | slide_deck | training_material
created_date:
created_by:
drafted_by: [LLM agent]
source_files_used: []
concepts_used: []
frameworks_used: []
tools_used: []
risk_checks_used: []
contradictions_checked: true | false
library_version:
schema_version:
review_status: draft | reviewed | approved | superseded
valid_until:
superseded_by:
```

**Internal outputs** — Q&A responses, analyses, explorations that file back into the wiki:[cite:32]

```yaml
output_id:
query:
response_date:
confidence: low | medium | high
source_files_used: []
contradictions_checked: true | false
filed_to: [target folder — e.g. 11-patterns/, 09-monitoring-learning/]
```

Internal outputs use a **lightweight filing path** — no full provenance block required — because their purpose is to compound the library's knowledge, not to produce certified artifacts. Every query should make the library smarter.

## Reverse Dependency Tracking

Every framework carries a `used_by_outputs: []` field. When a framework is updated, the Technical Maintainer identifies all affected outputs via this field and flags them for review. This prevents stale artifacts from circulating undetected.[cite:23]
