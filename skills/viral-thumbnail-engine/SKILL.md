---
name: viral-thumbnail-engine
description: Gemini-Powered Viral Thumbnail Engine. Generates high-CTR thumbnail concepts, expressive face crops, dynamic color grading, and high-contrast text overlays for vertical Shorts and Reels.
---

# Viral Thumbnail Engine Skill

## 1. High-CTR Principles for Shorts & Reels Covers
- **The Emotional Anchor**: High-arousal expressions (jaw drop, scream, disbelief, laughing hysterically).
- **Extreme Contrast & Saturation**: Boosted vibrance (+25%) and sharp contrast to pop on OLED smartphone screens and dark mode feeds.
- **Punchy Typography**: Maximum 3 to 4 words in ultra-bold sans-serif fonts (Impact, Montserrat, Bebas Neue). High-visibility colors: bright yellow (`#FFEA00`) or neon green (`#39FF14`) with thick black borders (`stroke=4px`) and soft drop shadow.
- **Curiosity Gap Visuals**: Highlighting the in-game action (explosions, glitch, police cars, red circles/arrows).

## 2. Gemini Visual Prompt Generation
- Automatically queries Gemini to extract the most sensational 2-word hook phrase and emotional description from the transcript.
- Generates high-res cover frame at peak action moment.

## 3. Automated Rendering Pipeline
- Extracts keyframe at peak audio/loudness moment using `ffmpeg`.
- Processes frame with Pillow (RGB normalization, contrast enhancement, text rasterization).
- Exports both `clipXX.jpg` cover thumbnail and preview card for YouTube & Instagram APIs.
