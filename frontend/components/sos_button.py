import streamlit as st
import api


def show():
    st.subheader("Emergency SOS")
    col1, col2 = st.columns(2)
    with col1:
        user = st.text_input("Your name", key="sos_user")
    with col2:
        location = st.text_input("Current location", key="sos_location")
    message = st.text_area("Emergency details", key="sos_message", value="Help needed!", height=120)

    if st.button("Send SOS", use_container_width=True):
        if user and location and message:
            ok, payload = api.send_sos(user=user, location=location, message=message)
            if ok:
                st.success("SOS sent successfully")
                email_info = payload.get("email", {})
                if email_info.get("sent"):
                    st.success(f"Email sent to {email_info.get('recipient')}")
                else:
                    detail = email_info.get("detail") or "Unknown reason"
                    st.warning(f"Email not sent: {detail}")
                st.json(payload)
            else:
                st.error(f"Request failed: {payload}")
        else:
            st.warning("Fill all fields")
