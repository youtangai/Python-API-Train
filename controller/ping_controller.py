from abc import ABCMeta, abstractmethod
from injector import Injector, inject
from flask import jsonify

class PingControllerInterface(metaclass=ABCMeta):
    """
    @param: None\n
    @return: Json
    """
    @abstractmethod
    def pong(self):
        pass

class PingController():
    @inject
    def __init__(self, i: PingControllerInterface):
        if not isinstance(i, PingControllerInterface):
            raise Exception("i is not Interface of Ping")
        self.pci = i

    def pong(self):
        return self.pci.pong()

class PingPong(PingControllerInterface):
    def pong(self):
        result = jsonify({'message':"pong"})
        return result