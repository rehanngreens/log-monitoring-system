# 📊 Real-Time Log Monitoring & Alerting System

A Python-based real-time log monitoring, alerting, and dashboard system that simulates how production systems track operational health using logs.

---

## 🚀 Project Overview

In real-world systems, applications and servers continuously generate logs.
Manually analyzing these logs during failures is inefficient and time-consuming.

This project automates that process by:

* Generating realistic logs
* Analyzing log data
* Detecting system issues
* Triggering alerts
* Displaying system health via a dashboard

---

## 🧠 Key Features

### ✅ Log Generation

* Simulates realistic system logs
* Supports:

  * `INFO`
  * `WARNING`
  * `ERROR`
* Stores logs in:

  ```
  logs/server.log
  ```

---

### ✅ Log Analysis

* Uses Python + Regex to parse logs
* Extracts:

  * Timestamp
  * Severity level
  * Message
* Counts occurrences of each log type

---

### ✅ System Health Classification

System status is determined based on log severity:

* `NORMAL`
* `WARNING`
* `CRITICAL`

---

### ✅ JSON Reporting

* Generates structured report:

  ```
  report.json
  ```
* Includes:

  * Total logs
  * INFO / WARNING / ERROR counts
  * System status
  * Timestamp

---

### ✅ Real-Time Monitoring

* Continuously monitors logs
* Runs in a loop
* Detects state transitions:

  * NORMAL → WARNING
  * WARNING → CRITICAL
  * CRITICAL → NORMAL

---

### ✅ Smart Alerting System

* Triggers alerts on:

  * WARNING
  * CRITICAL
* Prevents duplicate alert spam
* Detects recovery
* Stores alerts in:

  ```
  alerts.log
  ```

---

### ✅ Flask Dashboard

* Displays:

  * System status
  * Log counts
  * Last updated time
  * Alert history
* Accessible via browser

---

## 🏗 Project Structure

```
Real-Time-Log-Monitoring-System/
│
├── analyzer.py
├── monitor.py
├── app.py
│
├── report.json
├── alerts.log
│
├── logs/
│   └── server.log
│   └── log_generator.py
│
├── templates/
│   └── ops_dashboard.html
│
└── README.md
```

---

## ⚙️ Technologies Used

* Python 3
* Flask
* Regex
* JSON
* HTML / CSS

---

## 📌 How to Run

### 1️⃣ Generate Logs

```
python3 log_generator.py
```

---

### 2️⃣ Analyze Logs

```
python3 analyzer.py
```

---

### 3️⃣ Start Monitoring

```
python3 monitor.py
```

---

### 4️⃣ Run Dashboard

```
python3 app.py
```


## 📊 Dashboard Shows

* 🚦 System Status
* ℹ️ INFO count
* ⚠️ WARNING count
* ❌ ERROR count
* 📄 Total logs
* 🕒 Last updated time
* 🚨 Alert history

---

## 🧪 Use Cases

* Log Monitoring
* Incident Detection
* System Health Tracking
* DevOps / Cloud Learning
* Observability Basics

---


## 🚀 Future Improvements

* Multi-service log support
* Docker containerization
* CI/CD pipeline
* Prometheus metrics
* Grafana dashboard
* Email / Slack alerts

---

## 👨‍💻 Author

**Rehann John**

Aspiring Cloud & DevOps Engineer
