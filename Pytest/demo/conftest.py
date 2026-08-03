import pytest

@pytest.fixture
def setup():

    print("Database Connected")

    return "Connected"