import streamlit as st
import api


def show():
    st.subheader("Create Incident Report")
    col1, col2 = st.columns(2)
    with col1:
        user = st.text_input("Name", key="report_user")
    with col2:
        address = st.text_input("Location", key="report_loc")
    description = st.text_area("Description", key="report_desc", height=120)
    image = st.file_uploader("Attach image", type=["png", "jpg", "jpeg"])

    if st.button("Submit report", use_container_width=True):
        if user and description and address:
            ok, payload = api.create_report(
                user=user,
                description=description,
                address=address,
                image_file=image
            )
            if ok:
                st.success("Report submitted")
                st.json(payload)
            else:
                st.error(f"Request failed: {payload}")
        else:
            st.warning("Fill all required fields")
