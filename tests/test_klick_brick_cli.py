from klick_brick_cli import __version__, say_hello
import unittest
from types import SimpleNamespace

def test_version():
    assert __version__ == '0.1.0'

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.test_hello = say_hello.Hello()

    def test_Hello(self):
        self.assertEqual(self.test_hello.say_hello(SimpleNamespace(name='Test App', command='hello')), 'Hello Test App')

    def test_only_hello(self):
        self.assertEqual(self.test_hello.say_hello(SimpleNamespace(name=None, command='hello')), 'Hello')


if __name__ == '__main__':
    unittest.main()