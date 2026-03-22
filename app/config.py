from dotenv import load_dotenv
import os

load_dotenv()

API_KEY: str = os.getenv("STEAM_API_KEY", "")
