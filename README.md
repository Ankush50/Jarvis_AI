# JARVIS Voice Assistant

JARVIS is a Python-based voice assistant designed to assist users with tasks such as fetching weather, setting alarms, searching Wikipedia, and more.

## Features
- Voice commands for weather, news, and time updates.
- Memory management to store user preferences.
- Wikipedia integration for quick searches.
- Alarm functionality.
- Application and website management.

## Setup

### Prerequisites
- Python 3.7 or higher
- Internet connection for APIs and Wikipedia searches

### Installation
1. Clone the repository:
2. Install dependencies:

3. Add your API keys in `resources/config.json`.

### Running JARVIS
To start the assistant, run:


## Folder Structure
jarvis/ ├── jarvis.py # Main entry point ├── modules/ # Modular functionalities │ ├── memory.py # Memory management │ ├── tts.py # Text-to-speech │ ├── stt.py # Speech-to-text │ ├── api_utils.py # API interactions │ ├── app_manager.py # App and website management │ ├── conversation.py # Chat and conversation logic │ ├── alarm.py # Alarm functionalities │ └── wikipedia_utils.py # Wikipedia search functions ├── resources/ # Resources folder │ ├── app_mapping.json # Application mappings │ ├── memory.json # Persistent memory storage │ └── config.json # API keys and configurations ├── requirements.txt # Python dependencies └── README.md # Project setup instructions


### Future Enhancements
- Add support for multi-language voice recognition.
- Implement advanced machine learning features for natural conversation.
- Expand integrations with third-party services.

## License
MIT License. See `LICENSE` file for details.
