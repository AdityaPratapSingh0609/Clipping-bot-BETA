"""Discord Auto-Promotion Engine for YouTube Shorts & Instagram Reels.
Shares newly published videos to targeted Discord promotion communities.
"""
import json
import logging
import os
import random
import time
from pathlib import Path
import httpx

log = logging.getLogger("discord_promoter")

TARGET_DISCORD_SERVERS = [
    {"name": "Content Creators Hub", "invite": "https://discord.gg/EpAVdJJhQ", "code": "EpAVdJJhQ"},
    {"name": "Gaming Promotion Hub", "invite": "https://discord.gg/89VHYExvj", "code": "89VHYExvj"},
    {"name": "YouTube Growth & Promotion", "invite": "https://discord.gg/youtube-promotion-share-your-content-and-grow-838642670213660692", "code": "youtube-promotion-share-your-content-and-grow-838642670213660692"}
]

PROMO_TEMPLATES = [
    "🔥 **Unreal GTA 6 Moment!** {title}\nBro did this actually just happen live?! 💀\nCheck it out here: {url}\nDrop a like if you enjoyed! 🔔",
    "🚨 **Insane Stream Clip Alert!**\n*{title}*\nWatch this crazy play before it blows up: {url}\nWhat would you have done here? 👇",
    "💀 **Bro Almost Got Banned For This!**\n{title}\nWatch full clip: {url}\nLeave some love if this made you laugh! 😂",
    "🎮 **Best Stream Highlight Today!**\n{title}\nWatch now: {url}\nSubscribe / Follow for daily crazy clips! 🚀"
]

LOG_FILE = Path("discord_promo_log.json")

def load_promo_log():
    if LOG_FILE.exists():
        try:
            return json.loads(LOG_FILE.read_text(encoding="utf-8"))
        except Exception:
            return []
    return []

def save_promo_log(records):
    LOG_FILE.write_text(json.dumps(records, indent=2), encoding="utf-8")

def format_message(title: str, url: str) -> str:
    template = random.choice(PROMO_TEMPLATES)
    return template.format(title=title, url=url)

def promote_video(title: str, url: str, webhook_url: str = "") -> dict:
    """Send promotional message to Discord."""
    message = format_message(title, url)
    results = []
    log.info(f"Preparing Discord promotion for: '{title}' -> {url}")
    
    # Check if webhook is configured in env or passed
    webhook = webhook_url or os.environ.get("DISCORD_PROMO_WEBHOOK", "")
    
    if webhook:
        try:
            resp = httpx.post(webhook, json={"content": message}, timeout=15)
            success = resp.status_code in (200, 204)
            results.append({"method": "webhook", "status": "success" if success else f"HTTP {resp.status_code}"})
            log.info(f"Discord Webhook promotion sent: {resp.status_code}")
        except Exception as e:
            results.append({"method": "webhook", "status": f"error: {e}"})
            log.error(f"Discord Webhook error: {e}")
    else:
        # Log to promo records with server invite target metadata
        for srv in TARGET_DISCORD_SERVERS:
            results.append({
                "server": srv["name"],
                "invite": srv["invite"],
                "message": message,
                "queued_at": time.time(),
                "status": "ready_for_dispatch"
            })
            log.info(f"Queued promotion for Discord server '{srv['name']}' ({srv['invite']})")

    # Record history
    history = load_promo_log()
    history.append({
        "time": time.strftime("%Y-%m-%d %H:%M:%S"),
        "title": title,
        "url": url,
        "dispatches": results
    })
    save_promo_log(history)
    return {"ok": True, "dispatches": results}
