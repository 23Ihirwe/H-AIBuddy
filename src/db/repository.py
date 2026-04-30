import sqlite3
from pathlib import Path

# Ensures the data folder exists
Path("data").mkdir(exist_ok=True)
DB_PATH = Path("data/mothers.db")

def create_tables():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS mothers (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, skills TEXT, goals TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS children (id INTEGER PRIMARY KEY, mother_id INTEGER, name TEXT, age INTEGER, school_level TEXT, FOREIGN KEY (mother_id) REFERENCES mothers (id))")
    conn.commit()
    conn.close()