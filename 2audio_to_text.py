import pyttsx3 as p
import  speech_recognition as sr

r = sr.Recognizer()

with sr.AudioFile('harvard.wav') as source:
    audio_data = r.record(source)

text = r.recognize_google(audio_data)

print(text)