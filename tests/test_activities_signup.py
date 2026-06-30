from urllib.parse import quote


def test_signup_adds_participant(client):
    email = "new.student@mergington.edu"

    response = client.post(
        f"/activities/{quote('Chess Club', safe='')}/signup?email={quote(email, safe='')}"
    )

    assert response.status_code == 200
    assert response.json()["message"] == f"Signed up {email} for Chess Club"

    activities_response = client.get("/activities")
    participants = activities_response.json()["Chess Club"]["participants"]
    assert email in participants


def test_signup_rejects_duplicate_participant(client):
    existing_email = "michael@mergington.edu"

    response = client.post(
        f"/activities/{quote('Chess Club', safe='')}/signup?email={quote(existing_email, safe='')}"
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Student already signed up for this activity"


def test_signup_returns_not_found_for_unknown_activity(client):
    response = client.post("/activities/Unknown%20Club/signup?email=test%40mergington.edu")

    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_signup_requires_email_query_param(client):
    response = client.post(f"/activities/{quote('Chess Club', safe='')}/signup")

    assert response.status_code == 422
