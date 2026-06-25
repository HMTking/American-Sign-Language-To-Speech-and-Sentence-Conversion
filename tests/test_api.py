"""Smoke tests for the API using the Flask test client."""
import pytest

from asl_app import create_app
from asl_app.config import TestingConfig


@pytest.fixture()
def client():
    app = create_app(TestingConfig)
    with app.test_client() as test_client:
        yield test_client


def test_health(client):
    resp = client.get("/health")
    assert resp.status_code == 200
    data = resp.get_json()
    assert data["status"] == "healthy"
    assert data["labels_count"] >= 1


def test_index(client):
    resp = client.get("/")
    assert resp.status_code == 200


def test_suggest(client):
    resp = client.post("/suggest", json={"prefix": "hel"})
    assert resp.status_code == 200
    data = resp.get_json()
    assert data["success"] is True
    assert isinstance(data["suggestions"], list)


def test_process_frame_requires_landmarks(client):
    resp = client.post("/process_frame", json={})
    assert resp.status_code == 200
    assert resp.get_json()["success"] is False
