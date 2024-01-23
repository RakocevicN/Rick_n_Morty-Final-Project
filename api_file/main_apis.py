"""
Main_apis includes functions to retrieve episode, character, location, and location information.
Usage:
    - Use 'get_episode' to retrieve episode details by providing an episode ID.
    - Use 'get_character_by_id' to retrieve character details by providing a character ID.
    - Use 'get_all_locations' to retrieve information about all locations.
"""
import requests
from config import main_api
import allure


def get_episode(episode_id):
    episode_url = f"{main_api}/episode/{episode_id}"
    response = requests.get(episode_url)
    return response.json()


def get_character_by_id(character_id):
    id_url = f"{main_api}/character/{character_id}"
    response = requests.get(id_url)
    return response.json()


def get_all_locations():
    locations_url = f"{main_api}/location"
    response = requests.get(locations_url)
    return response.json()


def get_location_info(location_id):
    location_url = f"{main_api}/location/{location_id}"
    response = requests.get(location_url)
    return response.json()


@allure.step("Verify API Request")
def verify_api_request(url):
    try:
        with allure.step("Send API Request"):
            response = requests.get(url)

        allure.attach(str(response.status_code), "Response Status Code")

        if response.status_code == 200:
            return response.json()
        elif response.status_code == 429:
            raise Exception("Too Many Requests. Please try again later.")
        elif response.status_code == 403:
            raise Exception("Access Forbidden. Check your permissions.")
        else:
            raise Exception(f"Unexpected status code: {response.status_code}")
    except requests.exceptions.HTTPError as http_err:
        raise Exception(f"HTTP error occurred while fetching data: {http_err}")
    except requests.exceptions.RequestException as req_err:
        raise Exception(f"An error occurred while sending the request: {req_err}")
    except Exception as error:
        raise Exception(f"An unexpected error occurred: {error}")
