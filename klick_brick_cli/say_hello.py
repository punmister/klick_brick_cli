from argparse import ArgumentParser
from mdutils.mdutils import MdUtils
import webbrowser
import subprocess

class Hello():

    def __init__(self):
        self.parser = ArgumentParser()
        self.subparsers = self.parser.add_subparsers(title='command', dest='command')
        self.hi_parser = self.subparsers.add_parser("hello", help="say hello")
        self.hi_parser.add_argument("--name", help="your name to add in greetings")
        self.onboard_parser = self.subparsers.add_parser("onboard", help="say hello")
        self.onboard_parser.add_argument("--checklist", help="")
        self.onboard_parser.add_argument("--it-request", help="")
        self.onboard_parser.add_argument("--dev-tools", help="")

    def run_task(self, args=None):
        if args is None:
            args = self.parser.parse_args()
        if args.command == 'hello':
            self.say_hello(args)
        elif args.command == 'onboard':
            self.onboard(args)
            self.dev_tools(args)
            self.it_request(args)

    def say_hello(self, args):
        if hasattr(args, 'name'):
            if args.name is None:
                return "Hello"
            else:
                return f"Hello {args.name}"

    def onboard(self, args):
        if hasattr(args, 'checklist'):
            mdFile = MdUtils(file_name='Example_Markdown', title='Markdown File Example')
            items = ["engineering handbook", "complete corporate training"]
            mdFile.new_checkbox_list(items)
            mdFile.create_md_file()

    def it_request(self, args):
        if hasattr(args, 'it_request'):
            webbrowser.open(f"mailto:support@klick_brick_cli.com?subject=\"it-request\"& body = 'this is a sample'")

    def dev_tools(self, args):
        if hasattr(args, 'dev_tools'):
            subprocess.run('pip install poetry')
            subprocess.run('pip install pyenv')
            subprocess.run('sudo apt-get install git')


if __name__ == '__main__':
    sample = Hello()
    sample.run_task()
