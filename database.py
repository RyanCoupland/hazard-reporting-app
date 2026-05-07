import sqlite3

DB_NAME = "hazard_reports.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reports (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            report_id TEXT UNIQUE NOT NULL,
            submitted_time TEXT NOT NULL,
            hazard_type TEXT NOT NULL,
            location TEXT NOT NULL,
            severity TEXT NOT NULL,
            final_details TEXT,
            photo_attached TEXT NOT NULL,
            photo_data BLOB
        )
    """)

    ensure_column_exists(cursor, "reports", "final_details", "TEXT")
    ensure_column_exists(cursor, "reports", "photo_data", "BLOB")

    conn.commit()
    conn.close()


def ensure_column_exists(cursor, table_name, column_name, column_type):
    cursor.execute(f"PRAGMA table_info({table_name})")
    columns = cursor.fetchall()

    existing_columns = [column[1] for column in columns]

    if column_name not in existing_columns:
        cursor.execute(
            f"ALTER TABLE {table_name} ADD COLUMN {column_name} {column_type}"
        )


def save_report(report):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO reports (
            report_id,
            submitted_time,
            hazard_type,
            location,
            severity,
            final_details,
            photo_attached,
            photo_data
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        report["report_id"],
        report["submitted_time"],
        report["hazard_type"],
        report["location"],
        report["severity"],
        report.get("final_details", ""),
        report.get("photo_attached", "No"),
        report.get("photo_data"),
    ))

    conn.commit()
    conn.close()


def get_report_summaries():
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
        ORDER BY id DESC
    """)

    reports = cursor.fetchall()
    conn.close()

    return reports


def get_report_by_id(report_id):
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
            photo_attached,
            photo_data
        FROM reports
        WHERE report_id = ?
    """, (report_id,))

    report = cursor.fetchone()
    conn.close()

    return report
