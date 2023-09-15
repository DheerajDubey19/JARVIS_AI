import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# machine will wish me

def wishme():
    time=int(datetime.datetime.now().hour)
    if time>=0 and time<6:
        speak("Good Night Dear")
    elif time>=6 and time<12:
        speak("Good Morning Sir, How may i help you")
    elif time>=12 and time<18:
        speak("Good Afternoon Dear")
    else:
        speak("Good Evening Dear")


def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold=1
        r.energy_threshold= 20
        audio=r.listen(source)
    try:
        print('Recognizing..')
        query = r.recognize_google(audio, language ='en-in')
        print(f"user said : {query}\n")

    except Exception as e:
        # print(e)
        print('Speak again')
        return "none"
    return query


# if __name__ == "__main__":
    # speak("Dheeraj is playboy")

# if __name__ == "__main__":
#     # wishme()
#     takecommand() 

if __name__ == "__main__":
    wishme()
    while True:
    # if 1:
        query = takecommand().lower() #Converting user query into lower case

        # Logic for executing tasks based on query
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)