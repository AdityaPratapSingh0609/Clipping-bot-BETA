# 🚀 Autonomous Multi-Channel Viral Stream & Shorts Distribution Engine

An end-to-end autonomous pipeline that captures live streams, identifies viral gaming moments with Google Gemini, applies dynamic high-CTR captions, auto-renders vertical 9:16 cover thumbnails, and publishes them across dedicated Spanish, Indian, and American channels based on peak audience viewership hours.

---

## 🎯 Channel & Streamer Routing Matrix

| Channel / Account | Platform | Target Language | Allowed Streamers | Peak Hour Pacing |
|---|---|---|---|---|
| **Captain Inc.** | YouTube | Spanish (`es`) | Ibai, AuronPlay, IlloJuan, Rubius, TheGrefg, ElSpreen | 2.5 min (Peak) / 30 min (Off-peak) |
| **Soop Clips** | YouTube | Hindi (`hi`) | CarryisLive, Techno Gamerz, Total Gaming, Mortal, Samay Raina, Mythpat | 2.5 min (Peak) / 30 min (Off-peak) |
| **Aditya Singh** | YouTube | Hindi (`hi`) | CarryisLive, Techno Gamerz, Total Gaming, Mortal, Samay Raina, Mythpat | 2.5 min (Peak) / 30 min (Off-peak) |
| **Sooptipoop** | YouTube | English (`en`) | Kai Cenat, IShowSpeed, CaseOh, xQc, Jynxzi, MoistCr1TiKaL, Adin Ross | 2.5 min (Peak) / 30 min (Off-peak) |
| **Mild.lywashed** | YouTube | English (`en`) | Kai Cenat, IShowSpeed, CaseOh, xQc, Jynxzi, MoistCr1TiKaL, Adin Ross | 2.5 min (Peak) / 30 min (Off-peak) |
| **@mild.lywashed** | Instagram | English (`en`) | Kai Cenat, IShowSpeed, CaseOh, xQc, Jynxzi, MoistCr1TiKaL, Adin Ross | 2.5 min (Peak) / 30 min (Off-peak) |

---

## 🕒 Peak Viewership Hours Intelligence

- **India Audience (IST)**:
  - **Peak Window:** 6:00 PM – 10:30 PM IST (Evening Rush) & 12:00 PM – 2:30 PM IST (Lunch).
  - **Pacing:** High-frequency burst uploads at **2–3 min intervals**.
- **United States Audience (EST / PST)**:
  - **Peak Window (in IST):** 10:30 PM – 1:30 AM IST (US Lunch) & 4:30 AM – 8:30 AM IST (US Prime Evening).
  - **Pacing:** High-frequency burst uploads at **2–3 min intervals**.
- **Spain & LatAm Audience (CET / ART / CST)**:
  - **Peak Window (in IST):** 11:30 PM – 4:30 AM IST (Prime Evening).
  - **Pacing:** High-frequency burst uploads at **2–3 min intervals**.
- **Off-Peak Standard Hours**:
  - Automatically paces uploads at **30–60 min intervals** to prevent channel burnout.

---

## 🛠️ Integrated Skills & Subsystems

1. **`viral-stream-distributor`**: Directs stream ingestion and schedules posts to respective channels according to language.
2. **`viral-thumbnail-engine`**: Uses Pillow & Gemini to extract keyframes, boost saturation & contrast, and overlay high-contrast yellow/red hook banners.
3. **`discord-auto-promoter`**: Automatically broadcasts published links to target growth communities.
4. **`clip-render-repair`**: Protects rolling live buffers (180 mins) and falls back to VOD downloading on dropped fragments.
5. **`ai-resilience-guard`**: Cascades through 6 Gemini/Gemma models with automatic heuristic loudness/laughter failover.
6. **`streamer-discovery-engine`**: Real-time broadcast monitor for Twitch and YouTube live streams.
7. **`master-watchdog`**: Self-healing supervisor managing process health, restarts, and anti-ban delays.

---

## 🚀 Quickstart

```bash
# 1. Install dependencies
pip install httpx pillow yt-dlp numpy

# 2. Run the master orchestrator
python orchestrator.py
```
