"""Gemini-Powered Viral Thumbnail & Cover Generator for Shorts & Reels.
Generates vibrant, high-contrast, clickable 9:16 cover frames with bold typography.
"""
import logging
import os
import re
import subprocess
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter

log = logging.getLogger("thumbnails")

def extract_keyframe(video_path: Path, out_path: Path, timestamp: float = 2.0) -> bool:
    """Extract a high-quality frame at timestamp using ffmpeg."""
    try:
        cmd = [
            "ffmpeg", "-y", "-ss", str(timestamp), "-i", str(video_path),
            "-vframes", "1", "-q:v", "2", str(out_path)
        ]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        return out_path.exists() and out_path.stat().st_size > 5000
    except Exception as e:
        log.warning(f"Keyframe extraction failed at {timestamp}s: {e}")
        return False

def generate_viral_hook_text(title: str, hook: str = "") -> str:
    """Create a high-impact, 2-4 word punchy phrase suitable for large thumbnail text."""
    raw = hook or title
    clean = re.sub(r"[^\w\s!]", "", raw).strip().upper()
    words = clean.split()
    if len(words) <= 3:
        return " ".join(words)
    # Pick strong keywords
    buzzwords = ["NO WAY", "HE DID IT", "BUSTED", "INSANE", "WTF", "UNREAL", "LOST EVERYTHING", "BIGGEST L", "CAUGHT", "EPIC FAIL", "POLICE ESCAPE"]
    for b in buzzwords:
        if b in clean:
            return b
    return " ".join(words[:3])

def create_viral_thumbnail(video_path: Path, output_path: Path, title: str, hook: str = "") -> Path:
    """Generate a high-converting, high-CTR vertical thumbnail."""
    temp_frame = output_path.with_suffix(".raw.jpg")
    
    # Try frame at 2.0s, fallback to 1.0s or 0.5s
    if not extract_keyframe(video_path, temp_frame, 2.0):
        if not extract_keyframe(video_path, temp_frame, 1.0):
            extract_keyframe(video_path, temp_frame, 0.5)
            
    if not temp_frame.exists():
        raise RuntimeError(f"Could not extract frame from {video_path}")

    try:
        img = Image.open(temp_frame).convert("RGB")
        # Ensure 9:16 aspect ratio (1080x1920)
        img = img.resize((1080, 1920), Image.Resampling.LANCZOS)

        # 1. Boost Color Vibrance & Contrast
        enhancer = ImageEnhance.Color(img)
        img = enhancer.enhance(1.25)  # +25% saturation
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(1.20)  # +20% contrast

        # 2. Add Top & Bottom Subtle Vignette for Text Legibility
        overlay = Image.new("RGBA", (1080, 1920), (0, 0, 0, 0))
        draw_ov = ImageDraw.Draw(overlay)
        # Top gradient banner
        for y in range(400):
            alpha = int(140 * (1.0 - (y / 400.0)))
            draw_ov.line([(0, y), (1080, y)], fill=(0, 0, 0, alpha))
        # Bottom gradient banner
        for y in range(1520, 1920):
            alpha = int(160 * ((y - 1520) / 400.0))
            draw_ov.line([(0, y), (1080, y)], fill=(0, 0, 0, alpha))

        img = Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")
        draw = ImageDraw.Draw(img)

        # 3. Render Large Viral Hook Text Banner
        hook_text = generate_viral_hook_text(title, hook)
        
        # Try finding a bold font or fall back to default
        font_size = 90
        font = None
        for font_candidate in ["impact.ttf", "arialbd.ttf", "segoeuib.ttf", "tahoma.ttf"]:
            try:
                font = ImageFont.truetype(font_candidate, font_size)
                break
            except Exception:
                continue
        if not font:
            font = ImageFont.load_default()

        # Measure text
        bbox = draw.textbbox((0, 0), hook_text, font=font)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]

        # Draw Yellow Banner with Red Accent
        bx = (1080 - tw) // 2
        by = 220  # In upper third, optimal for mobile view

        # Background badge for text
        pad_x, pad_y = 30, 20
        badge_box = [bx - pad_x, by - pad_y, bx + tw + pad_x, by + th + pad_y]
        draw.rectangle(badge_box, fill=(220, 20, 20)) # High-energy red

        # Text with black stroke
        draw.text((bx, by), hook_text, font=font, fill=(255, 235, 0), stroke_width=6, stroke_fill=(0, 0, 0))

        img.save(output_path, "JPEG", quality=95)
        log.info(f"Generated viral thumbnail: {output_path} with hook '{hook_text}'")
        return output_path
    finally:
        temp_frame.unlink(missing_ok=True)
