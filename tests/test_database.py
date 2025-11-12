import pytest
from database import create_table, add_post, get_latest_post
import sqlite3

@pytest.fixture
def test_db():
    # Setup: create in-memory database
    conn = sqlite3.connect(":memory:")
    create_table(conn)
    yield conn
    # Teardown: close connection
    conn.close()

def test_add_and_get_post(test_db):
    add_post(test_db, "img.png", "Hello!", "Alice")
    latest = get_latest_post(test_db)
    
    assert latest is not None
    assert latest[0] == "img.png"       # image
    assert latest[1] == "Hello!"        # text
    assert latest[2] == "Alice"         # user
