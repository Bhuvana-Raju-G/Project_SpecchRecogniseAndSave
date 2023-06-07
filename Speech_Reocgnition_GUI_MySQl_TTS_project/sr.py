import speech_recognition as sr
import pyttsx3
from mysql2 import * 

engine=pyttsx3.init()
engine.say("Hello users ")
engine.runAndWait()

def sp_recognize():
   
    r=sr.Recognizer()
    print("speak anything")
    engine.say("Speak Anything")
    engine.runAndWait()
    with sr.Microphone() as source:
        audio=r.record(source,duration=5)
        
        try: 
            text=r.recognize_google(audio)
            print(text)
            savetoDB(text)
            engine.say("Records of recognized speech is saved to database")
            engine.runAndWait()
        except:
            print('Sorry,unable to recognise voice')

