# main.py
import tkinter as tk
from gui import InodeVisualizerApp

def main():
    root = tk.Tk()
    app = InodeVisualizerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
