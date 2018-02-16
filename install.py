import configparser

# Set desktop icons to 96 by 96
LIBFM_CONFIG_FILE = '/home/pi/.config/libfm/libfm.conf'
libfmconfig = configparser.ConfigParser()
libfmconfig.read(LIBFM_CONFIG_FILE)
libfmconfig['ui']['big_icon_size'] = "96"
with open(LIBFM_CONFIG_FILE, 'w') as configfile:
	libfmconfig.write(configfile)


# Remove wastebasket
PCMANFM_CONFIG_FILE = '/home/pi/.config/pcmanfm/LXDE-pi/desktop-items-0.conf'
pcmanfmconfig = configparser.ConfigParser()
pcmanfmconfig.read(PCMANFM_CONFIG_FILE)
pcmanfmconfig['*']['show_trash'] = "0"
pcmanfmconfig['*']['wallpaper'] = "/usr/share/rpd-wallpaper/road.jpg"
pcmanfmconfig['go.desktop']['x'] = "13"
pcmanfmconfig['go.desktop']['y'] = "61"
with open(PCMANFM_CONFIG_FILE, 'w') as configfile:
	pcmanfmconfig.write(configfile)

# Set count to 0
launcherconfig = configparser.ConfigParser()
launcherconfig.read('/home/pi/.activity_launcher/config.ini')
launcherconfig['Data']['Count'] = "0"
with open('/home/pi/.activity_launcher/config.ini', 'w') as configfile:
	launcherconfig.write(configfile)