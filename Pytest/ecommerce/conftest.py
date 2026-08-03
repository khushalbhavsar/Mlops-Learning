import pytest


@pytest.fixture
def setup():
    print("Application ready for testing")
    return "ready"
