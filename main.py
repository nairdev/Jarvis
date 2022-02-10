from django.template import engines
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import smtplib
import webbrowser
import os

MASTER = 'Devi Nair'
print ("Initializing JARVIS")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

#The speak function will pronounce the string argument passed to it.
def speak (text):
    engine.say(text)
    engine.runAndWait()

#The wishMe funtion will wish me based on the current time.
def wishMe():
    current_time = int(datetime.datetime.now().hour)
    if current_time >=0 and current_time <12:
        speak ("Good Morning" + MASTER)
    elif current_time >= 12 and current_time <= 16:
        speak ("Good Afternoon" + MASTER)
    else:
        speak ("Good Evening" + MASTER)
    speak ("I am JARVIS. How may I help you?")

#The takeCommand function will take commands from the Microphone.
def takeCommand():
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            speak("Listening...")
            audio = r.listen(source)
    
        speak ("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        speak(f"User said : {query}\n")
    except Exception as e:
        speak (f"Say that again, please")
        takeCommand()
    return query

#Logic for performing tasks using query
def processQuery(query):
    if 'wikipedia' in query.lower():
        speak("Searching wikipedia")
        query = query.replace("wikipedia","")
        print (query)
        results = wikipedia.summary(query, sentences=2)
        speak (results)

#The Main program starts here.
def main():
    speak("Initializing JARVIS...")
    wishMe()
    query = takeCommand()
    processQuery(query)

main()