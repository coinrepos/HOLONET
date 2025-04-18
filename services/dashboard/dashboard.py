from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)

# Paths to log files
LOGS_FOLDER = r"C:\Projects\HOLONET\services\logs"
SERVICE_MONITOR_LOG = os.path.join(LOGS_FOLDER, "service_monitor.log")

@app.route("/")
def dashboard():
    return render_template("dashboard.html")

@app.route("/get_logs")
def get_logs():
    """Fetch the latest service monitor logs."""
    try:
        with open(SERVICE_MONITOR_LOG, "r") as file:
            logs = file.readlines()[-10:]  # Get the last 10 log entries
        return jsonify({"logs": logs})
    except FileNotFoundError:
        return jsonify({"logs": ["No logs found."]})

if __name__ == "__main__":
    app.run(debug=True, port=8050)
