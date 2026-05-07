import streamlit as st

from styles import apply_global_styles

apply_global_styles()

st.title("Settings")
st.write("Prototype settings page.")

st.info(
    "This page is included as a placeholder. "
    "Additional settings may be added later if needed."
)

st.markdown(
    """
    Possible future settings:

    - Change default location options
    - Save a default reporter name
    - User login and account settings
    - Manage saved report preferences
    - Choose default hazard categories
    """
)

if st.button("Back to Home", use_container_width=True):
    st.switch_page("pages/home.py")