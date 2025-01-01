import speech_recognition as sr

recognizer = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        print("Listening for command...")
        recognizer.adjust_for_ambient_noise(source, duration=1)  # Adapt to ambient noise
        try:
            audio = recognizer.listen(source, timeout=5)  # Add timeout to prevent indefinite listening
            command = recognizer.recognize_google(audio, language='en-IN').lower()
            print(f"Recognized Command: {command}")  # Debug: Print recognized command
            return command
        except sr.UnknownValueError:
            print("Could not understand the command.")  # Debug: Log error
            return None
        except sr.RequestError as e:
            print(f"Speech recognition error: {e}")  # Debug: Log error
            return None
        except Exception as e:
            print(f"Unexpected error: {e}")  # Debug: Log unexpected issues
            return None
