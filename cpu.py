import piglow
from time import sleep
import psutil

piglow.auto_update = True

while True:
	cpu = psutil.cpu_percent()
	#piglow.all(0)

	if cpu < 5:
		piglow.all(0)
	if cpu > 10:
		piglow.white(20)
	if cpu > 20:
		piglow.blue(20)
	if cpu > 40:
		piglow.green(20)
	if cpu > 60:
		piglow.yellow(20)
	if cpu > 80:
		piglow.orange(20)
	if cpu > 90:
		piglow.red(20)

	piglow.show()
	sleep(0.01)
