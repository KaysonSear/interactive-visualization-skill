# Interactive Visualization Skill

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Version: 1.0](https://img.shields.io/badge/Version-1.0-green.svg)]()

A Claude Code skill for creating production-quality interactive charts, diagrams, and data visualizations as self-contained HTML files.

## ✨ Features

- **Charts** - Bar, line, pie, doughnut, radar, scatter, bubble charts using Chart.js
- **Maps** - Choropleth maps using D3 and TopoJSON
- **Diagrams** - Flowcharts, architecture diagrams, and structural diagrams using SVG
- **Interactive Explainers** - Dynamic visualizations with sliders and controls
- **Dashboards** - Metric cards and KPI displays
- **Dark Mode** - All visualizations automatically adapt to light/dark themes
- **Self-Contained** - Single HTML file output, no external dependencies

## 🚀 Quick Start

This skill helps Claude Code generate interactive visualizations based on your needs:

| What you want | What you get |
|--------------|--------------|
| "Chart this data" | Interactive Chart.js visualization |
| "Show on a map" | D3 choropleth map |
| "Create a flowchart" | SVG diagram with arrows and nodes |
| "How does X work?" | Interactive explainer with controls |
| "Compare these options" | Card grid layout |
| "Build a dashboard" | Metric cards + charts |

## 🎯 给你的Agent使用

复制以下提示词发送给你的Agent，即可快速安装并使用本Skill：

```
请安装并使用 interactive-visualization skill：

npx skills install KaysonSear/interactive-visualization-skill

然后帮我创建一个交互式数据可视化。
```

或者更详细的版本：

```
请安装 KaysonSear/interactive-visualization-skill 这个skill：

npx skills install KaysonSear/interactive-visualization-skill

安装完成后，请使用这个skill帮我：[描述你的需求，例如"创建一个展示2024年月度销售额的柱状图"]
```

## 📊 Supported Visualizations

### Chart.js Charts
- Bar & Horizontal Bar
- Line & Area
- Pie & Doughnut
- Radar & Polar Area
- Scatter & Bubble

### D3 Maps
- US States choropleth
- World countries map
- Country subdivisions

### SVG Diagrams
- Flowcharts with directional arrows
- Architecture diagrams
- Structural diagrams
- Illustrative diagrams

### Interactive Components
- Sliders and controls
- Real-time updating charts
- Comparison card grids
- Metric dashboards

## 🛠️ Technical Stack

- **Chart.js 4.4.1** - Canvas-based charts
- **D3 7.8.5** - Data-driven maps and visualizations
- **TopoJSON** - Geographic topology
- **Vanilla HTML/CSS/JS** - No build step required

### CDN Sources
All libraries load from trusted CDNs:
- `cdnjs.cloudflare.com`
- `cdn.jsdelivr.net`
- `esm.sh`
- `unpkg.com`

## 📁 Repository Structure

```
interactive-visualization/
├── SKILL.md                      # Main skill documentation
├── README.md                     # This file
├── assets/
│   └── template.html             # HTML scaffold template
├── references/
│   ├── chart-patterns.md         # Chart.js patterns & best practices
│   ├── diagram-patterns.md       # SVG diagram patterns
│   └── interactive-patterns.md   # Interactive explainer patterns
└── scripts/
    └── validate.py               # Validation script
```

## 💡 Usage Example

When using Claude Code with this skill, simply ask:

```
"Create a bar chart showing Q1-Q4 revenue data"
"Show me a flowchart of the user login process"
"Build an interactive dashboard for sales metrics"
```

Claude will generate a self-contained HTML file with your visualization, ready to open in any browser.

## 🎨 Design Principles

- **Single File** - Every visualization is one self-contained HTML file
- **Responsive** - Adapts to different screen sizes
- **Accessible** - Proper ARIA labels, roles, and color contrast
- **Dark Mode** - Automatic theme detection and adaptation
- **Clean** - Minimal, professional styling

## 📄 License

Apache-2.0 - See [SKILL.md](interactive-visualization/SKILL.md) for full details.

---

Created by Anthropic for Claude Code
