# CloudSentinel 🔐

CloudSentinel is an AWS Cloud Security Posture Assessment platform designed to identify common cloud security misconfigurations across AWS services.

## Features

- S3 security assessment
- S3 public access protection checks
- S3 encryption checks
- IAM MFA assessment
- IAM active access key detection
- EC2 Security Group assessment
- Internet-exposed SSH detection
- Internet-exposed RDP detection
- Risk severity classification
- Automated security scoring
- Remediation recommendations
- Demo scanning mode
- AWS account scanning mode
- Web-based security dashboard
- PDF security reports
- Automated tests

## Architecture

```text
                CloudSentinel
                     |
                 FastAPI API
                     |
        +------------+------------+
        |            |            |
       S3           IAM          EC2
     Scanner      Scanner       Scanner
        |            |            |
        +------------+------------+
                     |
                Risk Engine
                     |
              Security Score
                     |
             Remediation Advisor
                     |
                Web Dashboard



Technology Stack
Python
FastAPI
Boto3
AWS
HTML5
CSS3
JavaScript
ReportLab
Pytest
Security Checks
Amazon S3

CloudSentinel checks:

S3 public access protection
Default server-side encryption
AWS IAM

CloudSentinel checks:

MFA configuration
Active IAM access keys
EC2 Security Groups

CloudSentinel checks:

Internet-exposed SSH
Internet-exposed RDP
Other unrestricted inbound access
Risk Scoring

CloudSentinel assigns points based on finding severity.