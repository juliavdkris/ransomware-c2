from bottle import get, post, request, HTTPError, run
import json

import config


@post('/sendkey')
def sendkey():
	if request.json:
		uuid = request.json['uuid']
		key = request.json['key']

		with open('keys.json') as file:
			keys = json.load(file)
		keys[uuid] = {'key': key}
		with open('keys.json', 'w') as file:
			json.dump(keys, file)


@get('/getkey')
def getkey():
	if request.query:
		uuid = request.query['uuid']

		with open('keys.json') as file:
			keys = json.load(file)
		return keys[uuid]['key']


run(host='localhost', port=8000, reloader=True, debug=config.DEBUG, interval=0.1)