import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit
import pyautogui

listener = sr.Recognizer()
engine = pyttsx3.init()

engine.setProperty('rate', 165)
engine.setProperty('volume', 1.0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("\nListening...")
            listener.adjust_for_ambient_noise(source, duration=1)
            audio = listener.listen(source, timeout=5)
            command = listener.recognize_google(audio, language='en-IN')
            command = command.lower()
            print("You said:", command)
            return command
    except:
        return ""

def run_assistant():
    speak("Hello, I am your Artificial Intelligence Assistant. How can I help you?")

    while True:
        command = take_command()

        if command == "":
            speak("Say again clearly.")
            continue

        if "name" in command:
            speak("My name is AI Operating System Assistant.")

        elif "time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {current_time}")

        elif "date" in command:
            date = datetime.datetime.now().strftime("%d %B %Y")
            speak(f"Today's date is {date}")

        elif "play" in command:
            song = command.replace("play", "").strip()
            speak(f"Playing {song} on YouTube")
            pywhatkit.playonyt(song)

        elif "search" in command or "tell me about" in command:
            query = command.replace("search", "").replace("tell me about", "").strip()
            speak(f"Searching Wikipedia about {query}")
            try:
                info = wikipedia.summary(query, sentences=2)
                speak(info)
            except:
                speak("Sorry, topic not found on Wikipedia.")

        elif "open chrome" in command:
            speak("Opening Chrome")
            pyautogui.press("win")
            pyautogui.write("chrome")
            pyautogui.press("enter")

        elif "screenshot" in command:
            speak("Taking screenshot now")
            img = pyautogui.screenshot()
            img.save("assistant_screenshot.png")
            speak("Screenshot saved as assistant_screenshot.png")

        elif "shutdown" in command or "stop assistant" in command:
            speak("Shutting down assistant. Goodbye.")
            break

        else:
            speak("I cannot perform this command right now, please try again.")

run_assistant()
