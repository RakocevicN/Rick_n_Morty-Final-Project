"""
docstring  to add here
"""

import pytest
from api_file.main_apis import get_character_by_id
from asserts.id import assert_response_for_character, assert_response_for_negative_tests
from test_data.id import get_test_case_data, id_positive_expected_data, negative_id_expected_data


class TestRMAid:
    """Test for the Rick and Morty API."""

    @pytest.mark.parametrize("test_case_name", id_positive_expected_data.keys())
    def test_id_info(self, test_case_name):
        character_id, character_data = get_test_case_data(test_case_name, id_positive_expected_data)
        id_response = get_character_by_id(character_id)
        assert_response_for_character(id_response, character_data)

    @pytest.mark.parametrize("character_id, expected_error_message", negative_id_expected_data.items())
    def test_invalid_character_id(self, character_id, expected_error_message):
        """Test get_character_by_id function with invalid character IDs."""
        response = get_character_by_id(character_id)
        assert_response_for_negative_tests(response, expected_error_message)
