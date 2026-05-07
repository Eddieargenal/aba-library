---
name: vault-governance
description: Governance rules for vault content — citation, claim types, review status, append-only logging.
version: 1.0.0
author: Eddie Argenal
tags: [governance, rules]
---

# Vault Governance

## The 10 Rules

### 1. Cite Raw Sources
Every wiki page must cite raw sources.

### 2. Link Decisions to Evidence  
Every claim that affects decisions must link back to evidence.

### 3. Distinguish Claim Types
Use these symbols:
- ✅ Fact: verified externally
- 🔹 Inference: agent-derived
- 🎯 Decision: deliberate choice
- 💡 Hypothesis: unverified assumption
- ❓ Unresolved: open question

### 4. Contradictions → Unresolved
Contradictions go to `memory/categories/unresolved/contradictions/`.

### 5. index.md Updated After Ingest
Update indexes after every content addition.

### 6. log.md Append-Only
Never overwrite. Only append.

### 7. Don't Overwrite Raw Sources
Never edit tool definitions or raw source files.

### 8. Supersede, Don't Delete
Mark old claims as superseded, don't delete them.

### 9. Review Status
Use: draft → reviewed → validated → stale

### 10. Verify Against Sources
Start from wiki, verify against raw sources for accuracy.

## Claim Type Template

```markdown
✅ Fact: [verified fact with source]
🔹 Inference: [agent-derived with evidence chain]
🎯 Decision: [choice with rationale]
💡 Hypothesis: [assumption to verify]
❓ Unresolved: [question to answer]
```

## Supersession Template

```markdown
### Superseded
- date: YYYY-MM-DD
- superseded_by: [link to new claim]
- reason: [why it changed]
```

## Review Status

| Status | Meaning |
|--------|---------|
| draft | In progress, incomplete |
| reviewed | Agent verified |
| validated | User confirmed |
| stale | Needs re-verification |