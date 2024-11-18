"""
Configuring the webapp tests
"""

import pytest

# pylint: disable=import-error
from app import app
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture
def test_client():
    """Configuration"""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client
