#!/usr/bin/python3

# get requirements
import requests, psutil
from time import sleep

server = "dockerpi.local"

# forever do...
while True:
	# get CPU and memory usage
	cpu = psutil.cpu_percent()
	mem = psutil.virtual_memory().percent

	# update server
	res = requests.post('http://'+server+':8742/data', json={"uuid":"dockerpi-node-1", "stats": {"cpu": cpu, "memory": mem}})
	if res.ok:
		print(res.json())

	# do a little sleep
	sleep(0.5)
