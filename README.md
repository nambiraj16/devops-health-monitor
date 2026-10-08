# DevOps Health Monitor (DevOps Internship Task 4)

[![Git Version Control](https://img.shields.io/badge/Git-Best%20Practices-F05032?logo=git&logoColor=white)](https://git-scm.com/)
[![GitHub Branches](https://img.shields.io/badge/Branches-main%20%7C%20dev%20%7C%20feature-181717?logo=github)](https://github.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

A lightweight, professional DevOps monitoring utility and demonstration project created for **Task 4: Build a Version-Controlled DevOps Project with Git**.

---

## 📌 Project Overview
This project serves a dual purpose:
1. **Practical DevOps Utility:** A modular Python CLI application that inspects system resources with **enhanced diagnostics** (automated threshold evaluation for disk space reporting `HEALTHY` or `WARNING`) and verifies microservice health checks based on declarative JSON configurations.
2. **Version Control Demonstration:** Demonstrates an enterprise Git workflow including multi-branch branching strategies (`main`, `dev`, `feature/*`), GitHub Pull Requests, annotated semantic release tags (`v1.0.0`), `.gitignore` filtering, and markdown documentation.

### ✨ Key Features
- **Enhanced Diagnostics:** Automated disk capacity analysis against configurable thresholds with status classifications (`HEALTHY` vs `WARNING`).
- **Endpoint Verification:** Automated status checks and latency tracking for microservices.
- **Configurable Thresholds:** Declarative threshold settings in `config/config.json`.
- **JSON Report Export:** Option to generate timestamped audit reports via `--export`.
- **Zero Third-Party Dependencies:** Built entirely with the Python standard library.

---

## 🛠️ Tech Stack & Prerequisites
- **Language:** Python 3.8+ (Uses only standard library; zero third-party packages required).
- **Version Control:** Git & GitHub.
- **Tools:** No paid tools or external software required.

---

## 📂 Project Structure
```text
.
├── .gitignore                    # Git ignore file
├── README.md                     # Main documentation
├── config/
│   └── config.json               # Environment & service endpoints configuration
├── app/
│   ├── __init__.py               # Application package definition
│   ├── monitor.py                # Main monitoring logic
│   └── utils.py                  # Utility functions
├── tests/
│   ├── __init__.py               # Test package definition
│   └── test_monitor.py           # Unit tests
└── docs/
    ├── GIT_WORKFLOW.md           # Branching, PR, and release workflow guide
    └── INTERVIEW_QUESTIONS.md    # Task 4 interview answers
```

---

## 🚀 How to Run

### 1. Execute Health Check
```bash
python -m app.monitor
```

### 2. Execute with JSON Report Export
```bash
python -m app.monitor --export
```

### 3. Run Automated Tests
```bash
python -m unittest discover tests
```

---

## 🌿 Git Branching Strategy
- **`main`**: Production-ready code tagged with release versions (`v1.0.0`).
- **`dev`**: Staging/development branch.
- **`feature/*`**: Isolated branches for specific enhancements merged via Pull Requests.

For the detailed step-by-step walkthrough, see [GIT_WORKFLOW.md](docs/GIT_WORKFLOW.md).  
For the interview questions, see [INTERVIEW_QUESTIONS.md](docs/INTERVIEW_QUESTIONS.md).
