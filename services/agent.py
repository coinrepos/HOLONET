import os
import shutil
import time
import logging

# Paths
WATCH_FOLDER = "C:\\Projects\\HOLONET\\storage\\generated_scenes"
TARGET_FOLDER = "C:\\Projects\\HOLONET\\services\\3dviewer\\assets"
ARCHIVE_FOLDER = "C:\\Projects\\HOLONET\\services\\archive"
LOG_FILE = "C:\\Projects\\HOLONET\\services\\logs\\holonet_agent.log"

# Logging setup
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format="%(asctime)s - %(message)s")

def move_files():
    """Automatically moves new 3D files to the viewer's asset folder."""
    for file_name in os.listdir(WATCH_FOLDER):
        if file_name.endswith((".fbx", ".glb")):
            source = os.path.join(WATCH_FOLDER, file_name)
            destination = os.path.join(TARGET_FOLDER, file_name)

            # Move to assets
            shutil.move(source, destination)
            logging.info(f"Moved {file_name} to assets.")

def archive_old_files():
    """Archives older files to optimize storage."""
    for file_name in os.listdir(TARGET_FOLDER):
        file_path = os.path.join(TARGET_FOLDER, file_name)
        
        # Move files older than 7 days to archive
        if os.path.isfile(file_path) and (time.time() - os.path.getmtime(file_path)) > 7 * 86400:
            shutil.move(file_path, os.path.join(ARCHIVE_FOLDER, file_name))
            logging.info(f"Archived {file_name}.")

def agent_loop():
    """Continuously runs the Holonet Agent."""
    logging.info("Holonet AI Agent Started.")
    while True:
        move_files()
        archive_old_files()
        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    agent_loop()
