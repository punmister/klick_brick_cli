from behave import *
from klick_brick_cli import say_hello
from types import SimpleNamespace

@given('command hello on cli')
def step_impl(context):
    context.test_param = SimpleNamespace(name=None, command='hello')
    context.test_only_hello = say_hello.Hello()

@when('cli is run')
def step_impl(context):
    context.output = context.test_only_hello.say_hello(context.test_param)


@then('it should return \'Hello\'')
def step_impl(context):
    assert context.output == 'Hello'

