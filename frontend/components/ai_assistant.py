import streamlit as st
import requests
import folium
from streamlit_folium import st_folium
from geopy.geocoders import Nominatim

def show():
    st.subheader("🧠 AI Safety Assistant")

    user_input = st.text_input("What did you see?", key="ai_input")
    location = st.text_input("Enter location", key="ai_location")

    if st.button("🚀 Get Advice"):
        if user_input:
            res = requests.post(
                "http://127.0.0.1:8000/ai",
                json={"situation": f"{user_input} at {location}"}
            )

            if res.status_code == 200:
                st.success("AI Advice")
                st.write(res.json()["advice"])
            else:
                st.error("Backend error")
        else:
            st.warning("Enter situation")

    # 📍 Map Section
    st.markdown("---")
    st.subheader("📍 Location Map")

    lat, lng = 12.9716, 77.5946

    if location:
        try:
            geo = Nominatim(user_agent="streetguard")
            loc = geo.geocode(location)
            if loc:
                lat, lng = loc.latitude, loc.longitude
        except:
            pass

    m = folium.Map(location=[lat, lng], zoom_start=13)

    folium.Marker(
        [lat, lng],
        popup=location if location else "Default Location",
        icon=folium.Icon(color="blue")
    ).add_to(m)

    st_folium(m, width=900, height=400, key="ai_map_unique")