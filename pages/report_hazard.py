import streamlit as st
from styles import apply_global_styles
from workflow import clear_report_data

apply_global_styles()

def select_hazard(hazard_type):
    st.session_state.hazard_type = hazard_type

    if st.session_state.get("editing_from_review"):
        st.session_state.editing_from_review = False
        st.switch_page("pages/review_submission.py")
    else:
        st.switch_page("pages/hazard_location.py")


st.title("Hazard Type")
st.write("Step 1 of 4")

if st.button("Fall from Height Risk", type="primary", use_container_width=True, key="hazard_fall_height"):
    select_hazard("Fall from Height Risk")

if st.button("Falling Object Risk", type="primary", use_container_width=True, key="hazard_falling_object"):
    select_hazard("Falling Object Risk")

if st.button("Electrical Hazard", type="primary", use_container_width=True, key="hazard_electrical"):
    select_hazard("Electrical Hazard")

if st.button("Caught / Crush Risk", type="primary", use_container_width=True, key="hazard_crush"):
    select_hazard("Caught / Crush Risk")

if st.button("Slip / Trip Hazard", type="primary", use_container_width=True, key="hazard_slip_trip"):
    select_hazard("Slip / Trip Hazard")

if st.button("Moving Vehicle Risk", type="primary", use_container_width=True, key="hazard_vehicle"):
    select_hazard("Moving Vehicle Risk")

if st.button("Chemical / Spill Hazard", type="primary", use_container_width=True, key="hazard_chemical_spill"):
    select_hazard("Chemical / Spill Hazard")

if st.button("Other Hazard", type="primary", use_container_width=True, key="hazard_other"):
    select_hazard("Other Hazard")

if st.button("Cancel Report", use_container_width=True, key="hazard_cancel"):
    clear_report_data()
    st.switch_page("pages/home.py")