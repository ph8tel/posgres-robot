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
port = os.environ.get("PORT", 17995)

run(host='0.0.0.0', port=port, debug = True)

