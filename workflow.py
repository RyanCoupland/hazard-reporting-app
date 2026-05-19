import streamlit as st


def clear_report_data():
    """
    Clears all session state variables related to the current hazard report.
    Used when the user cancels a report or returns to the home screen.
    """
    # List of all session state keys that store report data.
    # ensures fresh when creating a new report.
    report_keys = [
        "hazard_type",
        "location",
        "severity",
        "hazard_photo",
        "hazard_photo_input",
        "final_details",
        "final_details_input",
        "report_timestamp",
        "submitted_report_id",
        "selected_report_id",
        "editing_from_review",
    ]

    # Removes each key.
    for key in report_keys:
        st.session_state.pop(key, None)