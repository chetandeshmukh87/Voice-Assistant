import pyttsx3 
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
from random import randint
import pywhatkit

# create a text-to-speech engine
engine = pyttsx3.init('sapi5')
engine.setProperty('volume', 1.0)
# Getting available properties: engine has inbuilt voices in it that are extracted using the following command
voices = engine.getProperty('voices')

# Setting the voice property: setting the voice of female
engine.setProperty('voice', voices[1].id)

# defining a speak function for the engine for the passed audio
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# creating a wish function upon start
def wishMe():
    hour = int(datetime.datetime.now().hour)

    if (hour>= 0 and hour<6):
        speak("Hi sir!")

    elif(hour >= 6 and hour<12):
        speak("Good Morning Sir!")

    elif(hour >=12 and hour<18):
        speak("Good Afternoon Sir!")

    else:
        speak("Good Evening Sir!")

    speak("I am Friday. How may I help you?")
   

# Quit function    
def quitNow():
    hour = int(datetime.datetime.now().hour)

    if (hour>= 18 and hour<=24) or(hour >0 and hour <=5):
        speak("Have a good night Sir!")

    else:
        speak("Have a good day sir!")

    speak("See you later.")




def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio)
        print("You said:" , query)
        speak("You said")
        speak(query)

    except:
        print("Could not recognize. Please repeat.")
        return "None"

    return query



if __name__ == "__main__":
    wishMe()
    
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching wikipedia....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube'  in query or 'start youtube' in query:
            speak("Opening Youtube")
            webbrowser.open("youtube.com")
        
        elif 'on youtube' in query:
            song = query.replace('play', '')
            speak('playing your video')
            pywhatkit.playonyt(song)

        elif 'open google'  in query or 'start google' in query:
            speak("Opening Google")
            webbrowser.open("google.com")

        elif 'open stack overflow'  in query or 'start stack overflow' in query or 'open stackoverflow'  in query or 'start stackoverflow' in query:
            speak("Opening Stackoverflow")
            webbrowser.open("stackoverflow.com")

        elif 'open facebook'  in query or 'start facebook' in query:
            speak("Opening Facebook")
            webbrowser.open("facebook.com")

        elif 'open instagram'  in query or 'start instagram' in query:
            speak("Opening Instagram")
            webbrowser.open("instagram.com")

        elif 'play music' in query:
            dir = 'G:\\songs\\Hindi'
            songs = os.listdir(dir)
            speak("Playing Music Sir. Enjoy!")
            os.startfile(os.path.join(dir, songs[randint(0, len(songs)-1)]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak("Sir, the current time is:")
            speak(strTime)

        elif 'open visual studio' in query:
            path = "F:\\VisualCode\\Microsoft VS Code\\Code.exe"
            speak("Opening Visual Studio. Happy coding sir!")
            os.startfile(path)

        elif 'quit' in query or 'stop' in query or 'exit' in query:
            quitNow()
            exit()
