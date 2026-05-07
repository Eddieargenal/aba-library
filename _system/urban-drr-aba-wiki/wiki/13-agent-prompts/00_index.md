---
type: section-index
status: active
updated: 2026-05-07
---

# 13 — Agent Prompts

Reusable operational prompts for AI agents performing standard wiki operations. Use by matching the operation you need to the prompt file — each prompt defines when to use it, the exact steps, and what output to produce. 7 prompts are fully operational; 3 are stubs.

## Documents

| Document | Description |
|---|---|
| [[create-decision-memo]] | **What:** A prompt for producing a structured decision memo after completing a tool assessment. **Why:** Standardizes how evidence is documented and decisions are recorded for field teams and coordination partners. **When/How:** Run after any Tool 01 assessment; use the decision-memo-template field instrument; include scoring, conditions, caveats, and next steps. |
| [[detect-duplication-and-gaps]] | **What:** A prompt for identifying activity overlap and uncovered needs before finalizing area strategy. **Why:** Prevents wasted resources and ensures no priority need goes unaddressed in the area. **When/How:** Run before finalizing the integrated area strategy; collect 5W data from field; produce a duplication list, gap list, and recommended coordination actions. |
| [[generate-field-instrument]] | **What:** A prompt for creating a new data collection form, checklist, interview guide, or matrix linked to a tool. **Why:** Ensures every instrument produces evidence for a specific decision domain and includes data quality checks and ethical safeguards. **When/How:** Run when a tool page identifies a data need without an existing instrument; follow the 9-step process including format selection, question design, and ethical review. |
| [[ingest-new-source]] | **What:** A prompt for adding a new document to the wiki from raw PDF through source page creation to wiki updates. **Why:** Maintains the three-layer architecture and ensures all new knowledge is properly attributed and cross-linked. **When/How:** Run whenever a new source document is available; follow the 12-step process from canonical filename assignment through contradiction checking and index update. |
| [[lint-wiki]] | **What:** A prompt for running a quality check on the wiki — orphan pages, missing citations, stubs without field instruments, and evidence gaps. **Why:** Keeps the wiki accurate and prevents degradation as content accumulates. **When/How:** Run periodically or after a major ingestion pass; record findings in outputs/wiki-lint-report.md and append to log.md. |
| [[query-wiki]] | **What:** A prompt for answering a domain question about urban DRR, ABA, field tools, or response design using wiki content. **Why:** Structures how agents navigate the wiki to produce cited, practical answers rather than unsupported assertions. **When/How:** Run on any domain question; start with index.md, then read tool, concept, source, and risk pages in sequence before composing the answer. |
| [[update-crosslinks]] | **What:** A prompt for updating cross-references after adding new pages or completing a major ingestion pass. **Why:** Prevents orphan pages and ensures new knowledge is reachable from all relevant entry points. **When/How:** Run after any new page creation; for each new page identify which concept, tool, lifecycle, and source pages should link to it, then add those links. |
| [[build-new-tool-from-sources]] | **What:** Prompt for constructing a new tool page from ingested source documents, defining decision domains, evidence requirements, field data points, and scoring thresholds. **Why:** Ensures tools are evidence-grounded — each decision domain must trace to an ingested source, not general knowledge. **When/How:** Use when a decision question requires a structured analytical tool; only build from pages already ingested into the wiki. |
| [[review-tool-quality]] | **What:** Audit prompt that checks whether a tool page meets the 10-field quality standard for every decision question. **Why:** Only Tool 01 currently meets the standard; this prompt enables systematic quality improvement of the remaining 16 tools. **When/How:** Use when a tool page is being developed or after ingestion adds source material that should populate a tool. |
| [[run-manual-lint-checklist]] | **What:** Command-based fallback lint procedure using Python scripts when the automated lint script is unavailable. **Why:** Provides a reproducible manual alternative so quality checks can still run in any environment. **When/How:** Use instead of lint-wiki.md when scripts/lint_wiki.py is not implemented; write output to outputs/wiki-lint-report.md. |
