import os

import pytest


@pytest.fixture
def json_file_path():
    return os.path.join(os.path.dirname(__file__), "data.json")
