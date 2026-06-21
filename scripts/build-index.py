#!/usr/bin/env python3
"""
build-index.py — v2.7 index compiler (CLI shell)

Owns the filesystem and the clock: scans markdown/frontmatter into Pages,
delegates the whole compile to compile_index() (the deterministic, testable
core in compile_index.py — see test_compile.py), then writes the JSONL/JSON
artifacts and publishes atomically to indexes/current when critical lint
errors are zero.

v2.7 enforcement lives behind compile_index + the lint_rules registry:
  - source_basis required on `retrieval_status: usable` technical pages (critical)
  - retrieval_status validated against controlled vocabulary (critical)
  - lifecycle_stage validated against controlled vocabulary (warning)
  - id prefix must match page type (warning)
  - related_risks required on usable tool pages (warning)
  - excessive primary_topics breadth (warning)
  - deprecated page still linked by an active playbook/protocol (warning)
  - routing-report.json: open findings + unrouted candidate target pages
"""

import argparse
import json
import os
import shutil
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, List

VAULT = Path(__file__).resolve().parents[1]
WIKI_ROOT = VAULT / "wiki" / "aba"
INDEXES_DIR = VAULT / "indexes"
BUILDS_DIR = INDEXES_DIR / "builds"
CURRENT_DIR = INDEXES_DIR / "current"

# Data model is the single source of truth in schema.py; the compile is the deep
# module in compile_index.py (a pure, in-memory test surface). This script is the
# filesystem/clock shell around it.
from compile_index import compile_index  # noqa: E402  (sibling module on sys.path)
from pages import read_pages  # noqa: E402  (filesystem -> Page seam)
from schema import SCHEMA_VERSION  # noqa: E402  (data-model generation stamp)

ARTIFACTS = [
    "manifest.json",
    "agent-index.jsonl",
    "graph-edges.jsonl",
    "unresolved-edges.jsonl",
    "section-index.jsonl",
    "source-evidence-index.jsonl",
    "lint-report.json",
    "routing-report.json",
    "graph-degree.jsonl",
    "term-index.json",
]


def now_build_id() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H%M%SZ")


def write_json(path: Path, data: Any) -> None:
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def write_jsonl(path: Path, rows: List[dict]) -> None:
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--strict", action="store_true", help="Fail build publication when warnings exist")
    args = parser.parse_args()

    build_id = now_build_id()
    build_dir = BUILDS_DIR / build_id
    build_dir.mkdir(parents=True, exist_ok=True)

    pages = read_pages(WIKI_ROOT)
    result = compile_index(
        pages,
        target_exists=lambda p: (VAULT / p).exists(),
        today=datetime.now(timezone.utc).date(),
    )

    manifest = {
        "build_id": build_id,
        "schema_version": SCHEMA_VERSION,
        "build_status": result.status,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "page_count": len(result.page_rows),
        "edge_count": len(result.valid_edges),
        "unresolved_edge_count": len(result.unresolved_edges),
        "pending_finding_count": len(result.routing_pending),
        "critical_error_count": len(result.critical),
        "warning_count": len(result.warnings),
        "active": False,
    }

    lint_report = {
        "build_id": build_id,
        "critical_errors": result.critical,
        "warnings": result.warnings,
    }

    routing_report = {
        "build_id": build_id,
        "pending_finding_count": len(result.routing_pending),
        "unrouted_finding_count": sum(1 for r in result.routing_pending if r["unsatisfied_target_pages"]),
        "pending_findings": result.routing_pending,
    }

    write_json(build_dir / "manifest.json", manifest)
    write_jsonl(build_dir / "agent-index.jsonl", result.page_rows)
    write_jsonl(build_dir / "graph-edges.jsonl", result.valid_edges)
    write_jsonl(build_dir / "unresolved-edges.jsonl", result.unresolved_edges)
    write_jsonl(build_dir / "section-index.jsonl", result.section_rows)
    write_jsonl(build_dir / "source-evidence-index.jsonl", result.evidence_rows)
    write_json(build_dir / "lint-report.json", lint_report)
    write_json(build_dir / "routing-report.json", routing_report)
    write_jsonl(
        build_dir / "graph-degree.jsonl",
        [{"id": pid, "inbound_degree": deg} for pid, deg in sorted(result.inbound_degree.items())],
    )
    write_json(build_dir / "term-index.json", result.term_index)

    publish_allowed = len(result.critical) == 0 and (not args.strict or len(result.warnings) == 0)
    if publish_allowed:
        temp_current = INDEXES_DIR / f".current-{build_id}"
        temp_current.mkdir(parents=True, exist_ok=True)
        for name in ARTIFACTS:
            shutil.copy2(build_dir / name, temp_current / name)

        if CURRENT_DIR.exists():
            shutil.rmtree(CURRENT_DIR)
        os.replace(temp_current, CURRENT_DIR)

        manifest["active"] = True
        write_json(build_dir / "manifest.json", manifest)
        write_json(CURRENT_DIR / "manifest.json", manifest)

    print(json.dumps({
        "build_id": build_id,
        "status": result.status,
        "published": publish_allowed,
        "critical_error_count": len(result.critical),
        "warning_count": len(result.warnings),
        "pending_finding_count": len(result.routing_pending),
    }))
    return 0 if publish_allowed else 2


if __name__ == "__main__":
    raise SystemExit(main())
