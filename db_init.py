import os
import sqlite3

# Define the database filename
db_filename = 'database.db'

# Check if the database file exists
if not os.path.isfile(db_filename):
    # If it doesn't exist, create the database and the 'users' table
    conn = sqlite3.connect(db_filename)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
    print(f"Database '{db_filename}' created with 'users' table.")
else:
    print(f"Database '{db_filename}' already exists.")
