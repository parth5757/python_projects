import os
import subprocess
import platform

def open_file_explorer(file_path):
    # for windows system
    if platform.system() == 'Windows':
        subprocess.run(['explorer', '/select', file_path.replace('/', '\\')])
    # for macos system
    elif platform.system() == 'Darwin':
        subprocess.run(['open', '-R', file_path])
    # for linux system
    else:
        subprocess.run(['xdg-open', file_path])

file_path = r"C:\Users\PARTH\AppData\Roaming\Google\AndroidStudio2024.1\early-access-registry.txt"

open_file_explorer(file_path)