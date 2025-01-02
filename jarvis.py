import os
import sys
from modules.tts import speak
from modules.stt import listen
from modules.conversation import engage_conversation
from modules.command_handler import handle_command
from modules.translation import translate_text
import memory


def main():
    memory.load_memory()  # Load memory data when the program starts
    user_name = memory.memory.get("user_name", "User")  # Default to "User" if not found
    speak(f"...Hello, {user_name}. JARVIS activated. You can use either voice or text commands. How can I assist you?")

    while True:
        speak("Would you like to use voice or text input? Say 'voice' or 'text'.")
        mode = listen()
        if mode:
            mode = mode.lower()
            if "voice" in mode:
                speak("Voice mode activated. Listening for commands.")
                while True:
                    command = listen()
                    if command:
                        process_command(command)
                    else:
                        speak("I didn't catch that. Please try again.")
                    speak("Say 'exit voice' to switch to text mode.")
                    if command and "exit voice" in command:
                        break

            elif "text" in mode:
                speak("Text mode activated. Type your commands below.")
                while True:
                    command = input("You: ")
                    if command.lower() in ["exit text", "quit"]:
                        speak("Exiting text mode. Returning to mode selection.")
                        break
                    process_command(command)
            else:
                speak("I didn't understand your choice. Please say 'voice' or 'text'.")
        else:
            speak("I didn't catch that. Please say 'voice' or 'text'.")


def process_command(command):
    """
    Processes the user's command for both voice and text input modes.
    """
    if "translate" in command:
        speak("What would you like me to translate?")
        text_to_translate = listen() if command.lower().startswith("voice") else input("Enter text to translate: ")
        speak("Which language should I translate to?")
        target_language = listen() if command.lower().startswith("voice") else input("Enter target language: ")
        translated_text = translate_text(text_to_translate, target_language)
        speak(f"The translation is: {translated_text}")
        print(f"Translated text: {translated_text}")

    elif "chat" in command or "talk" in command:
        engage_conversation()

    elif "my name is" in command:
        new_name = command.split("my name is")[-1].strip()
        memory.memory["user_name"] = new_name
        memory.save_memory()  # Save updated memory to file
        speak(f"Got it! I’ll remember your name as {new_name}.")
    else:
        handle_command(command)


# Run the assistant
if __name__ == "__main__":
    main()
