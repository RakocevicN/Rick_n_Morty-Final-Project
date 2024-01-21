import deepdiff
import allure


@allure.step("Assert Response Location")
def assert_response_location(response, expected_data):
    """
    This function checks if the response matches the expected data for location
    AssertionError will be present if the verification condition fails.
    """
    excluded = [
        "root['residents']",
        "root['url']",
        "root['created']"
    ]
    differences = deepdiff.DeepDiff(response, expected_data, exclude_paths=excluded)

    if differences:
        allure.attach("Response Data", str(response), allure.attachment_type.JSON)
        allure.attach("Expected Data", str(expected_data), allure.attachment_type.JSON)
        allure.attach("Differences", str(differences), allure.attachment_type.TEXT)
    assert not differences
