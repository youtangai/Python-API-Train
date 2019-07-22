from flask import jsonify, Flask
from controller.ping_controller import PingController
from controller.auth_controller import AuthController, ImplACI
from model.encrypter import ImplEI

app = Flask(__name__)

@app.route('/ping', methods=["GET"])
def ping():
    ctrl = PingController()
    return ctrl.pong()

@app.route('/signin', methods=["POST"])
def signin():
    aci = ImplACI()
    ei = ImplEI()
    ac = AuthController(aci, ei)
    return ac.signin()

if __name__ == "__main__":
    app.run(host='0.0.0.0')