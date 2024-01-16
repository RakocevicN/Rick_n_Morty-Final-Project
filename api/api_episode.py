""""
Docu to bi improved
"""
import requests
from config import main_api


def get_episode(episode_id):
    episode_url = f"{main_api}/episode/{episode_id}"
    response = requests.get(episode_url)
    return response.json()
