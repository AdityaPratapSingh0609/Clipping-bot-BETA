---
name: streamer-discovery-engine
description: Automated Top Streamer Discovery Engine. Scrapes and tracks Top 5 active streamers across Twitch & YouTube in Spanish, English, and Hindi, and auto-enqueues them into PeakCut.
---

# Streamer Discovery Engine Skill

## 1. Targeted Language Categories
1. **SPANISH (Español)**:
   - Primary: `Ibai`, `AuronPlay`, `IlloJuan`, `Rubius`, `TheGrefg`, `ElSpreen`
   - Platform Focus: Twitch & YouTube Gaming
   - Auto-mapped to: `Captain Inc.` (`yt_UCkjgTZmBmsDSQyLS_mcSkZg`)
2. **INDIAN (Hindi / Hinglish)**:
   - Primary: `CarryisLive`, `Techno Gamerz`, `Total Gaming`, `Mortal`, `Samay Raina`, `Mythpat`, `Scout`
   - Platform Focus: YouTube Gaming
   - Auto-mapped to: `Soop Clips` (`yt_UCbfjzxY9e8OkUG-S_rjFqjg`) and `Aditya Singh` (`yt_UCB_RlbZjHvjyhJPSvOOwAYw`)
3. **AMERICAN / GLOBAL (English)**:
   - Primary: `Kai Cenat`, `IShowSpeed`, `CaseOh`, `xQc`, `Jynxzi`, `MoistCr1TiKaL`, `Adin Ross`
   - Platform Focus: Twitch, YouTube, Kick
   - Auto-mapped to: `Sooptipoop` (`yt_UCEkDIG0cAeSjUKN5oUovO1w`), `Mild.lywashed` (`yt_UCg7auwLdmZqecnojVbFaXKg`), and Instagram `@mild.lywashed`

## 2. Real-Time Discovery Protocol
- Monitors Twitch GraphQL / GQL and YouTube live endpoints for active broadcasts.
- Checks live concurrent viewership (filters for streams with > 10,000 live viewers).
- Verifies gaming / GTA / high-energy category.
- Triggers PeakCut's `live.watch()` daemon to begin rolling buffer recording and real-time highlight slicing.
