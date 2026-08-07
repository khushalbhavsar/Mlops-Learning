from app.login import login


def test_login_success():
    assert login("admin", "admin123") is True


def test_login_wrong_password():
    assert login("admin", "wrongpass") is False


def test_login_unknown_user():
    assert login("unknown", "password") is False
