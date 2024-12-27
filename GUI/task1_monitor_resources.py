import os
import socket
import shutil

def monitor_resources(gui=False):
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    disk_usage = shutil.disk_usage(os.getcwd())
    
    output = (
        f"Hostname: {hostname}\n"
        f"IP Address: {ip_address}\n"
        f"Disk Usage (Current Directory):\n"
        f"  Total: {disk_usage.total / (1024 ** 3):.2f} GB\n"
        f"  Used: {disk_usage.used / (1024 ** 3):.2f} GB\n"
        f"  Free: {disk_usage.free / (1024 ** 3):.2f} GB\n"
    )
    
    if gui:
        return output
    else:
        print(output)
