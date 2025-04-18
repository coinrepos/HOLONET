import os
import time
import shutil

WATCH_FOLDER = "C:\\Projects\\HOLONET\\output_files"
STORAGE_FOLDER = "C:\\Projects\\HOLONET\\storage"
SORTED_FOLDERS = {
    "dance": ["Dancing", "Twerk"],
    "walk": ["Walk", "Step"],
    "run": ["Run", "Sprint"],
    "idle": ["Idle", "Stand"]
}
MISC_FOLDER = os.path.join(STORAGE_FOLDER, "misc")

# Ensure all necessary folders exist
for folder in SORTED_FOLDERS.keys():
    os.makedirs(os.path.join(STORAGE_FOLDER, folder), exist_ok=True)
os.makedirs(MISC_FOLDER, exist_ok=True)

def sort_fbx_files():
    """Moves new .fbx and .glb files into the correct category folder or misc/ if no match."""
    for file in os.listdir(WATCH_FOLDER):
        if (file.endswith(".fbx") or file.endswith(".glb")) and len(file) > 4 and not file.startswith("."):
            file_path = os.path.join(WATCH_FOLDER, file)
            moved = False  # Track if file is sorted

            # Check which category the file belongs to
            for category, keywords in SORTED_FOLDERS.items():
                if any(keyword.lower() in file.lower() for keyword in keywords):
                    destination = os.path.join(STORAGE_FOLDER, category, file)
                    shutil.move(file_path, destination)
                    print(f"Moved: {file} → {category}/")
                    moved = True
                    break  # Stop checking once a match is found
            
            # If no category matched, move to misc/
            if not moved:
                destination = os.path.join(MISC_FOLDER, file)
                shutil.move(file_path, destination)
                print(f"Moved: {file} → misc/")

def watch_folder():
    """Continuously watches for new .fbx and .glb files and sorts them."""
    print("Watching for new .fbx and .glb files...")
    while True:
        sort_fbx_files()
        time.sleep(5)  # Check for new files every 5 seconds

if __name__ == "__main__":
    watch_folder()
