from flask import jsonify, Flask, request
import secrets
import db_operation
from http import HTTPStatus
import encryption

app = Flask(__name__)


@app.route('/')
def index():
    pass


@app.route('/ping', methods=['GET'])
def pong():
    return jsonify({'message': "pong"}), HTTPStatus.OK


@app.route('/signin', methods=['POST'])
def signin():
    json = request.get_json()
    input_userid = json['userid']
    input_password = json['password']
    encryption_password = encryption.encryption_password(userid=input_userid, password=input_password)
    get_uid_pw = db_operation.select_userid_and_password(
        userid=input_userid, password=encryption_password)
    # 登録されていないユーザの処理
    if get_uid_pw == -1:
        return jsonify({'message': 'Not found user ID'}), HTTPStatus.OK

    userid = get_uid_pw.userid
    password = get_uid_pw.password

    if input_userid != userid and input_password != password:
        return jsonify({'message': 'faild login'}), HTTPStatus.OK

    token = 'hoge'+secrets.token_hex()
    return jsonify({'access_token': token}), HTTPStatus.OK


@app.route('/signup', methods=['POST'])
def signup():
    json = request.get_json()
    input_userid = json['userid']
    input_password = json['password']

    encrypted_password = encryption.encryption_password(input_userid, input_password) 
    db_operation.add_userid_and_password(
        userid=input_userid, password=encrypted_password)

    token = 'hoge'+secrets.token_hex()
    return jsonify({'access_token': token}), HTTPStatus.CREATED


if __name__ == "__main__":
    db_operation.init_db()
    db_operation.add_userid_and_password(
        userid='cloud-fun', password='cloud-fun')
    app.run(debug=True)

# status code を変数化
# requarement.txt 作って
