from behave import given, when, then
import speech_recognition as sr
from os import path
get_file = lambda f: path.join(path.dirname(path.realpath(__file__)), f.lower() + ".wav")

COMMANDS = ["add task", "delete task"]

######## GIVEN ########


@given('The assistant is listening')
def given_assistant_listening(context):
    context.recognizer = sr.Recognizer()


@given("tasklist exists")
def given_tasklist_exists(context):
    context.tasklist = []


######### WHEN ##########


@when('user says "{command}"')
def user_says_add_task(context, command):
    context.user_input = command.lower()


@when('user says word {command}')
def when_user_says(context, command):
    audio_file = get_file(command)
    context.audio_file = audio_file


@when('assistant recognizes command')
def when_assistant_recognizes_command(context):
    with sr.AudioFile(context.audio_file) as source:
        audio = context.recognizer.record(source)
    context.recognized_command = context.recognizer.recognize_sphinx(audio)


@when('assistant fails to recognize command')
def when_assistant_fails(context):
    context.response = ""


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


######### THEN #########


@then('assistant pronounces {answer}')
def then_assistant_replies(context, answer):
    if context.recognized_command == "hello":
        response = "Hello"
    else:
        response = "not recognized"
    assert answer == response


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

