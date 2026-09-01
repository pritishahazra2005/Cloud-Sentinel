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



