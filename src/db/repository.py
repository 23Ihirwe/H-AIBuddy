import sqlite3
from pathlib import Path

Path("data").mkdir(exist_ok=True)
DB_PATH = "data/h_aibuddy.db"

def init_brain():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS logs 
                     (id INTEGER PRIMARY KEY, event TEXT, status TEXT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    conn.close()
    print("🤖 H-AIBuddy: My memory brain is online!")

if __name__ == "__main__":
    init_brain()
