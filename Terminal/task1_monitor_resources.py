try:
    from colorama import Fore, Style
except ImportError:
    class DummyColor:
        def __getattr__(self, name):
            return ""
    Fore = Style = DummyColor()
import socket
import shutil
import os

def monitor_resources():
    """Fetch and display essential system resource information."""
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        total, used, free = shutil.disk_usage(os.getcwd())

        print(f"\n{Fore.CYAN}=== Monitor System Resources ===")
        print(f"{Fore.GREEN}Hostname: {Fore.YELLOW}{hostname}")
        print(f"{Fore.GREEN}IP Address: {Fore.YELLOW}{ip_address}")
        print(f"{Fore.GREEN}Total Disk Space: {Fore.YELLOW}{total / (1024 ** 3):.2f} GB")
        print(f"{Fore.GREEN}Used Disk Space: {Fore.YELLOW}{used / (1024 ** 3):.2f} GB")
        print(f"{Fore.GREEN}Free Disk Space: {Fore.YELLOW}{free / (1024 ** 3):.2f} GB")

    except Exception as e:
        print(f"{Fore.RED}Error: Unable to monitor system resources. Details: {e}")
