import sys, os, pickle, thread, datetime
import TwitterAuth
from twython import Twython

# run.py - run this when you are ready to begin gathering data from the keg

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

# define unit class
class unit:
	name = ""
	value = 0

# grab unit value of 1 liter (done by calibrate.py)
try:
	u = pickle.load(open(os.getcwd() + '/../config/unit.txt', 'r'))
except IOError:
	print "please run the calibration file, then restart this script"
	print "(calibration file located at Keglebone/src/calibrate.py)"
	sys.exit()

print "starting script"
print "unit: " + u.name
print "value: {}".format(u.value)
print "ready to collect data!"

# begin polling GPIO file for pulses 
while True:
	try:
		valuef = open('/sys/class/gpio/gpio48/value', 'r')
		val = valuef.read()
		valuef.close()
		if val != last:
			last = val
			totalPulses+=1
			if totalPulses % u.value == 0:
				n = totalPulses // u.value
				ts = datetime.datetime.now().strftime("%I:%M%p - %m/%d/%Y")
				twitter.update_status(status='just measured {} {}s at {}'.format(n, u.name, ts))
			print(totalPulses)
	except KeyboardInterrupt:
		# upon keyboard interrupt, unexport GPIO pin 48
		open('/sys/class/gpio/unexport', 'w').write("48")
		break

#twitter.update_status(status='test')
