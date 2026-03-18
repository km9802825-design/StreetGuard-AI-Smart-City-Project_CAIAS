import streamlit as st
import folium
from streamlit_folium import st_folium
from geopy.geocoders import Nominatim
import api

def show():
    st.subheader("AI Safety Assistant")

    col1, col2 = st.columns([2, 1])
    with col1:
        user_input = st.text_input("What happened?", key="ai_input")
    with col2:
        location = st.text_input("Location", key="ai_location")

    if st.button("Get safety advice", use_container_width=True):
        if user_input:
            situation = f"{user_input} at {location}".strip()
            ok, payload = api.get_ai_advice(situation=situation)
            if ok:
                st.success("Advice")
                st.write(payload.get("advice", "No advice returned"))
            else:
                st.error(f"Request failed: {payload}")
        else:
            st.warning("Enter a situation first")

    st.markdown("---")
    st.subheader("Location Map")

    lat, lng = 12.9716, 77.5946

    if location:
        try:
            geo = Nominatim(user_agent="streetguard")
            loc = geo.geocode(location)
            if loc:
                lat, lng = loc.latitude, loc.longitude
        except Exception:
            pass

    m = folium.Map(location=[lat, lng], zoom_start=13)
    folium.Marker([lat, lng], popup=location if location else "Default Location", icon=folium.Icon(color="blue")).add_to(m)
    st_folium(m, width=None, height=420, key="ai_map_unique")
