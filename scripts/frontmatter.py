"""
frontmatter.py — shared YAML frontmatter parse/serialize (no pip deps)

Single seam for reading and writing markdown frontmatter. Parsing and dumping
both go through Ruby's stdlib YAML (available by default on macOS), so there is
one parser for the whole system instead of build-index.py's full parser and the
sync script's former regex scalar parser.

  parse(text)  -> (frontmatter_dict, body_str)
  parse_yaml(s)-> dict          (frontmatter block only)
  dump(fm)     -> str           (YAML mapping, key order preserved, no --- fences)
  render(fm, body) -> str       (full document: fenced frontmatter + body)
"""

import json
import re
import subprocess
from typing import Dict, Tuple

FM_RE = re.compile(r"^---\n(.*?)\n---\n?", re.DOTALL)


def _ruby(args, stdin: str) -> str:
    proc = subprocess.run(["ruby", *args], input=stdin, capture_output=True, text=True, check=False)
    if proc.returncode != 0:
        raise ValueError(proc.stderr.strip() or "ruby invocation failed")
    return proc.stdout


def parse_yaml(text: str) -> Dict:
    """Parse a frontmatter block into a dict. Returns {} for non-mapping input."""
    out = _ruby(
        [
            "-rdate",
            "-ryaml",
            "-rjson",
            "-e",
            "obj = YAML.safe_load(STDIN.read, permitted_classes: [Date, Time], aliases: true); "
            "puts(JSON.generate(obj || {}))",
        ],
        text,
    )
    parsed = json.loads(out or "{}")
    return parsed if isinstance(parsed, dict) else {}


def split(text: str) -> Tuple[str, str]:
    """Return (frontmatter_text_or_None, body)."""
    m = FM_RE.match(text)
    if not m:
        return None, text
    return m.group(1), text[m.end():]


def parse(text: str) -> Tuple[Dict, str]:
    """Return (frontmatter_dict, body). Empty dict if there is no frontmatter."""
    fm_text, body = split(text)
    if fm_text is None:
        return {}, text
    return parse_yaml(fm_text), body


def dump(fm: Dict) -> str:
    """Serialize a dict to a YAML mapping, preserving key order, without --- fences."""
    out = _ruby(["-ryaml", "-rjson", "-e", "puts YAML.dump(JSON.parse(STDIN.read))"], json.dumps(fm))
    if out.startswith("---\n"):
        out = out[4:]
    return out.rstrip("\n")


def render(fm: Dict, body: str) -> str:
    """Full document: fenced frontmatter followed by body."""
    return f"---\n{dump(fm)}\n---\n\n{body.lstrip(chr(10))}"
