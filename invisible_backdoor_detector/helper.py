from datetime import datetime
from importlib import metadata
from typing import List # To support Python>3.5
import os
import sys
import glob

# Colors
SUCCESS_C = '\033[92m'
WARN_C = '\033[93m'
ERROR_C = '\033[91m'
BOLD = '\033[1m'
END_C = '\033[0m'

def get_version():
    try:
        version = metadata.version(__package__)
    except:
        version = None
    return version

def banner():
    version = get_version()
    tool_info = f"v{version}" if version else ""
    print(
    f'''
    ███████╗███████╗ ██████╗███████╗██╗
    ██╔════╝██╔════╝██╔════╝██╔════╝██║
    ███████╗█████╗  ██║     ███████╗██║
    ╚════██║██╔══╝  ██║     ╚════██║██║
    ███████║███████╗╚██████╗███████║██║
    ╚══════╝╚══════╝ ╚═════╝╚══════╝╚═╝
    invisible-backdoor-detector {tool_info} - https://github.com/cybersecsi/invisible-backdoor-detector
    ''')   

def log(msg):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"[{current_time}] - [LOG] - {msg}", flush=True)

def success(msg):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"{SUCCESS_C}[{current_time}] - [SUCCESS] - {msg}{END_C}", flush=True)

def warn(msg):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"{WARN_C}[{current_time}] - [WARN] - {msg}{END_C}", flush=True)

def err(msg):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"{ERROR_C}[{current_time}] - [ERROR] - {msg}{END_C}", flush=True)

def bold(msg):
    print(f"{BOLD}{msg}{END_C}", flush=True)

# Check if the path is a folder
def check_dir(path: str):
    if not os.path.isdir(path):
        err("This is not a folder, exiting...")
        sys.exit(1)

def get_utf8_files(path: str) -> List[str]:
    log(f"Getting valid text files in the following folder: '{path}'")
    textfiles = []
    for filename in glob.iglob(path + '**/**', recursive=True):
        if os.path.isfile(filename):
            with open(filename, encoding="utf-8", errors="strict") as f:
                try:
                    f.readline()
                    textfiles.append(filename)
                except UnicodeDecodeError:
                    err(f"{filename} is not a valid text file, discarding.")
    log(f"{len(textfiles)} files will be analyzed.")
    return textfiles