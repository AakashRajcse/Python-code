import datetime
import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import os
import random

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)  #female voice
engine.setProperty('rate', 150) #Rate of speech 150
print(type(engine))
print(engine)

def speak(msg):  #to speak. text to speech
    engine.say(msg)
    engine.runAndWait()


def wishMe():
    hour=int(datetime.datetime.now().hour)
    #minute=int(datetime.datetime.now().minute)
    if(hour>=0 and hour<12):
        speak("Good Morning Aakash!")   #Text to speech
    elif(hour>=12 and hour<18):
        speak("Good Afternoon Aakash")
    else:
        speak("Good Evening Aakash")
    speak("I am your Virtual Assistant, How may I help you?")

def takeCommand():   #speech to text converter
    r=sr.Recognition()   #recogniser class help in recognising the audio
    with sr.Microphone() as source:
        print("Listening ..")
        r.pause_threshold = .05  #it refers to the amount of time gap after which
        r.enregy_threshold=300 # Noise cancellation
        audio=r.listen(source)   #digitaldata of whatsoever hs been spoken will be
    try:
        print("Recognising..")
        query=r.recognize_google(audio,language="en-in")
        print("User Said:",query)
    except Exception as e:
        print("Say that again please!")
        return "None"

#pl
wishMe()
#while True:
if 1:
    query = takeCommand().lower()   #search covid 19 on wikipedia
    #logic for executing takes based on query
    if 'wikipedia' in query:   #wikipedia is a keyword. if user does
        speak("Searching Wikipedia")
        query=query.replace("wikipedia","")  #search covid on
        results=wikipedia.summary(query,sentences=2)
        speak("According to wikipedia")
        print(results)
        print(results)
    elif 'youtube' in query:
        webbrowser.open("youtube.com")

    elif 'facebook' in query:
        webbrowser.open("fb.com")
    elif 'stackoverflow' in query:
        webbrowser.open("stackoverflow.com")

    elif 'google' in query:  # search python tutorial on google
        query=query.replace("google","")  #search python tutorial on
        query=query.replace("search","")  #python tutorial on
        webbrowser.open("https://google.com/search?g= + query")
    elif(('music' in query) or ("song" in query)):
        music_dir='D:\\mySong' #\\slash is to escape the character
        song=os.listdir(music_dir)  #listdir is used to enlist all the songs of mentioned directory
        #print(songs)
        rdm_song=random.choice(song)
       # os.startfile(os.path.join(music_dir,song[0]))  #song[0  will play the first song using random music
        os.startfile(music_dir+'/'+rdm_song)
    elif 'time' in query:
        time=datetime.datetime.now().strftime("%H:%M")
        speak("sir, the time,is")
        speak(time)
    elif 'sleep' in query:
        speak("Thanks you")
        exit()
