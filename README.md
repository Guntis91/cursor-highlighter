\# Cursor Highlighter (Windows)



\## Overview



This is a lightweight Windows cursor highlighter designed for screen recordings, tutorials, and guide videos.

It makes the mouse cursor easier to see by displaying a yellow ring around it and showing a red click animation whenever the left mouse button is pressed.



The app does not automate clicks or change mouse behavior.

It is only a visual overlay for better visibility in recordings.





\## Features



• Always-on-top transparent overlay  

• Yellow ring follows the mouse cursor  

• Red shrinking circle animation on left click  

• Works across multiple monitors  

• Very lightweight and simple to use  





\## Requirements



• Windows 10 or Windows 11  

• Python installed on the system  



Python packages used:

• Pillow  

• pyautogui  

• pywin32  

• screeninfo  





\## Folder Structure



The files must stay in this structure for the app to work correctly.



cursor-highlighter  

│  

├─ cursor\_highlighter.py  

├─ Start\_CursorApp.bat  

├─ requirements.txt  

├─ README.md  

│  

└─ assets  

&nbsp;  └─ yellow\_ring\_small.png  





\## How to Install



1\. Make sure Python is installed on your system

2\. Open a terminal or command prompt inside the project folder

3\. Install required packages by running:



pip install -r requirements.txt





\## How to Start the App (Recommended)



\### The recommended way to start the app is using the batch file.



1\. Double-click Start\_CursorApp.bat

2\. The cursor highlighter will start immediately

3\. You can create a desktop shortcut to the BAT file for one-click launching



This is the same method used by the author.





Important: Batch File Path Setup



The Start\_CursorApp.bat file contains a hard-coded folder path.

You MUST edit this path to match where you place the project on your computer.



Example content of Start\_CursorApp.bat:



@echo off  

cd /d D:\\CursorApp  

python cursor\_highlighter.py  



If your project folder is NOT located at D:\\CursorApp, you must change that line.



For example, if the project is on your Desktop:



@echo off  

cd /d C:\\Users\\YourName\\Desktop\\cursor-highlighter  

python cursor\_highlighter.py  



After saving the file, double-click the BAT file again to start the app.





\## How to Close the App



• Press Alt + F4  

• Or close the terminal window started by the BAT file  





\## Notes



• The app is intended for tutorials, guides, and presentations

• It does not collect data or interact with other programs

• The overlay is visual only and safe to use during recording





\## License



This project is released under the MIT License.

You are free to use, modify, and share it.

Cursor Highlighter (Windows)



