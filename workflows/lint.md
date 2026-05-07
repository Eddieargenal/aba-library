---
type: workflow
status: validated
updated: 2026-05-07
---

# Lint Workflow

Health-check the wiki for stale pages, orphan pages, missing sources, and contradictions.

## When to Use

- Periodically (monthly or after large batches of ingests)
- When the wiki feels inconsistent or navigation is breaking down
- Before a major project starts, to ensure the knowledge base is sound

---

## Steps

### 1. Check for stale pages

Open each wiki page and compare its `updated:` date against the stale thresholds from `SCHEMA.md`:

| Category | Stale after |
|----------|-------------|
| infrastructure | 14 days |
| decisions | 90 days |
| procedures | 30 days |
| outcomes | 180 days |
| unresolved | 30 days |

For each page past its threshold:
- Set `status: stale` in frontmatter
- Add `⚠️ stale` to its entry in `wiki/index.md`

### 2. Check for missing source citations

Scan all `memory/categories/` pages for factual claims (✅ Fact entries) without a `[source: ...]` tag.

For each missing citation:
- If the source is known, add the citation
- If the source is unknown, change the claim type from ✅ to 💡 and log to unresolved

### 3. Check for orphan pages

An orphan page is any wiki page not listed in `wiki/index.md`.

Scan all files in `memory/categories/`, `workflows/`, `tools/`, `agents/`, `prompts/`. Cross-reference against `wiki/index.md`.

For each orphan:
- Add it to `wiki/index.md` with a placeholder summary, or
- If the page is empty or superseded, mark it for deletion and log to unresolved

### 4. Check for contradictions

Scan `memory/categories/` for claims that conflict with each other.

Common patterns:
- Two `✅ Fact` entries with the same subject but different values
- A decision that contradicts a later decision without a supersession record
- Infrastructure facts that conflict with each other (e.g., different IPs for the same host)

For each contradiction found:
- Log to `memory/categories/unresolved.md` with `type: contradiction`
- Add references to both conflicting claims

### 5. Produce a repair list

Summarize findings:

```markdown
## Lint Results [YYYY-MM-DD]

### Stale pages ([count])
- [[page]] — last updated YYYY-MM-DD, threshold N days

### Missing citations ([count])
- [[page]] — claim: "[text]"

### Orphan pages ([count])
- [[page]]

### Contradictions ([count])
- [[page-A]] vs [[page-B]] — subject: "[what conflicts]"
```

### 6. Append to log

```markdown
## [YYYY-MM-DD] lint | full vault
- Stale: [count]
- Missing citations: [count]
- Orphans: [count]
- Contradictions: [count]
- Logged to unresolved: [yes/no]
```

---

## Notes

- Lint is a scan-and-report operation. Fix issues in a separate pass (or immediately if trivial).
- Do not delete pages during lint — mark them for deletion in unresolved and let the user confirm.
- After resolving issues from a lint run, re-run lint to confirm the repair list is clear.

## Related

- [[../SCHEMA.md]] — Stale thresholds and review status definitions
- [[../wiki/index.md]] — Master catalog to update during lint
- [[../memory/categories/unresolved]] — Where contradictions and gaps are logged
- [[../memory/runtime/logs/log]] — Append lint summary here
