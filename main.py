from fastapi import FastAPI
import os

app = FastAPI()

STORAGE_FOLDER = "C:\\Projects\\HOLONET\\storage"

@app.get("/")
def home():
    return {"message": "Holonet 3D Asset API is running!"}

@app.get("/animations/list")
def list_animations():
    """Lists all available 3D animation files in storage, including subfolders."""
    files = []
    for root, _, filenames in os.walk(STORAGE_FOLDER):  # Search all subdirectories
        for filename in filenames:
            if filename.endswith((".fbx", ".glb")):
                relative_path = os.path.relpath(os.path.join(root, filename), STORAGE_FOLDER)
                files.append(relative_path.replace("\\", "/"))  # Normalize path for API response
    return {"animations": files}

@app.get("/animations/get/{filename}")
def get_animation(filename: str):
    """Fetches a specific 3D animation file (if it exists)."""
    for root, _, filenames in os.walk(STORAGE_FOLDER):
        if filename in filenames:
            file_path = os.path.join(root, filename)
            return {"file_path": file_path}
    return {"error": "File not found"}
