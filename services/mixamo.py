import requests
import os
from dotenv import load_dotenv

load_dotenv()

# Load Adobe Mixamo API credentials from .env
MIXAMO_API_URL = os.getenv("MIXAMO_API_URL")
ADOBE_CLIENT_ID = os.getenv("ADOBE_CLIENT_ID")
ADOBE_CLIENT_SECRET = os.getenv("ADOBE_CLIENT_SECRET")
ADOBE_ACCESS_TOKEN = os.getenv("ADOBE_ACCESS_TOKEN")

def get_adobe_access_token():
    """
    Refreshes Adobe OAuth token (if expired) using Client ID & Secret.
    """
    token_url = "https://api.adobe.com/oauth/token"
    payload = {
        "grant_type": "client_credentials",
        "client_id": ADOBE_CLIENT_ID,
        "client_secret": ADOBE_CLIENT_SECRET
    }

    try:
        response = requests.post(token_url, data=payload)
        if response.status_code == 200:
            token_data = response.json()
            return token_data["access_token"]
        else:
            print("Failed to get Adobe token:", response.text)
            return None
    except requests.exceptions.RequestException as e:
        print("Adobe token request failed:", str(e))
        return None

def upload_to_mixamo(character_file: str):
    """
    Uploads a character to Mixamo (Adobe Add-on) for auto-rigging.
    """

    # Ensure API credentials exist
    if not all([MIXAMO_API_URL, ADOBE_ACCESS_TOKEN]):
        return {"error": "Missing Adobe Mixamo API credentials in .env"}

    headers = {
        "Authorization": f"Bearer {ADOBE_ACCESS_TOKEN}",
        "Content-Type": "multipart/form-data"
    }

    files = {
        "file": open(character_file, "rb")
    }

    try:
        response = requests.post(MIXAMO_API_URL, headers=headers, files=files)

        if response.status_code == 200:
            fbx_url = response.json().get("fbx_url")
            return {"message": "Character rigged", "fbx_url": fbx_url}
        else:
            return {"error": f"Mixamo API failed. Status Code: {response.status_code}", "details": response.text}

    except requests.exceptions.RequestException as e:
        return {"error": "Mixamo API request failed", "details": str(e)}
