import streamlit as st

from styles import apply_global_styles, confirmation_styles
from workflow import clear_report_data
from database import update_report_details

apply_global_styles()
confirmation_styles()

st.title("Report Submitted")

# Get the report ID created on the review submission page
submitted_report_id = st.session_state.get("submitted_report_id")

# Confirmation message shown immediately after the report is saved
with st.container(key="submission_message"):
    st.subheader("Thank you.")
    st.write("Your hazard report has been submitted successfully.")

    if st.button("View Submitted Report", use_container_width=True, key="view_submitted_report"):
        if submitted_report_id:
            st.session_state.selected_report_id = submitted_report_id
            st.query_params["report_id"] = submitted_report_id
            st.switch_page("pages/report_details.py")
        else:
            st.warning("No submitted report found.")


# Optional details can be added after submission
with st.container(key="additional_information"):
    st.subheader("Additional Details")
    st.write("**Add any extra information or notes about the hazard (optional).**")

    additional_info = st.text_area(
        "Additional information",
        placeholder="Describe the hazard or add any relevant context",
        label_visibility="collapsed",
        key="additional_info_input",
        height=140,
    )

    if st.button("Update Report", use_container_width=True, type="primary", key="save_info"):
        if submitted_report_id:
            update_report_details(submitted_report_id, additional_info.strip())
            st.session_state.final_details = additional_info.strip()
            st.success("Report updated.")
        else:
            st.warning("No submitted report found.")


# Finish the workflow and return to the home screen
if st.button("Return to Home", use_container_width=True, key="return_home"):
    clear_report_data()
    st.switch_page("pages/home.py")