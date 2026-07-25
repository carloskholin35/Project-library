from flask import g
import sqlite3

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect("bookshelf.db")
    return g.db

def get_all_books():
    cn = get_db()
    cur = cn.cursor()
    res = cur.execute("SELECT * FROM Books ORDER BY book_id DESC")
    return res.fetchall()

def get_book_from_id(book_id):
    cn = get_db()
    cur = cn.cursor()

    cur.execute("SELECT book_id, book_name, author, genre FROM Books WHERE book_id = ?", (book_id,))
    book = cur.fetchone() # Returns a tuple (ordered group of elements) or None

    return book

def insert_book(book_name, author, genre):
    cn = get_db()
    cur = cn.cursor()

    query = "INSERT OR IGNORE INTO Books (book_name, author, genre) VALUES(?, ?, ?)"
    cur.execute(query, (book_name, author, genre))
    cn.commit()

def remove_book(book_id):
    cn = get_db()
    cur = cn.cursor()
    cur.execute("DELETE FROM Books WHERE book_id = ?", (book_id,))
    cn.commit()

def modify_book(book_id, book_name, author, genre):
    cn = get_db()
    cur = cn.cursor()
    cur.execute("UPDATE Books SET book_name = ?, author = ?, genre = ? WHERE book_id = ?", (book_name, author, genre, book_id))
    cn.commit()    