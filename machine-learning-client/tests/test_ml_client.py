"""
Tests ML client
"""

from io import BytesIO
from pymongo.errors import PyMongoError

# pylint: disable=unused-import
from src.app import app, fs, metadata, sr


def test_missing_file_id(test_client):
    """
    Test without file_id.
    """
    response = test_client.get("/predict")
    assert response.status_code == 400
    assert response.json == {"error": "file_id is required"}


def test_file_not_found(test_client, monkeypatch):
    """
    Test when the file does not exist.
    """

    def mock_get(file_id):
        """Mock get"""
        raise FileNotFoundError("File not found")

    monkeypatch.setattr(fs, "get", mock_get)

    response = test_client.get(
        "/predict", query_string={"file_id": "000000000000000000000000"}
    )
    assert response.status_code == 404
    assert response.json == {"error": "File not found in GridFS"}


def test_invalid_file_id_format(test_client):
    """
    Test with invalid format.
    """
    response = test_client.get("/predict?file_id=mock_id")
    assert response.status_code == 400
    assert response.json == {"error": "Invalid file_id format"}


def test_predict_server_error(test_client, monkeypatch):
    """
    Test for server error
    """

    def mock_get(file_id):
        """mock get"""
        raise PyMongoError("Database connection failed")

    monkeypatch.setattr(fs, "get", mock_get)

    response = test_client.get(
        "/predict", query_string={"file_id": "000000000000000000000000"}
    )

    assert response.status_code == 500
    assert response.json == {"error": "Database operation failed"}
