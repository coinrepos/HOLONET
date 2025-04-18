from fastapi import FastAPI, Form
import os
import shutil
import json
import speech_recognition as sr
from datetime import datetime

app = FastAPI()

# 📂 Storage Directories
STORAGE_FOLDER = "C:\\Projects\\HOLONET\\storage\\generated_scenes"
VIEWER_ASSETS_FOLDER = "C:\\Projects\\HOLONET\\services\\3dviewer\\assets"

# 🛠 Ensure folders exist
os.makedirs(STORAGE_FOLDER, exist_ok=True)
os.makedirs(VIEWER_ASSETS_FOLDER, exist_ok=True)

@app.get("/")
def home():
    return {"message": "Holonet AI Orchestrator is running (3D File Automation Enabled)."}

# 📝 Generate 3D Scene from Text
@app.post("/generate-text/")
def generate_scene_from_text(user_input: str = Form(...)):
    """Generates a scene from text input and saves it with automatic movement to viewer."""
    safe_filename = user_input.replace(" ", "_").replace("!", "").replace("?", "").replace(",", "")
    
    file_info = []
    
    for ext in [".fbx", ".glb"]:
        scene_filename = f"{safe_filename}{ext}"
        scene_path = os.path.join(STORAGE_FOLDER, scene_filename)
        
        # Create mock file (Replace with actual generation process)
        with open(scene_path, "w") as f:
            f.write(f"Mock 3D scene file for {user_input}")

        # 📂 Move file to viewer assets automatically
        viewer_path = os.path.join(VIEWER_ASSETS_FOLDER, scene_filename)
        shutil.move(scene_path, viewer_path)

        file_info.append({
            "name": scene_filename,
            "size": os.path.getsize(viewer_path),
            "path": viewer_path,
            "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

    return {"scene": user_input, "files": file_info, "status": "Scene successfully generated!"}

# 🎤 Generate Scene from Voice Input
@app.post("/generate-voice/")
def generate_scene_from_voice():
    """Processes voice input and generates a scene."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for voice command...")
        audio = recognizer.listen(source)

    try:
        user_input = recognizer.recognize_google(audio)
        return generate_scene_from_text(user_input)
    except sr.UnknownValueError:
        return {"error": "Could not understand the voice input."}
    except sr.RequestError:
        return {"error": "Could not request results, check internet connection."}

# 📂 List Available 3D Scenes
@app.get("/scenes/list/")
def list_scenes():
    """Lists all stored 3D animation files from the viewer's assets folder."""
    files = [
        {
            "name": f,
            "size": os.path.getsize(os.path.join(VIEWER_ASSETS_FOLDER, f)),
            "created": datetime.fromtimestamp(os.path.getctime(os.path.join(VIEWER_ASSETS_FOLDER, f))).strftime("%Y-%m-%d %H:%M:%S"),
            "path": f"/assets/{f}"
        }
        for f in os.listdir(VIEWER_ASSETS_FOLDER) if f.endswith((".fbx", ".glb"))
    ]
    return {"scenes": files}

# 📥 Retrieve a 3D Scene
@app.get("/scenes/get/{filename}")
def get_scene(filename: str):
    """Fetches a specific 3D scene file."""
    file_path = os.path.join(VIEWER_ASSETS_FOLDER, filename)
    if os.path.exists(file_path):
        return {"file": filename, "path": file_path}
    return {"error": "File not found"}
