""""
Docu to bi improved
"""
import requests

# Documentation can be found here: https://rickandmortyapi.com/documentation/#introduction
main_api = "https://rickandmortyapi.com/api"


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
