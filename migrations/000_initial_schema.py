import sqlite3

cn = sqlite3.connect("bookshelf.db")
cur = cn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS Books (
        book_id INTEGER PRIMARY KEY,
        book_name TEXT NOT NULL,
        author TEXT NOT NULL,
        genre TEXT NOT NULL
    )
""")

cn.commit()
cur.close()
cn.close()