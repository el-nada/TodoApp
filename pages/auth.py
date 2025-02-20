import streamlit as st
from auth.database_auth import create_user, verify_user

def render():
    st.subheader("Login / Register")
    tab1, tab2 = st.tabs(["Login", "Register"])
    
    with tab1:  # Login
        with st.form("login"):
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            if st.form_submit_button("Login"):
                if verify_user(username, password):
                    st.session_state.authenticated = True
                    st.session_state.username = username
                    st.rerun()
                else:
                    st.error("Invalid credentials")
    
    with tab2:  # Registration
        with st.form("register"):
            new_user = st.text_input("New Username")
            new_pass = st.text_input("New Password", type="password")
            if st.form_submit_button("Register"):
                if create_user(new_user, new_pass):
                    st.success("Account created! Please login")
                else:
                    st.error("Username already exists")

