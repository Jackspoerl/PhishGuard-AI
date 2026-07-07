import streamlit as st
import hashlib
from datetime import datetime


def create_fingerprint(email_text):
    normalized_text = email_text.strip().replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(normalized_text.encode("utf-8")).hexdigest()


def load_history():
    if "scan_history" not in st.session_state:
        st.session_state.scan_history = []
    return st.session_state.scan_history


def save_scan(sender, subject, score, classification, urls, email_text):
    history = load_history()
    fingerprint = create_fingerprint(email_text)

    for scan in history:
        if scan["fingerprint"] == fingerprint:
            return False

    history.append({
        "time": datetime.now().strftime("%Y-%m-%d %I:%M %p"),
        "sender": sender,
        "subject": subject,
        "score": score,
        "classification": classification,
        "url_count": len(urls),
        "fingerprint": fingerprint
    })

    return True
