from abc import ABCMeta, abstractmethod
from flask import jsonify

class PingControllerInterface(metaclass=ABCMeta):
    @abstractmethod
    def pong(self):
        pass

class PingController(PingControllerInterface):
    def pong(self):
        result = jsonify({'message':'pong'})
        return result