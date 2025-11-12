import sqlite3
from database import create_table, add_post, get_latest_post

DB_NAME = "social_media.db"

def main():
    # Initialize database connection
    conn = sqlite3.connect(DB_NAME)

    try:
        # Create table if it doesn't exist
        create_table(conn)

        # Example posts
        posts = [
            ("image1.png", "First post after testing was added!", "Alice"),
            ("image2.png", "Having a great day!", "Bob"),
            ("image3.png", "Just finished coding!", "Charlie")
        ]

        # Store posts
        for image, text, user in posts:
            add_post(conn, image, text, user)

        # Retrieve latest post
        latest = get_latest_post(conn)
        if latest:
            image, text, user, created_at = latest
            print("\n📢 Latest Post:")
            print(f"User: {user}")
            print(f"Image: {image}")
            print(f"Text: {text}")
            print(f"Created at: {created_at}")
        else:
            print("No posts found.")
    finally:
        # close the connection
        conn.close()

if __name__ == "__main__":
    main()
