import deepdiff


def assert_response_for_character(response, expected_data):
    """
    This function checks two conditions:
    1. It ensures that the provided response is a dictionary.
    2. It compares the response data with expected data from test_data -> id.py, excluding specified paths.

    AssertionError will be present if any of the verification conditions fail.

    """
    if not isinstance(response, dict):
        raise AssertionError("Invalid response type, expected type dictionary.")

    excluded = [
        "root['created']",
        "root['episode']",
        "root['origin']",
        "root['location']",
        "root['image']",
        "root['url']",
    ]

    # Compare the response data with expected data, excluding specified paths
    differences = deepdiff.DeepDiff(response, expected_data, exclude_paths=excluded)

    if differences:
        assert False, f"Response data does not match expected data, this are the differences: {differences}"


def assert_response_for_negative_tests(response, expected_error_message):
    """
    This function checks two conditions:
    1. It ensures that the provided response is a dictionary and contains an 'error' field.
    2. It compares the response error message with expected error message from test_data.

    AssertionError will be present if any of the verification conditions fail.

    """
    if not isinstance(response, dict):
        raise AssertionError("Invalid response type, expected type dictionary.")
    if "error" not in response:
        raise AssertionError("Expected error field in the response is missing.")
    error_message = response["error"]
    differences = deepdiff.DeepDiff(error_message, expected_error_message)
    if differences:
        assert False, f"Error message does not match expected test_data message, please see: differences"
