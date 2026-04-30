import streamlit as st
import sys
import os

# Helps Streamlit find your folders
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

# Set Page Look
st.set_page_config(page_title="H-AIBuddy: Leadership Core", layout="wide")

# --- ROBOT HEADER ---
st.image("https://giphy.com", width=150)
st.title("🤖 H-AIBuddy: Intelligence Guardian")

# --- SIDEBAR: INTERVIEW ---
with st.sidebar:
    st.header("👤 Profile Connection")
    name = st.text_input("Name:", placeholder="Enter your name...")
    is_mother = st.radio("Are you a mother?", ["Select...", "Yes", "No"])
    
    if is_mother == "Yes" and name:
        c_age_input = st.text_input("Child's Age (e.g., 2 or 19)")
        if st.button("Connect to Guardian"):
            st.session_state.connected = True
            st.balloons()

# --- MAIN DASHBOARD ---
if st.session_state.get('connected'):
    # 1. Leadership Slide (Visual Result like your image)
    st.markdown(f"""
    <div style="background-color:#ffffff; padding:40px; border-radius:15px; border: 2px solid #E0E0E0; box-shadow: 5px 5px 15px rgba(0,0,0,0.05);">
        <p style="color:#4CAF50; font-weight:bold; margin-bottom:0;">💠 Leadership Core</p>
        <h1 style="color:#1E3A8A; font-size:60px; margin-top:0;">DATA ANALYTICS</h1>
        <h3 style="color:#FFC107;">Ethics and Bias in Data Interpretation</h3>
        <hr>
        <p style="font-size:20px; color:#555;"><b>Guardian Notes for {name}:</b></p>
        <ul style="color:#555; font-size:18px;">
            <li>Science and Physics are the foundation of future leadership.</li>
            <li>We are currently monitoring development for child age: {c_age_input}</li>
            <li>Subject modules available: Math, Science, English, Deutsch.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # 2. Age-Specific Recommendations
    st.write("---")
    try:
        age = int(''.join(filter(str.isdigit, c_age_input)))
    except:
        age = 0

    if age < 5:
        st.info("👶 **Early Development Plan:** I recommend starting with 'Language Play' in English and Deutsch.")
    elif age >= 18:
        st.warning("🎓 **Advanced Career Path:** I have prepared a Mastery Track for Science and Physics for your adult child.")
    else:
        st.success("📚 **Core Student Path:** Standard modules for Math and Science are ready.")

    # 3. Download Section
    st.download_button("📥 Download This Slide as Notes", 
                     data=f"H-AIBuddy Lesson for {name}\nChild Age: {c_age_input}\nModule: Leadership Data Analytics",
                     file_name="H_AIBuddy_Lesson.txt")
else:
    st.warning("Please complete your profile in the sidebar to view the Leadership Core slides.")
