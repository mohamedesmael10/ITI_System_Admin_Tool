try:
    from colorama import Fore, Style
except ImportError:
    class DummyColor:
        def __getattr__(self, name):
            return ""
    Fore = Style = DummyColor()
import os

def list_directory(directory):
    """List all files and subdirectories within the directory"""
    try:
        if os.path.exists(directory):
            contents = os.listdir(directory)
            print(f"\n{Fore.CYAN}=== Contents of the Directory ===")
            if contents:
                for item in contents:
                    item_path = os.path.join(directory, item)
                    item_type = "Directory" if os.path.isdir(item_path) else "File"
                    print(f"{Fore.GREEN}{item_type}: {Fore.YELLOW}{item}")
            else:
                print(f"{Fore.YELLOW}The directory is empty.")
        else:
            print(f"{Fore.RED}Error: Directory '{directory}' does not exist (-_-;)")
    except Exception as e:
        print(f"{Fore.RED}Error: Unable to list directory contents Details: {e} (-_-;)")
