import os
import sys
from modules.tts import speak
from modules.stt import listen
from modules.conversation import engage_conversation
from modules.command_handler import handle_command
import memory


def main():
    memory.load_memory()  # Load memory data when the program starts
    # load_memory()  # Load memory data when the program starts
    user_name = memory.memory.get("User", "Sir")  # Default to "User" if not found
    speak(f"Hello, {user_name}. JARVIS activated. Listening for commands.")
    while True:
        command = listen()
        if command:
            if "chat" in command or "talk" in command:
                engage_conversation()
            if "my name is" in command:
                    new_name = command.split("my name is")[-1].strip()
                    memory.memory["user_name"] = new_name
                    memory.save_memory()  # Save updated memory to file
                    
            else:
                handle_command(command)



# Run the assistant
if __name__ == "__main__":
    main()
