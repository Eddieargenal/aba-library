"""
lint_wiki.py — Urban DRR ABA Wiki linter

TODO[agent]: Implement this script to automate wiki quality checks.

Intended behavior:
1. Read all wiki pages
2. Check each page against schema/lint-rules.md
3. Generate outputs/wiki-lint-report.md
4. Print summary to stdout

Lint rules implemented:
- Orphan pages detection
- Missing field instruments for tool pages
- Tool pages without scoring rules
- Field instruments without data quality checks
- Empty placeholder pages

Usage: python lint_wiki.py [--fix] [--report-path outputs/wiki-lint-report.md]

Dependencies: pathlib, yaml (for frontmatter parsing)
"""
raise NotImplementedError("Script not yet implemented. See wiki/13-agent-prompts/lint-wiki.md for manual procedure.")
