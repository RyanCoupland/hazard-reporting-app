import streamlit as st

from styles import apply_global_styles, confirmation_styles
from database import get_report_by_id


apply_global_styles()
confirmation_styles()


st.title("Report Details")

selected_report_id = st.session_state.get("selected_report_id")

if not selected_report_id:
    st.warning("No report selected.")

    if st.button("Return to Saved Reports", use_container_width=True, type="primary"):
        st.switch_page("pages/saved_reports.py")

else:
    report = get_report_by_id(selected_report_id)

    if not report:
        st.warning("Report could not be found.")

        if st.button("Return to Saved Reports", use_container_width=True, type="primary"):
            st.switch_page("pages/saved_reports.py")

    else:
        report_id = report[0]
        submitted_time = report[1]
        hazard_type = report[2]
        location = report[3]
        severity = report[4]
        final_details = report[5]
        photo_attached = report[6]
        photo_data = report[7]

        with st.container(key="review_summary"):
            st.write(f"Report ID: {report_id}")
            st.write(f"Hazard type: {hazard_type}")
            st.write(f"Location: {location}")
            st.write(f"Severity: {severity}")
            st.write(f"Report time: {submitted_time}")
            st.write(f"Photo: {photo_attached}")
            st.write(f"Additional information: {final_details if final_details else 'None provided'}")

        if photo_data:
            st.image(photo_data, use_container_width=True)

        if st.button("Return to Saved Reports", use_container_width=True, type="primary"):
            st.switch_page("pages/saved_reports.py")

        if st.button("Return to Home", use_container_width=True):
            st.switch_page("pages/home.py")