"""
docstring  to add here
"""
import pytest
from apis.main_apis import get_episode
from asserts.episode import assert_response_for_episode
from test_data.episode import episode_expected_data


class TestRMEpisode:
    """Test for the Rick and Morty episode."""

    @pytest.mark.parametrize("episode_id, expected_data", episode_expected_data.items())
    def test_get_episode(self, episode_id, expected_data):
        episode_response = get_episode(episode_id)
        assert_response_for_episode(episode_response, expected_data)
