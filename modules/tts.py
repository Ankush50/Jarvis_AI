import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set TTS properties
engine.setProperty("rate", 150)
engine.setProperty("volume", 0.9)

def speak(text):
    engine.say(text)
    engine.runAndWait()