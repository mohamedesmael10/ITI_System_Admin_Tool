import subprocess
import os
from GUI import task3_exit_tool


try:
    from colorama import Fore, Style, init
    init(autoreset=True)  
except ImportError:
    class DummyColor:
        def __getattr__(self, name):
            return ""
    Fore = Style = DummyColor()

GITHUB_LINK = "https://github.com/mohamedesmael10/ITI_System_Admin_Tool/tree/main"

def display_welcome():
    """Displays the welcome banner and project details"""
    print(Fore.GREEN + r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    ⠀   ⠀⢠⣤⣄⠀
	⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣧
	⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣶⣶⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣷⠀⠀⠀⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⡿
	⠀⠀⠀⠀⠀⢀⣤⣾⣿⡿⠛⢫⣿⡷⠀⠀⠀⢀⣄⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⠀⠀⣸⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⠁
	⠀⠀⠀⢀⣴⣿⡿⠛⠁⠀⢠⣿⡿⠁⠀⠀⢠⣾⡿⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⠃⠀⣰⣿⡟⢀⣤⣶⣦⣤⣤⠀⠀⠀⠀⣾⣿⣿⠇⠀
	⠀⠀⢠⣾⡿⠋⠀⠀⠀⢠⣿⡿⠁⠀⠀⢠⣿⡿⣁⣤⣤⣴⣦⠀⠀⢀⣾⣿⡟⠀⣰⣿⣿⣵⣿⣿⣿⣿⣿⣿⠃⢀⣶⣼⣿⣿⡟⠀⠀
	⠀⠀⠘⣿⡁⠀⠀⠀⢠⣿⡿⠁⠀⠀⣰⣿⣿⣾⣿⡿⣿⣿⡿⠀⢀⣼⣿⡟⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⣰⡿⠁⣿⣿⡿⠁⠀⠀
	⠀⠀⠀⠀⠀⠀⠀⢠⣿⡿⠁⠀⠀⣰⣿⣿⣿⣿⠏⣴⣿⡿⠁⣠⣿⣿⡟⠀⣴⣿⣿⣿⣿⣿⠏⣸⣿⣿⣷⡿⠋⠀⠈⣿⣿⠇⠀⠀⠀
	⠀⠀⠀⠀⠀⠀⣠⣿⣿⣷⣶⣿⣿⣿⣿⢻⣿⠿⣿⣿⠟⢁⣾⣿⣿⡿⣠⣾⣿⣿⣿⣿⡿⢣⣾⣿⡟⠉⠉⠀⠀⠀⠀⠹⣿⡆⠀⠀⠀
	⢀⣤⣶⣶⣾⣿⣿⣿⡟⠛⠉⠉⣿⣿⠃⢸⣿⡀⠀⢀⣴⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣷⣿⣿⠟⠀⠀⠀⠀⠀⣀⡀⠀⠈⠁⠀⠀⠀
	⠸⡿⠿⠛⠋⣽⣿⡟⠀⠀⠀⣸⣿⡟⠀⠀⠙⢿⣿⣿⣿⠏⠸⢿⡿⠟⠁⠙⠿⠿⠋⠈⠛⠛⠁⠀⠀⠀⠀⠀⢰⣿⣿⡆⠀⠀⠀⠀⠀
	⠀⠀⠀⠀⢰⣿⣿⠁⠀⠀⠀⣿⣿⠁⠀⠀⠀⠀⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⡇⠀⠀⠀⠀⠀
	⠀⠀⠀⢀⣿⣿⠇⠀⠀⠀⠀⠻⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⠃⠀⠀⠀⠀⠀
	⠀⠀⠀⣼⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⡟⠀⠀⠀⠀⠀⠀
	⠀⠀⢰⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠋⠁⠀⠀⠀⠀⠀⠀
	⠀⠀⠘⠻⡧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""")

    print(Fore.CYAN + "╔══════════════════════════════════════════════════════════════════════════════╗")
    print(Fore.CYAN + "║ Welcome to My Python Project  ⸜(｡ ˃ ᵕ ˂ )⸝                                   ║")
    print(Fore.CYAN + "║ Implemented by: Mohamed Esmael                                               ║")
    print(Fore.CYAN + "╠══════════════════════════════════════════════════════════════════════════════╣")
    print(Fore.CYAN + f"║ GitHub: {GITHUB_LINK:<48}   ║")
    print(Fore.CYAN + "╚══════════════════════════════════════════════════════════════════════════════╝" + Style.RESET_ALL)

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
    display_welcome()
    while True:
        print(f"\n{Fore.CYAN}=== Main Menu ==={Style.RESET_ALL}")
        print(f"{Fore.GREEN}1. Open GUI")
        print(f"{Fore.YELLOW}2. Open Terminal")
        print(f"{Fore.RED}3. Exit{Style.RESET_ALL}")
        
        choice = input(f"{Fore.CYAN}Enter your choice (1/2/3): {Style.RESET_ALL}")
        
        if choice == "1":
            print(f"{Fore.GREEN}Launching GUI (╯✧▽✧)╯...{Style.RESET_ALL}")
            launch_gui()
        elif choice == "2":
            print(f"{Fore.YELLOW}Launching Terminal Interface (╯✧▽✧)╯...{Style.RESET_ALL}")
            launch_terminal()
        elif choice == "3":
             task3_exit_tool.exit_tool()
 #           print(f"{Fore.RED}Exiting, Goodbye ヽ(･_･ ) (･_･)/...{Style.RESET_ALL}")
 #           break
        else:
            print(f"{Fore.RED}Invalid choice, Please select a valid option (-_-;)・・・{Style.RESET_ALL}")

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print(f"\n{Fore.MAGENTA}Tool interrupted by the user, Exiting (・_・;)...")
        task3_exit_tool.exit_tool()
    except SystemExit:
        pass
    except Exception as e:
        print(f"{Fore.RED}Critical Error: {e}  (-_-;)・・・")
        task3_exit_tool.exit_tool()