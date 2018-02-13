from bottle import *

@get("<filepath:re:.*\.(jpg|png|gif|ico|svg)>")
def img(filepath):
    return static_file(filepath, root="")

@route('/')
def index():
    return template('index.tpl')
run(host='localhost', port=80)
