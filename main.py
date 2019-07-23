from flask import jsonify, Flask
from controller.ping_controller import PingPong
from controller.auth_controller import UidAuth

ping_c = PingPong()
sign_in_c = UidAuth()

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def pin_pon():
    return ping_c.pong()

@app.route('/signin', methods=['POST'])
def login():
    return sign_in_c.sign_in()
    
if __name__ == "__main__":
    app.run(debug=True)