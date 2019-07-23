# conding: utf-8
import hashlib
from abc import ABCMeta, abstractmethod
from injector import Injector, inject

# インターフェースを定義(なぜインターフェースを定義しているかは考えてみて)
# インターフェースは，引数と返り値だけ持つ抽象クラス
class EncrypterInterface(metaclass=ABCMeta):
    # パスワードハッシュ化用のメソッド
    @abstractmethod
    def hashed_password(self, password):
        """
        @param: str
        @return: str
        """
        pass
    # ハッシュ化された文字列と対象が等価か評価するメソッド
    @abstractmethod
    def check_hashed(self, hashed, password):
        """
        @param: str, str
        @return: bool
        """
        pass

# 実際に暗号化を行う本体
# コンストラクタで，インターフェースをインジェクション
class Encrypter():
    @inject
    def __init__(self, i: EncrypterInterface):
        if not isinstance(i, EncrypterInterface):
            raise Exception("i is not Interface of Encrypter")
        self.enc_i = i
    
    def hashed_password(self, password):
        """
        @param: str
        @return: str
        """
        bin_password = password.encode()
        hashed_pass = hashlib.sha256(bin_password).hexdigest() 
        return self.enc_i.hashed_password(password)
    
    def check_hashed(self, hashed, password):
        """
        @param: str, str
        @return: bool
        """
        return self.enc_i.check_hashed(hashed, password)

class EncrypterForSha256(EncrypterInterface):
    def hashed_password(self, password):
        """
        @param: str
        @return str
        """
        bin_password = password.encode()
        hashed_pass = hashlib.sha256(bin_password).hexdigest()
        return hashed_pass
    def check_hashed(self, hashed, password):
        """
        @param: str, str
        @return: bool
        """
        bin_password = password.encode()
        hashed_pass = hashlib.sha256(bin_password).hexdigest() 
        if hashed == hashed_pass: return True
        else: return False