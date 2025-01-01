import time
from .tts import speak
import os
import memory
import webbrowser

def set_alarm(alarm_time):
    speak(f"Alarm set for {alarm_time}.")
    while True:
        current_time = time.strftime("%H:%M")
        if current_time == alarm_time:
            speak("Alarm ringing! Time to wake up.")
            break
        time.sleep(30)  # Check every 30 seconds

def clean_query(command):
    """
    Remove trigger words like 'search Wikipedia for' from a command string.
    """
    query = command.replace("search wikipedia", "").replace("search Wikipedia", "").strip()
    return query


# Function to set and remind user of birthdays
def birthday_reminder(command):
    if "remember my birthday" in command:
        date = command.replace("remember my birthday as", "").strip()
        memory["birthday"] = date
        speak(f"I’ll remember your birthday is on {date}.")
    elif "my birthday" in command:
        birthday = memory.get("birthday", "I don’t know your birthday yet.")
        speak(f"Your birthday is on {birthday}.")
        
        
        
# Function to launch an online game
def play_game(command):
    if "chess" in command:
        speak("Opening Chess.com")
        webbrowser.open("https://www.chess.com")
    elif "sudoku" in command:
        speak("Opening Sudoku.com")
        webbrowser.open("https://www.sudoku.com")
    elif "scrabble" in command:
        speak("Opening skribbl.io")
        webbrowser.open("https://skribbl.io/")
    else:
        speak("I'm sorry, I can't able to find that game.")