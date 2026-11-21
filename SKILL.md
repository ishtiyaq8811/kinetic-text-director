---
name: kinetic-text-director
description: An autonomous AI skill for directing dynamic kinetic typography, subtitle pop-in, and punchy 60fps vertical reel animations for video creators, educators, and social media producers.
version: 1.0.0
author: ishtiyaq8811
license: MIT
platforms:
  - Claude / Claude Code
  - Google Antigravity
  - Google Gemini
  - ChatGPT / Custom GPTs
  - Muse AI
---

# Kinetic Typography Reel Director

```
+-------------------------------------------------------+
|  [⚡ KINETIC TYPOGRAPHY DIRECTOR]    [🔊 AUDIO: ON]   |
+-------------------------------------------------------+
|                                                       |
|                     ( 9:16 Reel )                     |
|                                                       |
|                 +-------------------+                 |
|                 |                   |                 |
|                 |      CODE IS      |   <- Pop-in     |
|                 |     NO LONGER     |                 |
|                 |   *WRITTEN*       |   <- Highlight  |
|                 |     ALONE.        |      (Glow)     |
|                 |                   |                 |
|                 | — CH 1: SHIFT —   |   <- Subtitle   |
|                 +-------------------+                 |
|                                                       |
|       [=== Timeline: 2.4s / 10.0s =============]      |
|                                                       |
+-------------------------------------------------------+
|  [⏸ Pause]   [🔄 Replay]   [Aspect: 9:16]             |
+-------------------------------------------------------+
```

## Overview
**Kinetic Typography Reel Director** is a self-contained AI skill designed to convert scripts, quotes, technical explainers, and key ideas into punchy, high-retention 60fps kinetic typography reels.

It requires **zero external API keys**, **zero cloud rendering costs**, and **zero pip dependencies**. It generates lightweight, standalone HTML5 Canvas/SVG engines with built-in procedural Web Audio synthesis for sound effects (pops, whooshes, and chimes).

---

## ⚡ Step-by-Step Agent Workflow

When invoked to create or direct a kinetic typography reel:

1. **Deconstruct the Script into Beats:**
   - Break down input text into sequential phrases (3 to 8 words per phrase).
   - Aim for a total video duration between 6 to 15 seconds for optimal social retention.
2. **Assign Animation & Pacing:**
   - Assign pacing: typically 1,800ms to 3,000ms per phrase.
   - Choose animation styles per beat: `pop-in`, `slam-zoom`, `glow-burst`, `slide-up`, or `typewriter`.
3. **Select High-Impact Keywords:**
   - Mark 1–2 crucial focal words in each phrase inside `highlightWords`.
4. **Choose Color Aesthetic & Theme:**
   - Available themes: `electric-neon`, `cyberpunk`, `sunset-glow`, `minimal-dark`, `clean-paper`.
5. **Compile Standalone HTML Reel:**
   - Generate the JSON spec and run `python build.py <spec.json>` to produce a standalone `.reel.html` playable in any browser.

---

## 📐 Specification Schema

```json
{
  "title": "Title of Reel",
  "aspectRatio": "9:16",
  "theme": "electric-neon",
  "fps": 60,
  "soundEffects": true,
  "phrases": [
    {
      "text": "Idea to viral reel in seconds.",
      "durationMs": 2500,
      "animation": "pop-in",
      "highlightWords": ["viral", "seconds"],
      "subtitle": "Kinetic Text Engine"
    }
  ]
}
```

### Parameter Reference
| Property | Type | Default | Description |
|---|---|---|---|
| `title` | string | required | Project title or header label |
| `aspectRatio` | string | `"9:16"` | `"9:16"` (Reels/Shorts), `"16:9"` (YouTube), or `"1:1"` (Square) |
| `theme` | string | `"electric-neon"` | Color palette: `electric-neon`, `cyberpunk`, `sunset-glow`, `minimal-dark`, `clean-paper` |
| `soundEffects` | boolean | `true` | Procedural Web Audio synth pops, whooshes, and chimes |
| `phrases` | array | required | Array of phrase objects with `text`, `durationMs`, `animation`, `highlightWords`, and `subtitle` |

---

## 🎨 Aesthetic & Taste Standards

- **Word Economy:** Keep phrases punchy. Maximum 10 words per phrase; ideal is 4–6 words.
- **Rhythm & Timing:** Never display text faster than 1,200ms or slower than 3,500ms per phrase.
- **Contrast Guarantee:** Dark backgrounds strictly pair with bright high-contrast typography and glowing accents.
- **Visual Breathing Room:** Never allow text to touch viewport borders; 15% padding is strictly enforced by the engine.

---

## 🛠 Platform Adapters

### Claude / Claude Code
Save this skill into your Claude skills directory:
```bash
mkdir -p ~/.claude/skills/kinetic-text-director
cp SKILL.md template.html build.py ~/.claude/skills/kinetic-text-director/
```
Prompt: *"Use kinetic-text-director to create a 10-second vertical reel explaining the power of AI agents."*

### ChatGPT / Custom GPTs
1. Create a new Custom GPT.
2. In the **Instructions** tab, paste the contents of `SKILL.md`.
3. Upload `template.html` and `build.py` into Code Interpreter.

### Google Antigravity & Gemini CLI
Add this folder to your Antigravity plugin workspace:
```json
{
  "plugins": ["ishtiyaq8811/kinetic-text-director"]
}
```

---

## 🧪 Functional Example

```json
{
  "title": "Steve Jobs on Innovation",
  "aspectRatio": "9:16",
  "theme": "sunset-glow",
  "phrases": [
    {
      "text": "Innovation distinguishes between a leader and a follower.",
      "durationMs": 3000,
      "animation": "pop-in",
      "highlightWords": ["Innovation", "leader"],
      "subtitle": "Steve Jobs (1997)"
    },
    {
      "text": "Stay hungry. Stay foolish.",
      "durationMs": 2500,
      "animation": "glow-burst",
      "highlightWords": ["hungry", "foolish"],
      "subtitle": "Stanford Commencement Address"
    }
  ]
}
```
Run compiler:
```bash
python build.py examples/quote-reel.json
```
Produces `quote-reel.reel.html` ready to view at 60fps in any browser.