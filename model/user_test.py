import unittest
from user import UserRepository

class TestUserRepository(unittest.TestCase):
    def test_insert(self):
        repo = UserRepository()
        repo.insert(user_id='cloud', passwd='fun')
    
    def test_get_passwd(self):
        repo = UserRepository()
        passwd = repo.get_passwd(user_id='hoge')
        self.assertEqual('hoge', passwd)

if __name__ == "__main__":
    unittest.main()