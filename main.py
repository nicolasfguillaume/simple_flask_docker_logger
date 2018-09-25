# -*- coding: utf-8 -*-
import os
import subprocess
from flask import Flask
from flask import jsonify


app = Flask(__name__)


def get_output(cmd):
	output = subprocess.check_output(cmd, shell=True)
	return output.split('\n')


@app.route("/list")
def get_names():
	output = get_output("docker ps --format '{{.Names}}'")
	return '<br>'.join(['<a href=/logs/' + item + '>' + item + '</a>' for item in output])
	

@app.route("/logs/<container_name>")
def get_logs(container_name):
	return jsonify(get_output("docker logs --tail 1000 {}".format(container_name)))

 
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5001, debug=True)
