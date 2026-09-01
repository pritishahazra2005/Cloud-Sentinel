"""
CloudSentinel AI Security Advisor

Generates remediation recommendations for
security findings detected by CloudSentinel.
"""


def generate_advice(finding):
    """
    Generate a security recommendation based
    on the finding severity and title.
    """

    title = finding.get("title", "").lower()
    service = finding.get("service", "").upper()
    severity = finding.get("severity", "").upper()

    # S3 recommendations
    if service == "S3":

        if "public access" in title:
            return (
                "Enable S3 Block Public Access settings and "
                "review bucket policies and ACLs to prevent "
                "unauthorized public access."
            )

        if "encryption" in title:
            return (
                "Enable server-side encryption for the S3 bucket "
                "using SSE-S3 or AWS KMS."
            )

        return (
            "Review the S3 bucket configuration and apply "
            "AWS recommended security controls."
        )

    # IAM recommendations
    if service == "IAM":

        if "mfa" in title:
            return (
                "Enable Multi-Factor Authentication (MFA) for "
                "the IAM identity to reduce the risk of "
                "credential compromise."
            )

        return (
            "Review IAM permissions and follow the principle "
            "of least privilege."
        )

    # EC2 / Security Group recommendations
    if service in ["EC2", "SECURITY GROUP"]:

        if "ssh" in title:
            return (
                "Restrict SSH access to trusted IP addresses "
                "or a VPN instead of allowing port 22 from "
                "0.0.0.0/0."
            )

        return (
            "Review security group inbound rules and remove "
            "unnecessary internet exposure."
        )

    # Severity-based fallback
    if severity == "CRITICAL":
        return (
            "Address this finding immediately because it "
            "represents a critical security risk."
        )

    if severity == "HIGH":
        return (
            "Prioritize remediation of this high-risk finding "
            "to reduce the attack surface."
        )

    if severity == "MEDIUM":
        return (
            "Review and remediate this finding as part of "
            "regular cloud security maintenance."
        )

    return (
        "Review this finding and apply appropriate AWS "
        "security best practices."
    )