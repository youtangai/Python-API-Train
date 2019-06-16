from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound

sqlite_db = create_engine('sqlite:///db/uid_and_pass.db')


# テーブルの作成
Base: DeclarativeMeta = declarative_base()


# 次にベースモデルを継承してモデルクラスを定義します
class UseridAndPasword(Base):
    """
    UserIDとPasswordを管理
    必ず Base を継承
    """
    __tablename__: str = 'uid_and_pass'

    userid_limit: int = 40
    password_limit: int = 500

    #id: Column = Column(Integer, primary_key=True, autoincrement=True)
    userid: Column = Column(String(userid_limit), primary_key=True)
    password: Column = Column(String(password_limit))

    def __repr__(self):
        return "<UseridAndPasword(userid={userid}, password={password})>".format(userid=self.userid, password=self.password)


def init_db():
    # テーブルの作成
    # テーブルがない場合 CREATE TABLE 文が実行される
    Base.metadata.create_all(sqlite_db)


def add_userid_and_password(userid, password):
    # SQLAlchemy はセッションを介してクエリを実行する
    Session = sessionmaker(bind=sqlite_db)
    session = Session()
    try:
        session.add(UseridAndPasword(userid=userid, password=password))
        # コミット（データ追加を実行）
        session.commit()
    except:
        print('Already user ID "{}" exist.'.format(userid))

# 検索処理 SELECT filter 処理

# Userid と Passwordの認証をしている ここでログイン処理を賄える？
def select_userid_and_password(userid, password):
    Session = sessionmaker(bind=sqlite_db)
    session = Session()
    try:
        # sqlalchemy.orm.exc.NoResultFound: No row was found for one()
        result = session.query(UseridAndPasword).filter(
            UseridAndPasword.userid == userid, UseridAndPasword.password == password).one()
        session.commit()
        print(result.userid, result.password)
        return result
    except NoResultFound:
        print('Not found User ID "{}".'.format(userid))
        return -1


def check_all_db():
    Session = sessionmaker(bind=sqlite_db)
    session = Session()

    uid_pass_list = session.query(UseridAndPasword).all()
    print('{:<10} {:<10}'.format('userid', 'password'))
    for uid_pass in uid_pass_list:
        print(uid_pass.userid, uid_pass.password)
    # id管理が必要なら、SELECTとfor文使ってidの列数を数える
