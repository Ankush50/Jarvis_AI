#for male voice
# import pyttsx3

# # Initialize the text-to-speech engine
# engine = pyttsx3.init()

# # Set TTS properties
# engine.setProperty("rate", 150)
# engine.setProperty("volume", 0.9)

# def speak(text):
#     engine.say(text)
#     engine.runAndWait()


#for female voice 

import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Get available voices
voices = engine.getProperty('voices')

# Set the voice to a female one (index may vary)
engine.setProperty('voice', voices[1].id)  # Usually, index 1 is female

# Optional: Set speech rate and volume
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 0.9)  # Volume level (0.0 to 1.0)

# Now, the engine will use the female voice by default

def speak(text):
    engine.say(text)
    engine.runAndWait()