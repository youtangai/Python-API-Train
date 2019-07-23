import mysql.connector
from abc import ABCMeta, abstractmethod

class UserRepositoryInterface(metaclass=ABCMeta): 
    @abstractmethod
    def insert(self, user_id, passwd):
        pass

    @abstractmethod
    def get_passwd(self, user_id):
        pass

class UserRepository(UserRepositoryInterface):
    def __init__(self):
        try:
            self.ctx = mysql.connector.connect(
                host='172.17.0.2',
                port='3306',
                user='root',
                password='pass',
                database='cloudfun'
            )
        except mysql.connector.Error as err:
            raise err
        
    def __del__(self):
        self.ctx.close()

    def insert(self, user_id, passwd):
        cursor = self.ctx.cursor()
        try:
            cursor.execute("insert into account values (%s, %s);", (user_id, passwd))
        except mysql.connector.Error as err:
            print("failed to insert data to account: {}".format(err))
    
    def get_passwd(self, user_id):
        cursor = self.ctx.cursor()
        try:
            cursor.execute("select * from account where account.user_id = %s;", (user_id,))
        except mysql.connector.Error as err:
            print("failed to select data from account: {}".format(err))
        rows = cursor.fetchall()
        return rows[0][1]