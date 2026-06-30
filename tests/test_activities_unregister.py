from urllib.parse import quote


def test_unregister_removes_participant(client):
    email = "michael@mergington.edu"

    response = client.delete(
        f"/activities/{quote('Chess Club', safe='')}/participants/{quote(email, safe='')}"
    )

    assert response.status_code == 200
    assert response.json()["message"] == f"Unregistered {email} from Chess Club"

    activities_response = client.get("/activities")
    participants = activities_response.json()["Chess Club"]["participants"]
    assert email not in participants


def test_unregister_returns_not_found_for_unknown_activity(client):
    response = client.delete(
        "/activities/Unknown%20Club/participants/student%40mergington.edu"
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_unregister_returns_not_found_for_missing_participant(client):
    response = client.delete(
        f"/activities/{quote('Chess Club', safe='')}/participants/{quote('absent@mergington.edu', safe='')}"
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Participant not found in this activity"
