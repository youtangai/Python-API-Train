from abc import ABCMeta, abstractmethod
from injector import inject, Module
from flask import jsonify, request
import secrets
from model.encrypter import EncrypterInterface, Encrypter
from model.user import UserRepositoryInterface, UserRepository
import logging
from http import HTTPStatus

class AuthControllerInterface(metaclass=ABCMeta):
    @abstractmethod
    def sign_in(self):
        pass

    @abstractmethod
    def sign_up(self):
        pass

class AuthController(AuthControllerInterface):
    @inject
    def __init__(self, enc_i: EncrypterInterface, repo_i: UserRepositoryInterface):
        if not isinstance(enc_i, EncrypterInterface):
            raise Exception("enc_i is not Interface of Encrypter")
        if not isinstance(repo_i, UserRepositoryInterface):
            raise Exception("repo_i is not Interface of UserRepository")
        self.encManager = enc_i
        self.repo = repo_i
    
    def sign_in(self):
        # Convert Json Object
        json = request.get_json()
        req_userid = json['user_id']
        req_password = json['password']
        logging.info('[INFO]: user_id' + req_userid)
        logging.info('[INFO]: user_password' + req_password)

        # ハッシュ化 
        hashed_password = self.encManager.hashed_password(req_password)
        # dbからハッシュ化されたパスワードを取得
        registered_hashed_password = self.repo.get_passwd(user_id=req_userid)

        # 受け取った物とDBにあるものを比較
        if hashed_password != registered_hashed_password:
            return jsonify({'message': 'faild login'}), HTTPStatus.BAD_REQUEST
        # トークンを発行
        token = 'hoge'+secrets.token_hex()
        return jsonify({'access_token': token}), HTTPStatus.OK

    def sign_up(self):
        json = request.get_json()
        user_id = json['user_id']
        password = json['password']

        hashed = self.encManager.hashed_password(password)
        print(hashed)
        self.repo.insert(user_id=user_id, passwd=hashed)

        return jsonify({'message':'created user'}), HTTPStatus.CREATED

# DI用のモジュールを定義
class AuthControllerDIModule(Module):
    def configure(self, binder):
        binder.bind(EncrypterInterface, to=Encrypter)
        binder.bind(UserRepositoryInterface, to=UserRepository)