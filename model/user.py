import mysql.connector
from abc import ABCMeta, abstractmethod
from config.env import Env

class UserRepositoryInterface(metaclass=ABCMeta): 
    @abstractmethod
    def insert(self, user_id, passwd):
        pass

    @abstractmethod
    def get_passwd(self, user_id):
        pass

class UserRepository(UserRepositoryInterface):
    def __init__(self):
        env = Env()
        try:
            # 環境変数から値を取得
            self.ctx = mysql.connector.connect(
                host=env.get_host(),
                port=env.get_port(),
                user=env.get_user(),
                password=env.get_pass(),
                database=env.get_name(),
                ssl_disabled=True # uwsgiで起動した場合，デフォルトでfalseになり接続に失敗するためTrueを指定
            )
        except mysql.connector.Error as err:
            raise err
        # 不要なインスタンスなので削除
        del env
        
    def __del__(self):
        # デストラクタでコネクションを削除するようにする
        # (これ必要なのか正直わからない by youtangai)
        self.ctx.close()

    def insert(self, user_id, passwd):
        cursor = self.ctx.cursor()
        try:
            cursor.execute("insert into account values (%s, %s);", (user_id, passwd))
        except mysql.connector.Error as err:
            print("failed to insert data to account: {}".format(err))
            raise err
        # 一連の処理が終了したので，カーソルをとして結果をコミット
        cursor.close()
        self.ctx.commit()
    
    def get_passwd(self, user_id):
        cursor = self.ctx.cursor()
        try:
            cursor.execute("select * from account where account.user_id = %s;", (user_id,))
        except mysql.connector.Error as err:
            print("failed to select data from account: {}".format(err))
            raise err
        # fetchoneで最初の1つめのレコードを取得
        rows = cursor.fetchone()
        cursor.close()
        # (user_id, passwd) というタプルが手に入るため，passwdを取り出す
        return rows[1]