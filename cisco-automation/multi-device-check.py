import csv
import getpass
import time
from datetime import datetime
from netmiko import ConnectHandler


INVENTORY_FILE = "inventory.csv"

COMMANDS = {
    "linux": {
        "hostname": "hostname",
        "interfaces": "ip addr",
        "routes": "ip route",
    },
    "cisco_ios": {
        "hostname": "show version",
        "interfaces": "show ip interface brief",
        "routes": "show ip route",
    },
}


def check_device(device, password):
    name = device["name"]
    host = device["host"]
    port = int(device["port"])
    device_type = device["device_type"]
    username = device["username"]

    max_attempts = 3
    error_type = "UNKNOWN_FAILURE"

    for attempt in range(1, max_attempts + 1):
        print(
            f"\n[+] Checking {name} ({host}:{port}) "
            f"[Attempt {attempt}/{max_attempts}]..."
        )

        connection = None

        try:
            connection = ConnectHandler(
                device_type=device_type,
                host=host,
                port=port,
                username=username,
                password=password,
                conn_timeout=5,
            )

            commands = COMMANDS[device_type]

            hostname = connection.send_command(
                commands["hostname"]
            )

            ip_addr = connection.send_command(
                commands["interfaces"]
            )

            routes = connection.send_command(
                commands["routes"]
            )

            return {
                "name": name,
                "host": host,
                "port": port,
                "status": "SUCCESS",
                "details": "Data collected",
                "hostname": hostname.strip(),
                "ip_address": ip_addr.strip(),
                "routes": routes.strip(),
            }

        except Exception as error:
            error_text = str(error)

            if (
                "Authentication" in error_text
                or "authentication" in error_text
            ):
                error_type = "AUTHENTICATION_FAILURE"

            elif (
                "TCP connection" in error_text
                or "Connection refused" in error_text
            ):
                error_type = "TCP_CONNECTION_FAILURE"

            elif (
                "timed out" in error_text
                or "timeout" in error_text.lower()
            ):
                error_type = "TIMEOUT"

            else:
                error_type = "UNKNOWN_FAILURE"

            print(
                f"[!] Attempt {attempt}/{max_attempts} failed: "
                f"{error_type}"
            )

            if error_type == "AUTHENTICATION_FAILURE":
                break

            if attempt < max_attempts:
                delay = 2 ** (attempt - 1)

                print(
                    f"[*] Retrying in {delay} second(s)..."
                )

                time.sleep(delay)

            else:
                print("[!] Maximum attempts reached.")

        finally:
            if connection:
                connection.disconnect()

    return {
        "name": name,
        "host": host,
        "port": port,
        "status": "FAILED",
        "details": error_type,
        "hostname": "",
        "ip_address": "",
        "routes": "",
    }


def save_report(results):
    filename = "network-device-report.csv"

    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "timestamp",
            "name",
            "host",
            "port",
            "status",
            "hostname",
            "ip_address",
            "routes",
            "details",
        ])

        timestamp = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        for result in results:
            writer.writerow([
                timestamp,
                result["name"],
                result["host"],
                result["port"],
                result["status"],
                result["hostname"],
                result["ip_address"],
                result["routes"],
                result["details"],
            ])

    print(f"\n[+] Report saved to {filename}")


def main():
    password = getpass.getpass("SSH Password: ")

    results = []

    with open(INVENTORY_FILE, newline="") as file:
        devices = csv.DictReader(file)

        for device in devices:
            result = check_device(device, password)
            results.append(result)

    print("\n" + "=" * 70)
    print("NETWORK DEVICE AUTOMATION REPORT")
    print("=" * 70)

    successful = 0
    failed = 0

    for result in results:
        print(
            f"{result['name']:<12}"
            f"{result['host']:<16}"
            f"{result['port']:<8}"
            f"{result['status']:<10}"
            f"{result['details']}"
        )

        if result["status"] == "SUCCESS":
            successful += 1
        else:
            failed += 1

    print("\nSummary:")
    print(f"Successful: {successful}")
    print(f"Failed:     {failed}")

    save_report(results)


if __name__ == "__main__":
    main()
