import requests
import os
from dotenv import load_dotenv

load_dotenv()

# Load Sloyd API credentials from .env
SLOYD_API_URL = os.getenv("SLOYD_API_URL")
SLOYD_CLIENT_ID = os.getenv("SLOYD_CLIENT_ID")
SLOYD_CLIENT_SECRET = os.getenv("SLOYD_CLIENT_SECRET")

def generate_sloyd_environment(prompt: str = "default 3D environment"):
    """
    Calls Sloyd's GitHub Plugin API to generate a 3D environment.
    """

    # Ensure all required credentials exist
    if not all([SLOYD_API_URL, SLOYD_CLIENT_ID, SLOYD_CLIENT_SECRET]):
        return {"error": "Missing Sloyd API credentials in .env"}

    payload = {
        "Prompt": prompt,
        "ClientId": SLOYD_CLIENT_ID,
        "ClientSecret": SLOYD_CLIENT_SECRET,
        "ModelOutputType": "gltf",
        "ResponseEncoding": "json"
    }

    try:
        response = requests.post(SLOYD_API_URL, json=payload)
        
        if response.status_code == 200:
            return response.json()  # Expected to return the GLTF file URL
        else:
            return {"error": f"Failed to generate environment. Status Code: {response.status_code}", "details": response.text}
    
    except requests.exceptions.RequestException as e:
        return {"error": "API request failed", "details": str(e)}
