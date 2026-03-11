import pytest
from decimal import Decimal
from unittest.mock import patch

from app import app
from helpers.transactions import Transaction


@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client
