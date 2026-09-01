from backend.risk.risk_engine import calculate_score


def test_no_findings():

    result = calculate_score([])

    assert result["score"] == 100
    assert result["total_findings"] == 0


def test_critical_finding():

    findings = [
        {
            "severity": "CRITICAL"
        }
    ]

    result = calculate_score(findings)

    assert result["score"] == 75
    assert result["counts"]["CRITICAL"] == 1


def test_multiple_findings():

    findings = [
        {
            "severity": "HIGH"
        },
        {
            "severity": "MEDIUM"
        },
        {
            "severity": "LOW"
        }
    ]

    result = calculate_score(findings)

    assert result["total_findings"] == 3
    assert result["counts"]["HIGH"] == 1
    assert result["counts"]["MEDIUM"] == 1
    assert result["counts"]["LOW"] == 1