from bottle import post, request, HTTPError, run
import json

import config


@post('/')
def index():
	if request.json:
		key = request.json['key']
		print(key)


run(host='localhost', port=8000, reloader=True, debug=config.DEBUG, interval=0.1)