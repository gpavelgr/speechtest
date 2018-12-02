from behave import given, when, then


@given("there are missed messages")
def given_missed_messages(context):

    context.missed_messages = ["First missed message",
                               "Second missed message",
                               "Third missed message"]


@when("user has come home")
def when_user_comes_home(context):
    context.user_is_home = True


@when("it is evening")
def when_it_is_evening(context):
    context.it_is_evening = True

@when("it is not evening")
def when_it_is_not_evening(context):
    context.it_is_evening = False


@when("assistant is working")
def assistant_logic(context):
    # here is assistans' logic
    pass


@then("assistant says {message}")
def assistant_says(context, message):
    assert context.reply == message


@then("assistant does not say a thing")
def assistant_is_silent(context):
    assert context.reply == ""
