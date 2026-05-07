---
type: schema
created: 2026-05-07
updated: 2026-05-07
---
# Wiki Page Types

## source
Pages in wiki/01-sources/. One per canonical document. Frontmatter: type, source_id, title, authors_or_orgs, year, canonical_file, original_filename, source_url, source_matrix_row, status, relevance, primary_topics, used_for, confidence, created, updated.

## concept
Pages in wiki/02-concepts/. One per key concept. Frontmatter: type, status, maturity, source_count, related_tools, related_lifecycle_stages, created, updated.

## framework
Pages in wiki/03-frameworks/. Decision frameworks. Same frontmatter as concept plus decision_domains.

## tool
Pages in wiki/04-tools/. Operational tools with evidence collection. Frontmatter: type, tool_id, lifecycle_stage, status, primary_users, source_foundation, field_instruments, related_concepts, related_lifecycle_pages, created, updated.

## field-instrument
Pages in wiki/05-field-instruments/. Data collection instruments. Frontmatter: type, instrument_id, format, can_export_to, related_tool, required_for_decision_domains, created, updated.

## lifecycle
Pages in wiki/06-lifecycle/. One per lifecycle stage. Describes decisions, evidence, tools, outputs for that stage.

## sector-application
Pages in wiki/07-sector-applications/. One per sector. Links sector design to ABA, urban systems, DRR.

## coordination
Pages in wiki/08-coordination/. Covers actor mapping, duplication, referrals, municipal alignment.

## mel
Pages in wiki/09-monitoring-learning/. MEL frameworks, indicators, reassessment.

## transition
Pages in wiki/10-transition-scale/. Handover, scaling, municipal integration.

## risk-contradiction
Pages in wiki/12-risks-contradictions/. Known tensions, weak evidence, unresolved questions.

## agent-prompt
Pages in wiki/13-agent-prompts/. Reusable prompts for specific wiki operations.
