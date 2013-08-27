import time

open('/sys/class/gpio/export', 'w').write("30")
open('/sys/class/gpio/gpio30/direction', 'w').write("out")

while True:
	value = open('/sys/class/gpio/gpio30/value', 'w')
	value.write("1")
	value.close()
	time.sleep(0.05)
	value = open('/sys/class/gpio/gpio30/value', 'w')
	value.write("0")
	value.close()
	time.sleep(0.05)

open('/sys/class/gpio/unexport', 'w').write("30")