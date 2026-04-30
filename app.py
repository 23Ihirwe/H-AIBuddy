import streamlit as st
import time
from datetime import datetime

# --- 1. AI MEMORY & TIME TRACKING INITIALIZATION ---
if 'start_time' not in st.session_state:
    st.session_state.start_time = time.time()
if 'chat_memory' not in st.session_state:
    st.session_state.chat_memory = []
if 'connected' not in st.session_state:
    st.session_state.connected = False

st.set_page_config(page_title="H-AIBuddy: Professional Guardian", layout="wide")

# --- 2. VISUAL INTERFACE (Robot Presence) ---
st.image("https://giphy.com", width=150)
st.title("🤖 H-AIBuddy: Intelligence Guardian")
st.write("---")

# --- 3. THE ADAPTIVE INTERVIEW (Original Logic + Improvement) ---
with st.sidebar:
    st.header("👤 Security Connection")
    name = st.text_input("Mother's Name:")
    is_mother = st.radio("Are you a mother?", ["Select...", "Yes", "No"])
    
    if is_mother == "Yes" and name:
        permission = st.checkbox("Grant H-AIBuddy permission to interview?")
        if permission:
            career = st.text_input("Career Status")
            edu = st.text_input("Education Level")
            c_age = st.number_input("Child's Age", min_value=0, max_value=100)
            
            if st.button("Initialize Leadership Core"):
                st.session_state.connected = True
                st.balloons()

# --- 4. MAIN INTERACTION HUB ---
if st.session_state.connected:
    st.subheader(f"👋 Welcome back, {name}. How can I assist your family today?")
    
    # AI Conversation Area
    user_thought = st.text_area("Talk to me (I will adapt to your needs):", placeholder="Example: I want to focus on Math and French this week...")
    if st.button("Submit to Memory"):
        st.session_state.chat_memory.append({"time": datetime.now().strftime("%H:%M"), "note": user_thought})
        st.success("🤖 H-AIBuddy: Vision recorded. I am adapting our modules now.")

    # --- 5. THE LEARNING MODULES (Math, Science, Languages) ---
    st.write("---")
    st.header("📚 Learning Modules")
    
    tab1, tab2, tab3, tab4 = st.tabs(["🌎 Languages", "🌌 Science & Physics", "🧮 Math", "💼 Entrepreneurship"])

    with tab1:
        st.subheader("Language Specialist")
        lang = st.selectbox("Choose a language to study:", ["English", "Deutsch", "French", "Creole"])
        
        if lang == "French":
            st.image("https://unsplash.com", width=300)
            st.markdown("**Notes:** French is the language of diplomacy. *Greeting:* 'Bonjour' (Hello).")
        elif lang == "Creole":
            st.image("https://unsplash.com", width=300)
            st.markdown("**Notes:** Creole is built on phonetics and community. *Greeting:* 'Bonzour'.")
        elif lang == "Deutsch":
            st.markdown("**Notes:** German is the language of Engineering. *Greeting:* 'Guten Tag'.")
            
    with tab2:
        st.subheader("Science & Physics")
        st.image("https://unsplash.com", width=300)
        st.write("- **Physics:** Study the laws of motion (Newton's Laws).")
        st.write("- **Science:** Understanding data and evidence.")

    with tab3:
        st.subheader("Mathematics")
        st.write("- **Logic:** If A = B and B = C, then A = C.")
        st.write("- **Finance:** Managing family resources and business math.")

    with tab4:
        st.subheader("Entrepreneurship & Data")
        st.write("- **Strategy:** Identify a problem and build a solution.")
        st.write("- **Data:** Use analytics to track your success.")

    # --- 6. ANALYTICS & DOWNLOADS (The Memory) ---
    st.write("---")
    st.subheader("📊 Session Analytics")
    current_elapsed = round((time.time() - st.session_state.start_time) / 60, 2)
    st.info(f"⏱️ You have been interacting with H-AIBuddy for **{current_elapsed} minutes**.")
    
    # Download Notes
    report = f"H-AIBuddy Report for {name}\nTime Spent: {current_elapsed} mins\nNotes: {st.session_state.chat_memory}"
    st.download_button("📥 Download Lesson Notes & Progress", data=report, file_name=f"{name}_H_AIBuddy_Notes.txt")

else:
    st.warning("🤖 H-AIBuddy: Please connect your profile in the sidebar to begin our journey.")
