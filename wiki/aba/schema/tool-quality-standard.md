---
type: schema
created: 2026-05-07
updated: 2026-05-07
---
# Tool Quality Standard

## Minimum requirements for a tool page to pass quality review

Every decision question in a tool page must specify ALL of the following:

1. **Evidence required** — what information is needed to answer the question
2. **Field data points** — specific observable or measurable facts that constitute evidence
3. **Collection method** — how the data is gathered (observation, KII, survey, secondary data, etc.)
4. **Respondent or data source** — who provides the data or which data source is used
5. **Field instrument** — which form, guide, matrix, or checklist is used to collect it
6. **Analysis method** — how raw data is processed to produce an answer
7. **Scoring or decision threshold** — the rule that converts analysis into a decision
8. **Data quality checks** — how to verify data accuracy and completeness
9. **Risks and safeguards** — what could go wrong in data collection and how to mitigate it
10. **Source foundation** — which source documents support this approach

## Failure conditions

A tool page FAILS quality review if:
- It only asks questions without specifying how to collect data to answer them
- It describes analysis without providing decision rules
- It has no linked field instruments
- It has no source foundation
- Any required field above is missing for a decision question

## Stub exception

A stub page (status: draft, contains TODO markers) is acceptable if:
- Purpose is stated
- Source foundation is listed (even as TODO)
- TODO markers clearly identify what is missing
- At minimum one source page is linked

Stubs are NOT acceptable as final deliverables. They require ingestion passes.
