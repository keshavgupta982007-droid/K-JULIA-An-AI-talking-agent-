
document.addEventListener("DOMContentLoaded", () => {
  const body = document.body;
  const safeJSON = (val, fallback) => {
    try { return JSON.parse(val); } catch { return fallback; }
  };
  const inbound = Number(body.dataset.inbound) || 0;
  const outbound = Number(body.dataset.outbound) || 0;
  const durationData = safeJSON(body.dataset.duration, {});
  const hourlyData = safeJSON(body.dataset.hourly, {});
  const priorityData = safeJSON(body.dataset.priority, {});
  const languageData = safeJSON(body.dataset.language, {});
  const trendsData = safeJSON(body.dataset.trends, {});
  const topCategories = safeJSON(body.dataset.topCategories, []);
  
  // Global Chart Defaults
  Chart.defaults.color = "#94a3b8";
  Chart.defaults.font.family = "'Segoe UI', Tahoma, sans-serif";
  Chart.defaults.plugins.legend.labels.usePointStyle = true;
  
  const baseOptions = {
    responsive: true,
    maintainAspectRatio: false
  };
  
  const ctx = id => document.getElementById(id);
  
  // 1. Call Type (Doughnut)
  if (ctx("callTypeChart")) {
    new Chart(ctx("callTypeChart"), {
      type: "doughnut",
      data: {
        labels: ["Inbound Complaints", "Outbound Follow-ups"],
        datasets: [{
          data: [inbound, outbound],
          backgroundColor: ["rgba(59,130,246,.8)", "rgba(168,85,247,.8)"],
          borderWidth: 2
        }]
      },
      options: {
        ...baseOptions,
        plugins: {
          legend: { position: "bottom" },
          tooltip: {
            callbacks: {
              label(ctx) {
                const total = ctx.dataset.data.reduce((a, b) => a + b, 0);
                const pct = total ? ((ctx.parsed / total) * 100).toFixed(1) : 0;
                return `${ctx.label}: ${ctx.parsed} (${pct}%)`;
              }
            }
          }
        }
      }
    });
  }
  
  // 2. Duration (Bar)
  if (ctx("durationChart")) {
    new Chart(ctx("durationChart"), {
      type: "bar",
      data: {
        labels: ["0-1 min", "1-3 min", "3-5 min", "5-10 min", ">10 min"],
        datasets: [{
          label: "Number of Calls",
          data: [3200, 4800, 2100, 900, 450],
          backgroundColor: "#1c77c3",
          borderRadius: 8,
          barThickness: 36
        }]
      },
      options: {
        ...baseOptions,
        plugins: {
          title: {
            display: true,
            text: "Call Duration Distribution",
            font: { size: 20, weight: "bold" },
            color: "#0f4c81",
            padding: { bottom: 20 }
          },
          legend: {
            position: "top"
          }
        },
        scales: {
          x: { grid: { display: false } },
          y: { beginAtZero: true }
        }
      }
    });
  }
  
  // 3. Priority (Polar Area)
  if (ctx("priorityChart") && Object.keys(priorityData).length) {
    new Chart(ctx("priorityChart"), {
      type: "polarArea",
      data: {
        labels: Object.keys(priorityData),
        datasets: [{
          data: Object.values(priorityData),
          backgroundColor: [
            "rgba(16,185,129,.7)", // Low
            "rgba(245,158,11,.7)", // Medium
            "rgba(59,130,246,.7)", // High
            "rgba(239,68,68,.7)" // Critical
          ]
        }]
      },
      options: {
        ...baseOptions,
        plugins: {
          title: {
            display: true,
            text: "Call Priority Distribution",
            font: { size: 20, weight: "bold" },
            color: "#0f4c81",
            padding: { bottom: 20 }
          }
        }
      }
    });
  }
  
  // 4. Languages (Pie)
  if (ctx("languageChart") && Object.keys(languageData).length) {
    new Chart(ctx("languageChart"), {
      type: "pie",
      data: {
        labels: Object.keys(languageData),
        datasets: [{
          data: Object.values(languageData),
          backgroundColor: [
            "rgba(59,130,246,.8)",
            "rgba(168,85,247,.8)",
            "rgba(236,72,153,.8)",
            "rgba(245,158,11,.8)",
            "rgba(16,185,129,.8)"
          ]
        }]
      },
      options: {
        ...baseOptions,
        plugins: {
          title: {
            display: true,
            text: "Calls by Language",
            font: { size: 20, weight: "bold" },
            color: "#0f4c81",
            padding: { bottom: 20 }
          }
        }
      }
    });
  }
  
  // 5. Hourly Volume (Line)
  if (ctx("hourlyChart")) {
    new Chart(ctx("hourlyChart"), {
      type: "line",
      data: {
        labels: [...Array(24).keys()].map(h => `${h}:00`),
        datasets: [{
          label: "Call Volume",
          data: [200,250,300,350,400,200,250,300,800,600,700,800,400,400,400,400,400,800,600,700,800,250,300,350],
          borderColor: "#1c77c3",
          backgroundColor: "rgba(28,119,195,0.15)",
          fill: true,
          tension: 0.4,
          pointRadius: 4,
          pointBackgroundColor: "#1c77c3"
        }]
      },
      options: {
        ...baseOptions,
        plugins: {
          title: {
            display: true,
            text: "Hourly Call Volume",
            font: { size: 20, weight: "bold" },
            color: "#0f4c81",
            padding: { bottom: 20 }
          },
          legend: { position: "top" }
        },
        scales: {
          x: { grid: { display: false } },
          y: { beginAtZero: true }
        }
      }
    });
  }
  
  // 6. Top Civic Complaint Categories (Horizontal Bar)
  if (ctx("topCategoriesChart")) {
    new Chart(ctx("topCategoriesChart"), {
      type: "bar",
      data: {
        labels: [
          'Water Supply',
          'Road & Potholes',
          'Garbage Collection',
          'Electricity',
          'Street Lighting',
          'Sewage / Drainage'
        ],
        datasets: [{
          label: 'Complaints',
          data: [1450, 1120, 980, 750, 620, 500],
          backgroundColor: '#1c77c3',
          borderRadius: 8,
          barThickness: 28
        }]
      },
      options: {
        indexAxis: 'y',
        ...baseOptions,
        plugins: {
          title: {
            display: true,
            text: 'Top Civic Complaint Categories',
            font: { size: 20, weight: 'bold' },
            color: "#0f4c81",
            padding: { top: 10, bottom: 30 }
          },
          legend: { display: false }
        },
        scales: {
          x: { beginAtZero: true },
          y: { grid: { display: false } }
        }
      }
    });
  }
});
