from flask import jsonify, Flask, url_for, request, Response, make_response
import secrets

app = Flask(__name__)

# userid と passwordは固定
USERID = 'cloud-fun'
PASSWORD = 'cloud-fun'

@app.route('/')
def index():
    pass

@app.route('/user/<username>')
def show_user_status(userid):
    pass

@app.route('/ping', methods=['GET'])
def pong():
    return jsonify({'message':"pong"})

@app.route('/signin', methods=['POST'])
def signin():
    json = request.get_json()
    userid = json['userid']
    password = json['password']
    result = {
        "data": {
            "userid" : userid,
            "password" : password 
        }
    }
    print(result)
    if userid != USERID and password != PASSWORD:
        return jsonify({'message':'faild login'})
    
    token = 'hoge'+secrets.token_hex()
    return jsonify({'access_token' : token})

if __name__ == "__main__":
    app.run(debug=True)