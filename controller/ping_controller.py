from abc import ABCMeta, abstractmethod
from injector import Injector, inject
from flask import jsonify

class PingControllerInterface(metaclass=ABCMeta):
    @abstractmethod
    def pong(self):
        pass

class ImplPCI(PingControllerInterface):
    def pong(self):
        print("impl PingControllerInterface")

class PingController():
    @inject
    def __init__(self, i: PingControllerInterface):
        if not isinstance(i, PingControllerInterface):
            raise Exception("i is not Interface of Ping")
    
    def pong(self):
        result = jsonify({'message':"pong"})
        return result