import streamlit as st
import folium
from streamlit_folium import st_folium

def show():
    st.title("🛣️ Safe Route Finder")

    start = st.text_input("📍 Start Location", key="route_start")
    end = st.text_input("🏁 Destination", key="route_end")

    if st.button("Find Route"):
        st.success(f"Route from {start} → {end}")

        m = folium.Map(location=[12.9716, 77.5946], zoom_start=12)

        folium.Marker([12.9716, 77.5946], popup="Start").add_to(m)
        folium.Marker([12.9760, 77.6400], popup="End").add_to(m)

        folium.PolyLine(
            locations=[
                [12.9716, 77.5946],
                [12.9730, 77.6100],
                [12.9760, 77.6400]
            ],
            color="blue"
        ).add_to(m)

        st_folium(m, width=700, height=400, key="route_map")