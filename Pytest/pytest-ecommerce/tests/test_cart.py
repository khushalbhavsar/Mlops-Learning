import pytest

from app.cart import add_to_cart, calculate_total


def test_add_product_to_cart(empty_cart, laptop):
    result = add_to_cart(empty_cart, laptop, 2)
    assert result is True
    assert len(empty_cart) == 1


def test_add_to_cart_fails_when_out_of_stock(empty_cart, laptop):
    result = add_to_cart(empty_cart, laptop, 11)
    assert result is False
    assert len(empty_cart) == 0


@pytest.mark.parametrize(
    "quantity,expected_total",
    [
        (1, 50000),
        (2, 100000),
        (3, 150000),
    ],
)
def test_cart_total_by_quantity(empty_cart, laptop, quantity, expected_total):
    add_to_cart(empty_cart, laptop, quantity)
    assert calculate_total(empty_cart) == expected_total
