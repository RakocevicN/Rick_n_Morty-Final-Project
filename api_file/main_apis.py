"""
Main_apis includes functions to retrieve episode, character, location, and location information.
Usage:
    - Use 'get_episode' to retrieve episode details by providing an episode ID.
    - Use 'get_character_by_id' to retrieve character details by providing a character ID.
    - Use 'get_all_locations' to retrieve information about all locations.
"""
import requests
from config import main_api


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
