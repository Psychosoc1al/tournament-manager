from behave import *  # pip install behave


@given(u'I open programm')
def step_impl(context):
    context.a = 4


@when(u'I press add button')
def step_impl(context):
    context.a += 1


@then(u'Add window opens')
def step_impl(context):
    assert context.a == 5
