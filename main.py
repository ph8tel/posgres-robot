from bottle import *
import db
@get("/")
def index():
    print("fired")
    return template("index")

@get("/cmd/<direction>")
def handle_command(direction):
    db.send_cmd(direction)
    return True
@get("/all-stop")
def stopn_now(d):
    db.stopper()
    return True

run(host='0.0.0.0', port=44321, debug = True)

