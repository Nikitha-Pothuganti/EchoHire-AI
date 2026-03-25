#this file helps us to show how how the Brain , stt and Voice work together.(sample)
from stt import listen_to_user
from backend import get_ai_response, speak_with_murf

def start_interview():
    print("--- Welcome to EchoHire AI Interview ---")
    
    # Start with a greeting
    initial_greeting = "Hello! I am your AI interviewer. To start, please tell me about yourself."
    speak_with_murf(initial_greeting)
    
    # Run the loop for 3 questions
    for i in range(3):
        # 1. EAR: Listen to the user
        user_answer = listen_to_user()
        if "Error" in user_answer:
            print(user_answer)
            continue
            
        print(f"You said: {user_answer}")

        # 2. BRAIN: Get Gemini's next question
        print("Gemini is thinking...")
        ai_question = get_ai_response(user_answer)
        
        # 3. VOICE: Murf speaks the question
        speak_with_murf(ai_question)

    speak_with_murf("Thank you for the interview. We will be in touch!")
    print("--- Interview Finished ---")

if __name__ == "__main__":
    start_interview()