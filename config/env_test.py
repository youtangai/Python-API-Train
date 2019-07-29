import unittest
from env import Env



class TestEnv(unittest.TestCase):
    def test_get_host(self):
        config = Env()
        host = config.get_host()
        self.assertEqual("127.0.0.1", host)
    def test_get_port(self):
        config = Env()
        port = config.get_port()
        self.assertEqual("3306", port)
    def test_get_name(self):
        config = Env()
        name = config.get_name()
        self.assertEqual("cloudfun", name)
    def test_get_user(self):
        config = Env()
        user = config.get_user()
        self.assertEqual("root", user)
    def test_get_pass(self):
        config = Env()
        passwd = config.get_pass()
        self.assertEqual("pass", passwd)

if __name__ == '__main__':
    unittest.main()