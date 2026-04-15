# Diagram patterns reference

Detailed patterns for SVG diagrams. Load this file when building flowcharts, structural diagrams, or illustrative diagrams.

## Color ramps

9 ramps, each with 7 stops (lightest → darkest). Use the 50 stop for fills, 600 for strokes, 800-900 for text on colored fills.

| Name | 50 (fill) | 200 | 400 | 600 (stroke) | 800 (text) | 900 |
|------|-----------|-----|-----|--------------|------------|-----|
| Purple | #EEEDFE | #AFA9EC | #7F77DD | #534AB7 | #3C3489 | #26215C |
| Teal | #E1F5EE | #5DCAA5 | #1D9E75 | #0F6E56 | #085041 | #04342C |
| Coral | #FAECE7 | #F0997B | #D85A30 | #993C1D | #712B13 | #4A1B0C |
| Pink | #FBEAF0 | #ED93B1 | #D4537E | #993556 | #72243E | #4B1528 |
| Gray | #F1EFE8 | #B4B2A9 | #888780 | #5F5E5A | #444441 | #2C2C2A |
| Blue | #E6F1FB | #85B7EB | #378ADD | #185FA5 | #0C447C | #042C53 |
| Green | #EAF3DE | #97C459 | #639922 | #3B6D11 | #27500A | #173404 |
| Amber | #FAEEDA | #EF9F27 | #BA7517 | #854F0B | #633806 | #412402 |
| Red | #FCEBEB | #F09595 | #E24B4A | #A32D2D | #791F1F | #501313 |

### Light mode pattern

```
fill:   ramp-50
stroke: ramp-600, 0.5px
title:  ramp-800, 14px, font-weight 500
subtitle: ramp-600, 12px
```

### Dark mode pattern

```
fill:   ramp-800
stroke: ramp-200, 0.5px
title:  ramp-50 (lightest), 14px, font-weight 500
subtitle: ramp-200, 12px
```

### Applying dark mode in standalone HTML

```javascript
const dark = matchMedia('(prefers-color-scheme: dark)').matches;

// Example: blue node
const fill   = dark ? '#0C447C' : '#E6F1FB';
const stroke = dark ? '#85B7EB' : '#185FA5';
const title  = dark ? '#E6F1FB' : '#0C447C';
const sub    = dark ? '#85B7EB' : '#185FA5';
```

## Color assignment rules

- Color encodes **category**, not sequence. All nodes of the same type share one color.
- Use 2-3 colors max per diagram. Gray for neutral/structural nodes.
- Reserve blue/green/amber/red for their semantic meanings (info/success/warning/error) unless in an illustrative diagram where they map to physical properties.
- Prefer purple, teal, coral, pink for general categories.

## Flowchart patterns

### Single-line node (44px)

```svg
<g>
  <rect x="100" y="20" width="180" height="44" rx="8"
        fill="#E6F1FB" stroke="#185FA5" stroke-width="0.5"/>
  <text x="190" y="42" text-anchor="middle" dominant-baseline="central"
        font-family="system-ui" font-size="14" font-weight="500"
        fill="#0C447C">Process step</text>
</g>
```

### Two-line node (56px)

```svg
<g>
  <rect x="100" y="20" width="200" height="56" rx="8"
        fill="#E1F5EE" stroke="#0F6E56" stroke-width="0.5"/>
  <text x="200" y="38" text-anchor="middle" dominant-baseline="central"
        font-family="system-ui" font-size="14" font-weight="500"
        fill="#085041">Auth service</text>
  <text x="200" y="54" text-anchor="middle" dominant-baseline="central"
        font-family="system-ui" font-size="12"
        fill="#0F6E56">Validates tokens</text>
</g>
```

### Neutral node (gray)

```svg
<g>
  <rect x="100" y="20" width="160" height="44" rx="8"
        fill="#F1EFE8" stroke="#5F5E5A" stroke-width="0.5"/>
  <text x="180" y="42" text-anchor="middle" dominant-baseline="central"
        font-family="system-ui" font-size="14" font-weight="500"
        fill="#444441">Start</text>
</g>
```

### Decision diamond (as rounded rect with question)

Use a rounded rect with a question label instead of a true diamond (diamonds are hard to size for text):

```svg
<g>
  <rect x="100" y="20" width="200" height="44" rx="22"
        fill="#FAEEDA" stroke="#854F0B" stroke-width="0.5"/>
  <text x="200" y="42" text-anchor="middle" dominant-baseline="central"
        font-family="system-ui" font-size="14" font-weight="500"
        fill="#633806">Valid token?</text>
</g>
```

### Straight connector

```svg
<line x1="200" y1="76" x2="200" y2="120"
      stroke="#888" stroke-width="1.5" fill="none"
      marker-end="url(#arrow)"/>
```

### L-bend connector (avoid crossing boxes)

```svg
<path d="M200 76 L200 98 L400 98 L400 120"
      stroke="#888" stroke-width="1.5" fill="none"
      marker-end="url(#arrow)"/>
```

### Arrow label

Place labels in clear space near arrows, not on top of them:

```svg
<text x="210" y="95" font-family="system-ui" font-size="12"
      fill="#888">success</text>
```

## Structural diagram patterns

### Outer container

```svg
<rect x="40" y="30" width="600" height="300" rx="20"
      fill="#EAF3DE" stroke="#3B6D11" stroke-width="0.5"/>
<text x="340" y="58" text-anchor="middle"
      font-family="system-ui" font-size="14" font-weight="500"
      fill="#27500A">System name</text>
```

### Inner region

```svg
<rect x="70" y="80" width="240" height="180" rx="12"
      fill="#E1F5EE" stroke="#0F6E56" stroke-width="0.5"/>
<text x="190" y="108" text-anchor="middle"
      font-family="system-ui" font-size="14" font-weight="500"
      fill="#085041">Subsystem A</text>
<text x="190" y="126" text-anchor="middle"
      font-family="system-ui" font-size="12"
      fill="#0F6E56">Handles requests</text>
```

Use different color ramps for parent vs child containers to maintain visual hierarchy.

## Illustrative diagram guidelines

- Shapes are freeform: `<path>`, `<ellipse>`, `<circle>`, `<polygon>`.
- Layout follows the subject's geometry, not a grid.
- Color encodes intensity: warm = active/hot, cool = calm/cold, gray = inert.
- Layering and overlap encouraged for shapes, but text must never overlap shapes.
- Leader lines for labels: 0.5px dashed stroke from label to annotated part.
- One gradient per diagram maximum (only for showing continuous physical property).
- Keep shapes simple: if a `<path>` needs more than ~6 segments, simplify.

### Leader line pattern

```svg
<line x1="380" y1="120" x2="480" y2="80"
      stroke="#888" stroke-width="0.5" stroke-dasharray="3 3"/>
<circle cx="380" cy="120" r="2" fill="#888"/>
<text x="486" y="84" font-family="system-ui" font-size="12"
      fill="#888">Component name</text>
```

## Layout computation

Before placing boxes, always compute:

1. **Box width** = `max(title_chars × 8, subtitle_chars × 7) + 48`
2. **Row width** = `sum(box_widths) + gaps × (n-1)`, where gap ≥ 20px
3. Verify row width ≤ 600 (safe area is x=40 to x=640)
4. **ViewBox height** = bottom of lowest element + 40px

If a row doesn't fit, either shrink boxes, remove subtitles, or split into two rows.

## Mermaid.js for ERDs

For database schemas, use mermaid.js instead of hand-drawn SVG:

```html
<div id="erd"></div>
<script type="module">
import mermaid from 'https://esm.sh/mermaid@11/dist/mermaid.esm.min.mjs';
const dark = matchMedia('(prefers-color-scheme: dark)').matches;
mermaid.initialize({
  startOnLoad: false,
  theme: 'base',
  themeVariables: {
    darkMode: dark,
    fontSize: '13px',
    lineColor: dark ? '#9c9a92' : '#73726c',
    textColor: dark ? '#c2c0b6' : '#3d3d3a',
  },
});
const { svg } = await mermaid.render('erd-svg', `erDiagram
  USERS ||--o{ POSTS : writes
  POSTS ||--o{ COMMENTS : has
  USERS {
    uuid id PK
    string email
  }`);
document.getElementById('erd').innerHTML = svg;
</script>
```
