def assert_response_for_episode(response, expected_data):
    assert response['id'] == expected_data['id'], f"Expected id: {expected_data['id']}, but got: {response['id']}"
    assert response['name'] == expected_data['name'], f"Expected name: {expected_data['name']}, but got: {response['name']}"
    assert response['air_date'] == expected_data['air_date'], f"Expected air_date: {expected_data['air_date']}, but got: {response['air_date']}"
    assert response['episode'] == expected_data['episode'], f"Expected episode: {expected_data['episode']}, but got: {response['episode']}"
