from flask import Flask
from controller.ping_controller import PingController
from controller.auth_controller import AuthController, AuthControllerDIModule
from injector import Injector

app = Flask(__name__)

injector = Injector([AuthControllerDIModule()])
ac = injector.get(AuthController)

@app.route('/ping', methods=["GET"])
def ping():
    ctrl = PingController()
    return ctrl.pong()

@app.route('/signin', methods=["POST"])
def signin():
    return ac.sign_in()

@app.route('/signup', methods=["POST"])
def signup():
    return ac.sign_up()

if __name__ == "__main__":
    app.run(host='0.0.0.0')