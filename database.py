import sqlite3

def connect_db():
    return sqlite3.connect("students.db")

def setup_database():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            roll_number TEXT UNIQUE NOT NULL,
            marks INTEGER NOT NULL,
            grade TEXT
        )
    ''')
    conn.commit()
    conn.close()
