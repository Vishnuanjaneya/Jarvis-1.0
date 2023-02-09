import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import psutil
import pyjokes
import os
import pyautogui
import random
import operator
import json
import wolframalpha
import time
from urllib.request import urlopen
import requests
import pywhatkit as kit




engine= pyttsx3.init()
wolframalpha_app_id = "wolfram alpha api"


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def time_():
    Time=datetime.datetime.now().strftime("%I:%M:%S") #for 24 hour clock
    speak("the current time is")
    speak(Time)
 

def date_():
    year = (datetime.datetime.now().year)
    month = (datetime.datetime.now().month)
    date = (datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)


def wishme():
    speak("Welcome back Vishnu!")
    hour = datetime.datetime.now().hour
    if hour >=6 and hour<12:
        speak("Good Morning Sir")
    elif hour >=12 and hour<18:
        speak("Good Afternoon Sir!")
    elif hour >=18 and hour <24:
        speak("Good Evening Sir!")
    else:
        speak("Good Night Sir!")
    speak("JARVIS at your service boss. Please tell me how can I help you sir?")

def Introduction():
    speak("I am JARVIS 1.0 , Personal AI assistant , "
    "I am created by Vishnu , "
    "I can help you in various regards , "
    "I can search for you on the Internet , "
    "I can also grab definitions for you from wikipedia , "
    "In layman terms , I can try to make your life a bed of roses , "
    "Where you just have to command me , and I will do it for you , ")

def Creator():
    speak("Vishnu is an extra-ordinary person ,"
    "He has a passion for Robotics, Artificial Intelligence and Machine Learning ,"
    "He is very co-operative ,"
    "If you are facing any problem regarding the 'Jarvis', He will be glad to help you ")

    


def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-pk')
        print(query)
        
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    # Enable low security in gmail 
    server.login('Your email', 'Your password')
    server.sendmail('Your email', to, content)
    server.close()

def screenshot():
    img = pyautogui.screenshot()
    img.save("C:\\Users\\ADMIN\\Desktop\\mm\\screenshot.png")
    
def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at'+ usage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)
def jokes():
    speak(pyjokes.get_joke())

if __name__ == "__main__":
    wishme()
    
    while True:
        query = TakeCommand().lower()
        
        if 'time' in query: 
            time_()
        elif 'date' in query: 
            date_()
        elif 'wikipedia' in query:
            speak('Searching....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'creator' in query or 'created' in query:
            Creator()
        elif 'how are you' in query:
            speak("I am fine, Sir Thanks for asking")
        elif 'comand mode' in query:
            speak("Command mode activated")
            speak("How are you Sir?")
        elif 'fine' in query or "great" in query: 
                speak("Awesome boss,It's good to know that your great")
        elif'not'in query:
                speak("I hope you get well soon.")
                speak("Awesome boss,It's good to know that your great")
        elif'thankyou'in query or 'thanks' in query:
                speak("Its always my pleasure to help you boss.")
        elif "who am i" in query:
            speak("If you can talk, then definitely you are a human")
        elif "why you came to this world" in query:
            speak("Thanks to Vishnu. further it is a secret")
        elif 'what is love' and 'tell me about love' in query:
            speak("It is 7th sense that destroy all other senses , "
            "And I think it is just a mere illusion , "
            "It is waste of time")
        elif "friends" in query:
            speak("Akash J, Subiksha chechi, Sreeja chechi, Yuva shree, Pavithra, Bharathi, Vijay, Rahul, Ajith Kumar ")
        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = TakeCommand()
                speak("Who is the Reciever?")
                reciever = input("Enter reciever's name: ")
                to = (reciever)
                sendEmail(to,content)
                speak(content)
                speak("Email has been sent.")
            except Exception as e:
                print(e)
                speak("Unable to send the email.")
        elif 'search in chrome' in query:
            speak("What should I search ?")
            chromepath = 'C:\\Program Files\\Google\Chrome\Application\chrome.exe'
            search = TakeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')
        elif 'open youtube' in query:
            speak("What should I search sir?")
            Search_term = TakeCommand().lower()
            speak("Here we go to Youtube\n")
            wb.open("https://www.youtube.com/results?search_query="+Search_term)
            speak("Here the results for"+Search_term)
            
        elif 'open google' in query:
            speak("What should I search?")
            Search_term = TakeCommand().lower()
            wb.open('https://www.google.com/search?q='+Search_term)
            speak("Here the results for"+Search_term)
        elif 'cpu' in query:
            cpu()
        elif 'joke' in query:
            jokes()
        elif 'offline' in query:
            speak("Jarvis going Offline Boss thankyou and have a nice day")
            quit()
        elif "write a note" in query:
            speak("What should i write, sir")
            note = TakeCommand()
            file = open('note.txt', 'w')
            speak("Sir, Should i include date and time")
            dt = TakeCommand()
            if 'yes' in dt or 'sure' in dt:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
                speak('done')
            else:
                file.write(note)
        elif "show note" in query:
            speak("Showing Notes")
            file = open("note.txt", "r")
            print(file.read())
            speak(file.read()) 
        elif 'take screenshot' in query:
            screenshot()
            speak("Done!")
        elif 'play music' in query:
            songs_dir = 'C:\\Users\\ADMIN\\Desktop\\Songs'
            music = os.listdir(songs_dir)
            speak("What should I play?")
            ans = TakeCommand().lower()
            no = int(ans.replace('number',''))
            os.startfile(os.path.join(songs_dir,music[no]))
        elif 'remember that' in query:
            speak("What should I remember ?")
            memory = TakeCommand()
            speak("You asked me to remember that"+memory)
            remember = open('memory.txt','w')
            remember.write(memory)
            remember.close()

        elif 'do you remember anything' in query:
            remember =open('memory.txt', 'r')
            speak("You asked me to remeber that"+remember.read())
        elif 'news' in query:
            try:

                jsonObj = urlopen('''https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=0c7895d312944d62a3283167bf5e4541''')
                data = json.load(jsonObj)
                i = 1
                
                speak('Here are some top news from the times of india')
                print('''=============== TOP HEADLINES ============'''+ '\n')
                
                for item in data['articles']:
                    
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
                    
            except Exception as e:
                print(str(e))
        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            wb.open("https://www.google.com/maps/place/" + location + "")
        elif "calculate" in query:
            
            app_id = "wolfram alpha api"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer) 

        



        #General Questions
        elif "what is" in query or "who is" in query: 
			
			# Use the same API key 
			# that we have generated earlier
            client = wolframalpha.Client("wolfram alpha api")
            res = client.query(query)
            
            try:
                print (next(res.results).text)
                speak (next(res.results).text)
            except StopIteration:
                print ("No results") 
        elif "don't listen" in query or "stop listening" in query:
            speak("for how much seconds you want me to stop listening commands")
            a = int(TakeCommand())
            time.sleep(a)
            print(a)
        elif 'log out' in query:
            os.system("shutdown -l")
        elif 'restart' in query:
            os.system("shutdown /r /t 1")
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")


 
        
            
                

    
    

    
