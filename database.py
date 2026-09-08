from flask import g
import sqlite3

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect("bookshelf.db")
    return g.db

def get_all_books():
    cn = get_db()
    cur = cn.cursor()
    res = cur.execute("""
        SELECT b.book_id, b.book_name, a.author_name
        FROM Books b
        INNER JOIN Authors a ON b.author_id = a.author_id 
        ORDER BY b.book_id DESC
    """)
    return res.fetchall()

def get_all_genres():
    cn = get_db()
    cur = cn.cursor()
    res = cur.execute("""
        SELECT * FROM Genres
    """)
    return res.fetchall()

def get_book_from_id(book_id):
    cn = get_db()
    cur = cn.cursor()
    cur.execute("""
        SELECT b.book_id, b.book_name, a.author_name, b.cover_url, b.publication_year 
        FROM Books b
        INNER JOIN Authors a ON b.author_id = a.author_id 
        WHERE b.book_id = ?
        """, (book_id,))
    book = cur.fetchone() # Returns a tuple (ordered group of elements) or None
    return book

def insert_book(book_name, author_name, genre):
    cn = get_db()
    cur = cn.cursor()
    author_id = get_or_create_author_id(author_name)
    query = "INSERT OR IGNORE INTO Books (author_id, book_name, genre) VALUES(?, ?, ?)"
    cur.execute(query, (author_id, book_name, genre))
    cn.commit()

def remove_book(book_id):
    cn = get_db()
    cur = cn.cursor()
    cur.execute("DELETE FROM Books WHERE book_id = ?", (book_id,))
    cn.commit()

def modify_book(book_id, book_name, author_name, cover_url, publication_year):
    cn = get_db()
    cur = cn.cursor()
    author_id = get_or_create_author_id(author_name)
    cur.execute("UPDATE Books SET author_id = ?, book_name = ?, cover_url = ?, publication_year = ? WHERE book_id = ?", (author_id, book_name, cover_url, publication_year, book_id))
    cn.commit()

def modify_book_genres(book_id, genre_ids):
    cn = get_db()
    cur = cn.cursor()
    cur.execute("DELETE FROM Book_Genres WHERE book_id = ?", (book_id,))
    data = [(book_id, genre) for genre in genre_ids]
    query = "INSERT OR IGNORE INTO Book_Genres (book_id, genre_id) VALUES(?, ?)"
    cur.executemany(query, data)
    cn.commit()

def get_or_create_author_id(author_name):
    cn = get_db()
    cur = cn.cursor()

    cur.execute("SELECT author_id FROM Authors WHERE author_name = ?", (author_name,))
    result = cur.fetchone()
    if result:
        author_id = result[0]
    else:
        cur.execute("INSERT OR IGNORE INTO Authors (author_name) VALUES(?)", (author_name,))
        author_id = cur.lastrowid
    return author_id         