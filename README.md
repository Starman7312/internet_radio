# internet_radio
An internet-streaming based radio player, using the VLC framework to stream the radio  

Provides a text based interface for controlling the radio, with these feature:  

    • tune - connects to selected station (runs by default on boot of radio.py)
    • fine tune - allows for selection of specific URL radio stream
    • stop - stops the current playback
    • resume - resumes the current playback (live, not from stop point)
    • volume - allows for radio volume control (application volume level, not speakers)
    • exit - exits playback

Automatic Setup:  
Windows install can be run by downloading and opening one of the **windows_installer files** located here: https://github.com/Starman7312/internet_radio/tree/9addb45271b1ce3dac4310aadd65fc59991fed74/Automatic%20Installers/Windows  
• Recommended downloads are **windows_installer.ps1** or **windows_installer.vbs** (as windows_installer.bat is *hard* to download / often blocked)  
• If you recieve any warnings while trying to download the install files, select keep (they're safe)  
• You can also just copy the **windows_installer.bat** file contents and paste into a terminal to run  

Manual Setup:  
• Install **VLC media player** (https://www.videolan.org/vlc/)  
• May already be installed in some OS's (e.g. Linux)  

Then:  
• Windows:  
    ---- Install the vlc python library via this command line:
    
    pip install python-vlc
    
• Linux or other similar OS:  
    ---- Install the vlc python library via this command line:

    sudo apt-install python3-vlc
        
• Download both files in the **Internet Radio** folder:  


• If using git, run this via command line to download

    git clone https://github.com/Starman7312/internet_radio

Then navigate to installation:

    cd internet_radio/Internet Radio

Then run (Windows Only):

    python radio.py

Then run (Linux etc.):

    python3 radio.py
   
Otherwise, manually download:  
    • Make sure to have both the **radio.py** and **stations.py** files in the same folder (as radio is dependant on stations)  
    • Then just run the code file named **radio.py** and you should be up and running

Note:  
• Comes with a few radio stations pre-installed (BBC etc.), but you can add more  
• Pages such as this are great for finding the radio stations URL's: https://en.everybodywiki.com/List_of_BBC_radio_stream_URLs  
• Or you can often get them directly from the station or a search for something like: radio stream URL for StationXXXX  
