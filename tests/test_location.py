import pytest
from api_file import get_location_info
from asserts.location import assert_response_for_location
from test_data.location import location_expected_data

"""
Test class for the Rick and Morty location.

This test class contains test cases for the Rick and Morty location-related APIs.

"""


class TestRMALocation:

    """This test case fetches location information by ID and compares it with the expected data."""
    @pytest.mark.parametrize("location_id, expected_data", location_expected_data.items())
    def test_get_location_info(self, location_id, expected_data):
        location_info = get_location_info(location_id)
        assert_response_for_location(location_info, expected_data)
