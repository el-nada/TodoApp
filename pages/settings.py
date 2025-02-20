import streamlit as st
from auth.database_auth import update_password

def render():
    st.title("Settings")

    with st.form("Change password"):
            new_password = st.text_input("Password", type="password")
            if st.form_submit_button("Change password"):
                update_password(st.session_state.username, new_password)
