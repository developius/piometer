#!/usr/bin/python3

# import the necessary components
from flask import Flask, request, jsonify
app = Flask(__name__)

# define a dictionary to store our information in
info = {}

# listen for data at /data
@app.route("/data", methods=["GET", "POST"])
def api():
	# convert the data to a dict
	data = request.get_json(silent=True)

	# pretty debug
	print("%s sent: %s" % (data['uuid'], data['stats']))

	# replace the old data with the new data
	info[data['uuid']] = {'cpu': data['stats']['cpu'], 'mem': data['stats']['memory']}

	# keep count of the CPU and memory across all devices
	totalCpu = 0
	totalMem = 0

	# loop through all devices
	for key, stats in info.items():
		# add the CPU and memory to their respective counters
		totalCpu += stats['cpu']
		totalMem += stats['mem']

	# calculate means
	meanCpu = totalCpu / len(info)
	meanMem = totalMem / len(info)

	# more nice debugging
	print("Mean CPU: %s" % meanCpu)
	print("Mean memory: %s" % meanMem)

	# tell the client that all is well
	return(jsonify({"message": "ok"}))

# if file is called directly...
if __name__ == "__main__":
	# ...start the server on port 8742
	app.run(port=8742, host="0.0.0.0")
