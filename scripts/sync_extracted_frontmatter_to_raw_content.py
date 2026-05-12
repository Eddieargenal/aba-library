#!/usr/bin/env python3
"""
Sync selected frontmatter fields from wiki/aba/01-sources/extracted/*.md
into matching wiki/aba/01-sources/raw-content/*.raw-extract.md files.

Matching rule:
- Use extracted frontmatter `canonical_file` (../raw/<pdf_name>.pdf)
- Target file in raw-content is <pdf_stem>.raw-extract.md

By default this is a dry run. Use --apply to write changes.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple


DEFAULT_EXTRACTED = Path("wiki/aba/01-sources/extracted")
DEFAULT_RAW_CONTENT = Path("wiki/aba/01-sources/raw-content")

# Agreed fields copied from extracted pages.
COPIED_FIELDS = [
    "status",
    "title",
    "author",
    "institution",
    "year",
    "source_id",
    "source_type",
    "source_url",
    "file_type",
    "canonical_file",
    "created",
    "updated",
    "ingest_date",
    "ingest_status",
    "confidence",
]

# Ordered output schema for raw-content files.
OUTPUT_ORDER = [
    "type",
    "zone",
    "status",
    "title",
    "author",
    "institution",
    "year",
    "source_id",
    "source_type",
    "source_url",
    "file_type",
    "canonical_file",
    "created",
    "updated",
    "ingest_date",
    "ingest_status",
    "confidence",
]


def extract_frontmatter_block(text: str) -> str | None:
    if not text.startswith("---\n"):
        return None
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None
    return parts[1]


def parse_scalar_frontmatter(frontmatter_block: str) -> Dict[str, str]:
    """Parse top-level scalar key: value lines.

    Keeps raw RHS string to preserve quoting/content from extracted files.
    Ignores list/nested bodies.
    """
    out: Dict[str, str] = {}
    for raw_line in frontmatter_block.splitlines():
        line = raw_line.rstrip()
        if not line or line.lstrip().startswith("#"):
            continue
        if line.startswith(" ") or line.startswith("\t"):
            # Skip nested/list continuations.
            continue
        m = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if not m:
            continue
        key, value = m.group(1), m.group(2)
        out[key] = value
    return out


def remove_existing_frontmatter(text: str) -> str:
    if not text.startswith("---\n"):
        return text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return text
    body = parts[2]
    return body.lstrip("\n")


def raw_value_for_yaml(v: str) -> str:
    """Return value as YAML-safe scalar preserving extracted literal when possible."""
    vv = v.strip()
    if vv == "":
        return '""'
    # Preserve already-quoted values.
    if (vv.startswith('"') and vv.endswith('"')) or (vv.startswith("'") and vv.endswith("'")):
        return vv
    # Preserve plain numbers / booleans.
    if re.fullmatch(r"-?\d+", vv):
        return vv
    if vv in {"true", "false", "null", "[]", "{}"}:
        return vv
    # Quote everything else for safety.
    escaped = vv.replace('"', '\\"')
    return f'"{escaped}"'


def build_frontmatter(src: Dict[str, str]) -> Tuple[str, List[str]]:
    missing: List[str] = []
    merged: Dict[str, str] = {
        "type": "source_raw_extract",
        "zone": "raw-content",
    }

    for key in COPIED_FIELDS:
        if key in src:
            merged[key] = src[key]
        else:
            missing.append(key)

    lines = ["---"]
    for key in OUTPUT_ORDER:
        if key in merged:
            lines.append(f"{key}: {raw_value_for_yaml(merged[key])}")
    lines.append("---")
    return "\n".join(lines) + "\n\n", missing


def resolve_target_from_canonical(canonical_file_value: str, raw_content_dir: Path) -> Path | None:
    canonical = canonical_file_value.strip().strip('"').strip("'")
    base = Path(canonical).name
    if not base.lower().endswith(".pdf"):
        return None
    stem = base[:-4]
    return raw_content_dir / f"{stem}.raw-extract.md"

def resolve_target_from_source_id(source_id_value: str, raw_content_dir: Path) -> Path | None:
    source_id = source_id_value.strip().strip('"').strip("'")
    if not source_id:
        return None
    return raw_content_dir / f"{source_id}.raw-extract.md"


def iter_extracted_files(extracted_dir: Path) -> List[Path]:
    out = []
    for p in sorted(extracted_dir.glob("*.md")):
        if p.name.startswith("00_"):
            continue
        out.append(p)
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync extracted frontmatter into raw-content files")
    parser.add_argument("--extracted-dir", type=Path, default=DEFAULT_EXTRACTED)
    parser.add_argument("--raw-content-dir", type=Path, default=DEFAULT_RAW_CONTENT)
    parser.add_argument("--apply", action="store_true", help="Write changes (default is dry-run)")
    args = parser.parse_args()

    extracted_dir = args.extracted_dir
    raw_content_dir = args.raw_content_dir

    if not extracted_dir.exists():
        print(f"ERROR: extracted dir not found: {extracted_dir}")
        return 2
    if not raw_content_dir.exists():
        print(f"ERROR: raw-content dir not found: {raw_content_dir}")
        return 2

    extracted_files = iter_extracted_files(extracted_dir)
    if not extracted_files:
        print("ERROR: no extracted source files found")
        return 2

    total = len(extracted_files)
    matched = 0
    written = 0
    missing_target: List[str] = []
    missing_canonical: List[str] = []
    missing_fields_report: List[Tuple[str, List[str]]] = []
    source_id_fallback_used: List[Tuple[str, str]] = []

    for src_path in extracted_files:
        text = src_path.read_text(encoding="utf-8", errors="ignore")
        fm_block = extract_frontmatter_block(text)
        if fm_block is None:
            missing_canonical.append(f"{src_path.name} (no frontmatter)")
            continue

        src_fm = parse_scalar_frontmatter(fm_block)
        canonical_value = src_fm.get("canonical_file")
        if not canonical_value:
            missing_canonical.append(f"{src_path.name} (missing canonical_file)")
            continue

        target = resolve_target_from_canonical(canonical_value, raw_content_dir)
        if target is None:
            missing_canonical.append(f"{src_path.name} (invalid canonical_file={canonical_value})")
            continue
        if not target.exists():
            # Fallback for known metadata drift: try source_id-based target.
            source_id_value = src_fm.get("source_id")
            fallback_target = (
                resolve_target_from_source_id(source_id_value, raw_content_dir)
                if source_id_value
                else None
            )
            if fallback_target is not None and fallback_target.exists():
                source_id_fallback_used.append((src_path.name, fallback_target.name))
                target = fallback_target
            else:
                missing_target.append(f"{src_path.name} -> {target.name}")
                continue

        matched += 1
        new_frontmatter, missing_fields = build_frontmatter(src_fm)
        if missing_fields:
            missing_fields_report.append((src_path.name, missing_fields))

        target_text = target.read_text(encoding="utf-8", errors="ignore")
        target_body = remove_existing_frontmatter(target_text)
        new_text = new_frontmatter + target_body

        if args.apply and new_text != target_text:
            target.write_text(new_text, encoding="utf-8")
            written += 1

    mode = "APPLY" if args.apply else "DRY-RUN"
    print(f"mode: {mode}")
    print(f"extracted files scanned: {total}")
    print(f"matches found: {matched}")
    print(f"files {'written' if args.apply else 'would write'}: {written if args.apply else matched}")

    if missing_target:
        print("\nmissing raw-content targets:")
        for item in missing_target:
            print(f"  - {item}")

    if missing_canonical:
        print("\ncanonical mapping issues:")
        for item in missing_canonical:
            print(f"  - {item}")

    if missing_fields_report:
        print("\nmissing agreed fields in extracted frontmatter:")
        for src_name, fields in missing_fields_report:
            print(f"  - {src_name}: {', '.join(fields)}")

    if source_id_fallback_used:
        print("\nsource_id fallback matches used:")
        for src_name, target_name in source_id_fallback_used:
            print(f"  - {src_name} -> {target_name}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
