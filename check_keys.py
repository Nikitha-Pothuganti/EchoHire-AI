import os
import google.generativeai as genai
from dotenv import load_dotenv

# 1. Load the .env file
load_dotenv()

# 2. Grab the keys from the environment
murf_key = os.getenv("MURF_API_KEY")
google_key = os.getenv("GOOGLE_API_KEY")

print("--- EchoHire AI: Final Key Verification ---")

# 3. Check Murf Key (Voice)
if murf_key:
    print(f"✅ Murf API Key: FOUND (Starts with {murf_key[:5]}...)")
else:
    print("❌ Murf API Key: NOT FOUND. Check .env for MURF_API_KEY")

# 4. Check Google Key (Brain)
if google_key:
    print(f"✅ Google API Key: FOUND (Starts with {google_key[:5]}...)")
    
    # Test the specific model your account supports
    try:
        genai.configure(api_key=google_key)
        
        # Updated to use your specific model name
        model = genai.GenerativeModel('gemini-3-flash-preview') 
        
        # Test a tiny generation
        response = model.generate_content("Say 'EchoHire Brain is Online'")
        print(f"✅ Google API Connection: ACTIVE ({response.text.strip()})")
        
    except Exception as e:
        print(f"❌ Google API Connection: FAILED. Error: {e}")
        print("Tip: Run the 'List Models' script to ensure gemini-3-flash-preview is correct.")
else:
    print("❌ Google API Key: NOT FOUND. Check .env for GOOGLE_API_KEY")

print("-------------------------------------------")