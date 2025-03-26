Set shell = CreateObject("WScript.Shell")

' Step 1: Install python-vlc
shell.Run "cmd /c pip install python-vlc", 0, True

' Step 2: Clone the repository
shell.Run "cmd /c git clone https://github.com/Starman7312/internet_radio", 0, True

' Step 3: Navigate to the directory and run the script
shell.Run "cmd /c cd internet_radio\Internet Radio && python radio.py", 1, True