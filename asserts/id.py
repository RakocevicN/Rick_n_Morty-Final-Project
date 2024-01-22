"""
asserts.id.py contains functions for asserting response data in id tests
"""
import allure
import deepdiff


@allure.step("Assert Response Positive Test")
def assert_response_id(response, expected_data):
    """
    This function checks two conditions:
    1. It ensures that the provided response is a dictionary.
    2. It compares the response data with expected data from test_data -> id.py, excluding specified paths.

    AssertionError will be present if any of the verification conditions fail.

    """

    allure.attach("Response", str(response), allure.attachment_type.JSON)
    allure.attach("Expected Data", str(expected_data), allure.attachment_type.JSON)

    excluded = [
        "root['created']",
        "root['episode']",
        "root['origin']",
        "root['location']",
        "root['image']",
        "root['url']",
    ]

    differences = deepdiff.DeepDiff(response, expected_data, exclude_paths=excluded)

    if differences:
        raise AssertionError(
            f"Response data does not match expected data, these are the differences: {differences}"
        )


@allure.step("Assert Response Negative Test")
def assert_response_negative_tests(response, expected_error_message):
    """
    This function checks two conditions:
    1. It ensures that the provided response is a dictionary and contains an 'error' field.
    2. It compares the response error message with the expected error message from test_data.

    AssertionError will be present if any of the verification conditions fail.

    """
    allure.attach("Response", str(response), allure.attachment_type.JSON)
    allure.attach("Expected Error Message", str(expected_error_message), allure.attachment_type.TEXT)

    if not isinstance(response, dict):
        raise AssertionError("Invalid response type, expected type dictionary.")

    if "error" not in response:
        raise AssertionError("Expected error field in the response is missing.")

    error_message = response["error"]

    if error_message != expected_error_message:
        raise AssertionError(
            f"Error message does not match expected test_data message. "
            f"Expected: '{expected_error_message}', Actual: '{error_message}'"
        )
