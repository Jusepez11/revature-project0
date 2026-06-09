import sqlite3

DB_NAME = "my.db"


def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with sqlite3.connect("students.db") as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                role TEXT NOT NULL
            )
        """)
#examples lowk I should move these to each individual controller
def get_all(table):
    with get_connection() as conn:
        cursor = conn.execute(
            "FROM ? SELECT *",
            (table)
        )
    return cursor.lastrowid

def get(table, id):
    with get_connection() as conn:
        cursor = conn.execute(
            "FROM ? SELECT * WHERE id=?",
            (table,id)
        )
    return cursor.lastrowid


