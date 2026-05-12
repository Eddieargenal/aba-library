#!/usr/bin/env python3
"""
build-index.py — generates indexes/agent-index.md from vault frontmatter.
Run after every ingest. Standard library only.
"""

import os
import re
import sys
import yaml
from datetime import date

VAULT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DIRS = {
    "source":           "wiki/aba/01-sources/extracted",
    "concept":          "wiki/aba/02-concepts",
    "framework":        "wiki/aba/03-frameworks",
    "tool":             "wiki/aba/04-tools",
    "field-instrument": "wiki/aba/05-field-instruments",
}

EXCLUDE = None  # files whose names start with "00_" are excluded (see collect())
OUTPUT = os.path.join(VAULT, "indexes", "agent-index.md")


def parse_frontmatter(path):
    try:
        content = open(path, encoding="utf-8").read()
        m = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
        if not m:
            return None
        return yaml.safe_load(m.group(1)) or {}
    except Exception as e:
        print(f"WARNING: skipping {path}: {e}", file=sys.stderr)
        return None


def fmt_list(val, sep=" · "):
    if not val:
        return "—"
    if isinstance(val, list):
        items = [str(v) for v in val if v]
        return sep.join(items) if items else "—"
    return str(val)


def fmt_count(val):
    if not val:
        return "none"
    if isinstance(val, list):
        return str(len(val)) if val else "none"
    return str(val)


def rel(path):
    return os.path.relpath(path, VAULT)


def collect(ptype):
    dirpath = os.path.join(VAULT, DIRS[ptype])
    if not os.path.isdir(dirpath):
        print(f"WARNING: directory not found: {dirpath}", file=sys.stderr)
        return []
    pages = []
    for fname in sorted(os.listdir(dirpath)):
        if not fname.endswith(".md") or fname.startswith("00_"):
            continue
        fpath = os.path.join(dirpath, fname)
        fm = parse_frontmatter(fpath)
        if fm is None:
            continue
        pages.append((rel(fpath), fm))
    return pages


def build_sources(pages):
    rows = []
    rows.append("| path | title | status | lifecycle_stage | confidence |")
    rows.append("|---|---|---|---|---|")
    for path, fm in pages:
        rows.append(
            f"| {path} | {fm.get('title', '—')} | {fm.get('status', '—')} "
            f"| {fmt_list(fm.get('lifecycle_stage'))} | {fm.get('confidence', '—')} |"
        )
    return rows


def build_concepts(pages):
    rows = []
    rows.append("| path | title | status | maturity | source_count |")
    rows.append("|---|---|---|---|---|")
    for path, fm in pages:
        rows.append(
            f"| {path} | {fm.get('title', '—')} | {fm.get('status', '—')} "
            f"| {fm.get('maturity', '—')} | {fm.get('source_count', '—')} |"
        )
    return rows


def build_frameworks(pages):
    tier1 = [(p, fm) for p, fm in pages if str(fm.get('tier', '2')) == '1']
    tier2 = [(p, fm) for p, fm in pages if str(fm.get('tier', '2')) != '1']

    def rows(items):
        out = []
        out.append("| path | title | status | lifecycle_stage |")
        out.append("|---|---|---|---|")
        for path, fm in items:
            out.append(
                f"| {path} | {fm.get('title', '—')} | {fm.get('status', '—')} "
                f"| {fmt_list(fm.get('lifecycle_stage'))} |"
            )
        return out

    return tier1, tier2, rows


def build_tools(pages):
    rows = []
    rows.append("| path | title | status | lifecycle_stage | field_instruments |")
    rows.append("|---|---|---|---|---|")
    for path, fm in pages:
        rows.append(
            f"| {path} | {fm.get('title', '—')} | {fm.get('status', '—')} "
            f"| {fmt_list(fm.get('lifecycle_stage'))} | {fmt_count(fm.get('field_instruments'))} |"
        )
    return rows


def build_instruments(pages):
    rows = []
    rows.append("| path | title | format | lifecycle_stage | related_tools |")
    rows.append("|---|---|---|---|---|")
    for path, fm in pages:
        rows.append(
            f"| {path} | {fm.get('title', '—')} | {fm.get('format', '—')} "
            f"| {fmt_list(fm.get('lifecycle_stage'))} | {fmt_list(fm.get('related_tools'))} |"
        )
    return rows


def main():
    sources     = collect("source")
    concepts    = collect("concept")
    frameworks  = collect("framework")
    tools       = collect("tool")
    instruments = collect("field-instrument")

    total = len(sources) + len(concepts) + len(frameworks) + len(tools) + len(instruments)

    tier1, tier2, fw_rows = build_frameworks(frameworks)

    lines = []
    lines.append("# Agent Index")
    lines.append(f"Generated: {date.today().isoformat()} | Total pages: {total}")
    lines.append("")

    lines.append(f"## Sources ({len(sources)})")
    lines.extend(build_sources(sources))
    lines.append("")

    lines.append(f"## Concepts ({len(concepts)})")
    lines.extend(build_concepts(concepts))
    lines.append("")

    lines.append(f"## Frameworks — Tier 1 ({len(tier1)})")
    lines.extend(fw_rows(tier1))
    lines.append("")

    lines.append(f"## Frameworks — Tier 2 ({len(tier2)})")
    lines.extend(fw_rows(tier2))
    lines.append("")

    lines.append(f"## Tools ({len(tools)})")
    lines.extend(build_tools(tools))
    lines.append("")

    lines.append(f"## Field Instruments ({len(instruments)})")
    lines.extend(build_instruments(instruments))
    lines.append("")

    with open(OUTPUT, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"Indexed {total} pages across 5 types. Output: indexes/agent-index.md")


if __name__ == "__main__":
    main()
