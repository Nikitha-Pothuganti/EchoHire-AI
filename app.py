# import streamlit as st
# import time
# from backend import get_ai_response, speak_with_murf
# from stt import listen_to_user

# # --- PAGE CONFIG ---
# st.set_page_config(page_title="EchoHire AI", page_icon="🎙️", layout="wide")

# # --- ENHANCED CSS FOR A PREMIUM LOOK ---
# st.markdown("""
#     <style>
#     /* Gradient Background for the whole app */
#     .stApp {
#         background: radial-gradient(circle at top right, #1e293b, #0f172a);
#     }
    
#     /* Title Styling */
#     .main-title {
#         font-family: 'Helvetica Neue', sans-serif;
#         font-weight: 800;
#         background: -webkit-linear-gradient(#58a6ff, #2f81f7);
#         -webkit-background-clip: text;
#         -webkit-text-fill-color: transparent;
#         font-size: 3.5rem;
#         margin-bottom: 0px;
#     }
    
#     /* Quotation Styling */
#     .quote-text {
#         font-style: italic;
#         color: #8b949e;
#         font-size: 1.1rem;
#         border-left: 3px solid #2f81f7;
#         padding-left: 15px;
#         margin: 10px 0 30px 0;
#     }

#     /* Card Styling */
#     .glass-card {
#         background: rgba(22, 27, 34, 0.7);
#         padding: 25px;
#         border-radius: 20px;
#         border: 1px solid rgba(48, 54, 61, 0.8);
#         box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
#         margin-bottom: 20px;
#     }
    
#     /* Button Hover Effects */
#     .stButton>button {
#         transition: all 0.3s ease;
#         border-radius: 12px;
#         font-weight: 600;
#         text-transform: uppercase;
#         letter-spacing: 1px;
#     }
#     .stButton>button:hover {
#         transform: translateY(-2px);
#         box-shadow: 0 5px 15px rgba(47, 129, 247, 0.4);
#     }
#     </style>
#     """, unsafe_allow_html=True)

# # --- SESSION STATE ---
# if 'logged_in' not in st.session_state: st.session_state.logged_in = False
# if 'user_name' not in st.session_state: st.session_state.user_name = ""

# # --- LOGIN / SETUP PAGE ---
# def login_page():
#     # Hero Section
#     st.markdown('<h1 class="main-title">EchoHire</h1>', unsafe_allow_html=True)
#     st.markdown('<p class="quote-text">"The best way to predict the future is to create it. Let’s start with your voice."</p>', unsafe_allow_html=True)
    
#     col1, col2 = st.columns([1.5, 1])
    
#     with col1:
#         st.markdown('<div class="glass-card">', unsafe_allow_html=True)
#         st.write("### ✨ Prepare for your Dream Role")
#         st.write("Our AI analyzes your tone, content, and confidence in real-time.")
        
#         name = st.text_input("Enter your Full Name", placeholder="e.g. Nikitha Pothuganti")
#         role = st.selectbox("Which role are you interviewing for?", 
#                            ["Software Engineer", "Data Scientist", "Product Manager", "UX Designer"])
        
#         if st.button("Proceed to Interview Room →"):
#             if name:
#                 st.session_state.user_name = name
#                 st.session_state.job_role = role
#                 st.session_state.logged_in = True
#                 st.rerun()
#             else:
#                 st.warning("Please let us know your name before we begin!")
#         st.markdown('</div>', unsafe_allow_html=True)

#     with col2:
#         st.markdown('<div class="glass-card">', unsafe_allow_html=True)
#         st.write("### 🤝 Quick Connect")
#         st.button("Continue with Google 🌐")
#         st.write("---")
#         st.write("💡 **Hackathon Tip:** Make sure your mic is clear for better STT accuracy.")
#         st.markdown('</div>', unsafe_allow_html=True)

# # --- DASHBOARD ---
# def dashboard():
#     st.title(f"Ready, {st.session_state.user_name}?")
#     st.write(f"Conducting interview for: **{st.session_state.job_role}**")
#     # ... (Keep the rest of your dashboard logic here)

# # Navigation
# if not st.session_state.logged_in:
#     login_page()
# else:
#     dashboard()


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