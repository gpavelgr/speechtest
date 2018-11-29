from behave import given, when, then

COMMANDS = ["add task", "delete task"]


@given("tasklist exists")
def given_tasklist_exists(context):
    context.tasklist = []


@when('user says "{command}"')
def user_says_add_task(context, command):
    context.user_input = command.lower()


@when("assistant processes input")
def adds_task_to_tasklist(context):
    command = ""
    argument = ""
    for c in COMMANDS:
        if c in context.user_input:
            argument = context.user_input.replace(c, "")
            command = c
            break
    # We now know the command and the argument
    if command == "add task":
        context.tasklist.append(argument)
        context.reply = "Task Added"
    else:
        context.reply = "Please Repeat"


@then("task is added")
def task_is_added(context):
    if not context.tasklist:
        raise Exception("No tasks!")


@then('assistant replies "Task Added"')
def assistant_replies(context):
    print("ASSISTANT REPLIES: " + context.reply)
    print("")
    assert context.reply == "Task Added"

@then('assistant asks to repeat')
def assistant_asks_to_repeat(context):
    print("ASSISTANT REPLIES: " + context.reply)
    print("")
    assert context.reply == "Please Repeat"
