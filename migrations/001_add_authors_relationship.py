import sqlite3

cn = sqlite3.connect("bookshelf.db")
cur = cn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS Authors (
        author_id INTEGER PRIMARY KEY,
        author_name TEXT NOT NULL UNIQUE
    )
""")

try:
    cur.execute("ALTER TABLE Books ADD COLUMN author_id INTEGER REFERENCES Authors(author_id)")
except sqlite3.OperationalError as e:
    print(f"Skipped: {e}")
    
try:
    cur.execute("ALTER TABLE Books DROP COLUMN author")
except sqlite3.OperationalError as e:
    print(f"Skipped: {e}")    

cn.commit()
cur.close()
cn.close()