import streamlit as st
from datetime import datetime

from styles import apply_global_styles, apply_review_styles
from database import get_report_by_id, update_report_details


apply_global_styles()
apply_review_styles()


def format_report_time(submitted_time):
    """
    Converts the stored timestamp into a readable date/time format.
    """
    try:
        return datetime.fromisoformat(submitted_time).strftime("%d/%m/%Y %H:%M")
    except ValueError:
        return submitted_time


st.title("Report Details")


# Get the selected report ID from session state.
# If the page was refreshed, try to recover it from the URL.
selected_report_id = st.session_state.get("selected_report_id")

if not selected_report_id:
    selected_report_id = st.query_params.get("report_id")

if selected_report_id:
    st.session_state.selected_report_id = selected_report_id


# Stop the page if no report has been selected.
if not selected_report_id:
    st.warning("No report selected.")

    if st.button("Return to Saved Reports", use_container_width=True, type="primary"):
        st.switch_page("pages/saved_reports.py")

    st.stop()


# Load the selected report from the database.
report = get_report_by_id(selected_report_id)

if not report:
    st.warning("Report could not be found.")

    if st.button("Return to Saved Reports", use_container_width=True, type="primary"):
        st.switch_page("pages/saved_reports.py")

    st.stop()


# Match the order of fields returned by get_report_by_id().
report_id = report[0]
submitted_time = report[1]
hazard_type = report[2]
location = report[3]
severity = report[4]
final_details = report[5] or ""
photo_data = report[6]

display_time = format_report_time(submitted_time)
photo_status = "Photo provided" if photo_data is not None else "No photo provided"


# Main saved report summary
with st.container(key="review_summary"):
    st.write(f"Report ID: **{report_id}**")
    st.write(f"Hazard type: **{hazard_type}**")
    st.write(f"Location: **{location}**")
    st.write(f"Severity: **{severity}**")
    st.write(f"Report time: **{display_time}**")
    st.write(f"Photo: **{photo_status}**")
    st.write(f"Additional information: **{final_details if final_details else 'None provided'}**")


# Show the saved photo only if one was stored with the report.
if photo_data is not None:
    st.subheader("Saved Photo")
    st.image(photo_data, use_container_width=True)
else:
    st.info("No photo was saved with this report.")


# Allows additional written detail to be added or updated after submission.
with st.container(key="additional_information"):
    st.subheader("Add/Update additional information")
    st.write("Use this section to describe the hazard in more detail.")

    updated_details = st.text_area(
        "Additional information",
        value=final_details,
        placeholder="Describe the hazard in more detail.",
        label_visibility="collapsed",
        key="report_details_update_input",
        height=140,
    )

    if st.button("Update Report", use_container_width=True, type="primary", key="update_report_details"):
        update_report_details(report_id, updated_details.strip())
        st.success("Report updated.")
        st.rerun()


# Navigation buttons
if st.button("Return to Saved Reports", use_container_width=True, type="primary"):
    st.switch_page("pages/saved_reports.py")

if st.button("Return to Home", use_container_width=True):
    st.switch_page("pages/home.py")