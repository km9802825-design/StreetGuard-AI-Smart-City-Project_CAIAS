import streamlit as st
import folium
from streamlit_folium import st_folium
import api


def show():
    st.subheader("Safe Route Finder")
    default_locations = [[12.9716, 77.5946], [12.98, 77.60]]
    if "route_locations" not in st.session_state:
        st.session_state["route_locations"] = default_locations
    if "route_status" not in st.session_state:
        st.session_state["route_status"] = "Enter start and destination, then click Find route."

    col1, col2 = st.columns(2)
    with col1:
        start = st.text_input("Start location", key="route_start")
    with col2:
        end = st.text_input("Destination", key="route_end")

    if st.button("Find route", use_container_width=True):
        if not start or not end:
            st.session_state["route_status"] = "Enter both start and destination."
        else:
            ok, payload = api.get_route(start=start, end=end)
            if not ok:
                st.session_state["route_status"] = f"Request failed: {payload}"
            else:
                points = payload.get("route", [])
                if not points:
                    st.session_state["route_status"] = "No route points returned."
                else:
                    st.session_state["route_locations"] = [[p["lat"], p["lng"]] for p in points]
                    st.session_state["route_status"] = payload.get("message", "Route generated")

    status = st.session_state["route_status"]
    if "failed" in status.lower() or "enter both" in status.lower() or "no route" in status.lower():
        st.warning(status)
    else:
        st.success(status)

    locations = st.session_state["route_locations"]
    m = folium.Map(location=locations[0], zoom_start=12)
    folium.Marker(locations[0], popup="Start").add_to(m)
    folium.Marker(locations[-1], popup="Destination").add_to(m)
    folium.PolyLine(locations=locations, color="blue", weight=6).add_to(m)
    st_folium(m, width=None, height=420, key="route_map")
