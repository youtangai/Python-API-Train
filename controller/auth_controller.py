from abc import ABCMeta, abstractmethod
from injector import Injector, inject
from flask import jsonify, Flask, url_for, request, Response, make_response
import secrets
from model import encrypter
import logging
from http import HTTPStatus

# userid と passwordは固定
USERID = 'cloud-fun'
PASSWORD = 'cloud-fun'

enc = encrypter.EncrypterForSha256()

class AuthControllerInterface(metaclass=ABCMeta):
    @abstractmethod
    def sign_in(self):
        """
        @param: None \n
        @return: Json, HTTPStatus
        """
        pass

    def sign_up(self):
        """
        @param: None \n
        @return: Json, HTTPStatus
        """
        pass


class AuthController():
    @inject
    def __init__(self, i: AuthControllerInterface):
        if not isinstance(i, AuthControllerInterface):
            raise Exception("i is not Interface of Ping")
        self.auth_i = i

    def sign_in(self):
        return self.auth_i.sign_in()
    
    def sign_up(self):
        return self.auth_i.sign_up()


class UidAuth(AuthControllerInterface):
    def sign_in(self):
       # Convert Json Object
        json = request.get_json()
        req_userid = json['user_id']
        req_password = json['password']
        logging.info('[INFO]: user_id' + req_userid)
        logging.info('[INFO]: user_password' + req_password)
        # 
        #hashed_password = self.encrypterManager.hashed_password(req_password)
        hashed_password = enc.hashed_password(req_password)
        logging.debug(hashed_password)
        #get_uid_pw = db_operation.select_userid_and_password(userid=input_userid, password=encryption_password)
        # 登録されていないユーザの処理
        # if get_uid_pw == -1:
        #     return jsonify({'message': 'Not found user ID'}), HTTPStatus.OK

        # userid = get_uid_pw.userid
        # password = get_uid_pw.password

        # 受け取った物とDBにあるものを比較
        if req_userid != "userid" or req_password != "password":
            return jsonify({'message': 'faild login'}), HTTPStatus.FORBIDDEN
        # トークンを発行
        token = 'hoge'+secrets.token_hex()
        return jsonify({'access_token': token}), HTTPStatus.OK 

    def sign_up(self):
        return jsonify({'message':'wait!!'}), HTTPStatus.OK

