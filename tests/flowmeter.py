
# a test script to read digital input from a flowmeter

print "starting script"

open('/sys/class/gpio/export', 'w').write("48")
open('/sys/class/gpio/gpio48/direction', 'w').write("in")

valuef = open('/sys/class/gpio/gpio48/value', 'r')
last = valuef.read()
valuef.close()

total = 0

while True:
	try:
		valuef = open('/sys/class/gpio/gpio48/value', 'r')
		val = valuef.read()
		valuef.close()
		if val != last:
			last = val
			total+=1
			print(total)
	except KeyboardInterrupt:
		open('/sys/class/gpio/unexport', 'w').write("48")
		break