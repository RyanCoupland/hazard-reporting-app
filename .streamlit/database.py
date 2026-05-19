import sqlite3
from pathlib import Path

# Path to the SQLite database file.
DB_PATH = Path(__file__).parent / "hazard_reports.db"


def get_connection():
    """Return a new connection to the SQLite database."""
    return sqlite3.connect(DB_PATH)


def init_db():
    """
    Create the reports table if it does not already exist.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reports (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            report_id       TEXT UNIQUE NOT NULL,
            submitted_time  TEXT NOT NULL,
            hazard_type     TEXT NOT NULL,
            location        TEXT NOT NULL,
            severity        TEXT NOT NULL,
            final_details   TEXT,
            photo_data      BLOB
        )
    """)

    conn.commit()
    conn.close()


def save_report(report):
    """
    Save a completed hazard report to the database.

    The report is passed as a dictionary from the review submission page.
    Photo data is converted to a BLOB if present.
    """
    conn = get_connection()
    cursor = conn.cursor()

    photo_data = report.get("photo_data")

    if photo_data is not None:
        photo_data = sqlite3.Binary(photo_data)

    cursor.execute("""
        INSERT INTO reports (
            report_id,
            submitted_time,
            hazard_type,
            location,
            severity,
            final_details,
            photo_data
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        report["report_id"],
        report["submitted_time"],
        report["hazard_type"],
        report["location"],
        report["severity"],
        report.get("final_details", ""),
        photo_data,
    ))

    conn.commit()
    conn.close()


def get_report_summaries():
    """
    Return a list of report summaries for the Saved Reports page.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            report_id,
            submitted_time,
            hazard_type,
            location,
            severity
        FROM reports
        ORDER BY submitted_time DESC
    """)

    reports = cursor.fetchall()
    conn.close()

    return reports


def get_report_by_id(report_id):
    """
    Return the full details of a single report by its report_id.

    Used by the Report Details page to display complete report information.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            report_id,
            submitted_time,
            hazard_type,
            location,
            severity,
            final_details,
            photo_data
        FROM reports
        WHERE report_id = ?
    """, (report_id,))

    report = cursor.fetchone()
    conn.close()

    return report


def update_report_details(report_id, final_details):
    """
    Update the optional additional details of an existing report.

    Allows users to add more information after the initial submission.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE reports
        SET final_details = ?
        WHERE report_id = ?
    """, (final_details, report_id))

    conn.commit()
    conn.close()