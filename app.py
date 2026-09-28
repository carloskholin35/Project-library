import sqlite3

from flask import (
    Flask,
    render_template, 
    request, 
    redirect, 
    url_for, 
    abort, 
    g, 
    flash,
)
from database import (
    get_all_books, 
    get_all_genres, 
    get_book_from_id,
    get_genres_by_book, 
    insert_book, 
    modify_book, 
    modify_book_genres,
    remove_book,
)

app = Flask(__name__)
app.secret_key = '12345' # Temporary key while on localhost

@app.teardown_appcontext
def teardown_app(exception):
    db = g.pop('db', None)
    if db is not None:
        db.close()

@app.route("/")
def index():
    """Main web interface"""
    all_books = get_all_books()
    genres = get_all_genres()
    return render_template("index.html", books=all_books, genres=genres)

@app.route("/add_book", methods=['POST'])
def add_book():
    book_name = request.form.get('book_name')
    author_name = request.form.get('author_name')
    # Convert to None if they have no data
    cover_url = request.form.get('cover_url') or None
    year = request.form.get('publication_year')
    publication_year = int(year) if year else None
    genre_ids = [int(genre) for genre in request.form.getlist('genres[]')] #List comprehension

    book_id, created = insert_book(book_name, author_name, cover_url, publication_year)
    modify_book_genres(book_id, genre_ids)

    if created:
        flash("Book added")
    else:
        flash("This book already exists")    
    return redirect(url_for('index'))

@app.route('/book/<int:book_id>')
def show_book_profile(book_id):
    book = get_book_from_id(book_id)
    book_genres = get_genres_by_book(book_id)
    book_genres_ids = [g[0] for g in book_genres]
    genres = get_all_genres()
    if book is None:
        abort(404)
    return render_template('book_detail.html', book=book, book_genres=book_genres, book_genres_ids=book_genres_ids, genres=genres)

@app.route('/book/<int:book_id>/delete', methods=['POST'])
def delete_book(book_id):
    try:
        remove_book(book_id)
        flash("Book deleted")
    except sqlite3.IntegrityError:
        flash("This book can't be deleted because it has readings") 
        return redirect(url_for('show_book_profile', book_id=book_id))
    
    return redirect(url_for('index'))

@app.route('/book/<int:book_id>/update', methods=['POST'])
def update_book(book_id):
    book_name = request.form.get('book_name')
    author_name = request.form.get('author_name')
    genre_ids = [int(genre) for genre in request.form.getlist('genres[]')] #List comprehension
    # Convert to None if they have no data
    cover_url = request.form.get('cover_url') or None
    year = request.form.get('publication_year')
    publication_year = int(year) if year else None

    modify_book(book_id, book_name, author_name, cover_url, publication_year)
    modify_book_genres(book_id, genre_ids)
    return redirect(url_for('index'))        