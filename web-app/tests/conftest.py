"""
Configuring the webapp tests
"""
import pytest
from ..app import app

@pytest.fixture
def client():
    """Configuration"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
