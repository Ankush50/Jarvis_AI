import json
import os

# Memory dictionary
memory = {}

def save_memory():
    with open("memory.json", "w") as file:
        json.dump(memory, file)

def load_memory():
    global memory
    try:
        with open("memory.json", "r") as file:
            content = file.read().strip()
            memory = json.loads(content) if content else {}
    except (FileNotFoundError, json.JSONDecodeError):
        memory = {}
