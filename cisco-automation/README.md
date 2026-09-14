# Cisco Network Automation with Netmiko

A Python-based network automation project for connecting to Cisco IOS devices through SSH and collecting operational information.

## Objective

Automate common network-engineering tasks that would otherwise require manually connecting to each Cisco device and running CLI commands.

## Technologies

- Python 3
- Netmiko
- SSH
- Cisco IOS
- TCP/IP
- Git

## Current Automation

The `show-device.py` script:

1. Accepts a device IP address from the command line.
2. Prompts for SSH credentials securely.
3. Establishes an SSH connection using Netmiko.
4. Executes `show ip interface brief`.
5. Displays the device output.
6. Closes the SSH session.
7. Reports connection errors.

## Usage

```bash
python show-device.py <device-ip>
