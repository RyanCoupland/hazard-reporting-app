import streamlit as st
from styles import apply_global_styles
from workflow import clear_report_data


apply_global_styles()


if "severity" not in st.session_state:
    st.session_state.severity = None


selected_severity = st.session_state.get("severity")

st.title("Hazard Details")
st.write("Step 3 of 4")

st.write("How serious is the hazard?")

severity_options = ["Low", "Medium", "High"]

for severity in severity_options:
    button_type = "primary" if selected_severity == severity else "secondary"
    button_label = f"{severity} ✓" if selected_severity == severity else severity

    if st.button(
        button_label,
        type=button_type,
        use_container_width=True,
        key=f"severity_{severity.lower()}"
    ):
        st.session_state.severity = severity
        st.rerun()

st.write("Provide photo (optional)")

st.camera_input(
    "Take photo (optional)",
    key="hazard_photo",
    label_visibility="collapsed",
)

if st.button("Continue to Review", use_container_width=True, type="primary"):
    if not st.session_state.get("severity"):
        st.warning("Please select a severity before continuing.")
    else:
        st.switch_page("pages/review_submission.py")

if st.button("Cancel Report", use_container_width=True):
    clear_report_data()
    st.switch_page("pages/home.py")
