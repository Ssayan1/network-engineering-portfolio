#!/bin/bash

echo "===== NETWORK HEALTH CHECK ====="

echo
echo "[1] Network Interfaces"
ip -br addr

echo
echo "[2] Routing Table"
ip route

echo
echo "[3] Default Gateway"
ip route | grep default

echo
echo "[4] Internet Connectivity"
ping -c 3 8.8.8.8

echo
echo "[5] DNS Resolution"
dig +short google.com

echo
echo "[6] Listening TCP Services"
ss -lnt

echo
echo "===== CHECK COMPLETE ====="
