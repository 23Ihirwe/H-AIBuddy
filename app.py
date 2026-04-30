import streamlit as st
import pyttsx3
import sys
import os

# --- SETUP VOICE ENGINE ---
def robot_speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150) # Set speed
    engine.say(text)
    engine.runAndWait()

st.set_page_config(page_title="H-AIBuddy Guardian", layout="centered")

# Robot Visual
st.image("https://giphy.com", width=250)
st.title("🤖 H-AIBuddy")

# --- PHASE 1: Personal Info ---
name = st.text_input("🤖 Name:")
role = st.radio("Are you a mother?", ["Select...", "Yes", "No"])

if role == "Yes" and name:
    st.info(f"Welcome, {name}. Let's secure your family's profile.")
    
    col1, col2 = st.columns(2)
    with col1:
        career = st.text_input("Career Status")
        c_age_input = st.text_input("Child's Age (e.g. 2 or 19)")
    with col2:
        emp = st.selectbox("Employed?", ["Yes", "No"])

    if st.button("Connect with Guardian"):
        st.session_state.connected = True
        robot_speak(f"Connection established. Welcome {name}.")

    if st.session_state.get('connected'):
        st.success("✅ Information secured.")
        try:
            age_num = int(''.join(filter(str.isdigit, c_age_input)))
        except:
            age_num = 0

        st.write("---")
        
        # --- PHASE 2: Mother's Willingness First ---
        st.subheader(f"👩‍🏫 Mother's Learning Path")
        m_learn = st.radio(f"🤖 {name}, are YOU willing to learn our modules (Science, Physics, Math, Languages)?", ["Select...", "Yes", "No"])
        
        if m_learn == "Yes":
            st.write("🤖 **H-AIBuddy:** Excellent! A leading mother creates a leading family.")
            if st.button("Listen to Message"):
                robot_speak("Excellent choice. A leading mother creates a leading family.")

        # --- PHASE 3: Child's Specific Path ---
        st.write("---")
        st.subheader(f"👶 Child's Path (Age: {age_num})")
        
        if age_num < 5:
            st.write("🤖 **H-AIBuddy Recommendation:** At this young age, I recommend focusing on **Language (English/Deutsch) Basics** and **Number Play**.")
            st.checkbox("Enable Early Language Development")
            st.checkbox("Enable Math logic for Toddlers")
        
        elif age_num >= 18:
            st.write("🤖 **H-AIBuddy:** For older children, I understand they may prefer independence. Mother, you can choose a 'Mastery Track' for them:")
            track = st.selectbox("Choose the best path for your child:", ["Select...", "Advanced Physics & Science", "Professional English/Deutsch", "Career Mathematics"])
        
        else:
            st.write("🤖 **H-AIBuddy:** They are at a prime age for learning! I can offer Science, Math, and Physics.")

        # --- PHASE 4: Slides & Notes ---
        if st.button("Generate Learning Slides & Notes"):
            st.write("---")
            st.subheader("📚 Your H-AIBuddy Lesson Pack")
            st.info("Here are your introductory slides:")
            st.markdown("""
            **Slide 1: Introduction to H-AIBuddy Systems**
            - The Guardian's role in education.
            - How Science and Language shield the mind.
            
            **Slide 2: Your Custom Path**
            - Focus: Science & Deutsch Language.
            - Goal: 15 minutes of interactive daily play.
            """)
            st.balloons()
            robot_speak("Your learning pack is ready. Let us begin!")
