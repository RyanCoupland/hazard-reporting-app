import streamlit as st

from styles import apply_global_styles, show_step_bar
from workflow import clear_report_data


apply_global_styles()


def select_location(location):
    """
    Saves the selected location and navigate to the next step.

    If the user is editing from the review screen, they return to the review
    page after choosing a new location.
    """
    st.session_state.location = location

    if st.session_state.get("editing_from_review"):
        st.session_state.editing_from_review = False
        st.switch_page("pages/review_submission.py")
    else:
        st.switch_page("pages/hazard_details.py")


# Main page content
st.title("Select Location")
st.write("Step 2 of 4")
show_step_bar(2)


# Available location choices for the report
location_options = [
    ("Walkway / Access Route", "location_walkway"),
    ("Scaffold / Height Area", "location_scaffold"),
    ("Loading / Delivery Zone", "location_loading"),
    ("Storage / Materials Area", "location_storage"),
    ("Vehicle Route", "location_vehicle_route"),
    ("Plant / Equipment Area", "location_equipment"),
    ("Welfare / Office Area", "location_welfare"),
    ("Other", "location_other"),
]


# Display the location choices as large selection buttons
for location_label, button_key in location_options:
    if st.button(
        location_label,
        type="primary",
        use_container_width=True,
        key=button_key,
    ):
        select_location(location_label)


# Cancel the current report and return to the home screen
if st.button("Cancel Report", use_container_width=True, key="location_cancel"):
    clear_report_data()
    st.switch_page("pages/home.py")
