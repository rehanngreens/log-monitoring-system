import time
from datetime import datetime
import json
import subprocess


previous_status = None

while True:
    print("=== MONITORING CYCLE STARTED ===\n")
    print("checking logs at :",datetime.now().replace(microsecond=0))
    subprocess.run(["python", "analyzer/analyzer.py"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    with open("reports.json","r") as json_file:
        data=json.load(json_file)
        current_status=data["status"]
        print(f"INFO: {data["info"]}")
        print(f"WARNING: {data["warning"]}")
        print(f"ERROR: {data["error"]}")
        print(f"SYSTEM STATUS: {data["status"]}")

        if previous_status is not None and previous_status != current_status:
            print(f"ALERT: STATUS CHANGED: {previous_status} -> {current_status}")

            alert_msg = None 

            if current_status == "WARNING":
                alert_msg = "⚠️ ALERT: SYSTEM IS IN WARNING STATE"
            elif current_status == "CRITICAL":
                alert_msg = "🚨 ALERT: SYSTEM IS IN CRITICAL STATE"
            elif current_status=="NORMAL":
                alert_msg="✅ SYSTEM RECOVERED TO NORMAL STATE"
            

            if alert_msg:
                print(alert_msg)
                timestamp = datetime.now().replace(microsecond=0)
                with open("alerts.log", "a", encoding="utf-8") as f:
                    f.write(f"[{timestamp}] {alert_msg}\n")
        previous_status = current_status

    print("\nWaiting 5 seconds before next check...")
    print("========================================\n")
    time.sleep(5)