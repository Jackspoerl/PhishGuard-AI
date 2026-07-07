import plotly.graph_objects as go
import pandas as pd
import streamlit as st
from history import load_history

def get_risk_class(score):
    if score >= 85:
        return "critical"
    elif score >= 60:
        return "high"
    elif score >= 30:
        return "suspicious"
    else:
        return "safe"

def render_metric_card(title, value, icon, color):
    st.markdown(
        f"""
        <div class="metric-card" style="border-left: 5px solid {color};">
            <div class="metric-icon">{icon}</div>
            <div class="metric-title">{title}</div>
            <div class="metric-value">{value}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

def render_dashboard():
    history = load_history()

    critical_count = sum(1 for scan in history if scan["score"] >= 85)
    high_count = sum(1 for scan in history if 60 <= scan["score"] < 85)
    suspicious_count = sum(1 for scan in history if 30 <= scan["score"] < 60)
    safe_count = sum(1 for scan in history if scan["score"] < 30)

    st.subheader("Security Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        render_metric_card("Critical Threats", critical_count, "🔴", "#ef4444")

    with col2:
        render_metric_card("High Risk", high_count, "🟠", "#f97316")

    with col3:
        render_metric_card("Suspicious", suspicious_count, "🟡", "#eab308")

    with col4:
        render_metric_card("Safe Emails", safe_count, "🟢", "#22c55e")

    if history:
        st.subheader("Threat Distribution")

        labels = ["Critical", "High Risk", "Suspicious", "Safe"]
        values = [critical_count, high_count, suspicious_count, safe_count]
        colors = ["#ef4444", "#f97316", "#eab308", "#22c55e"]

        fig = go.Figure(
            data=[
                go.Pie(
                    labels=labels,
                    values=values,
                    hole=0.58,
                    marker=dict(colors=colors),
                    textinfo="label+percent",
                    textfont=dict(
                        color="white",
                        size=18
                    ),
                    hoverinfo="label+value+percent"
                )
            ]
        )

        fig.update_layout(
            paper_bgcolor="#0b1220",
            plot_bgcolor="#0b1220",
            font=dict(color="white"),
            height=420,
            margin=dict(t=30, b=30, l=30, r=30),
            showlegend=True,
            legend=dict(
                orientation="h",
                y=-0.08,
                x=0.5,
                xanchor="center",
                font=dict(
                    color="white",
                    size=18
                )
            )
        )

        st.plotly_chart(fig, use_container_width=True)

    st.divider()

    left, right = st.columns([2, 1])

    with left:
        st.subheader("Recent Scans")

        if history:
            recent_scans = history[-5:][::-1]

            st.markdown("<div class='card'>", unsafe_allow_html=True)

            for scan in recent_scans:
                risk_class = get_risk_class(scan["score"])

                st.markdown(
                    f"""
                    <div class="scan-row {risk_class}">
                        <div>
                            <b>{scan["subject"]}</b><br>
                            <span>{scan["sender"]}</span>
                        </div>
                        <div>
                            {scan["classification"]} • {scan["score"]}/100
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            st.markdown("</div>", unsafe_allow_html=True)

        else:
            st.info("No scans yet. Go to Analyze Email to scan your first message.")

    with right:
        st.subheader("System Status")
        st.markdown("""
        <div class="card">
            <p>🟢 Rule Engine: Active</p>
            <p>🟡 AI Analysis: Preview Mode</p>
            <p>🟢 Email Parser: Online</p>
            <p>🔵 Dashboard: Live Data</p>
        </div>
        """, unsafe_allow_html=True)