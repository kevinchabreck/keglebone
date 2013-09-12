import os, pickle

# a script for calibrating the flowmeter
#
# this script will ask you to input the name of the desired unit, and then ask
# to record a series of calibration runs. It will measure the pulses from each 
# run, average them, and write the resulting unit/value pair to a file called 
# unit.txt

print "\nKeglebone Calibration Tool\n"
unitName = raw_input('enter the name of the unit you wish to measure: ')

# prepare pin 
open('/sys/class/gpio/export', 'w').write("48")
open('/sys/class/gpio/gpio48/direction', 'w').write("in")
valuef = open('/sys/class/gpio/gpio48/value', 'r')
last = valuef.read()
valuef.close()

# initialize vars
trials = []
totalPulses = 0

print 'Preparing to gather data. Press ctrl + c when done with each trial'

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
		valid = raw_input('keep this run? (y/n) ')
		if valid == 'y':
			print 'adding run to batch'
			trials.append(totalPulses)
		proceed = raw_input('run again? (y/n)')
		if proceed == 'y':
			totalPulses = 0
		else:
			open('/sys/class/gpio/unexport', 'w').write("48")
			break

class unit:
	name = unitName
	value = sum(trials)/trials.len

pickle.dump(unit, open(os.getcwd() + '/../config/unit.txt', 'w'))

unit2 = pickle.load(open(os.getcwd() + '/../config/unit.txt', 'r'))
print 'unit: ' + unit2.name
print "value: {}".format(unit2.value)
