import streamlit as st

def load_styles():
    st.markdown("""
    <style>

    .stApp {
        background-color: #0b1220;
        color: white;
    }

    .card {
        background-color: #111827;
        padding: 24px;
        border-radius: 16px;
        border: 1px solid #263244;
        box-shadow: 0 4px 20px rgba(0,0,0,0.25);
    }

    .big-score {
        font-size: 64px;
        font-weight: 800;
        text-align: center;
    }

    .threat {
        background-color: #1f2937;
        padding: 12px;
        border-radius: 10px;
        margin-bottom: 10px;
    }

    .timeline-step {
        background-color: #111827;
        border-left: 4px solid #27B5FF;
        padding: 14px 18px;
        margin-bottom: 12px;
        border-radius: 10px;
    }

    .metric-card {
        background: linear-gradient(135deg, #111827, #0f172a);
        padding: 22px;
        border-radius: 16px;
        border: 1px solid #263244;
        box-shadow: 0 4px 20px rgba(0,0,0,0.25);
        min-height: 130px;
        transition: 0.25s;
    }

    .metric-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 8px 28px rgba(39,181,255,.25);
    }

    .metric-icon {
        font-size: 28px;
        margin-bottom: 10px;
    }

    .metric-title {
        color: #94a3b8;
        font-size: 15px;
        margin-bottom: 10px;
    }

    .metric-value {
        color: white;
        font-size: 42px;
        font-weight: 800;
    }

    .scan-row {
        padding: 14px 16px;
        border-radius: 10px;
        margin-bottom: 12px;
        background-color: #1f2937;
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-weight: 600;
    }

    .scan-row span {
        color: #94a3b8;
    }

    .critical {
        border-left: 5px solid #ef4444;
    }

    .high {
        border-left: 5px solid #f97316;
    }

    .suspicious {
        border-left: 5px solid #eab308;
    }

    .safe {
        border-left: 5px solid #22c55e;
    }

    /* Streamlit Buttons */

    .stButton > button {
        width: 100%;
        background: linear-gradient(90deg, #1E88E5, #27B5FF);
        color: white !important;
        border: none;
        border-radius: 12px;
        padding: 0.7rem 1.2rem;
        font-size: 18px;
        font-weight: 700;
        transition: all 0.25s ease;
        box-shadow: 0 4px 14px rgba(39,181,255,.25);
    }

    .stButton > button:hover {
        background: linear-gradient(90deg, #1976D2, #2196F3);
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(39,181,255,.4);
        color: white !important;
    }

    .stButton > button:focus {
        outline: none;
        border: none;
        color: white !important;
    }

    .stButton > button p {
        color: white !important;
    }

    /* Download Button */

    .stDownloadButton > button {
        width: 100%;
        background: linear-gradient(90deg, #1E88E5, #27B5FF);
        color: white !important;
        border: none;
        border-radius: 12px;
        padding: 0.7rem 1.2rem;
        font-size: 18px;
        font-weight: 700;
        transition: all 0.25s ease;
        box-shadow: 0 4px 14px rgba(39,181,255,.25);
    }

    .stDownloadButton > button:hover {
        background: linear-gradient(90deg, #1976D2, #2196F3);
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(39,181,255,.4);
        color: white !important;
    }

    .stDownloadButton > button p {
        color: white !important;
    }

    </style>
    """, unsafe_allow_html=True)