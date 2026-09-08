from flask import Flask, render_template, request, redirect, url_for, abort, g
from database import *
import sqlite3

app = Flask(__name__)

@app.teardown_appcontext
def teardown_app(exception):
    db = g.pop('db', None)
    if db is not None:
        db.close()

@app.route("/")
def index():
    """Main web interface"""
    all_books = get_all_books()
    return render_template("index.html", books=all_books)

@app.route("/add_book", methods=['POST'])
def add_book():
    if request.method == 'POST':
        # Capture the data from the three input text using request.form
        book_name = request.form.get('book_name')
        author_name = request.form.get('author_name')
        genre = request.form.get('genre')
        # Save in the bookshelf.db
        insert_book(book_name, author_name, genre)

        return redirect(url_for('index'))

@app.route('/book/<int:book_id>')
def show_book_profile(book_id):
    book = get_book_from_id(book_id)
    genres = get_all_genres()
    # If book doesn't exists throws error 404 (Not found)
    if book is None:
        abort(404)

    return render_template('book_detail.html', book=book, genres=genres)

@app.route('/book/<int:book_id>/delete', methods=['POST'])
def delete_book(book_id):
    if request.method == 'POST':
        remove_book(book_id)
    return redirect(url_for('index'))

@app.route('/book/<int:book_id>/update', methods=['POST'])
def update_book(book_id):
    if request.method == 'POST':
        book_name = request.form.get('book_name')
        author_name = request.form.get('author_name')
        genre_ids = [int(genre) for genre in request.form.getlist('genres[]')] #List comprehension
        cover_url = request.form.get('cover_url')
        publication_year = int(request.form.get('publication_year'))
        modify_book(book_id, book_name, author_name, cover_url, publication_year)
        modify_book_genres(book_id, genre_ids)
    return redirect(url_for('index'))        