from bottle import route, run, template
import config


@route('/')
def index():
	test = {'a': 123, 'b': 456}
	return test


run(host='localhost', port=8000, reloader=True, debug=config.DEBUG)