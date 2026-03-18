import streamlit as st
import api
from components import ai_assistant, map, report_form, route_ui, sos_button

st.set_page_config(page_title="StreetGuard AI", layout="wide")

st.markdown(
    """
<style>
:root {
    --bg: #0b1220;
    --card: #111b31;
    --border: #20304f;
    --text: #f4f7ff;
    --muted: #a9b8d6;
    --primary: #2d7ff9;
}
[data-testid="stAppViewContainer"] {
    background: radial-gradient(circle at top right, #111d35, var(--bg) 55%);
    color: var(--text);
}
[data-testid="stSidebar"] {
    background: #0f1729;
    border-right: 1px solid var(--border);
}
h1, h2, h3, h4, p, label {
    color: var(--text) !important;
}
.sg-card {
    background: color-mix(in srgb, var(--card) 95%, black 5%);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 16px;
    margin-bottom: 16px;
}
.sg-kpi {
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 14px;
    background: #0f1c35;
}
.sg-kpi-label {
    color: var(--muted);
    font-size: 0.9rem;
    margin-bottom: 6px;
}
.sg-kpi-value {
    font-size: 1.5rem;
    font-weight: 700;
}
button[kind="primary"], .stButton>button {
    width: 100%;
    border-radius: 10px;
    background-color: var(--primary) !important;
    color: #fff !important;
    font-weight: bold;
}
@media (max-width: 900px) {
    .sg-kpi-value {
        font-size: 1.2rem;
    }
}
</style>
""",
    unsafe_allow_html=True,
)

st.title("StreetGuard AI")
st.caption("Real-time city safety operations")

stats_ok, stats_payload = api.get_dashboard_stats()
if stats_ok:
    c1, c2, c3, c4 = st.columns(4)
    c1.markdown(
        f"<div class='sg-kpi'><div class='sg-kpi-label'>Reports</div><div class='sg-kpi-value'>{stats_payload.get('total_reports', 0)}</div></div>",
        unsafe_allow_html=True,
    )
    c2.markdown(
        f"<div class='sg-kpi'><div class='sg-kpi-label'>SOS Alerts</div><div class='sg-kpi-value'>{stats_payload.get('total_sos', 0)}</div></div>",
        unsafe_allow_html=True,
    )
    c3.markdown(
        f"<div class='sg-kpi'><div class='sg-kpi-label'>Risk Zones</div><div class='sg-kpi-value'>{stats_payload.get('high_risk_zones', 0)}</div></div>",
        unsafe_allow_html=True,
    )
    c4.markdown(
        f"<div class='sg-kpi'><div class='sg-kpi-label'>Safety Index</div><div class='sg-kpi-value'>{stats_payload.get('safety_index', '-')}</div></div>",
        unsafe_allow_html=True,
    )
else:
    st.warning(f"Backend connection issue: {stats_payload}")

page = st.sidebar.radio("Navigate", ["SOS", "Report", "AI Assistant", "Route", "Map"], index=0)

if page == "SOS":
    st.markdown("<div class='sg-card'>", unsafe_allow_html=True)
    sos_button.show()
    st.markdown("</div>", unsafe_allow_html=True)
elif page == "Report":
    st.markdown("<div class='sg-card'>", unsafe_allow_html=True)
    report_form.show()
    st.markdown("</div>", unsafe_allow_html=True)
elif page == "AI Assistant":
    st.markdown("<div class='sg-card'>", unsafe_allow_html=True)
    ai_assistant.show()
    st.markdown("</div>", unsafe_allow_html=True)
elif page == "Route":
    st.markdown("<div class='sg-card'>", unsafe_allow_html=True)
    route_ui.show()
    st.markdown("</div>", unsafe_allow_html=True)
elif page == "Map":
    st.markdown("<div class='sg-card'>", unsafe_allow_html=True)
    map.show()
    st.markdown("</div>", unsafe_allow_html=True)
