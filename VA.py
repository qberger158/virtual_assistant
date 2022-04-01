# Author: Quentin Bergeron
# File: VA.py
# Date started: 23 September 2021
# Description: This code will be used to create a virtual assistant called "JARVIS".
# It is inspired by digital voice assistant's such as Alexa and Siri.

import output as output
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser

audience = sr.Recognizer()
engine = pyttsx3.init()


def speak(written_word):
    engine.say(written_word)
    engine.runAndWait()
hour = int(datetime.datetime.now().hour)


if hour >= 4 and hour < 12:
    print("Good morning boss. I am your virtual assistant JARVIS. How may I help you?")
    speak("Good morning boss. I am your virtual assistant JARVIS. How may I help you?")

elif hour >= 12 and hour < 18:
    print("Good afternoon boss. I am your virtual assistant JARVIS. How may I help you?")
    speak("Good afternoon boss. I am your virtual assistant JARVIS. How may I help you?")

elif hour >= 18 and hour <= 22:
    print("Good evening boss. I am your virtual assistant JARVIS. How may I help you?")
    speak("Good evening boss. I am your virtual assistant JARVIS. How may I help you?")

else:
    print("Hello boss. I am your virtual assistant JARVIS. How may I help you?")
    speak("Hello boss. I am your virtual assistant JARVIS. How may I help you?")

def take_command(question = False):
    try:
        with sr.Microphone() as source:
            print("State your command now...")
            speak("State your command now")
            voice = audience.listen(source)
            instruct = audience.recognize_google(voice)
            instruct = instruct.lower()
            if "jarvis" in instruct:
                instruct = instruct.replace("jarvis", "")
                print(instruct)
        if question:
            print(question)
    except:
        pass
    return instruct

def inputCommand():
    pass

def run_jarvis():
    instruct = take_command()
    print(instruct)

    # plays a video from Youtube
    if "play" in instruct:
        video = instruct.replace("play", "")
        speak("playing" + video)
        pywhatkit.playonyt(video)

    elif "time" in instruct:
        time = datetime.datetime.now().strftime("%H:%M:%S")
        print(time)
        speak("Current time is " + time)

    elif "who is" in instruct:
        person = instruct.replace("who is ", "")
        info = wikipedia.summary(person, 1)
        print(info)
        speak(info)

    elif "who are" in instruct:
        person = instruct.replace("who are ", "")
        info = wikipedia.summary(person, 1)
        print(info)
        speak(info)

    elif "joke" in instruct:
        speak(pyjokes.get_j3oke())

    elif "date" in instruct:
        date = datetime.datetime.now().strftime("%d/%m/%Y")
        print(date)
        speak("Today's date is " + date)

    elif "what are you" in instruct:
        print("I am a virtual assistant created by Quentin Bergeron on September twenty-third, two thousand twenty one")
        speak("I am a virtual assistant created by Quentin Bergeron on September twenty-third, two thousand twenty one")

    elif "what is your name" in instruct:
        print("I already told you that my name is Jarvis... were you not listening")
        speak("I already told you that my name is Jarvis... were you not listening ")

    elif "how are you" in instruct:
        print("As I am just a virtual software presence, I have no feelings. Therefore asking me how\n"
              "I am is irrelevant... On another note, how are you")
        speak("As I am just a virtual software presence, I have no feelings. Therefore asking me how"
              "I am is irrelevant... On another note... how are you")

    elif "tell me your abilities" in instruct:
        print("I can play videos from Youtube, do Google searches, do quick Wikipedia searches,\n"
              "tell jokes and tell you the date and time")
        speak("I can play videos from Youtube, do Google searches, do quick Wikipedia searches\n"
              "tell jokes and tell you the date and time")

    elif "google search" in instruct:
        speak("What would you like to search ")
        search = take_command("What to search for")
        url = "https://google.com/search?q=" + search
        webbrowser.get().open(url)
        speak("Here are the results I found for " + search)
        print("Here are the results I found for " + search)

    elif 'open google' in instruct:
        speak("Opening google")
        webbrowser.open("https://google.com/search?q=")

    elif "provide location" in instruct:
        speak("where would you like to locate")
        location = take_command("Tell me the location")
        url = "https://google.nl/maps/place/" + location + "/&amp;"
        webbrowser.get().open(url)
        speak("Finding the requested location")
        print("Here is the location of " + location)

    elif "power off" in instruct:
        speak("Powering off")
        exit()

    else:
        speak("I do not understand, please repeat the command again")

while True:
    run_jarvis()