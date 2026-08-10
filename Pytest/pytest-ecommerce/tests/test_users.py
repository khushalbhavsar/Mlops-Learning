import pytest

from app.users import login


@pytest.mark.smoke
def test_valid_login(customer):
    result = login(customer["username"], customer["password"])
    assert result["success"] is True
    assert result["username"] == "customer"


def test_customer_role(customer):
    result = login(customer["username"], customer["password"])
    assert result["role"] == "customer"


@pytest.mark.regression
def test_invalid_login():
    result = login("customer", "wrongpassword")
    assert result["success"] is False
    assert result["message"] == "Invalid credentials"


@pytest.mark.parametrize(
    "username,password,expected",
    [
        ("customer", "customer123", True),
        ("customer", "wrong", False),
        ("admin", "admin123", True),
        ("admin", "wrong", False),
    ],
)
def test_login_cases(username, password, expected):
    result = login(username, password)
    assert result["success"] is expected
