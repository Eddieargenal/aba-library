---
type: schema
created: 2026-05-07
updated: 2026-05-07
---
# Frontmatter Schema

## Source page
type: source
source_id: [canonical-filename-without-ext]
title: [full title]
authors_or_orgs: [list]
year: [YYYY or range]
canonical_file: ../raw/pdf/[canonical-filename].pdf
original_filename: [from source_metadata.csv]
source_url: [URL or "unknown"]
source_matrix_row: [row numbers]
status: not-started | copied | extracted | ingested | reviewed
relevance: [one sentence]
primary_topics: [list]
used_for: [tools/methods that cite this]
confidence: high | medium | low
created: YYYY-MM-DD
updated: YYYY-MM-DD

## Tool page
type: tool
tool_id: tool-NN-short-name
lifecycle_stage: [stage name]
status: draft | tested | validated
primary_users: [list]
source_foundation: [list of source_ids]
field_instruments: [list of instrument_ids]
related_concepts: [list]
related_lifecycle_pages: [list]
created: YYYY-MM-DD
updated: YYYY-MM-DD

## Field instrument page
type: field-instrument
instrument_id: [short-name]
format: form | checklist | guide | matrix | survey | dashboard
can_export_to: [list: markdown, excel, kobo, word]
related_tool: [tool_id]
required_for_decision_domains: [list]
created: YYYY-MM-DD
updated: YYYY-MM-DD

## Concept page
type: concept
status: draft | stable | contested
maturity: emerging | established | contested
source_count: [N]
related_tools: [list]
related_lifecycle_stages: [list]
created: YYYY-MM-DD
updated: YYYY-MM-DD
