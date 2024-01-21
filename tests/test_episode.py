"""
docstring  to add here
"""
import pytest
import allure
from api_file.main_apis import get_episode
from asserts.episode import assert_response_episode
from test_data.episode import get_test_case_data, episode_expected_data


@allure.feature("Rick and Morty Episode")
class TestRMEpisode:
    """Test for the Rick and Morty episode."""

    @allure.story("Episode Information")
    @allure.suite("Tests for episode of Rick & Morty")
    @pytest.mark.parametrize("test_case_name", episode_expected_data.keys())
    def test_episode_info(self, test_case_name):
        episode_id, episode_data = get_test_case_data(test_case_name, episode_expected_data)
        episode_response = get_episode(episode_id)
        assert_response_episode(episode_response, episode_data)
