import webbrowser
import datetime
import wikipedia
from voice import speak


def process_command(command):

    print("Processing:", command)

    # TIME
    if "time" in command:
        time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {time}")

    # DATE
    elif "date" in command:
        date = datetime.datetime.now().strftime("%d %B %Y")
        speak(f"Today is {date}")

    # OPEN WEBSITE
    elif "open" in command:
        site = command.replace("open", "").strip()
        speak(f"Opening {site}")
        webbrowser.open(f"https://www.{site}.com")

    # WIKIPEDIA QUESTIONS
    else:
        try:
            speak("Searching information")
            result = wikipedia.summary(command, sentences=2)
            speak(result)

        except:
            speak("I will search it on Google")
            webbrowser.open(
                f"https://www.google.com/search?q={command}"
            )