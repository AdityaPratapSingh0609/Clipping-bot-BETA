---
name: discord-auto-promoter
description: Autonomous Discord Video & Reel Promotion Engine. Automatically shares published YouTube Shorts and Instagram Reels into targeted gaming and content promotion Discord servers to drive initial viewer velocity.
---

# Discord Auto-Promoter Skill

## 1. Target Promotion Servers
- **Server 1:** `https://discord.gg/EpAVdJJhQ`
- **Server 2:** `https://discord.gg/89VHYExvj`
- **Server 3:** `https://discord.gg/youtube-promotion-share-your-content-and-grow-838642670213660692`

## 2. High-Engagement Promotion Templates
To avoid being flagged as generic bot spam and maximize click-throughs from server members:
- **Format 1 (Curiosity Gap):**
  > "Bro did Kai Cenat / CarryMinati actually just do this in GTA 6?! 💀💀 Watch this before it gets taken down: [LINK] Drop your thoughts!"
- **Format 2 (Discussion Trigger):**
  > "Is this the craziest glitch in GTA 6 so far or what?! 😭 [LINK] What would you do in this situation?"
- **Format 3 (Short & Punchy):**
  > "Bro no way this just happened live 💀🚨 [LINK] #gaming #clips"

## 3. Automation Protocol
- Listens for `status == "posted"` events in PeakCut.
- Formats dynamic, non-repetitive promo copy with the live URL.
- Routes promo delivery safely via webhooks or user client session spaced by anti-spam delays (at least 120 seconds between servers).
