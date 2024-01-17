import deepdiff


def assert_response_for_location(response, expected_data):
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
        assert False, f"Response data does not match location expected data, there are the differences"
