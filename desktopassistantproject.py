import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import pyautogui
import tkinter as tk
engine = pyttsx3.init()
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)
    print("The current time is ", Time)
def date():
    day = int(datetime.datetime.now().day)
    month = int(datetime.datetime.now().month)
    year = int(datetime.datetime.now().year)
    speak("the current date is")
    speak(str(day))
    speak(str(month))
    speak(str(year))
    print("The current date is " + str(day) + "/" + str(month) + "/" + str(year))
def wishme():
    print("Welcome back sir!!")
    speak("Welcome back sir!!")
    hour = datetime.datetime.now().hour
    if 4 <= hour < 12:
        speak("Good Morning Sir!!")
        print("Good Morning Sir!!")
    elif 12 <= hour < 16:
        speak("Good Afternoon Sir!!")
        print("Good Afternoon Sir!!")
    elif 16 <= hour < 24:
        speak("Good Evening Sir!!")
        print("Good Evening Sir!!")
    else:
        speak("Good Night Sir, See You Tomorrow")
    speak("Lilpy at your service sir, please tell me how may I help you.")
    print("Lilpy at your service sir, please tell me how may I help you.")
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(query)
    except Exception as e:
        print(e)
        speak("Please say that again")
        return "Try Again"
    return query
def open_website(website):
    try:
        speak(f"Opening {website}...")
        wb.open(website)
    except Exception as e:
        speak(f"Couldn't open {website}. Please try again later.")
def on_click():
    query = takecommand().lower()
    if "time" in query:
        time()
    elif "date" in query:
        date()
    elif "who are you" in query:
        speak("I'm Lilpy and I'm a desktop voice assistant.")
    elif "how are you" in query:
        speak("I'm fine sir, What about you?")
    elif "fine" in query or "good" in query:
        speak("Glad to hear that sir!!")
    elif "wikipedia" in query:
        try:
            speak("Ok wait sir, I'm searching Wikipedia...")
            open_website("https://www.wikipedia.com")
        except Exception as e:
            speak("Can't find this page sir, please ask something else")
    elif "open youtube" in query:
        open_website("https://www.youtube.com")
    elif "open google" in query:
        open_website("https://www.google.com")
    elif "open stack overflow" in query:
        open_website("https://stackoverflow.com")
    elif "play music" in query:
        open_website("https://www.spotify.com")
    elif "open chrome" in query:
        chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        os.startfile(chrome_path)
    elif "search on chrome" in query:
        try:
            speak("What should I search?")
            search_query = takecommand()
            wb.open(f"https://www.google.com/search?q={search_query}")
        except Exception as e:
            speak("Can't search now, please try again later.")
    elif "remember that" in query:
        speak("What should I remember")
        data = takecommand()
        speak("You said me to remember that " + data)
        with open("data.txt", "w") as file:
            file.write(data)
    elif "do you remember anything" in query:
        try:
            with open("data.txt", "r") as file:
                data = file.read()
                speak("You told me to remember that " + data)
        except FileNotFoundError:
            speak("I don't have any specific information to remember.")
    elif "screenshot" in query:
        try:
            speak("Taking a screenshot...")
            img = pyautogui.screenshot()
            img.save("screenshot.png")
            speak("I've taken a screenshot, please check it")
        except Exception as e:
            speak("Couldn't take a screenshot. Please try again.")
    elif "offline" in query:
        speak("Going offline. Goodbye!")
        exit()
root = tk.Tk()
root.title("Lilpy Voice Assistant")
root.geometry("400x300")  
root.configure(bg="#FDF5E6")
label = tk.Label(root, text="I am Lilpy Voice Assistant", font=("Arial", 20, "bold"), fg="#8F9779",bg="white")
label.pack(pady=20)
button = tk.Button(root, text="Click to Speak", font=("Arial", 16, "bold"), bg="white", fg="#8F9779", command=on_click)
button.pack(pady=30)
root.mainloop()
