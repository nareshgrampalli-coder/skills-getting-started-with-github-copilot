def test_signup_then_unregister_round_trip(client):
    # Arrange
    activity_name = "Art Studio"
    email = "roundtrip_student@mergington.edu"

    # Act
    signup_response = client.post(f"/activities/{activity_name}/signup?email={email}")
    activities_after_signup = client.get("/activities")
    unregister_response = client.delete(f"/activities/{activity_name}/signup?email={email}")
    activities_after_unregister = client.get("/activities")

    # Assert
    assert signup_response.status_code == 200
    assert unregister_response.status_code == 200

    signed_up_participants = activities_after_signup.json()[activity_name]["participants"]
    unregistered_participants = activities_after_unregister.json()[activity_name]["participants"]

    assert email in signed_up_participants
    assert email not in unregistered_participants
