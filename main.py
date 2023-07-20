# For converting Speech to text
import speech_recognition as sr

# For converting text to Speech
import pyttsx3 as tts

# Use for playing music by using google
import pywhatkit as kit

# Current Date And Time
import datetime as dt

# Find a result from wikipedia
import wikipedia as wiki

# Randomly get a joke
import pyjokes as pj

import os

import subprocess

import webbrowser

#tkinter is a GUI of python
from tkinter import *
from PIL import ImageTk,Image


listener = sr.Recognizer()
Speaker = tts.init()

# Change Voices 0 for male and 1 for female
voices = Speaker.getProperty('voices')
Speaker.setProperty('voice', voices[0].id)

def talk(text):
    Speaker.say(text)
    Speaker.runAndWait()

# Taking and Printing any Command
def take_Command():
    try:
        Command = ""
        with sr.Microphone() as source:
            talk('I am ready Sir. Please tell me, how can I help you?')
            print('Now I am listening...........')
            voice = listener.listen(source)
            Command = listener.recognize_google(voice)
            Command = Command.lower()

    except:
        pass
    return Command

# Taking and Printing any Command
def run_Jonny():
    Command = take_Command()
    print(Command)

    # Let's Introduce about my Assistant
    if 'who are you' in Command:
        print('My name is Jonny & I am invented by Team Phantom. The members of team phantom are Md Rehan Ali and Md Sabbir Ahmed.')
        talk('My name is Jonny & I am invented by Team Phantom. The members of team phantom are Md Rehan Ali and Md Sabbir Ahmed.')

    elif 'yourself' in Command:
        print('My name is Jonny & I am invented by Team Phantom. The members of team phantom are Md Rehan Ali and Md Sabbir Ahmed.')
        talk('My name is Jonny & I am invented by Team Phantom. The members of team phantom are Md Rehan Ali and Md Sabbir Ahmed.')

    # Simple Conversation like:    Hi, Hello or Good Morning
    elif 'jonny' in Command:
        Command = Command.replace('jonny', '')
        print(Command)
        talk(Command)

    # Playing anything using Youtuber
    elif 'play' in Command:
        song = Command.replace('play', '')
        talk('playing'+song)
        kit.playonyt(song)

    # Time and date
    elif 'time' in Command:
        time = dt.datetime.now().strftime('%H:%M')
        print(time)
        talk('Current time is ' + time)

    # Wikipedia Searching person by mentioning who is
    elif 'who is' in Command:
        person = Command.replace('who is', '')
        info = wiki.summary(person, 2)
        print(info)
        talk(info)

    # Wikipedia Searching something by mentioning what is
    elif 'what is' in Command:
        something = Command.replace('what is', '')
        result = wiki.summary(something, 2)
        print(result)
        talk(result)

    # Randomly Generated jokes
    elif 'joke' in Command:
        Jokes = pj.get_joke()
        print(Jokes)
        talk(Jokes)

    elif 'shutdown' in Command:
        print(Command)
        talk('Wait a Sec ! Your system is on its way to shut down.')
        os.system('shutdown /s /t 0')

    elif 'restart' in Command:
        print(Command)
        talk('Wait a Sec ! Your system is on its way to restart.')
        os.system('shutdown /r /t 0')

    elif 'notepad' in Command:
        print(Command)
        talk('Opening notepad')
        subprocess.Popen('notepad')

    elif 'browser' in Command:
        print(Command)
        talk('Opening Web browser')
        webbrowser.open('https://www.google.com')

    elif 'search' in Command:
        Search = Command.replace('search', '')
        talk('searching' + Search)
        print(Command)
        webbrowser.open('https://www.google.com/search?q=' + Search)

    elif 'calculator' in Command:
        print('Opening Calculator')
        talk('Opening Calculator')
        subprocess.Popen('calc.exe')

    elif 'photo' in Command:
        print('Opening your desired photo')
        talk('Opening your desired photo')
        file_path = 'D:\Programming\Python\Virtual_Assistant\Assistant.jpg'
        image = Image.open(file_path)
        image.show()

    elif 'pdf' in Command:
        print('Opening your desired pdf file')
        talk('Opening your desired pdf file')
        file_path = r'D:\Programming\Python\Virtual_Assistant\Assistant.pdf'
        os.startfile(file_path)

    elif 'video' in Command:
        print('Opening your desired video file')
        talk('Opening your desired video file')
        file_path = r'D:\Programming\Python\Virtual_Assistant\Assistant.mp4'
        os.startfile(file_path)

    elif 'powerpoint file' in Command:
        print('Opening powerpoint file file')
        talk('Opening powerpoint file file')
        file_path = r'D:\Programming\Python\Virtual_Assistant\Assistant.pptx'
        os.startfile(file_path)

    elif 'word' in Command:
        print('Opening MS word')
        talk('Opening MS word')
        application = r'C:\Program Files\Microsoft Office\Office16\WINWORD.EXE'
        os.startfile(application)

    elif 'excel' in Command:
        print('Opening MS Excel')
        talk('Opening MS Excel')
        application = r'C:\Program Files\Microsoft Office\Office16\EXCEL.EXE'
        os.startfile(application)


    elif 'powerpoint' in Command:
        print('Opening MS powerpoint')
        talk('Opening MS powerpoint')
        application = r'C:\Program Files\Microsoft Office\Office16\POWERPNT.EXE'
        os.startfile(application)

    elif 'code blocks' in Command:
        print('Opening Code blocks')
        talk('Opening Code blocks')
        application = r'C:\Program Files\CodeBlocks\codeblocks.exe'
        os.startfile(application)



    # Repeating the previous Command

    else:
        talk('Please click the run button and say the Command again.')

# Call under while loop
#while True:
    #run_Jonny()

#tkinter is a GUI of python

root = Tk()

root.title('Virtual Assistant')
root.geometry('320x320')

#img = ImageTk.PhotoImage(Image.open('Assistant.jpg'))
#panel = Label(root, image=img)
#panel.pack(side='right', fill='both', expand='no')

userText = StringVar()

userText.set('Welcome to our Virtual World!')
userFrame = LabelFrame(root, text='', font=('Railways', 20, 'bold'))
userFrame.pack(fill='both', expand='yes')

top = Message(userFrame, textvariable=userText, bg='light blue', fg='dark blue')
top.config(font=("Tahoma", 25, 'bold'))
top.pack(side='top', fill='both', expand='yes')

btn1 = Button(root, text='Run', font=('Tahoma', 18, 'bold'), bg='light green', fg='Green', command=run_Jonny)
btn1.pack(fill='x', expand='no')

btn2 = Button(root, text='Close', font=('Tahoma', 18, 'bold'), bg='light yellow', fg='red', command=root.destroy)
btn2.pack(fill='x', expand='no')

root.mainloop()