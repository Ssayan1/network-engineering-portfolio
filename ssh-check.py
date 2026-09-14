import paramiko

host = "localhost"
username = "sayans"

password = input("SSH Password: ")

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    ssh.connect(
        hostname=host,
        username=username,
        password=password,
        timeout=5
    )

    print(f"[+] Connected to {host}")

    stdin, stdout, stderr = ssh.exec_command("hostname")
    output = stdout.read().decode().strip()

    print(f"Hostname: {output}")

    ssh.close()

except Exception as e:
    print(f"[-] SSH connection failed: {e}")
