import psutil
import socket

hostname = socket.gethostname()

cpu = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory()
disk = psutil.disk_usage("/")

print("===== SRE Infrastructure Health =====")
print(f"Hostname: {hostname}")
print(f"CPU Utilization: {cpu}%")
print(f"Memory Utilization: {memory.percent}%")
print(f"Disk Utilization: {disk.percent}%")
