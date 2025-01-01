import requests
from modules.tts import speak

def get_weather(city, api_key):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={
            city}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()
        if data["cod"] == 200:
            main = data["main"]
            weather = data["weather"][0]
            return {"temp": main["temp"], "description": weather["description"]}
        else:
            return None
    except Exception as e:
        print(f"Error getting weather: {e}")
        return None

def get_news():
    api_key = "80ff8174d555467abbba5ec79809ecc0"  # Replace with your NewsAPI key
    url = f"https://newsdata.io/api/1/news?apikey=pub_59415a2176d471eb3f4ecb18387abb22c1638&q=india "
    try:
        response = requests.get(url).json()
        articles = response.get("articles", [])[:5]  # Fetch top 5 articles
        if articles:
            speak("Here are the top news headlines:")
            for article in articles:
                # Speak out the news headline
                speak(article["title"])

                # Print the details for debugging or logging
                print(f"Title: {article['title']}")
                print(f"Source: {article['source']['name']}")
                print(f"URL: {article['url']}")
        else:
            speak("I couldn't find any news updates right now.")
    except Exception as e:
        print(f"Error fetching news: {e}")  # Log the error for debugging
        speak("I encountered an error fetching the news.")


    # api_key = "8df2794fcab292e33b7f615e59cad51b"
        # api_key = "pub_59415a2176d471eb3f4ecb18387abb22c1638"