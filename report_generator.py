from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime
from pathlib import Path
from history import load_history

REPORTS_DIR = Path("reports")
REPORTS_DIR.mkdir(exist_ok=True)

def generate_security_report():
    history = load_history()
    file_path = REPORTS_DIR / "phishguard_ai_security_report.pdf"

    doc = SimpleDocTemplate(
        str(file_path),
        pagesize=letter,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()
    elements = []

    elements.append(Paragraph("PhishGuard AI Security Report", styles["Title"]))
    elements.append(Paragraph(
        f"Generated: {datetime.now().strftime('%Y-%m-%d %I:%M %p')}",
        styles["Normal"]
    ))
    elements.append(Spacer(1, 20))

    total = len(history)
    critical = sum(1 for scan in history if scan["score"] >= 85)
    high = sum(1 for scan in history if 60 <= scan["score"] < 85)
    suspicious = sum(1 for scan in history if 30 <= scan["score"] < 60)
    safe = sum(1 for scan in history if scan["score"] < 30)

    elements.append(Paragraph("Executive Summary", styles["Heading2"]))

    summary_data = [
        ["Metric", "Count"],
        ["Total Emails Scanned", total],
        ["Critical Threats", critical],
        ["High Risk Emails", high],
        ["Suspicious Emails", suspicious],
        ["Safe Emails", safe],
    ]

    summary_table = Table(summary_data, colWidths=[300, 120])
    summary_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#0b1220")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("PADDING", (0, 0), (-1, -1), 8),
    ]))

    elements.append(summary_table)
    elements.append(Spacer(1, 25))

    elements.append(Paragraph("Recent Scans", styles["Heading2"]))

    scan_data = [["Time", "Sender", "Subject", "Score", "Classification"]]

    for scan in history[-25:][::-1]:
        scan_data.append([
            scan.get("time", ""),
            scan.get("sender", "")[:28],
            scan.get("subject", "")[:38],
            f"{scan.get('score', 0)}/100",
            scan.get("classification", "")
        ])

    scan_table = Table(scan_data, colWidths=[95, 125, 170, 60, 90])
    scan_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#0b1220")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("GRID", (0, 0), (-1, -1), 0.4, colors.lightgrey),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 8),
        ("PADDING", (0, 0), (-1, -1), 5),
    ]))

    elements.append(scan_table)
    elements.append(Spacer(1, 25))

    elements.append(Paragraph("Recommendations", styles["Heading2"]))

    recommendations = [
        "Do not click links in suspicious emails.",
        "Verify sender domains before responding.",
        "Report suspected phishing emails to security teams.",
        "Use multi-factor authentication when available.",
        "Train users to recognize urgency-based phishing tactics."
    ]

    for rec in recommendations:
        elements.append(Paragraph(f"• {rec}", styles["Normal"]))
        elements.append(Spacer(1, 6))

    doc.build(elements)

    return file_path