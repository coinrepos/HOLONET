import requests
import os
from dotenv import load_dotenv

load_dotenv()
TRIPO_API_KEY = os.getenv("TRIPO_API_KEY")

def fetch_tripo_character():
    url = "https://api.tripo.com/characters"
    headers = {"Authorization": f"Bearer {TRIPO_API_KEY}"}
    
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else {"error": "Failed to fetch character"}
