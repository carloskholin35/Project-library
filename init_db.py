import sqlite3

cn = sqlite3.connect("bookshelf.db")
cur = cn.cursor()
cur.execute("UPDATE Books SET author_id = 3 WHERE book_id = 6")
cn.commit()
cur.close()
cn.close()

cur.execute("""
    CREATE TABLE IF NOT EXISTS Authors (
        author_id INTEGER PRIMARY KEY,
        author_name TEXT NOT NULL UNIQUE 
    )
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS Genres (
        genre_id INTEGER PRIMARY KEY,
        genre_name TEXT NOT NULL UNIQUE
    )
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS Books (
        book_id INTEGER PRIMARY KEY,
        author_id INTEGER,
        book_name TEXT NOT NULL,
        cover_url TEXT,
        publication_year INTEGER,
        UNIQUE(book_name, author_id),
        FOREIGN KEY (author_id) REFERENCES Authors(author_id)
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

# For every item in parameters, repeatedly execute the parameterized DML SQL statement sql
data = [
    ("The Way of Kings", "Brandon Sanderson", "Epic Fantasy"),
    ("Project Hail Mary", "Andy Weir", "Science Fiction"),
    ("Words of Radiance", "Brandon Sanderson", "Epic Fantasy"),
]

for bookName, authorName, bookGenre in data:
    cur.execute("SELECT author_id FROM Authors WHERE author_name = ?", (authorName,))
    result = cur.fetchone()
    if result:
        author_id = result[0]
    else:
        cur.execute("INSERT OR IGNORE INTO Authors (author_name) VALUES(?)", (authorName,))
        author_id = cur.lastrowid
    cur.execute("INSERT OR IGNORE INTO Books (author_id, book_name, genre) VALUES(?, ?, ?)", (author_id, bookName, bookGenre,))    

cn.commit()
cur.close()
cn.close()