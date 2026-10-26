#!/usr/bin/env python3
"""Export the current build as a FieldWise vault zip: exports/fieldwise-<build_id>.zip (see export_fieldwise.py)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from export_fieldwise import NotClean, StaleBuild, export_from_disk  # noqa: E402

VAULT = Path(__file__).resolve().parents[1]

if __name__ == "__main__":
    try:
        out = export_from_disk(VAULT, VAULT / "exports")
    except (NotClean, StaleBuild) as e:
        print(f"Not exported: {e}", file=sys.stderr)
        sys.exit(1)
    print(f"Wrote {out.relative_to(VAULT)}")
