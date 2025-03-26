#!/bin/bash

echo "Installing python-vlc..."
sudo apt-get install python3-vlc

echo "Cloning repository..."
git clone https://github.com/Starman7312/internet_radio

echo "Navigating to the repository directory..."
cd "$(dirname "$0")/internet_radio/Internet Radio"

echo "Running the Python script..."
python3 radio.py
