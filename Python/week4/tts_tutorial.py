import pyttsx3

engine = pyttsx3.init()  # initialize and create an object
# set properties
RATE = 175
VOLUME = 0.7
VOICE = 1
engine.setProperty("rate", RATE)
engine.setProperty("volume", VOLUME)
voices = engine.getProperty("voices")
for voice in voices:
    print(voice)
engine.setProperty("voice", voices[VOICE].id)
# get user input
speak = input("What would you like to say? ").strip()

engine.say(speak)

engine.runAndWait()
