#!/bin/bash

echo "===== NETWORK HEALTH CHECK ====="

# Interface
if ip link show eth0 | grep -q "state UP"; then
    echo "Interface       : PASS"
else
    echo "Interface       : FAIL"
fi

# Default route
if ip route | grep -q "^default"; then
    echo "Default Route   : PASS"
else
    echo "Default Route   : FAIL"
fi

# Internet
if ping -c 2 -W 2 8.8.8.8 >/dev/null 2>&1; then
    echo "Internet        : PASS"
else
    echo "Internet        : FAIL"
fi

# DNS
if dig +short google.com | grep -qE '^[0-9]+\.'; then
    echo "DNS             : PASS"
else
    echo "DNS             : FAIL"
fi

# SSH
if ss -lnt | grep -q ':22 '; then
    echo "SSH :22         : PASS"
else
    echo "SSH :22         : FAIL"
fi

echo
echo "===== CHECK COMPLETE ====="
