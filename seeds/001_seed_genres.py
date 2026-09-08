import sqlite3

cn = sqlite3.connect("bookshelf.db")
cur = cn.cursor()

genres_list = [
    "Fantasy", "Science Fiction", "Mystery", "Thriller", "Horror", 
    "Romance", "Historical Fiction", "Literary Fiction", "Dystopian", 
    "Adventure", "Biography", "Memoir", "History", "Philosophy", 
    "Psychology", "Self-Help", "Science", "Essay", "Poetry", "True Crime"
]

# Converts each genre into a tuple format to insert into the column "(Fantasy,)"
data = [(genre,) for genre in genres_list]

cur.executemany("""
    INSERT OR IGNORE INTO Genres (genre_name) VALUES (?)
""", data)

cn.commit()
cur.close()
cn.close()