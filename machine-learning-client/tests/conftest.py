"""
Configuring the ML tests
"""

# pylint: disable=import-error
from src.app import app

import warnings

import pytest

warnings.filterwarnings("ignore", category=RuntimeWarning, module="pydub.utils")


@pytest.fixture
def test_client():
    """Configuration"""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client
