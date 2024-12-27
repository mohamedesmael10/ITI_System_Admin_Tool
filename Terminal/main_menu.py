try:
    from colorama import Fore, Style, init
    init(autoreset=True)  
except ImportError:
    class DummyColor:
        def __getattr__(self, name):
            return ""
    Fore = Style = DummyColor()

import task1_monitor_resources
import task2_list_directory
import task3_exit_tool

def main_menu():
    """Display the main menu and handle user actions"""
    while True:
        print(f"\n{Fore.CYAN}==============================")
        print(f"{Fore.YELLOW}   System Administration Tool")
        print(f"{Fore.CYAN}==============================")
        print(f"{Fore.GREEN}1. Monitor System Resources")
        print(f"{Fore.GREEN}2. List Directory Contents")
        print(f"{Fore.GREEN}3. Exit the Tool")
        print(f"{Fore.CYAN}==============================")
        
        try:
            choice = int(input(f"{Fore.BLUE}Enter the number of your choice: {Style.RESET_ALL}"))
            if choice == 1:
                task1_monitor_resources.monitor_resources()
            elif choice == 2:
                directory = input(f"{Fore.BLUE}Enter the directory path: {Style.RESET_ALL}").strip()
                task2_list_directory.list_directory(directory)
            elif choice == 3:
                task3_exit_tool.exit_tool()
            else:
                print(f"{Fore.RED}Invalid choice, Please enter a number between 1 and 3  (-_-;)・・・")
        except ValueError:
            print(f"{Fore.RED}Error: Invalid input, Please enter a number  (-_-;)・・・")
        except Exception as e:
            print(f"{Fore.RED}Unexpected Error: {e}  (-_-;)・・・")

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
