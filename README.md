# 🎬 Clipping bot BETA
### Autonomous Multi-Channel Viral Stream & Shorts Distribution Engine

An end-to-end autonomous AI clipping and distribution system that ingests live streams from Twitch and YouTube, identifies viral gaming moments (90+ score) with Google Gemini and audio energy heuristics, generates 9:16 vertical high-contrast thumbnails, and publishes them across dedicated Spanish, Indian, and American channels based on peak audience viewership hours.

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
2. **`viral-thumbnail-engine`**: Uses Pillow & Gemini to extract keyframes, boost saturation & contrast (+20%), and overlay high-contrast yellow hook banners with black stroke.
3. **`discord-auto-promoter`**: Automatically broadcasts published links to target growth communities across Discord.
4. **`clip-render-repair`**: Protects rolling live buffers (180 mins) and falls back to VOD downloading on dropped fragments.
5. **`ai-resilience-guard`**: Cascades through 6 Gemini/Gemma models with automatic heuristic loudness/laughter failover.
6. **`streamer-discovery-engine`**: Real-time broadcast monitor for Twitch and YouTube live streams across 24 top creators.
7. **`meta-monetization-originality-guard`**: Transformative video filters (`eq=contrast=1.08:saturation=1.15`) preventing Meta Unoriginal Content strikes.
8. **`viral-velocity-1k-trainer`**: Optimizes retention loops, 3-second non-swipeable hooks, and Sends-per-Reach (SPR) triggers for rapid 1k+ view velocity.
9. **`master-watchdog`**: Self-healing supervisor managing process health, restarts, and anti-ban delays.

---

## 🚀 Quickstart

```bash
# 1. Install dependencies
pip install httpx pillow yt-dlp numpy

# 2. Run the master orchestrator
python orchestrator.py
```
