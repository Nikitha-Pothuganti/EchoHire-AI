import streamlit as st
import time
from backend import get_ai_response, speak_with_murf
from stt import listen_to_user

# --- PAGE CONFIG ---
st.set_page_config(page_title="EchoHire AI", page_icon="🎙️", layout="wide")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button { width: 100%; border-radius: 20px; height: 3em; background-color: #2e7af1; color: white; border: none; }
    .interview-card { background-color: #161b22; padding: 20px; border-radius: 15px; border: 1px solid #30363d; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- SESSION STATE ---
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'interview_started' not in st.session_state:
    st.session_state.interview_started = False
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'user_name' not in st.session_state:
    st.session_state.user_name = ""
if 'job_role' not in st.session_state:
    st.session_state.job_role = ""

# --- LOGIN & SETUP PAGE ---
def login_page():
    st.title("🎙️ EchoHire")
    st.subheader("Personalized AI Interview Prep")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="interview-card">', unsafe_allow_html=True)
        st.write("### 1. Identify Yourself")
        name_input = st.text_input("Enter your Full Name", placeholder="e.g. Nikitha Pothuganti")
        
        st.write("### 2. Select Targeted Role")
        role_input = st.selectbox("Which role are you interviewing for?", [
            "Software Engineer",
            "Data Scientist",
            "Product Manager",
            "Cybersecurity Analyst",
            "UX Designer",
            "HR Specialist"
        ])
        
        if st.button("Proceed to Interview Room"):
            if name_input:
                st.session_state.user_name = name_input
                st.session_state.job_role = role_input
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("Please enter your name to continue.")
        
        st.write("---")
        if st.button("Continue with Google 🌐"):
            st.session_state.user_name = "Guest Candidate"
            st.session_state.job_role = "General Associate"
            st.session_state.logged_in = True
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

# --- MAIN INTERVIEW DASHBOARD ---
def dashboard():
    st.sidebar.title("EchoHire AI")
    st.sidebar.write(f"**Candidate:** {st.session_state.user_name}")
    st.sidebar.write(f"**Target Role:** {st.session_state.job_role}")
    
    if st.sidebar.button("Exit Session"):
        st.session_state.logged_in = False
        st.session_state.interview_started = False
        st.session_state.chat_history = []
        st.rerun()

    st.title(f"Live Interview: {st.session_state.job_role}")
    
    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown('<div class="interview-card">', unsafe_allow_html=True)
        st.image("https://cdn-icons-png.flaticon.com/512/4112/4112232.png", width=100)
        st.write(f"### {st.session_state.user_name}")
        st.write(f"**Current Path:** {st.session_state.job_role}")
        st.markdown('</div>', unsafe_allow_html=True)

        if not st.session_state.interview_started:
            if st.button("Start Interview"):
                st.session_state.interview_started = True
                greeting = f"Hello {st.session_state.user_name}. Welcome to your interview for the {st.session_state.job_role} position. To begin, please tell me why you are interested in this role."
                st.session_state.chat_history.append({"role": "AI", "text": greeting})
                speak_with_murf(greeting)
                st.rerun()

    with col2:
        if st.session_state.interview_started:
            st.write("### Conversation Transcript")
            
            # Action Buttons
            if st.button("🎤 Push to Talk"):
                user_text = listen_to_user()
                st.session_state.chat_history.append({"role": "User", "text": user_text})
                
                with st.spinner(f"Gemini is analyzing your skills as a {st.session_state.job_role}..."):
                    # Pass the role to the backend to make Gemini smarter
                    ai_response = get_ai_response(f"Candidate for {st.session_state.job_role} says: {user_text}")
                    st.session_state.chat_history.append({"role": "AI", "text": ai_response})
                    speak_with_murf(ai_response)
                    st.rerun()

            # Display Chat History
            for message in reversed(st.session_state.chat_history):
                if message["role"] == "AI":
                    st.info(f"🤖 **Interviewer:** {message['text']}")
                else:
                    st.success(f"👤 **{st.session_state.user_name}:** {message['text']}")
        else:
            st.warning("Click 'Start Interview' on the left to begin.")

# --- APP NAVIGATION ---
if not st.session_state.logged_in:
    login_page()
else:
    dashboard()