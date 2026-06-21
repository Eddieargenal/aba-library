#!/usr/bin/env python3
"""
test_check_schema.py — tests for check-schema.py's prose-vs-schema drift checker.

The checker's filename is hyphenated (it's a CLI entry point referenced as
`python3 scripts/check-schema.py`), so it isn't importable by name. We load it
by path. The test surface is run(dirs, strict=False) -> (drift_records, exit_code):
write temp .md files holding ```schema:<key>``` blocks and assert the drift the
checker reports against scripts/schema.py. Run:  python3 scripts/test_check_schema.py
"""

import importlib.util
import tempfile
import unittest
from pathlib import Path

import schema

_SPEC = importlib.util.spec_from_file_location(
    "check_schema", Path(__file__).resolve().with_name("check-schema.py")
)
check_schema = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(check_schema)
run = check_schema.run


def block(key, values):
    body = "\n".join(values)
    return f"```schema:{key}\n{body}\n```\n"


class Run(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)

    def tearDown(self):
        self._tmp.cleanup()

    def write(self, rel, text):
        p = self.root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")
        return p

    def test_promotion_stage_matching_vocab_has_no_drift(self):
        self.write("g/p.md", block("promotion_stage", sorted(schema.PROMOTION_STAGE_VOCAB)))
        drift, code = run([self.root])
        self.assertEqual(drift, [])
        self.assertEqual(code, 0)

    def test_promotion_stage_missing_value_is_drift(self):
        values = sorted(schema.PROMOTION_STAGE_VOCAB - {"validated"})
        self.write("g/p.md", block("promotion_stage", values))
        drift, _ = run([self.root])
        self.assertEqual(len(drift), 1)
        _, key, msgs = drift[0]
        self.assertEqual(key, "promotion_stage")
        self.assertTrue(any("missing from doc" in m and "validated" in m for m in msgs))

    def test_promotion_stage_extra_value_is_drift(self):
        values = sorted(schema.PROMOTION_STAGE_VOCAB) + ["bogus-stage"]
        self.write("g/p.md", block("promotion_stage", values))
        drift, _ = run([self.root])
        self.assertEqual(len(drift), 1)
        _, key, msgs = drift[0]
        self.assertEqual(key, "promotion_stage")
        self.assertTrue(any("extra in doc" in m and "bogus-stage" in m for m in msgs))

    def test_implementation_tier_matching_vocab_has_no_drift(self):
        self.write("g/t.md", block("implementation_tier", sorted(schema.IMPLEMENTATION_TIER_VOCAB)))
        drift, _ = run([self.root])
        self.assertEqual(drift, [])

    def test_cross_cutting_topics_matching_vocab_has_no_drift(self):
        self.write("g/x.md", block("cross_cutting_topics", sorted(schema.CROSS_CUTTING_TOPICS_VOCAB)))
        drift, _ = run([self.root])
        self.assertEqual(drift, [])

    def test_unknown_schema_key_is_flagged(self):
        self.write("g/u.md", block("not_a_real_key", ["whatever"]))
        drift, _ = run([self.root])
        self.assertEqual(len(drift), 1)
        _, key, msgs = drift[0]
        self.assertEqual(key, "not_a_real_key")
        self.assertTrue(any("unknown schema key" in m for m in msgs))

    def test_drift_is_non_blocking_by_default_but_blocks_under_strict(self):
        self.write("g/p.md", block("promotion_stage", ["bogus-stage"]))
        drift_default, code_default = run([self.root])
        drift_strict, code_strict = run([self.root], strict=True)
        self.assertTrue(drift_default)  # drift exists
        self.assertEqual(code_default, 0)  # but default never blocks
        self.assertEqual(code_strict, 1)  # --strict turns drift into a failure

    def test_clean_run_exits_zero_even_under_strict(self):
        self.write("g/p.md", block("promotion_stage", sorted(schema.PROMOTION_STAGE_VOCAB)))
        drift, code = run([self.root], strict=True)
        self.assertEqual(drift, [])
        self.assertEqual(code, 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
