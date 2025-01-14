import os
import sys
from PyQt5.QtWidgets import QApplication
from GUI import JarvisApp  # Assuming you have a `gui.py` with `JarvisApp` class
from modules.tts import speak
from modules.stt import listen
from modules.conversation import engage_conversation
from modules.conversation import chatting
from modules.command_handler import handle_command
from modules.translation import translate_text
import memory

def main_cli():
    """
    Main CLI/voice-based function for JARVIS.
    """
    memory.load_memory()  # Load memory data when the program starts
    user_name = memory.memory.get("user_name", "User")  # Default to "User" if not found
    
    speak(f"...Hello Boss, {user_name}. Friday is Online. How can I make your day good?")
    
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
                    speak("Say 'Switch Mode' to switch to text mode.")
                    if command and "switch" in command.lower():
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

    elif "chat" in command:
        engage_conversation(command)
        
    elif "talk" in command:
        chatting(command)

    elif "my name is" in command:
        new_name = command.split("my name is")[-1].strip()
        memory.memory["user_name"] = new_name
        memory.save_memory()  # Save updated memory to file
        speak(f"Got it! I’ll remember your name as {new_name}.")
    else:
        handle_command(command)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "gui":
        # Launch GUI mode
        app = QApplication([])
        jarvis_app = JarvisApp()
        jarvis_app.show()
        app.exec_()
    else:
        # Launch CLI/voice mode
        main_cli()
