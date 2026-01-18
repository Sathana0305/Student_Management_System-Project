import sqlite3
def get_connection():
    return sqlite3.connect("students.db")
def create_student_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            student_id INTEGER PRIMARY KEY,
            name TEXT,
            department TEXT,
            year INTEGER,
            marks INTEGER
        )
    """)
    conn.commit()
    conn.close()
