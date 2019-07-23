from flask import jsonify, Flask
from controller.ping_controller import PingPong

ping_c = PingPong()

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def pin_pon():
    return ping_c.pong()

if __name__ == "__main__":
    app.run(debug=True)