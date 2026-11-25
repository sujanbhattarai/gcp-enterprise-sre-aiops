import socket
import platform
from datetime import datetime, timezone

hostname = socket.gethostname()
os_name = platform.system()
os_version = platform.release()
current_time = datetime.now(timezone.utc)

print("===== SRE System Information =====")
print("Hostname:", hostname)
print("Operating System:", os_name)
print("Kernel Version:", os_version)
print("Timestamp:", current_time)
