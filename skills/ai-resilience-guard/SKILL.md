---
name: ai-resilience-guard
description: AI Reliability & Fault-Tolerant Fallback Guard. Manages multi-model cascading fallback across Gemini, Gemma, and local heuristic engines so clip generation never stops.
---

# AI Resilience Guard Skill

## 1. Problem Root Causes
1. **Model Quota Exhaustion (429 Rate Limits)**:
   - Free tiers on specific preview models (`flash-lite`) have strict daily request and token ceilings.
2. **Provider 503 Spikes & Timeouts**:
   - High-demand spikes cause temporary 503 errors or socket timeouts.
3. **Pipeline Stalling**:
   - When all models fail, standard implementations throw unhandled `RuntimeError` and halt the clipping pipeline.

## 2. Permanent Architectural Fixes Applied
1. **6-Stage Cascading Fallback Chain**:
   - `gemini-3.5-flash` (Primary high-quota, fast reasoning)
   - `gemini-3.6-flash` (Secondary failover)
   - `gemini-3-flash-preview` (Tertiary failover)
   - `gemma-4-26b-a4b-it` (Open model failover)
   - `gemini-2.5-flash` (Stable LTS fallback)
   - `gemini-flash-latest` (General endpoint fallback)
2. **Exponential Backoff with Jitter**:
   - Automatically catches rate limits, inspects `retry-after` headers, and retries gracefully.
3. **Autonomous Heuristic Fallback Engine**:
   - If external APIs are completely unreachable or network drops, `_heuristic_clips_from_prompt` extracts peak moments from audio loudness + punctuation + dialogue clusters.
   - Clips are scored (88–92), titled, captioned, and rendered with zero pipeline disruption.
