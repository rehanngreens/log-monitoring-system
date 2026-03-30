import re
import json
from datetime import datetime

pattern = re.compile(r"\[(?P<ts>.*?)\]\s*\[(?P<lvl>.*?)\]\s*(?P<msg>.*)")

info_count=0
error_count=0
warning_count=0

try:
        with open("logs/server.log","r")  as f:
            print("\n=== LOG ANALYZER REPORT ===\n")
            for line in f:
                line=line.strip()
                if not line: 
                    continue
                match=pattern.search(line)

                if match:
                     print(f"Timestamp: {match.group('ts')}")
                     print(f"Level: {match.group('lvl')}")
                     print(f"Message: {match.group('msg')}")
                     print("------------")

                level=match.group('lvl')
                if level == "INFO":
                     info_count+=1
                elif level =="ERROR":
                     error_count+=1
                elif level =="WARNING":
                     warning_count+=1
            print("\n----- SUMMARY -----")
            print(f"INFO: {info_count}")
            print(f"WARNING: {warning_count}")
            print(f"ERROR: {error_count}")
            
            total_log=info_count+warning_count+error_count
            system_status=""
            report_time = str(datetime.now().replace(microsecond=0))

            if error_count>=5:
                 print(f"\nSYSTEM STATUS: CRITICAL!!")
                 system_status="CRITICAL"
            elif warning_count>=5:
                 print("\nSYSTEM STATUS: WARNING!")
                 system_status="WARNING"
            else:
                 print("\nSYSTEM STATUS: NORMAL\n")
                 system_status="NORMAL"

            report={
                 "generated_at":report_time,
                 "source_file":"logs/server.log",
                 "total_logs":total_log,
                 "info":info_count,
                 "warning":warning_count,
                 "error":error_count,
                 "status":system_status
            }

            with open("reports.json","w") as json_file:
                 json.dump(report,json_file,indent=4)  #python function to conver dict into json
            
            print("✅ JSON report generated: report.json")

except FileNotFoundError:
     print(f"ERROR: 'server.log' not found!!")

                

