import pyttsx3      # pip install pyttsx3
import datetime     
import speech_recognition as sr     #pip install SpeechRecognition
import wikipedia        #pip install wikipedia
import webbrowser       #pip install webbrowser
import os
import pyautogui        #pip install pyautogui
import pyjokes          #pip install pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishings():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Jarvis: Good Morning BOSS")
        speak("Good Morning BOSS")
    elif hour>=12 and hour<17:
        print("Jarvis: Good Afternoon BOSS")
        speak("Good Afternoon BOSS")
    elif hour>=17 and hour<21:
        print("Jarvis: Good Evening BOSS")
        speak("Good Evening BOSS")
    else:
        print("Jarvis: Good Night BOSS")
        speak("Good Night BOSS")
    
    

# * BEFORE RUNNING THE CODE MAKE SURE YOU HAVE INTERNET CONNECTION *
def commands():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source, duration=1)
        audio=r.listen(source)

    try:
        print("Wait for few Moments..")
        query=r.recognize_google(audio,language='en-in')
        print(f"You just said: {query}\n")

    except Exception as e:
        print(e)
        speak("Please tell me again")
        query="none"
    return query

def wakeUpCommands():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Jarvis is Sleeping...")
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source,duration=1)
        audio=r.listen(source)
    try:
        query=r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        query="none"
    return query


if __name__ == "__main__":          # Before running the code make sure you have Internet Connection 
    
    while True:
        query=wakeUpCommands().lower()
        if "wake up" in query:
            wishings()
            speak("Yes BOSS What can I do for you!")
            while True:
                
                query=commands().lower()
                if "wikipedia" in query:
                    speak("Searching in Wikipedia")
                    try:
                        query=query.replace("wikipedia","")
                        results=wikipedia.summary(query,sentences=1)
                        speak("According to Wikipedia,")
                        print(results)
                        speak(results)
                    except:
                        speak("No Results found Sir...")
                        print("No results Found")
                
                elif "open youtube" in query:
                    speak("opening Youtube")
                    webbrowser.open("youtube.com")

                elif 'time' in query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                    speak(f"Sir, the time is {strTime}")

                elif "mute" in query:
                    speak("I'm Muting Sir...")
                    break
                elif 'exit program' in query or 'exit the program' in query:
                    speak("I'm Leaving Sir, Byeee...")
                    quit()
                
                elif "open google" in query:
                    speak("Opening Google Chrome Sir")
                    os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")        # Use the path of your file here
                    while True:
                        chromeQuery=commands().lower()
                        if "search" in chromeQuery:
                            youtubeQuery=chromeQuery
                            youtubeQuery=youtubeQuery.replace("search","")
                            pyautogui.write(youtubeQuery)
                            pyautogui.press('enter')
                            speak('Searching...')
                            
                        elif "close chrome" in chromeQuery or "exit chrome" in chromeQuery or "exit google" in chromeQuery or "close window" in chromeQuery or "close this window" in chromeQuery:
                            pyautogui.hotkey('ctrl','w')
                            speak("Closing Google Chrome Sir...")
                            break
                
               
                elif "what can you do for me" in query:
                    speak('Yes sir, Nice Question')
                    speak('As per my Program, I\'m a bot which can perform tasks through your voice commands')
                elif "cool" in query or "nice" in query or "awsome" in query or "thank you" in query:
                    speak("Yes sir, That's my Pleasure!")
                elif "minimize" in query or 'minimise' in query:
                    speak('Minimizing Sir')
                    pyautogui.hotkey('win', 'down','down')
                elif "maximize" in query or 'maximise' in query:
                    speak('Maximizing Sir')
                    pyautogui.hotkey('win', 'up','up')
                elif "close the window" in query or 'close the application' in query:
                    speak('Closing Sir')
                    pyautogui.hotkey('ctrl','w')
                elif "screenshot" in query:
                    speak("Taking Screenshot sir...")
                    pyautogui.press('prtsc')
                elif "open paint" in query:
                    speak("Opening Paint Application Sir...")           
                    os.startfile('C:\\Windows\\System32\\mspaint.exe')      # Use the path of your file here
                    while True:
                        paintQuery=commands().lower()
                        if "close" in paintQuery:
                            speak("Closing The Application sir")
                            pyautogui.leftClick(x=1344, y=11)
                            break
                        elif "paste" in paintQuery:
                            pyautogui.hotkey('ctrl', 'v')
                            speak("Done Sir!")
                        elif "save" in paintQuery:
                            pyautogui.hotkey('ctrl','s')
                            speak("saving sir!")
                        elif "minimize" in paintQuery:
                            speak('Minimizing Sir')
                            pyautogui.hotkey('win', 'down','down')
                            break
                        elif "maximize" in paintQuery:
                            speak('Maximizing Sir')
                            pyautogui.hotkey('win', 'up','up')
                        elif "minimise" in paintQuery:
                            speak('Minimizing Sir')
                            pyautogui.hotkey('win', 'down','down')
                        elif "maximise" in paintQuery:
                            speak('Maximizing Sir')
                            pyautogui.hotkey('win', 'up','up')
                elif "open notepad" in query:
                    speak("Opening Notepad Application sir...")
                    os.startfile('C:\\Windows\\System32\\notepad.exe')          # Use the path of your file here
                    while True:
                        notepadQuery=commands().lower()
                        if "paste" in notepadQuery:
                            pyautogui.hotkey('ctrl','v')
                            speak("Done Sir!")
                        elif "save this file" in notepadQuery:
                            pyautogui.hotkey('ctrl','s')
                            speak("Sir, Please Specify a name for this file")
                            notepadSavingQuery=commands()
                            pyautogui.write(notepadSavingQuery)
                            pyautogui.press('enter')
                        elif 'type' in notepadQuery:
                            speak("Please Tell me what should I Write...")
                            while True:
                                writeInNotepad=commands()
                                if writeInNotepad == 'exit typing':
                                    speak("Done Sir.")
                                    break
                                else:
                                    pyautogui.write(writeInNotepad)
                                
                        elif "exit notepad" in notepadQuery or 'close notepad' in notepadQuery:
                            speak('quiting Notepad Sir...')
                            pyautogui.hotkey('ctrl', 'w')
                            break
                elif 'play song' in query or 'sing a song' in query or 'play a song' in query or 'play music' in query or 'play a music' in query:
                    speak("Yes Sir Please Wait a moment")
                    songs=os.listdir('B:\Musics')       # Use the path of your file here
                    os.startfile(os.path.join('B:\Musics',songs[0]))        # Use the path of your file here
                elif 'pause' in query or 'pass' in query:
                    pyautogui.press('space')
                    speak('Done Sir')
                elif 'joke' in query:
                    jarvisJoke = pyjokes.get_joke()
                    print(jarvisJoke)
                    speak(jarvisJoke)
