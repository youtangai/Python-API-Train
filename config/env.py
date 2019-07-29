from os import environ

class Env:
    def __init__(self):
        try:
            self.__db_host = environ['DB_HOST']
        except KeyError:
            self.__db_host = "127.0.0.1"

        try:    
            self.__db_port = environ['DB_PORT']
        except KeyError:
            self.__db_port = "3306"

        try:
            self.__db_name = environ['DB_NAME']
        except KeyError:
            self.__db_name = "cloudfun"

        try:
            self.__db_user = environ['DB_USER']
        except KeyError:
            self.__db_user = "root"

        try:
            self.__db_pass = environ['DB_PASS']
        except KeyError:
            self.__db_pass = "pass"
    
    def get_host(self):
        return self.__db_host

    def get_port(self):
        return self.__db_port

    def get_name(self):
        return self.__db_name

    def get_user(self):
        return self.__db_user

    def get_pass(self):
        return self.__db_pass