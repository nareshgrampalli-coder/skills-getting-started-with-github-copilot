def test_get_activities_returns_expected_shape(client):
    # Arrange
    expected_fields = {"description", "schedule", "max_participants", "participants"}

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    payload = response.json()
    assert isinstance(payload, dict)
    assert payload

    for details in payload.values():
        assert set(details.keys()) == expected_fields
        assert isinstance(details["participants"], list)


def test_get_activities_is_stable_across_calls(client):
    # Arrange
    endpoint = "/activities"

    # Act
    first_response = client.get(endpoint)
    second_response = client.get(endpoint)

    # Assert
    assert first_response.status_code == 200
    assert second_response.status_code == 200
    assert first_response.json() == second_response.json()
