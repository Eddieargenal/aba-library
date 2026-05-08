---
type: memory
title: Vault Compliance Rules (On-Wiki Canonical Reference)
status: validated
updated: 2026-05-08
sources: ['memory/vault-compliance-rules.md']
tags: ['governance','rules','compliance']
---

# Vault Compliance Rules (Canonical on-Wiki Reference)

These 10 rules govern all vault content. No exceptions.

1) Cite Raw Sources
- Every wiki page must cite raw sources. Every factual claim needs a source.

2) Link Decisions to Evidence
- Every claim that affects decisions must link back to evidence.

3) Distinguish Claim Types
- Types: ✅ Fact, 🔹 Inference, 🎯 Decision, 💡 Hypothesis, ❓ Unresolved

4) Contradictions → Unresolved
- Contradictions go inline in `memory/categories/unresolved.md`. Never hide conflicts or create duplicate pages.
- Use type: contradiction with references to both sources.

5) index.md Updated After Ingest
- Update indexes (e.g., `indexes/` or `wiki/index.md`) after ingesting new content.

6) log.md Is Append-Only
- The log at `memory/runtime/logs/log.md` must only append; never overwrite.

7) Don't Overwrite Raw Sources
- Raw sources are immutable. Corrections belong in derived wiki content, not the original sources.

8) Supersede, Don't Delete
- When updating a claim, create a new entry and mark the old one as superseded.

9) Review Status
- Pages require a clear review status: draft, reviewed, validated, stale.

10) Verify Against Sources
- For accuracy-critical outputs, verify claims against sources and cite verification.

Optional but recommended governance signals
- Provenance markers for multi-source syntheses (append source references in the text).
- Append-only change history for major sections.
- Automated frontmatter validation prior to publishing.

---

See also: [[index]] · [[../SCHEMA]] · [[workflows/lint-plan]]

