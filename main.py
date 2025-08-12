import speech_recognition as sr
import os
import webbrowser
import subprocess
import cv2

# Set your music folder path
MUSIC_FOLDER = r"C:\Users\adiku\Downloads\music"

# Function to make Zira speak
def say(text):
    text = text.replace("'", " ")  # Prevent issues with apostrophes
    command = f'powershell -Command "Add-Type -AssemblyName System.Speech; ' \
              f'$speak = New-Object System.Speech.Synthesis.SpeechSynthesizer; ' \
              f'$speak.SelectVoice(\'Microsoft Zira Desktop\'); ' \
              f'$speak.Speak(\'{text}\')"'
    os.system(command)

apps = {
    "snapchat": r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge_proxy.exe",
    "instagram": r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge_proxy.exe",
    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "vscode": r"C:\Users\YourUsername\AppData\Local\Programs\Microsoft VS Code\Code.exe",
    "whatsapp":  r"https://web.whatsapp.com/",
    "facebook": r"https://www.facebook.com/",
    "digiicampus": r"https://nshmd.digiicampus.com/home",
    "camera": r""

}

# Function to take voice command
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
        return query.lower()
    except Exception as ex:
        print("Error:", ex)
        return ""

# Load songs from the music folder
def loadSongs():
    songs = {}
    for file in os.listdir(MUSIC_FOLDER):
        if file.endswith(".mp3"):
            name = os.path.splitext(file)[0].lower()
            path = os.path.join(MUSIC_FOLDER, file)
            songs[name] = path
    return songs

# Main program
if __name__ == '__main__':
    print('Zira starting...')
    say("Hello, I am Zira, your assistant.")

    sites = [
        ["youtube", "https://www.youtube.com"],
        ["google", "https://www.google.com"]
    ]

    songs = loadSongs()

    try:
        while True:
            print("\nWaiting for wake word: 'anu'...")
            wake = takeCommand()
            if "anu" in wake:
                say("Hello Sir, how can I help you?")
                query = takeCommand()

                # Open websites
                for site in sites:
                    if f"open {site[0]}" in query:
                        say(f"Opening {site[0]}, sir...")
                        webbrowser.open(site[1])
                        break

                # Play music
                if "play" in query:
                    found = False
                    for song_name in songs:
                        if song_name in query:
                            say(f"Playing {song_name}")
                            os.startfile(songs[song_name])
                            found = True
                            break

                if "open" in query:
                    for app in apps:
                        if app in query:
                            say(f"Opening {app}")
                            os.startfile(apps[app])
                            break






    except KeyboardInterrupt:
        print("\nZira stopped.")
        say("Goodbye sir!")
