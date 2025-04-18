import os
import time
import requests
import shutil

# Directories
VIDEO_INPUT_DIR = r"C:\Projects\HOLONET\services\tensor_holography\input"
OUTPUT_DIR = r"C:\Projects\HOLONET\services\tensor_holography\output"
VIEWER_ASSETS_DIR = r"C:\Projects\HOLONET\services\3dviewer\assets"

# TensorHolo API URL
TENSORHOLO_API = "http://127.0.0.1:8501/process"

def process_video(video_file):
    """ Sends a video frame to TensorHolo and gets the hologram output. """
    print(f"Processing {video_file}...")
    
    # Prepare data
    files = {'file': open(video_file, 'rb')}
    
    try:
        response = requests.post(TENSORHOLO_API, files=files)
        if response.status_code == 200:
            print(f"✅ Successfully processed {video_file}")
        else:
            print(f"❌ Error processing {video_file}: {response.text}")
    except Exception as e:
        print(f"⚠️ Failed to send request: {e}")

def move_holograms():
    """ Moves processed holograms to the 3D viewer assets folder. """
    for file in os.listdir(OUTPUT_DIR):
        if file.endswith(".glb"):
            src = os.path.join(OUTPUT_DIR, file)
            dst = os.path.join(VIEWER_ASSETS_DIR, file)
            shutil.move(src, dst)
            print(f"📁 Moved {file} to viewer.")

def main():
    """ Main loop to automate processing. """
    print("🔄 Holonet Hologram Automation Running...")
    
    while True:
        for video in os.listdir(VIDEO_INPUT_DIR):
            if video.endswith((".mp4", ".avi", ".mov")):
                process_video(os.path.join(VIDEO_INPUT_DIR, video))
        
        move_holograms()
        print("🕒 Waiting for new videos...")
        time.sleep(10)  # Adjust as needed

if __name__ == "__main__":
    main()
