<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>AI Voice Automation – Civic Services Command Center</title>

  <!-- Font Awesome for Icons -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" />

  <!-- Chart.js -->
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

  <style>
    :root {
      --primary: #0f4c81;
      --primary-light: #1c77c3;
      --bg: #f4f6f9;
      --card: #ffffff;
      --text: #2c3e50;
      --muted: #7f8c8d;
      --success: #27ae60;
      --warning: #f39c12;
      --danger: #e74c3c;
      --info: #3498db;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: "Segoe UI", Arial, sans-serif;
      background: var(--bg);
      color: var(--text);
      line-height: 1.6;
    }

    /* Animations */
    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(20px); }
      to { opacity: 1; transform: translateY(0); }
    }

    @keyframes pulse {
      0% { box-shadow: 0 0 0 0 rgba(15, 76, 129, 0.4); }
      70% { box-shadow: 0 0 0 10px rgba(15, 76, 129, 0); }
      100% { box-shadow: 0 0 0 0 rgba(15, 76, 129, 0); }
    }

    .animate-fade { animation: fadeIn 0.8s ease-out forwards; }
    .animate-pulse { animation: pulse 2s infinite; }

    /* Header */
    header {
      background: linear-gradient(135deg, var(--primary), var(--primary-light));
      color: white;
      padding: 32px;
      box-shadow: 0 4px 20px rgba(0,0,0,0.1);
    }

    .header-content {
      max-width: 1400px;
      margin: 0 auto;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 20px;
    }

    h1 { font-size: 2.2rem; }
    .subtitle { opacity: 0.9; font-size: 1.1rem; }

    .header-actions button {
      padding: 12px 20px;
      border: none;
      border-radius: 8px;
      background: white;
      color: var(--primary);
      font-weight: 600;
      cursor: pointer;
      transition: all 0.3s;
    }

    .header-actions button:hover {
      transform: translateY(-2px);
      box-shadow: 0 6px 15px rgba(0,0,0,0.15);
    }

    /* Sections */
    section {
      max-width: 1400px;
      margin: 40px auto;
      padding: 0 32px;
    }

    h2 {
      font-size: 1.8rem;
      margin-bottom: 24px;
      color: var(--primary);
      display: flex;
      align-items: center;
      gap: 10px;
    }

    /* Grid */
    .grid {
      display: grid;
      gap: 24px;
    }

    .grid-3 { grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); }
    .grid-4 { grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); }
    .grid-5 { grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); }

    /* Cards */
    .card {
      background: var(--card);
      padding: 24px;
      border-radius: 12px;
      box-shadow: 0 6px 18px rgba(0,0,0,0.08);
      transition: all 0.4s;
      opacity: 0;
    }

    .card:hover {
      transform: translateY(-8px);
      box-shadow: 0 12px 30px rgba(0,0,0,0.15);
    }

    .card-label {
      color: var(--muted);
      font-size: 0.95rem;
      margin-bottom: 8px;
    }

    .card-value {
      font-size: 2.2rem;
      font-weight: 700;
      color: var(--primary);
    }

    /* Insights Banner */
    .insights-banner {
      background: linear-gradient(135deg, #eef4ff, #f0f8ff);
      border-radius: 16px;
      padding: 24px;
      box-shadow: 0 6px 20px rgba(0,0,0,0.05);
      margin: 40px auto;
      max-width: 1400px;
    }

    .insights-container {
      display: flex;
      gap: 16px;
      flex-wrap: wrap;
    }

    .insight-card {
      padding: 14px 20px;
      border-radius: 12px;
      font-weight: 500;
      display: flex;
      align-items: center;
      gap: 10px;
      min-width: 280px;
      flex: 1;
      opacity: 0;
      animation: fadeIn 1s ease-out forwards;
    }

    .insight-card.info { background: #d6eaff; color: var(--info); }
    .insight-card.warning { background: #fff0d6; color: var(--warning); }
    .insight-card.success { background: #d6f0e0; color: var(--success); }
    .insight-card.alert { background: #ffd6d6; color: var(--danger); }

    /* Charts */
    .charts-grid {
      display: grid;
      gap: 20px;
      grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
    }

    .chart-container {
      background: var(--card);
      padding: 20px;
      border-radius: 16px;
      box-shadow: 0 6px 20px rgba(0,0,0,0.08);
      opacity: 0;
      height: 350px;
      display: flex;
      flex-direction: column;
    }

    .chart-container.chart-wide {
      grid-column: span 2;
    }

    .chart-container h3 {
      margin-bottom: 20px;
      color: var(--primary);
      text-align: center;
    }

    canvas {
      flex: 1;
    }

    .section-loader {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      min-height: 400px;
      color: var(--primary);
    }

    .section-loader .loader {
      width: 50px;
      height: 50px;
      border: 4px solid var(--muted);
      border-top: 4px solid var(--primary);
      border-radius: 50%;
      animation: spin 1s linear infinite;
      margin-bottom: 16px;
    }

    @keyframes spin {
      from { transform: rotate(0deg); }
      to { transform: rotate(360deg); }
    }

    /* Footer */
    footer {
      text-align: center;
      padding: 24px;
      background: var(--card);
      color: var(--muted);
      font-size: 0.9rem;
      margin-top: 60px;
      box-shadow: 0 -4px 15px rgba(0,0,0,0.05);
    }

    /* Responsive */
    @media (max-width: 1024px) {
      .charts-grid { grid-template-columns: 1fr; }
      .chart-container.chart-wide { grid-column: span 1; }
    }

    @media (max-width: 768px) {
      h1 { font-size: 1.8rem; }
      section { padding: 0 16px; }
    }
  </style>
</head>
<body>

  <!-- ================= HEADER ================= -->
  <header>
    <div class="header-content">
      <div>
        <h1><i class="fas fa-headset"></i> AI Voice Automation System</h1>
        <p class="subtitle">Intelligent Civic Services Command Center</p>
      </div>
      <div class="header-actions">
        <button onclick="location.reload()">
          <i class="fas fa-sync-alt"></i> Refresh
        </button>
        <button onclick="alert('Report export feature coming soon!')">
          <i class="fas fa-download"></i> Export Report
        </button>
      </div>
    </div>
  </header>

  <!-- ================= INSIGHTS ================= -->
  <section class="insights-banner">
    <h2><i class="fas fa-lightbulb"></i> Real-Time Insights & Alerts</h2>
    <div class="insights-container">
      <div class="insight-card info animate-fade" style="animation-delay: 0.2s;">
        <i class="fas fa-info-circle"></i>
        <span>Call volume increased by 18% compared to yesterday.</span>
      </div>
      <div class="insight-card warning animate-fade" style="animation-delay: 0.4s;">
        <i class="fas fa-exclamation-triangle"></i>
        <span>High priority complaints up by 12% in the last hour.</span>
      </div>
      <div class="insight-card success animate-fade" style="animation-delay: 0.6s;">
        <i class="fas fa-check-circle"></i>
        <span>AI resolution rate at all-time high: 71.6%</span>
      </div>
      <div class="insight-card alert animate-fade animate-pulse" style="animation-delay: 0.8s;">
        <i class="fas fa-bell"></i>
        <span>Peak hour approaching – prepare agent staffing.</span>
      </div>
    </div>
  </section>

  <!-- ================= SYSTEM OVERVIEW ================= -->
  <section>
    <h2><i class="fas fa-tachometer-alt"></i> System Performance Overview</h2>
    <div class="grid grid-4">
      <div class="card animate-fade" style="animation-delay: 0.1s;">
        <div class="card-label">Total Calls Handled</div>
        <div class="card-value">12,450</div>
      </div>
      <div class="card animate-fade" style="animation-delay: 0.2s;">
        <div class="card-label">Inbound Civic Requests</div>
        <div class="card-value">9,870</div>
      </div>
      <div class="card animate-fade" style="animation-delay: 0.3s;">
        <div class="card-label">Outbound Follow-ups</div>
        <div class="card-value">2,580</div>
      </div>
      <div class="card animate-fade" style="animation-delay: 0.4s;">
        <div class="card-label">Avg Call Duration</div>
        <div class="card-value">185 sec</div>
      </div>
    </div>
  </section>

  <!-- ================= AI PERFORMANCE ================= -->
  <section>
    <h2><i class="fas fa-robot"></i> AI Resolution Performance</h2>
    <div class="grid grid-3">
      <div class="card animate-fade" style="animation-delay: 0.5s;">
        <div class="card-label">AI-Resolved Calls</div>
        <div class="card-value">8,920</div>
      </div>
      <div class="card animate-fade" style="animation-delay: 0.6s;">
        <div class="card-label">Human Escalations</div>
        <div class="card-value">3,530</div>
      </div>
      <div class="card animate-fade" style="animation-delay: 0.7s;">
        <div class="card-label">Auto-Resolution Rate</div>
        <div class="card-value">77.1%</div>
      </div>
    </div>
  </section>

  <!-- ================= COMPLAINT INTELLIGENCE ================= -->
  <section>
    <h2><i class="fas fa-file-alt"></i> Civic Complaint Intelligence</h2>
    <div class="grid grid-5">
      <div class="card animate-fade" style="animation-delay: 0.8s;">
        <div class="card-label">Registered</div>
        <div class="card-value">5,420</div>
      </div>
      <div class="card animate-fade" style="animation-delay: 0.9s;">
        <div class="card-label">Resolved</div>
        <div class="card-value">4,180</div>
      </div>
      <div class="card animate-fade" style="animation-delay: 1s;">
        <div class="card-label">Auto-Resolved</div>
        <div class="card-value">3,120</div>
      </div>
      <div class="card animate-fade" style="animation-delay: 1.1s;">
        <div class="card-label">Pending</div>
        <div class="card-value">890</div>
      </div>
      <div class="card animate-fade" style="animation-delay: 1.2s;">
        <div class="card-label">Escalated</div>
        <div class="card-value">350</div>
      </div>
    </div>
  </section>

  <!-- ================= ANALYTICS ================= -->
  <section>
    <h2><i class="fas fa-chart-bar"></i> Call Analytics</h2>
    <div id="chartsLoader" class="section-loader">
      <div class="loader"></div>
      <p>Loading Analytics Data...</p>
    </div>
    <div class="charts-grid" style="display: none;">
      <div class="chart-container animate-fade" style="animation-delay: 0.2s;">
        <h3>Inbound vs Outbound</h3>
        <canvas id="callTypeChart"></canvas>
      </div>

      <div class="chart-container animate-fade" style="animation-delay: 0.4s;">
        <h3>Call Duration Distribution</h3>
        <canvas id="durationChart"></canvas>
      </div>

      <div class="chart-container animate-fade" style="animation-delay: 0.6s;">
        <h3>Priority Levels</h3>
        <canvas id="priorityChart"></canvas>
      </div>

      <div class="chart-container animate-fade" style="animation-delay: 0.8s;">
        <h3>Languages Used</h3>
        <canvas id="languageChart"></canvas>
      </div>

      <div class="chart-container chart-wide animate-fade" style="animation-delay: 1s;">
        <h3>Hourly Call Volume</h3>
        <canvas id="hourlyChart"></canvas>
      </div>

      <div class="chart-container chart-wide animate-fade" style="animation-delay: 1.2s;">
        <h3>Top Civic Complaint Categories</h3>
        <canvas id="categoryChart"></canvas>
      </div>
    </div>
  </section>

  <!-- ================= FOOTER ================= -->
  <footer>
    <p>
      <i class="fas fa-lock"></i> Secure |
      <i class="fas fa-user-shield"></i> Privacy-First |
      <i class="fas fa-shield-alt"></i> Government-Grade
    </p>
    <p>Last Updated: <span id="lastUpdate"></span></p>
  </footer>

  <script>
    // Trigger animations on load
    window.addEventListener('load', () => {
      document.querySelectorAll('.animate-fade').forEach(el => {
        el.style.opacity = 1;
      });
      document.getElementById('lastUpdate').textContent = new Date().toLocaleString();

      setTimeout(() => {
        // Chart Configuration
        const chartOptions = {
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
            legend: { position: 'top' },
            tooltip: { backgroundColor: 'rgba(0,0,0,0.8)' }
          },
          animation: {
            duration: 1500,
            easing: 'easeOutQuart'
          }
        };

        // Inbound vs Outbound - Doughnut
        new Chart(document.getElementById('callTypeChart'), {
          type: 'doughnut',
          data: {
            labels: ['Inbound', 'Outbound'],
            datasets: [{
              data: [9870, 2580],
              backgroundColor: ['#0f4c81', '#1c77c3'],
              borderWidth: 0
            }]
          },
          options: chartOptions
        });

        // Duration Distribution - Bar
        new Chart(document.getElementById('durationChart'), {
          type: 'bar',
          data: {
            labels: ['0-1 min', '1-3 min', '3-5 min', '5-10 min', '>10 min'],
            datasets: [{
              label: 'Number of Calls',
              data: [3200, 4800, 2100, 900, 450],
              backgroundColor: '#0f4c81'
            }]
          },
          options: { ...chartOptions, scales: { y: { beginAtZero: true } } }
        });

        // Priority Levels - Pie
        new Chart(document.getElementById('priorityChart'), {
          type: 'pie',
          data: {
            labels: ['Low', 'Medium', 'High', 'Critical'],
            datasets: [{
              data: [6200, 3000, 850, 400],
              backgroundColor: ['#27ae60', '#f39c12', '#e67e22', '#e74c3c']
            }]
          },
          options: chartOptions
        });

        // Languages - Doughnut
        new Chart(document.getElementById('languageChart'), {
          type: 'doughnut',
          data: {
            labels: ['English', 'Hindi', 'Tamil', 'Telugu', 'Others'],
            datasets: [{
              data: [5800, 3200, 600, 450, 400],
              backgroundColor: ['#0f4c81', '#1c77c3', '#3498db', '#9b59b6', '#7f8c8d']
            }]
          },
          options: chartOptions
        });

        // Hourly Volume - Line
        new Chart(document.getElementById('hourlyChart'), {
          type: 'line',
          data: {
            labels: ['00:00','01:00','02:00','03:00','04:00','05:00','06:00','07:00','08:00','09:00','10:00','11:00','12:00','13:00','14:00','15:00','16:00','17:00','18:00','19:00','20:00','21:00','22:00','23:00'],
            datasets: [{
              label: 'Call Volume',
              data: [200,250,300,350,400,200,250,300,800,600,700,800,400,400,400,400,400,800,600,700,800,250,300,350],
              borderColor: '#0f4c81',
              backgroundColor: 'rgba(15,76,129,0.1)',
              fill: true,
              tension: 0.4
            }]
          },
          options: { ...chartOptions, scales: { y: { beginAtZero: true } } }
        });

        // Top Categories - Horizontal Bar
        new Chart(document.getElementById('categoryChart'), {
          type: 'bar',
          data: {
            labels: ['Water Supply', 'Road & Potholes', 'Garbage Collection', 'Electricity', 'Street Lighting', 'Sewage/Drainage'],
            datasets: [{
              label: 'Complaints',
              data: [1450,1120,980,750,620,500],
              backgroundColor: '#1c77c3'
            }]
          },
          options: {
            ...chartOptions,
            indexAxis: 'y',
            scales: { x: { beginAtZero: true } }
          }
        });

        document.getElementById('chartsLoader').style.display = 'none';
        document.querySelector('.charts-grid').style.display = 'grid';
      }, 1500);
    });
  </script>
</body>
</html>
