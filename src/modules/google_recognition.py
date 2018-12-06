
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

import speech_recognition as sr


def recognize_file(audio_file):
    r = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = r.record(source)
    return r.recognize_google_cloud(
        audio,
        credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS, language="ru-RU", show_all=True
    )
