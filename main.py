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
def run_siri():
    Command = take_Command()
    print(Command)

    # Let's Introduce about my Assistant
    if 'are you' in Command:
        print('My name is Siri & I am invented by team phantom.')
        talk('My name is Siri & I am invented by team phantom.')

    elif 'yourself' in Command:
        print('My name is Siri & I am invented by team phantom.')
        talk('My name is Siri & I am invented by team phantom.')

    # Simple Conversation like:    Hi, Hello or Good Morning
    elif 'siri' in Command:
        Command = Command.replace('siri', '')
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

    # Repeating the previous Command

    else:
        talk('Please say the Command again.')

# Call under while loop
while True:
    run_siri()