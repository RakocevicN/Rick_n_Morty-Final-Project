import requests


def assert_response_for_character(response, expected_data):
    # Check if the response is a dictionary
    if isinstance(response, dict):
        response_data = response
    else:

        if not isinstance(response, requests.Response):
            raise AssertionError("Invalid response type -expected an HTTP response object.")

        assert response.status_code == 200, f"Expected status code 200, but failed with {response.status_code}"

        if isinstance(response.json(), dict):
            response_data = response.json()
        else:
            response_data = response.json()[0]

    # Check other fields in the response
    for key, value in expected_data.items():
        assert response_data[key] == value, f"Expected {key}: {value}, but got {response_data[key]}"
