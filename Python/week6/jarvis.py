"""
Name: jarvis.py
Author: Mikhail Zubko
Created: 2025-02-12
Purpose: Voice recognition from Google Sample code
    using Google Speech Recognition library sample code.
    Google Speech API free usage: 50 times per day
    Wikipedia mode added!
Dependencies:
    Linux: espeak-ng
    Python: pyaudio, setuptools, speechrecognition, pyttsx4, google-api-python-client
"""

import os
import speech_recognition as sr
from tts_cli import TextToSpeech
from wikipedia_oop import WikipediaApp

r = sr.Recognizer()  # define recognizer
tts = TextToSpeech()  # define text-to-speech object
wikiapp = WikipediaApp()


class App:
    def __init__(self):
        self.wiki = False

    def main(self):
        with sr.Microphone(19) as source:
            # calibrage the recognizer to the noise level
            r.adjust_for_ambient_noise(source, duration=1)
            while True:
                try:
                    print("Say something...")
                    audio = r.listen(source, timeout=5)
                    print("Recognizing...")
                    recognized_words = r.recognize_google(
                        audio, language="en-US", show_all=True
                    )
                    recognized_words = recognized_words.get("alternative")[0].get(
                        "transcript"
                    )
                    print(f"You may have said: {recognized_words.lower()}")
                    self.command_handler(recognized_words)
                except KeyboardInterrupt:
                    print("\nExit program")
                    break
                except sr.WaitTimeoutError:
                    print("No speech detected within the timeout")
                except sr.UnknownValueError:
                    print("Google Speech Recognition could not understand audio")
                except sr.RequestError as e:
                    print(f"Google Speech did not respond: {e}")

    def command_handler(self, cmd: str):
        if "stop wikipedia" in cmd.lower():
            tts.speak("Wikipedia mode stopped.")
            self.wiki = False
        if "start wikipedia" in cmd.lower():
            tts.speak("Wikipedia mode started.")
            self.wiki = True
        elif self.wiki:
            tts.speak("Searching in Wikipedia")
            # here voice command will be sent to Wikipedia,
            # then tts will speak the result returned from Wikipedia
            tts.speak(wikiapp.get_wiki(cmd))
        elif "exit program" in cmd.lower():
            tts.speak("Exiting the program")
            os._exit(0)
        elif "open terminal" in cmd.lower():
            tts.speak("Opening the terminal")
            os.system("terminator")
        elif "open browser" in cmd.lower():
            tts.speak("Opening the browser")
            os.system("thorium-browser")
        elif "suspend computer" in cmd.lower():
            tts.speak("The system will be suspended")
            os.system("systemctl suspend")
        elif "shutdown computer" in cmd.lower():
            tts.speak("The system will be shutdown")
            os.system("systemctl poweroff")


if __name__ == "__main__":
    app = App()
    app.main()
