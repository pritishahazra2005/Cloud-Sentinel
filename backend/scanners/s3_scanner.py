import boto3
from botocore.exceptions import ClientError


def scan_s3():
    findings = []

    s3 = boto3.client("s3")

    try:
        response = s3.list_buckets()

        for bucket in response.get("Buckets", []):
            bucket_name = bucket["Name"]

            # -------------------------
            # Public Access Protection
            # -------------------------

            try:
                config = s3.get_public_access_block(
                    Bucket=bucket_name
                )["PublicAccessBlockConfiguration"]

                protection_enabled = all([
                    config.get("BlockPublicAcls", False),
                    config.get("IgnorePublicAcls", False),
                    config.get("BlockPublicPolicy", False),
                    config.get("RestrictPublicBuckets", False)
                ])

                if not protection_enabled:
                    findings.append({
                        "service": "S3",
                        "resource": bucket_name,
                        "severity": "CRITICAL",
                        "title": "S3 Public Access Protection Disabled",
                        "description": (
                            "One or more S3 public access protection "
                            "controls are disabled."
                        )
                    })

            except ClientError:
                findings.append({
                    "service": "S3",
                    "resource": bucket_name,
                    "severity": "MEDIUM",
                    "title": "Unable to Check Public Access",
                    "description": (
                        "CloudSentinel could not retrieve the "
                        "bucket public access configuration."
                    )
                })

            # -------------------------
            # Encryption
            # -------------------------

            try:
                s3.get_bucket_encryption(
                    Bucket=bucket_name
                )

            except ClientError as error:

                code = error.response["Error"]["Code"]

                if code == "ServerSideEncryptionConfigurationNotFoundError":

                    findings.append({
                        "service": "S3",
                        "resource": bucket_name,
                        "severity": "HIGH",
                        "title": "S3 Encryption Not Configured",
                        "description": (
                            "Default server-side encryption is not "
                            "configured for this bucket."
                        )
                    })

    except Exception as error:

        findings.append({
            "service": "S3",
            "resource": "AWS Account",
            "severity": "HIGH",
            "title": "S3 Scanner Error",
            "description": str(error)
        })

    return findings