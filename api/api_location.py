""""
Docu to bi improved
"""
import requests
from config import main_api


def get_all_locations():
    locations_url = f"{main_api}/location"
    response = requests.get(locations_url)
    return response.json()


# To get location info
def get_location_info(location_id):
    location_url = f"{main_api}/location/{location_id}"
    response = requests.get(location_url)
    return response.json()
