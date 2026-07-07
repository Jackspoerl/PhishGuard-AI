import streamlit as st

def get_page():

    if "page" not in st.session_state:
        st.session_state.page = "Dashboard"

    return st.session_state.page