from klick_brick_cli import __version__
import unittest
from klick_brick_cli import say_hello

def test_version():
    assert __version__ == '0.1.0'

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.mode = 'unittest'
        self.test_param = ['hello', {'name': 'Test App'}]
        self.test_hello = say_hello.Hello(mode=self.mode, test_param=self.test_param)
        self.test_param = ['hello', 'None']
        self.test_only_hello = say_hello.Hello(mode=self.mode, test_param=self.test_param)

    def test_Hello(self):
        self.assertEqual(self.test_hello.say_hello(), 'Hello Test App')

    def test_only_hello(self):
        self.assertEqual(self.test_only_hello.say_hello(), 'Hello')


if __name__ == '__main__':
    unittest.main()