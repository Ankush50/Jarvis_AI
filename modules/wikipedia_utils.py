import wikipediaapi
from modules.tts import speak

def search_wikipedia(command):
    # Specify a user agent
    wiki = wikipediaapi.Wikipedia(
        language="en",
        extract_format=wikipediaapi.ExtractFormat.WIKI,
        user_agent="JARVIS Voice Assistant (https://yourwebsite.com)"
    )

    topic = command.replace("search wikipedia for", "").strip()
    page = wiki.page(topic)

    if page.exists():
        summary = page.summary[:400]
        speak(f"According to Wikipedia, {summary}")
    else:
        speak("Sorry, I could not find information on that topic.")
