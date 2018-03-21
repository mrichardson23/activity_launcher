# This is used for possible future functionality where tips can appear next to the Thonny window.

import subprocess
from time import sleep

# Get Thonny Process ID

while True:
	myProcess = subprocess.run(['xwininfo', '-root', '-tree'], stdout=subprocess.PIPE, universal_newlines=True)
	outputString = str(myProcess.stdout)
	ThonnyFound = False
	for line in outputString.split("\n"):
		if "Thonny" in line:
			ThonnyFound = True
			try:
				windowInfo = line.split(" ")
				position = windowInfo[25].split("+")
				xpos = position[1]
				ypos = position[2]
				size = windowInfo[23]
				width = size[0:size.find("x")]
				height = size[size.find("x")+1:size.find("+")]
				print("x: " + xpos + " y: " + ypos + " width: " + width + " height: " + height)
			except:
				print("Problem with this one:")
				print(windowInfo)
	if ThonnyFound is False:
		print("No Thonny window Found")
	sleep(.03)
	
