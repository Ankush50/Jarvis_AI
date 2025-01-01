import os
import webbrowser
import json
import requests
from modules.tts import speak


APP_MAPPING_FILE = os.path.join(os.path.dirname(__file__), '..', 'config', 'app_mapping.json')

def load_app_mapping():
    try:
        with open(APP_MAPPING_FILE, "r") as file:
            return json.load(file)
    except Exception as e:
        print(f"Error loading app mapping: {e}")
        return {}

app_mapping = load_app_mapping()


def open_application(command):
    # Check if the command includes an application name
    for app_name, app_path in app_mapping.items():
        if app_name in command:
            try:
                os.startfile(app_path)  # Open the application
                speak(f"Opening {app_name}.")
                return
            except Exception as e:
                print(f"Error opening {app_name}: {e}")
                return
    # Provide feedback if no application is found
    speak("Sorry, I could not find that application.")

def open_website(command):
    # Extract the website name from the command
    website_name = command.replace("open ", "").strip()
    if "on browser" in website_name:
        website_name = website_name.replace("on browser", "").strip()

    # Replace spaces with '.' for subdomains
    website_name = website_name.replace(" ", ".")

    # List of common domain suffixes to try
    common_domains = ['.com', '.org', '.net',
                      '.edu', '.gov', '.co.in', '.io', '.me']

    # Attempt to find the best URL
    found_url = False
    for domain in common_domains:
        test_url = f"https://{website_name}{domain}"
        try:
            # Perform a request to see if the URL is valid
            response = requests.head(test_url, allow_redirects=True)
            if response.status_code == 200:
                webbrowser.open(test_url)  # Open the valid website
                speak(f"Opening {test_url}.")
                found_url = True
                break
        except requests.RequestException:
            continue  # Move on to the next domain if the request fails

    if not found_url:
        # If no valid URL was found, search on Google
        search_url = f"https://www.google.com/search?q={website_name}"
        webbrowser.open(search_url)
        speak(f"Could not find a specific website. Searching for {
              website_name} on Google.")