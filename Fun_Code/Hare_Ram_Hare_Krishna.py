# The library which are required
# pip install SpeechRecognition 
# pip install pyttsx3
# pip install pyaudio

# import speech_recognition as sr
# import pyttsx3
# import time

# # Initialize the speech engine for text-to-speech

# engine = pyttsx3.init()

# def 


import speech_recognition as sr
import pyttsx3
import time

# Initialize the speech engine for text-to-speech
engine = pyttsx3.init()

def chant_hare_krishna():
    while True:
        # Continue chanting "Hare Ram Hare Krishna"
        engine.say("Hare Ram Hare Krishna")
        engine.runAndWait()
        time.sleep(1)  # Chant every second

def listen_for_silence():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening for the user's chant... (say something to stop chanting)")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        try:
            audio = recognizer.listen(source, timeout=5)  # Listen for 5 seconds or until speech is detected
            print(audio)
            print("You are chanting0!")
            text = recognizer.recognize_google(audio)
            print("You are chanting!", text)
            return True  # Chanting detected
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        except sr.WaitTimeoutError:
            print("No input detected, continue chanting.")
            return False  # No input detected (silence)

def main():
    print("Starting Hare Ram Hare Krishna Chanting...")
    # chant_hare_krishna()  # Start chanting
    
    while True:
        if not listen_for_silence():  # If no chanting is detected, prompt user to chant
            engine.say("Start chanting Hare Ram Hare Krishna.")
            engine.runAndWait()
            time.sleep(2)  # Wait before continuing the chant

if __name__ == "__main__":
    main()
