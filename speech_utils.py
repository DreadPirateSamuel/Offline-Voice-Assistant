import speech_recognition as sr
import pyttsx3
from gtts import gTTS
from playsound import playsound
import os
import uuid

recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Configure voice properties
engine.setProperty('rate', 160)  # Speed
engine.setProperty('volume', 0.9)  # Volume

# Select voice (you can change index for different voices)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Use voices[1].id for female on many systems

def speak(text):
    """Speak using gTTS and playsound (reliable cross-platform)."""
    print(f"[Assistant says]: {text}")
    try:
        filename = f"temp_{uuid.uuid4().hex}.mp3"
        tts = gTTS(text=text, lang='en')
        tts.save(filename)
        playsound(filename)
        os.remove(filename)
    except Exception as e:
        print(f"[TTS ERROR]: {e}")


def listen():
    """Listen to the microphone and return recognized speech."""
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        try:
            print("Listening for a command...")
            audio = recognizer.listen(source, timeout=5)
            return recognizer.recognize_google(audio)
        except sr.WaitTimeoutError:
            return None
        except sr.UnknownValueError:
            return None
        except sr.RequestError:
            return None

def detect_hotword():
    """Detect the hotword 'hey assistant' to activate the assistant."""
    print("Waiting for hotword 'hey assistant'...")
    with sr.Microphone() as source:
        try:
            audio = recognizer.listen(source, timeout=6)
            phrase = recognizer.recognize_google(audio).lower()
            return 'hey assistant' in phrase
        except:
            return False
