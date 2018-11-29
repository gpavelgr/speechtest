from behave import given, when, then


@given("tasklist exists")
def given_tasklist_exists(context):
    context.tasklist = []


@when('user says "{command}"')
def user_says_add_task(context, command):
    context.user_input = command.lower()


@when("assistant processes input")
def adds_task_to_tasklist(context):
    if "add task" in context.user_input:
        context.tasklist.append(context.user_input)
        context.reply = "Task Added"
    else:
        context.reply = "Please Repeat"


@then("task is added")
def task_is_added(context):
    if not context.tasklist:
        raise Exception("No tasks!")


@then('assistant replies "Task Added"')
def assistant_replies(context):
    assert context.reply == "Task Added"

@then('assistant asks to repeat')
def assistant_asks_to_repeat(context):
    assert context.reply == "Please Repeat"
