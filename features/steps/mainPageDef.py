from behave import given, when, then  # pip install behave


@given("I open programm")
def step_impl(context):
    context.a = 4


@when("I press add button")
def step_impl(context):
    context.a += 1


@then("Add window opens")
def step_impl(context):
    assert context.a == 5
