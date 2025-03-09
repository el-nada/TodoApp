import streamlit as st
from auth.database_auth import update_password, update_username

def render():
    st.title("Settings")

    with st.form("Change password"):
        new_username = st.text_input("Username", value=f"{st.session_state.username}")
        new_password = st.text_input("Password", type="password")

        submitted = st.form_submit_button("Change settings")
        if submitted and new_username and new_password:
            if new_username=={st.session_state.username}:
                update_password(st.session_state.username, new_password)

            if update_username(st.session_state.username, new_username):
                st.session_state.username = new_username
                update_password(st.session_state.username, new_password)
                st.success("Settings changed !")
            else : 
                st.error("Username already exists")
            
        else : 
            st.error("Please fill in all the required fields before submitting.")