from modules import google_recognition


class VoiceAssistantBase:

    def _recognize_commmand(command):
        google_recognition.recognize_file(command + ".wav")




