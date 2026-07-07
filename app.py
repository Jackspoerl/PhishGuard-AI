from reports_page import render_reports_page
from history_page import render_history_page
from history import save_scan
from dashboard import render_dashboard
from pages import get_page
from styles import load_styles
from timeline import build_timeline
from parser import read_uploaded_file, parse_txt_email
from rules import analyze_email
from sample_loader import SAMPLE_EMAILS, load_sample_email
from ui import render_sidebar, render_header
import streamlit as st

st.set_page_config(
    page_title="PhishGuard AI",
    page_icon="assets/logo.png",
    layout="wide"
)

load_styles()
render_sidebar()
render_header()

page = st.session_state.get("page", "Dashboard")

if page == "Dashboard":
    render_dashboard()

elif page == "Analyze Email":
    uploaded_file = st.file_uploader(
        "Upload a .txt or .eml email file",
        type=["txt", "eml"]
    )

    sample_choice = st.selectbox(
        "Or choose a sample email",
        ["None"] + list(SAMPLE_EMAILS.keys())
    )

    email_text = None

    if uploaded_file:
        email_text = read_uploaded_file(uploaded_file)
    elif sample_choice != "None":
        email_text = load_sample_email(sample_choice)

    if email_text:
        sender, recipient, subject, date, body = parse_txt_email(email_text)
        score, classification, findings, urls = analyze_email(email_text)
        new_scan_saved = save_scan(sender, subject, score, classification, urls, email_text)

        if new_scan_saved:
            st.success("Email analyzed and saved to history.")
        else:
            st.info("This email was already scanned, so it was not added again.")
        timeline = build_timeline(email_text, sender, subject, urls, findings, score)

        st.success("Email analyzed successfully.")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.subheader("Risk Score")
            st.markdown(f"<div class='big-score'>{score}</div>", unsafe_allow_html=True)
            st.progress(score / 100)
            st.write(f"**{classification}**")
            st.markdown("</div>", unsafe_allow_html=True)

        with col2:
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.subheader("Threat Summary")
            if findings:
                for finding in findings:
                    st.markdown(f"<div class='threat'>⚠️ {finding}</div>", unsafe_allow_html=True)
            else:
                st.write("No major threats detected.")
            st.markdown("</div>", unsafe_allow_html=True)

        with col3:
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.subheader("Recommended Action")
            if score >= 60:
                st.error("Do NOT click links or provide personal information.")
                st.write("Report this email as phishing.")
            elif score >= 30:
                st.warning("Review carefully before interacting.")
            else:
                st.success("Email appears low risk.")
            st.markdown("</div>", unsafe_allow_html=True)

        with col4:
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.subheader("AI Analysis")
            if score >= 85:
                st.write("This email shows multiple signs of phishing, including suspicious links, urgent language, and possible brand impersonation.")
            elif score >= 60:
                st.write("This email contains several suspicious indicators and should be reviewed carefully before interacting.")
            elif score >= 30:
                st.write("This email has some warning signs, but more review is needed before labeling it as phishing.")
            else:
                st.write("This email appears low risk based on the current detection rules.")
            st.markdown("</div>", unsafe_allow_html=True)

        st.divider()

        left, right = st.columns([1, 2])

        with left:
            st.subheader("Email Details")
            st.write("**From:**", sender)
            st.write("**To:**", recipient)
            st.write("**Subject:**", subject)
            st.write("**Date:**", date)

        with right:
            st.subheader("Body Preview")
            st.text_area("Email Body", body, height=250)

        st.subheader("Links Found")
        if urls:
            for url in urls:
                st.code(url)
        else:
            st.write("No links found.")

        st.subheader("Analysis Timeline")

        for step in timeline:
            st.markdown(
                f"<div class='timeline-step'>✅ {step}</div>",
                unsafe_allow_html=True
            )

    else:
        st.info("Upload an email or choose a sample email to begin.")

elif page == "History":
    render_history_page()

elif page == "Reports":
    render_reports_page()
