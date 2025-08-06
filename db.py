import sqlite3

def create_connection():
    return sqlite3.connect("bottles.db")

def creat_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bottles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            volume TEXT,
            date TEXT,
            quality TEXT,
            price REAL,
            notes TEXT
        );
    """)
    conn.commit()
    conn.close()