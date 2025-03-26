# internet_radio
An internet-streaming based radio player, using the VLC framework to stream the radio  

Provides a text based interface for controlling the radio, with these feature:  

    • tune - connects to selected station (runs by default on boot of radio.py)
    • fine tune - allows for selection of specific URL radio stream
    • stop - stops the current playback
    • resume - resumes the current playback (live, not from stop point)
    • volume - allows for radio volume control (application volume level, not speakers)
    • exit - exits playback

----------------------------------------------------------------------------------------------------

## Dependancy:  
• Make sure **VLC media player** is downloaded (https://www.videolan.org/vlc/)  
• May already be installed in some OS's (e.g. Linux)

----------------------------------------------------------------------------------------------------

## Automatic Setup:  

### Windows Install:  
> Can be installed using **windows_installer files** located here: [windows_installer](https://github.com/Starman7312/internet_radio/tree/02032895425020bbc481dde72ef0498992a3021c/Automatic%20Installers/Windows)
> 
> Recommended install file is **windows_installer.vbs** or **windows_installer.ps1** (as .bat file can be difficult to download)  
> If you recieve any warnings while trying to download and/or run the install files, select keep / run (they're safe) 

### Linux (or similar) Install:  
> Can be installed by downloading the **linux_installer.sh** file, located here: [linux installer](https://github.com/Starman7312/internet_radio/blob/e92258c32b95f6edf25f62e8047b2a816145ccec/Automatic%20Installers/Linux%20(or%20similar)/linux_installer.sh)
> 
> To run the file, you will first need to make it executable, via these commands:
>
>     cd Downloads # Replace with your download folder, if not Downloads
>     chmod +x linux_installer.sh  
> Then just open the file (in the desired install location) and the software will install and run  

----------------------------------------------------------------------------------------------------

## Command Line Download:
### Windows:
> Install the code via these command line instructions:
    
    pip install python-vlc
    git clone https://github.com/Starman7312/internet_radio
    cd internet_radio/Internet Radio
    python radio.py
    
### Linux or other similar OS:
> Install the code via these command line instructions:

    sudo apt-install python3-vlc
    git clone https://github.com/Starman7312/internet_radio
    cd "internet_radio/Internet Radio"
    python3 radio.py

----------------------------------------------------------------------------------------------------
    
## Manual Download:  
> Make sure to have both the **radio.py** and **stations.py** files in the same folder (as radio is dependant on stations)  
> Then just run the code file named **radio.py** and you should be up and running

----------------------------------------------------------------------------------------------------

## Running Post-Install:
• The source python file has now been installed, and can be run  
• It can be located at:

    "cwd/internet_radio/Internet Radio/radio.py" # replace cwd with the directory used for installing

Alternatively, you can run it using the installed **Run Files**, which when opened will run the software
> These can be located at: *cwd/internet_radio/Run Files/Windows/Radio.bat* or *cwd/internet_radio/Run Files/Windows/Radio.sh*
> # replace cwd with the directory used for installing
> - E.g. Windows:
```
cd "Downloads/internet_radio/Run Files/Windows"
Radio.bat
```
>
> - Linux:
>
```
cd "cwd/internet_radio/Run Files/Windows" # replace cwd with the directory used for installing
Radio.sh
```
>   

**Note: You can create a shortcut to the Run File, to allow for the program to be launched from another location (e.g. Desktop)**

----------------------------------------------------------------------------------------------------

## Notes:  
• Comes with a few radio stations pre-installed (BBC etc.), but you can add more  
• Pages such as this are great for finding the radio stations URL's: https://en.everybodywiki.com/List_of_BBC_radio_stream_URLs  
• Or you can often get them directly from the station or a search for something like: radio stream URL for StationXXXX  
