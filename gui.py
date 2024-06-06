import tkinter as tk
from tkinter import filedialog, messagebox
from inode_analyzer import analyze_inodes
from visualizer import plot_inodes


class InodeVisualizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Inode Allocation Visualizer")

        self.label = tk.Label(root, text="Select Filesystem Path:")
        self.label.pack(pady=5)

        self.path_entry = tk.Entry(root, width=50)
        self.path_entry.pack(pady=5)

        self.browse_button = tk.Button(root, text="Browse", command=self.browse)
        self.browse_button.pack(pady=5)

        self.analyze_button = tk.Button(root, text="Analyze", command=self.analyze)
        self.analyze_button.pack(pady=20)

    def browse(self):
        path = filedialog.askdirectory()
        if path:
            self.path_entry.delete(0, tk.END)  # Clear the entry box before inserting new path
            self.path_entry.insert(0, path)

    def analyze(self):
        path = self.path_entry.get()
        if not path:
            messagebox.showwarning("Input Error", "Please select a filesystem path.")
            return

        print(f"Analyzing path: {path}")  # Debug statement
        try:
            inode_info = analyze_inodes(path)
            plot_inodes(inode_info)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to analyze inodes: {e}")
            print(f"Error: {e}")  # Debug statement


if __name__ == "__main__":
    root = tk.Tk()
    app = InodeVisualizerApp(root)
    root.mainloop()