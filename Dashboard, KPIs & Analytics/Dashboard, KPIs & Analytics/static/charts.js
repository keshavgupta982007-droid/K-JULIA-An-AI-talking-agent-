// Fetch data from body attributes
const body = document.body;

const inbound = parseInt(body.dataset.inbound) || 0;
const outbound = parseInt(body.dataset.outbound) || 0;
const durationData = JSON.parse(body.dataset.duration || '{}');
const hourlyData = JSON.parse(body.dataset.hourly || '{}');
const priorityData = JSON.parse(body.dataset.priority || '{}');
const languageData = JSON.parse(body.dataset.language || '{}');
const trendsData = JSON.parse(body.dataset.trends || '{}');
const topCategories = JSON.parse(body.dataset.topCategories || '[]');

// Chart configuration
Chart.defaults.color = '#94a3b8';
Chart.defaults.borderColor = 'rgba(255, 255, 255, 0.1)';
Chart.defaults.font.family = "'Segoe UI', Tahoma, Geneva, Verdana, sans-serif";

// 1. Call Type Distribution (Doughnut)
new Chart(document.getElementById("callTypeChart"), {
  type: "doughnut",
  data: {
    labels: ["Inbound Complaints", "Outbound Follow-ups"],
    datasets: [{
      data: [inbound, outbound],
      backgroundColor: [
        'rgba(59, 130, 246, 0.8)',
        'rgba(168, 85, 247, 0.8)'
      ],
      borderColor: [
        'rgba(59, 130, 246, 1)',
        'rgba(168, 85, 247, 1)'
      ],
      borderWidth: 2
    }]
  },
  options: {
    responsive: true,
    maintainAspectRatio: true,
    plugins: {
      legend: {
        position: 'bottom',
        labels: {
          padding: 15,
          font: { size: 12 }
        }
      },
      tooltip: {
        callbacks: {
          label: function(context) {
            const label = context.label || '';
            const value = context.parsed || 0;
            const total = context.dataset.data.reduce((a, b) => a + b, 0);
            const percentage = ((value / total) * 100).toFixed(1);
            return `${label}: ${value} (${percentage}%)`;
          }
        }
      }
    }
  }
});

// 2. Duration Analysis (Bar Chart)
new Chart(document.getElementById("durationChart"), {
  type: "bar",
  data: {
    labels: Object.keys(durationData),
    datasets: [{
      label: 'Number of Calls',
      data: Object.values(durationData),
      backgroundColor: 'rgba(34, 211, 238, 0.8)',
      borderColor: 'rgba(34, 211, 238, 1)',
      borderWidth: 2,
      borderRadius: 6
    }]
  },
  options: {
    responsive: true,
    maintainAspectRatio: true,
    plugins: {
      legend: { display: false },
      tooltip: {
        callbacks: {
          label: function(context) {
            return `Calls: ${context.parsed.y}`;
          }
        }
      }
    },
    scales: {
      y: {
        beginAtZero: true,
        ticks: { stepSize: 1 },
        grid: { color: 'rgba(255, 255, 255, 0.05)' }
      },
      x: {
        grid: { display: false }
      }
    }
  }
});

// 3. Priority Distribution (Polar Area)
if (Object.keys(priorityData).length > 0) {
  new Chart(document.getElementById("priorityChart"), {
    type: "polarArea",
    data: {
      labels: Object.keys(priorityData),
      datasets: [{
        data: Object.values(priorityData),
        backgroundColor: [
          'rgba(239, 68, 68, 0.7)',    // Critical - Red
          'rgba(245, 158, 11, 0.7)',   // High - Orange
          'rgba(59, 130, 246, 0.7)',   // Medium - Blue
          'rgba(16, 185, 129, 0.7)'    // Low - Green
        ],
        borderColor: [
          'rgba(239, 68, 68, 1)',
          'rgba(245, 158, 11, 1)',
          'rgba(59, 130, 246, 1)',
          'rgba(16, 185, 129, 1)'
        ],
        borderWidth: 2
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: true,
      plugins: {
        legend: {
          position: 'bottom',
          labels: { padding: 15, font: { size: 12 } }
        }
      },
      scales: {
        r: {
          ticks: { display: false },
          grid: { color: 'rgba(255, 255, 255, 0.1)' }
        }
      }
    }
  });
}

// 4. Language Support (Pie Chart)
if (Object.keys(languageData).length > 0) {
  const languageColors = [
    'rgba(59, 130, 246, 0.8)',
    'rgba(168, 85, 247, 0.8)',
    'rgba(236, 72, 153, 0.8)',
    'rgba(245, 158, 11, 0.8)',
    'rgba(16, 185, 129, 0.8)',
    'rgba(239, 68, 68, 0.8)'
  ];

  new Chart(document.getElementById("languageChart"), {
    type: "pie",
    data: {
      labels: Object.keys(languageData),
      datasets: [{
        data: Object.values(languageData),
        backgroundColor: languageColors.slice(0, Object.keys(languageData).length),
        borderColor: languageColors.slice(0, Object.keys(languageData).length).map(c => c.replace('0.8', '1')),
        borderWidth: 2
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: true,
      plugins: {
        legend: {
          position: 'bottom',
          labels: { padding: 15, font: { size: 12 } }
        },
        tooltip: {
          callbacks: {
            label: function(context) {
              const label = context.label || '';
              const value = context.parsed || 0;
              const total = context.dataset.data.reduce((a, b) => a + b, 0);
              const percentage = ((value / total) * 100).toFixed(1);
              return `${label}: ${value} calls (${percentage}%)`;
            }
          }
        }
      }
    }
  });
}

// 5. Hourly Call Volume (Line Chart)
if (Object.keys(hourlyData).length > 0) {
  const hours = Object.keys(hourlyData).map(h => `${h}:00`);
  const values = Object.values(hourlyData);

  new Chart(document.getElementById("hourlyChart"), {
    type: "line",
    data: {
      labels: hours,
      datasets: [{
        label: 'Calls per Hour',
        data: values,
        backgroundColor: 'rgba(139, 92, 246, 0.2)',
        borderColor: 'rgba(139, 92, 246, 1)',
        borderWidth: 3,
        fill: true,
        tension: 0.4,
        pointRadius: 5,
        pointHoverRadius: 7,
        pointBackgroundColor: 'rgba(139, 92, 246, 1)',
        pointBorderColor: '#fff',
        pointBorderWidth: 2
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: true,
      plugins: {
        legend: { display: false },
        tooltip: {
          callbacks: {
            title: function(context) {
              return `Hour: ${context[0].label}`;
            },
            label: function(context) {
              return `Total Calls: ${context.parsed.y}`;
            }
          }
        }
      },
      scales: {
        y: {
          beginAtZero: true,
          ticks: { stepSize: 1 },
          grid: { color: 'rgba(255, 255, 255, 0.05)' },
          title: {
            display: true,
            text: 'Number of Calls',
            color: '#94a3b8'
          }
        },
        x: {
          grid: { display: false },
          title: {
            display: true,
            text: 'Time of Day',
            color: '#94a3b8'
          }
        }
      }
    }
  });
}

// 6. Top Complaint Categories (Horizontal Bar)
if (topCategories.length > 0) {
  const categories = topCategories.map(c => c[0]);
  const counts = topCategories.map(c => c[1]);

  new Chart(document.getElementById("categoryChart"), {
    type: "bar",
    data: {
      labels: categories,
      datasets: [{
        label: 'Number of Complaints',
        data: counts,
        backgroundColor: [
          'rgba(59, 130, 246, 0.8)',
          'rgba(16, 185, 129, 0.8)',
          'rgba(245, 158, 11, 0.8)',
          'rgba(239, 68, 68, 0.8)',
          'rgba(168, 85, 247, 0.8)'
        ],
        borderColor: [
          'rgba(59, 130, 246, 1)',
          'rgba(16, 185, 129, 1)',
          'rgba(245, 158, 11, 1)',
          'rgba(239, 68, 68, 1)',
          'rgba(168, 85, 247, 1)'
        ],
        borderWidth: 2,
        borderRadius: 6
      }]
    },
    options: {
      indexAxis: 'y',
      responsive: true,
      maintainAspectRatio: true,
      plugins: {
        legend: { display: false },
        tooltip: {
          callbacks: {
            label: function(context) {
              return `Complaints: ${context.parsed.x}`;
            }
          }
        }
      },
      scales: {
        x: {
          beginAtZero: true,
          ticks: { stepSize: 1 },
          grid: { color: 'rgba(255, 255, 255, 0.05)' }
        },
        y: {
          grid: { display: false }
        }
      }
    }
  });
}

// 7. Trend Analysis (Multi-line Chart)
if (Object.keys(trendsData).length > 0) {
  const dates = Object.keys(trendsData);
  const totalData = dates.map(date => trendsData[date].total);
  const resolvedData = dates.map(date => trendsData[date].resolved);
  const escalatedData = dates.map(date => trendsData[date].escalated);
  const satisfiedData = dates.map(date => trendsData[date].satisfied);

  new Chart(document.getElementById("trendChart"), {
    type: "line",
    data: {
      labels: dates,
      datasets: [
        {
          label: 'Total Calls',
          data: totalData,
          borderColor: 'rgba(59, 130, 246, 1)',
          backgroundColor: 'rgba(59, 130, 246, 0.1)',
          borderWidth: 2,
          tension: 0.4,
          fill: false
        },
        {
          label: 'Resolved',
          data: resolvedData,
          borderColor: 'rgba(16, 185, 129, 1)',
          backgroundColor: 'rgba(16, 185, 129, 0.1)',
          borderWidth: 2,
          tension: 0.4,
          fill: false
        },
        {
          label: 'Escalated',
          data: escalatedData,
          borderColor: 'rgba(239, 68, 68, 1)',
          backgroundColor: 'rgba(239, 68, 68, 0.1)',
          borderWidth: 2,
          tension: 0.4,
          fill: false
        },
        {
          label: 'Satisfied Citizens',
          data: satisfiedData,
          borderColor: 'rgba(245, 158, 11, 1)',
          backgroundColor: 'rgba(245, 158, 11, 0.1)',
          borderWidth: 2,
          tension: 0.4,
          fill: false
        }
      ]
    },
    options: {
      responsive: true,
      maintainAspectRatio: true,
      plugins: {
        legend: {
          position: 'bottom',
          labels: { padding: 15, font: { size: 12 } }
        },
        tooltip: {
          mode: 'index',
          intersect: false
        }
      },
      scales: {
        y: {
          beginAtZero: true,
          ticks: { stepSize: 1 },
          grid: { color: 'rgba(255, 255, 255, 0.05)' },
          title: {
            display: true,
            text: 'Number of Calls',
            color: '#94a3b8'
          }
        },
        x: {
          grid: { display: false },
          title: {
            display: true,
            text: 'Date',
            color: '#94a3b8'
          }
        }
      }
    }
  });
}