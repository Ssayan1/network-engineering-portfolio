import subprocess
import re
from datetime import datetime
import csv
hosts = [
    "8.8.8.8",
    "1.1.1.1",
    "192.168.1.1"
]

print("===== NETWORK CONNECTIVITY CHECK =====")

for host in hosts:
    result = subprocess.run(
        ["ping", "-c", "1", "-W", "2", host],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        match = re.search(r"time[=<]([\d.]+)", result.stdout)

        if match:
            latency = match.group(1)
            print(f"{host:15} UP    {latency} ms")
        else:
            print(f"{host:15} UP")
    else:
        print(f"{host:15} DOWN")

print("=======================================")
