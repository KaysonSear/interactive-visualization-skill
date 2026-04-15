# Interactive patterns reference

Patterns for interactive explainers, comparison grids, and dashboards. Load this when building HTML-based interactive visualizations.

## Controls

### Range slider with live readout

```html
<div style="display: flex; align-items: center; gap: 12px; margin-bottom: 1rem;">
  <label style="font-size: 14px; color: #666; min-width: 80px;">Interest rate</label>
  <input type="range" min="1" max="20" value="7" step="0.5" id="rate"
         style="flex: 1;" oninput="update()">
  <span id="rate-val" style="font-size: 14px; font-weight: 500; min-width: 40px;
        text-align: right;">7.0%</span>
</div>
```

Always set `step` to prevent float artifacts. Round display values:

```javascript
function update() {
  const rate = parseFloat(document.getElementById('rate').value);
  document.getElementById('rate-val').textContent = rate.toFixed(1) + '%';
}
```

### Toggle switch

```html
<label style="display: flex; align-items: center; gap: 8px; cursor: pointer;
              user-select: none; font-size: 14px; color: #666;">
  <div style="position: relative; width: 36px; height: 20px;">
    <input type="checkbox" id="toggle" checked onchange="onToggle(this.checked)"
           style="position: absolute; opacity: 0; width: 100%; height: 100%;
                  cursor: pointer; margin: 0;">
    <div id="track" style="width: 36px; height: 20px; border-radius: 10px;
         background: #378ADD; transition: background 0.2s;"></div>
    <div id="thumb" style="position: absolute; top: 2px; left: 18px; width: 16px;
         height: 16px; background: #fff; border-radius: 50%;
         transition: left 0.2s; pointer-events: none;"></div>
  </div>
  Enable feature
</label>
<script>
function onToggle(on) {
  document.getElementById('track').style.background = on ? '#378ADD' : '#ccc';
  document.getElementById('thumb').style.left = on ? '18px' : '2px';
}
</script>
```

### Button group (select one)

```html
<div style="display: flex; gap: 4px;">
  <button onclick="selectOption('monthly')" id="btn-monthly"
          style="padding: 6px 14px; border: 0.5px solid #ccc; border-radius: 6px;
                 background: #378ADD; color: #fff; cursor: pointer; font-size: 13px;">
    Monthly
  </button>
  <button onclick="selectOption('yearly')" id="btn-yearly"
          style="padding: 6px 14px; border: 0.5px solid #ccc; border-radius: 6px;
                 background: transparent; color: inherit; cursor: pointer; font-size: 13px;">
    Yearly
  </button>
</div>
<script>
function selectOption(opt) {
  document.querySelectorAll('[id^="btn-"]').forEach(b => {
    b.style.background = 'transparent';
    b.style.color = 'inherit';
  });
  const active = document.getElementById('btn-' + opt);
  active.style.background = '#378ADD';
  active.style.color = '#fff';
  // Update visualization...
}
</script>
```

## Comparison card grid

```html
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 16px;">

  <!-- Regular option -->
  <div style="background: #fff; border: 0.5px solid #ddd; border-radius: 12px;
              padding: 1.25rem;">
    <h3 style="font-size: 16px; font-weight: 500; margin-bottom: 4px;">Basic</h3>
    <p style="font-size: 24px; font-weight: 500; margin-bottom: 12px;">$9/mo</p>
    <ul style="list-style: none; padding: 0; font-size: 13px; color: #666;">
      <li style="padding: 4px 0;">10 projects</li>
      <li style="padding: 4px 0;">1 GB storage</li>
    </ul>
  </div>

  <!-- Featured / recommended option -->
  <div style="background: #fff; border: 2px solid #378ADD; border-radius: 12px;
              padding: 1.25rem; position: relative;">
    <span style="position: absolute; top: -10px; left: 16px;
                 background: #E6F1FB; color: #0C447C;
                 font-size: 11px; font-weight: 500; padding: 2px 10px;
                 border-radius: 6px;">Recommended</span>
    <h3 style="font-size: 16px; font-weight: 500; margin-bottom: 4px;">Pro</h3>
    <p style="font-size: 24px; font-weight: 500; margin-bottom: 12px;">$29/mo</p>
    <ul style="list-style: none; padding: 0; font-size: 13px; color: #666;">
      <li style="padding: 4px 0;">Unlimited projects</li>
      <li style="padding: 4px 0;">50 GB storage</li>
    </ul>
  </div>
</div>
```

**Dark mode adjustments:**

```css
@media (prefers-color-scheme: dark) {
  .card { background: #2a2a2a; border-color: rgba(255,255,255,0.1); }
  .card.featured { border-color: #378ADD; }
  .badge { background: #0C447C; color: #E6F1FB; }
}
```

## Metric card

```html
<div style="background: #f5f5f5; border-radius: 8px; padding: 1rem;">
  <div style="font-size: 13px; color: #888; margin-bottom: 4px;">Total users</div>
  <div style="font-size: 24px; font-weight: 500;">12,847</div>
  <div style="font-size: 12px; color: #1D9E75; margin-top: 4px;">↑ 12.4%</div>
</div>
```

Use in a grid for dashboards:

```html
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
            gap: 12px; margin-bottom: 1.5rem;">
  <!-- 2-4 metric cards -->
</div>
```

## Animation (CSS only)

Permitted for illustrative interactive diagrams:

```css
@keyframes flow {
  to { stroke-dashoffset: -20; }
}

@media (prefers-reduced-motion: no-preference) {
  .flow-line {
    stroke-dasharray: 5 5;
    animation: flow 1.6s linear infinite;
  }
}
```

Rules:
- Only animate `transform` and `opacity` (plus `stroke-dashoffset` for flow effects).
- Wrap in `@media (prefers-reduced-motion: no-preference)`.
- Keep loops under 2 seconds.
- Animations show mechanism, not decoration.

## Complete interactive explainer template

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Compound Interest Calculator</title>
<style>
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    font-family: system-ui, -apple-system, sans-serif;
    color: #1a1a1a; background: #fff; padding: 2rem; line-height: 1.6;
  }
  @media (prefers-color-scheme: dark) {
    body { background: #1a1a1a; color: #e8e8e8; }
    .metric-card { background: #2a2a2a !important; }
    .label { color: #999 !important; }
  }
  .controls { margin-bottom: 1.5rem; }
  .control-row {
    display: flex; align-items: center; gap: 12px; margin-bottom: 0.75rem;
  }
  .label { font-size: 14px; color: #666; min-width: 100px; }
  .value { font-size: 14px; font-weight: 500; min-width: 48px; text-align: right; }
  .result { font-size: 28px; font-weight: 500; margin-bottom: 1.5rem; }
  .chart-wrap { position: relative; width: 100%; height: 300px; }
  .metric-card {
    background: #f5f5f5; border-radius: 8px; padding: 1rem;
  }
</style>
</head>
<body>
  <div class="controls">
    <div class="control-row">
      <span class="label">Principal</span>
      <input type="range" min="1000" max="100000" value="10000" step="1000"
             id="principal" style="flex:1" oninput="update()">
      <span class="value" id="p-val">$10,000</span>
    </div>
    <div class="control-row">
      <span class="label">Rate (%)</span>
      <input type="range" min="1" max="20" value="7" step="0.5"
             id="rate" style="flex:1" oninput="update()">
      <span class="value" id="r-val">7.0%</span>
    </div>
    <div class="control-row">
      <span class="label">Years</span>
      <input type="range" min="1" max="40" value="20" step="1"
             id="years" style="flex:1" oninput="update()">
      <span class="value" id="y-val">20</span>
    </div>
  </div>

  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;
              margin-bottom: 1.5rem;">
    <div class="metric-card">
      <div style="font-size: 13px; color: #888;">Final value</div>
      <div class="result" id="result">$38,697</div>
    </div>
    <div class="metric-card">
      <div style="font-size: 13px; color: #888;">Interest earned</div>
      <div class="result" id="interest" style="color: #1D9E75;">$28,697</div>
    </div>
  </div>

  <div class="chart-wrap">
    <canvas id="chart" role="img"
            aria-label="Growth of investment over time">
      Investment growth chart
    </canvas>
  </div>

  <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.js"></script>
  <script>
    const dark = matchMedia('(prefers-color-scheme: dark)').matches;
    let chart;

    function update() {
      const P = +document.getElementById('principal').value;
      const r = +document.getElementById('rate').value / 100;
      const n = +document.getElementById('years').value;

      document.getElementById('p-val').textContent = '$' + P.toLocaleString();
      document.getElementById('r-val').textContent = (r * 100).toFixed(1) + '%';
      document.getElementById('y-val').textContent = n;

      const labels = [];
      const principal = [];
      const compound = [];

      for (let y = 0; y <= n; y++) {
        labels.push('Year ' + y);
        principal.push(P);
        compound.push(Math.round(P * Math.pow(1 + r, y)));
      }

      const final = compound[compound.length - 1];
      document.getElementById('result').textContent = '$' + final.toLocaleString();
      document.getElementById('interest').textContent =
        '$' + (final - P).toLocaleString();

      if (chart) chart.destroy();
      chart = new Chart(document.getElementById('chart'), {
        type: 'line',
        data: {
          labels,
          datasets: [
            {
              label: 'With compound interest',
              data: compound,
              borderColor: '#378ADD',
              backgroundColor: 'rgba(55,138,221,0.1)',
              fill: true,
              tension: 0.3,
              pointRadius: 0
            },
            {
              label: 'Principal only',
              data: principal,
              borderColor: '#888',
              borderDash: [5, 5],
              fill: false,
              pointRadius: 0
            }
          ]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: { legend: { display: false } },
          scales: {
            y: {
              ticks: {
                callback: v => '$' + (v/1000).toFixed(0) + 'k',
                color: dark ? '#999' : '#666'
              },
              grid: { color: dark ? 'rgba(255,255,255,0.08)' : 'rgba(0,0,0,0.06)' }
            },
            x: {
              ticks: { color: dark ? '#999' : '#666', maxTicksLimit: 10 },
              grid: { display: false }
            }
          }
        }
      });
    }

    update();
  </script>
</body>
</html>
```
