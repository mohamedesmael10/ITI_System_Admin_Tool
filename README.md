# Python Project: System Administration Tool

This is a Python-based project offering both graphical user interface (GUI) and terminal-based interaction for system administration tasks.

---

## Features
- **GUI Interface:** Simplified navigation for system tasks using tkinter.
- **Terminal Interface:** Command-line access to essential functionalities.
- **Interactive Menu:** Easy-to-use options to choose your desired interface.

---

## Requirements
The project requires the following dependencies:
- **Python**: Version 3.x
- **tkinter**: For GUI interface.
- **colorama**: For colorful output in the terminal.

### Install Dependencies
Ensure the following are installed in your environment:

1. Install `colorama`:
   ```bash
   pip install colorama
   ```

2. Install `tkinter`:
   
   For Debian/Ubuntu:
   ```bash
   sudo apt-get install python3-tk
   ```
   For Fedora/RHEL:
   ```bash
   sudo dnf install python3-tkinter
   ```
   

   For macOS:
   
   tkinter is included by default with Python installation. If not:
   ```bash
   brew install python-tk
   ```

   For Windows:
   
   Ensure you have the latest version of Python from [python.org](https://www.python.org).

---

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/mohamedesmael10/ITI_System_Admin_Tool.git
   cd ITI_System_Admin_Tool
   ```

   ```bash
   cd ITI_System_Admin_Tool
   ```

2. Run the main script:
   ```bash
   python3 menu.py
   ```

3. Follow the menu to:
   - Launch the GUI.
   - Open the terminal interface.
   - Exit the application.

---

## Structure
```
ITI_System_Admin_Tool/
├── menu.py         # Main entry point
├── GUI
│   ├── gui_main.py
│   ├── task1_monitor_resources.py
│   ├── task2_list_directory.py
│   └── task3_exit_tool.py
│
└── Terminal
│   ├── main_menu.py
│   ├── task1_monitor_resources.py
│   ├── task2_list_directory.py
│   └── task3_exit_tool.py
└── README.md       # Project documentation
```

---

**Mohamed Esmael**
