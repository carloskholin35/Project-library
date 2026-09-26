import sqlite3

cn = sqlite3.connect("bookshelf.db")
cur = cn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS Readings (
        reading_id INTEGER PRIMARY KEY,
        user_id INTEGER NOT NULL,
        book_id INTEGER NOT NULL,
        status TEXT NOT NULL CHECK (status IN ('want_to_read', 'reading', 'read', 'did_not_finish')),
        rating REAL CHECK (rating IN (0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0)),
        review TEXT,
        liked INTEGER NOT NULL DEFAULT 0 CHECK (liked IN (0, 1)),
        start_date TEXT,
        end_date TEXT,
        FOREIGN KEY (user_id) REFERENCES Users(user_id),
        FOREIGN KEY (book_id) REFERENCES Books(book_id)
    )
""")

cn.commit()
cur.close()
cn.close()