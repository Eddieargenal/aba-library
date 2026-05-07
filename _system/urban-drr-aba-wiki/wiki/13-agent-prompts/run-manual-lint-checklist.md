---
type: agent-prompt
prompt_id: run-manual-lint-checklist
status: operational
created: 2026-05-07
updated: 2026-05-07
---
# Run Manual Lint Checklist

## When to use
Use this checklist when `scripts/lint_wiki.py` is not implemented or unavailable.

## Output target
Write findings to `outputs/wiki-lint-report.md` and append `log.md`.

## Command checklist (run from wiki root)

1. Orphan pages (no inbound links in `wiki/` + `index.md`)
```bash
python - <<'PY'
from pathlib import Path
import re
root = Path("wiki")
all_pages = [p for p in root.rglob("*.md")]
link_re = re.compile(r"\[\[([^\]]+)\]\]")
inbound = {p.as_posix(): 0 for p in all_pages}
for p in [Path("index.md")] + all_pages:
    txt = p.read_text(encoding="utf-8", errors="ignore")
    for m in link_re.findall(txt):
        target = m.split("|")[0].strip()
        if target.endswith(".md"):
            target = target[:-3]
        if not target.startswith("wiki/"):
            continue
        cand = Path(target + ".md").as_posix()
        if cand in inbound:
            inbound[cand] += 1
orphans = sorted([k for k, v in inbound.items() if v == 0])
print("\n".join(orphans) if orphans else "NONE")
PY
```

2. Tool pages missing field instruments
```bash
rg -n "type:\\s*tool|field_instruments:\\s*\\[\\]" wiki/04-tools
```

3. Draft/stub density
```bash
rg -n "status:\\s*draft|TODO\\[agent\\]" wiki | wc -l
```

4. Empty placeholder sections
```bash
rg -n "^## .*\\nTODO\\[agent\\]" -U wiki
```

5. Tools lacking scoring or thresholds
```bash
rg -n -L "score|scoring|threshold|decision rule" wiki/04-tools/*.md
```

6. Field instruments lacking data quality checks
```bash
rg -n -L "data quality|validation|cross-check|skip pattern" wiki/05-field-instruments/*.md
```

7. Coordination pages lacking duplication/gap logic
```bash
rg -n -L "duplication|gap|who.*where.*for whom|4W|5W" wiki/08-coordination/*.md
```

8. Uncited claims heuristic (sections with no source links)
```bash
rg -n "^#|^##|\\[\\[wiki/01-sources/" wiki | head -n 400
```

## Closeout
1. Summarize findings by severity: critical, high, medium.
2. Add a dated entry to `log.md`:
   - `## [YYYY-MM-DD] lint | Manual lint checklist run`
3. List exact pages requiring population or correction.

