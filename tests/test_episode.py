import pytest
import allure
from api_file.main_apis import get_episode
from asserts.episode import assert_response_episode
from test_data.episode import get_test_case_data, episode_expected_data


@allure.feature("Rick and Morty Episode")
class TestRMEpisode:
    """
Test class for the Rick and Morty episode.

This test class contains test cases for the Rick and Morty episode-related APIs.

"""

    @allure.story("Rick & Morty Episode tests")
    @allure.suite("Positive episode tests")
    @pytest.mark.parametrize("test_case_name", episode_expected_data.keys())
    def test_episode_info(self, test_case_name):
        """Verifies episode information retrieval by episode id"""
        with allure.step(f"1.Get test case data for {test_case_name}"):
            episode_id, episode_data = get_test_case_data(test_case_name, episode_expected_data)
        with allure.step(f"2.Get episode by episode id: {episode_id} for {test_case_name}"):
            episode_response = get_episode(episode_id)
        with allure.step(f"3.Assert response for {test_case_name} test case"):
            assert_response_episode(episode_response, episode_data)
