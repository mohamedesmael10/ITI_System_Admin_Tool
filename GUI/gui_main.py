import tkinter as tk
from tkinter import messagebox, filedialog
import task1_monitor_resources
import task2_list_directory
import task3_exit_tool

class SystemAdminToolGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("System Administration Tool")
        self.root.geometry("600x400")
        self.root.resizable(False, False)

        # Title Label
        title_label = tk.Label(
            root,
            text="System Administration Tool",
            font=("Helvetica", 16, "bold"),
            pady=20,
        )
        title_label.pack()

        # Task Buttons
        task1_button = tk.Button(
            root, 
            text="Monitor System Resources", 
            font=("Helvetica", 12), 
            command=self.monitor_resources
        )
        task1_button.pack(pady=10)

        task2_button = tk.Button(
            root, 
            text="List Directory Contents", 
            font=("Helvetica", 12), 
            command=self.list_directory
        )
        task2_button.pack(pady=10)

        exit_button = tk.Button(
            root, 
            text="Exit the Tool", 
            font=("Helvetica", 12), 
            command=self.exit_tool
        )
        exit_button.pack(pady=10)

        # Output Area
        self.output_text = tk.Text(
            root, 
            wrap=tk.WORD, 
            height=10, 
            width=70, 
            state=tk.DISABLED
        )
        self.output_text.pack(pady=10)

    def monitor_resources(self):
        """Execute Task 1: Monitor system resources and display the output"""
        try:
            output = task1_monitor_resources.monitor_resources(gui=True)
            self.display_output(output)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to monitor resources.\n\n{e}")

    def list_directory(self):
        """Execute Task 2: List directory contents and display the output"""
        directory = filedialog.askdirectory(title="Select a Directory")
        if not directory:
            return
        try:
            output = task2_list_directory.list_directory(directory, gui=True)
            self.display_output(output)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to list directory contents.\n\n{e}")

    def exit_tool(self):
        """Exit the tool gracefully."""
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            task3_exit_tool.exit_tool()

    def display_output(self, message):
        """Display output in the text area."""
        self.output_text.configure(state=tk.NORMAL)
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, message)
        self.output_text.configure(state=tk.DISABLED)

# Main entry point
if __name__ == "__main__":
    root = tk.Tk()
    app = SystemAdminToolGUI(root)
    root.mainloop()
