import sqlite3

cn = sqlite3.connect("bookshelf.db")
cur = cn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS Book_Likes (
        user_id INTEGER NOT NULL,
        book_id INTEGER NOT NULL,
        PRIMARY KEY (user_id, book_id),
        FOREIGN KEY (user_id) REFERENCES Users(user_id),
        FOREIGN KEY (book_id) REFERENCES Books(book_id)
    )
""")

try:
    cur.execute("""
    ALTER TABLE Readings DROP COLUMN liked; 
    """)
except sqlite3.OperationalError as e:
    print(f"Skipped: {e}")   

cn.commit()
cur.close()
cn.close()