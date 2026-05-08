---
type: audit-diagnosis
status: draft
updated: 2026-05-09
---

# Karpathy Vault Audit 2026-05-09

This is the first on-wiki audit artifact following the remediation plan. Summary:

- Frontmatter hygiene: wiki/index.md requires canonical frontmatter; current state shows duplicated blocks.
- Governance: vault-compliance-rules mirrored in memory; on-wiki reference exists but not yet canonical.
- Link health: audit of broken links and orphans pending; lint-plan not yet on-wiki.
- Cross-linking: several pages link to many others; ensure two outbound wikilinks per page where possible.

Actions:
1) Consolidate wiki/index.md frontmatter into a single block with required keys.
2) Create wiki/vault-compliance-rules.md and cross-link from key pages.
3) Publish lint-plan.md on-wiki and link from diagnosis.
4) Update SCHEMA.md to include link-audit guidance and audit-logging.
5) Run a first on-wiki audit pass and record results in a new page.

Status: draft; awaiting approvals to execute remediation tasks.
