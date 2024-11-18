"""
This file contains tests for the web app portion
"""
import sys
import os
from io import BytesIO
from unittest.mock import patch, MagicMock
import importlib

webapp_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(webapp_path)
app_module = importlib.import_module('app')
app = app_module.app
audio_collection = app_module.audio_collection
metadata_collection = app_module.metadata_collection

import pytest

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def mock_test():
    """
    Mock test
    """
    assert True


def test_index(client):
    """
    Test the index route
    """
    response = client.get("/")
    assert response.status_code == 200


def test_record_route(client):
    """
    Test the record route
    """
    response = client.get("/record")
    assert response.status_code == 200


@patch("app.audio_collection.insert_one")
def test_missing_filename(mock_audio, client):
    """
    Test the app with a missing filename
    """
    file_info = (BytesIO(b"fake_audio_data"), "test_audio.wav")
    response = client.post("/upload-audio", data={"audio": file_info})
    assert response.status_code == 400
    assert not mock_audio.called


@patch("app.audio_collection.insert_one")
@patch("app.requests.get")
@patch("app.metadata_collection.insert_one")
def test_upload_audio(mock_req, mock_md, mock_audio, client):
    """
    Test the app with a successful file
    """
    mock_audio.return_value.inserted_id = "mock_file"
    mock_md.return_value.acknowledged = True
    mock_req.return_value.ok = True
    mock_req.return_value.text = "Success"

    data = {
        "name": "test_audio",
    }
    file_info = (BytesIO(b"fake_audio_data"), "test_audio.wav")
    response = client.post("/upload-audio", data={"audio": file_info, **data})

    assert response.status_code == 302
    assert mock_audio.called
    assert mock_md.called
    assert mock_req.called


@patch("app.audio_collection.insert_one")
@patch("app.metadata_collection.insert_one")
def test_db_failure(mock_audio, client):
    """
    Test the app with a failing db
    """
    mock_audio.return_value.inserted_id = None

    data = {
        "name": "test_audio",
    }
    file_info = (BytesIO(b"fake_audio_data"), "test_audio.wav")
    response = client.post("/upload-audio", data={"audio": file_info, **data})

    assert response.status_code == 500


@patch("app.audio_collection.insert_one")
def test_audio_missing(mock_audio, client):
    """
    Test the app with no audio
    """
    response = client.post("/upload-audio", data={"name": "test_audio"})
    assert response.status_code == 400
    assert not mock_audio.called
