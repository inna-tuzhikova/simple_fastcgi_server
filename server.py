#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from flup.server.fcgi import WSGIServer

def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])

    yield '<h1>FastCGI Environment</h1>'
    yield '<table>'
    for k, v in sorted(environ.items()):
        yield '<tr><th>%s</th><td>%s</td></tr>' % (k, v)
    yield '</table>'

WSGIServer(app, bindAddress=('python_fcgi', 9000)).run()
