import os
import shutil
import time
from datetime import datetime, timedelta

# Define paths
ASSETS_FOLDER = r"C:\Projects\HOLONET\services\3dviewer\assets"
ARCHIVE_FOLDER = r"C:\Projects\HOLONET\services\archive"
LOG_FOLDER = r"C:\Projects\HOLONET\services\logs"
LOG_FILE = os.path.join(LOG_FOLDER, "cleanup.log")

# Ensure necessary folders exist
os.makedirs(ARCHIVE_FOLDER, exist_ok=True)
os.makedirs(LOG_FOLDER, exist_ok=True)

# Set cleanup threshold (days)
DAYS_THRESHOLD = 7
DELETE_THRESHOLD = timedelta(days=DAYS_THRESHOLD)

# Get current time
now = datetime.now()

def log_action(message):
    """Logs cleanup actions to a file."""
    with open(LOG_FILE, "a") as log:
        log.write(f"{datetime.now()} - {message}\n")
    print(message)

def cleanup_old_files():
    """Moves old .fbx and .glb files to the archive folder."""
    for file in os.listdir(ASSETS_FOLDER):
        file_path = os.path.join(ASSETS_FOLDER, file)
        
        # Skip directories
        if os.path.isdir(file_path):
            continue
        
        # Check file type
        if file.endswith((".fbx", ".glb")):
            file_modified_time = datetime.fromtimestamp(os.path.getmtime(file_path))
            
            if now - file_modified_time > DELETE_THRESHOLD:
                archive_path = os.path.join(ARCHIVE_FOLDER, file)
                
                # Move the file to archive
                shutil.move(file_path, archive_path)
                log_action(f"Moved {file} to archive. Original path: {file_path}")

# Run cleanup
cleanup_old_files()
log_action("Cleanup process completed successfully.\n")
