import sqlite3

cn = sqlite3.connect("bookshelf.db")
cur = cn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS Books (
        book_id INTEGER PRIMARY KEY,
        book_name TEXT NOT NULL,
        author TEXT NOT NULL,
        genre TEXT NOT NULL,
        UNIQUE(book_name, author)
    )
""")

# For every item in parameters, repeatedly execute the parameterized DML SQL statement sql
data = [
    ("The Way of Kings", "Brandon Sanderson", "Epic Fantasy"),
    ("Project Hail Mary", "Andy Weir", "Science Fiction"),
    ("Words of Radiance", "Brandon Sanderson", "Epic Fantasy"),
]

cur.executemany("""
    INSERT OR IGNORE INTO Books (book_name, author, genre) 
    VALUES(?, ?, ?)
""", data)

cn.commit()
cur.close()
cn.close()