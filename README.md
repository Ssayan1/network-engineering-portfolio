# Linux Network Monitoring & SSH Automation

Practical Linux networking and automation tools built with Bash and Python.

## Objective

Automate common network-engineering tasks such as:

- Network interface and routing checks
- Internet connectivity testing
- DNS resolution testing
- TCP listening-port inspection
- Host reachability monitoring
- Network latency measurement
- CSV-based monitoring logs
- SSH-based remote network diagnostics

## Technologies

- Linux
- Bash
- Python 3
- SSH
- Paramiko
- tcpdump
- DNS
- TCP/IP
- Git

## Tools

### network-check.sh

Performs a basic Linux network health check:

- IP addresses
- Routing table
- Default gateway
- Internet connectivity
- DNS resolution
- Listening TCP ports

### network-check_v2.sh

Improved version that reports network checks using PASS/FAIL results.

### ping-checker.py

Tests multiple hosts and reports:

- UP/DOWN status
- ICMP response latency

### CSV_Network_Monitoring.py

Records monitoring results into a CSV file containing:

- Timestamp
- Host
- Status
- Latency

### ssh-check.py

Uses Python Paramiko to connect to a remote Linux system through SSH.

### ssh-check_2.py

Extends the SSH automation workflow by remotely collecting:

- Hostname
- IP addresses
- Routing table
- Listening TCP ports

## Example Workflow

```text
Python Script
     |
     v
SSH
     |
     v
Remote Linux Host
     |
     +--> hostname
     +--> IP configuration
     +--> routing table
     +--> listening ports
