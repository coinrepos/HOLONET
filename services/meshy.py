import requests
import os
from dotenv import load_dotenv

load_dotenv()
MESHY_API_KEY = os.getenv("MESHY_API_KEY")

def optimize_mesh(model_file):
    url = "https://api.meshy.com/optimize"
    headers = {"Authorization": f"Bearer {MESHY_API_KEY}"}
    files = {"file": open(model_file, "rb")}
    
    response = requests.post(url, headers=headers, files=files)
    return response.json() if response.status_code == 200 else {"error": "Failed to optimize mesh"}
