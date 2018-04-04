# Raspberry Pi Foundation Drop-in Activity Launcher for Events
## Installation
    curl -L http://bit.ly/activity_launcher | bash
This inelegant install script will clone this repo into `~/.activity_launcher`, create a desktop icon, install guizero, create a Thonny preferences directory, and set the counter to zero.
## Configuration
Configuration options are found in `config.ini`
## Event Set up
Below are some rough notes for what I do in order to get this ready for an event:

Raspberry Pi > Preferences > Raspberry Pi Configuration:
Disable underscan if needed
Set keyboard to US English
Select Wifi Country if needed

Connect to Wifi, install activity launcher (instructions above)

Raspberry Pi > Preferences > Appearance Settings >
Desktop tab:
Layout: Center image on sceen
Picture: select `raspberry-pi-logo.png`
Change text color to Raspberry Red: `R 197 G 26 B 74` or `#c51a4a`
Uncheck Wastebasket to hide it from the desktop.

Raspberry Pi > Preferences > Main Menu Editor
Uncheck the "show" box next to Games if you wish to hide that

Open a file browser window:
Click Edit... Preferences
Under Display, update size of large icons to 96 x 96 

Open the file: `/home/pi/.config/pcmanfm/LXDE-pi/desktop-items-0.conf`
Update the value for `desktop_font` to `Piboto Bold 18`

Right click on taskbar launcher icons, click "Application Launch Bar Settings"
Hide any icons you don't want on the taskbar.
