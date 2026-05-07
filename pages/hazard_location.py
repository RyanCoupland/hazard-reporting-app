import streamlit as st
from styles import apply_global_styles
from workflow import clear_report_data


apply_global_styles()


def select_location(location):
    st.session_state.location = location

    if st.session_state.get("editing_from_review"):
        st.session_state.editing_from_review = False
        st.switch_page("pages/review_submission.py")
    else:
        st.switch_page("pages/hazard_details.py")


st.title("Hazard Location")
st.write("Step 2 of 4")

if st.button("Walkway / Access Route", type="primary", use_container_width=True, key="location_walkway"):
    select_location("Walkway / Access Route")

if st.button("Scaffold / Height Area", type="primary", use_container_width=True, key="location_scaffold"):
    select_location("Scaffold / Height Area")

if st.button("Loading / Delivery Zone", type="primary", use_container_width=True, key="location_loading"):
    select_location("Loading / Delivery Zone")

if st.button("Storage / Materials Area", type="primary", use_container_width=True, key="location_storage"):
    select_location("Storage / Materials Area")

if st.button("Vehicle Route", type="primary", use_container_width=True, key="location_vehicle_route"):
    select_location("Vehicle Route")

if st.button("Plant / Equipment Area", type="primary", use_container_width=True, key="location_equipment"):
    select_location("Plant / Equipment Area")

if st.button("Welfare / Office Area", type="primary", use_container_width=True, key="location_welfare"):
    select_location("Welfare / Office Area")

if st.button("Other Location", type="primary", use_container_width=True, key="location_other"):
    select_location("Other Location")

if st.button("Cancel Report", use_container_width=True, key="location_cancel"):
    clear_report_data()
    st.switch_page("pages/home.py")