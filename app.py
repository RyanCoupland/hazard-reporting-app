import streamlit as st

from database import init_db

st.set_page_config(
    page_title="Hazard Reporter",
    page_icon="⚠️",
    layout="centered",
    initial_sidebar_state="collapsed",
)

init_db()

pages = {
    "Main": [
        st.Page("pages/home.py", title="Home", icon="🏠", default=True),
        st.Page("pages/report_hazard.py", title="Report Hazard", icon="🚨"),
    ],
    "Reports": [
        st.Page("pages/saved_reports.py", title="Saved Reports", icon="📋"),
        st.Page("pages/report_details.py", title="Report Details"),
    ],
    "Settings": [
        st.Page("pages/settings.py", title="Settings", icon="⚙️"),
    ],
    "Workflow": [
        st.Page("pages/hazard_location.py", title="Hazard Location"),
        st.Page("pages/hazard_details.py", title="Hazard Details"),
        st.Page("pages/review_submission.py", title="Review Submission"),
        st.Page("pages/confirmation.py", title="Confirmation"),
    ],
}

pg = st.navigation(pages, position="hidden")
pg.run()