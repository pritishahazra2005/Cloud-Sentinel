def check_public_buckets(buckets):
    findings = []
    for bucket in buckets:
        if not bucket["public_access_blocked"]:
            findings.append({
                "resource": bucket["name"],
                "severity": "CRITICAL",
                "issue": "S3 bucket is publicly accessible",
                "recommendation": "Enable Block Public Access on this bucket"
            })
    return findings