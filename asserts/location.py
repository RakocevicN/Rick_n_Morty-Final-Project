

def assert_response_for_location(response, expected_data):
    for expected_key, expected_value in expected_data.items():
        assert response.get(
            expected_key) == expected_value, f"Expected {expected_key}: {expected_value}, but got {response.get(expected_key)}"
