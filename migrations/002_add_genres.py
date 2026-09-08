import sqlite3

cn = sqlite3.connect("bookshelf.db")
cur = cn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS Genres (
        genre_id INTEGER PRIMARY KEY,
        genre_name TEXT NOT NULL UNIQUE
    )
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS Book_Genres (
        book_id INTEGER,
        genre_id INTEGER,
        PRIMARY KEY (book_id, genre_id),
        FOREIGN KEY (book_id) REFERENCES Books(book_id),
        FOREIGN KEY (genre_id) REFERENCES Genres(genre_id)
    )
""")

cur.execute("""
    ALTER TABLE Books DROP COLUMN genre; 
""")

cn.commit()
cur.close()
cn.close()