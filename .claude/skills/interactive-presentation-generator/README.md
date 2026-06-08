# Interactive Presentation Generator Skill

A Claude skill for generating professional, interactive HTML presentations with intelligent narrative structure, detailed visual guidance, and speaker notes with oral delivery timing.

## 📁 Folder Structure

```
interactive-presentation-generator/
├── SKILL.md                  # Main skill definition and instructions
├── README.md                 # This file
├── references/               # Reference materials and frameworks
│   ├── narrative-frameworks.md     # 5 core narrative structures
│   └── design-systems.md           # CGE-GO, Corporate, Academic, Startup styles
├── scripts/                  # Utility scripts (bundled with skill)
│   └── generate_html.py      # Python script to generate HTML from JSON
└── evals/                    # Evaluation test cases
    └── evals.json            # 5 test prompts for skill validation
```

## 🚀 Quick Start

### For Users: How to Use the Skill

1. **Invoke the skill:**
   ```
   I need to create a presentation about [topic] for [audience].
   Here's the context: [2-3 sentences about what you want to achieve]
   ```

2. **Provide details:**
   - Topic
   - Audience (who, size, technical level)
   - Duration (how long?)
   - Style (CGE-GO, Corporate, Academic, or Startup)
   - Key points you must cover
   - Any constraints (branding, format, specific data)

3. **The skill will:**
   - Select the best narrative framework
   - Generate 10-15 slides with titles and content
   - Create detailed visual guidance for each slide
   - Write speaker notes with timing and delivery directions
   - Produce an interactive HTML file
   - Return both files for download

4. **Customize as needed:**
   - Reorder slides
   - Expand or condense sections
   - Change tone or emphasis
   - Add specific visuals

### For Developers: How This Skill Works

The skill uses Claude's reasoning to:

1. **Analyze input** (topic + audience + goal)
2. **Select narrative framework** from 5 options:
   - Hero's Journey (innovation, transformation)
   - Problem-Solution (pitches, business cases)
   - Case Study (proof, credibility)
   - Data Story (research, analytics)
   - Chronological (training, roadmaps)

3. **Generate slide structure** with:
   - Intelligent slide sequencing
   - Titles and bullet points
   - Visual design specifications
   - Speaker notes with timing

4. **Apply design system** (CGE-GO, Corporate, Academic, Startup)

5. **Output**:
   - Interactive HTML (inline CSS, no dependencies)
   - Speaker notes document (text/markdown)
   - Visual guidance for each slide

## 📚 Reference Materials

### Narrative Frameworks (`references/narrative-frameworks.md`)

Five core structures the skill can use:

| Framework | Best For | Slide Count |
|-----------|----------|------------|
| Hero's Journey | Innovation, transformation | 10-15 |
| Problem-Solution | Pitches, business cases | 10-12 |
| Case Study | Proof, credibility | 12-15 |
| Data Story | Research, analytics | 12-18 |
| Chronological | Training, timelines | 15-25 |

### Design Systems (`references/design-systems.md`)

Each design system includes:
- Color palette (6-8 colors)
- Typography (fonts, sizes, weights)
- Layout and spacing guidelines
- Tone and voice
- Visual style recommendations

## 🧪 Testing the Skill

### Test Cases (`evals/evals.json`)

Five realistic scenarios to validate the skill:

1. **Corporate Pitch** - Inventory management system to plant managers (12 min)
2. **CGE-GO Report** - Budget allocation system for government agencies (15 min)
3. **Startup Pitch** - Fintech startup seeking seed funding (10 min)
4. **Academic Research** - PhD presentation on climate and crop diversity (20 min)
5. **Training Module** - Company history for new employees (30 min)

## 🛠️ Scripts

### `scripts/generate_html.py`

Utility script that converts structured slide data (JSON) into interactive HTML.

## 🎨 Design Principles

All generated presentations follow:

1. **Narrative coherence** — One idea flows logically to the next
2. **Visual hierarchy** — Clear distinction between title, content, supporting info
3. **Appropriate pacing** — Timing recommendations based on slide type
4. **Accessibility** — WCAG AA contrast, readable fonts, keyboard navigation
5. **Device compatibility** — Works on desktop, tablet, projected screen
6. **Speaker-friendly** — Notes are clear, timing is realistic, delivery cues are specific

---

**Last Updated:** 2026-05-23  
**Created for:** Interactive presentation generation with intelligent narrative structures  
**Author:** Claude Code (generated via skill-creator)
