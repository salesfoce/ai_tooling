import os
import time
import platform
import subprocess
import random
import sys

# ANSI color codes
COLORS = {
    "green": "\033[92m",
    "cyan": "\033[94m",
    "yellow": "\033[93m",
    "red": "\033[91m",
    "blue": "\033[94m",
    "bold": "\033[1m",
    "end": "\033[0m"
}

ASCII_ART = r"""
   ____       _            __  ___           __           
  / __/__  __(_)___  ___  /  |/  /___ ______/ /____  _____
 _\ \/ _ \/ __/ __ \/ _ \/ /|_/ / __ `/ ___/ __/ _ \/ ___/
/___/ .__/_/ / / / /  __/ /  / / /_/ / /__/ /_/  __/ /    
   /_/   /_/_/ /_/\___/_/  /_/\__,_/\___/\__/\___/_/     
                                                       
"""

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

def slow_print(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def rainbow_ascii():
    colors = list(COLORS.values())[:-1]  # Exclude 'end'
    for line in ASCII_ART.splitlines():
        color = random.choice(colors)
        print(f"{color}{line}{COLORS['end']}")
        time.sleep(0.05)

def debug_prints():
    slow_print(f"{COLORS['cyan']} Connecting to external server...{COLORS['end']}")
    time.sleep(0.3)
    for i in range(4):
        log = random.choice(LOGS)
        slow_print(f"{COLORS['yellow']}[+] {log}{COLORS['end']}")
        time.sleep(0.3)
    slow_print(f"{COLORS['green']}Installation complete!{COLORS['end']}")
    time.sleep(0.3)

def open_cmd():
    if platform.system() == "Windows":
        subprocess.Popen(["cmd.exe", "/k", "echo Running installation... && echo && echo Simulating connection to localhost... && ping -n 10 127.0.0.1 >nul && echo Done"])
    else:
        subprocess.Popen(["bash", "-c", "echo 'Running installation...' && echo && echo 'Simulating connection to localhost...' && sleep 10 && echo 'Done'"])

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    rainbow_ascii()
    slow_print(f"{COLORS['bold']}Installing Salesforce Package...{COLORS['end']}", delay=0.01)
    time.sleep(1)
    open_cmd()
    debug_prints()
