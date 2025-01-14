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
    """
    Processes user commands and returns a string response or executes a task.
    """
    try:
        # Handle invalid or empty commands
        if not command or not isinstance(command, str):
            return "I'm sorry, I didn't receive a valid command."

        command = command.lower()

        if "hello" in command:
            response = "Hello! How can I assist you today?"
            speak(response)
            return response

        elif "what's your name" in command:
            response = "I am JARVIS, your personal AI assistant."
            speak(response)
            return response

        elif "my name is" in command:
            name = command.replace("my name is", "").strip()
            memory["name"] = name
            response = f"Nice to meet you, {name}!"
            speak(response)
            return response

        elif "time" in command:
            current_time = datetime.datetime.now().strftime("%H:%M")
            response = f"The current time is {current_time}."
            speak(response)
            return response

        elif "date" in command:
            current_date = datetime.datetime.now().strftime("%Y-%m-%d")
            response = f"Today's date is {current_date}."
            speak(response)
            return response

        elif "weather" in command:
            api_key = "e34b7e8319b74d23b04132656240612"  # Replace with your real API key
            city = command.replace("weather in", "").strip()
            weather = get_weather(city, api_key)
            if weather:
                response = f"The weather in {city} is currently {weather['description']} with a temperature of {weather['temp']}°C."
                speak(response)
                return response
            else:
                response = "I'm sorry, I couldn't get the weather information."
                speak(response)
                return response

        elif "open google" in command:
            webbrowser.open("https://www.google.com")
            response = "Opening Google."
            speak(response)
            return response

        elif "open youtube" in command:
            webbrowser.open("https://www.youtube.com")
            response = "Opening YouTube."
            speak(response)
            return response

        elif "search wikipedia" in command or "about" in command:
            return search_wikipedia(command)

        elif "play" in command and ("song" in command or "video" in command):
            return play_youtube(command)

        elif "search youtube" in command:
            search_query = command.replace("search youtube", "").strip()
            return search_youtube(search_query)

        elif "exit" in command or "stop" in command:
            response = "Goodbye! Have a great day!"
            speak(response)
            # Save memory or perform cleanup before exiting
            exit()

        elif "open" in command:
            if "website" in command or "browser" in command:
                return open_website(command)
            else:
                return open_application(command)

        elif "tell me a fact" in command:
            return tell_fact()

        elif "set alarm for" in command:
            return set_alarm(command)

        elif "news" in command or "headlines" in command:
            return get_news()

        elif "tell me a joke" in command:
            return tell_joke()

        elif "motivate me" in command or "daily quote" in command:
            return daily_quote()

        elif "play game" in command:
            return play_game(command)

        elif "talk to AI" in command or "chatbot" in command:
            return ai_chat(command)

        else:
            response = "I'm sorry, I didn't understand that."
            speak(response)
            return response

    except Exception as e:
        # Handle unexpected errors gracefully
        error_message = f"An error occurred: {str(e)}"
        speak(error_message)
        return error_message