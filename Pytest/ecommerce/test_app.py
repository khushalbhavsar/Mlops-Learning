import time

import pytest

from ecommerce.app import add, checkout, login


@pytest.fixture
def credentials():
    return {"username": "admin", "password": "admin123"}


@pytest.mark.smoke
def test_login_smoke(credentials):
    assert login(credentials["username"], credentials["password"]) == "Login Success"


@pytest.mark.smoke
def test_checkout_smoke():
    assert checkout(1000) == "Order Placed"


@pytest.mark.sanity
def test_login_fix(credentials):
    assert login(credentials["username"], credentials["password"]) == "Login Success"


@pytest.mark.regression
def test_login_regression(credentials):
    assert login(credentials["username"], credentials["password"]) == "Login Success"


@pytest.mark.regression
def test_add_regression():
    assert add(10, 20) == 30


@pytest.mark.regression
def test_checkout_regression():
    assert checkout(2000) == "Order Placed"


@pytest.mark.performance
def test_response_time():
    start = time.time()
    checkout(500)
    end = time.time()

    assert (end - start) < 2
