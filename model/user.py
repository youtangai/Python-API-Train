from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from abc import ABCMeta, abstractmethod
from injector import Injector, inject

# MySQL 使用時のサンプルコード
 
# 接続ホスト名: localhost
# データベース名: sample_db
# ユーザー名: testuser
# パスワード: testpass
# 文字コード: UTF-8

# テーブルの作成
Base: DeclarativeMeta = declarative_base()

class UserInterface(metaclass=ABCMeta):
    @abstractmethod
    def init_db(self):
        pass
    @abstractmethod
    def insert(self, userid, password):
        pass
    @abstractmethod
    def select(self, userid, password):
        pass

# 次にベースモデルを継承してモデルクラスを定義します
class User(Base):
    CONNECTION_STRING = 'mysql://akane:kawaiiyatta@localhost/uid_pass' 
    @inject
    def __init__(self, i: UserInterface):
        if not isinstance(i, UserInterface):
            raise Exception("i is not Interface of Encrypter")
        self.DB_ENGINE = create_engine(self.CONNECTION_STRING, echo=True)
    # テーブル名
    __tablename__: str = 'user'
    # 文字数制限
    id_num_limit: int = 40
    password_num_limit: int = 500
    # カラム設定
    id: Column = Column(String(id_num_limit), primary_key=True)
    password: Column = Column(String(password_num_limit))

    def __repr__(self):
        return "<User(id={self.id}, password={password})>".format(id=self.id, password=self.password)

    def init_db(self):
        Base.metadata.create_all(self.DB_ENGINE)

    def insert(self, userid, password):
        # SQLAlchemy はセッションを介してクエリを実行する
        Session = sessionmaker(bind=self.DB_ENGINE)
        session = Session()
        try:
            session.add(User(id=self.id, password=password))
            # コミット（データ追加を実行）
            session.commit()
        except:
            print('Already user ID "{}" exist.'.format(userid))

    # 検索
    def select(self, userid, password):
        Session = sessionmaker(bind=self.DB_ENGINE)
        session = Session()
        try:
            result = session.query(User).filter(User.id == id, User.password == password).one()
            session.commit()
            return result
        except NoResultFound:
            print('Not found User ID "{}".'.format(userid))
            return -1
