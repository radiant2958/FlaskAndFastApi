import sqlite3

DATABASE = 'users.db'

def init_db():
    with sqlite3.connect(DATABASE) as conn:
        cur = conn.cursor()
        cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password_hash TEXT NOT NULL
        )
        ''')

def insert_user(first_name, last_name, email, password_hash):
    try:
        with sqlite3.connect(DATABASE) as conn:
            cur = conn.cursor()
            cur.execute('''
            INSERT INTO users (first_name, last_name, email, password_hash)
            VALUES (?, ?, ?, ?)
            ''', (first_name, last_name, email, password_hash))
        return True
    except sqlite3.IntegrityError:
        return False
