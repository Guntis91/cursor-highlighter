# Cursor Highlighter (Windows)



## Overview



Cursor Highlighter is a lightweight Windows overlay tool designed for **screen recordings, tutorials, and guide videos**.



It improves cursor visibility by displaying a **yellow ring** around the mouse pointer and showing a **red click animation** whenever the left mouse button is pressed.



The application is **visual only**:

- It does **not** automate clicks

- It does **not** modify mouse behaviour

- It is safe to use while recording





## Features



- Always-on-top transparent overlay  

- Yellow ring follows the mouse cursor  

- Red shrinking circle animation on left click  

- Works across multiple monitors  

- Lightweight and simple to use  





## Requirements



- Windows 10 or Windows 11  

- Python installed on the system  



### Python Packages Used



- Pillow  

- pyautogui  

- pywin32  

- screeninfo  





## Folder Structure



The files **must remain in this structure** for the application to work correctly.



```text

cursor-highlighter

│

├─ cursor_highlighter.py

├─ Start_CursorApp.bat

├─ requirements.txt

├─ README.md

├─ LICENSE

│

└─ assets

&nbsp;  └─ yellow_ring_small.png

```


## Installation


1. Make sure Python is installed

2. Open a terminal or command prompt inside the project folder

3. Install required packages:


Copy code

```bat

pip install -r requirements.txt

```

## Starting the App (Recommended)


The recommended way to start the application is by using the batch file.


1. Double-click Start_CursorApp.bat

2. The cursor highlighter will start immediately

3. You can create a desktop shortcut to the BAT file for one-click launching


This is the same launch method used by the author.


## Important: Batch File Path Setup

The Start_CursorApp.bat file contains a hard-coded folder path.

You must edit this path to match where the project is located on your computer.


## Example: Current BAT File Content


Copy code

```bat

@echo off

cd /d D:\CursorApp

python cursor_highlighter.py

```

If your project is not located at D:\CursorApp, this will not work.


## Example: Desktop Location


Copy code

```bat

@echo off

cd /d C:\Users\YourName\Desktop\cursor-highlighter

python cursor_highlighter.py

```

After editing and saving the file, double-click the BAT file again to start the app.


## Closing the App


- Press Alt + F4
- Or close the terminal window started by the BAT file



## Notes


- Intended for tutorials, guides, and presentations
- Visual overlay only, no automation
- Safe to use during screen recording


## License

This project is licensed under the MIT License.

You are free to use, modify, and share it.

