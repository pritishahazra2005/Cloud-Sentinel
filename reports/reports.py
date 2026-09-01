from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet


def generate_report(scan_data, filename="reports/cloudsentinel_report.pdf"):

    document = SimpleDocTemplate(
        filename,
        pagesize=A4
    )

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "CloudSentinel Security Assessment Report",
            styles["Title"]
        )
    )

    content.append(
        Spacer(1, 20)
    )

    security = scan_data["security"]

    content.append(
        Paragraph(
            f"Security Score: {security['score']}/100",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            f"Security Rating: {security['rating']}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Scan Mode: {scan_data['mode']}",
            styles["Normal"]
        )
    )

    content.append(
        Spacer(1, 20)
    )

    data = [
        ["Severity", "Count"],
        ["Critical", security["counts"]["CRITICAL"]],
        ["High", security["counts"]["HIGH"]],
        ["Medium", security["counts"]["MEDIUM"]],
        ["Low", security["counts"]["LOW"]]
    ]

    table = Table(data)

    table.setStyle(
        TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.darkblue),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("GRID", (0, 0), (-1, -1), 1, colors.grey),
            ("PADDING", (0, 0), (-1, -1), 8)
        ])
    )

    content.append(table)

    content.append(
        Spacer(1, 25)
    )

    content.append(
        Paragraph(
            "Security Findings",
            styles["Heading2"]
        )
    )

    for finding in scan_data["findings"]:

        content.append(
            Paragraph(
                f"<b>{finding['severity']}: "
                f"{finding['title']}</b>",
                styles["Heading3"]
            )
        )

        content.append(
            Paragraph(
                f"Service: {finding['service']}<br/>"
                f"Resource: {finding['resource']}<br/>"
                f"Description: {finding['description']}<br/>"
                f"Recommendation: "
                f"{finding.get('recommendation', 'Review resource.')}",
                styles["Normal"]
            )
        )

        content.append(
            Spacer(1, 15)
        )

    document.build(content)

    return filename