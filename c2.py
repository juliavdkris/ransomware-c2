from bottle import post, request, HTTPError, run
import json

import config


@post('/sendkey')
def index():
	if request.json:
		uuid = request.json['uuid']
		key = request.json['key']

		with open('keys.json', ) as file:
			keys = json.load(file)
		keys[uuid] = {'key': key}
		with open('keys.json', 'w') as file:
			json.dump(keys, file)



run(host='localhost', port=8000, reloader=True, debug=config.DEBUG, interval=0.1)