---
type: governance
status: active
created: 2026-05-11
updated: 2026-05-11
---

# Review Cadence & Governance Metrics

*Part of the Knowledge Library Governance Framework v2.0. See [[00_index]] for all governance sub-documents.*

---

## Review Cadence

| Frequency | Activities |
|---|---|
| **After every ingest** | LLM updates relevant `00_index.md`; adds backlinks; checks contradiction relevance |
| **Weekly** | Agent Maintainer reviews lint queue; clears critical and high flags |
| **Quarterly** | Governance Council: reviews `01-sources/` for new authoritative docs; clears stale guidance flags; reviews `11-patterns/` promotion queue; checks output validity dates; reviews lint report |
| **Annually** | Full relevance review of all primary sources; revalidate major concepts, frameworks, tools; Steward reviews `AGENTS.md` for behavioral drift; full schema review |
| **Event-triggered** | New donor guidance; new cluster/agency standard; major emergency evaluation; contradiction discovered during use; repeated field finding challenging existing framework; new urban/ABA/DRR guidance |

---

## Governance Metrics (Quarterly Dashboard)

| Metric | Target | Alert Threshold |
|---|---|---|
| `00_index.md` coverage (% files with compliant entries) | 100% | < 95% |
| Frontmatter compliance (% active files with all required fields) | 100% | < 98% |
| Stale content (% files past `next_review` date) | 0% | > 5% |
| Pattern queue age (avg days in `candidate` status) | < 90 days | > 180 days |
| External output provenance completeness | 100% | < 100% |
| Contradiction register response time (discovery → logged) | < 7 days | > 14 days |
| Lint report frequency | Weekly | > 14 days between reports |
| Schema changelog entries | All changes logged | Any unlogged change = critical failure |
| Internal outputs filed back into wiki | Tracked | Not tracked = compounding failure |

---

## Lint Cadence Expectation

- **Target frequency:** Weekly (every 7 days)
- **Filing path:** `wiki/aba/outputs/internal/lint-report-YYYY-MM-DD.md`
- **Trigger:** After any ingest, or on the weekly review schedule
- **Responsible:** Agent Maintainer (per governance/governance-model.md)
- **Last run:** 2026-05-11
