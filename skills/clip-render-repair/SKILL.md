---
name: clip-render-repair
description: Diagnostics and Self-Healing Engine for PeakCut Video Rendering. Prevents buffer eviction errors, handles VOD piece fallback, and auto-recovers interrupted clips.
---

# Clip Render Repair Skill

## 1. Problem Root Causes
1. **Live Rolling Buffer Eviction (`That part of the stream is no longer in the buffer`)**:
   - Short default buffer retention (20 min) deleted `.ts` transport stream segments before AI could analyze and render them.
2. **Buffer Destruction on Stream Stop (`cleanup()`)**:
   - Stream end callbacks previously purged the buffer immediately even while clips were still queued or rendering.
3. **Restart Invalidation in `_load_file()`**:
   - On server restart, in-progress clips were set to `status: "error"` instead of resuming or validating finished mp4 files on disk.

## 2. Permanent Architectural Fixes Applied
1. **Dynamic Segment Lock**:
   - `keep_from = min(self.seg_clock - buf_min * 60, needed_start - 30.0)` ensures no buffer piece is unlinked while a clip needs it.
2. **Autonomous VOD Recovery Fallback**:
   - If buffer segments are missing, `live.py` automatically falls back to `media.download_section(vod_url)` via `yt-dlp` directly from the stream VOD!
3. **Safe Cleanup Barrier**:
   - `cleanup()` checks for any `queued` or `rendering` clips in the job before unlinking.
4. **Disk Self-Healing in `jobs.py` & `posting.py`**:
   - If the rendered MP4 exists on disk and is > 100KB, it automatically marks `status: "done"` and proceeds to publishing without error.
