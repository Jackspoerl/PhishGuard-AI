def build_timeline(email_text, sender, subject, urls, findings, score):
    timeline = []

    timeline.append("Email loaded successfully")
    timeline.append(f"Parsed sender: {sender}")
    timeline.append(f"Parsed subject: {subject}")

    if urls:
        timeline.append(f"Extracted {len(urls)} URL(s)")
    else:
        timeline.append("No URLs found")

    if findings:
        timeline.append(f"Rule engine detected {len(findings)} threat indicator(s)")
    else:
        timeline.append("Rule engine found no major threat indicators")

    timeline.append(f"Final risk score calculated: {score}/100")

    return timeline