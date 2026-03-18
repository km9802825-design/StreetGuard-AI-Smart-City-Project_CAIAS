import streamlit as st
import requests
import folium
from streamlit_folium import st_folium

def show():
    st.title("🗺️ City Safety Map")

    m = folium.Map(location=[12.9716, 77.5946], zoom_start=12)

    try:
        res = requests.get("http://127.0.0.1:8000/reports/")
        data = res.json()

        reports = data.get("reports", data)

        for r in reports:
            lat = r.get("lat")
            lng = r.get("lng")

            if lat and lng:
                folium.Marker(
                    [lat, lng],
                    popup=r.get("description", "Report"),
                    icon=folium.Icon(color="red")
                ).add_to(m)

    except:
        st.warning("⚠️ Backend not running or no data")

    st_folium(m, width=700, height=500, key="main_map")