
try:
    from colorama import Fore, Style
except ImportError:
    class DummyColor:
        def __getattr__(self, name):
            return ""
    Fore = Style = DummyColor()
import sys

def exit_tool():
    """Exit the tool safely"""
    try:
        print(f"\n{Fore.MAGENTA}Thank you for using the System Administration Tool, Goodbye ヽ(･_･ ) (･_･)/")
        sys.exit(0)
    except Exception as e:
        print(f"{Fore.RED}Error: Unable to exit the tool, Details: {e} (-_-;)")
        sys.exit(1)
