import os
import requests

# Define storage path
AVATAR_FOLDER = r"C:\Projects\HOLONET\services\avatars"
os.makedirs(AVATAR_FOLDER, exist_ok=True)

# ReadyPlayerMe API (Replace USER_ID with actual user ID)
AVATAR_API_URL = "https://api.readyplayer.me/v1/avatars"

def fetch_avatar(user_id):
    """Fetch an avatar from ReadyPlayerMe and save it locally."""
    try:
        response = requests.get(f"{AVATAR_API_URL}/{user_id}.glb")
        if response.status_code == 200:
            avatar_path = os.path.join(AVATAR_FOLDER, f"{user_id}.glb")
            with open(avatar_path, "wb") as avatar_file:
                avatar_file.write(response.content)
            print(f"✅ Avatar saved: {avatar_path}")
        else:
            print(f"❌ Failed to fetch avatar! Status Code: {response.status_code}")
    except Exception as e:
        print(f"❌ Error fetching avatar: {e}")

# Example Usage
if __name__ == "__main__":
    test_user_id = "example_user_id"  # Replace with a valid user ID
    fetch_avatar(test_user_id)
