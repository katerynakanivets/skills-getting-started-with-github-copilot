def test_get_activities_returns_all_activities(client):
    response = client.get("/activities")

    assert response.status_code == 200

    payload = response.json()
    assert isinstance(payload, dict)
    assert "Chess Club" in payload


def test_get_activities_item_structure(client):
    response = client.get("/activities")
    activity = response.json()["Programming Class"]

    assert set(activity.keys()) == {
        "description",
        "schedule",
        "max_participants",
        "participants",
    }
    assert isinstance(activity["participants"], list)
