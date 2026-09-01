import boto3
from botocore.exceptions import ClientError


def scan_iam():
    findings = []

    try:
        iam = boto3.client("iam")

        users = iam.list_users().get("Users", [])

        for user in users:
            username = user["UserName"]

            # Check MFA
            try:
                mfa_devices = iam.list_mfa_devices(
                    UserName=username
                ).get("MFADevices", [])

                if not mfa_devices:
                    findings.append({
                        "service": "IAM",
                        "resource": username,
                        "severity": "HIGH",
                        "title": "MFA Not Enabled",
                        "description": (
                            f"IAM user '{username}' does not have "
                            "a registered MFA device."
                        )
                    })

            except ClientError as error:
                findings.append({
                    "service": "IAM",
                    "resource": username,
                    "severity": "MEDIUM",
                    "title": "Unable to Verify MFA",
                    "description": str(error)
                })

            # Check access keys
            try:
                keys = iam.list_access_keys(
                    UserName=username
                ).get("AccessKeyMetadata", [])

                for key in keys:
                    if key["Status"] == "Active":
                        findings.append({
                            "service": "IAM",
                            "resource": username,
                            "severity": "MEDIUM",
                            "title": "Active Access Key Detected",
                            "description": (
                                f"User '{username}' has an active "
                                "programmatic access key."
                            )
                        })

            except ClientError:
                pass

    except Exception as error:
        findings.append({
            "service": "IAM",
            "resource": "AWS Account",
            "severity": "HIGH",
            "title": "IAM Scanner Error",
            "description": str(error)
        })

    return findings