---
type: schema
created: 2026-05-07
updated: 2026-05-07
---
# Lint Rules

Run these checks when auditing the wiki.

1. Orphan pages — pages with no inbound links from index.md or other wiki pages
2. Source pages not linked — source pages not referenced in concept, tool, or lifecycle pages
3. Tool pages missing field instruments — tool pages with no linked field instruments
4. Decision questions without evidence requirements — tool pages that ask "what is X?" without specifying how to collect data to answer it
5. Field instruments not linked to tools — field instrument pages with no related_tool in frontmatter
6. Source claims without traceable references — claims not backed by a wiki/01-sources/ page
7. Contradictions between sources — conflicting guidance from two or more sources (flag in wiki/12-risks-contradictions/known-contradictions.md)
8. Old guidance superseded by newer coordination guidance — outdated recommendations not flagged in stale-guidance-watchlist.md
9. Lifecycle stages missing tools — lifecycle pages with no linked tool pages
10. Coordination pages missing duplication/gap logic — coordination pages that don't address who is doing what, where, and for whom
11. DRR pages mentioning resilience without HEVC logic — DRR guidance not grounded in hazard/exposure/vulnerability/capacity analysis
12. Participation guidance without inclusion and safety safeguards — participation tools that don't address gender, age, disability, protection
13. Handover pages missing responsible actor, budget, maintenance, unresolved risk — transition pages that don't specify who takes over and under what conditions
14. Tool pages without scoring or decision rules — tools that describe analysis but don't specify how to make a decision from the evidence
15. Field instruments without data quality checks — instruments with no guidance on verifying data accuracy
16. Empty placeholder pages — any wiki page with no content beyond frontmatter

## Hard lint rule
A tool page FAILS lint if it asks diagnostic questions but does not define how field teams collect and analyze the evidence needed to answer them.
