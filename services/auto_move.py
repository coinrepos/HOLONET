import os
import time
import shutil

# Paths
GENERATED_SCENES_FOLDER = r"C:\Projects\HOLONET\storage\generated_scenes"
VIEWER_ASSETS_FOLDER = r"C:\Projects\HOLONET\services\3dviewer\assets"

def move_scene_files():
    while True:
        for filename in os.listdir(GENERATED_SCENES_FOLDER):
            if filename.endswith(".glb") or filename.endswith(".fbx"):
                src_path = os.path.join(GENERATED_SCENES_FOLDER, filename)
                dest_path = os.path.join(VIEWER_ASSETS_FOLDER, filename)
                
                try:
                    shutil.move(src_path, dest_path)
                    print(f"✅ Moved: {filename} → {VIEWER_ASSETS_FOLDER}")
                except Exception as e:
                    print(f"⚠️ Error moving {filename}: {e}")
        
        time.sleep(5)  # Check every 5 seconds

if __name__ == "__main__":
    move_scene_files()
