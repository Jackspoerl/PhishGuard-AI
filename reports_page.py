from report_generator import generate_security_report
import streamlit as st
from history import load_history

def render_reports_page():
    st.subheader("Threat Reports")

    history = load_history()

    if not history:
        st.info("No scan data available yet. Analyze emails first.")
        return

    total_scans = len(history)
    critical = sum(1 for scan in history if scan["score"] >= 85)
    high = sum(1 for scan in history if 60 <= scan["score"] < 85)
    suspicious = sum(1 for scan in history if 30 <= scan["score"] < 60)
    safe = sum(1 for scan in history if scan["score"] < 30)

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.write("### Report Summary")
    st.write(f"**Total Emails Scanned:** {total_scans}")
    st.write(f"**Critical Threats:** {critical}")
    st.write(f"**High Risk Emails:** {high}")
    st.write(f"**Suspicious Emails:** {suspicious}")
    st.write(f"**Safe Emails:** {safe}")
    st.markdown("</div>", unsafe_allow_html=True)

    st.divider()

    st.write("### Analyst Notes")

    if critical > 0:
        st.error("Critical phishing activity has been detected. Immediate review is recommended.")
    elif high > 0 or suspicious > 0:
        st.warning("Some suspicious activity was found. Review flagged emails carefully.")
    else:
        st.success("No major threats detected in the current scan history.")

    st.divider()

    st.write("### Generate PDF Report")

    if st.button("Generate Security Report"):
        report_path = generate_security_report()

        with open(report_path, "rb") as file:
            st.download_button(
                label="Download PDF Report",
                data=file,
                file_name="phishguard_ai_security_report.pdf",
                mime="application/pdf"
            )