"""
Name: tts_cli.py
Author:
Created:
Purpose: Render text into speech
"""

# pip install pyttsx4
import pyttsx4


class TextToSpeech:
    def __init__(self):
        # -------------- INITIALIZE TEXT TO SPEECH ENGINE ------------ #
        self.engine = pyttsx4.init()  # initialize and create an object
        # set properties
        # --------------- VOICE PROPERTIES CONSTANTS ----------------- #
        RATE = 175
        VOLUME = 0.7
        # VOICE = 1
        # ------------------ SET VOICE PROPERTIES -------------------- #
        self.engine.setProperty("rate", RATE)
        self.engine.setProperty("volume", VOLUME)
        self.engine.setProperty("voice", "English (America)")

    def speak(self, speak):
        self.engine.say(speak)
        self.engine.runAndWait()


def main():
    # Create text to speech object
    text_to_speech = TextToSpeech()
    while True:
        try:
            # Get input from user
            speak = input("What would you like me to say? ").strip()
            # exit if no input
            if not speak:
                break
            # Queue up things to say
            text_to_speech.speak(speak)
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"Something went wrong:\n{e.with_traceback(None)}")
    text_to_speech.speak("Bye!")


if __name__ == "__main__":
    main()
