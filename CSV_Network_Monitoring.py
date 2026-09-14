import subprocess
import re
import csv
from datetime import datetime

hosts = [
    "8.8.8.8",
    "1.1.1.1",
    "192.168.1.1"
]

results = []

print("===== NETWORK CONNECTIVITY CHECK =====")

for host in hosts:
    result = subprocess.run(
        ["ping", "-c", "1", "-W", "2", host],
        capture_output=True,
        text=True
    )

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if result.returncode == 0:
        match = re.search(r"time[=<]([\d.]+)", result.stdout)

        if match:
            latency = float(match.group(1))
            status = "UP"
            print(f"{host:15} UP    {latency} ms")
        else:
            latency = ""
            status = "UP"
            print(f"{host:15} UP")
    else:
        latency = ""
        status = "DOWN"
        print(f"{host:15} DOWN")

    results.append([timestamp, host, status, latency])

with open("network-results.csv", "a", newline="") as file:
    writer = csv.writer(file)

    for row in results:
        writer.writerow(row)

print("=======================================")
print("Results saved to network-results.csv")
