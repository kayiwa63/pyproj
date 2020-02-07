import pyttsx3 as px
import speech_recognition as sr
import datetime


engine = px.init()
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning!')

    elif hour>=12 and hour<18:
        speak('Good Afternoon')

    else:
        speak('Good Evening')

    speak('I am Lyn. Please tell me how  may help you')

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-sa')
        print("User said: {query}\n")
    
    except Exception as e:
        print(e)
        print("Say that again please....")
        return "None"
    return query
    
if __name__ == "__main__":
    wishMe()
    takeCommand()
