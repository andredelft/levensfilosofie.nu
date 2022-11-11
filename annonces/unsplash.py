import requests
from decouple import config

UNSPLASH_API_BASE = "https://api.unsplash.com"


def get_unsplash_data(id: str, return_keys=["id", "urls", "user"]):
    r = requests.get(
        f"{UNSPLASH_API_BASE}/photos/{id}",
        params={"client_id": config("UNSPLASH_ACCESS_KEY")},
        headers={"Accept-Version": "v1"},
    )

    r.raise_for_status()

    response = r.json()
    return {key: response.get(key) for key in return_keys}
