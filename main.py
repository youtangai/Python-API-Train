from flask import jsonify, Flask
from controller.ping_controller import PingController
from controller.auth_controller import AuthController, AuthControllerDIModule
from model.encrypter import Encrypter
from injector import Injector

app = Flask(__name__)

@app.route('/ping', methods=["GET"])
def ping():
    ctrl = PingController()
    return ctrl.pong()

@app.route('/signin', methods=["POST"])
def signin():
    injector = Injector([AuthControllerDIModule()])
    ac = injector.get(AuthController)
    return ac.sign_in()

if __name__ == "__main__":
    app.run(host='0.0.0.0')