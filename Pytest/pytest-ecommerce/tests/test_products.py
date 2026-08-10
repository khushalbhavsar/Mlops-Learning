import pytest

from app.products import get_all_products, get_product, is_available


def test_get_product():
    product = get_product(1)
    assert product is not None
    assert product["name"] == "Laptop"
    assert product["price"] == 50000


@pytest.mark.regression
def test_get_all_products():
    products = get_all_products()
    assert len(products) == 3


def test_product_available():
    assert is_available(1, 2) is True


@pytest.mark.parametrize(
    "product_id,expected_name",
    [
        (1, "Laptop"),
        (2, "Mobile"),
        (3, "Headphones"),
    ],
)
def test_product_names(product_id, expected_name):
    product = get_product(product_id)
    assert product["name"] == expected_name


@pytest.mark.parametrize(
    "product_id,expected_price",
    [
        (1, 50000),
        (2, 20000),
        (3, 2000),
    ],
)
def test_product_prices(product_id, expected_price):
    product = get_product(product_id)
    assert product["price"] == expected_price


@pytest.mark.parametrize(
    "product_id,quantity,expected",
    [
        (1, 5, True),
        (1, 10, True),
        (1, 11, False),
    ],
)
def test_product_stock_availability(product_id, quantity, expected):
    assert is_available(product_id, quantity) is expected
