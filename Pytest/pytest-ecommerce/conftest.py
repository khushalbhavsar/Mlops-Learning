import pytest


@pytest.fixture(scope="session")
def store_name():
    return "Amazon Demo Store"


@pytest.fixture(scope="function")
def customer():
    return {
        "username": "customer",
        "password": "customer123",
    }


@pytest.fixture
def empty_cart():
    return []


@pytest.fixture
def laptop():
    return {
        "id": 1,
        "name": "Laptop",
        "price": 50000,
        "stock": 10,
    }


@pytest.fixture
def mobile():
    return {
        "id": 2,
        "name": "Mobile",
        "price": 20000,
        "stock": 20,
    }
