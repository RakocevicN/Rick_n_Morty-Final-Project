import requests
from config import main_api


# To get single character by adding the ID as a parameter, e.g./character/2
def get_character_by_id(character_id):
    id_url = f"{main_api}/character/{character_id}"
    response = requests.get(id_url)
    return response.json()


def get_all_locations():
    locations_url = f"{main_api}/location"
    response = requests.get(locations_url)
    return response.json()


# To get location info
def get_location_info(location_id):
    location_url = f"{main_api}/location/{location_id}"
    response = requests.get(location_url)
    return response.json()


# To get episode
def get_episode(episode_id):
    episode_url = f"{main_api}/episode/{episode_id}"
    response = requests.get(episode_url)
    return response.json()


if __name__ == '__main__':
    print("Ovaj kod se pokrece kad se skripta egzekutuje direktno")
