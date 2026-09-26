import sqlite3

cn = sqlite3.connect("bookshelf.db")
cur = cn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS Users (
        user_id INTEGER PRIMARY KEY,
        username TEXT NOT NULL UNIQUE
    )
""")

name = "carloskholin"
cur.execute("""
    INSERT OR IGNORE INTO Users (username) VALUES (?)
""", [name])

cn.commit()
cur.close()
cn.close()