from commands import execute_command
from speech_utils import listen, speak, detect_hotword

def main():
    speak("Assistant ready. Say 'hey assistant' to begin.")
    
    while True:
        if detect_hotword():
            speak("Listening...")
            command = listen()
            if command:
                print(f"You said: {command}")
                if 'exit' in command or 'quit' in command:
                    speak("Goodbye!")
                    break
                execute_command(command)
            else:
                speak("Sorry, I didn’t catch that. Please try again.")

if __name__ == "__main__":
    main()

