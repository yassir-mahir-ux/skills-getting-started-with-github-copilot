from fastapi.testclient import TestClient

from src.app import app, activities

client = TestClient(app)


def test_unregister_participant_removes_email():
    original = activities["Chess Club"]["participants"][:]
    try:
        response = client.delete("/activities/Chess%20Club/unregister?email=michael@mergington.edu")

        assert response.status_code == 200
        assert "michael@mergington.edu" not in activities["Chess Club"]["participants"]
        assert response.json()["message"] == "Unregistered michael@mergington.edu from Chess Club"
    finally:
        activities["Chess Club"]["participants"] = original


def test_unregister_missing_participant_returns_not_found():
    response = client.delete("/activities/Chess%20Club/unregister?email=missing@mergington.edu")

    assert response.status_code == 404
