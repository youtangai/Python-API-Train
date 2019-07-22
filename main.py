from flask import jsonify, Flask
from controller.ping_controller import PingController, ImplPCI

app = Flask(__name__)

@app.route('/ping')
def ping():
    pci = ImplPCI()
    pc = PingController(pci)
    return pc.pong()

if __name__ == "__main__":
    app.run()