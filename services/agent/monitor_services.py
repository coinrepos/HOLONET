import os
import time
import logging
import subprocess
from datetime import datetime

# Configure logging
LOG_FOLDER = r"C:\Projects\HOLONET\services\logs"
LOG_FILE = os.path.join(LOG_FOLDER, "service_monitor.log")

# Ensure log folder exists
os.makedirs(LOG_FOLDER, exist_ok=True)

logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%(asctime)s - %(message)s')

# Services to monitor (Name -> Command)
SERVICES = {
    "HolonetAI": "schtasks /run /tn HolonetAI",
    "3D Viewer": "python C:\\Projects\\HOLONET\\services\\3dviewer\\server.py",
    "Dashboard": "python C:\\Projects\\HOLONET\\services\\dashboard\\dashboard.py"
}

def is_service_running(service_name):
    """Check if a service is running."""
    try:
        result = subprocess.check_output(f'tasklist | findstr /I "{service_name}"', shell=True)
        return service_name in result.decode()
    except subprocess.CalledProcessError:
        return False

def restart_service(service_name, command):
    """Restart a service if it's not running."""
    logging.warning(f"{service_name} is NOT running! Attempting restart...")
    os.system(command)
    time.sleep(5)
    if is_service_running(service_name):
        logging.info(f"{service_name} restarted successfully.")
    else:
        logging.error(f"Failed to restart {service_name}!")

if __name__ == "__main__":
    logging.info("Holonet Service Monitor Started.")
    while True:
        for service, command in SERVICES.items():
            if not is_service_running(service):
                restart_service(service, command)
        time.sleep(30)  # Check every 30 seconds
