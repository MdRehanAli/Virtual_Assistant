import speech_recognition as sr
import pyttsx3 as tts
import pywhatkit as kit


listener = sr.Recognizer()
Speaker = tts.init()

#Change Voices 0 for male and 1 for female
voices = Speaker.getProperty('voices')
Speaker.setProperty('voice', voices[1].id)

def talk(text):
    Speaker.say(text)
    Speaker.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('Now I am listening')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()

            if 'siri' in command:
                command = command.replace('siri', '')
                print(command)
    except:
        pass
    return command

def run_siri():
    command = take_command()
    print(command)

    #Playing anything using Youtuber
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing')
        kit.playonyt(song)

run_siri()
