import paramiko
import sys

if len(sys.argv) != 2:
    print("Usage: python ssh-check.py <host>")
    sys.exit(1)

host = sys.argv[1]
username = "sayans"

password = input("SSH Password: ")

commands = [
    "hostname",
    "ip -br addr",
    "ip route",
    "ss -lnt"
]

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    ssh.connect(
        hostname=host,
        username=username,
        password=password,
        timeout=5
    )

    print(f"\n[+] Connected to {host}")
    print("=" * 50)

    for command in commands:
        print(f"\n$ {command}")
        
        stdin, stdout, stderr = ssh.exec_command(command)
        output = stdout.read().decode().strip()
        error = stderr.read().decode().strip()

        if output:
            print(output)

        if error:
            print(f"ERROR: {error}")

    ssh.close()
    print("\n[+] Connection closed")

except Exception as e:
    print(f"[-] SSH connection failed: {e}")
