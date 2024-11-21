"""
Configuring the ML tests
"""
import warnings

import pytest

# pylint: disable=import-error
from src.app import app

warnings.filterwarnings("ignore", category=RuntimeWarning, module="pydub.utils")


@pytest.fixture
def test_client():
    """Configuration"""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client
