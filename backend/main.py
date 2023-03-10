from waitress import serve
from app import *


# in commandline : waitress-serve --call 'app:smart_backend'

def smart_backend(environ, start_response):
    return app(environ, start_response)


serve(smart_backend, listen='127.0.0.1:5000')
