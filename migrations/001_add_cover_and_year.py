import sqlite3

cn = sqlite3.connect("bookshelf.db")
cur = cn.cursor()

cur.execute("""
    ALTER TABLE Books ADD COLUMN cover_url TEXT;
""")

cur.execute("""
    ALTER TABLE Books ADD COLUMN publication_year INTEGER;
""")

cn.commit()
cur.close()
cn.close()