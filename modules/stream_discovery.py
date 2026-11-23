"""Streamer Discovery Engine.
Continuously scans Twitch and YouTube for active Top-5 streamers across Spanish, English, and Hindi.
"""
import logging
import time
from pathlib import Path
import httpx
from studio import creators, ctx, live

log = logging.getLogger("stream_discovery")

STREAMERS_REGISTRY = {
    "es": [
        {"id": "ibai", "name": "Ibai Llanos", "platform": "twitch", "channel": "ibai", "target": "yt_UCkjgTZmBmsDSQyLS_mcSkZg"},
        {"id": "auronplay", "name": "AuronPlay", "platform": "twitch", "channel": "auronplay", "target": "yt_UCkjgTZmBmsDSQyLS_mcSkZg"},
        {"id": "illojuan", "name": "IlloJuan", "platform": "twitch", "channel": "illojuan", "target": "yt_UCkjgTZmBmsDSQyLS_mcSkZg"},
        {"id": "rubius", "name": "Rubius", "platform": "twitch", "channel": "rubius", "target": "yt_UCkjgTZmBmsDSQyLS_mcSkZg"},
        {"id": "thegrefg", "name": "TheGrefg", "platform": "twitch", "channel": "thegrefg", "target": "yt_UCkjgTZmBmsDSQyLS_mcSkZg"},
        {"id": "elspreen", "name": "ElSpreen", "platform": "twitch", "channel": "elspreen", "target": "yt_UCkjgTZmBmsDSQyLS_mcSkZg"},
    ],
    "hi": [
        {"id": "carryminati", "name": "CarryisLive", "platform": "youtube", "channel": "https://www.youtube.com/@CarryisLive/live", "target": "yt_UCbfjzxY9e8OkUG-S_rjFqjg"},
        {"id": "techno-gamerz", "name": "Techno Gamerz", "platform": "youtube", "channel": "https://www.youtube.com/@TechnoGamerzOfficial/live", "target": "yt_UCbfjzxY9e8OkUG-S_rjFqjg"},
        {"id": "total-gaming", "name": "Total Gaming", "platform": "youtube", "channel": "https://www.youtube.com/@TotalGaming093/live", "target": "yt_UCB_RlbZjHvjyhJPSvOOwAYw"},
        {"id": "mortal", "name": "Mortal", "platform": "youtube", "channel": "https://www.youtube.com/@Mortalyt/live", "target": "yt_UCB_RlbZjHvjyhJPSvOOwAYw"},
        {"id": "samay-raina", "name": "Samay Raina", "platform": "youtube", "channel": "https://www.youtube.com/@samayraina/live", "target": "yt_UCbfjzxY9e8OkUG-S_rjFqjg"},
        {"id": "mythpat", "name": "Mythpat", "platform": "youtube", "channel": "https://www.youtube.com/@Mythpat/live", "target": "yt_UCB_RlbZjHvjyhJPSvOOwAYw"},
    ],
    "en": [
        {"id": "kai-cenat-live", "name": "Kai Cenat", "platform": "twitch", "channel": "kaicenat", "target": "yt_UCEkDIG0cAeSjUKN5oUovO1w"},
        {"id": "ishowspeed", "name": "IShowSpeed", "platform": "youtube", "channel": "https://www.youtube.com/@IShowSpeed/live", "target": "yt_UCg7auwLdmZqecnojVbFaXKg"},
        {"id": "caseoh", "name": "CaseOh", "platform": "twitch", "channel": "caseoh_", "target": "ig_17841471973196375"},
        {"id": "xqc", "name": "xQc", "platform": "twitch", "channel": "xqc", "target": "yt_UCEkDIG0cAeSjUKN5oUovO1w"},
        {"id": "jynxzi", "name": "Jynxzi", "platform": "twitch", "channel": "jynxzi", "target": "yt_UCg7auwLdmZqecnojVbFaXKg"},
        {"id": "moistcr1tikal", "name": "MoistCr1TiKaL", "platform": "twitch", "channel": "moistcr1tikal", "target": "ig_17841471973196375"},
    ]
}

def check_twitch_live(channel_name: str) -> bool:
    """Fast check whether a Twitch streamer is currently live using public endpoint."""
    try:
        url = f"https://www.twitch.tv/{channel_name}"
        headers = {"User-Agent": "Mozilla/5.0"}
        r = httpx.get(url, headers=headers, timeout=10, follow_redirects=True)
        return '"isLiveBroadcast":true' in r.text or 'isLive' in r.text
    except Exception:
        return False

def discover_active_streams() -> list:
    """Scan all top streamers across Spanish, Hindi, and English and return active ones."""
    active = []
    log.info("Scanning for active Top-5 streamers across Spanish, Hindi, and English...")
    for lang, streamers in STREAMERS_REGISTRY.items():
        for s in streamers:
            is_live = False
            if s["platform"] == "twitch":
                is_live = check_twitch_live(s["channel"])
            if is_live:
                log.info(f"Streamer IS LIVE: [{lang.upper()}] {s['name']} on {s['platform']}")
                active.append({**s, "lang": lang})
    log.info(f"Active live streamers detected: {len(active)}")
    return active
