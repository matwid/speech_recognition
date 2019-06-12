#  Speech Recognition in Python
#  Zhang, A. (2017). Speech Recognition (Version 3.8) [Software]. Available from https://github.com/Uberi/speech_recognition#readme.
#  Licensing information for SpeechRecognition can be found within the SpeechRecognition README

import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Talk now")
    audio = recognizer.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You just said : {}".format(text))
    except:
        print("No voice recognized")
