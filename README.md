# ⚡ Kinetic Typography Reel Director

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Platform](https://img.shields.io/badge/Platforms-Claude%20%7C%20ChatGPT%20%7C%20Antigravity%20%7C%20Gemini-blue.svg)]()
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-Zero-brightgreen.svg)]()
[![Web Audio](https://img.shields.io/badge/Audio-Procedural%20Web%20Audio-orange.svg)]()

> **Direct dynamic, punchy kinetic typography animations and 60fps social reels directly from your AI agent.**

---

## 🌟 Highlights

- **Zero External API Keys:** 100% self-contained HTML5 Canvas/SVG engine with procedural Web Audio sound synthesis.
- **Multi-Aspect Ratio:** Switch between `9:16` (Instagram Reels, YouTube Shorts, TikTok), `16:9` (Widescreen), and `1:1` (Square).
- **5 Built-in Aesthetic Themes:** `electric-neon`, `cyberpunk`, `sunset-glow`, `minimal-dark`, and `clean-paper`.
- **Dynamic Word Animations:** `pop-in` (with bounce overshoot), `slam-zoom`, `glow-burst`, `slide-up`, and `typewriter`.
- **Procedural Sound FX:** High-impact pops, whooshes, and chimes synthesized directly via the Web Audio API.
- **Multi-Platform Support:** Ready-to-use adapters for Claude Code, Google Antigravity, ChatGPT, and Google Gemini.

---

## 🚀 Quickstart

### 1. Compile an Example Reel
```bash
python build.py examples/tech-explainer.json
```
This generates `examples/tech-explainer.reel.html`. Double-click or open it in any browser to watch the 60fps kinetic reel!

### 2. Validate Spec Only
```bash
python build.py examples/quote-reel.json --validate
```

---

## 📦 Package Structure

```
kinetic-text-director/
├── SKILL.md                 # All-in-one skill specification & multi-agent instructions
├── template.html            # Standalone 60fps Canvas engine & Web Audio synthesizer
├── build.py                 # Zero-dependency Python CLI runner & compiler
├── spec.schema.json         # JSON Schema Draft-07 specification
├── README.md                # Documentation & quickstart guide
└── examples/
    ├── tech-explainer.json  # Tech explainer fixture
    └── quote-reel.json      # Quote reel fixture
```

---

## 📜 License
MIT License. Free for personal and commercial use.