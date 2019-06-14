from flask import jsonify, Flask, url_for, request, Response, make_response
import secrets
import db_operation

db_operation.init_db()
db_operation.add_userid_and_password(userid='cloud-fun', password='cloud-fun')
app = Flask(__name__)


@app.route('/')
def index():
    pass


@app.route('/ping', methods=['GET'])
def pong():
    return jsonify({'message': "pong"})


@app.route('/signin', methods=['POST'])
def signin():
    json = request.get_json()
    input_userid = json['userid']
    input_password = json['password']
    get_uid_pw = db_operation.select_userid_and_password(
        userid=input_userid, password=input_password)
    # 登録されていないユーザの処理
    if get_uid_pw == -1:
        return jsonify({'message': 'Not found user ID'})

    userid = get_uid_pw.userid
    password = get_uid_pw.password

    if input_userid != userid and input_password != password:
        return jsonify({'message': 'faild login'})

    token = 'hoge'+secrets.token_hex()
    return jsonify({'access_token': token})


@app.route('/signup', methods=['POST'])
def signup():
    json = request.get_json()
    input_userid = json['userid']
    input_password = json['password']
    db_operation.add_userid_and_password(
        userid=input_userid, password=input_password)

    token = 'hoge'+secrets.token_hex()
    return jsonify({'access_token': token}), 404 


if __name__ == "__main__":
    app.run(debug=True)
