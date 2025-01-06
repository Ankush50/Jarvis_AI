import webbrowser
import random
import datetime
import os
from modules.tts import speak
from modules.api_utils import get_weather, get_news
from modules.app_manager import open_application, open_website
from modules.wikipedia_utils import search_wikipedia
from modules.youtube_utils import search_youtube, play_youtube
from modules.utils import set_alarm, play_game
from modules.jokes_facts import tell_joke, daily_quote, tell_fact
from modules.conversation import ai_chat
import memory



def handle_command(command):
    if "hello" in command:
        # speak("Hello, I am JARVIS. How can I assist you today?")
        speak("Hello, I am Friday. How can I assist you today?")
    elif "my name is" in command:
        name = command.replace("my name is", "").strip()
        memory["name"] = name
        speak(f"Nice to meet you, {name}!")
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The current time is {current_time}")
    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        speak(f"Today’s date is {current_date}")
    elif "weather" in command:
        # You need to replace this with a real API key
        api_key = "e34b7e8319b74d23b04132656240612"
        city = command.replace("weather in", "").strip()
        weather = get_weather(city, api_key)
        if weather:
            speak(f"The weather in {city} is currently {
                weather['description']} with a temperature of {weather['temp']}°C.")
        else:
            speak("I'm sorry, I couldn't get the weather information.")
    elif "open google" in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Google")
    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")
    elif "search wikipedia" in command or "about" in command:
        search_wikipedia(command)
    elif "play" in command and ("song" in command or "video" in command):
        play_youtube(command)

    elif "search youtube" in command:
        search_query = command.replace("search youtube", "").strip()
        search_youtube(search_query)

    elif "exit" in command or "stop" in command:
        speak("Goodbye! Sir.")
        # Save memory data before exiting
        exit()
    elif "open" in command:
        if "website" in command or "browser" in command:
            open_website(command)
        else:
            open_application(command)

    elif "tell me a fact" in command:
        tell_fact()


    elif "set alarm for" in command:
        set_alarm(command)

    elif "news" in command or "headlines" in command:
        get_news()

    elif "tell me a joke" in command:
        tell_joke()

    elif "motivate me" in command or "daily quote" in command:
        daily_quote()
        
    elif "play game" in command:
        play_game(command)

    elif "talk to AI" in command or "chatbot" in command:
        ai_chat(command)

    else:
        speak("Sorry, I didn't catch that. Please try again.")
