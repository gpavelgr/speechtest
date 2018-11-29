from behave import given, when, then
import speech_recognition as sr
from os import path


get_file = lambda f: path.join(path.dirname(path.realpath(__file__)), f.lower() + ".wav")


@given('The assistant is listening')
def given_assistant_listening(context):
    context.recognizer = sr.Recognizer()


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


@then('assistant says {answer}')
def then_assistant_replies(context, answer):
    if context.recognized_command == "hello":
        response = "Hello"
    else:
        response = "not recognized"

    if answer == response:
        # everything is ok!
        pass
    else:
        raise Exception('%r not in %r' % (answer, response))

