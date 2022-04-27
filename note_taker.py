import speech_recognition as sr
import pyttsx3
r = sr.Recognizer()

while True:
    with sr.Microphone() as source:
        engine = pyttsx3.init()
        print("Hey! I'm going to help you take notes in class")
        engine.say("Hey! I'm going to help you take notes in class")
        engine.runAndWait()
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            engine.say("Here are your notes")
            engine.runAndWait()
            print("Here are your notes:\n"+format(text))
        except:
            print("Sorry your voice was not clear")
            engine.say("Sorry, your voice was not clear")
            engine.runAndWait()