import pyttsx3
import speech_recognition as sr
import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import tempfile

engine = pyttsx3.init()


def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


def take_command():
    fs = 16000   
    seconds = 6

    try:
        speak("Cheppandi nenu vintunnanu...")

        print("Recording...")

        recording = sd.rec(
            int(seconds * fs),
            samplerate=fs,
            channels=1,
            dtype=np.int16
        )

        sd.wait()

        temp_file = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".wav"
        )

        write(temp_file.name, fs, recording)

        recognizer = sr.Recognizer()

        with sr.AudioFile(temp_file.name) as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.record(source)

        command = recognizer.recognize_google(audio)

        print("You said:", command)

        return command.lower()

    except Exception as e:
        print("REAL MIC ERROR:", e)
        return "none"