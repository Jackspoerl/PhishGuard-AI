import re

def analyze_email(text):
    findings = []
    urls = re.findall(r'https?://\S+', text)
    score = 0
    lower_text = text.lower()

    if urls:
        score += 15
        findings.append(f"Contains {len(urls)} URL(s)")

    suspicious_domains = [
        "micr0soft", "login-security", "account-verify", "secure-update",
        "paypal-security", "dropbox-share", "fileshare", "chase-security",
        "benefits-login", "payroll-update", "microsoft-support365"
    ]

    if any(pattern in url.lower() for url in urls for pattern in suspicious_domains):
        score += 25
        findings.append("Suspicious or lookalike domain detected")

    credential_words = [
        "login", "log in", "sign in", "verify your account",
        "password", "confirm identity", "verify your identity"
    ]

    if any(word in lower_text for word in credential_words):
        score += 25
        findings.append("Possible credential harvesting language detected")

    urgency_words = [
        "urgent", "immediately", "today", "within 24 hours",
        "within 30 minutes", "expires", "expired", "action required",
        "final notice"
    ]

    if any(word in lower_text for word in urgency_words):
        score += 15
        findings.append("Urgent or pressure-based language detected")

    threat_words = [
        "suspension", "suspended", "locked", "disabled",
        "lose access", "loss of coverage", "failure to respond",
        "failure to verify"
    ]

    if any(word in lower_text for word in threat_words):
        score += 15
        findings.append("Threatens negative consequences")

    financial_words = [
        "bank", "fraud", "payment", "payroll", "invoice",
        "billing", "credit card", "wire"
    ]

    if any(word in lower_text for word in financial_words):
        score += 15
        findings.append("Financial or payroll-related targeting detected")

    brand_words = [
        "microsoft", "amazon", "dropbox", "chase",
        "paypal", "linkedin", "apple"
    ]

    if any(word in lower_text for word in brand_words):
        score += 10
        findings.append("Brand or service impersonation indicators detected")

    score = min(score, 100)

    if score >= 85:
        classification = "Critical Risk"
    elif score >= 65:
        classification = "High Risk"
    elif score >= 40:
        classification = "Suspicious"
    elif score >= 20:
        classification = "Low Risk"
    else:
        classification = "Safe"

    return score, classification, findings, urls