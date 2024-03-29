# Execute Scripts
Multiplatform Desktop app for managing script execution.

# Dependencies and Build
Python 3.11 installed.

## Install libraries
```
 pip install tkinter
 pip install subprocess

 pip install pyinstaller
```

## Start Virtual Environment

```
  py -3 -m venv .venv
  .venv\Scripts\activate
```

## Visual Studio Code
You can run the project by having all files from the repo in the same root.
Build app.py

## Build using PyInstaller
The following command should be ran from the root folder:
```
pyinstaller --name="execute-scripts" --onefile app.py
```
The command creates a few folders in the root, the important one is the .\dist

# Screenshots
<img src=https://github.com/n1sk4/execute-scripts/assets/92214769/7e32f66f-398c-4cd9-a3c9-d3d049b54cf1 alt="drawing" width="450"/>
