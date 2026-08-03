import pytest

from calculator import add, divide, multiply, subtract

def test_add():
    assert add(10, 20) == 30


def test_subtract():
    assert subtract(20, 10) == 10


def test_multiply():
    assert multiply(2, 5) == 10


def test_divide():
    assert divide(20, 2) == 10


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)


def test_setup_fixture(setup):
    assert setup == "Connected"


@pytest.mark.parametrize(
    "a, b, result",
    [
        (1, 2, 3),
        (2, 3, 5),
        (10, 20, 30),
    ],
)
def test_add_parameterized(a, b, result):
    assert add(a, b) == result


@pytest.mark.smoke
def test_login():
    assert True


@pytest.mark.regression
def test_signup():
    assert True