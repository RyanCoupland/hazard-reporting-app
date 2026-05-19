import streamlit as st

from styles import apply_global_styles, show_step_bar
from workflow import clear_report_data


# Apply global styles (button appearance, layout, hidden Streamlit elements, etc.)
apply_global_styles()

# Initialise session state variables for this page if they don't exist yet.
# This prevents errors when the page is first visited.
if "severity" not in st.session_state:
    st.session_state.severity = None

if "hazard_photo" not in st.session_state:
    st.session_state.hazard_photo = None


def select_severity(severity: str):
    """
    Store the selected severity level in session state and rerun the page.

    Updates button visually when selected
    """
    st.session_state.severity = severity
    st.rerun()


# Page header and progress indicator
st.title("Add Details")
st.write("**Step 3 of 4**")
show_step_bar(3)

# Severity selection section
st.write("**Select severity level**")

severity_options = ["Low", "Medium", "High"]

for severity in severity_options:
    is_selected = st.session_state.get("severity") == severity

    button_type = "primary" if is_selected else "secondary"
    button_label = f"{severity} ✓" if is_selected else severity

    if st.button(
        button_label,
        type=button_type,
        use_container_width=True,
        key=f"severity_{severity.lower()}",
    ):
        select_severity(severity)


# Optional photo capture section
st.write("**Add photo evidence (optional)**")

photo_input = st.camera_input(
    "Take photo",
    key="hazard_photo_input",
    label_visibility="collapsed",
)

# Store the photo bytes if the user took one
if photo_input is not None:
    st.session_state.hazard_photo = photo_input.getvalue()


# Continue button with validation
if st.button("Continue to Review", use_container_width=True, type="primary"):
    if not st.session_state.get("severity"):
        st.warning("Please select a severity level before continuing.")
    else:
        st.switch_page("pages/review_submission.py")


# Cancel button clears the current report and returns to the home screen
if st.button("Cancel Report", use_container_width=True):
    clear_report_data()
    st.switch_page("pages/home.py")