---
name: interactive-visualization
description: >-
  Create interactive charts, diagrams, and data visualizations as self-contained
  HTML files. Supports Chart.js bar/line/pie/doughnut/radar/scatter/bubble charts,
  D3 choropleth maps, SVG flowcharts, structural diagrams, illustrative diagrams,
  interactive explainers with sliders and controls, comparison card grids, and
  metric dashboards. Use when the user asks to visualize data, draw a chart,
  create a diagram, build an interactive explainer, or produce any visual output
  that benefits from interactivity or graphical presentation.
license: Apache-2.0
compatibility: Requires a browser-based rendering environment that can display HTML files with inline SVG, CSS, and JavaScript. Scripts load libraries from CDN (cdnjs.cloudflare.com, cdn.jsdelivr.net, esm.sh, unpkg.com).
metadata:
  author: anthropic
  version: "1.0"
---

# Interactive visualization skill

Create production-quality interactive visualizations as self-contained HTML files. This skill covers charts, diagrams, maps, dashboards, and interactive explainers.

## Quick decision: what to build

| User intent | Output type | Key tech |
|---|---|---|
| "chart / graph this data" | Chart.js chart | `<canvas>` + Chart.js UMD |
| "show on a map" | D3 choropleth | D3 + TopoJSON |
| "diagram / flowchart / architecture" | SVG diagram | Raw `<svg>` |
| "how does X work" (intuition) | Interactive explainer | HTML + inline SVG + controls |
| "compare options" | Card grid | HTML layout |
| "dashboard / KPIs" | Metric cards + chart | HTML + Chart.js |

## Step 1: Scaffold the HTML file

Every visualization is a **single self-contained HTML file**. Use this skeleton:

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Visualization Title</title>
<style>
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    font-family: system-ui, -apple-system, sans-serif;
    color: #1a1a1a;
    background: #ffffff;
    padding: 2rem;
    line-height: 1.6;
  }
  @media (prefers-color-scheme: dark) {
    body { background: #1a1a1a; color: #e8e8e8; }
  }
  /* Add component styles here */
</style>
</head>
<body>
  <!-- Visualization content here -->

  <!-- Load libraries BEFORE using them -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.js"></script>
  <script>
    // Your visualization logic here
  </script>
</body>
</html>
```

### Allowed CDN domains

Only these CDN origins are guaranteed to work in sandboxed environments:

- `cdnjs.cloudflare.com`
- `cdn.jsdelivr.net`
- `esm.sh`
- `unpkg.com`

Do NOT use `raw.githubusercontent.com` or other hosts.

## Step 2: Build the visualization

### Charts (Chart.js)

Use Chart.js for: bar, line, pie, doughnut, radar, scatter, bubble, polar area charts.

```html
<div style="position: relative; width: 100%; max-width: 700px; height: 350px;">
  <canvas id="myChart"></canvas>
</div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.js"></script>
<script>
new Chart(document.getElementById('myChart'), {
  type: 'bar',
  data: {
    labels: ['Q1', 'Q2', 'Q3', 'Q4'],
    datasets: [{
      label: 'Revenue ($M)',
      data: [12, 19, 8, 15],
      backgroundColor: ['#378ADD', '#1D9E75', '#EF9F27', '#D85A30']
    }]
  },
  options: {
    responsive: true,
    maintainAspectRatio: false,
    plugins: { legend: { display: false } }
  }
});
</script>
```

**Chart.js rules:**

1. Canvas cannot resolve CSS variables — use hardcoded hex colors.
2. Set height ONLY on the wrapper `<div>`, never on `<canvas>` directly.
3. Always set `responsive: true` and `maintainAspectRatio: false`.
4. For horizontal bar charts, wrapper height should be at least `(num_bars × 40) + 80` px.
5. Load UMD build via `<script src>` — sets `window.Chart` global. Follow with a plain `<script>` (no `type="module"`).
6. Round all displayed numbers: use `Math.round()`, `.toFixed(n)`, or `Intl.NumberFormat`.
7. Negative currency: `-$5M` not `$-5M` — sign before symbol.
8. Build custom HTML legends instead of the Chart.js default (see [references/chart-patterns.md](references/chart-patterns.md)).
9. For ≤12 x-axis categories, set `scales.x.ticks: { autoSkip: false, maxRotation: 45 }` to prevent label skipping.

### Dark mode for charts

Chart.js doesn't auto-adapt. Detect and apply:

```javascript
const dark = matchMedia('(prefers-color-scheme: dark)').matches;
const textColor = dark ? '#e8e8e8' : '#1a1a1a';
const gridColor = dark ? 'rgba(255,255,255,0.1)' : 'rgba(0,0,0,0.1)';
// Pass into scales.x.ticks.color, scales.y.ticks.color, scales.y.grid.color, etc.
```

### SVG diagrams

Use raw SVG for flowcharts, structural diagrams, and illustrative diagrams.

**Core setup:**

```svg
<svg width="100%" viewBox="0 0 680 H" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5"
            markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke"
            stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
    </marker>
  </defs>
  <!-- diagram content -->
</svg>
```

Replace `H` with actual content height + 40px padding. ViewBox width MUST stay 680.

**SVG text sizing** (Anthropic Sans / system-ui approximation):
- Each character at 14px ≈ 8px wide
- Each character at 12px ≈ 7px wide
- Box width = `max(title_chars × 8, subtitle_chars × 7) + 48`
- Always use `text-anchor="middle"` + `dominant-baseline="central"` for centered text

**Flowchart node pattern:**

```svg
<g>
  <rect x="100" y="20" width="180" height="44" rx="8"
        fill="#E6F1FB" stroke="#378ADD" stroke-width="0.5"/>
  <text x="190" y="42" text-anchor="middle" dominant-baseline="central"
        font-family="system-ui" font-size="14" font-weight="500"
        fill="#0C447C">Node label</text>
</g>
```

**Arrow pattern:**

```svg
<line x1="190" y1="64" x2="190" y2="100"
      stroke="#888" stroke-width="1.5" fill="none"
      marker-end="url(#arrow)"/>
```

**Key constraints:**
- Max 4-5 nodes per diagram. Split complex topics into multiple diagrams.
- 60px minimum gap between boxes, 24px padding inside boxes.
- Arrows must NEVER cross through unrelated boxes — route around with L-bends.
- Use 0.5px stroke width for borders and edges.
- All connector `<path>` elements MUST have `fill="none"`.

See [references/diagram-patterns.md](references/diagram-patterns.md) for color ramps and advanced patterns.

### Geographic maps (D3 choropleth)

```html
<div id="map" style="width: 100%; max-width: 900px;"></div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/d3/7.8.5/d3.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/topojson/3.0.2/topojson.min.js"></script>
<script>
const data = { 'California': 39, 'Texas': 30, 'New York': 19 };
const dark = matchMedia('(prefers-color-scheme: dark)').matches;
const color = d3.scaleQuantize([0, 40],
  dark ? d3.schemeBlues[5].slice().reverse() : d3.schemeBlues[5]);

const svg = d3.select('#map').append('svg')
  .attr('viewBox', '0 0 900 560').attr('width', '100%');
const path = d3.geoPath(d3.geoAlbersUsa().scale(1100).translate([450, 280]));

d3.json('https://cdn.jsdelivr.net/npm/us-atlas@3/states-10m.json').then(us => {
  svg.selectAll('path')
    .data(topojson.feature(us, us.objects.states).features)
    .join('path')
    .attr('d', path)
    .attr('stroke', dark ? 'rgba(255,255,255,.15)' : '#fff')
    .attr('fill', d => color(data[d.properties.name] ?? 0));
});
</script>
```

**Topology sources (jsdelivr only):**

| Scope | URL | Projection | Object key |
|---|---|---|---|
| US states | `us-atlas@3/states-10m.json` | `geoAlbersUsa()` | `.states` |
| World | `world-atlas@2/countries-110m.json` | `geoNaturalEarth1()` | `.countries` |
| Country subdivisions | `datamaps@0.5.10/src/js/data/{iso3}.topo.json` | varies | `.{iso3}` |

**Critical:** Never invent GeoJSON coordinates. Always fetch real topology files.

### Interactive explainers

Combine HTML controls with live-updating SVG or canvas:

```html
<div style="display: flex; align-items: center; gap: 12px; margin-bottom: 1.5rem;">
  <label style="font-size: 14px; color: #666;">Rate (%)</label>
  <input type="range" min="1" max="20" value="7" id="rate"
         style="flex: 1;" oninput="update()">
  <span id="rate-val" style="font-size: 14px; font-weight: 500; min-width: 32px;">7%</span>
</div>
<div id="result" style="font-size: 24px; font-weight: 500; margin-bottom: 2rem;">
  $19,672
</div>
<div style="position: relative; height: 300px;">
  <canvas id="chart"></canvas>
</div>
```

**Gotchas:**

- Place `<style>` blocks and inline styles BEFORE content so controls look correct during page load.
- Load `<script src="...">` for libraries BEFORE your inline `<script>`.
- Round ALL slider readouts: use `Math.round()` or `.toFixed(n)`.
- Set `step` attribute on range inputs to emit clean values.

### Metric dashboards

Use summary cards above charts:

```html
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 12px; margin-bottom: 1.5rem;">
  <div style="background: #f5f5f5; border-radius: 8px; padding: 1rem;">
    <div style="font-size: 13px; color: #666;">Total revenue</div>
    <div style="font-size: 24px; font-weight: 500;">$2.4M</div>
  </div>
  <div style="background: #f5f5f5; border-radius: 8px; padding: 1rem;">
    <div style="font-size: 13px; color: #666;">Growth</div>
    <div style="font-size: 24px; font-weight: 500; color: #1D9E75;">+18%</div>
  </div>
</div>
<!-- Chart below -->
```

## Step 3: Dark mode

Every visualization MUST support dark mode. Mental test: if the background were near-black, would every element still be readable?

**CSS approach for HTML elements:**

```css
@media (prefers-color-scheme: dark) {
  body { background: #1a1a1a; color: #e8e8e8; }
  .card { background: #2a2a2a; border-color: rgba(255,255,255,0.1); }
}
```

**JS approach for Chart.js / D3:**

```javascript
const dark = matchMedia('(prefers-color-scheme: dark)').matches;
```

## Step 4: Accessibility

1. Every `<canvas>` chart must have `role="img"`, `aria-label`, and fallback text content.
2. Every `<svg>` must have `role="img"` with `<title>` and `<desc>` as first children.
3. Never rely on color alone to distinguish data — pair with pattern, dash style, or shape.
4. No font-size below 11px.

## Gotchas

- `grid-template-columns: 1fr` has `min-width: auto` — children can overflow. Use `minmax(0, 1fr)`.
- Chart.js `type: 'bar'` with `indexAxis: 'y'` (horizontal) needs taller wrapper — at least `(bars × 40) + 80` px.
- SVG `<text>` never auto-wraps. Each line break needs `<tspan x="..." dy="1.2em">`.
- SVG paths default to `fill: black` — connectors without `fill="none"` render as solid black shapes.
- D3 topology files: country subdivisions use ISO 3166-1 alpha-3 codes (lowercase), e.g. `deu.topo.json` for Germany.
- Bubble/scatter charts: data points near axis edges get clipped. Pad scale range ~10% beyond data bounds.
- `position: fixed` does not work in sandboxed iframe environments — use normal flow with min-height.
