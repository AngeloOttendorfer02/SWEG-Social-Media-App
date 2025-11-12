import sqlite3
from datetime import datetime

DB_NAME = "social_media.db"


def create_table():
    """Create posts table if it doesn't exist."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            image TEXT NOT NULL,
            text TEXT NOT NULL,
            user TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()


def add_post(image: str, text: str, user: str):
    """Insert a new post into the database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO posts (image, text, user, created_at)
        VALUES (?, ?, ?, ?)
    """, (image, text, user, datetime.now()))
    conn.commit()
    conn.close()


def get_latest_post():
    """Retrieve the most recent post."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT image, text, user, created_at
        FROM posts
        ORDER BY created_at DESC
        LIMIT 1
    """)
    post = cursor.fetchone()
    conn.close()
    return post
