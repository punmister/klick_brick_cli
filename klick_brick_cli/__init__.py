__version__ = '0.1.0'

from argparse import ArgumentParser
from klick_brick_cli import say_hello


def main():
    parser = ArgumentParser()
    parser.add_argument("hello", help="say hello")
    parser.add_argument("--name", help="say name")
    arg = parser.parse_args()
    if arg.name==None:
        arg.name = 'None'
    sample = say_hello.Hello(test_param=[arg.hello, {'name': arg.name}])
    return sample.say_hello()
