import pytest
from main4 import init_db, add_user, get_users


@pytest.fixture
def db_conn():
    conn = init_db()
    yield conn
    conn.close()

def test_add_or_get_user(db_conn):
    add_user(db_conn, "John", 30)
    user = get_users(db_conn, "John")
    assert user == (1,"John", 30)