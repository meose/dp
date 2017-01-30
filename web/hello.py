def app(environ, start_response):
    data = environ['QUERY_STRING'].split('&')
    for i in range(len(data)):
    	data[i] += "\n"
    	data[i] = bytes(data[i], "utf-8")
    	print(bytes(data[i]))
    start_response('200 OK', [('Concept-Type', 'text/plain')])
    return iter(data)
