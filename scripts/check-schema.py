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

from schema import ID_PREFIX_BY_TYPE, LIFECYCLE_VOCAB, RETRIEVAL_STATUS_VOCAB  # noqa: E402

VAULT = Path(__file__).resolve().parents[1]
SCAN_DIRS = [VAULT / "governance"]

# key -> ("set"|"map", schema object)
KEYS = {
    "retrieval_status": ("set", RETRIEVAL_STATUS_VOCAB),
    "lifecycle_stage": ("set", LIFECYCLE_VOCAB),
    "id_prefix": ("map", ID_PREFIX_BY_TYPE),
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


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict", action="store_true", help="exit 1 if any drift is found")
    args = ap.parse_args()

    md_files = sorted(p for d in SCAN_DIRS for p in d.rglob("*.md"))
    drift = []
    checked = 0

    for path in md_files:
        text = path.read_text(encoding="utf-8")
        for m in BLOCK_RE.finditer(text):
            key, body = m.group(1), m.group(2)
            if key not in KEYS:
                drift.append((path, key, [f"unknown schema key '{key}'"]))
                continue
            checked += 1
            rel = path.relative_to(VAULT).as_posix()
            kind, schema_obj = KEYS[key]
            doc = parse_block(key, body)
            if kind == "set":
                missing, extra = diff_set(doc, schema_obj)
                msgs = []
                if missing:
                    msgs.append(f"missing from doc: {missing}")
                if extra:
                    msgs.append(f"extra in doc (not in schema): {extra}")
                if msgs:
                    drift.append((rel, key, msgs))
            else:
                missing, extra, mismatched = diff_map(doc, schema_obj)
                msgs = []
                if missing:
                    msgs.append(f"missing from doc: {missing}")
                if extra:
                    msgs.append(f"extra in doc (not in schema): {extra}")
                if mismatched:
                    msgs.append(f"prefix mismatch: {mismatched}")
                if msgs:
                    drift.append((rel, key, msgs))

    if drift:
        print(f"SCHEMA DRIFT — {len(drift)} block(s) disagree with scripts/schema.py:\n")
        for rel, key, msgs in drift:
            print(f"  {rel}  [schema:{key}]")
            for msg in msgs:
                print(f"      - {msg}")
        print(f"\n{checked} block(s) checked, {len(drift)} drifted.")
    else:
        print(f"OK — {checked} schema block(s) match scripts/schema.py across {len(md_files)} docs.")

    return 1 if (drift and args.strict) else 0


if __name__ == "__main__":
    raise SystemExit(main())
