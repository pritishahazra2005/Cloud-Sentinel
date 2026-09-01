from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.scanners.s3_scanner import scan_s3
from backend.scanners.iam_scanner import scan_iam
from backend.scanners.security_group_scanner import scan_security_groups

from backend.risk.risk_engine import calculate_score
from backend.ai.advisor import generate_advice


# ============================================================
# CloudSentinel FastAPI Application
# ============================================================

app = FastAPI(
    title="CloudSentinel",
    description="AWS Cloud Security Posture Assessment Platform",
    version="1.0.0"
)


# ============================================================
# CORS Configuration
# ============================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================================
# Demo Findings
# ============================================================

def demo_findings():

    return [

        {
            "service": "S3",
            "resource": "customer-data-demo",
            "severity": "CRITICAL",
            "title": "S3 Public Access Protection Disabled",
            "description": (
                "Public access protection is not completely enabled."
            )
        },

        {
            "service": "IAM",
            "resource": "developer-demo",
            "severity": "HIGH",
            "title": "MFA Not Enabled",
            "description": (
                "The IAM user does not have MFA enabled."
            )
        },

        {
            "service": "EC2",
            "resource": "sg-demo123",
            "severity": "CRITICAL",
            "title": "SSH Exposed to Internet",
            "description": (
                "Port 22 is accessible from 0.0.0.0/0."
            ),
            "port": "22",
            "protocol": "tcp"
        },

        {
            "service": "S3",
            "resource": "logs-demo",
            "severity": "MEDIUM",
            "title": "S3 Encryption Not Configured",
            "description": (
                "Default server-side encryption is not configured."
            )
        }
    ]


# ============================================================
# Root Endpoint
# ============================================================

@app.get("/")
def root():

    return {
        "application": "CloudSentinel",
        "status": "running",
        "version": "1.0.0"
    }


# ============================================================
# Demo Scan Endpoint
# ============================================================

@app.get("/api/demo-scan")
def demo_scan():

    findings = demo_findings()

    for finding in findings:

        finding["recommendation"] = generate_advice(
            finding
        )

    security = calculate_score(
        findings
    )

    return {
        "mode": "DEMO",
        "security": security,
        "findings": findings
    }


# ============================================================
# AWS Scan Endpoint
# ============================================================

@app.get("/api/aws-scan")
def aws_scan():

    findings = []

    findings.extend(
        scan_s3()
    )

    findings.extend(
        scan_iam()
    )

    findings.extend(
        scan_security_groups()
    )

    for finding in findings:

        finding["recommendation"] = generate_advice(
            finding
        )

    security = calculate_score(
        findings
    )

    return {
        "mode": "AWS",
        "security": security,
        "findings": findings
    }