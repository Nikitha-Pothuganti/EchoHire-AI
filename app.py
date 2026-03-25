import streamlit as st
import time
from backend import get_ai_response, speak_with_murf
from stt import listen_to_user

# --- PAGE CONFIG ---
st.set_page_config(page_title="EchoHire AI", page_icon="🎙️", layout="wide")

# --- ENHANCED CSS FOR A PREMIUM LOOK ---
st.markdown("""
    <style>
    /* Gradient Background for the whole app */
    .stApp {
        background: radial-gradient(circle at top right, #1e293b, #0f172a);
    }
    
    /* Title Styling */
    .main-title {
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: 800;
        background: -webkit-linear-gradient(#58a6ff, #2f81f7);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3.5rem;
        margin-bottom: 0px;
    }
    
    /* Quotation Styling */
    .quote-text {
        font-style: italic;
        color: #8b949e;
        font-size: 1.1rem;
        border-left: 3px solid #2f81f7;
        padding-left: 15px;
        margin: 10px 0 30px 0;
    }

    /* Card Styling */
    .glass-card {
        background: rgba(22, 27, 34, 0.7);
        padding: 25px;
        border-radius: 20px;
        border: 1px solid rgba(48, 54, 61, 0.8);
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
        margin-bottom: 20px;
    }
    
    /* Button Hover Effects */
    .stButton>button {
        transition: all 0.3s ease;
        border-radius: 12px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(47, 129, 247, 0.4);
    }
    </style>
    """, unsafe_allow_html=True)

# --- SESSION STATE ---
if 'logged_in' not in st.session_state: st.session_state.logged_in = False
if 'user_name' not in st.session_state: st.session_state.user_name = ""

# --- LOGIN / SETUP PAGE ---
def login_page():
    # Hero Section
    st.markdown('<h1 class="main-title">EchoHire</h1>', unsafe_allow_html=True)
    st.markdown('<p class="quote-text">"The best way to predict the future is to create it. Let’s start with your voice."</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1.5, 1])
    
    with col1:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.write("### ✨ Prepare for your Dream Role")
        st.write("Our AI analyzes your tone, content, and confidence in real-time.")
        
        name = st.text_input("Enter your Full Name", placeholder="e.g. Nikitha Pothuganti")
        role = st.selectbox("Which role are you interviewing for?", 
                           ["Software Engineer", "Data Scientist", "Product Manager", "UX Designer"])
        
        if st.button("Proceed to Interview Room →"):
            if name:
                st.session_state.user_name = name
                st.session_state.job_role = role
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.warning("Please let us know your name before we begin!")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.write("### 🤝 Quick Connect")
        st.button("Continue with Google 🌐")
        st.write("---")
        st.write("💡 **Hackathon Tip:** Make sure your mic is clear for better STT accuracy.")
        st.markdown('</div>', unsafe_allow_html=True)

# --- DASHBOARD ---
def dashboard():
    st.title(f"Ready, {st.session_state.user_name}?")
    st.write(f"Conducting interview for: **{st.session_state.job_role}**")
    # ... (Keep the rest of your dashboard logic here)

# Navigation
if not st.session_state.logged_in:
    login_page()
else:
    dashboard()