import streamlit as st
import folium
from streamlit_folium import st_folium
import api

def show():
    st.subheader("City Safety Map")
    m = folium.Map(location=[12.9716, 77.5946], zoom_start=12)
    ok, payload = api.get_reports()
    if ok:
        reports = payload.get("reports", [])
        for report in reports:
            lat = report.get("lat")
            lng = report.get("lng")
            if lat is not None and lng is not None:
                folium.Marker(
                    [lat, lng],
                    popup=report.get("description", "Report"),
                    icon=folium.Icon(color="red")
                ).add_to(m)
    else:
        st.warning(f"Unable to load reports: {payload}")
    st_folium(m, width=None, height=500, key="main_map")
