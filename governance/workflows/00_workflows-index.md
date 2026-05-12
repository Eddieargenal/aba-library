---
type: section-index
status: active
updated: 2026-05-11
---
# Workflows — Section Index

All vault-level operational workflows. Each file defines a named, repeatable procedure. Load only the workflow relevant to your current task.

| Workflow                    | Trigger                                               | Output                                               | Note                                                  |
| --------------------------- | ----------------------------------------------------- | ---------------------------------------------------- | ----------------------------------------------------- |
| [[ingest.md]]               | New source document to add to knowledge base          | Updated wiki pages, log entry, updated index         | Start here for any new document                       |
| [[query.md]]                | Factual question answerable from the wiki             | Answer with citations, optional filed knowledge page | Check wiki/index.md first                             |
| [[lint.md]]                 | Periodic health check or post-ingest audit            | Repair list, updated stale flags, log entry          | Also contains Link Audit bash commands                |
| [[lint-plan.md]]            | Repeatable structured lint routine                    | Lint report file + log entry                         | Use after ingest batches or monthly                   |
| [[vault-maintenance.md]]    | After significant session or when gaps found          | Log entry, updated context/handoff, gap proposals    | Also contains Log Format reference                    |
| [[vault-initialization.md]] | Session start                                         | Loaded context from memory, active handoff applied   | Run before any other task                             |
| [[model-routing.md]]        | Before any task — select correct model tier           | Correct model mode selected                          | cheap → fix → code → plan                             |
| [[document-extraction.md]]  | PDF, image, spreadsheet, or document to extract       | Structured markdown output                           | Exact reproduction only — no interpretation           |
| [[memory-recall.md]]        | User asks about previous decisions or session history | Answer from memory categories or "not found"         | Never fabricate                                       |
| [[coding-tasks.md]]         | Writing, editing, debugging, or refactoring code      | Modified files, validation summary                   | **Domain workflow — candidate for future relocation** |
| [[odoo-accounting.md]]      | Odoo accounting tasks, reports, chart of accounts     | Verified mappings, import-ready output               | **Domain workflow — candidate for future relocation** |
