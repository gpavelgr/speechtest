#!/usr/bin/env python3
# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr

# import os
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials.json"

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

print("Recognizing")

# recognize speech using Sphinx
try:
    print("Sphinx thinks you said " + r.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))

'''
# recognize speech using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    print("Google Speech Recognition thinks you said " + r.recognize_google(audio, key="AIzaSyCKcGDWDg19CumatMva2gbAX4i0jGkREDk"))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

'''

# recognize speech using Google Cloud Speech
GOOGLE_CLOUD_SPEECH_CREDENTIALS = r"""
{
  "type": "service_account",
  "project_id": "nosoc-1193",
  "private_key_id": "fe149964b53a23ac702a6bf2770d7661ae5fc1d4",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDPhwPVFptZr3v0\n27V4+WYbbw78TULOiO4YsXqPbg3ctlEJc7sVEU2o0GIozaLNnriFe4sOf0GfsJK9\nWJRGpkAUJQWDMQ0MdSBylkM+mgyjrMEfXegw/oK+liOOW98tWQxDQRkW5oPLdLWa\nILXGxlt2nY10krpcuQBzZcaJJdDbFnQx+u8mj3piMJeefqHTJxz0+zZnVhxplkpv\n+aYQ+addJsOxWJujyvu75rzY9ZxG0L8QehdilnmMjI+9HRSdwKAsZ8tJvKe+qv1M\ndUyjUPGncyFBGunsV0Cckr/Hm+AhAdk7BLp0ozgroSCW8A9H44pwerGlTSG4bkgy\nD2lJ8y4bAgMBAAECggEAAJ6/B1+4NMWWaGv8uh4Zcpb21P/Bzo1H6hj1VmSPV7Mf\nd/9kjjdfJJVT71VLR7GIuoSG3TKHYJBPh/AtttG9OSFmTdNJ/+XASgMq8qXua/uq\nuz40kRtWby8TnbZWz6rvZG/j3B0XpT+8CVBIN1vDaINmlKqmS27pl6+69ku8ffzM\nknbXSR0AcB7GFIVJovFSC9vM1ZNWaabjO8VrIkY6EBxRqt/Rww+NJFYVZwQoZhM1\nUv0Ub6sADy/ILkYLMDRAFYk34tBTUL2d4zHJT28oGemWMFn0L87CneV4X6tRXNAW\nh3ew1WlCWgEWtJvWBZ3HA5ns+J1eD0YIa1FR3lY31QKBgQDw+X6l6o5xM5y1iHab\ngYKe0bP7w8+YI9FkPgfZ9t5txIcec770dJD5c+vn9bRRvMGAv3wuLR3PrOkA6NjV\nWyy0k1Fx9PPzdkWBiB9kIgPkcLl7+mfxry2M/my39vSHPIVfr3xcGY0JKrRJnyiP\n1xCmm/Jgb97IjaqO3fwZwgK0tQKBgQDcd6BvOfpxdwPgAhdrt5HG18vsCyoff3be\ntjgxSr5B2F+Zx5lFd6NwoqL/KyE5Y/HKR6JfK+ZheOS7AAjb5PEWnurkoaWzKC2r\n01W1iICGTZptj/oR1AH190smI6wS9EUvxbq+fTYlmBQl3+pgeK7rah9PCMboV9n+\n3NrdikppjwKBgQDbuNLHHFlnVMVGLTjg0DU29UUkgkXOlpI90eW808G62uDNXoK2\nSXdLTWzEI6CYiwDxkSf8vryY+TO31Zio6iqYOF+iBdVOn//+fQ0Kc42TBUnLhuay\nU6W4EuE02OPcT83ZEpzVKaMUwbCEFLCaf2I6WKWnUzoTKkFjZXuSTPnEpQKBgDfp\nyvGKhb6zDXOJdEEoXDtOzXP+3N8CJ7aSBixSJXBznMNWgMPCdNwDE02dtZ5lf5Pq\nmP6EFriPvYrDlnuWU6KGCVKUwH5waSzTuz//74CgO9Mfma9d0mV8Iz33/BMOimF0\nR0k6XjoomKuGX126HbqsvmX/9tpENZBSmNto0Dh3AoGBALCCRnlG+DrRGVW/7wgR\n0OrGUsSzqPEXDTbvu7Em1uNShrNYgZ0WR3EScGh4OolQxACxRGUTcpWMEWfR5OVF\nB/gFxSBW61PcRwMvGe1pxc3SRGg3jJa3NCSpbsHzvGG4WdPR6rABTwlXhfMLusiE\niLRyYJsIcDcZmtTsSAbpKApH\n-----END PRIVATE KEY-----\n",
  "client_email": "nosoc-1193@appspot.gserviceaccount.com",
  "client_id": "",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/nosoc-1193%40appspot.gserviceaccount.com"
}
"""

try:
    print("Google Cloud Speech thinks you said " + str(r.recognize_google_cloud(
        audio,
        credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS, language="ru-RU", show_all=True
        )
    ))
except sr.UnknownValueError:
    print("Google Cloud Speech could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Cloud Speech service; {0}".format(e))


exit(0)

# recognize speech using Wit.ai
WIT_AI_KEY = "INSERT WIT.AI API KEY HERE"  # Wit.ai keys are 32-character uppercase alphanumeric strings
try:
    print("Wit.ai thinks you said " + r.recognize_wit(audio, key=WIT_AI_KEY))
except sr.UnknownValueError:
    print("Wit.ai could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Wit.ai service; {0}".format(e))

# recognize speech using Microsoft Bing Voice Recognition
BING_KEY = "INSERT BING API KEY HERE"  # Microsoft Bing Voice Recognition API keys 32-character lowercase hexadecimal strings
try:
    print("Microsoft Bing Voice Recognition thinks you said " + r.recognize_bing(audio, key=BING_KEY))
except sr.UnknownValueError:
    print("Microsoft Bing Voice Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Microsoft Bing Voice Recognition service; {0}".format(e))

# recognize speech using Houndify
HOUNDIFY_CLIENT_ID = "INSERT HOUNDIFY CLIENT ID HERE"  # Houndify client IDs are Base64-encoded strings
HOUNDIFY_CLIENT_KEY = "INSERT HOUNDIFY CLIENT KEY HERE"  # Houndify client keys are Base64-encoded strings
try:
    print("Houndify thinks you said " + r.recognize_houndify(audio, client_id=HOUNDIFY_CLIENT_ID, client_key=HOUNDIFY_CLIENT_KEY))
except sr.UnknownValueError:
    print("Houndify could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Houndify service; {0}".format(e))

# recognize speech using IBM Speech to Text
IBM_USERNAME = "INSERT IBM SPEECH TO TEXT USERNAME HERE"  # IBM Speech to Text usernames are strings of the form XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
IBM_PASSWORD = "INSERT IBM SPEECH TO TEXT PASSWORD HERE"  # IBM Speech to Text passwords are mixed-case alphanumeric strings
try:
    print("IBM Speech to Text thinks you said " + r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD))
except sr.UnknownValueError:
    print("IBM Speech to Text could not understand audio")
except sr.RequestError as e:
    print("Could not request results from IBM Speech to Text service; {0}".format(e))
