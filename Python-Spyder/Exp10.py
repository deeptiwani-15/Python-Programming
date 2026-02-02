# -*- coding: utf-8 -*-
"""
Innovative Streamlit App – Mood Magic
@author: User
"""

import streamlit as st

st.set_page_config(page_title="Mood Magic App", page_icon="🎨")

# Title
st.title("🎨 Mood Magic App")
st.write("### Select your mood and see the magic ✨")

# Mood selection
mood = st.selectbox(
    "😊 How are you feeling today?",
    ["Happy", "Sad", "Excited", "Tired", "Angry"]
)

# Mood logic
if mood == "Happy":
    st.success("😊 Stay happy! Spread your smile!")
    st.balloons()

elif mood == "Sad":
    st.info("💙 It's okay to feel sad. Better days are coming 🌈")

elif mood == "Excited":
    st.markdown("### 🚀 Woohoo! Channel that energy!")
    st.snow()

elif mood == "Tired":
    st.warning("😴 Take some rest. You deserve it!")

elif mood == "Angry":
    st.error("🔥 Take a deep breath. Calm mind = strong mind.")

# Fun slider
energy = st.slider("⚡ Energy Level", 0, 100)

if energy > 70:
    st.write("💪 You are full of energy!")
elif energy > 40:
    st.write("🙂 Balanced energy level.")
else:
    st.write("🛌 Time to recharge.")

# Footer
st.markdown("---")
st.write("✨ Built with Streamlit | Simple • Creative • Interactive")
