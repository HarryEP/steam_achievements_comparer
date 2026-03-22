from typing import Dict, Any
import requests
from app.config import API_KEY


def get_player_summary(steam_id: str) -> Dict[str, Any]:
    url = "https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/"

    params = {
        "key": API_KEY,
        "steamids": steam_id,
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    return response.json()
