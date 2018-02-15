from bottle import *
from socket import *

@get("<filepath:re:.*\.(jpg|png|gif|ico|svg)>")
def img(filepath):
    return static_file(filepath, root="")

@route('/')
def index():
    ip = gethostbyname_ex(gethostname())[2][0]
    
    return template('index.tpl', ip=ip)
run(host='0.0.0.0', port=80)
