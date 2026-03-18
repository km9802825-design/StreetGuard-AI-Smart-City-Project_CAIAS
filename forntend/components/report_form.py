import streamlit as st
import requests

def show():
    st.title("📍 Report Issue")

    user = st.text_input("👤 Name", key="report_user")
    description = st.text_area("📝 Description", key="report_desc")
    address = st.text_input("📍 Location", key="report_loc")

    if st.button("Submit Report"):
        if user and description and address:
            try:
                requests.post(
                    "http://127.0.0.1:8000/reports/",
                    data={
                        "user": user,
                        "description": description,
                        "address": address
                    }
                )
                st.success("✅ Report submitted")
            except:
                st.error("❌ Backend not running")
        else:
            st.warning("⚠️ Fill all fields")