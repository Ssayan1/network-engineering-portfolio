from netmiko import ConnectHandler
import getpass
import sys


if len(sys.argv) != 2:
    print("Usage: python show-device.py <device-ip>")
    sys.exit(1)

host = sys.argv[1]

username = input("Username: ")
password = getpass.getpass("SSH Password: ")

device = {
    "device_type": "cisco_ios",
    "host": host,
    "username": username,
    "password": password,
}

print(f"\n[+] Connecting to {host}...")

try:
    connection = ConnectHandler(**device)

    print("[+] Connected successfully")

    output = connection.send_command("show ip interface brief")

    print("\n===== SHOW IP INTERFACE BRIEF =====")
    print(output)

    connection.disconnect()

    print("\n[+] Connection closed")

except Exception as error:
    print(f"\n[!] Connection failed: {error}")
    sys.exit(1)
