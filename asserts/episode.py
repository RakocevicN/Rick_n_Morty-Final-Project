import deepdiff


def assert_response_episode(response, expected_data):
    # Exclude from comparison
    excluded = [
        "root['characters']",
        "root['url']",
        "root['created']"
    ]

    # Find differences excluding the specified paths
    differences = deepdiff.DeepDiff(response, expected_data, exclude_paths=excluded)
    if differences:
        assert False, f"Response data does not match expected data, this are the differences: {differences}"
