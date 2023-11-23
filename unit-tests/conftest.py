import pytest


@pytest.fixture(scope="class", autouse=True)
def print_1():
    print("Fixture called")
