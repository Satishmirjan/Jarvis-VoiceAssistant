import speech_recognition as sr
import pyttsx3
import webbrowser
import musical

recognizer = sr.Recognizer()
ttsx = pyttsx3.init()

def speak(line):
    ttsx.say(line)
    ttsx.runAndWait()

def process(com):
    if "open google" in com.lower():
        webbrowser.open("http://google.com")
        speak("Executed successfully")
    elif "open facebook" in com.lower():
        webbrowser.open("http://facebook.com")
        speak("Executed successfully")
    elif "open linkedin" in com.lower():
        webbrowser.open("http://linkedin.com")
        speak("Executed successfully")
    elif "open youtube" in com.lower():
        webbrowser.open("http://youtube.com")
        speak("Executed successfully")
    elif com.lower().startswith("play"):
        song=com.lower().split(" ")[1]
        link=musical.music[song]
        webbrowser.open(link)

if __name__ == "__main__":
    speak("Hello, my name is Jarvis. What can I do for you, Satish?")

    while True:
       
        try:
            with sr.Microphone() as source:
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=1)
            word = recognizer.recognize_google(audio)
            if word.lower() == "hello":
                speak("Yes, I am here")


                with sr.Microphone() as source:
                    audio = recognizer.listen(source)
                    order = recognizer.recognize_google(audio)
                    process(order)

        except Exception as e:
            print("Error occured: {0}".format(e))

