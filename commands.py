import os
import webbrowser
from speech_utils import speak
import datetime
import subprocess
import wikipedia
import pyjokes
import random
import time
import platform
import shutil
import smtplib
from email.message import EmailMessage
import string

# Helper function for unit conversion
unit_map = {
    'kilometers to miles': lambda x: x * 0.621371,
    'miles to kilometers': lambda x: x * 1.60934,
    'celsius to fahrenheit': lambda x: (x * 9/5) + 32,
    'fahrenheit to celsius': lambda x: (x - 32) * 5/9
}

def execute_command(command):
    command = command.lower().translate(str.maketrans('', '', string.punctuation)).strip()
    print(f"DEBUG: Normalized command -> {command}")

    # === General Utilities (Moved Up for Testing) ===
    if 'what is the date' in command or ('date' in command and 'what' in command):
        today = datetime.date.today().strftime('%A, %B %d, %Y')
        speak(f"Today is {today}")
    elif 'what time is it' in command or ('time' in command and 'what' in command):
        now = datetime.datetime.now().strftime('%I:%M %p')
        speak(f"The time is {now}")
    elif 'tell me a joke' in command:
        joke = pyjokes.get_joke()
        speak(joke)

    # === File Management ===
    elif 'copy file' in command:
        speak("Copying file...")
        try:
            shutil.copy("test.txt", "backup_test.txt")
            speak("File copied successfully")
        except Exception as e:
            speak(f"Failed to copy file: {str(e)}")

    elif 'delete file' in command:
        try:
            os.remove("test.txt")
            speak("File deleted successfully")
        except Exception as e:
            speak(f"Error deleting file: {str(e)}")

    # === Unit Conversion ===
    elif 'unit conversion' in command:
        for key in unit_map:
            if key in command:
                number = [float(s) for s in command.split() if s.replace('.', '', 1).isdigit()]
                if number:
                    result = unit_map[key](number[0])
                    speak(f"{number[0]} {key} is {round(result, 2)}")
                    return
        speak("Could not complete the conversion")

    # === Email ===
    elif 'send email' in command:
        try:
            msg = EmailMessage()
            msg.set_content("This is a test email from your assistant.")
            msg["Subject"] = "Voice Assistant Test"
            msg["From"] = "youremail@example.com"
            msg["To"] = "recipient@example.com"
            server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            server.login("youremail@example.com", "yourpassword")
            server.send_message(msg)
            server.quit()
            speak("Email sent successfully")
        except:
            speak("Failed to send email")

    # === VPN Control ===
    elif 'start vpn' in command:
        if 'germany' in command:
            os.system("tunnelbear connect DE")
            speak("Connecting to VPN in Germany")
        elif 'canada' in command:
            os.system("tunnelbear connect CA")
            speak("Connecting to VPN in Canada")
        elif 'united states' in command:
            os.system("tunnelbear connect US")
            speak("Connecting to VPN in the United States")
        else:
            speak("Please specify a supported country for VPN connection")

    # === Dev/Terminal Commands (expanded set) ===
    elif 'open vscode' in command:
        subprocess.Popen(["code"])
        speak("Opening VS Code")
    elif 'open terminal' in command:
        subprocess.Popen(["wt.exe"])
        speak("Opening Terminal")
    elif 'open powershell' in command:
        subprocess.Popen(["powershell.exe"])
        speak("Opening PowerShell")
    elif 'open command prompt' in command:
        subprocess.Popen(["cmd.exe"])
        speak("Opening Command Prompt")
    elif 'open git bash' in command:
        subprocess.Popen(["C:\\Program Files\\Git\\git-bash.exe"])
        speak("Opening Git Bash")
    elif 'git status' in command:
        os.system("git status")
        speak("Running git status")
    elif 'git pull' in command:
        os.system("git pull")
        speak("Pulling latest changes")
    elif 'git push' in command:
        os.system("git push")
        speak("Pushing changes")
    elif 'create virtual environment' in command:
        os.system("python -m venv venv")
        speak("Virtual environment created")
    elif 'activate virtual environment' in command:
        os.system("venv\\Scripts\\activate")
        speak("Virtual environment activated")
    elif 'install requirements' in command:
        os.system("pip install -r requirements.txt")
        speak("Installing requirements")
    elif 'run tests' in command:
        os.system("pytest")
        speak("Running test suite")
    elif 'start flask' in command:
        os.system("flask run")
        speak("Starting Flask app")
    elif 'start django' in command:
        os.system("python manage.py runserver")
        speak("Starting Django app")
    elif 'run jupyter' in command:
        os.system("jupyter notebook")
        speak("Opening Jupyter Notebook")
    elif 'list files' in command:
        os.system("dir")
        speak("Listing files")
    elif 'make directory' in command:
        os.system("mkdir new_folder")
        speak("Created a new folder")
    elif 'delete directory' in command:
        os.system("rmdir /s /q new_folder")
        speak("Deleted the folder")
    elif 'clear terminal' in command:
        os.system("cls")
        speak("Terminal cleared")
    elif 'ip config' in command:
        os.system("ipconfig")
        speak("IP configuration output displayed")
    elif 'ping google' in command:
        os.system("ping www.google.com")
        speak("Pinging Google")

    # === Online Search ===
    elif 'search for' in command:
        query = command.split("search for")[-1].strip()
        webbrowser.open(f"https://www.google.com/search?q={query}")
        speak(f"Searching Google for {query}")
    elif 'wikipedia' in command:
        topic = command.replace("wikipedia", "").strip()
        try:
            summary = wikipedia.summary(topic, sentences=2)
            speak(summary)
        except:
            speak("Sorry, I couldn't find that on Wikipedia.")

    else:
        speak("Sorry, I don’t know how to do that yet.")
