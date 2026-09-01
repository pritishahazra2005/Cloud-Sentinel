# 🛡️ CloudSentinel

### AWS Cloud Security Posture Assessment Platform

> **CloudSentinel** is a lightweight AWS security assessment tool designed to identify common cloud security misconfigurations, evaluate risk, and provide actionable remediation recommendations through a clean web dashboard.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-Boto3-FF9900?style=for-the-badge\&logo=amazonaws\&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge\&logo=fastapi\&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-Frontend-F7DF1E?style=for-the-badge\&logo=javascript\&logoColor=black)
![Testing](https://img.shields.io/badge/Tests-Pytest-0A9EDC?style=for-the-badge\&logo=pytest\&logoColor=white)

---

## ✨ Overview

CloudSentinel performs a **Cloud Security Posture Assessment (CSPA)** against selected AWS services.

The project combines:

* 🔍 AWS security scanning
* 🧑‍💻 IAM security checks
* 🪣 S3 configuration assessment
* 🌐 Security Group exposure analysis
* 📊 Risk-based security scoring
* 🤖 Automated remediation recommendations
* 📄 PDF security reports
* 🧪 Automated unit testing
* 🖥️ Interactive web dashboard

CloudSentinel also includes a **Demo Scan mode**, allowing the complete assessment workflow to be demonstrated without requiring access to an AWS environment.

---

# 🚀 Key Features

### 🔎 AWS Security Scanner

CloudSentinel currently assesses selected AWS resources for common security issues.

| AWS Service            | Security Checks                          |
| ---------------------- | ---------------------------------------- |
| 🪣 Amazon S3           | Public access configuration, encryption  |
| 👤 AWS IAM             | MFA and identity-related security checks |
| 🌐 EC2 Security Groups | Exposed ports and unrestricted access    |

---

### 📊 Risk Scoring Engine

Detected findings are evaluated according to their severity.

```text
CRITICAL  → Highest Risk
HIGH      → High Risk
MEDIUM    → Moderate Risk
LOW       → Lower Risk
```

The risk engine converts the findings into an overall **Security Score out of 100**.

Example:

```text
┌──────────────────────────────┐
│       SECURITY SCORE         │
│                              │
│           82 / 100           │
│                              │
│  Critical   0                │
│  High       1                │
│  Medium     2                │
│  Low        1                │
└──────────────────────────────┘
```

---

### 🤖 AI-Assisted Security Advisor

CloudSentinel generates remediation recommendations for detected findings.

Instead of simply reporting:

> "MFA is not enabled."

the system can provide actionable guidance such as:

> Enable MFA for IAM identities to reduce the risk of credential compromise.

This makes the assessment more useful for developers and cloud administrators.

---

### 🖥️ Security Dashboard

The frontend provides a simple security-focused dashboard containing:

* Security score
* Scan mode
* Finding count
* Severity breakdown
* Security findings
* Remediation recommendations

The dashboard supports both:

```text
Demo Scan
    ↓
Simulated security findings
```

and:

```text
AWS Scan
    ↓
Real AWS security assessment
```

---

### 📄 Security Reports

CloudSentinel can generate security assessment reports containing:

* Assessment summary
* Security score
* Finding severity
* Affected resources
* Security descriptions
* Remediation recommendations

Reports can be used as assessment artifacts for documentation and review.

---

### 🧪 Automated Testing

The project includes unit tests for important components such as the risk scoring engine.

Testing is performed using **pytest**.

Run:

```bash
pytest
```

---

# 🏗️ Project Architecture

```text
                         ┌─────────────────────┐
                         │      AWS Account    │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   AWS Scanners      │
                         │                     │
                         │  S3   IAM   EC2 SG  │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   Finding Engine    │
                         └──────────┬──────────┘
                                    │
                     ┌──────────────┴──────────────┐
                     ▼                             ▼
          ┌──────────────────┐          ┌──────────────────┐
          │   Risk Engine    │          │   AI Advisor     │
          │                  │          │                  │
          │ Security Score   │          │ Recommendations  │
          └────────┬─────────┘          └────────┬─────────┘
                   │                             │
                   └──────────────┬──────────────┘
                                  ▼
                       ┌─────────────────────┐
                       │  FastAPI Backend    │
                       └──────────┬──────────┘
                                  │
                                  ▼
                       ┌─────────────────────┐
                       │   Web Dashboard     │
                       └─────────────────────┘
```

---

# 📁 Project Structure

```text
Cloud-Sentinel/
│
├── backend/
│   ├── app.py
│   │
│   ├── ai/
│   │   ├── __init__.py
│   │   └── advisor.py
│   │
│   ├── scanners/
│   │   ├── __init__.py
│   │   ├── s3_scanner.py
│   │   ├── iam_scanner.py
│   │   └── security_group_scanner.py
│   │
│   └── risk/
│       ├── __init__.py
│       └── risk_engine.py
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── dashboard.js
│
├── reports/
│   └── reports.py
│
├── tests/
│   └── test_risk.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ Technologies Used

| Technology              | Purpose                             |
| ----------------------- | ----------------------------------- |
| **Python**              | Core application and security logic |
| **FastAPI**             | Backend REST API                    |
| **Boto3**               | AWS SDK for Python                  |
| **AWS IAM**             | Identity security assessment        |
| **Amazon S3**           | Storage security assessment         |
| **EC2 Security Groups** | Network exposure assessment         |
| **JavaScript**          | Frontend interaction                |
| **HTML/CSS**            | Dashboard interface                 |
| **ReportLab**           | PDF report generation               |
| **Pytest**              | Automated testing                   |

---

# 🛠️ Installation

## 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/Cloud-Sentinel.git
cd Cloud-Sentinel
```

---

## 2. Create a virtual environment

### Windows

```powershell
python -m venv venv
```

Activate it:

```powershell
.\venv\Scripts\Activate.ps1
```

---

## 3. Install dependencies

```powershell
pip install -r requirements.txt
```

---

# 🔐 AWS Configuration

CloudSentinel uses **Boto3** to communicate with AWS.

Make sure your AWS CLI is installed and authenticated before running a real AWS scan.

Verify your identity:

```bash
aws sts get-caller-identity
```

A successful response should contain your AWS identity information.

> ⚠️ **Never commit AWS access keys, secret keys, passwords, or other credentials to GitHub.**

CloudSentinel's AWS scanners should use the minimum permissions required for the security checks being performed.

---

# ▶️ Running the Application

CloudSentinel consists of a FastAPI backend and a lightweight frontend server.

## Start the Backend

From the project directory:

```powershell
python -m uvicorn backend.app:app --reload
```

The API will run at:

```text
http://127.0.0.1:8000
```

---

## Start the Frontend

Open another terminal:

```powershell
python -m http.server 5500 --directory frontend --bind 127.0.0.1
```

Then open:

```text
http://127.0.0.1:5500
```

---

# 🧪 Demo Mode

CloudSentinel includes a **Demo Scan** for testing and demonstration.

The Demo Scan uses predefined security findings and does **not modify or access your AWS environment**.

This allows the complete workflow to be demonstrated without AWS resources:

```text
Demo Scan
   ↓
Sample Findings
   ↓
Risk Assessment
   ↓
Security Score
   ↓
AI Recommendations
   ↓
Dashboard
```

---

# ☁️ AWS Scan

The **Scan AWS Account** feature performs an assessment using the authenticated AWS account.

The current scanner modules include:

```text
S3 Scanner
    ↓
IAM Scanner
    ↓
Security Group Scanner
    ↓
Risk Engine
    ↓
AI Advisor
    ↓
Security Report
```

The scanner is intended for **security assessment and read-only analysis** and should not modify AWS resources.

---

# 🧪 Running Tests

Run the test suite using:

```bash
pytest
```

For more detailed output:

```bash
pytest -v
```

---

# 🔒 Security Considerations

CloudSentinel is designed as a security assessment project and follows several important principles:

* 🔐 Do not hard-code AWS credentials
* 🔐 Avoid committing secrets to source control
* 👁️ Prefer read-only AWS permissions
* 🧩 Keep scanner modules separated by service
* 🧪 Test security logic independently
* 📊 Provide transparent risk scoring
* 📝 Provide actionable remediation guidance

---

# 🎯 Project Goals

The primary goals of CloudSentinel are to demonstrate practical knowledge of:

* Cloud security
* AWS security services
* IAM security
* Network security
* Security automation
* Python development
* REST API development
* Risk assessment
* Security reporting
* Automated testing

---

# 🔮 Future Improvements

Potential future enhancements include:

* [ ] Amazon EBS security checks
* [ ] CloudTrail configuration assessment
* [ ] RDS security assessment
* [ ] AWS Config integration
* [ ] CIS benchmark mapping
* [ ] More advanced IAM analysis
* [ ] Historical scan tracking
* [ ] Database-backed findings
* [ ] Authentication for the dashboard
* [ ] Docker deployment
* [ ] CI/CD security checks
* [ ] Cloud deployment
* [ ] Expanded test coverage

---

# 📸 Dashboard

> Add a screenshot of your CloudSentinel dashboard here after completing the final UI.

```text
docs/
└── dashboard.png
```

Then replace this section with:

```markdown
![CloudSentinel Dashboard](docs/dashboard.png)
```

---

# 📌 Disclaimer

CloudSentinel is an educational and internship portfolio project designed for authorized AWS security assessment.

Only use the scanner against AWS accounts and resources that you own or have explicit permission to assess.

---


