---
type: governance
status: active
created: 2026-05-18
updated: 2026-05-18
---

# ID Registry

## Stable Prefixes

Canonical page-id prefixes — verified against `scripts/schema.py:ID_PREFIX_BY_TYPE`:

```schema:id_prefix
S- source
C- concept
F- framework
T- tool
I- field-instrument
R- risk
KTN- known-tension
P- advisory-playbook
D- decision-protocol
O- output-template
SS- slice-spec
OVR- overview
```

Runtime-only prefixes (not page ids, not validated by the index builder): `EP-` evidence packet, `PU-` proposed update.

## Registry Rule

Relationships must target stable IDs, never file paths.
