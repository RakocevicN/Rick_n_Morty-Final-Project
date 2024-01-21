import pytest
from api_file.main_apis import get_location_info
from asserts.location import assert_response_location
from test_data.location import get_test_case_data, location_expected_data
import allure
"""
Test class for the Rick and Morty location.

This test class contains test cases for the Rick and Morty location-related APIs.

"""


@allure.feature("Rick and Morty Location")
class TestRMALocation:

    """This tests fetches location information by location names and compares it with the expected data."""
    @allure.story("Location tests")
    @allure.suite("Tests for location of Rick & Morty")
    @pytest.mark.parametrize("test_case_name", location_expected_data.keys())
    def test_location_info(self, test_case_name):
        location_id, location_data = get_test_case_data(test_case_name, location_expected_data)
        location_response = get_location_info(location_id)
        assert_response_location(location_response, location_data)
