from database import create_table, add_post, get_latest_post


def main():
    # Initialize database
    create_table()

    # Example posts
    posts = [
        ("image1.png", "First post!", "Alice"),
        ("image2.png", "Having a great day!", "Bob"),
        ("image3.png", "Just finished coding!", "Charlie")
    ]

    # Store posts
    for image, text, user in posts:
        add_post(image, text, user)

    # Retrieve latest post
    latest = get_latest_post()
    if latest:
        image, text, user, created_at = latest
        print("\n📢 Latest Post:")
        print(f"User: {user}")
        print(f"Image: {image}")
        print(f"Text: {text}")
        print(f"Created at: {created_at}")
    else:
        print("No posts found.")


if __name__ == "__main__":
    main()
