import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import os

import helpers

file_types = {
    "Script files": "*.sh *.bat"
}

script_list = []

class ExecuteScriptsWindow:
  def __init__(self, root):
    self.root = root
    self.root.title("Execute scripts")
    self.root.resizable(width=False, height=False)
    self.label_width = 20
    self.button_width = 20
    self.setup_window()
    self.fill_combobox()

  def setup_window(self):
    self.top_frame = tk.Frame(self.root)
    self.top_frame.pack(anchor="n", fill='x', padx=5, pady=5)
    self.combobox = ttk.Combobox(self.top_frame, width=self.button_width)
    self.combobox.pack(fill='x')
    
    self.bottom_frame = tk.Frame(self.root)
    self.bottom_frame.pack(anchor="s")
    self.run_script_button = tk.Button(
            self.bottom_frame,
            text="Run",
            command=lambda: self.start_script(),
            width=self.button_width,
        )
    self.run_script_button.grid(row=0, column=1, padx=5, pady=5)

    self.add_new_button = tk.Button(
            self.bottom_frame,
            text="Add new",
            command=lambda: self.add_new_script(),
            width=self.button_width,
        )
    self.add_new_button.grid(row=1, column=1, padx=5, pady=5)

    self.remove_button = tk.Button(
            self.bottom_frame,
            text="Remove",
            command=lambda: self.remove_script(),
            width=self.button_width,
        )
    self.remove_button.grid(row=1, column=0, padx=5, pady=5)

  def start_script(self):
    print("Start script")
    file_name = self.combobox.get()
    helpers.execute_script(file_name)

  def add_new_script(self):
    print("Add new script")
    file_types_formated = [(desc, patterns) for desc, patterns in file_types.items()]
    file_path = filedialog.askopenfilename(
      title="Select a script file",
      filetypes=(file_types_formated)
    )
    if not file_path:
      return
    
    file_name = os.path.basename(file_path)
    script_list = helpers.read_script_list_json() or []
    script_list.append(file_name)

    if(helpers.check_for_duplicates_in_list(script_list)):
      messagebox.showwarning("Warning", f"Script with the name {file_name} already exists in the list")
      return
    
    destination_path = os.path.join(os.getcwd(), "Scripts")
    helpers.copy_script_to_local_folder(file_path, destination_path, file_name)
    helpers.write_script_list_json(script_list)

    self.combobox["values"] = script_list

  def remove_script(self):
    print("Removing script")
    file_name = self.combobox.get()
    helpers.remove_script_from_folder(file_name)
    self.combobox.set("")
    self.fill_combobox()

  def fill_combobox(self):
    loaded_list = helpers.read_script_list_json()
    self.combobox["values"] = loaded_list or []