#!/usr/bin/env python3
"""
lint_wiki.py — Urban DRR ABA Wiki linter

Automates a focused lint pass with an incremental parser cache to reduce compute
cost on repeated runs.

Implemented rules:
1. Orphan pages (no inbound wikilinks)
2. Tool pages missing field instruments
3. Tool pages without scoring/decision-rule language
4. Field instruments without data-quality language
5. Empty placeholder pages
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

try:
    import yaml  # type: ignore
except Exception:  # pragma: no cover
    yaml = None  # fallback parser is used


SCRIPT_DIR = Path(__file__).resolve().parent
WIKI_ROOT = SCRIPT_DIR.parent
OUTPUT_DIR = WIKI_ROOT / "outputs"
DEFAULT_REPORT_PATH = OUTPUT_DIR / "wiki-lint-report.md"
CACHE_PATH = OUTPUT_DIR / ".wiki-lint-cache.json"
CACHE_VERSION = 1

EXCLUDED_PARTS = {"raw", "outputs", "scripts", "__pycache__", ".git", ".obsidian"}
LINK_RE = re.compile(r"\[\[([^\]]+)\]\]")
SCORING_RE = re.compile(
    r"\b(score|scoring|scored|threshold|decision rule|decision rules|weighted|pass/fail)\b",
    flags=re.IGNORECASE,
)
DATA_QUALITY_RE = re.compile(
    r"\b(data quality|quality check|verification|validate|validation|triangulat|spot check|consisten|audit trail)\b",
    flags=re.IGNORECASE,
)
TODO_RE = re.compile(r"^\s*TODO\[agent\]", flags=re.IGNORECASE)


@dataclass
class PageInfo:
    rel_path: str
    mtime_ns: int
    size: int
    frontmatter: dict[str, Any]
    links: list[str]
    has_scoring_language: bool
    has_data_quality_language: bool
    is_placeholder: bool

    @property
    def path_obj(self) -> Path:
        return Path(self.rel_path)

    def is_tool_page(self) -> bool:
        page_type = str(self.frontmatter.get("type", "")).strip().lower()
        if page_type:
            return page_type == "tool"
        return "04-tools" in self.path_obj.parts and self.path_obj.name != "00_index.md"

    def is_field_instrument_page(self) -> bool:
        page_type = str(self.frontmatter.get("type", "")).strip().lower()
        if page_type:
            return page_type == "field-instrument"
        return "05-field-instruments" in self.path_obj.parts and self.path_obj.name != "00_index.md"

    def cache_entry(self) -> dict[str, Any]:
        return {
            "mtime_ns": self.mtime_ns,
            "size": self.size,
            "frontmatter": self.frontmatter,
            "links": self.links,
            "has_scoring_language": self.has_scoring_language,
            "has_data_quality_language": self.has_data_quality_language,
            "is_placeholder": self.is_placeholder,
        }

    @classmethod
    def from_cache(cls, rel_path: str, data: dict[str, Any]) -> "PageInfo":
        return cls(
            rel_path=rel_path,
            mtime_ns=int(data["mtime_ns"]),
            size=int(data["size"]),
            frontmatter=dict(data.get("frontmatter") or {}),
            links=list(data.get("links") or []),
            has_scoring_language=bool(data.get("has_scoring_language")),
            has_data_quality_language=bool(data.get("has_data_quality_language")),
            is_placeholder=bool(data.get("is_placeholder")),
        )


def _iter_markdown_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*.md"):
        if any(part in EXCLUDED_PARTS for part in path.parts):
            continue
        files.append(path)
    return sorted(files)


def _strip_link_target(raw_target: str) -> str:
    target = raw_target.split("|", 1)[0]
    target = target.split("#", 1)[0]
    return target.strip()


def _extract_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    if not text.startswith("---\n"):
        return {}, text
    second = text.find("\n---\n", 4)
    if second == -1:
        second = text.find("\n---", 4)
        if second == -1:
            return {}, text
        end = second + 4
    else:
        end = second + 5

    raw_fm = text[4:second]
    body = text[end:].lstrip("\n")
    return _parse_yaml_subset(raw_fm), body


def _parse_yaml_subset(raw: str) -> dict[str, Any]:
    if yaml is not None:
        try:
            parsed = yaml.safe_load(raw)  # type: ignore[attr-defined]
            if isinstance(parsed, dict):
                return parsed
        except Exception:
            pass

    # Fallback parser: handles the subset we use (key: value and key: + list).
    out: dict[str, Any] = {}
    current_key: str | None = None
    for line in raw.splitlines():
        if not line.strip() or line.strip().startswith("#"):
            continue

        list_match = re.match(r"^\s*-\s+(.*)\s*$", line)
        if list_match and current_key:
            if not isinstance(out.get(current_key), list):
                out[current_key] = []
            out[current_key].append(_parse_scalar(list_match.group(1)))
            continue

        key_match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if not key_match:
            continue

        key = key_match.group(1)
        raw_value = key_match.group(2).strip()
        current_key = key

        if raw_value == "":
            out[key] = []
            continue
        out[key] = _parse_scalar(raw_value)
    return out


def _parse_scalar(value: str) -> Any:
    if value.startswith("[") and value.endswith("]"):
        inside = value[1:-1].strip()
        if not inside:
            return []
        return [_parse_scalar(part.strip()) for part in inside.split(",")]
    if (value.startswith("'") and value.endswith("'")) or (
        value.startswith('"') and value.endswith('"')
    ):
        return value[1:-1]
    low = value.lower()
    if low in {"true", "false"}:
        return low == "true"
    if low in {"null", "none"}:
        return None
    return value


def _is_placeholder_body(body: str) -> bool:
    meaningful = 0
    for raw_line in body.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if line.startswith("#"):
            continue
        if TODO_RE.match(line):
            continue
        meaningful += 1
        if meaningful > 0:
            return False
    return True


def _parse_page(path: Path) -> PageInfo:
    text = path.read_text(encoding="utf-8")
    frontmatter, body = _extract_frontmatter(text)
    links = [_strip_link_target(m.group(1)) for m in LINK_RE.finditer(text)]
    body_lower = body.lower()
    stat = path.stat()
    return PageInfo(
        rel_path=path.relative_to(WIKI_ROOT).as_posix(),
        mtime_ns=stat.st_mtime_ns,
        size=stat.st_size,
        frontmatter=frontmatter,
        links=links,
        has_scoring_language=bool(SCORING_RE.search(body_lower)),
        has_data_quality_language=bool(DATA_QUALITY_RE.search(body_lower)),
        is_placeholder=_is_placeholder_body(body),
    )


def _load_cache() -> dict[str, Any]:
    if not CACHE_PATH.exists():
        return {"version": CACHE_VERSION, "files": {}}
    try:
        data = json.loads(CACHE_PATH.read_text(encoding="utf-8"))
        if data.get("version") != CACHE_VERSION:
            return {"version": CACHE_VERSION, "files": {}}
        if "files" not in data or not isinstance(data["files"], dict):
            return {"version": CACHE_VERSION, "files": {}}
        return data
    except Exception:
        return {"version": CACHE_VERSION, "files": {}}


def _save_cache(cache: dict[str, Any]) -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    CACHE_PATH.write_text(json.dumps(cache, indent=2, sort_keys=True), encoding="utf-8")


def _normalize_frontmatter_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(v).strip() for v in value if str(v).strip()]
    if isinstance(value, str):
        value = value.strip()
        return [value] if value else []
    return []


def _resolve_link(
    source_rel: str,
    target: str,
    path_index: dict[str, str],
    stem_index: dict[str, list[str]],
) -> str | None:
    cleaned = target.strip().strip("/")
    if not cleaned:
        return None

    if "/" in cleaned:
        c1 = Path(cleaned).with_suffix(".md").as_posix()
        c2 = (Path(source_rel).parent / cleaned).with_suffix(".md").as_posix()
        for candidate in (c1, c2):
            if candidate in path_index:
                return path_index[candidate]
        return None

    stem = Path(cleaned).name
    candidates = stem_index.get(stem, [])
    if not candidates:
        return None
    if len(candidates) == 1:
        return candidates[0]

    source_parent = Path(source_rel).parent
    same_dir = [c for c in candidates if Path(c).parent == source_parent]
    if same_dir:
        return same_dir[0]
    return candidates[0]


def _build_report(
    report_path: Path,
    pages: list[PageInfo],
    orphan_pages: list[str],
    missing_field_instruments: list[str],
    tools_without_scoring: list[str],
    instruments_without_data_quality: list[str],
    empty_placeholders: list[str],
    cache_hits: int,
    cache_misses: int,
) -> None:
    now_dt = datetime.now().astimezone()
    now = now_dt.strftime("%Y-%m-%d %H:%M:%S %Z")
    total_issues = (
        len(orphan_pages)
        + len(missing_field_instruments)
        + len(tools_without_scoring)
        + len(instruments_without_data_quality)
        + len(empty_placeholders)
    )

    def section(title: str, items: list[str]) -> str:
        if not items:
            return f"## {title}\n- None\n"
        lines = "\n".join(f"- `{item}`" for item in items)
        return f"## {title} ({len(items)})\n{lines}\n"

    text = f"""---
type: lint-report
status: complete
generated: {now_dt.date().isoformat()}
method: automated-script
---

# Wiki Lint Report

Generated: {now}
Wiki root: `{WIKI_ROOT.as_posix()}`
Pages scanned: {len(pages)}
Cache hits: {cache_hits}
Cache misses: {cache_misses}

## Summary

| Issue type | Count |
|---|---:|
| Orphan pages | {len(orphan_pages)} |
| Tool pages missing field instruments | {len(missing_field_instruments)} |
| Tool pages without scoring rules | {len(tools_without_scoring)} |
| Field instruments without data-quality checks | {len(instruments_without_data_quality)} |
| Empty placeholder pages | {len(empty_placeholders)} |
| **Total issues** | **{total_issues}** |

{section("Orphan Pages", orphan_pages)}
{section("Tool Pages Missing Field Instruments", missing_field_instruments)}
{section("Tool Pages Without Scoring Rules", tools_without_scoring)}
{section("Field Instruments Without Data-Quality Checks", instruments_without_data_quality)}
{section("Empty Placeholder Pages", empty_placeholders)}
"""
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(text, encoding="utf-8")


def run(report_path: Path, fix: bool) -> int:
    all_files = _iter_markdown_files(WIKI_ROOT)
    cache = _load_cache()
    cache_files: dict[str, Any] = dict(cache.get("files", {}))
    new_cache_files: dict[str, Any] = {}

    pages: list[PageInfo] = []
    cache_hits = 0
    cache_misses = 0

    for path in all_files:
        rel = path.relative_to(WIKI_ROOT).as_posix()
        stat = path.stat()
        cached = cache_files.get(rel)
        if (
            isinstance(cached, dict)
            and int(cached.get("mtime_ns", -1)) == stat.st_mtime_ns
            and int(cached.get("size", -1)) == stat.st_size
        ):
            page = PageInfo.from_cache(rel, cached)
            cache_hits += 1
        else:
            page = _parse_page(path)
            cache_misses += 1
        pages.append(page)
        new_cache_files[rel] = page.cache_entry()

    cache["files"] = new_cache_files
    _save_cache(cache)

    path_index: dict[str, str] = {p.rel_path: p.rel_path for p in pages}
    stem_index: dict[str, list[str]] = {}
    for p in pages:
        stem_index.setdefault(Path(p.rel_path).stem, []).append(p.rel_path)

    inbound: dict[str, int] = {p.rel_path: 0 for p in pages}
    for p in pages:
        for target in p.links:
            resolved = _resolve_link(p.rel_path, target, path_index, stem_index)
            if resolved is None or resolved == p.rel_path:
                continue
            inbound[resolved] += 1

    orphan_allow_names = {"index.md", "00_index.md", "README.md", "AGENTS.md", "CLAUDE.md"}
    orphan_pages = sorted(
        p.rel_path
        for p in pages
        if inbound[p.rel_path] == 0 and Path(p.rel_path).name not in orphan_allow_names
    )

    missing_field_instruments: list[str] = []
    tools_without_scoring: list[str] = []
    instruments_without_data_quality: list[str] = []
    empty_placeholders: list[str] = sorted(p.rel_path for p in pages if p.is_placeholder)

    for p in pages:
        if p.is_tool_page():
            fm_fi = _normalize_frontmatter_list(p.frontmatter.get("field_instruments"))
            link_fi = [link for link in p.links if "05-field-instruments/" in link]
            if not fm_fi and not link_fi:
                missing_field_instruments.append(p.rel_path)
            if not p.has_scoring_language:
                tools_without_scoring.append(p.rel_path)
        if p.is_field_instrument_page() and not p.has_data_quality_language:
            instruments_without_data_quality.append(p.rel_path)

    missing_field_instruments.sort()
    tools_without_scoring.sort()
    instruments_without_data_quality.sort()

    if fix:
        # Placeholder hook to keep CLI contract stable; add concrete fixers later.
        print("Note: --fix is currently a no-op for these rule checks.", file=sys.stderr)

    _build_report(
        report_path=report_path,
        pages=pages,
        orphan_pages=orphan_pages,
        missing_field_instruments=missing_field_instruments,
        tools_without_scoring=tools_without_scoring,
        instruments_without_data_quality=instruments_without_data_quality,
        empty_placeholders=empty_placeholders,
        cache_hits=cache_hits,
        cache_misses=cache_misses,
    )

    total_issues = (
        len(orphan_pages)
        + len(missing_field_instruments)
        + len(tools_without_scoring)
        + len(instruments_without_data_quality)
        + len(empty_placeholders)
    )

    print(f"Pages scanned: {len(pages)}")
    print(f"Cache hits: {cache_hits} | Cache misses: {cache_misses}")
    print(f"Report: {report_path.as_posix()}")
    print(f"Total issues: {total_issues}")
    print(f"- Orphans: {len(orphan_pages)}")
    print(f"- Missing field instruments: {len(missing_field_instruments)}")
    print(f"- Tools without scoring rules: {len(tools_without_scoring)}")
    print(f"- Field instruments without data quality checks: {len(instruments_without_data_quality)}")
    print(f"- Empty placeholders: {len(empty_placeholders)}")

    return 1 if total_issues > 0 else 0


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Lint Urban DRR ABA wiki pages.")
    parser.add_argument(
        "--fix",
        action="store_true",
        help="Reserved for future auto-remediation. Currently no-op.",
    )
    parser.add_argument(
        "--report-path",
        type=Path,
        default=DEFAULT_REPORT_PATH,
        help=f"Where to write the markdown report (default: {DEFAULT_REPORT_PATH.as_posix()})",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    report_path = args.report_path
    if not report_path.is_absolute():
        report_path = (Path.cwd() / report_path).resolve()
    return run(report_path=report_path, fix=bool(args.fix))


if __name__ == "__main__":
    raise SystemExit(main())
