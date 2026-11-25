import psutil
import socket
import json
from datetime import datetime, timezone

def check_health(value, warning, critical):
    if value >= critical:
        return "CRITICAL"
    elif value >= warning:
        return "WARNING"
    return "HEALTHY"

cpu = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory().percent
disk = psutil.disk_usage("/").percent

cpu_status = check_health(cpu, 70, 90)
memory_status = check_health(memory, 75, 90)
disk_status = check_health(disk, 80, 95)

statuses = [cpu_status, memory_status, disk_status]

if "CRITICAL" in statuses:
    overall_status = "CRITICAL"
elif "WARNING" in statuses:
    overall_status = "WARNING"
else:
    overall_status = "HEALTHY"

report = {
    "hostname": socket.gethostname(),
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "environment": "development",
    "metrics": {
        "cpu": {
            "utilization": cpu,
            "status": cpu_status
        },
        "memory": {
            "utilization": memory,
            "status": memory_status
        },
        "disk": {
            "utilization": disk,
            "status": disk_status
        }
    },
    "overall_status": overall_status
}

print(json.dumps(report, indent=4))

with open("diagnostic_report.json", "w") as file:
    json.dump(report, file, indent=4)

print("Diagnostic report saved successfully.")
