from app.steam_api import get_player_summary
from dotenv import load_dotenv
import os

FRIEND1_STEAM_ID: str = os.getenv("FriendID1", "")


def main() -> None:

    steam_id = FRIEND1_STEAM_ID

    print(steam_id)

    data = get_player_summary(steam_id)

    print("Full response:")
    print(data)


if __name__ == "__main__":
    main()
