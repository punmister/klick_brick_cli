from behave import *
from klick_brick_cli import say_hello


@given('command hello on cli')
def step_impl(context):
    context.test_param = ['hello', 'None']
    context.test_only_hello = say_hello.Hello(mode='unittest', test_param=context.test_param)


@when('cli is run')
def step_impl(context):
    context.output = context.test_only_hello.say_hello()


@then('it should return \'Hello\'')
def step_impl(context):
    assert context.output == 'Hello'