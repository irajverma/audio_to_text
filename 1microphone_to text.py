import pyttsx3 as p
import  speech_recognition as sr
import pyaudio



engine = p.init()# initalize
rate = engine.getProperty('rate')
engine.setProperty('rate', 180)
voice = engine.getProperty('voices')
# engine.setProperty('voice',voice[0].id)# for male voice
engine.setProperty('voice',voice[1].id)
# print(voice)
# print(rate)
def speak(text): 
    engine.say(text)
    engine.runAndWait()
    print(text)
r =  sr.Recognizer()#retrieve data from the microphone
speak("Hello boss. My name is Friday")


with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source , 1.2)
    print("listening")
    audio = r.listen(source)
    text = r.recognize_google(audio)#use the google api to convert the speech to text
    print(text) 

if "what" and "about" and "you" in text:
    speak("I am having a great time sir")
speak("how can i help you")

