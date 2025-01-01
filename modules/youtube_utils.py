import webbrowser
from modules.tts import speak

def search_youtube(query):
    url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
    webbrowser.open(url)
    speak(f"Searching YouTube for {query}.")

def play_youtube(command):
    search_query = command.replace("play", "").strip()
    if search_query:
        url = f"https://www.youtube.com/results?search_query={search_query}"
        webbrowser.open(url)
        speak(f"Playing {search_query} on YouTube.")
    else:
        speak("Please specify what you want to play.")
