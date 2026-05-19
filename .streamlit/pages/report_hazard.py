import streamlit as st

from styles import apply_global_styles, show_step_bar
from workflow import clear_report_data


# Apply global styles (layout, button styling, hidden elements, etc.)
apply_global_styles()


def select_hazard(hazard_type: str):
    """
    Save the selected hazard type to session state and navigate to the next page.

    If the user is editing from the review page, they are returned there.
    Otherwise, they continue to the hazard location step.
    """
    st.session_state.hazard_type = hazard_type

    if st.session_state.get("editing_from_review"):
        st.session_state.editing_from_review = False
        st.switch_page("pages/review_submission.py")
    else:
        st.switch_page("pages/hazard_location.py")


# Main page content
st.title("Select Hazard Type")
st.write("**Step 1 of 4**")
show_step_bar(1)


# List of available hazard types with unique button keys.
hazard_options = [
    ("Fall from Height Risk",        "hazard_fall_height"),
    ("Falling / Moving Object Risk", "hazard_falling_object"),
    ("Caught / Crush Risk",          "hazard_crush"),
    ("Moving Vehicle Risk",          "hazard_vehicle"),
    ("Slip / Trip Hazard",           "hazard_slip_trip"),
    ("Electrical Hazard",            "hazard_electrical"),
    ("Chemical / Spill Hazard",      "hazard_chemical_spill"),
    ("Other",                        "hazard_other"),
]

# Display each hazard type as a large, tap-friendly button.
for hazard_label, button_key in hazard_options:
    if st.button(
        hazard_label,
        type="primary",
        use_container_width=True,
        key=button_key,
    ):
        select_hazard(hazard_label)

# Cancel button clears any in-progress report data and returns to the home screen.
if st.button("Cancel Report", use_container_width=True, key="hazard_cancel"):
    clear_report_data()
    st.switch_page("pages/home.py")
