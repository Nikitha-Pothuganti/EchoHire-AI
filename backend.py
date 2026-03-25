#file contains thinking and speaking of the project 
import os
import pyaudio
import google.generativeai as genai
from murf import Murf
from dotenv import load_dotenv

# 1. Setup & Keys
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
murf_client = Murf(api_key=os.getenv("MURF_API_KEY"))

# Use the specific model confirmed by your 'List Models' test
gemini_model = genai.GenerativeModel('gemini-3-flash-preview')

def get_ai_response(user_input):
    # Gemini 3 Flash is smart enough to see the "Candidate for [Role]" part of the input
    prompt = (
        "You are EchoHire AI, an expert HR interviewer. "
        "Acknowledge the candidate's answer and ask a follow-up question "
        "specifically relevant to the job role mentioned in the input. "
        "Keep it professional and under 30 words."
    )
    try:
        response = gemini_model.generate_content(f"{prompt}\n\n{user_input}")
        return response.text
    except Exception as e:
        return f"Error: {e}"

def speak_with_murf(text_to_say):
    """Streams text to Murf Falcon and plays it immediately."""
    SAMPLE_RATE = 24000
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=SAMPLE_RATE, output=True)

    try:
        # FALCON model is essential for hackathon real-time speed
        audio_stream = murf_client.text_to_speech.stream(
            text=text_to_say,
            voice_id="Matthew", 
            model="FALCON",
            sample_rate=SAMPLE_RATE,
            format="PCM"
        )

        print(f"AI is speaking: {text_to_say}")
        for chunk in audio_stream:
            if chunk:
                stream.write(chunk)
    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()