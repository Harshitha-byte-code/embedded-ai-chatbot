import streamlit as st
import requests

st.title("🚗 Remote Vehicle Control Panel")

FLASK_URL = "http://127.0.0.1:5001/move"

speed = st.slider("Speed", 0, 255, 100)

def send(direction):
    try:
        res = requests.post(FLASK_URL, json={
            "direction": direction,
            "speed": speed
        })
        if res.status_code == 200:
            st.success(f"Sent '{direction}' at speed {speed}")
        else:
            st.error("Command failed.")
    except Exception as e:
        st.error(f"Error: {e}")

col1, col2, col3 = st.columns(3)

with col2:
    if st.button("⬆ Forward"):
        send("forward")

col4, col5, col6 = st.columns(3)

with col4:
    if st.button("⬅ Left"):
        send("left")

with col6:
    if st.button("➡ Right"):
        send("right")

if st.button("⬇ Backward"):
    send("backward")

if st.button("🛑 STOP"):
    send("stop")
