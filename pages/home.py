import streamlit as st

from styles import apply_global_styles, apply_home_styles
from workflow import clear_report_data


apply_global_styles()
apply_home_styles()

st.title("HAZARD REPORTER")
st.subheader("SELECT AN OPTION")

if st.button(
    "REPORT A HAZARD",
    type="primary",
    use_container_width=True,
):
    clear_report_data()
    st.switch_page("pages/report_hazard.py")

if st.button(
    "VIEW REPORTS",
    type="secondary",
    use_container_width=True,
):
    st.switch_page("pages/saved_reports.py")

if st.button(
    "SETTINGS",
    type="secondary",
    use_container_width=True,
):
    st.switch_page("pages/settings.py")