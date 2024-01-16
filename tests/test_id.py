"""
docstring  to add here
"""

import pytest
from api.api_id import get_character_by_id
from asserts.character import assert_response_for_character
from test_data.id import id_expected_data


class TestRMAid:
    """Test for the Rick and Morty API."""

    @pytest.mark.parametrize("character_id, expected_data", id_expected_data.items())
    def test_get_characters_by_id(self, character_id, expected_data):
        """Test get_character_by_id function."""
        character_response = get_character_by_id(character_id)
        assert_response_for_character(character_response, expected_data)
