# Design Systems for Presentations

## Design System 1: CGE-GO (Goiás Government)

**When to use:** Government reports, policy briefings, institutional presentations, SGOe agencies

### Color Palette
```css
--primary: #003A7E;         /* Azul Goiás - strong, institutional */
--success: #1CAD47;         /* Verde Êxito - positive outcomes */
--alert: #F7B600;           /* Amarelo Alerta - warnings, attention */
--critical: #C80000;        /* Vermelho Crítico - critical issues */
--neutral-light: #E8E8E8;   /* Cinza Claro - backgrounds, borders */
--neutral-dark: #4A4A4A;    /* Cinza Escuro - text, strong elements */
--white: #FFFFFF;
--black: #000000;
```

### Typography
```css
--font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;

/* Heading 1: Titles */
font-family: "Segoe UI", sans-serif;
font-weight: 700;     /* Bold */
font-size: 28-32px;
line-height: 1.2;
color: #003A7E;       /* Azul Goiás */

/* Body Text */
font-weight: 400;     /* Regular */
font-size: 14px;
line-height: 1.6;
color: #4A4A4A;
```

### Mandatory Vocabulary
- **SGOe**, **LAI**, **LGPD**, **Manifestação**, **Resolutividade**, **Transparência**

### Tone & Voice
- Formal, institutional
- Fact-based, evidence-driven
- Emphasis on governance, accountability, citizen benefit

---

## Design System 2: Corporate (Business)

**When to use:** Business pitches, investor decks, corporate presentations, product launches

### Color Palette
```css
--primary: #0066CC;         /* Trust blue */
--accent: #FF6B35;          /* Energy orange */
--success: #00A86B;         /* Professional green */
--neutral-light: #F5F5F5;   /* Clean white-gray */
--neutral-dark: #2C3E50;    /* Strong dark */
```

### Tone & Voice
- Confident, direct
- Results-focused
- Fast-paced

---

## Design System 3: Academic (Research)

**When to use:** University presentations, research findings, scholarly conferences, thesis defenses

### Color Palette
```css
--primary: #1F4788;         /* Academic blue */
--accent: #8B4513;          /* Warm brown (heritage) */
--neutral-light: #F9F9F9;   /* Soft white */
--neutral-dark: #1A1A1A;    /* Deep black */
```

### Tone & Voice
- Rigorous, academic
- Cite sources
- Acknowledge limitations

---

## Design System 4: Startup (Innovation)

**When to use:** Pitch decks, product demos, founder pitches, innovation workshops

### Color Palette
```css
--primary: #6C5CE7;         /* Bold purple */
--accent: #00B894;          /* Fresh green */
--alert: #FF7675;           /* Energetic red */
--neutral-light: #F0F0F0;   /* Modern gray */
--neutral-dark: #2D3436;    /* Deep charcoal */
```

### Tone & Voice
- Energetic, optimistic
- Vision-driven ("imagine if...")
- Story-heavy, data-light

---

## Accessibility Requirements (All Systems)

Every design system must include:
- **Color contrast:** 4.5:1 for text, 3:1 for graphics (WCAG AA standard)
- **Font sizes:** Minimum 14px for body text
- **Readable fonts:** Sans-serif preferred, avoid script fonts
- **High contrast mode:** All systems support dark mode
- **Keyboard navigation:** All interactive elements accessible via keyboard
- **Alt text:** All charts and images have descriptions
