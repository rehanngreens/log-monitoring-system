import json
import subprocess
import time
from datetime import datetime


STATUS_MESSAGES = {
    "WARNING": "ALERT: SYSTEM IS IN WARNING STATE",
    "CRITICAL": "ALERT: SYSTEM IS IN CRITICAL STATE",
    "NORMAL": "SYSTEM RECOVERED TO NORMAL STATE",
}

previous_status = None

while True:
    now = datetime.now().replace(microsecond=0)
    print("=== MONITORING CYCLE STARTED ===\n")
    print("checking logs at:", now)

    subprocess.run(["python", "analyzer/analyzer.py"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    with open("reports.json", "r", encoding="utf-8") as json_file:
        data = json.load(json_file)

    current_status = data["status"]
    print(f"INFO: {data['info']}")
    print(f"WARNING: {data['warning']}")
    print(f"ERROR: {data['error']}")
    print(f"SYSTEM STATUS: {current_status}")

    if previous_status and previous_status != current_status:
        message = STATUS_MESSAGES.get(current_status)
        print(f"ALERT: STATUS CHANGED: {previous_status} -> {current_status}")
        if message:
            print(message)
            with open("alerts.log", "a", encoding="utf-8") as alert_file:
                alert_file.write(f"[{now}] {message}\n")

    previous_status = current_status

    print("\nWaiting 5 seconds before next check...")
    print("========================================\n")
    time.sleep(5)
