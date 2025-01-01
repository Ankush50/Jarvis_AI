from modules import tts
from modules.wikipedia_utils import search_wikipedia
from .stt import listen
from .tts import speak
import random

def handle_command(command):
    if "hello" in command:
        tts.speak("Hello, I am JARVIS. How can I assist you today?")
    elif "time" in command:
        from datetime import datetime
        tts.speak(f"The current time is {datetime.now().strftime('%H:%M')}")
    # Add more commands here...

def engage_conversation():
    speak("Let's have a chat. How are you feeling today?")

    while True:
        command = listen()
        if command:
            if "good" in command or "fine" in command:
                speak("That's great to hear! What made your day good?")
                follow_up_question("good")
            elif "bad" in command or "not well" in command:
                speak("I'm sorry to hear that. What seems to be bothering you?")
                follow_up_question("bad")
            elif "help" in command:
                speak("I’m here for you. What do you need help with?")
            elif "exit" in command or "stop" in command:
                speak("Goodbye! I'm always here for you.")
                break
            elif "search" in command:
                search_wikipedia(command)
            else:
                handle_command(command)
                
                
def follow_up_question(emotion):
    if emotion == "good":
        questions = [
            "What did you do today?",
            "Do you have any plans for the weekend?",
            "What’s something that made you smile?"
        ]
    else:
        questions = [
            "What’s been troubling you lately?",
            "Is there something specific you'd like to talk about?",
            "Would you like to hear a joke or something uplifting?"
        ]

    question = random.choice(questions)
    speak(question)