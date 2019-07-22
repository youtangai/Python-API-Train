from abc import ABCMeta, abstractmethod
from injector import Injector, inject
from flask import jsonify, Flask, url_for, request, Response, make_response
import secrets
from model.encrypter import EncrypterInterface, Encrypter
import logging
from http import HTTPStatus

# userid と passwordは固定
USERID = 'cloud-fun'
PASSWORD = 'cloud-fun'

class AuthControllerInterface(metaclass=ABCMeta):
    @abstractmethod
    def sign_in(self):
        pass

    @abstractmethod
    def sign_up(self):
        pass

class AuthController(AuthControllerInterface):
    @inject
    def __init__(self, enc_i: EncrypterInterface):
        if not isinstance(enc_i, EncrypterInterface):
            raise Exception("enc_i is not Interface of Encrypter")
        self.encManager = enc_i
    
    def sign_in(self):
        # Convert Json Object
        json = request.get_json()
        req_userid = json['user_id']
        req_password = json['password']
        logging.info('[INFO]: user_id' + req_userid)
        logging.info('[INFO]: user_password' + req_password)
        # 
        hashed_password = self.encManager.hashed_password(req_password)
        #get_uid_pw = db_operation.select_userid_and_password(userid=input_userid, password=encryption_password)
        # 登録されていないユーザの処理
        # if get_uid_pw == -1:
        #     return jsonify({'message': 'Not found user ID'}), HTTPStatus.OK

        # userid = get_uid_pw.userid
        # password = get_uid_pw.password

        # 受け取った物とDBにあるものを比較
        if req_userid != USERID and req_password != PASSWORD:
            return jsonify({'message': 'faild login'}), HTTPStatus.BAD_REQUEST
        # トークンを発行
        token = 'hoge'+secrets.token_hex()
        return jsonify({'access_token': token}), HTTPStatus.OK

    def sign_up(self):
        print("signup")