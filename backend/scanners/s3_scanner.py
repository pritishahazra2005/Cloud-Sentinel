import boto3
from botocore.exceptions import ClientError


def scan_s3():
    findings = []

    try:
        s3 = boto3.client("s3")
        buckets = s3.list_buckets().get("Buckets", [])

        for bucket in buckets:
            name = bucket["Name"]

            # Check public access block
            try:
                public_block = s3.get_public_access_block(
                    Bucket=name
                )["PublicAccessBlockConfiguration"]

                all_blocked = all([
                    public_block.get("BlockPublicAcls", False),
                    public_block.get("IgnorePublicAcls", False),
                    public_block.get("BlockPublicPolicy", False),
                    public_block.get("RestrictPublicBuckets", False)
                ])

                if not all_blocked:
                    findings.append({
                        "service": "S3",
                        "resource": name,
                        "severity": "CRITICAL",
                        "title": "S3 Public Access Protection Disabled",
                        "description": (
                            "The bucket does not have all S3 public access "
                            "protection controls enabled."
                        )
                    })

            except ClientError:
                findings.append({
                    "service": "S3",
                    "resource": name,
                    "severity": "HIGH",
                    "title": "Unable to Verify S3 Public Access",
                    "description": (
                        "The application could not verify the bucket's "
                        "public access configuration."
                    )
                })

            # Check encryption
            try:
                s3.get_bucket_encryption(Bucket=name)

            except ClientError as error:
                if error.response["Error"]["Code"] == "ServerSideEncryptionConfigurationNotFoundError":
                    findings.append({
                        "service": "S3",
                        "resource": name,
                        "severity": "HIGH",
                        "title": "S3 Bucket Encryption Disabled",
                        "description": (
                            "The bucket does not appear to have default "
                            "server-side encryption configured."
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