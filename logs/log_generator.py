import random
from datetime import datetime
import time

messages={
"INFO":["Server started successfully","User login successful","Backup completed successfully","Scheduled task executed","Configuration loaded","Service restarted successfully","New user session created","System health check passed","Cache cleared successfully","File upload completed"],
"WARNING":["High Memory usage detected","CPU usage above threshold","Disk usage nearing limit","slow response from database","unusual login attempt detected","API response delay noticed","Network latency increased","service restart took longer than expected","temporary files storage nearing capacity","high number of failed login attempts"],
"ERROR":["Database connection failed","Disk full error encountered","Service crashed unexpectedly","Authentication service unavailable","Failed to write backup file","API request failed with timeout","File system permission denied","Application process terminated unexpectedly","Network connection lost","Configuration file missing or corrupted"]
}

list_logs=["INFO","WARNING","ERROR"]

try:
        with open("server.log","a") as f:
            for _ in range(10):
                level=random.choice(list_logs)
                message=random.choice(messages[level])
                timestamp=datetime.now().replace(microsecond=0)
                f.write(f"[{timestamp}] [{level}] {message}\n")
                time.sleep(1)
                
except Exception as e:
    print(f"Failed to write log: {e}")



