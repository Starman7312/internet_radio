#!/bin/bash
echo "Installing python-vlc..."
sudo apt-install python3-vlc

echo "Cloning repository..."
git clone https://github.com/Starman7312/internet_radio

echo "Navigating and running the script..."
cd internet_radio/Internet Radio
python3 radio.py