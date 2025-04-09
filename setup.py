import os
import time
import platform
import subprocess

def fake_payload():
    print("Connecting to external server...")
    time.sleep(1)
    print("Uploading environment variables...")
    time.sleep(1)
    print("Installing backdoor...")
    time.sleep(1)
    print("Execution complete.")

def open_fake_cmd():
    if platform.system() == "Windows":
        # Windows: simulate opening a command prompt
        subprocess.Popen(["cmd.exe", "/k", "echo WARNING: You installed a fake package & echo. & echo Simulating data exfiltration... & ping -n 10 127.0.0.1 >nul & echo Done"])
    else:
        # macOS/Linux: simulate a terminal output
        os.system('xterm -e "echo WARNING: You installed a fake package; echo Simulating data exfiltration...; sleep 5; echo Done" &')

if __name__ == "__main__":
    print("Installing salesfoce package...")
    time.sleep(1)
    open_fake_cmd()
    fake_payload()
