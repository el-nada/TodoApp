import streamlit as st
from pages import auth, home, settings

# Initialize session state
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
    st.session_state.username = None

# Function to hide default menu
def hide_default_menu():
    hide_menu = """
    <style>
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
    """
    st.markdown(hide_menu, unsafe_allow_html=True)

def hide_sidebar():
    st.markdown(
        """
        <style>
            [data-testid="stSidebar"] {
                display: none;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

# Authentication check
if not st.session_state.authenticated:
    hide_default_menu()  # Hide menus
    hide_sidebar()
    auth.render()        # Show login/registration page
    st.stop()

page = st.sidebar.radio("Navigation", ["Home", "Settings"])

# Render the selected page
if page == "Home":
    home.render()
elif page == "Settings":
    settings.render()

