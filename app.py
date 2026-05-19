import streamlit as st

from database import init_db

# Configure page settings.
st.set_page_config(
    page_title="Hazard Reporter",
    page_icon="⚠️",
    layout="centered",
    initial_sidebar_state="collapsed",   # Sidebar hidden because navigation is handled manually
)

# Initialises the database and create tables if they don't exist.
init_db()

# Define all pages in the application.
pages = [
    st.Page("pages/home.py", title="Home", default=True),
    st.Page("pages/report_hazard.py", title="Report Hazard"),
    st.Page("pages/hazard_location.py", title="Hazard Location"),
    st.Page("pages/hazard_details.py", title="Hazard Details"),
    st.Page("pages/review_submission.py", title="Review Submission"),
    st.Page("pages/confirmation.py", title="Confirmation"),
    st.Page("pages/saved_reports.py", title="Saved Reports"),
    st.Page("pages/report_details.py", title="Report Details"),
    st.Page("pages/settings.py", title="Settings"),
]

# Create the navigation object with the sidebar hidden.
pg = st.navigation(pages, position="hidden")

# Run the selected page.
pg.run()
