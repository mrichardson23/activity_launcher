#!/bin/sh

cd ~
git clone https://github.com/mrichardson23/activity_launcher.git .activity_launcher
cp /home/pi/.activity_launcher/go.desktop /home/pi/Desktop/go.desktop
python3 /home/pi/.activity_launcher/install.py
