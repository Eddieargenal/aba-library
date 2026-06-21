---
status: accepted
date: 2026-06-21
---

# Publishing gates on criticals only; warnings are advisory and index health is observed, not enforced

Atomic publication to `indexes/current/` is gated on **zero critical lint failures and nothing else**. Warnings never block publication; `--strict` (which would block on any warning) stays **opt-in, off by default**. Index-health metrics (`orphan_pct`, `ghost_pct`, `stale_pct`) are computed and stamped into `manifest.health` (ADR follows #28) as an **observability** signal for humans to watch over time — they are **not** a publish gate.

This is a deliberate design choice, recorded so the absence of a health/warning gate is not mistaken for an oversight.

## Why not make `--strict` the default

The vault is deliberately sparse while findings are being routed into pages (#13). Today the build carries 31 warnings and reads 84.6% orphan / 58.3% ghost — these reflect *expected sparsity*, not degradation. Defaulting to `--strict` would set `published: false` on every build and halt the very population work that resolves the warnings. Strictness is only meaningful once there is content to be strict about.

## Why not gate on a health ceiling now

Same reason. Any defensible ceiling (e.g. orphan ≤ 30%) fails immediately on a sparse vault, blocking all publishes; a ceiling permissive enough to pass the current 84.6% would be meaningless. A health gate only earns its keep once a populated vault makes a *rising* orphan/ghost rate a genuine degradation signal rather than a sparsity artifact.

## What gates instead

The critical lint failures — the data-integrity floor — remain the hard gate: missing/duplicate `id`, invalid YAML, missing required fields, an unsupported `usable` claim (`missing_source_basis_usable`), broken section anchors. These are correctness, not health, and they block publish as before. Warnings and `manifest.health` are surfaced (printed at build time and stamped into the manifest) for humans to track the trend.

## Consequence

`build_status` stays `valid_with_warnings`, but it is no longer the only signal: `manifest.health` carries the orphan/ghost/stale trend alongside it. No code change to the publish gate; `--strict` remains available for anyone who wants a clean-only build locally or in CI.

**Revisit when:** the vault is substantially populated (#13). At that point a rising orphan/ghost rate becomes a real degradation signal, and a health-ceiling or strict-default gate should be reconsidered (the enforcement mechanism, if adopted, is future work).
