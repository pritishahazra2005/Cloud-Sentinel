SEVERITY_POINTS = {
    "CRITICAL": 25,
    "HIGH": 15,
    "MEDIUM": 8,
    "LOW": 3
}


def calculate_score(findings):

    total_risk = 0

    counts = {
        "CRITICAL": 0,
        "HIGH": 0,
        "MEDIUM": 0,
        "LOW": 0
    }

    for finding in findings:

        severity = finding.get(
            "severity",
            "LOW"
        )

        total_risk += SEVERITY_POINTS.get(
            severity,
            0
        )

        if severity in counts:
            counts[severity] += 1

    score = max(
        0,
        100 - total_risk
    )

    if score >= 90:
        rating = "Excellent"

    elif score >= 75:
        rating = "Good"

    elif score >= 50:
        rating = "Needs Improvement"

    else:
        rating = "Critical Risk"

    return {
        "score": score,
        "rating": rating,
        "counts": counts,
        "total_findings": len(findings)
    }