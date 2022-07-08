import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os  # for music
import smtplib  # for mails :Simple Mail Transfer Protocol
import pywhatkit
import random
import operator
import json
from urllib.request import urlopen
import requests
import time
import pyautogui  # (For Screenshot)
import pyjokes
import winshell
import wolframalpha
import spotipy
import spotipy.util as util
from json.decoder import JSONDecodeError
import string
import urllib
from os import startfile
from pyautogui import click
from keyboard import press
from keyboard import write
from time import sleep


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time_():
    Time = datetime.datetime.now().strftime("%H:%M:%S")  # for 24 hour clock
    speak("the current time is")
    speak(Time)


def date():
    year = (datetime.datetime.now().year)
    month = (datetime.datetime.now().month)
    date = (datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)


def wishme():
    speak("Welcome back Ayush sir!")
    time_()
    date()
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good Morning Sir")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir!")
    elif hour >= 18 and hour < 24:
        speak("Good Evening Sir!")
    else:
        speak("Good Night Sir!")
    speak("TAASK at your service. Please tell me  how can I help you?")


def takecommand():
    # It takes micrphone input from the user and returns string as ouput

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)

        print("Say that again plaese...")
        return "None"

    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    # sender's mail address
    server.login('aimupsc09@gmail.com', '@aimupsc2909')
    server.sendmail('aimupsc09@gmail.com', to, content)
    server.close()


def Introduction():
    speak("I am TAASK 1.0 , Personal AI assistant , "
          "I am created by Ayush , "
          "I can help you in various regards , "
          "I can search for you on the Internet , "
          "I can also grab definitions for you from wikipedia , "
          "In layman terms , I can try to make your life a bed of roses , "
          "Where you just have to command me , and I will do it for you , ")


def Creator():
    speak("Ayush is an extra-ordinary person ,"
          "He has a passion for Robotics, Artificial Intelligence and Machine Learning ,"
          "He is very co-operative ,"
          "If you are facing any problem regarding the 'Jarvis', He will be glad to help you ")


def Spotify(song_name, Play):
    startfile("C:\\Users\\pinga\\AppData\\Roaming\\Spotify\\Spotify.exe")

    sleep(6)

    click(x=112, y=124)  # for search

    sleep(1)

    click(x=593, y=38)  # selcting where we type songs

    write(song_name)

    sleep(5)
    click(x=858, y=358)  # selcecting songs

    sleep(2)
    click(x=378, y=489)  # for clicking on play button
    sleep(2)
    click(x=1796, y=23)  # for minimizing spotify


def WhatsappMsg(name, message):
    startfile("C:\\Users\\pinga\\AppData\\Local\\WhatsApp\\WhatsApp.exe")

    sleep(10)

    click(x=135, y=149)

    sleep(1)

    write(name)

    sleep(1)
    click(x=104, y=286)
    sleep(1)
    click(x=775, y=982)
    sleep(1)
    write(message)
    press('enter')


def screenshot():
    img = pyautogui.screenshot()
    img.save("C:\\Users\\pinga\Desktop\\screenshot")


def jokes():
    speak(pyjokes.get_joke())


class SpotifyClient(object):
    def __init__(self, api_token):
        self.api_token = api_token

    def get_random_tracks(self):
        wildcard = f'%{random.choice(string.ascii_lowercase)}%'
        query = urllib.parse.quote(wildcard)
        offset = random.randint(0, 2000)
        url = f"https://api.spotify.com/v1/search?q={query}&offset={offset}&type=track"
        response = requests.get(
            url,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_token}"
            }
        )
        response_json = response.json()

        tracks = [
            track for track in response_json['tracks']['items']
        ]

        print(f'Found {len(tracks)} tracks to add to your library')

        return tracks

    def add_tracks_to_library(self, track_ids):
        url = "https://api.spotify.com/v1/me/tracks"
        response = requests.put(
            url,
            json={
                "ids": track_ids
            },
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_token}"
            }
        )

        return response.ok


if __name__ == "__main__":

    
    wishme()
    while True:
        query = takecommand().lower()
        # Logic for executinng tasks based on query
        if "wikipedia" in query:  # for any results you want to search on wikipedia
            speak("Searching Wikipedia...")
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "who are you" in query:
            Introduction()

        elif 'how are you' in query:
            speak("I am fine, Sir Thanks for asking")
            speak("How are you Sir?")
            if 'fine' in query or "good" in query:
                speak("It's good to know that your fine")
            else:
                speak("I hope you get well soon.")
        elif 'open youtube' in query:
            speak("What should I search?")
            Search_term = takecommand().lower()
            if Search_term == "home":
                webbrowser.open("https://www.youtube.com/")
            else:

                speak("Here we go to Youtube\n")
                webbrowser.open(
                    "https://www.youtube.com/results?search_query="+Search_term)
                time.sleep(5)

        elif 'open Google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
      # elif 'open Instagram' in query:
          #  webbrowser.open("instagram.com")
        elif 'play music' in query:
            music = "C:\\Users\\pinga\\Desktop\\Songs"
            Desktop = os.listdir(music)
            print(Desktop)
            os.startfile(os.path.join(music, Desktop[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif "open vs code" in query:
            vscode = "C:\\Users\\pinga\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vscode)
        elif "open cmd" in query:
            cmd = "%windir%\system32\cmd.exe"
            os.startfile(cmd)
        elif 'email to my brother' in query:
            try:
                speak("What should I say?")
                content = takecommand()
                  #reciver's mail address
                to = "ayushsharma7403@gmail.com",
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend ayush . I am not able to send this email")
        elif "exit" in query:
            activateRecognition = False
            speak("Exiting. Have a nice day sir.")
            print("Closing Jarvis...")
        elif 'take screenshot' in query:
            screenshot()
            speak("Done!")

    # show location on map
        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open(
                "https://www.google.com/maps/place/" + location + "")

        elif "who am i" in query:
            speak("If you can talk, then definitely you are a human")
        elif "why you came to this world" in query:
            speak("Thanks to Ayush Sir and TAASK team. further it is a secret")

        elif 'search in chrome' in query:
            speak("What should I search ?")
            chromepath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            search = takecommand().lower()
            webbrowser.get(chromepath).open_new_tab(search)

        elif 'remember that' in query:      # for creating text file by just voice commands
            speak("What should I remember ?")
            memory = takecommand()
            speak("You asked me to remember that"+memory)
            remember = open('memory.txt', 'w')
            remember.write(memory)
            remember.close()
        elif 'do you remember anything' in query:
            remember = open('memory.txt', 'r')
            speak("You asked me to remeber that"+remember.read())

        elif "write a note" in query:
            speak("What should i write, sir")
            note = takecommand()
            file = open('note.txt', 'w')
            speak("Sir, Should i include date and time")
            dt = takecommand()
            if 'yes' in dt or 'sure' in dt:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
                speak('done')
            else:
                file.write(note)
        elif "open WhatsApp" in query:
            WhatsappMsg(
                "AIM_UPSC", "Hi this is TAASk Assitant, Call from Ayush Sir")
        elif "show note" in query:
            speak("Showing Notes")
            file = open("note.txt", "r")
            print(file.read())
            speak(file.read())

        elif 'word' in query:
            speak("opening MS Word")
            word = r'Word path'
            os.startfile(word)
        elif "weather" in query:   # for temperature in your city

            # Google Open weather website
            # to get API of Open weather
            api_key = "open weather api"
            base_url = "http://api.openweathermap.org/data /2.5/weather?q="
            speak(" City name ")
            print("City name : ")
            city_name = takecommand()
            complete_url = base_url + "appid =" + api_key + "&q =" + city_name
            response = requests.get(complete_url)
            x = response.json()

            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                print(" Temperature (in kelvin unit) = " + str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(
                    current_pressure) + "\n humidity (in percentage) = " + str(current_humidiy) + "\n description = " + str(weather_description))

            else:
                speak(" City Not Found ")
        elif "play spotify" in query:
            speak("What should I play")
            Search_term = takecommand().lower()
            Spotify(Search_term, "Play")

        elif 'news' in query:  # news headlines

            try:

                jsonObj = urlopen(
                    "https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en")
                data = json.load(jsonObj)
                i = 1

                speak('here are some top news from the times of india')
                print('''=============== TOP HEADLINES ============''' + '\n')

                for item in data['articles']:

                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1

            except Exception as e:
                print(str(e))

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            speak("Recycle Bin Recycled")
        elif 'offline' in query:  # for stopping assistant
            speak("going Offline")
            quit()
