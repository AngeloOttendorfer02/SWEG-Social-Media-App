from datetime import datetime

def create_table(conn):
    """Create posts table if it doesn't exist."""
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


def add_post(conn, image: str, text: str, user: str):
    """Insert a new post into the database."""
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO posts (image, text, user, created_at)
        VALUES (?, ?, ?, ?)
    """, (image, text, user, datetime.now().isoformat()))
    conn.commit()


def get_latest_post(conn):
    """Retrieve the most recent post."""
    cursor = conn.cursor()
    cursor.execute("""
        SELECT image, text, user, created_at
        FROM posts
        ORDER BY created_at DESC
        LIMIT 1
    """)
    post = cursor.fetchone()
    return post
