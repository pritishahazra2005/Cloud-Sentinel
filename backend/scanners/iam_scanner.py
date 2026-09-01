import boto3


def scan_iam():
    findings = []

    iam = boto3.client("iam")

    try:
        response = iam.list_users()

        for user in response.get("Users", []):

            username = user["UserName"]

            # -------------------------
            # MFA Check
            # -------------------------

            try:
                mfa_response = iam.list_mfa_devices(
                    UserName=username
                )

                mfa_devices = mfa_response.get(
                    "MFADevices",
                    []
                )

                if not mfa_devices:

                    findings.append({
                        "service": "IAM",
                        "resource": username,
                        "severity": "HIGH",
                        "title": "MFA Not Enabled",
                        "description": (
                            f"IAM user '{username}' does not "
                            "have MFA enabled."
                        )
                    })

            except Exception:
                pass

            # -------------------------
            # Access Key Check
            # -------------------------

            try:

                key_response = iam.list_access_keys(
                    UserName=username
                )

                keys = key_response.get(
                    "AccessKeyMetadata",
                    []
                )

                for key in keys:

                    if key["Status"] == "Active":

                        findings.append({
                            "service": "IAM",
                            "resource": username,
                            "severity": "MEDIUM",
                            "title": "Active IAM Access Key",
                            "description": (
                                f"User '{username}' has an "
                                "active programmatic access key."
                            )
                        })

            except Exception:
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