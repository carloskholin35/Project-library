import sqlite3

cn = sqlite3.connect("bookshelf.db")
cur = cn.cursor()

try:
    cur.execute("""
    ALTER TABLE Books ADD COLUMN cover_url TEXT;
    """)
except sqlite3.OperationalError as e:
    print(f"Skipped: {e}")    

try:
    cur.execute("""
    ALTER TABLE Books ADD COLUMN publication_year INTEGER;
    """)
except sqlite3.OperationalError as e:
    print(f"Skipped: {e}")   

cn.commit()
cur.close()
cn.close()