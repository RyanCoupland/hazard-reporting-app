import streamlit as st

def apply_global_styles():
    st.markdown(
        """
        <style>
        section[data-testid="stMain"] > div[data-testid="stMainBlockContainer"] {
            width: min(100%, 900px);
            max-width: 900px;
            padding-top: 0rem;
            padding-bottom: 0.5rem;
        }

        /* Hide Streamlit header/menu/footer */
        header[data-testid="stHeader"] {
            display: none !important;
        }

        #MainMenu {
            display: none !important;
        }

        footer {
            display: none !important;
        }

        .stHeadingActionButton,
        h1 a,
        h2 a,
        h3 a {
            display: none !important;
        }

        h1, h3 {
            text-align: center;
        }
        
        h1 {
            font-size: 2.2rem !important;
        }

        div.stButton > button {
            border: 4px solid #000000;
        }

        div.stButton > button,
        div.stButton > button p {
            font-size: 1.3rem !important;
            font-weight: 900 !important;
        }

        div.stButton > button[kind="primary"] {
            background-color: #FFD400;
            color: #000000;
        }

        div.stButton > button[kind="secondary"] {
            background-color: #000000;
            color: #FFFFFF;
        }

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
    st.markdown(
        """
        <style>
        .st-key-review_summary {
            background-color: #FFD400;
            padding: 0.8rem;
            border: 4px solid #000000;
        }

        .st-key-review_summary div[data-testid="stMarkdownContainer"] p {
            text-align: left !important;
            line-height: 0.75 !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

def confirmation_styles():
    st.markdown(
        """
        <style>
        .st-key-review_summary {
            background-color: #FFD400;
            padding: 1.5rem;
            border: 4px solid #000000;
            margin-bottom: clamp(1.8rem, 4vh, 2.5rem) !important;
        }

        .st-key-review_summary div[data-testid="stMarkdownContainer"] p {
            text-align: left !important;
            line-height: 1.5 !important;
        }
        
         div.stButton > button {
            min-height: clamp(6.5rem, 13vh, 8.5rem);
            margin-bottom: clamp(1.25rem, 3vh, 2rem);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

def apply_saved_reports_styles():
    st.markdown(
        """
        <style>
        div[class*="st-key-report_card_"] {
            background-color: #FFD400;
            padding: 1.5rem;
            border: 4px solid #000000;
        }

        div[class*="st-key-report_card_"] div[data-testid="stMarkdownContainer"] p {
            text-align: left !important;
            line-height: 1 !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )