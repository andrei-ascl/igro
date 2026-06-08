#!/usr/bin/env python3
"""
Generate interactive HTML presentation from structured slide data.

Usage:
    python generate_html.py --slides slides.json --output presentation.html --style cge-go
"""

import json
import sys
from pathlib import Path
from dataclasses import dataclass, asdict
from typing import Optional, List, Dict


@dataclass
class Slide:
    """Single slide in presentation."""
    id: int
    title: str
    subtitle: Optional[str] = None
    content: List[str] = None  # Bullet points
    speaker_notes: str = ""
    duration_seconds: int = 60
    visual_guidance: str = ""
    style: str = "default"

    def __post_init__(self):
        if self.content is None:
            self.content = []


@dataclass
class Presentation:
    """Complete presentation metadata."""
    title: str
    topic: str
    audience: str
    objective: str
    duration_minutes: int
    narrative_framework: str
    style: str  # cge-go, corporate, academic, startup
    slides: List[Slide] = None

    def __post_init__(self):
        if self.slides is None:
            self.slides = []


# Color schemes
COLOR_SCHEMES = {
    "cge-go": {
        "primary": "#003A7E",
        "success": "#1CAD47",
        "alert": "#F7B600",
        "critical": "#C80000",
        "neutral_light": "#E8E8E8",
        "neutral_dark": "#4A4A4A",
        "white": "#FFFFFF",
        "black": "#000000",
        "font_family": "'Segoe UI', Tahoma, Geneva, Verdana, sans-serif",
    },
    "corporate": {
        "primary": "#0066CC",
        "accent": "#FF6B35",
        "success": "#00A86B",
        "neutral_light": "#F5F5F5",
        "neutral_dark": "#2C3E50",
        "white": "#FFFFFF",
        "font_family": "'Inter', 'Helvetica Neue', sans-serif",
    },
    "academic": {
        "primary": "#1F4788",
        "accent": "#8B4513",
        "neutral_light": "#F9F9F9",
        "neutral_dark": "#1A1A1A",
        "white": "#FFFFFF",
        "font_family": "'Georgia', 'Times New Roman', serif",
    },
    "startup": {
        "primary": "#6C5CE7",
        "accent": "#00B894",
        "alert": "#FF7675",
        "neutral_light": "#F0F0F0",
        "neutral_dark": "#2D3436",
        "white": "#FFFFFF",
        "font_family": "'Poppins', 'Roboto', sans-serif",
    },
}


def get_color_scheme(style: str) -> Dict[str, str]:
    """Get color scheme for a given style."""
    return COLOR_SCHEMES.get(style, COLOR_SCHEMES["corporate"])


def generate_slide_html(slide: Slide, colors: Dict[str, str], slide_number: int, total_slides: int) -> str:
    """Generate HTML for a single slide."""
    bullets = "".join(
        f'<li class="slide-bullet">{bullet}</li>'
        for bullet in slide.content
    )

    visual_note = ""
    if slide.visual_guidance:
        visual_note = f'''
        <div class="visual-guidance">
            <strong>Visual Guidance:</strong> {slide.visual_guidance}
        </div>
        '''

    return f'''
    <div class="slide" id="slide-{slide.id}" data-slide-number="{slide_number}">
        <div class="slide-header">
            <h1 class="slide-title" style="color: {colors['primary']};">{slide.title}</h1>
            {f'<p class="slide-subtitle">{slide.subtitle}</p>' if slide.subtitle else ''}
        </div>

        <div class="slide-content">
            {f'<ul class="slide-bullets">{bullets}</ul>' if bullets else ''}
        </div>

        {visual_note}

        <div class="slide-footer">
            <span class="slide-number">{slide_number} / {total_slides}</span>
            <span class="slide-duration" data-duration="{slide.duration_seconds}">
                {slide.duration_seconds}s
            </span>
        </div>
    </div>
    '''


def generate_html(presentation: Presentation) -> str:
    """Generate complete HTML presentation."""
    colors = get_color_scheme(presentation.style)

    slides_html = "".join(
        generate_slide_html(slide, colors, i+1, len(presentation.slides))
        for i, slide in enumerate(presentation.slides)
    )

    # Calculate total duration
    total_seconds = sum(s.duration_seconds for s in presentation.slides)
    total_minutes = total_seconds // 60

    html = f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{presentation.title}</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: {colors['font_family']};
            background-color: {colors['neutral_light']};
            color: {colors['neutral_dark']};
            overflow: hidden;
        }}

        .presentation {{
            width: 100vw;
            height: 100vh;
            display: flex;
            flex-direction: column;
        }}

        .slides-container {{
            flex: 1;
            position: relative;
            background: white;
        }}

        .slide {{
            position: absolute;
            width: 100%;
            height: 100%;
            padding: 40px;
            display: none;
            flex-direction: column;
            justify-content: flex-start;
            background: linear-gradient(135deg, {colors['white']}, {colors['neutral_light']});
            opacity: 0;
            transition: opacity 0.5s ease-in-out;
        }}

        .slide.active {{
            display: flex;
            opacity: 1;
        }}

        .slide-header {{
            margin-bottom: 40px;
        }}

        .slide-title {{
            font-size: 36px;
            font-weight: 700;
            margin-bottom: 10px;
            color: {colors['primary']};
        }}

        .slide-subtitle {{
            font-size: 20px;
            font-weight: 600;
            color: {colors['neutral_dark']};
        }}

        .slide-content {{
            flex: 1;
            overflow-y: auto;
        }}

        .slide-bullets {{
            list-style-position: inside;
            font-size: 16px;
            line-height: 1.8;
        }}

        .slide-bullet {{
            margin: 15px 0;
            margin-left: 20px;
            color: {colors['neutral_dark']};
        }}

        .slide-bullet::marker {{
            color: {colors['primary']};
            font-weight: bold;
        }}

        .visual-guidance {{
            background-color: {colors['neutral_light']};
            border-left: 4px solid {colors.get('alert', colors['primary'])};
            padding: 15px;
            margin: 20px 0;
            border-radius: 4px;
            font-size: 14px;
            color: {colors['neutral_dark']};
        }}

        .slide-footer {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-top: 30px;
            padding-top: 20px;
            border-top: 1px solid {colors['neutral_light']};
            font-size: 12px;
            color: {colors['neutral_dark']};
        }}

        .slide-number {{
            font-weight: 600;
        }}

        .slide-duration {{
            background-color: {colors['primary']};
            color: white;
            padding: 4px 10px;
            border-radius: 3px;
            font-size: 11px;
        }}

        .controls {{
            background-color: {colors['primary']};
            color: white;
            padding: 15px 40px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}

        .controls button {{
            background-color: {colors.get('accent', colors['primary'])};
            color: white;
            border: none;
            padding: 8px 20px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 14px;
            transition: opacity 0.3s;
        }}

        .controls button:hover {{
            opacity: 0.9;
        }}

        .progress-bar {{
            width: 100%;
            height: 4px;
            background-color: {colors['neutral_light']};
            position: relative;
        }}

        .progress-fill {{
            height: 100%;
            background-color: {colors.get('success', colors['primary'])};
            transition: width 0.3s;
        }}

        @media (max-width: 1024px) {{
            .slide {{
                padding: 20px;
            }}
            .slide-title {{
                font-size: 28px;
            }}
        }}

        @media print {{
            .controls {{
                display: none;
            }}
            .progress-bar {{
                display: none;
            }}
            .slide {{
                position: relative;
                page-break-after: always;
                display: flex !important;
                opacity: 1 !important;
            }}
        }}
    </style>
</head>
<body>
    <div class="presentation">
        <div class="progress-bar">
            <div class="progress-fill"></div>
        </div>

        <div class="slides-container" id="slides-container">
            {slides_html}
        </div>

        <div class="controls">
            <div>
                <span id="presentation-title">{presentation.title}</span>
                <span style="opacity: 0.7;">({total_minutes} min, {len(presentation.slides)} slides)</span>
            </div>
            <div>
                <button onclick="previousSlide()">← Anterior</button>
                <button onclick="toggleSpeakerMode()">Modo Apresentador</button>
                <button onclick="nextSlide()">Próximo →</button>
            </div>
        </div>
    </div>

    <script>
        let currentSlide = 0;
        let totalSlides = document.querySelectorAll('.slide').length;

        function showSlide(n) {{
            const slides = document.querySelectorAll('.slide');

            if (n >= totalSlides) {{
                currentSlide = totalSlides - 1;
            }} else if (n < 0) {{
                currentSlide = 0;
            }} else {{
                currentSlide = n;
            }}

            slides.forEach(slide => slide.classList.remove('active'));
            slides[currentSlide].classList.add('active');

            // Update progress bar
            const progress = ((currentSlide + 1) / totalSlides) * 100;
            document.querySelector('.progress-fill').style.width = progress + '%';
        }}

        function nextSlide() {{
            showSlide(currentSlide + 1);
        }}

        function previousSlide() {{
            showSlide(currentSlide - 1);
        }}

        function toggleSpeakerMode() {{
            const current = document.querySelectorAll('.slide')[currentSlide];
            const notes = current.querySelector('.speaker-notes');

            if (notes) {{
                notes.classList.toggle('active');
            }}
        }}

        // Keyboard navigation
        document.addEventListener('keydown', (e) => {{
            if (e.key === 'ArrowRight' || e.key === ' ') {{
                nextSlide();
            }} else if (e.key === 'ArrowLeft') {{
                previousSlide();
            }} else if (e.key === 's' || e.key === 'S') {{
                toggleSpeakerMode();
            }} else if (e.key === 'p' || e.key === 'P') {{
                window.print();
            }}
        }});

        // Initialize
        showSlide(0);
    </script>
</body>
</html>
'''
    return html


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: generate_html.py <slides.json> [--output output.html] [--style style]")
        sys.exit(1)

    slides_file = Path(sys.argv[1])
    output_file = Path("presentation.html")
    style = "corporate"

    # Parse arguments
    for i, arg in enumerate(sys.argv[2:]):
        if arg == "--output" and i + 3 < len(sys.argv):
            output_file = Path(sys.argv[i + 3])
        elif arg == "--style" and i + 3 < len(sys.argv):
            style = sys.argv[i + 3]

    # Load slides
    try:
        with open(slides_file) as f:
            data = json.load(f)

        # Convert to Presentation object
        presentation = Presentation(
            title=data.get("title", "Apresentação"),
            topic=data.get("topic", ""),
            audience=data.get("audience", ""),
            objective=data.get("objective", ""),
            duration_minutes=data.get("duration_minutes", 15),
            narrative_framework=data.get("framework", "Problem-Solution"),
            style=style,
            slides=[Slide(**s) for s in data.get("slides", [])]
        )

        # Generate HTML
        html = generate_html(presentation)

        # Write to file
        output_file.write_text(html, encoding="utf-8")
        print(f"✓ Presentation generated: {output_file}")
        print(f"  • Slides: {len(presentation.slides)}")
        print(f"  • Duration: {presentation.duration_minutes} minutes")
        print(f"  • Style: {style}")
        print(f"  • Framework: {presentation.narrative_framework}")

    except FileNotFoundError:
        print(f"Error: File not found: {slides_file}")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in {slides_file}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
