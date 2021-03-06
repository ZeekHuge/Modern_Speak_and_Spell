#!/bin/sh
# This script is mainly to install and update all the dependencies for this project.

# Checking for root access
if [ "$EUID" -ne 0 ]; then
    echo "Requires root to install dependencies. Use : sudo setup.sh"
    exit 1
fi

# Install espeak
apt-get install -y espeak

# Installing pyaudio
apt-get install -y libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0
apt-get install -y ffmpeg libav-tools
pip install pyaudio

# Installing Wave
pip install Wave

# Installing pygame
python3 -m pip install -U pygame --user

# Installing PyDictionary
pip install PyDictionary
