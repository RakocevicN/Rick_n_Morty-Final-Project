"""
docstring  to add here
"""

import pytest
from apis.main_apis import get_character_by_id
from asserts.character import assert_response_for_character, assert_response_for_negative_tests
from test_data.id import positive_id_expected_data, negative_id_expected_data


class TestRMAid:
    """Test for the Rick and Morty API."""

    @pytest.mark.parametrize("character_id, expected_data", positive_id_expected_data.items())
    def test_get_characters_by_id(self, character_id, expected_data):
        """Test get_character_by_id function and response"""
        character_response = get_character_by_id(character_id)
        assert_response_for_character(character_response, expected_data)

    @pytest.mark.parametrize("character_id, expected_error_message", negative_id_expected_data.items())
    def test_invalid_character_id(self, character_id, expected_error_message):
        """Test get_character_by_id function with invalid character IDs."""
        response = get_character_by_id(character_id)
        assert_response_for_negative_tests(response, expected_error_message)
