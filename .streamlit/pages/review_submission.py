import streamlit as st
from datetime import datetime
from uuid import uuid4

from styles import apply_global_styles, apply_review_styles, show_step_bar
from workflow import clear_report_data
from database import save_report


apply_global_styles()
apply_review_styles()


def format_report_time(submitted_time):
    """
    Converts the stored ISO timestamp into a readable display format.
    """
    try:
        return datetime.fromisoformat(submitted_time).strftime("%d/%m/%Y %H:%M")
    except ValueError:
        return submitted_time


def return_to_edit_page(page_path):
    """
    Sends the user back to a previous workflow page to change part of the report.
    """
    st.session_state.editing_from_review = True
    st.switch_page(page_path)


# Page title and progress indicator
st.title("Review Report")
st.write("Step 4 of 4")
show_step_bar(4)


# Get the report information collected from earlier workflow steps
hazard_type = st.session_state.get("hazard_type", "Not selected")
location = st.session_state.get("location", "Not selected")
severity = st.session_state.get("severity", "Not selected")
photo_data = st.session_state.get("hazard_photo")


# Create the timestamp once so it does not change every time the page reruns
if "report_timestamp" not in st.session_state:
    st.session_state.report_timestamp = datetime.now().isoformat(timespec="minutes")


display_time = format_report_time(st.session_state.report_timestamp)
photo_status = "Photo provided" if photo_data is not None else "No photo provided"


# Summary card shown before final submission
with st.container(key="review_summary"):
    st.subheader("Report Summary")
    st.write(f"Hazard type: **{hazard_type}**")
    st.write(f"Location: **{location}**")
    st.write(f"Severity: **{severity}**")
    st.write(f"Report time: **{display_time}**")
    st.write(f"Photo: **{photo_status}**")


# Show the captured photo only if one was provided
if photo_data is not None:
    st.subheader("Photo Preview")
    st.image(photo_data, use_container_width=True)


# Final check before saving the report
with st.container(key="confirm_check"):
    st.subheader("Is this information correct?")
    st.write("Please review the information above and confirm it is accurate.")

    with st.expander("Edit Report"):
        edit_options = [
            ("Change Hazard Type", "pages/report_hazard.py", "edit_hazard_type"),
            ("Change Location", "pages/hazard_location.py", "edit_location"),
            ("Change Severity/Photo", "pages/hazard_details.py", "edit_details"),
        ]

        for label, page_path, button_key in edit_options:
            if st.button(label, use_container_width=True, key=button_key):
                return_to_edit_page(page_path)


# Save the report to the database and move to the confirmation screen
if st.button("Submit Report", use_container_width=True, type="primary"):
    report = {
        "report_id": f"HR-{uuid4().hex[:8].upper()}",
        "submitted_time": st.session_state.report_timestamp,
        "hazard_type": hazard_type,
        "location": location,
        "severity": severity,
        "final_details": None,
        "photo_data": photo_data,
    }

    save_report(report)

    st.session_state.submitted_report_id = report["report_id"]
    st.switch_page("pages/confirmation.py")


# Cancel clears the current report data and exits the reporting workflow
if st.button("Cancel Report", use_container_width=True):
    clear_report_data()
    st.switch_page("pages/home.py")
