""""
Docu to bi improved
"""
import requests
from config import main_api


def get_character_by_id(character_id):
    id_url = f"{main_api}/character/{character_id}"
    response = requests.get(id_url)
    return response.json()
