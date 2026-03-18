import streamlit as st
import requests

def show():
    st.title("🚨 Emergency SOS")

    user = st.text_input("👤 Your Name", key="sos_user")
    location = st.text_input("📍 Your Location", key="sos_location")

    if st.button("🚨 Send SOS"):
        if user and location:
            try:
                requests.post(
                    "http://127.0.0.1:8000/emergency/",
                    json={
                        "user": user,
                        "location": location,
                        "message": "Help needed!"
                    }
                )
                st.success("🚨 SOS Sent Successfully!")
            except:
                st.error("❌ Backend not running")
        else:
            st.warning("⚠️ Fill all fields")