from urllib.parse import quote


def test_state_isolation_resets_mutations_between_tests(client):
    email = "transient@mergington.edu"

    client.post(
        f"/activities/{quote('Chess Club', safe='')}/signup?email={quote(email, safe='')}"
    )

    first_read = client.get("/activities").json()["Chess Club"]["participants"]
    assert email in first_read



def test_state_isolation_confirms_clean_state(client):
    participants = client.get("/activities").json()["Chess Club"]["participants"]

    assert "transient@mergington.edu" not in participants
