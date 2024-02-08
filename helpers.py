import json
import os
import sys
import shutil
import subprocess

def execute_script(file_name):
  script_path = os.path.join(os.getcwd(), "Scripts")
  script_path = os.path.join(script_path, file_name)

  print(f"{script_path}")
  try:
    if sys.platform == "win32":
      subprocess.Popen(['cmd', '/k', 'start', script_path], shell=True)
    elif sys.platform == "linux":
      terminal_command = ["x-terminal-emulator", "-e", script_path]
    elif sys.platform == "darwin":
      terminal_command = ["open", "-a", "Terminal", script_path]
  except Exception as e:
    print(f"Error occoured while running the script, E: {e}")

def write_script_list_json(script_list):
  try:
      with open("script_list.json", "w") as f:
        json.dump(script_list, f)
  except Exception as e:
    print(f"Error occoured while opening the file E: {e}")
    return

def read_script_list_json():
  list = find_all_script_files()
  
  if len(list) == 0:
    try:
      with open("script_list.json", "w") as f:
        json.dump([], f)
    except Exception as e:
      print(f"Error occoured while deleting file content E: {e}")
    return 
  
  try:
    with open("script_list.json", "r") as f:
      return json.load(f) 
  except Exception as e:
    print(f"Error occoured while loading the file E: {e}")
    return
  
def find_all_script_files():
  files_only = []
  folder_path = os.path.join(os.getcwd(), "Scripts")
  
  if(not os.path.exists(folder_path)):
    return files_only
  
  files_in_folder = os.listdir(folder_path)
  files_only = [file for file in files_in_folder if os.path.isfile(os.path.join(folder_path, file))] 

  return files_only

def check_for_duplicates_in_list(list):
  return any(list.count(item) > 1 for item in list)

def copy_script_to_local_folder(file_path, destination_path, file_name):
  try:
    if not os.path.exists(destination_path):
      os.makedirs(destination_path)
  except:
    print(f"Error occoured trying to create a folder, E: {e}")
      
  destination_path = os.path.join(destination_path, file_name)
    
  try:
    shutil.copy(file_path, destination_path)
    print(f"File '{file_name}' copied successfully to '{destination_path}'")
  except Exception as e:
    print(f"Error occoured trying to copy a file, E: {e}")

def remove_script_from_folder(file_name):
  folder_path = os.path.join(os.getcwd(), "Scripts")
  file_path = os.path.join(folder_path, file_name)

  try:
    if os.path.exists(file_path):
      os.remove(file_path)
      print(f"File '{file_path}' deleted successfully.")
    else:
      print(f"File '{file_path}' does not exist.")
  except Exception as e:
    print(f"Error occoured trying to delete a file, E: {e}")
