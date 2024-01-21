import allure
import deepdiff

@allure.step("Assert Response Episode")
def assert_response_episode(response, expected_data):
    """
    This function checks two conditions:
    1. It ensures that the provided response is a dictionary.
    2. It compares the response data with expected data for episodes, excluding specified paths.

    AssertionError will be present if any of the verification conditions fail.

    """

    allure.attach("Response", str(response), allure.attachment_type.JSON)
    allure.attach("Expected Data", str(expected_data), allure.attachment_type.JSON)

    excluded = [
        "root['characters']",
        "root['url']",
        "root['created']"
    ]

    differences = deepdiff.DeepDiff(response, expected_data, exclude_paths=excluded)

    if differences:
        error_message = f"Response data does not match expected data, these are the differences: {differences}"
        allure.attach("Assertion Error", error_message, allure.attachment_type.TEXT)
        raise AssertionError(error_message)
