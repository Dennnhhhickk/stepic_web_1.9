def pars(a):
	b = ''
	for i in a:
		if (i == '&'):
			b += '\n'
		else:
			b += str(i)
	b += '\n'
	return b

def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return [pars(env['QUERY_STRING'])]