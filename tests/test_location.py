import pytest
import allure
from api_file.main_apis import get_location_info
from asserts.location import assert_response_location
from test_data.location import get_test_case_data, location_expected_data


@allure.feature("Rick and Morty Location")
class TestRMALocation:
    """
Test class for the Rick and Morty location.

This test class contains test cases for the Rick and Morty location-related APIs.

"""

    @allure.story("Rick & Morty Location tests")
    @allure.suite("Positive location tests")
    @pytest.mark.parametrize("test_case_name", location_expected_data.keys())
    def test_location_info(self, test_case_name):
        """This tests fetches location information by location names and compares it with the expected data."""
        with allure.step(f"1.Get test case data for {test_case_name} "):
            location_id, location_data = get_test_case_data(test_case_name, location_expected_data)
        with allure.step(f"2.Get location by location id:{location_id} for {test_case_name}"):
            location_response = get_location_info(location_id)
        with allure.step(f"3.Assert response for {test_case_name} test case"):
            assert_response_location(location_response, location_data)
