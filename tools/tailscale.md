---
type: tool
tool: tailscale
status: active
updated: 2026-05-06
---

# Tool: Tailscale

## Purpose

Tailscale creates a secure private mesh network between devices, allowing agents to reach VPS services, Proxmox, and other nodes without exposing them publicly.

## Used For

- Secure SSH access to VPS or Proxmox from local agent sessions
- Connecting OpenClaw on a remote server to local tooling
- Accessing private services (databases, internal APIs) across network boundaries
- Replacing public port exposure for sensitive services

## Safety Rules

- Tailscale auth keys and API keys must not be stored in this wiki.
- Device approval should require explicit admin action — do not enable auto-approval unless intentional.
- ACLs (access control lists) should be reviewed before adding new devices to the tailnet.
- Log VPN-accessed actions that have external consequences in [[../memory/runtime/logs/task-log]].

## Related Files

- [[../memory/categories/infrastructure]]
- [[../agents/OpenClaw]]

## Notes

- Tailscale MagicDNS allows reaching devices by hostname (e.g., `pve1`, `vps1`) within the tailnet.
- Tailscale exit nodes can route all traffic — use with care to avoid routing mismatches.
- Check `tailscale status` to verify current device connectivity before assuming a host is reachable.
