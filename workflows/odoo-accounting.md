---
type: workflow
scope: odoo-accounting
status: active
updated: 2026-05-06
---

# Workflow: Odoo Accounting

Use this workflow for Odoo tasks, accounting reports, chart of accounts, and financial data work.

## Steps

1. **Identify country and localization context.**
   - Which country is this deployment for?
   - Which localization module is active (e.g., Honduras `l10n_hn`, Spain `l10n_es`)?
   - Note any custom localization overrides.

2. **Identify the chart of accounts.**
   - Which accounts are in scope?
   - Are account codes standardized or customized?
   - Confirm the account structure (asset, liability, equity, income, expense).

3. **Map transaction categories.**
   - What transaction types are being processed (sales, purchases, journal entries, payroll)?
   - Map each category to the correct account or account range.

4. **Verify reports against ledger logic.**
   - Do not trust report output blindly.
   - Cross-check report totals against the underlying journal entries.
   - Identify any report lines that do not match the expected account range.

5. **Identify defective report lines.**
   - Name the specific report and the specific line that appears wrong.
   - State what value the line shows vs. what it should show.
   - Identify which accounts feed that line.

6. **Specify how each report line should calculate from accounts.**
   - Define the account range or account codes that should contribute to each line.
   - Do not guess — verify against the localization module or chart of accounts documentation.

7. **Avoid one-off fixes that only work for one sample.**
   - Any fix must work correctly for all transactions of that type, not just the example provided.
   - Test the fix against at least one additional sample before confirming.

8. **Produce import-ready outputs when requested.**
   - If a CSV or XML import is required, match the Odoo import format exactly.
   - Validate required fields before producing the output.

## Model Tier

- Report analysis and mapping → plan mode → [[../prompts/plan-architecture]]
- Import file generation → code mode → [[../prompts/code-debug]]

## Linked Files

- [[../prompts/plan-architecture]]
- [[../prompts/code-debug]]
- [[../memory/categories/projects]]
- [[../memory/runtime/logs/task-log]]
