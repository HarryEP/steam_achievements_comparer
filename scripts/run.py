from app.steam_api import get_player_summary
from dotenv import load_dotenv
import os

load_dotenv()

FRIEND1_STEAM_ID: str = os.getenv("FriendID1", "")


def main() -> None:
    if not FRIEND1_STEAM_ID:
        raise ValueError("FriendID1 is not set in .env")

    print("Steam ID:", FRIEND1_STEAM_ID)

    data = get_player_summary(FRIEND1_STEAM_ID)

    print("Full response:")
    print(data)


if __name__ == "__main__":
    main()
