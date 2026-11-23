---
name: master-watchdog
description: Master System Watchdog & Self-Healing Service. Keeps PeakCut, live recording, multi-channel distribution, and anti-ban scheduling intact and running continuously with health checks and crash recovery.
---

# Master Watchdog Skill

## 1. Responsibilities
- **Service Supervision**: Monitors PeakCut server process (`http://127.0.0.1:8765`), Cloudflare tunnel, and background clipping threads.
- **Dynamic Pacing Enforcement**:
  - Automatically checks local IST clock and audience time zones.
  - During Peak Windows: enforces **2–3 min safety interval** per channel.
  - Outside Peak Windows: switches to **30–60 min interval** to preserve daily upload limits and audience retention.
- **Failover & Self-Healing**: Automatically revives stopped workers, handles network re-connections, and clears hung ffmpeg processes.
- **Live Status Reporting**: Continually writes real-time metrics and evidence links to `OVERNIGHT_VIRAL_REPORT.md`.
