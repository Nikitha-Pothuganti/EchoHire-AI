import speech_recognition as sr

def listen_to_user():
    """Listens to the mic and returns the text transcript."""
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("\n🎤 Listening... Speak your answer now.")
        # Adjust for ambient noise (fans, typing, etc.)
        recognizer.adjust_for_ambient_noise(source, duration=1)
        
        try:
            # Captures the audio
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            print("⏳ Processing your voice...")
            
            # Converts audio to text using Google's free web API
            text = recognizer.recognize_google(audio)
            return text
            
        except sr.WaitTimeoutError:
            return "Error: I didn't hear anything. Please try again."
        except sr.UnknownValueError:
            return "Error: I couldn't understand the audio. Speak more clearly."
        except sr.RequestError:
            return "Error: Speech Service is down. Check your internet."