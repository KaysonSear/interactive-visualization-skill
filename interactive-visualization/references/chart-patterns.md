# Chart patterns reference

Detailed patterns for Chart.js visualizations. Load this file when building charts.

## Color palette

Use these colors for data series. They are designed to be distinguishable in both light and dark mode, and for common forms of color blindness.

### Primary series colors (use in order)

```
Blue:   #378ADD
Teal:   #1D9E75
Amber:  #EF9F27
Coral:  #D85A30
Purple: #7F77DD
Pink:   #D4537E
Green:  #639922
Gray:   #888780
Red:    #E24B4A
```

### Semantic colors

```
Positive / success: #1D9E75
Negative / danger:  #E24B4A
Warning:            #EF9F27
Neutral:            #888780
Info / highlight:   #378ADD
```

## Custom HTML legend pattern

Always disable Chart.js default legend and build HTML:

```javascript
plugins: { legend: { display: false } }
```

```html
<div style="display: flex; flex-wrap: wrap; gap: 16px; margin-bottom: 8px;
            font-size: 12px; color: #666;">
  <span style="display: flex; align-items: center; gap: 4px;">
    <span style="width: 10px; height: 10px; border-radius: 2px;
                 background: #378ADD;"></span>
    Chrome 65%
  </span>
  <span style="display: flex; align-items: center; gap: 4px;">
    <span style="width: 10px; height: 10px; border-radius: 2px;
                 background: #888780;"></span>
    Safari 18%
  </span>
</div>
```

For categorical charts (pie, doughnut, single-series bar), include the value or percentage in each legend label.

## Chart type recipes

### Line chart with multiple series

```javascript
new Chart(ctx, {
  type: 'line',
  data: {
    labels: months,
    datasets: [
      {
        label: 'Revenue',
        data: revenueData,
        borderColor: '#378ADD',
        backgroundColor: 'rgba(55,138,221,0.1)',
        fill: true,
        tension: 0.3,
        pointRadius: 3,
        borderDash: []         // solid line
      },
      {
        label: 'Expenses',
        data: expenseData,
        borderColor: '#D85A30',
        backgroundColor: 'transparent',
        fill: false,
        tension: 0.3,
        pointRadius: 3,
        pointStyle: 'rect',    // different shape for accessibility
        borderDash: [5, 5]     // dashed line for accessibility
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
          callback: v => '$' + v.toLocaleString(),
          color: dark ? '#ccc' : '#666'
        },
        grid: { color: dark ? 'rgba(255,255,255,0.08)' : 'rgba(0,0,0,0.08)' }
      },
      x: {
        ticks: { color: dark ? '#ccc' : '#666' },
        grid: { display: false }
      }
    }
  }
});
```

### Doughnut / pie chart

```javascript
new Chart(ctx, {
  type: 'doughnut',
  data: {
    labels: ['Chrome', 'Safari', 'Firefox', 'Edge'],
    datasets: [{
      data: [65, 18, 10, 7],
      backgroundColor: ['#378ADD', '#1D9E75', '#EF9F27', '#D85A30'],
      borderWidth: 2,
      borderColor: dark ? '#1a1a1a' : '#ffffff'
    }]
  },
  options: {
    responsive: true,
    maintainAspectRatio: false,
    cutout: '55%',
    plugins: {
      legend: { display: false },
      tooltip: {
        callbacks: {
          label: ctx => `${ctx.label}: ${ctx.parsed}%`
        }
      }
    }
  }
});
```

### Horizontal bar chart

```javascript
new Chart(ctx, {
  type: 'bar',
  data: {
    labels: categories,
    datasets: [{
      data: values,
      backgroundColor: '#378ADD',
      borderRadius: 4,
      barPercentage: 0.7
    }]
  },
  options: {
    indexAxis: 'y',
    responsive: true,
    maintainAspectRatio: false,
    plugins: { legend: { display: false } },
    scales: {
      x: {
        grid: { color: dark ? 'rgba(255,255,255,0.08)' : 'rgba(0,0,0,0.06)' },
        ticks: { color: dark ? '#ccc' : '#666' }
      },
      y: {
        grid: { display: false },
        ticks: { color: dark ? '#ccc' : '#666' }
      }
    }
  }
});
```

**Remember:** wrapper div height must be at least `(num_bars × 40) + 80` px.

### Stacked bar chart

Add `stacked: true` to both x and y scales:

```javascript
scales: {
  x: { stacked: true },
  y: { stacked: true }
}
```

### Radar chart

```javascript
new Chart(ctx, {
  type: 'radar',
  data: {
    labels: ['Speed', 'Reliability', 'Comfort', 'Safety', 'Efficiency'],
    datasets: [{
      label: 'Model A',
      data: [85, 90, 70, 95, 80],
      borderColor: '#378ADD',
      backgroundColor: 'rgba(55,138,221,0.15)',
      pointRadius: 3
    }]
  },
  options: {
    responsive: true,
    maintainAspectRatio: false,
    scales: {
      r: {
        beginAtZero: true,
        max: 100,
        ticks: { stepSize: 20, color: dark ? '#999' : '#666' },
        grid: { color: dark ? 'rgba(255,255,255,0.1)' : 'rgba(0,0,0,0.1)' },
        pointLabels: { color: dark ? '#ccc' : '#333', font: { size: 12 } }
      }
    },
    plugins: { legend: { display: false } }
  }
});
```

## Tooltip customization

```javascript
plugins: {
  tooltip: {
    backgroundColor: dark ? '#333' : '#fff',
    titleColor: dark ? '#eee' : '#111',
    bodyColor: dark ? '#ccc' : '#333',
    borderColor: dark ? 'rgba(255,255,255,0.1)' : 'rgba(0,0,0,0.1)',
    borderWidth: 1,
    cornerRadius: 6,
    padding: 10,
    callbacks: {
      label: ctx => `${ctx.dataset.label}: $${ctx.parsed.y.toLocaleString()}`
    }
  }
}
```

## Responsive layout pattern

For dashboards with metric cards above a chart:

```html
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
            gap: 12px; margin-bottom: 1.5rem;">
  <!-- metric cards -->
</div>
<div style="position: relative; width: 100%; height: 350px;">
  <canvas id="chart"></canvas>
</div>
```
