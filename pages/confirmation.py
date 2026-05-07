import streamlit as st

from styles import apply_global_styles, confirmation_styles
from workflow import clear_report_data


apply_global_styles()
confirmation_styles()


st.title("Report Submitted")
st.write("Thank you.")
st.write("Your report has been submitted successfully.")

hazard_type = st.session_state.get("hazard_type", "Not selected")
location = st.session_state.get("location", "Not selected")
severity = st.session_state.get("severity", "Not selected")
report_time = st.session_state.get("report_timestamp", "Not recorded")
photo_data = st.session_state.get("hazard_photo")
final_details = st.session_state.get("final_details", "").strip()

with st.container(key="review_summary"):
    st.write(f"Hazard type: {hazard_type}")
    st.write(f"Location: {location}")
    st.write(f"Severity: {severity}")
    st.write(f"Report time: {report_time}")

    if photo_data is not None:
        st.write("Photo: Photo provided")
    else:
        st.write("Photo: No photo provided")

    st.write(f"Additional information: {final_details if final_details else 'None provided'}")


if st.button("Return to Home", use_container_width=True, type="primary"):
    clear_report_data()
    st.switch_page("pages/home.py")