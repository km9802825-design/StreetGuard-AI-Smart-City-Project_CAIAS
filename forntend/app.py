import streamlit as st
from components import ai_assistant, report_form, sos_button, route_ui, map

# 🔥 Page config
st.set_page_config(page_title="StreetGuard AI", layout="wide")

# 🎨 Custom CSS
st.markdown("""
<style>
.main {
    background-color: #0f172a;
}
h1, h2, h3 {
    color: white;
}
.stButton>button {
    width: 100%;
    border-radius: 10px;
    background-color: #2563eb;
    color: white;
    font-weight: bold;
}
.card {
    background: #1e293b;
    padding: 20px;
    border-radius: 12px;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# 🏠 Title
st.title("🚨 StreetGuard AI Dashboard")

# 📌 Sidebar
page = st.sidebar.radio(
    "📌 Navigate",
    ["🚨 SOS", "📍 Report", "🧠 AI Assistant", "🗺️ Route", "🌍 Map"]
)

# 🎯 Routing
if page == "🚨 SOS":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    sos_button.show()
    st.markdown('</div>', unsafe_allow_html=True)

elif page == "📍 Report":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    report_form.show()
    st.markdown('</div>', unsafe_allow_html=True)

elif page == "🧠 AI Assistant":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    ai_assistant.show()
    st.markdown('</div>', unsafe_allow_html=True)

elif page == "🗺️ Route":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    route_ui.show()
    st.markdown('</div>', unsafe_allow_html=True)

elif page == "🌍 Map":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    map.show()
    st.markdown('</div>', unsafe_allow_html=True)