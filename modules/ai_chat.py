import openai
import pyttsx3
import os


# Set up OpenAI API key securely
# openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize TTS engine
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def ai_chat(command):
    """Chat with OpenAI API and speak the response."""
    try:
        openai.api_key = "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"
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
