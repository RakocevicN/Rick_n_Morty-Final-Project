""""
Docu to bi improved
"""
import requests

# Documentation can be found here: https://rickandmortyapi.com/documentation/#introduction
glavni = "https://rickandmortyapi.com/api"


def get_episode(episode_id):
    episode_url = f"{glavni}/episode/{episode_id}"
    response = requests.get(episode_url)
    return response.json()


def get_character_by_id(character_id):
    id_url = f"{glavni}/character/{character_id}"
    response = requests.get(id_url)
    return response.json()


def get_all_locations():
    locations_url = f"{glavni}/location"
    response = requests.get(locations_url)
    return response.json()


def get_location_info(location_id):
    location_url = f"{glavni}/location/{location_id}"
    response = requests.get(location_url)
    return response.json()
