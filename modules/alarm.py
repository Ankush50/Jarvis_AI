import datetime
import threading
from modules.tts import speak

def set_alarm(command):
    try:
        time_str = command.replace("set alarm for", "").strip()
        alarm_time = datetime.datetime.strptime(time_str, "%H:%M").time()
        speak(f"Alarm set for {alarm_time.strftime('%I:%M %p')}.")

        def alarm_ring():
            while True:
                now = datetime.datetime.now().time()
                if now.hour == alarm_time.hour and now.minute == alarm_time.minute:
                    speak("Alarm ringing! Time to wake up.")
                    break

        threading.Thread(target=alarm_ring, daemon=True).start()
    except Exception as e:
        speak("I couldn't understand the time. Please use the format HH:MM.")
