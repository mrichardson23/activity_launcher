#!/usr/bin/python3

import configparser
import shutil
import subprocess
from guizero import App, Picture, Text
import os

# Set the home path for files to the director of this script:
home_path = os.path.dirname(os.path.realpath(__file__)) + "/"

# Set up configuration file parser:
config = configparser.ConfigParser()
config.read(home_path + 'config.ini')

# Close Thonny and any running sparkle programs forcefully if open:
os.system("pgrep -f myProgram | xargs kill")
# (this is a total hack. Killing thonny alone doesn't kill running sparkles.)

# Clear the Sense HAT
from sense_hat import SenseHat
sense = SenseHat()
sense.clear()

#### Splash Screen ####
if config['SplashScreen']['enabled'] == "True":
	splashApp = App(width=int(config['SplashScreen']['imageWidth']), height=int(config['SplashScreen']['imageHeight']), title=config['SplashScreen']['titleBarCaption'])

	def onClick(event):
		# This handles clicks to advance the frames of the animation and to start the activity:
		global currentFrame
		if currentFrame  < int(config['SplashScreen']['frames']):
			nextFrame()
		else:
			splashApp.destroy()

	def onKeyPress(event):
		# This will show the number of launches in the menu bar.
		if event.char == "C":
			splashApp.title = (config['Data']['count'])

	def nextFrame():
		# Frame advancer
		global currentFrame
		if currentFrame  < int(config['SplashScreen']['frames']):
			picture.cancel(nextFrame) # necessary so that a click will advance the frame, but cancel the previously scheduled advance
			currentFrame = currentFrame + 1
			picture.value = home_path + str(currentFrame) + config['SplashScreen']['imageFile']
			picture.after( int(config['SplashScreen']['animateSecondsPerFrame']) * 1000, nextFrame )

	currentFrame = 1
	picture = Picture(splashApp, image=home_path + str(currentFrame) + config['SplashScreen']['imageFile'])
	timer = picture.after( int(config['SplashScreen']['animateSecondsPerFrame']) * 1000, nextFrame ) # kick off the animation
	splashApp.tk.bind("<Key>", onKeyPress) # bind keypresses to the handler
	splashApp.tk.bind("<Button-1>", onClick) # Bind mouseclicks to the handler
	splashApp.display()

#### IDE Launch ####

# Take the starter file and move it into place, overwriting the file that's there:
shutil.copyfile(home_path + config['Activity']['starterFile'], config['Activity']['newFileLocation'] + config['Activity']['newFileName'] )

# Update launch count in the config file:
count = int(config['Data']['count'])
count = count + 1
config['Data']['count'] = str(count)
with open(home_path + 'config.ini', 'w') as configfile:
	config.write(configfile)

# Move IDE configuration files into place
shutil.copyfile(home_path + config['Activity']['freshIDEConfigFileName'], config['Activity']['IDEConfigDestination'] + config['Activity']['IDEConfigFileName'] )

# Launch the editor with the new file
activityProcess = subprocess.run( [config['Activity']['launchCommand'], config['Activity']['newFileLocation'] + config['Activity']['newFileName']] )

#### Golden Screen ####

# Check how much larger the user's file is from the one we started them with:
fileSizeDifference = os.path.getsize(config['Activity']['newFileLocation'] + config['Activity']['newFileName']) - os.path.getsize(home_path + config['Activity']['starterfile'])

#Checking for returncode 0 is a way to make sure the golden screen pops up when user closes the window, as opposed to it being killed.
if activityProcess.returncode == 0 and config['GoldenScreen']['enabled'] == "True": 
	#Check if the file is bigger by the threshold amount:
	if fileSizeDifference > int(config['GoldenScreen']['fileSizeThreshold']):
		# Launch Golden Screen
		goldenApp = App(width=int(config['GoldenScreen']['imageWidth']), height=int(config['GoldenScreen']['imageHeight']), title=config['GoldenScreen']['titleBarCaption'])

		def closeWindow(event):
			goldenApp.destroy()

		picture = Picture(goldenApp, image=home_path + config['GoldenScreen']['imageFile'])
		goldenApp.tk.bind("<Button-1>", closeWindow)
		goldenApp.display()
	else:
		pass
		#failed file size check
