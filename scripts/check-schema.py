#!/usr/bin/env python3
"""
check-schema.py — verify prose docs against scripts/schema.py (non-blocking)

The data model lives in schema.py. Prose docs (governance/schema/*.md,
governance/id-registry.md) mirror the controlled vocabularies inside fenced
blocks tagged ```schema:<key>```. This script parses those blocks and reports
any drift from schema.py. It NEVER blocks a build: exit 0 by default; pass
--strict to exit 1 when drift is found (for CI).

Recognised keys:
  schema:retrieval_status  — one value per line
  schema:lifecycle_stage   — one value per line
  schema:id_prefix         — "<prefix> <type>" per line  (e.g. "C- concept")
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from schema import (  # noqa: E402
    CROSS_CUTTING_TOPICS_VOCAB,
    ID_PREFIX_BY_TYPE,
    IMPLEMENTATION_TIER_VOCAB,
    LIFECYCLE_VOCAB,
    PROMOTION_STAGE_VOCAB,
    RETRIEVAL_STATUS_VOCAB,
)

VAULT = Path(__file__).resolve().parents[1]
SCAN_DIRS = [VAULT / "governance"]

# key -> ("set"|"map", schema object)
KEYS = {
    "retrieval_status": ("set", RETRIEVAL_STATUS_VOCAB),
    "lifecycle_stage": ("set", LIFECYCLE_VOCAB),
    "id_prefix": ("map", ID_PREFIX_BY_TYPE),
    "promotion_stage": ("set", PROMOTION_STAGE_VOCAB),
    "implementation_tier": ("set", IMPLEMENTATION_TIER_VOCAB),
    "cross_cutting_topics": ("set", CROSS_CUTTING_TOPICS_VOCAB),
}

BLOCK_RE = re.compile(r"^```schema:([a-z_]+)\s*$(.*?)^```\s*$", re.DOTALL | re.MULTILINE)


def parse_block(key: str, body: str):
    lines = [ln.strip() for ln in body.splitlines() if ln.strip()]
    kind, _ = KEYS[key]
    if kind == "set":
        return set(lines)
    mapping = {}
    for ln in lines:
        parts = ln.split()
        if len(parts) >= 2:
            prefix, ptype = parts[0], parts[1]
            mapping[ptype] = prefix
    return mapping


def diff_set(doc: set, schema: set):
    return sorted(schema - doc), sorted(doc - schema)  # missing_from_doc, extra_in_doc


def diff_map(doc: dict, schema: dict):
    missing = sorted(t for t in schema if t not in doc)
    extra = sorted(t for t in doc if t not in schema)
    mismatched = sorted(f"{t}: doc={doc[t]} schema={schema[t]}" for t in schema if t in doc and doc[t] != schema[t])
    return missing, extra, mismatched


def _diff_messages(key: str, body: str):
    """Return drift messages for one recognised schema block (empty list if clean)."""
    kind, schema_obj = KEYS[key]
    doc = parse_block(key, body)
    msgs = []
    if kind == "set":
        missing, extra = diff_set(doc, schema_obj)
    else:
        missing, extra, mismatched = diff_map(doc, schema_obj)
    if missing:
        msgs.append(f"missing from doc: {missing}")
    if extra:
        msgs.append(f"extra in doc (not in schema): {extra}")
    if kind == "map" and mismatched:
        msgs.append(f"prefix mismatch: {mismatched}")
    return msgs


def run(dirs, strict=False):
    """Scan dirs for *.md and diff every ```schema:<key>``` block against schema.py.

    Returns (drift_records, exit_code). drift_records is a list of
    (rel_path, key, messages); clean blocks are not recorded. Pure and
    side-effect-free so it can be tested directly. exit_code is 1 only when
    drift exists AND strict is set; otherwise 0.
    """
    drift = []
    for d in dirs:
        d = Path(d)
        for path in sorted(d.rglob("*.md")):
            text = path.read_text(encoding="utf-8")
            for m in BLOCK_RE.finditer(text):
                key, body = m.group(1), m.group(2)
                try:
                    rel = path.relative_to(VAULT).as_posix()
                except ValueError:
                    rel = path.relative_to(d).as_posix()
                if key not in KEYS:
                    drift.append((rel, key, [f"unknown schema key '{key}'"]))
                    continue
                msgs = _diff_messages(key, body)
                if msgs:
                    drift.append((rel, key, msgs))
    exit_code = 1 if (drift and strict) else 0
    return drift, exit_code


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict", action="store_true", help="exit 1 if any drift is found")
    args = ap.parse_args()

    n_docs = sum(1 for d in SCAN_DIRS for _ in Path(d).rglob("*.md"))
    drift, exit_code = run(SCAN_DIRS, strict=args.strict)

    if drift:
        print(f"SCHEMA DRIFT — {len(drift)} block(s) disagree with scripts/schema.py:\n")
        for rel, key, msgs in drift:
            print(f"  {rel}  [schema:{key}]")
            for msg in msgs:
                print(f"      - {msg}")
        print(f"\n{len(drift)} block(s) drifted across {n_docs} docs.")
    else:
        print(f"OK — no schema drift across {n_docs} docs.")

    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
