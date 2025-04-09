import os
import time
import platform
import subprocess

def debug_prints():
    print("Connecting to external server...")
    time.sleep(1)
    print("Uploading environment variables...")
    time.sleep(1)
    print("Setting service...")
    time.sleep(1)
    print("Installation complete.")

def open_cmd():
    if platform.system() == "Windows":
        subprocess.Popen(["cmd.exe", "/k", "echo: running installation & echo. & echo Simulating coonection to localhost... & ping -n 10 127.0.0.1 >nul & echo Done"])
    else:
        subprocess.Popen(["bash", "-c", "echo 'Running installation...' && echo && echo 'Simulating connection to localhost...' && sleep 10 && echo 'Done'"])

if __name__ == "__main__":
    print("Installing salesforce package...")
    time.sleep(1)
    open_cmd()
    debug_prints()
