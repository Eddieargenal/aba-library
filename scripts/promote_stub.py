#!/usr/bin/env python3
"""
promote_stub.py — Gate-D promotion helper: turn a PU- proposed-update stub into
a publishable wiki page.

Promotion is a human Gate-D action (governance/human-review-gates.md); this
script only performs the mechanical transform once a human has decided a stub
should be published and at what ladder position. Pure core
(promote / strip_pu_note / target_path) + a thin CLI, dry-run by default.
"""

import argparse
from pathlib import Path
from typing import Dict, Tuple

from schema import (
    IMPLEMENTATION_TIER_VOCAB,
    LADDER_TYPES,
    PAGE_TYPE_DIR,
    PROMOTION_STAGE_VOCAB,
    RETRIEVAL_STATUS_VOCAB,
)
import frontmatter as fmlib

VAULT = Path(__file__).resolve().parents[1]


def strip_pu_note(body: str) -> str:
    """Drop the leading PU draft note (a blockquote plus surrounding blank
    lines) so the published page starts at its first real content. Only the
    LEADING run is removed; blockquotes deeper in the body are untouched."""
    lines = body.splitlines()
    i = 0
    while i < len(lines) and (not lines[i].strip() or lines[i].lstrip().startswith(">")):
        i += 1
    rest = "\n".join(lines[i:]).lstrip("\n")
    return rest + "\n" if (rest and body.endswith("\n")) else rest


def target_path(fm: Dict) -> str:
    """Canonical wiki path for a page: wiki/aba/<type-folder>/<slug>.md."""
    folder = PAGE_TYPE_DIR.get(fm.get("type"))
    if not folder:
        raise ValueError(f"no canonical folder for type {fm.get('type')!r}")
    slug = fm.get("slug")
    if not slug:
        raise ValueError("stub has no slug")
    return f"wiki/aba/{folder}/{slug}.md"


def promote(fm: Dict, body: str, *, status: str, promotion_stage: str,
            implementation_tier: str) -> Tuple[Dict, str]:
    """Transform a PU stub's (fm, body) into a publishable wiki page: set
    retrieval_status and the ladder axes (validated against the controlled
    vocab), and strip the PU note. Raises ValueError on an out-of-vocab value so
    a bad promotion fails fast rather than producing an unbuildable page."""
    if status not in RETRIEVAL_STATUS_VOCAB:
        raise ValueError(f"invalid retrieval_status: {status}")
    if fm.get("type") in LADDER_TYPES:
        if promotion_stage not in PROMOTION_STAGE_VOCAB:
            raise ValueError(f"invalid promotion_stage: {promotion_stage}")
        if implementation_tier not in IMPLEMENTATION_TIER_VOCAB:
            raise ValueError(f"invalid implementation_tier: {implementation_tier}")
    out = dict(fm)
    out["retrieval_status"] = status
    out["promotion_stage"] = promotion_stage
    out["implementation_tier"] = implementation_tier
    return out, strip_pu_note(body)


def main(argv=None) -> int:
    p = argparse.ArgumentParser(
        prog="promote_stub.py",
        description="Promote a PU- proposed-update stub into a wiki page (Gate D). Dry-run by default.",
    )
    p.add_argument("stub", help="path to the PU- stub file")
    p.add_argument("--status", default="limited",
                   help="retrieval_status for the published page (default: limited)")
    p.add_argument("--promotion-stage", required=True, help="ladder stage (ADR-0001)")
    p.add_argument("--implementation-tier", required=True, help="actor tier (ADR-0001)")
    p.add_argument("--apply", action="store_true", help="write the wiki page (else dry-run)")
    p.add_argument("--remove-stub", action="store_true",
                   help="delete the PU stub after a successful --apply")
    args = p.parse_args(argv)

    stub = Path(args.stub)
    fm, body = fmlib.parse(stub.read_text(encoding="utf-8"))
    new_fm, new_body = promote(fm, body, status=args.status,
                               promotion_stage=args.promotion_stage,
                               implementation_tier=args.implementation_tier)
    rel = target_path(new_fm)
    dest = VAULT / rel
    if not args.apply:
        print(f"[dry-run] would write {rel}  "
              f"(status={args.status}, stage={args.promotion_stage}, tier={args.implementation_tier})")
        return 0
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(fmlib.render(new_fm, new_body), encoding="utf-8")
    print(f"wrote {rel}")
    if args.remove_stub:
        stub.unlink()
        print(f"removed {stub}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
