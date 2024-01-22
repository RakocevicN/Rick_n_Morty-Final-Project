import allure
import pytest
from api_file.main_apis import get_character_by_id
from asserts.id import assert_response_id, assert_response_negative_tests
from test_data.id import get_test_case_data, id_positive_expected_data, negative_id_expected_data


@allure.feature("Rick and Morty ID")
class TestRMAid:
    """
    Test class for the Rick and Morty ID tests.
    This test class contains positive and negative test cases for the Rick and Morty
    id-related APIs.
    """

    @allure.story("Rick & Morty positive ID tests")
    @allure.suite("Positive ID tests")
    @pytest.mark.parametrize("test_case_name", id_positive_expected_data.keys())
    def test_id_info(self, test_case_name):
        """Verifies character information retrieval by ID for positive scenarios."""
        with allure.step(f"1.Get test case data for {test_case_name} "):
            character_id, character_data = get_test_case_data(test_case_name, id_positive_expected_data)
        with allure.step(f"2.Get character by character id:{character_id} for {test_case_name}"):
            id_response = get_character_by_id(character_id)
        with allure.step(f"3.Assert response for {test_case_name} test case"):
            assert_response_id(id_response, character_data)

    @allure.story("Rick & Morty negative ID tests")
    @allure.suite("Negative ID tests")
    @pytest.mark.parametrize("character_id, expected_error_message", negative_id_expected_data.items())
    def test_invalid_character_id(self, character_id, expected_error_message):
        """Verifies character information retrieval by ID for negative scenarios."""
        with allure.step(f"1.Get character by ID: {character_id}"):
            response = get_character_by_id(character_id)
        with allure.step("2.Assert response for negative scenario"):
            assert_response_negative_tests(response, expected_error_message)
