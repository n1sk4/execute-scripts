import tkinter as tk
import execute_scripts_window 

root = tk.Tk()

if __name__ == "__main__":
  app = execute_scripts_window.ExecuteScriptsWindow(root)
  print("Running...")

root.mainloop()