import openai
import pyttsx3
import os

# Initialize TTS engine
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def ai_chat(command):
    """Chat with OpenAI API and speak the response."""
    try:
        # Set up OpenAI API key securely, you have to add you api key.
        # openai.api_key = "api-key"
        # Call OpenAI API
        response = openai.Completion.create(
            model="gpt-4o-mini",
            prompt=f"User: {command}\nAssistant:",
            max_tokens=150
        )
        # Extract response text
        answer = response.choices[0].text.strip()
        print(f"AI: {answer}")
        
        # Speak the response
        speak(answer)
    except Exception as e:
        error_message = "Sorry, I couldn't connect to the AI service."
        speak(error_message)
        print(f"Error: {e}")
