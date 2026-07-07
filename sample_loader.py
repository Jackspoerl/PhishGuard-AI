from pathlib import Path

from pathlib import Path

SAMPLE_EMAILS = {
    "LinkedIn Newsletter": Path("sample_emails/linkedin_newsletter.txt"),
    "Amazon Delivery Delay": Path("sample_emails/amazon_delivery_delay.txt"),
    "Payroll Update": Path("sample_emails/suspicious_payroll.txt"),
    "Microsoft Password Expiring": Path("sample_emails/microsoft_password_expiring.txt"),
    "Dropbox Shared Document": Path("sample_emails/dropbox_shared_document.txt"),
    "HR Benefits Enrollment": Path("sample_emails/hr_benefits_update.txt"),
    "Bank Fraud Alert": Path("sample_emails/bank_fraud_alert.txt"),
    "Microsoft Account Verification": Path("sample_emails/fake_microsoft.txt"),
}

def load_sample_email(sample_name):
    path = SAMPLE_EMAILS.get(sample_name)

    if path and path.exists():
        return path.read_text(encoding="utf-8", errors="ignore")

    return None

def load_sample_email(sample_name):
    path = SAMPLE_EMAILS.get(sample_name)

    if path and path.exists():
        return path.read_text(encoding="utf-8", errors="ignore")

    return None