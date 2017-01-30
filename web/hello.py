def app(environ, start_response):
    data = environ['QUERY_STRING'].split('&')
    for i in range(len(data)):
     	data[i] += "\n"
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return iter(data)