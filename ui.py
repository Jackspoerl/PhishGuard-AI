import streamlit as st

def nav_button(icon, page_name, current_page):
    active = current_page == page_name

    if active:
        st.markdown(
            f"""
            <div style="
                background: linear-gradient(90deg, #007BFF, #27B5FF);
                color: white;
                padding: 12px 16px;
                border-radius: 10px;
                font-weight: 700;
                margin-bottom: 8px;
            ">
                {icon} &nbsp; {page_name}
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        if st.button(
            f"{icon}  {page_name}",
            key=page_name,
            use_container_width=True
        ):
            st.session_state.page = page_name
            st.rerun()


def render_sidebar():
    with st.sidebar:
        st.image("assets/logo.png", width=210)

        st.markdown("""
        <h2 style="text-align:center;">
        PhishGuard <span style="color:#27B5FF;">AI</span>
        </h2>
        """, unsafe_allow_html=True)

        st.caption("AI-Powered Email Threat Detection")
        st.divider()

        current = st.session_state.get("page", "Dashboard")

        nav_button("🏠", "Dashboard", current)
        nav_button("📧", "Analyze Email", current)
        nav_button("📊", "History", current)
        nav_button("📄", "Reports", current)

        st.divider()
        st.caption("Version 1.0")


def render_header():
    col1, col2 = st.columns([1.2, 5.8])

    with col1:
        st.image("assets/logo.png", width=150)

    with col2:
        st.markdown("""
        <h1 style="margin-bottom:0px;">
        PhishGuard <span style="color:#27B5FF;">AI</span>
        </h1>

        <p style="color:#94A3B8;font-size:20px;">
        AI-Powered Email Threat Detection Platform
        </p>
        """, unsafe_allow_html=True)