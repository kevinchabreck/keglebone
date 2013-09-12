import sys, os
import TwitterAuth
from twython import Twython

# fetch a Twitter object authorized to an account 
twitter = TwitterAuth.getTwitter()

# initialize GPIO pin 48 as an input pin
open('/sys/class/gpio/export', 'w').write("48")
open('/sys/class/gpio/gpio48/direction', 'w').write("in")

# read the initial value of the pin
valuef = open('/sys/class/gpio/gpio48/value', 'r')
last = valuef.read()
valuef.close()

# initialize pulse counter
totalPulses = 0

print "starting script"

# begin polling GPIO file for pulses 
while True:
	try:
		valuef = open('/sys/class/gpio/gpio48/value', 'r')
		val = valuef.read()
		valuef.close()
		if val != last:
			last = val
			totalPulses+=1
			print(totalPulses)
	except KeyboardInterrupt:
		# upon keyboard interrupt, unexport GPIO pin 48
		open('/sys/class/gpio/unexport', 'w').write("48")
		break

#twitter.update_status(status='test')
