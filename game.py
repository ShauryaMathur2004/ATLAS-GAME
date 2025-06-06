import streamlit as st
import pandas as pd
import random

# Load data
@st.cache_data
def load_data():
    df = pd.read_excel("worldcities.xlsx")
    cities = df['city'].dropna().str.title().unique().tolist()
    states = df['admin_name'].dropna().str.title().unique().tolist()
    countries = df['country'].dropna().str.title().unique().tolist()
    return list(set(cities + states + countries))

# Get next place starting with last letter
def get_next_place(user_input, used, places):
    last_letter = user_input.strip()[-1].lower()
    for place in places:
        if place.lower().startswith(last_letter) and place not in used:
            return place
    return None

# Initialize session state
if 'history' not in st.session_state:
    st.session_state.history = []
if 'used' not in st.session_state:
    st.session_state.used = []

st.title("🌍 ATLAS")
st.write("Enter any **city, state, or country**, and I'll respond with one starting with the last letter of yours!")

places = load_data()

user_input = st.text_input("Your Turn", "")

if st.button("Submit") or user_input:
    user_input = user_input.strip().title()

    if user_input not in places:
        st.warning("⚠️ Not found in known place names. Try another.")
    elif user_input in st.session_state.used:
        st.warning("♻️ This place was already used. Try a new one.")
    else:
        st.session_state.history.append(("You", user_input))
        st.session_state.used.append(user_input)

        ai_choice = get_next_place(user_input, st.session_state.used, places)
        if ai_choice:
            st.session_state.history.append(("Bot", ai_choice))
            st.session_state.used.append(ai_choice)
        else:
            st.session_state.history.append(("Bot", "I couldn't think of any! You win 🎉"))

# Show history
st.markdown("### 🕹️ Game History")
for player, word in st.session_state.history[::-1]:
    st.markdown(f"**{player}:** {word}")

if st.button("🔁 Restart Game"):
    st.session_state.history = []
    st.session_state.used = []
    st.experimental_rerun()
