import pytest

from app.cart import add_to_cart
from app.orders import create_order


@pytest.mark.smoke
def test_create_order(empty_cart, laptop):
    add_to_cart(empty_cart, laptop, 2)
    order = create_order(empty_cart)
    assert order is not None
    assert order["status"] == "confirmed"
    assert order["total"] == 100000


def test_empty_cart_order():
    order = create_order([])
    assert order is None
