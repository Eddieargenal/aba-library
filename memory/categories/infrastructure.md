---
type: memory-category
scope: infrastructure
status: validated
updated: 2026-05-06
---

# Infrastructure — Servers, Networks, Configs

Stores factual infrastructure knowledge. All entries must cite sources.

## Claim Types

| Type | When to Use |
|------|-------------|
| ✅ Fact | Verified server config, IP, network setup |
| 🔹 Inference | Derived from logs or commands (cite the command) |

## Format

```markdown
### [resource-name]
- type: infrastructure
- status: draft | reviewed | validated | stale
- claim_type: fact | inference
- source: [command output, screenshot, documentation link]
- verified: YYYY-MM-DD
- updated: YYYY-MM-DD

## Details
[configuration or details]

## Source Evidence
[command run or link to documentation]
```

## Examples

### Fact Example

```markdown
### vps-production
- type: infrastructure
- status: validated
- claim_type: fact
- source: VPS shell access via SSH, 2026-05-06
- verified: 2026-05-06
- updated: 2026-05-06

## Details
- IP: 107.172.157.153
- OS: Ubuntu 22.04
- Services: Odoo 17, PostgreSQL 14
- Ports: 22, 80, 443, 8069

## Source Evidence
$ ssh admin@107.172.157.153 "uname -a && systemctl list-units --type=service"
```

### Inference Example

```markdown
### proxmox-network-inference
- type: infrastructure
- status: reviewed
- claim_type: inference
- source: ping test from Mac mini to 192.168.1.3, 2026-05-06
- verified: 2026-05-06
- updated: 2026-05-06

## Details
- Proxmox on 192.168.1.3 accessible from Mac mini LAN

## Source Evidence
$ ping -c 3 192.168.1.3
PING 192.168.1.3 (192.168.1.3): 56 data bytes
64 bytes from 192.168.1.3: icmp_seq=0 ttl=64 time=1.234 ms
```

## Superseding

When infrastructure changes, mark old entry as superseded:

```markdown
### Superseded
- date: 2026-05-06
- superseded_by: vps-production-v2
- reason: New VPS provisioned
```