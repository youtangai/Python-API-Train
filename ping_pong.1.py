from flask import jsonify, Flask

app = Flask(__name__)

@app.route('/')
def index():
    pass

@app.route('/ping', methods=['GET'])
def pong():
    return jsonify({'message':"pong"})

if __name__ == "__main__":
    app.run()