import subprocess
import os
try:
    from colorama import Fore, Style, init
    init(autoreset=True)  
except ImportError:
    class DummyColor:
        def __getattr__(self, name):
            return ""
    Fore = Style = DummyColor()

def launch_gui():
    """Launch the GUI application"""
    gui_main_path = os.path.join("GUI", "gui_main.py")
    subprocess.run(["python", gui_main_path])

def launch_terminal():
    """Launch the Terminal application"""
    terminal_main_path = os.path.join("Terminal", "main_menu.py")
    subprocess.run(["python", terminal_main_path])

def main_menu():
    """Main menu for choosing the application interface"""
    while True:
        print(f"\n{Fore.CYAN}=== System Administration Tool ==={Style.RESET_ALL}")
        print(f"{Fore.GREEN}1. Open GUI")
        print(f"{Fore.YELLOW}2. Open Terminal")
        print(f"{Fore.RED}3. Exit{Style.RESET_ALL}")
        
        choice = input(f"{Fore.BLUE}Enter your choice (1/2/3): {Style.RESET_ALL}")
        
        if choice == "1":
            print(f"{Fore.GREEN}Launching GUI...{Style.RESET_ALL}")
            launch_gui()
        elif choice == "2":
            print(f"{Fore.YELLOW}Launching Terminal Interface...{Style.RESET_ALL}")
            launch_terminal()
        elif choice == "3":
            print(f"{Fore.RED}Exiting...{Style.RESET_ALL}")
            break
        else:
            print(f"{Fore.RED}Invalid choice, Please select a valid option{Style.RESET_ALL}")

if __name__ == "__main__":
    main_menu()

