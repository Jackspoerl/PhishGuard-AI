import streamlit as st
import pandas as pd
from history import load_history

def render_history_page():
    st.subheader("Scan History")

    history = load_history()

    if not history:
        st.info("No scan history yet. Analyze an email first.")
        return

    df = pd.DataFrame(history)

    df = df[[
        "time",
        "sender",
        "subject",
        "score",
        "classification",
        "url_count"
    ]]

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )