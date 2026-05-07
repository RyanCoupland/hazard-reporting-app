import streamlit as st
from datetime import datetime, timedelta

from styles import apply_global_styles, apply_saved_reports_styles
from database import get_report_summaries


apply_global_styles()
apply_saved_reports_styles()


REPORTS_PER_PAGE = 3


def parse_report_time(submitted_time):
    try:
        return datetime.strptime(submitted_time, "%d/%m/%Y %H:%M")
    except ValueError:
        return None


st.title("Saved Reports")
st.write("Filter and view saved hazard reports.")

reports = get_report_summaries()

severity_options = ["All", "Low", "Medium", "High"]

hazard_type_options = ["All Types"] + sorted({
    report[2] for report in reports
})

location_options = ["All Locations"] + sorted({
    report[3] for report in reports
})

date_options = ["All Time", "Today", "Last 7 Days", "Last 30 Days"]

severity_filter = st.selectbox(
    "Filter by severity",
    severity_options,
)

hazard_type_filter = st.selectbox(
    "Filter by hazard type",
    hazard_type_options,
)

location_filter = st.selectbox(
    "Filter by location",
    location_options,
)

date_filter = st.selectbox(
    "Filter by date",
    date_options,
)

filtered_reports = []
now = datetime.now()

for report in reports:
    report_id = report[0]
    submitted_time = report[1]
    hazard_type = report[2]
    location = report[3]
    severity = report[4]

    matches_severity = severity_filter == "All" or severity == severity_filter
    matches_hazard_type = hazard_type_filter == "All Types" or hazard_type == hazard_type_filter
    matches_location = location_filter == "All Locations" or location == location_filter

    report_time = parse_report_time(submitted_time)

    if date_filter == "All Time":
        matches_date = True
    elif date_filter == "Today":
        matches_date = report_time is not None and report_time.date() == now.date()
    elif date_filter == "Last 7 Days":
        matches_date = report_time is not None and report_time >= now - timedelta(days=7)
    elif date_filter == "Last 30 Days":
        matches_date = report_time is not None and report_time >= now - timedelta(days=30)
    else:
        matches_date = True

    if matches_severity and matches_hazard_type and matches_location and matches_date:
        filtered_reports.append(report)

if "saved_reports_page" not in st.session_state:
    st.session_state.saved_reports_page = 1

total_reports = len(filtered_reports)
total_pages = max(1, (total_reports + REPORTS_PER_PAGE - 1) // REPORTS_PER_PAGE)

if st.session_state.saved_reports_page > total_pages:
    st.session_state.saved_reports_page = total_pages

start_index = (st.session_state.saved_reports_page - 1) * REPORTS_PER_PAGE
end_index = start_index + REPORTS_PER_PAGE
reports_to_show = filtered_reports[start_index:end_index]

if total_reports == 0:
    st.write("No reports found.")
else:
    st.write(
        f"Reports found: {total_reports}  |  "
        f"Page {st.session_state.saved_reports_page} of {total_pages}"
    )

    for report in reports_to_show:
        report_id = report[0]
        submitted_time = report[1]
        hazard_type = report[2]
        location = report[3]
        severity = report[4]

        with st.container(key=f"report_card_{report_id}"):
            st.write(f"Severity: {severity}")
            st.write(f"Hazard type: {hazard_type}")
            st.write(f"Location: {location}")
            st.write(f"Time: {submitted_time}")

            if st.button(
                "View Report",
                use_container_width=True,
                key=f"view_{report_id}",
            ):
                st.session_state.selected_report_id = report_id
                st.switch_page("pages/report_details.py")

    col1, col2 = st.columns(2)

    with col1:
        if st.button(
            "Previous",
            use_container_width=True,
            disabled=st.session_state.saved_reports_page == 1,
            key="previous_reports_page",
        ):
            st.session_state.saved_reports_page -= 1
            st.rerun()

    with col2:
        if st.button(
            "Next",
            use_container_width=True,
            disabled=st.session_state.saved_reports_page == total_pages,
            key="next_reports_page",
        ):
            st.session_state.saved_reports_page += 1
            st.rerun()

if st.button("Return to Home", use_container_width=True, type="primary"):
    st.switch_page("pages/home.py")