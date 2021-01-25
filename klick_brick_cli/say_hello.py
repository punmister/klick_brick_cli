from argparse import ArgumentParser

class Hello():

    def __init__(self, mode='cli', test_param=None):
        self.mode = mode
        self.test_param = test_param

    def say_hello(self):
        if self.mode=='cli':
            parser = ArgumentParser()
            parser.add_argument("--name", help="your name to add in greetings")
            parser.add_argument("hello", help="say hello")
            args = parser.parse_args()
            if args.hello:
                if args.name is None:
                    print("Hello")
                    return "Hello"
                else:
                    print(f"Hello {args.name}")
                    return f"Hello {args.name}"
        elif self.mode == 'unittest':
            if self.test_param[0]:
                if self.test_param[1] == 'None':
                    return "Hello"
                else:
                    return f"Hello {self.test_param[1]['name']}"


if __name__ == '__main__':
    sample = Hello()
    sample.say_hello()