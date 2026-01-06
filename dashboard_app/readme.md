# AI Voice Automation System – Civic Services Agent

## Overview
This module implements the **AI Voice Automation layer** of a Civic Services platform.
It is responsible for handling **inbound and outbound voice interactions**, registering civil complaints,
performing automated resolution using AI logic, and escalating unresolved cases to human agents.

This system focuses on **voice-driven civic problem management** and operational analytics.

This module is **independent** of:
- Real telecom or IVR providers (numbers are simulated)
- External LLM reasoning engines
- Third-party government databases

It operates as a **self-contained, simulation-ready system** suitable for demos, MVPs, and system design evaluations.

---

## Responsibilities

- Capture and simulate voice-based citizen interactions
- Register and categorize civic complaints
- Track AI-handled vs human-escalated calls
- Calculate KPIs and operational metrics
- Visualize system performance via a dashboard
- Manage simulated toll-free and virtual numbers

---

## Key Features

- Inbound & outbound call simulation
- Complaint registration & categorization
- AI auto-resolution tracking
- Human escalation handling
- SLA & escalation monitoring
- Citizen experience & CSAT metrics
- Interactive analytics dashboard
- Modular and extensible architecture

---

## Supported Civic Domains

The system is designed to support multiple **civil and public service domains**, including:

- Water Supply & Sanitation
- Roads & Infrastructure
- Electricity & Power
- Public Safety
- Municipal Services
- General Civic Grievances

---

## Project Structure


---

## Module Breakdown

### 1. `dashboard.py`
**Purpose:**  
Acts as the main application controller.

**Responsibilities:**
- Initializes the Flask server
- Loads call logs
- Invokes KPI and analytics calculations
- Passes processed data to the dashboard UI

---

### 2. `kpi_calculations.py`
**Purpose:**  
Encapsulates all analytics and business logic.

**Responsibilities:**
- Parse call logs
- Compute system KPIs
- Separate logic from presentation
- Enable scalability and future database integration

**KPIs calculated include:**
- Total calls handled
- Inbound vs outbound distribution
- AI vs human resolution rate
- Complaint resolution rate
- Escalation metrics
- Citizen satisfaction indicators

---

### 3. `logs.csv`
**Purpose:**  
Simulated data source representing voice call interactions.

**Role:**
- Each row corresponds to a single call
- Acts as a lightweight stand-in for a production database
- Enables repeatable testing and analytics validation

---

### 4. `templates/dashboard.html`
**Purpose:**  
Frontend dashboard layer.

**Responsibilities:**
- Render KPI cards
- Display complaint statistics
- Inject backend data into the UI
- Act as the visualization layer

---

### 5. `static/style.css`
**Purpose:**  
Controls UI presentation.

**Responsibilities:**
- Layout styling
- Color themes
- Responsiveness and spacing
- Visual clarity for analytics

---

### 6. `static/charts.js`
**Purpose:**  
Handles all graphical analytics.

**Responsibilities:**
- Read dynamic data from the HTML layer
- Render charts using Chart.js
- Visualize trends, distributions, and KPIs

### Technology Stack
Backend-Python, Flask
Frontend-HTML, CSS, JS
Visualization-Chart.js
Data Source-CSV (simulated)

---

## System Workflow


---

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Install Dependencies
```bash
pip install flask