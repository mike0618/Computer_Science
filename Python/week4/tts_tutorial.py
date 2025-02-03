import pyttsx4  # this is a fork of pyttsx3
# pyttsx3 did not work on my Linux
# also I installed alsa-utils

engine = pyttsx4.init()  # initialize and create an object
# set properties
RATE = 175
VOLUME = 0.7
# VOICE = 1
engine.setProperty("rate", RATE)
engine.setProperty("volume", VOLUME)
# voices = engine.getProperty("voices")
# for voice in voices:
#    print(voice)  # see what voices are available
# engine.setProperty("voice", voices[VOICE].id)
engine.setProperty("voice", "English (America)")
# get user input
speak = input("What would you like to say? ").strip()

engine.say(speak)

engine.runAndWait()
