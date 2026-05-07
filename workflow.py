import streamlit as st


def clear_report_data():
    report_keys = [
        "hazard_type",
        "location",
        "severity",
        "hazard_photo",
        "hazard_photo_input",
        "final_details",
        "final_details_input",
        "report_timestamp",
        "editing_from_review",
        "confirm_cancel",
    ]

    for key in report_keys:
        st.session_state.pop(key, None)
