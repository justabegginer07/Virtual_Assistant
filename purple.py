import pyttsx3
from decouple import config
import speech_recognition as sr
from random import choice
from utility import opening_text
import requests
from functions.online_ops import search_on_google,search_on_wikipedia,send_email,send_whatsapp_message,get_latest_news,get_random_advice,get_random_joke,get_weather_report,play_on_youtube,get_city
from functions.os_ops import open_notepad,open_cmd,open_calculator,open_camera
from pprint import pprint
from datetime import datetime
#import sys

USERNAME=config('USER')
BOTNAME=config('BOTNAME')


engine=pyttsx3.init('sapi5')
engine.setProperty('rate',200)
engine.setProperty('volume',1)
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait() # without this line you can't hear anything.

#speak(' hello. This is Purple. nice to meet you')

def greet():
    hour=datetime.now().hour
    if (hour>=4) and (hour<12):
        speak(f'Good Morning {USERNAME}')
    elif (hour>=12) and (hour<17):
        speak(f'Good Afternoon {USERNAME}')
    elif (hour>=17) and (hour<21):
        speak(f'Good Evening {USERNAME}')
    speak(f'I am {BOTNAME}. How may i assist you, mam?')

def user_input():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print('Recognizing....')
        query=r.recognize_google(audio,language='en-in')
        if 'exit' in query or 'stop' in query:
            hour=datetime.now().hour
            if hour >=21 and hour <4:
                speak('Good night Mam. Take care')
            else:
                speak('have a good day Mam')
            exit()
        else:
            speak(choice(opening_text))
    except Exception:
        speak('Sorry Mam, I could not understand. Could you say that again.')
        query='None'
    return query

if __name__=='__main__':
    greet()
    while True:
        query=user_input().lower()
        
        if 'open notepad' in query:
            open_notepad()

        elif 'open calculator' in query:
            open_calculator()
        
        elif 'open command prompt' in query:
            open_cmd()

        elif 'open camera' in query:
            open_camera()
        
        elif 'wikipedia' in query:
            speak('What do you want to search in wikipedia, Mam?')
            search_query=user_input().lower()
            res=search_on_wikipedia(search_query)
            speak(f"According to Wikipedia, {res}")
            speak("For your convenience, I am printing it on the screen mam.")
            print(res)

        elif 'youtube' in query:
            speak('What do you want to play on youtube, mam?')
            video=user_input().lower()
            play_on_youtube(video)

        elif 'search on google' in query:
            speak('What do you want to search on Google, mam?')
            query=user_input().lower()
            search_on_google(query)

        elif 'send whatsapp message' in query:
            speak('On What number should i send the message sir? Please enter in the console: ')
            number=input('Enter the number: ')
            speak('What is the message mam?')
            message=user_input().lower()
            send_whatsapp_message(number,message)
            speak("I've sent the message mam.")

        elif 'send an email' in query:
            speak('On what email address do I send sir? Please enter in the console: ')
            receiver_address=input('Enter email address: ')
            speak("What should be the subject mam?")
            subject=user_input().capitalize()
            speak("What's the message mam?")
            message=user_input().capitalize()
            if send_email(receiver_address,subject,message):
                speak("I've sent the email mam.")
            else:
                speak("Something went wrong while I was sending the mail. Please check the error logs.")

        elif 'joke' in query:
            speak(f'Hope you like this one mam')
            joke=get_random_joke()
            speak(joke)
            speak('For your convenience, I am printing it on the screen mam.')
            pprint(joke)

        elif 'advice' in query:
            speak("Here's an advice for you, mam")
            advice=get_random_advice()
            speak(advice)
            speak('For your convenience, I am printing it on the screen mam.')
            pprint(advice)

        elif 'weather' in query:
            city=get_city()
            speak(f"Getting weather report for your city {city}")
            weather,temperature,feels_like=get_weather_report(city)
            speak(f"The current temperature is {temperature}, but it feels like {feels_like}.")
            speak(f"Also the weather report talks about {weather}")
            speak('For your convenience, I am printing it on the screen mam.')
            print(f"Description: {weather}\nTemperature: {temperature}\nFeels like: {feels_like}")

        elif 'news' in query:
            speak(f"I'm reading out the latest news headlines, mam")
            speak(get_latest_news())
            speak('For your convenience, I am printing it on the screen mam.')
            print(*get_latest_news(),sep='\n')


