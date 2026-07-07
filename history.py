import json
import hashlib
from pathlib import Path
from datetime import datetime

HISTORY_FILE = Path("scan_history.json")


def load_history():
    if HISTORY_FILE.exists():
        return json.loads(HISTORY_FILE.read_text())
    return []


def create_fingerprint(email_text):
    normalized_text = email_text.strip().replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(normalized_text.encode("utf-8")).hexdigest()


def save_scan(sender, subject, score, classification, urls, email_text):
    history = load_history()
    fingerprint = create_fingerprint(email_text)

    for scan in history:
        if scan.get("fingerprint") == fingerprint:
            return False

    scan = {
        "time": datetime.now().strftime("%Y-%m-%d %I:%M %p"),
        "sender": sender,
        "subject": subject,
        "score": score,
        "classification": classification,
        "url_count": len(urls),
        "fingerprint": fingerprint
    }

    history.append(scan)
    HISTORY_FILE.write_text(json.dumps(history, indent=4))
    return True