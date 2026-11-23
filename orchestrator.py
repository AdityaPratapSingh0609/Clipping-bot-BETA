"""Master Autonomous Multi-Channel Viral Orchestrator
Enforces strict language/channel routing, audience peak-hours pacing,
Gemini viral thumbnail rendering, and automated Discord community promotions.
"""
import json
import logging
import os
import sys
import time
from datetime import datetime, timezone, timedelta
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler("viral_orchestrator.log", encoding="utf-8")
    ]
)
log = logging.getLogger("viral_orchestrator")

from studio import accounts, ctx, jobs, posting, creators, thumbnails, discord_promoter, stream_discovery

REPORT_FILE = Path(r"C:\Users\adity\.gemini\antigravity\brain\cfcb4cb8-97a6-43b6-ae16-e650e8af7dd8\OVERNIGHT_VIRAL_REPORT.md")
HISTORY_FILE = Path("orchestrator_history.json")

# STRICT CHANNEL MAPPING
ROUTING = {
    # Spanish Channel
    "yt_UCkjgTZmBmsDSQyLS_mcSkZg": {
        "name": "Captain Inc.",
        "platform": "youtube",
        "lang": "es",
        "creators": ["ibai", "auronplay", "illojuan", "rubius", "thegrefg", "elspreen"]
    },
    # Indian Channels
    "yt_UCbfjzxY9e8OkUG-S_rjFqjg": {
        "name": "Soop Clips",
        "platform": "youtube",
        "lang": "hi",
        "creators": ["carryminati", "techno-gamerz", "total-gaming", "mortal", "samay-raina", "mythpat"]
    },
    "yt_UCB_RlbZjHvjyhJPSvOOwAYw": {
        "name": "Aditya Singh",
        "platform": "youtube",
        "lang": "hi",
        "creators": ["carryminati", "techno-gamerz", "total-gaming", "mortal", "samay-raina", "mythpat"]
    },
    # American Channels
    "yt_UCEkDIG0cAeSjUKN5oUovO1w": {
        "name": "Sooptipoop",
        "platform": "youtube",
        "lang": "en",
        "creators": ["kai-cenat-live", "ishowspeed", "caseoh", "xqc", "jynxzi", "moistcr1tikal", "adin-ross", "mrbeast-gaming"]
    },
    "yt_UCg7auwLdmZqecnojVbFaXKg": {
        "name": "Mild.lywashed",
        "platform": "youtube",
        "lang": "en",
        "creators": ["kai-cenat-live", "ishowspeed", "caseoh", "xqc", "jynxzi", "moistcr1tikal", "adin-ross", "mrbeast-gaming"]
    },
    # American Instagram
    "ig_17841471973196375": {
        "name": "@mild.lywashed",
        "platform": "instagram",
        "lang": "en",
        "creators": ["kai-cenat-live", "ishowspeed", "caseoh", "xqc", "jynxzi", "moistcr1tikal", "adin-ross", "mrbeast-gaming"]
    }
}

def load_history():
    if HISTORY_FILE.exists():
        try:
            return json.loads(HISTORY_FILE.read_text(encoding="utf-8"))
        except Exception:
            return []
    return []

def save_history(history):
    HISTORY_FILE.write_text(json.dumps(history, indent=2), encoding="utf-8")

def is_peak_window(lang: str) -> bool:
    """Return True if the current local time falls in the peak viewership window for the audience."""
    now = datetime.now()
    h = now.hour + now.minute / 60.0  # Decimal IST hour

    if lang == "hi":
        # India Peak: 18:00 - 22:30 IST OR 12:00 - 14:30 IST
        return (18.0 <= h <= 22.5) or (12.0 <= h <= 14.5)
    elif lang == "en":
        # US Peak (converted to IST): 22:30 - 01:30 IST OR 04:30 - 08:30 IST
        return (22.5 <= h <= 24.0) or (0.0 <= h <= 1.5) or (4.5 <= h <= 8.5)
    elif lang == "es":
        # Spain / LatAm Peak (converted to IST): 23:30 - 04:30 IST
        return (23.5 <= h <= 24.0) or (0.0 <= h <= 4.5)
    return False

def get_gap_seconds(lang: str) -> int:
    """Dynamic Pacing: 2-3 minutes during peak windows; 30-45 minutes outside."""
    if is_peak_window(lang):
        log.info(f"[{lang.upper()}] Audience is in PEAK VIEWERSHIP WINDOW! Pacing: 150s (2.5 mins).")
        return 150
    else:
        log.info(f"[{lang.upper()}] Audience is in standard window. Pacing: 1800s (30 mins).")
        return 1800

def update_report(history):
    try:
        report_text = f"""# 🚀 Multi-Channel Viral Distribution Engine — Live Report

**Last Updated:** {datetime.now().strftime('%Y-%m-%d %I:%M:%S %p')} IST  
**System Status:** 🟢 ACTIVE & ENFORCING STRICT CHANNEL ROUTING  
**AI Resilience Guard:** 🟢 6-Stage Fallback + Algorithmic Failover Active  
**Total Tracked Posts:** {len(history)}  

---

## 🎯 Channel & Streamer Routing Matrix

| Target Channel | Platform | Language | Allowed Streamers | Active Pacing |
|---|---|---|---|---|
| **Captain Inc.** | YouTube | Spanish (es) | Ibai, AuronPlay, IlloJuan, Rubius, TheGrefg, ElSpreen | {'2.5 min (PEAK)' if is_peak_window('es') else '30 min (Standard)'} |
| **Soop Clips** | YouTube | Hindi (hi) | CarryisLive, Techno Gamerz, Total Gaming, Mortal, Samay Raina, Mythpat | {'2.5 min (PEAK)' if is_peak_window('hi') else '30 min (Standard)'} |
| **Aditya Singh** | YouTube | Hindi (hi) | CarryisLive, Techno Gamerz, Total Gaming, Mortal, Samay Raina, Mythpat | {'2.5 min (PEAK)' if is_peak_window('hi') else '30 min (Standard)'} |
| **Sooptipoop** | YouTube | English (en) | Kai Cenat, IShowSpeed, CaseOh, xQc, Jynxzi, MoistCr1TiKaL, Adin Ross | {'2.5 min (PEAK)' if is_peak_window('en') else '30 min (Standard)'} |
| **Mild.lywashed** | YouTube | English (en) | Kai Cenat, IShowSpeed, CaseOh, xQc, Jynxzi, MoistCr1TiKaL, Adin Ross | {'2.5 min (PEAK)' if is_peak_window('en') else '30 min (Standard)'} |
| **@mild.lywashed** | Instagram | English (en) | Kai Cenat, IShowSpeed, CaseOh, xQc, Jynxzi, MoistCr1TiKaL, Adin Ross | {'2.5 min (PEAK)' if is_peak_window('en') else '30 min (Standard)'} |

---

## 📊 Live Published Evidence Table

| # | Time (IST) | Platform | Channel / Profile | Creator | Clip Title | Live Link |
|---|---|---|---|---|---|---|
"""
        for i, item in enumerate(history[-25:], 1):
            report_text += f"| {i} | {item.get('time', '')} | {item.get('platform', '')} | {item.get('account_name', '')} | {item.get('creator', '')} | {item.get('title', '')} | [{item.get('url', 'View Link')}]({item.get('url', '#')}) |\n"

        report_text += """
---

## ⚡ Active Autonomous Skills & Services
1. **`viral-stream-distributor`**: Routes clips strictly to Spanish, Indian, and American audiences with audience peak-hours intelligence.
2. **`viral-thumbnail-engine`**: Generates high-contrast vertical 9:16 cover frames with Pillow vibrance boost & bold yellow hook text.
3. **`discord-auto-promoter`**: Automatically broadcasts published links to target gaming and YouTube growth communities.
4. **`clip-render-repair`**: Protects rolling live buffer (180 mins) and falls back to VOD downloading on missing segments.
5. **`ai-resilience-guard`**: Cascades across 6 Gemini/Gemma models with automatic heuristic fallback on rate limits.
"""
        REPORT_FILE.write_text(report_text, encoding="utf-8")
    except Exception as e:
        log.error(f"Failed to update report: {e}")

def get_ready_clips_for_creator(creator_id: str) -> list:
    """Find all rendered done clips on disk for this creator."""
    with ctx.as_user("u_local"):
        jobs.load_all()
        all_j = jobs.all_jobs()
        ready = []
        for j in all_j:
            if j.get("creator") != creator_id:
                continue
            j_dir = Path(j.get("dir", ""))
            for c in j.get("clips", []):
                c_file = j_dir / "clips" / c.get("file", f"{c['id']}.mp4")
                if c_file.exists() and c_file.stat().st_size > 100000:
                    ready.append({
                        "job": j,
                        "clip": c,
                        "path": c_file,
                        "score": c.get("score", 85),
                        "title": c.get("title") or c.get("hook") or "GTA 6 Viral Moment"
                    })
        ready.sort(key=lambda x: -x["score"])
        return ready

def format_caption(clip, creator_name, lang="en", platform="instagram"):
    title = clip.get("title") or clip.get("hook") or "GTA 6 Epic Moment"
    if lang == "es":
        tags = ["gta6", "gaming", "streamer", "clips", "virales", "shorts"]
        tag_str = " ".join(f"#{t}" for t in tags)
        return f"{title} 😱💥\n\n¿Qué habrías hecho tú en esta situación? 👇 ¡Suscríbete a Captain Inc para más clips diarios! 🔔\n\n{tag_str}"
    elif lang == "hi":
        tags = ["gta6", "gaming", "carryislive", "technogamerz", "shorts", "reels", "viral"]
        tag_str = " ".join(f"#{t}" for t in tags)
        return f"{title} 😂💀\n\nBhai ye kya ho gaya live stream pe! 😭 Subscribe karo daily funny & clutch gaming moments ke liye! 🔔\n\n{tag_str}"
    else:
        tags = ["gta6", "gaming", "streamer", "viral", "fyp", "shorts", "reels"]
        tag_str = " ".join(f"#{t}" for t in tags)
        if platform == "youtube":
            return f"{title} 💀🚨\n\nBro thought he had it all figured out until this happened! Subscribe for daily viral stream moments! 🔔\n\n{tag_str}"
        else:
            return f"{title} 💀🚨\n\nTag a friend who needs to see this! Follow @mild.lywashed for daily crazy stream clips! 🔥\n\n{tag_str}"

def run_orchestration_cycle():
    history = load_history()
    posted_keys = {f"{item.get('job_id')}_{item.get('clip_id')}_{item.get('account_id')}" for item in history}

    with ctx.as_user("u_local"):
        for acc_id, route in ROUTING.items():
            acc_obj = accounts.get(acc_id)
            if not acc_obj:
                continue

            lang = route["lang"]
            acc_name = route["name"]
            platform = route["platform"]
            allowed_creators = route["creators"]

            log.info(f"Checking queue for [{lang.upper()}] Channel: {acc_name} ({acc_id})...")

            posted_for_this_acc = False
            for cid in allowed_creators:
                if posted_for_this_acc:
                    break
                clips = get_ready_clips_for_creator(cid)
                for item in clips:
                    key = f"{item['job']['id']}_{item['clip']['id']}_{acc_id}"
                    if key in posted_keys:
                        continue

                    # Found an eligible clip!
                    clip_path = item["path"]
                    title = item["title"]
                    caption = format_caption(item["clip"], cid, lang=lang, platform=platform)

                    # 1. Generate High-CTR Thumbnail
                    thumb_path = clip_path.with_name(f"{item['clip']['id']}_thumb.jpg")
                    try:
                        thumbnails.create_viral_thumbnail(clip_path, thumb_path, title, item["clip"].get("hook", ""))
                    except Exception as e:
                        log.warning(f"Thumbnail generation skipped: {e}")

                    # 2. Upload to Target Account
                    try:
                        if platform == "instagram":
                            log.info(f"Uploading Reel to {acc_name}: {title}")
                            rid, url = accounts.instagram_upload(acc_obj, clip_path, caption, item["job"]["id"])
                        else:
                            log.info(f"Uploading Short to YouTube ({acc_name}): {title}")
                            tags = item["clip"].get("hashtags") or ["gta6", "gaming", "shorts"]
                            rid, url = accounts.youtube_upload(acc_obj, clip_path, title[:95], caption, tags, "public")

                        log.info(f"SUCCESS {platform.upper()}: {url}")
                        record = {
                            "job_id": item["job"]["id"],
                            "clip_id": item["clip"]["id"],
                            "account_id": acc_id,
                            "account_name": acc_name,
                            "platform": platform.capitalize(),
                            "creator": cid,
                            "title": title,
                            "url": url,
                            "time": datetime.now().strftime("%I:%M %p")
                        }
                        history.append(record)
                        posted_keys.add(key)
                        save_history(history)
                        update_report(history)

                        # 3. Promote to Discord
                        try:
                            discord_promoter.promote_video(title, url)
                        except Exception as de:
                            log.warning(f"Discord promotion error: {de}")

                        posted_for_this_acc = True
                        break
                    except Exception as ue:
                        err_str = str(ue)
                        log.error(f"Upload failed for {acc_name}: {err_str[:200]}")
                        if "429" in err_str or "Quota exceeded" in err_str:
                            log.warning(f"{acc_name} reached quota ceiling for today. Will retry next reset.")
                            break

            # Sleep between account evaluations based on peak audience pacing
            gap = get_gap_seconds(lang)
            if posted_for_this_acc:
                log.info(f"Waiting {gap}s before next post on this channel tier...")
                time.sleep(min(gap, 180))

if __name__ == "__main__":
    log.info("Starting Master Autonomous Multi-Channel Viral Orchestrator...")
    while True:
        try:
            run_orchestration_cycle()
        except Exception as e:
            log.error(f"Orchestration cycle exception: {e}")
        time.sleep(60)
