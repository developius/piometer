# this code is modified from https://github.com/Boeeerb/PiGlow/blob/master/Examples/cpu.py and was originally written by @Boeeerb

# load requirements
import piglow
from time import sleep
import psutil

# loop forever
while True:

	# get CPU percentage
	cpu = psutil.cpu_percent()
	
	# reset PiGlow
	piglow.all(0)

	if cpu < 5:
		piglow.white(20)
	elif cpu < 20:
		piglow.white(20)
		piglow.blue(20)
	elif cpu < 40:
		piglow.white(20)
		piglow.blue(20)
		piglow.green(20)
	elif cpu < 60:
		piglow.white(20)
		piglow.blue(20)
		piglow.green(20)
		piglow.yellow(20)
	elif cpu < 80:
		piglow.white(20)
		piglow.green(20)
		piglow.blue(20)
		piglow.orange(20)
		piglow.red(20)
	else:
		piglow.all(20)
		piglow.show()
		
	# add little sleep
	sleep(0.1)
