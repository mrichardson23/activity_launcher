#!/bin/sh

cd ~
git clone https://github.com/mrichardson23/activity_launcher .activity_launcher
mv /home/pi/.activity_launcher/go.desktop /home/pi/Desktop/go.desktop
python3 home/pi/.activity_launcher/install.py