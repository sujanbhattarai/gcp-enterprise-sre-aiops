import psutil
import socket

def check_health(value, warning, critical):
    if value >= critical:
        return "CRITICAL"
    elif value >= warning:
        return "WARNING"
    else:
        return "HEALTHY"

hostname = socket.gethostname()

cpu = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory().percent
disk = psutil.disk_usage("/").percent

cpu_status = check_health(cpu, 70, 90)
memory_status = check_health(memory, 75, 90)
disk_status = check_health(disk, 80, 95)

print("===== Automated SRE Health Check =====")
print(f"Hostname: {hostname}")
print(f"CPU: {cpu}% - {cpu_status}")
print(f"Memory: {memory}% - {memory_status}")
print(f"Disk: {disk}% - {disk_status}")

statuses = [cpu_status, memory_status, disk_status]

if "CRITICAL" in statuses:
    print("Overall Status: CRITICAL")
elif "WARNING" in statuses:
    print("Overall Status: WARNING")
else:
    print("Overall Status: HEALTHY")
