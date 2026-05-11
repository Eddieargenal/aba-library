---
type: session-prep
status: active
updated: 2026-05-11
---

# Next Session

## Next Session Should

1. Run a fresh lint report (`python3 wiki/aba/scripts/lint_wiki.py` from vault root) to confirm the audit remediation closed all findings
2. Check whether H-3 (field instruments for 14 tool pages) is ready for domain expert input — if yes, gather requirements before writing
3. Check whether M-1 (pattern candidates for `wiki/aba/11-patterns/`) has enough accumulated field evidence to begin drafting

## Quick Context

Two-sprint day on 2026-05-11:
- **Sprint 1:** Governance consolidation — all operational docs moved to `governance/`, 5 root nav files replaced by single AGENTS.md, rule copies deduplicated
- **Sprint 2:** Audit remediation — 10 open findings closed (C-2, C-3, H-1, H-2, H-4, M-2, M-3, M-4, M-5, L-3)

Vault now fully indexed: `governance/00_index.md` routes to all governance; `wiki/aba/03-frameworks/00_index.md` indexes all 41 frameworks (9 Tier 1 + 32 Tier 2).

## If Blocked

- Check `git log --oneline -5` for last commits and state
- Read `governance/briefs/` for scope and brief documents from both sprints
- Read `governance/00_index.md` to orient to governance structure
- Read `wiki/aba/AGENTS.md` for ABA operating rules entry point (stub → `governance/aba/CLAUDE.md`)
