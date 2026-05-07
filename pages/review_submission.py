import streamlit as st
from datetime import datetime
from uuid import uuid4

from styles import apply_global_styles, apply_review_styles
from workflow import clear_report_data
from database import save_report


apply_global_styles()
apply_review_styles()


st.title("Review Report")
st.write("Step 4 of 4")

hazard_type = st.session_state.get("hazard_type", "Not selected")
location = st.session_state.get("location", "Not selected")
severity = st.session_state.get("severity", "Not selected")
photo = st.session_state.get("hazard_photo")

if "report_timestamp" not in st.session_state:
    st.session_state.report_timestamp = datetime.now().strftime("%d/%m/%Y %H:%M")

with st.container(key="review_summary"):
    st.write(f"Hazard type: {hazard_type}")
    st.write(f"Location: {location}")
    st.write(f"Severity: {severity}")
    st.write(f"Report time: {st.session_state.report_timestamp}")
    st.write(f"Photo: {'Photo provided' if photo else 'No photo provided'}")

if photo:
    st.image(photo, use_container_width=True)

st.write("Provide additional information (optional)")

final_details_input = st.text_area(
    "Final details",
    placeholder="Add any extra information here if needed.",
    key="final_details_input",
    label_visibility="collapsed",
)

st.write("Need to change something?")

if st.button("Edit Hazard Type", use_container_width=True, key="edit_hazard_type"):
    st.session_state.editing_from_review = True
    st.switch_page("pages/report_hazard.py")

if st.button("Edit Location", use_container_width=True, key="edit_location"):
    st.session_state.editing_from_review = True
    st.switch_page("pages/hazard_location.py")

if st.button("Edit Details", use_container_width=True, key="edit_details"):
    st.switch_page("pages/hazard_details.py")

st.divider()

if st.button("Submit Report", use_container_width=True, type="primary"):
    st.session_state.final_details = final_details_input.strip()

    report = {
        "report_id": f"HR-{uuid4().hex[:8].upper()}",
        "submitted_time": st.session_state.report_timestamp,
        "hazard_type": hazard_type,
        "location": location,
        "severity": severity,
        "final_details": st.session_state.final_details,
        "photo_attached": "Yes" if photo else "No",
    }

    save_report(report)

    st.session_state.submitted_report_id = report["report_id"]

    st.switch_page("pages/confirmation.py")

if st.button("Cancel Report", use_container_width=True):
    clear_report_data()
    st.switch_page("pages/home.py")