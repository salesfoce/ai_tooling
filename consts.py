import os
import platform
import socket
import pwd
import grp
import subprocess
import getpass
import json
from pathlib import Path
import tempfile
import time

# Terminal Colors
HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
ENDC = '\033[0m'
BOLD = '\033[1m'

def print_section(title):
    print(f"\n{HEADER}{BOLD}--- {title} ---{ENDC}")

def run_command(cmd):
    try:
        return subprocess.check_output(cmd, shell=True, stderr=subprocess.DEVNULL).decode('utf-8').strip()
    except:
        return None

def get_system_info():
    print_section("System Info")
    print(f"{OKBLUE}Collecting basic system information...{ENDC}")
    return {
        "Hostname": socket.gethostname(),
        "Platform": platform.platform(),
        "OS": platform.system(),
        "OS Version": platform.version(),
        "Architecture": platform.machine(),
        "Processor": platform.processor(),
        "Kernel": run_command("uname -r"),
        "Uptime": run_command("uptime -p"),
        "Current User": getpass.getuser(),
        "Logged-in Users": run_command("who")
    }

def get_users_and_groups():
    print_section("Users and Groups")
    print(f"{OKBLUE}Listing all user accounts and groups defined on the system...{ENDC}")
    users = [user.pw_name for user in pwd.getpwall()]
    groups = [g.gr_name for g in grp.getgrall()]
    return {
        "Users": users,
        "Groups": groups
    }

def get_sensitive_env_vars():
    print_section("Sensitive Environment Variables")
    print(f"{OKBLUE}Searching for environment variables that might contain secrets...{ENDC}")
    sensitive_keys = ['KEY', 'TOKEN', 'SECRET', 'PASSWORD', 'CREDENTIAL']
    results = {
        k: v for k, v in os.environ.items()
        if any(word in k.upper() for word in sensitive_keys)
    }
    print(f"{OKGREEN}Found {len(results)} possibly sensitive environment variables.{ENDC}")
    return results

def scan_home_for_secrets():
    print_section("Scanning for Secret Files in Home Directory")
    print(f"{OKBLUE}Looking for common file patterns that might store secrets or credentials...{ENDC}")
    suspicious_files = []
    home = Path.home()
    patterns = ['*.env', '*.pem', '*.key', '*.crt', '*.conf', '*.cfg', '*credentials*', '*pass*']
    for pattern in patterns:
        suspicious_files.extend(home.glob(f'**/{pattern}'))
    found = [str(f) for f in suspicious_files if f.is_file()]
    print(f"{OKGREEN}Found {len(found)} files matching secret patterns.{ENDC}")
    return found

def get_ssh_keys():
    print_section("SSH Keys")
    print(f"{OKBLUE}Checking for SSH keys in the user's .ssh directory...{ENDC}")
    ssh_dir = Path.home() / ".ssh"
    if ssh_dir.exists():
        files = [str(f) for f in ssh_dir.glob("*") if f.is_file()]
        print(f"{OKGREEN}Found {len(files)} SSH-related files.{ENDC}")
        return files
    print(f"{WARNING}No .ssh directory found.{ENDC}")
    return []

def get_sudoers():
    print_section("Sudo Configuration")
    print(f"{OKBLUE}Reading sudoers file and sudo group memberships...{ENDC}")
    return {
        "Sudoers File": run_command("cat /etc/sudoers"),
        "Sudo Group Members": run_command("getent group sudo") or run_command("getent group wheel")
    }

def get_crontab():
    print_section("Scheduled Tasks")
    print(f"{OKBLUE}Checking for user and system-wide scheduled tasks...{ENDC}")
    return {
        "User Crontab": run_command("crontab -l"),
        "System Crontab": run_command("cat /etc/crontab"),
        "Cron.d Directory": run_command("ls /etc/cron.d/")
    }

def simulate_telemetry(data):
    print_section(" Sending C2 Telemetry")
    print(f"{OKBLUE}Sending collected data to central server...{ENDC}")
    time.sleep(1)
    print(f"{OKGREEN}✔  transmission complete .{ENDC}")

def simulate_command_prompt_flash():
    print(f"{OKBLUE}Starting backdoor process...{ENDC}")
    
        # Open and close a real command window very quickly
    subprocess.Popen(["cmd.exe", "/c", "start", "wsl.exe", "python", "-c \"import time; time.sleep(0.1)\""], shell=True)
    time.sleep(0.1)  # Wait for the command window to open and close
    # print(f"{OKGREEN}✔ Command window flashed briefly.{ENDC}") 
    
    time.sleep(1)

def save_to_file(data):
    print_section("Saving to Local File")
    with tempfile.NamedTemporaryFile(delete=False, suffix=".json", prefix="sys_audit_", mode='w') as f:
        json.dump(data, f, indent=4)
        print(f"{OKGREEN}✔ Data written to: {f.name}{ENDC}")
    return f.name

def collect_all_info():
    info = {
        "System Info": get_system_info(),
        "Users and Groups": get_users_and_groups(),
        "Sensitive Environment Variables": get_sensitive_env_vars(),
        "Home Directory Secrets": scan_home_for_secrets(),
        "SSH Keys": get_ssh_keys(),
        "Sudo Configuration": get_sudoers(),
        "Scheduled Tasks": get_crontab()
    }
    print(f"\n{OKGREEN}{BOLD}✔ Collection complete!{ENDC}")
    return info

if __name__ == "__main__":
    all_info = collect_all_info()
    filepath = save_to_file(all_info)
    simulate_telemetry(all_info)
    simulate_command_prompt_flash()
