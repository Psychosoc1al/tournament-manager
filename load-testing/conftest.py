import os

import pytest


@pytest.fixture
def json_file_path(size: int = 0):
    size_str = 0
    if 0 < size < 1000:
        size_str = str(size)
    elif size >= 1000:
        size_str = str(size / 1000) + "k"

    return os.path.join(os.path.dirname(__file__), f"data_{size_str}.json")
