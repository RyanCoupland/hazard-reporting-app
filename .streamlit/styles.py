import streamlit as st


def apply_global_styles():
    """
    Applies shared styling used across the entire prototype.

    """
    st.markdown(
        """
        <style>
        /* Main page width and spacing */
        section[data-testid="stMain"] > div[data-testid="stMainBlockContainer"] {
            width: min(100%, 900px);
            max-width: 900px;
            padding-top: 0rem;
            padding-bottom: 0.5rem;
        }

        /* Hide default Streamlit interface elements */
        header[data-testid="stHeader"],
        #MainMenu,
        footer {
            display: none !important;
        }

        /* Hide Streamlit heading anchor/link buttons */
        .stHeadingActionButton,
        h1 a,
        h2 a,
        h3 a {
            display: none !important;
        }

        /* Shared heading styles */
        h1, h3 {
            text-align: center;
        }

        h1 {
            font-size: 2.2rem !important;
        }

        /* Shared button border */
        div.stButton > button {
            border: 4px solid #000000;
        }

        /* Shared button text styling */
        div.stButton > button,
        div.stButton > button p {
            font-size: 1.3rem !important;
            font-weight: 900 !important;
        }

        /* Primary action buttons */
        div.stButton > button[kind="primary"] {
            background-color: #FFD400;
            color: #000000;
        }

        /* Secondary action buttons */
        div.stButton > button[kind="secondary"] {
            background-color: #000000;
            color: #FFFFFF;
        }

        /* General paragraph styling */
        div[data-testid="stMarkdownContainer"] p {
            text-align: center;
            font-size: 1.1rem;
            font-weight: 900;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def apply_home_styles():
    """
    Applies larger button and spacing styles for the home screen.
    """
    st.markdown(
        """
        <style>
        h3 {
            margin-bottom: clamp(1.8rem, 4vh, 2.5rem) !important;
            margin-top: clamp(1.8rem, 4vh, 2.5rem) !important;
            font-size: 1.5rem !important;
        }

        div.stButton > button {
            min-height: clamp(6.5rem, 13vh, 8.5rem);
            margin-bottom: clamp(1.25rem, 3vh, 2rem);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def apply_review_styles():
    """
    Applies styles for the review/report summary screens.

    """
    st.markdown(
        """
        <style>
        /* Shared card styling */
        .st-key-review_summary,
        .st-key-confirm_check {
            border: 4px solid #000000;
            border-radius: 8px;
            padding: 1rem;
        }

        /* Yellow report summary card */
        .st-key-review_summary {
            background-color: #FFD400;
        }

        .st-key-review_summary p {
            text-align: left !important;
            margin-left: 1rem;
        }

        /* Confirmation/check section on the review page */
        .st-key-confirm_check {
            margin-top: 0.5rem;
            margin-bottom: 0.5rem;
            background-color: #FFF7CC;
        }

        .st-key-confirm_check h3 {
            font-size: 1.5rem;
            font-weight: 900;
        }

        .st-key-confirm_check p {
            font-weight: 700 !important;
        }

        /* Remove default expander border used for the edit-report section */
        div[data-testid="stExpander"] details {
            border: none;
        }

        /* Style the expander header like a black secondary action */
        div[data-testid="stExpander"] details summary {
            background-color: #000000 !important;
            color: #FFFFFF;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def confirmation_styles():
    """
    Applies styles for the report confirmation page.

    The submission message is highlighted to clearly show that the report has
    been saved successfully.
    """
    st.markdown(
        """
        <style>
        .st-key-submission_message {
            background-color: #FFD400;
            border: 3px solid #000000;
            border-radius: 8px;
            padding: 1rem;
            margin-top: 1rem;
        }

        .st-key-submission_message h3 {
            font-weight: 900;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def apply_saved_reports_styles():
    """
    Applies styles for saved report cards.
    """
    st.markdown(
        """
        <style>
        /* Saved report cards */
        div[class*="st-key-report_card_"] {
            background-color: #FFD400;
            padding: 1.5rem;
            border: 4px solid #000000;
        }

        /* Left-align report card text */
        div[class*="st-key-report_card_"] div[data-testid="stMarkdownContainer"] p {
            text-align: left !important;
            line-height: 1 !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def show_step_bar(current_step: int, total_steps: int = 4):
    """
    Displays a simple segmented progress bar for the reporting workflow.

    Filled segments show completed/current steps, while lighter segments show the
    remaining steps.
    """
    st.markdown(
        f"""
        <div style="display: flex; gap: 6px; margin-bottom: 1rem;">
            {''.join([
                f'<div style="flex: 1; height: 8px; background-color: {"#FFD400" if i <= current_step else "#D9D9D9"};"></div>'
                for i in range(1, total_steps + 1)
            ])}
        </div>
        """,
        unsafe_allow_html=True,
    )