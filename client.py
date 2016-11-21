#!/usr/bin/python3

# get requirements
import requests, psutil
from time import sleep
import os, socket

hostname = socket.gethostname()
server = "dockerpi.local"

# forever do...
while True:
	# get CPU and memory usage
	cpu = psutil.cpu_percent()
	mem = psutil.virtual_memory().percent

	# update server
	res = requests.post('http://'+server+':8742/data', json={"uuid":hostname, "stats": {"cpu": cpu, "memory": mem}})
	if res.ok:
		print(res.json())
