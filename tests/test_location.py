"""
docstring  to add here
"""

import pytest
from rick_n_morty import get_location_info
from asserts.location import assert_response_for_location
from test_data.location import location_expected_data


class TestRMALocation:
    """Test for the Rick and Morty location."""

    @pytest.mark.parametrize("location_id, expected_data", location_expected_data.items())
    def test_get_location_info(self, location_id, expected_data):
        location_info = get_location_info(location_id)
        assert_response_for_location(location_info, expected_data)
