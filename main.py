import speech_recognition
import pyttsx3
from termcolor import cprint
from ai import GenAi

ai = GenAi()

recognizer = speech_recognition.Recognizer()

while True:
    cprint("Listening...", "cyan", attrs=["bold"])

    try:
        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)

            text = recognizer.recognize_google(audio)
            text = text.lower()

            cprint(f"Recognized: {text}", "green", attrs=["bold"])
            cprint(f"AI: {ai.send_message(text)}", "green", attrs=["bold"])

    except speech_recognition.UnknownValueError:

        recognizer = speech_recognition.Recognizer()
        cprint("Sorry, I did not hear that", "red", attrs=["bold"])

        continue
