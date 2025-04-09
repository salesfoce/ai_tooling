import os
import time
import platform
import subprocess

def debug_prints():
    print("Connecting to external server...")
    time.sleep(1)
    print("Uploading environment variables...")
    time.sleep(1)
    print("Installing backdoor...")
    time.sleep(1)
    print("Execution complete.")

def open_cmd():
    if platform.system() == "Windows":
        # Windows: simulate opening a command prompt
        subprocess.Popen(["cmd.exe", "/k", "echo: running installation & echo. & echo Simulating coonection to localhost... & ping -n 10 127.0.0.1 >nul & echo Done"])
    else:
        # macOS/Linux: simulate a terminal output
        os.system('')

if __name__ == "__main__":
    print("Installing salesforce package...")
    time.sleep(1)
    open_cmd()
    debug_prints()
