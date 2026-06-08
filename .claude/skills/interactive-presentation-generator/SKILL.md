---
name: interactive-presentation-generator
description: Generate interactive HTML presentations with intelligent narrative structure, modular slides, visual design guidance, and oral delivery scripts. Use this skill whenever you need to create presentations for corporate pitches, government reports (CGE-GO style), academic talks, startup demos, or any formal presentation context. The skill automatically selects the best narrative framework based on your topic, generates reusable slide blocks you can customize, provides detailed visual instructions (layout, colors, imagery suggestions, pacing), and produces both an interactive HTML file and speaker notes with timing and delivery directions.
compatibility:
  tools:
    - Write
    - Read
  optional: 
    - Knowledge of your audience and presentation context
---

# Interactive Presentation Generator

## When to Use This Skill

You should use this skill when you need to **create any formal presentation** and want:

1. **Narrative intelligence** — The skill analyzes your topic and automatically chooses the best story structure (Hero's Journey for innovation, Problem-Solution for corporate pitches, Case Study for government reports, etc.)
2. **Modular, customizable slides** — Each slide block (Hook, Context, Data, Solution, Case Study, CTA) can be reordered, merged, or split without breaking the flow
3. **Professional visual design** — Detailed instructions for every slide: layout grid, color palette, imagery suggestions, typography, animation timing
4. **Oral delivery guidance** — Speaker notes with exact timing, pauses, emphasis marks, hand gesture suggestions, and pacing cues
5. **Institutional style compliance** — Built-in support for CGE-GO (Goiás government), corporate, or academic design systems
6. **Interactive output** — Single HTML file with navigation, speaker mode, timer, and printable speaker notes

**Typical use cases:**
- Corporate pitch deck for investor meeting
- Government report (CGE-GO institutional style)
- Academic research presentation
- Product launch announcement
- Policy briefing
- Training module or workshop slide deck
- Any formal presentation where storytelling matters

---

## How It Works: The Three-Phase Generation

### Phase 1: Narrative Framework Selection

You provide:
- **Topic** — What are you presenting about? (e.g., "new budget allocation system")
- **Audience** — Who's watching? (e.g., "government officials, 20 people")
- **Objective** — What should they feel/believe/do? (e.g., "adopt the new system confidently")
- **Style** — Institutional (CGE-GO), corporate, academic, or startup?
- **Duration** — How long? (e.g., 15 minutes = 10-12 slides)

The skill analyzes these inputs and selects from 5 core narrative frameworks:

| Framework | Best For | Structure |
|-----------|----------|-----------|
| **Hero's Journey** | Innovation, transformation, change management | Challenge → Struggle → Revelation → Triumph |
| **Problem-Solution** | Business pitches, sales, process improvement | Pain → Root Cause → Your Solution → Benefits → CTA |
| **Case Study** | Proof, credibility, government reports | Background → Approach → Results → Lessons → Application |
| **Data Story** | Analytics, research, policy insights | Question → Hypothesis → Evidence → Conclusion → Action |
| **Chronological** | Training, historical overview, process flows | Past → Present → Future with key decision points |

### Phase 2: Modular Block Generation

The skill generates **reusable slide blocks** in this sequence:

1. **Opening Hook** (1 slide) — Grab attention with a provocative question, surprising stat, or personal story
2. **Context & Background** (1-2 slides) — Set the stage, establish stakes
3. **Data & Evidence** (2-3 slides) — Charts, metrics, proof points
4. **Your Solution/Insight** (1-2 slides) — The core value proposition
5. **Case Study or Example** (1-2 slides) — Real-world application
6. **Benefits & Impact** (1 slide) — "Here's what improves"
7. **Call to Action** (1 slide) — Next steps, commitment, decision needed

**Each block includes:**
- **Slide content** — Headline, bullet points, key message
- **Visual layout** — Grid position, white space, element placement
- **Design specs** — Colors, fonts, imagery (e.g., "Use a photo of people collaborating, 60% opacity, right side")
- **Speaker notes** — What to say, emphasis, timing (e.g., "Pause 3 seconds after the stat, let it sink in")
- **Animation/interaction** — Click-to-reveal, fade-in timing, navigation cues

### Phase 3: Output Generation

**Output 1: Interactive HTML File**
- Single `.html` file (no external dependencies, copy-paste shareable)
- Inline CSS with responsive design (works on desktop, mobile, projector)
- Slide navigation with arrow keys or buttons
- Speaker mode (timer, current slide + next slide preview, notes sidebar)
- Printable speaker notes (one-page per slide)
- Dark mode toggle for presenter comfort

**Output 2: Speaker Notes Document**
- Text file with full delivery script
- Timing breakdown (time per slide, cumulative time)
- Pacing annotations ("slow down", "energetic", "pause 3 sec")
- Gesture cues ("point to chart on screen", "make eye contact", "walk to the left")
- Pronunciation guide for difficult terms
- Audience interaction cues ("Ask hands: who's experienced this?")

---

## How to Use: Step-by-Step

### Step 1: Describe Your Presentation

Provide the skill with this information:

```
Topic: [What you're presenting about]
Audience: [Who? Size? Technical level?]
Objective: [What should they understand/feel/do?]
Duration: [How many minutes? (15min = 10-12 slides)]
Style: [CGE-GO institutional / Corporate / Academic / Startup]
Key Points: [2-3 main messages you must convey]
Constraints: [Any required data, branding, format limits?]
```

### Step 2: Skill Generates Draft Presentation

The skill will:
1. Select the best narrative framework for your topic
2. Generate slide-by-slide outline with titles, bullets, visual cues
3. Write speaker notes with timing and delivery guidance
4. Create HTML preview with inline styling
5. Return both files for your review

### Step 3: Customize & Iterate

You can ask the skill to:
- **Reorder slides** — "Move the case study to after the data, before benefits"
- **Expand or condense** — "Add a second data slide about budget impact"
- **Change tone** — "Make this more energetic/formal/conversational"
- **Add visuals** — "Suggest 3 chart types for the financial data"
- **Adjust timing** — "This is running long, trim speaker notes to 2 minutes per slide"

### Step 4: Export & Present

Download the HTML and speaker notes. Open HTML in your browser:
- Press `S` to enter speaker mode (timer, notes, preview)
- Use arrow keys to navigate
- Print speaker notes as PDF for reference

---

## Design System Support

### CGE-GO Institutional Style (Goiás Government)

If you select `Style: CGE-GO`, the skill applies:

**Color Palette:**
- Primary: Azul Goiás (#003A7E)
- Success: Verde Êxito (#1CAD47)
- Alert: Amarelo Alerta (#F7B600)
- Critical: Vermelho Crítico (#C80000)
- Neutral: Cinza Claro (#E8E8E8), Cinza Escuro (#4A4A4A)

**Typography:**
- Titles: Segoe UI Bold, 24-32px
- Subtitles: Segoe UI Semibold, 16-20px
- Body: Segoe UI Regular, 12-14px
- Metrics/KPIs: Bold, 28-48px

**Tone & Vocabulary:**
- Formal, institutional language
- Mandatory terms: SGOe, LAI, LGPD, manifestação, resolutividade, transparência
- Emphasis on governance, compliance, citizen impact

### Corporate & Startup Styles

For corporate/startup, the skill generates:
- Modern, minimal design (lots of white space)
- Sans-serif fonts (Inter, Roboto)
- Brand color integration
- Data visualization emphasis
- Energetic pacing, shorter notes

For academic:
- Serif titles (Georgia, Cambria)
- Detailed citations and references
- Evidence-first pacing
- Conservative color palette
- Longer speaker notes with context

---

## Narrative Framework Examples

### Example 1: Problem-Solution (Corporate Pitch)

**Topic:** "Why adopt our inventory management system"  
**Slides:**
1. Hook: "How much revenue are you leaving on the table right now?" (stat: 15% stock-outs)
2. Problem: "Manual tracking causes delays, errors, lost sales"
3. Root cause: "Spreadsheets can't scale, no real-time visibility"
4. Your solution: "AI-powered forecasting, real-time stock levels"
5. Case study: "Company X reduced stockouts 80%, revenue +12%"
6. Benefits: "Save $50K/year in lost sales + staff time"
7. CTA: "Schedule a 20-minute demo this week"

### Example 2: Case Study (Government Report)

**Topic:** "New budget allocation system for SGOe agencies"  
**Slides:**
1. Hook: "Agencies wasted 6 months on manual budget requests"
2. Context: "SGOe's current system: decentralized, paper-based, opaque"
3. Approach: "We built a centralized platform with LAI compliance, audit trail"
4. Results: "Allocation time: 6 months → 2 weeks, 100% LGPD compliant"
5. Implementation: "Phase 1 (3 agencies) → Phase 2 (all SGOe)"
6. Benefits: "Transparency, speed, accountability"
7. CTA: "Agencies: register for onboarding next month"

### Example 3: Data Story (Analytics/Research)

**Topic:** "Climate impact of policy X in Goiás"  
**Slides:**
1. Hook: "If current trends continue, 20% water deficit by 2035"
2. Question: "Can policy X reduce emissions while maintaining productivity?"
3. Hypothesis: "Policy X + incentives → 30% emissions reduction"
4. Evidence: "6-month pilot in 5 municipalities: actual reduction 28%"
5. Conclusion: "Policy X works, tweaks needed for full state implementation"
6. Benefits: "Meet Paris targets, economic growth maintained"
7. CTA: "Full rollout vote: September budget session"

---

## Output Format: What You Get

### Interactive HTML File

```html
<!DOCTYPE html>
<html>
<head>
  <title>Your Presentation Title</title>
  <style>
    /* Inline CSS with responsive design */
  </style>
</head>
<body>
  <div class="slide" id="slide-1">
    <h1>Your Opening Hook</h1>
    <p>Subtitle or key stat</p>
    <div class="visual-note">
      Image: Compelling photo of [description], 60% opacity, positioned right
    </div>
  </div>
  <!-- More slides... -->
  <script>
    // Navigation, timer, speaker mode logic
  </script>
</body>
</html>
```

### Speaker Notes (Text File)

```
=== SLIDE 1: OPENING HOOK ===
Duration: 1 minute 30 seconds

What to say:
"Good morning. I want to start with a question that might surprise you. 
[PAUSE 3 SECONDS - let this sink in]
How much revenue are you leaving on the table right now?

[Gesture to slide]
Studies show that for companies like yours, stockouts account for about 
15% of potential revenue. That's...

[PAUSE, make eye contact with 3-4 people]
...significant. And it doesn't have to be this way."

Delivery notes:
- Speak slowly, let the opening question hang
- Make eye contact when you pause
- Point to the stat on screen when you mention "15%"
- Shift your weight to the right as you transition to "it doesn't have to be"

Next slide preview: A chart showing the financial impact
```

---

## Advanced Features

### Customization Options

Ask the skill to:

**Reorder narrative** — "Can you swap the case study and benefits sections?"  
**Add interactivity** — "Include audience poll: 'Have you experienced this problem?'"  
**Expand visuals** — "Generate 3 chart mockups for the data slide"  
**Multi-language** — "Generate Portuguese + English side-by-side versions"  
**Presentation mode** — "Add speaker timer for 15-minute delivery"

### Accessibility

All generated presentations include:
- ARIA labels for screen readers
- High contrast mode (dark mode toggle)
- Text alternatives for charts
- Keyboard navigation (arrow keys, space)
- Readable fonts (minimum 14px)

---

## Best Practices

1. **Keep Hook to 30 seconds** — Grab attention fast, don't spend too long on the problem
2. **Data = Visual** — Every data slide should have a chart, not just numbers
3. **Stories beat stats** — Use the case study section to make it human
4. **One idea per slide** — If you're explaining 3 things, you probably need 3 slides
5. **Speaker notes ≠ Slide text** — Slide has headline + 3 bullets; notes have your full script
6. **Pacing matters** — 1 slide per minute average; data slides can go slower (2 min)
7. **End strong** — CTA slide should be memorable and specific ("Sign up by Friday" not "Let's talk about this")

---

## Tips for Different Contexts

### Government/Institutional (CGE-GO)
- Lead with compliance and transparency
- Use official terminology (LAI, LGPD, SGOe, etc.)
- Include audit trail / accountability messaging
- Cite relevant legislation
- Use institutional color palette strictly

### Corporate/Sales Pitch
- Lead with a problem the audience feels
- Use social proof (logos of similar companies)
- Quantify the benefit in their language (revenue, time saved, cost reduction)
- Make the CTA time-bound ("This offer expires Friday")

### Academic/Research
- Lead with the research question
- Dedicate 2-3 slides to methodology
- Show limitations honestly
- End with "further research needed" or practical applications
- Use formal citation style

### Startup/Innovation
- Lead with the vision (future state)
- Use bold, energetic language
- Include founder story if relevant
- Emphasize speed and disruption
- Make CTA about joining the movement, not just signing a contract

---

## Troubleshooting

**"My presentation feels too formal for our audience"**  
→ Ask the skill to adjust tone from CGE-GO to "startup" or "conversational"

**"I'm running over time"**  
→ Ask the skill to condense speaker notes to 1 minute per slide, or remove one block

**"The narrative doesn't fit my data"**  
→ Provide more context about your data (what story does it tell?) and ask the skill to reframe

**"I want to add a slide in the middle"**  
→ Ask: "Add a slide after slide 4 about [topic], following the [framework name] structure"

**"Colors don't match my brand"**  
→ Provide your brand color codes and ask for a custom color version

---

## Example Usage in Action

**You say:**
```
Topic: Adopting a new quality assurance system for our manufacturing plant
Audience: Plant managers (15 people, mixed technical backgrounds)
Objective: Get buy-in for the QA system implementation
Duration: 12 minutes (10 slides)
Style: Corporate
Key points: (1) Current system is costing us rework, (2) New system is proven, (3) 3-month transition is painless
```

**Skill generates:**
- Draft HTML with 10 slides following Problem-Solution narrative
- Speaker notes with 1:12 per slide timing
- Visual cues for each slide (layout, chart suggestions)
- Suggested Q&A time at end

**You refine:**
"Add a slide about staff training and move it before benefits. Can you make the opening hook more personal — maybe a story from someone on the floor?"

**Skill revises:**
- Adds training slide with new narrative flow
- Rewrites opening to include employee testimonial
- Adjusts timing to still fit 12 minutes

---

This skill turns the work of presentation design into an interactive, intelligent process. It handles the structure and pacing so you can focus on your content and delivery.
