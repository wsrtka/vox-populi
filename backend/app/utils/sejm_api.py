import requests

from ..config import settings


BASE_URL = settings.SEJM_API_BASE.rstrip('/')


def get_json(endpoint):
    url = f"{BASE_URL}/{endpoint.lstrip('/')}"
    res = requests.get(url)
    res.raise_for_status()
    return res.json()
