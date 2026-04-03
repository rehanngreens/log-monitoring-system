from flask import Flask, render_template
import json

app = Flask(__name__)


def parse_alert_line(line):
    line = line.strip()
    if not line:
        return None

    timestamp = "Unknown time"
    message = line
    if line.startswith("[") and "] " in line:
        raw_timestamp, message = line.split("] ", 1)
        timestamp = raw_timestamp[1:]

    normalized = message.lower()
    if "recovered" in normalized or "normal state" in normalized:
        level = "recovered"
    elif "warning state" in normalized:
        level = "warning"
    else:
        level = "critical"

    return {
        "raw": line,
        "message": message,
        "timestamp": timestamp,
        "level": level,
    }


@app.route("/")
def home():
    with open("reports.json", "r", encoding="utf-8") as json_file:
        data = json.load(json_file)

    with open("alerts.log", "r", encoding="utf-8") as alert_file:
        alerts = [parse_alert_line(line) for line in alert_file]
        alerts = [alert for alert in alerts if alert]
        alerts.reverse()

    return render_template("ops_dashboard.html", data=data, alerts=alerts)


if __name__ == "__main__":
    app.run(debug=True)
