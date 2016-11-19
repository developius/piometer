#!/usr/bin/python3

import time
from gpiozero import AngularServo

cpu = AngularServo(7)	#one on left
ram = AngularServo(25)	#one on right

cpu.detach() 	#Detach servos to prevent "juddering"
ram.detach()

def pushToServos(cpuVal, ramVal):
	print("Received {} cpu, {} ram".format(cpuVal, ramVal))
	move(cpuVal, ramVal)

def move(cpuVal, ramVal):
	cpuVal = (cpuVal * -1.4) + 70 #map percentages to relevant servo values
	ramVal = (ramVal * -1.4) + 70 + 15 #same as above, minus servo offset	

	cpu.angle = cpuVal
	ram.angle = ramVal
	
	time.sleep(0.5)	#Allow servo to reach new position before detaching
	cpu.detach()	#Detach servos to prevent "juddering"
	ram.detach()	
	time.sleep(0.5) #Sleep so that if move() contantly called, no judder occurs

